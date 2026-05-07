#!/usr/bin/env python3
"""
Synchronizes external/ submodules with registry/skills.yaml configuration.

Actions:
1. Reads skills.yaml to get all enabled sources with pinned commits
2. Adds new submodules if they don't exist
3. Removes old submodules if they're no longer in config or not trusted/reviewed
4. Updates all submodules to the correct pinned commit
5. Cleans up empty indexes/ directory if no longer needed
6. Verifies all submodules are at correct commit after sync
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from registry_lib import ROOT, load_all


def run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> str:
    """Run a command and return stdout."""
    result = subprocess.run(
        cmd,
        cwd=cwd or ROOT,
        capture_output=True,
        text=True,
        check=check,
    )
    return result.stdout.strip()


def get_gitmodules() -> dict[str, dict[str, str]]:
    """Parse .gitmodules and return submodule info."""
    gitmodules_path = ROOT / ".gitmodules"
    if not gitmodules_path.exists():
        return {}
    
    content = gitmodules_path.read_text()
    modules: dict[str, dict[str, str]] = {}
    current_section = None
    
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("[submodule "):
            current_section = line[12:-1].strip('"')
            modules[current_section] = {}
        elif "=" in line and current_section:
            key, value = line.split("=", 1)
            modules[current_section][key.strip()] = value.strip()
    
    return modules


def get_current_submodules() -> dict[str, str]:
    """Get current submodule state: path -> commit hash."""
    try:
        output = run(["git", "submodule", "status"])
    except subprocess.CalledProcessError:
        return {}
    
    status: dict[str, str] = {}
    for line in output.splitlines():
        parts = line.strip().split()
        if len(parts) >= 2:
            commit = parts[0]
            path = parts[1]
            status[path] = commit
    return status


def add_submodule(url: str, path: str, commit: str) -> bool:
    """Add a new submodule at the specified path and checkout the commit."""
    print(f"  Adding submodule: {path}")
    try:
        # Clone non-recursively first
        run(["git", "submodule", "add", "--force", url, path], check=True)
        # Checkout the specific commit
        run(["git", "checkout", commit], cwd=ROOT / path, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  Warning: Failed to add submodule {path}: {e}")
        return False


def remove_submodule(path: str) -> bool:
    """Remove a submodule completely."""
    print(f"  Removing submodule: {path}")
    try:
        # Deinit first
        run(["git", "submodule", "deinit", "-f", path], check=True)
        # Remove from index
        run(["git", "rm", "-f", path], check=True)
        # Remove .git/modules
        git_module_path = ROOT / ".git" / "modules" / path
        if git_module_path.exists():
            shutil.rmtree(git_module_path)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  Warning: Failed to remove submodule {path}: {e}")
        return False


def update_submodule(path: str, expected_commit: str) -> bool:
    """Update submodule to the expected commit."""
    try:
        # Get current commit
        current = run(["git", "rev-parse", "HEAD"], cwd=ROOT / path)
        if current == expected_commit:
            print(f"  {path}: already at {expected_commit[:8]}")
            return True
        
        print(f"  {path}: updating from {current[:8]} to {expected_commit[:8]}")
        run(["git", "fetch", "--recurse-submodules", "--all"], cwd=ROOT / path, check=True)
        run(["git", "checkout", expected_commit], cwd=ROOT / path, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  Warning: Failed to update submodule {path}: {e}")
        return False


def sync_submodules(registry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Synchronize external/ submodules with registry config.
    
    Returns dict of expected submodules: path -> {url, commit, id}
    """
    allowed_trust = {"trusted", "reviewed"}
    
    # Get sources that should exist
    should_exist: dict[str, dict[str, Any]] = {}
    for item in registry["skills"]:
        trust_level = item.get("trust", {}).get("level", "unknown")
        if trust_level not in allowed_trust:
            continue
        if not item.get("enabled"):
            continue
        
        source = item.get("source", {})
        external_path = source.get("external_path")
        if not external_path:
            continue
        
        commit = item.get("version", {}).get("commit")
        repo_url = source.get("repo")
        
        if commit and repo_url:
            should_exist[external_path] = {
                "url": repo_url,
                "commit": commit,
                "id": item["id"],
            }
    
    # Get current state
    current_gitmodules = get_gitmodules()
    current_submodules = get_current_submodules()
    
    # Determine what to add, remove, and update
    to_add = set(should_exist.keys()) - set(current_gitmodules.keys())
    to_remove = set(current_gitmodules.keys()) - set(should_exist.keys())
    to_update = set(should_exist.keys()) & set(current_gitmodules.keys())
    
    # Handle removals first
    if to_remove:
        print(f"\nRemoving old submodules ({len(to_remove)}):")
        for path in sorted(to_remove):
            remove_submodule(path)
    
    # Handle additions
    if to_add:
        print(f"\nAdding new submodules ({len(to_add)}):")
        for path in sorted(to_add):
            info = should_exist[path]
            add_submodule(info["url"], path, info["commit"])
    
    # Handle updates
    if to_update:
        print(f"\nUpdating submodules ({len(to_update)}):")
        for path in sorted(to_update):
            info = should_exist[path]
            update_submodule(path, info["commit"])
    
    # Clean up indexes/ directory if empty or not needed
    indexes_path = ROOT / "external" / "indexes"
    if indexes_path.exists():
        try:
            if not any(indexes_path.iterdir()):
                print(f"\nRemoving empty indexes directory")
                shutil.rmtree(indexes_path)
                # Also remove from gitmodules if present
                run(["git", "rm", "-f", "external/indexes"], check=False)
        except OSError:
            pass
    
    return should_exist


def verify_submodules(expected: dict[str, dict[str, Any]]) -> bool:
    """Verify all submodules are at the correct commit."""
    print("\nVerifying submodule commits:")
    all_ok = True
    
    for path, info in sorted(expected.items()):
        expected_commit = info["commit"]
        submodule_path = ROOT / path
        
        if not submodule_path.exists():
            print(f"  {path}: MISSING")
            all_ok = False
            continue
        
        try:
            current = run(["git", "rev-parse", "HEAD"], cwd=submodule_path)
            if current == expected_commit:
                print(f"  {path}: {expected_commit[:8]} OK")
            else:
                print(f"  {path}: MISMATCH (expected {expected_commit[:8]}, got {current[:8]})")
                all_ok = False
        except subprocess.CalledProcessError:
            print(f"  {path}: ERROR reading commit")
            all_ok = False
    
    return all_ok


def main() -> int:
    print("Synchronizing external submodules with registry/skills.yaml...\n")
    
    # Load registry
    registry = load_all()
    
    # Sync submodules
    expected = sync_submodules(registry)
    
    # Verify
    all_ok = verify_submodules(expected)
    
    if all_ok:
        print("\n✓ All submodules at correct commits")
    else:
        print("\n✗ Some submodules have issues - run bootstrap again to fix")
        return 1
    
    print("\nSync complete!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
