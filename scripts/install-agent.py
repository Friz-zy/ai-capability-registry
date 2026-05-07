#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
GENERATED = ROOT / "generated"
ACTIVE_ROOT = GENERATED / "active"
CONFIG_ROOT = GENERATED / "configs"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def run_git_head(path: Path) -> str:
    result = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"], check=True, capture_output=True, text=True)
    return result.stdout.strip()


def verify_pins() -> None:
    pins = load_json(GENERATED / "install-bundle.json")["source_pins"]
    errors: list[str] = []
    for pin in pins:
        if not pin.get("enabled"):
            continue
        expected = pin.get("expected_commit")
        source_path = ROOT / pin["external_path"]
        if not expected:
            errors.append(f"{pin['id']}: enabled source has no expected commit")
            continue
        if not source_path.exists():
            errors.append(f"{pin['id']}: missing source path {pin['external_path']}")
            continue
        try:
            actual = run_git_head(source_path)
        except subprocess.CalledProcessError:
            errors.append(f"{pin['id']}: cannot read git HEAD in {pin['external_path']}")
            continue
        if actual != expected:
            errors.append(f"{pin['id']}: expected {expected}, got {actual}")
    if errors:
        details = "\n".join(f"- {error}" for error in errors)
        raise SystemExit(f"Pin verification failed:\n{details}")


def resolve_target(path: str) -> Path:
    target = Path(path).expanduser().resolve()
    active = ACTIVE_ROOT.resolve()
    if not target.is_relative_to(active):
        raise ValueError(f"Refusing to write outside repo-local active cache: {path}")
    return target


def copy_tree(source: Path, target: Path, dry_run: bool) -> None:
    if dry_run:
        print(f"DRY-RUN copy {source} -> {target}")
        return
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, symlinks=True, ignore=shutil.ignore_patterns(".git", "node_modules", "__pycache__"))


def write_json(path: Path, data: Any, dry_run: bool) -> None:
    if dry_run:
        print(f"DRY-RUN write {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def install_payload(agent_id: str, profile: str, dry_run: bool) -> dict[str, Any]:
    bundle = load_json(GENERATED / "install-bundle.json")
    try:
        manifest = bundle["profiles"][profile]["agents"][agent_id]["manifest"]
    except KeyError as exc:
        raise SystemExit(f"Unknown agent/profile combination: {agent_id}/{profile}") from exc
    active_root = Path(manifest["active_root"])
    if active_root.exists() and not dry_run:
        shutil.rmtree(active_root)
    for item in manifest.get("capabilities", []):
        copy_tree(ROOT / item["source"], resolve_target(item["target"]), dry_run)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Install a generated profile into the repo-local active cache.")
    parser.add_argument("agent_id")
    parser.add_argument("--profile", default="core")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-pin-check", action="store_true", help="Do not use except for local debugging.")
    args = parser.parse_args()

    if not args.skip_pin_check:
        verify_pins()
    manifest = install_payload(args.agent_id, args.profile, args.dry_run)
    bundle = load_json(GENERATED / "install-bundle.json")
    config = bundle["profiles"][args.profile]["agents"][args.agent_id]["config"]
    role_instruction = bundle["profiles"][args.profile]["role_instruction"]
    write_json(CONFIG_ROOT / args.agent_id / f"{args.profile}.json", config, args.dry_run)
    if args.dry_run:
        print(f"DRY-RUN write {CONFIG_ROOT / args.agent_id / (args.profile + '.md')}")
    else:
        role_path = CONFIG_ROOT / args.agent_id / f"{args.profile}.md"
        role_path.parent.mkdir(parents=True, exist_ok=True)
        role_path.write_text(role_instruction.rstrip() + "\n", encoding="utf-8")

    print(f"Installed {len(manifest.get('capabilities', []))} capabilities for {args.agent_id} profile {args.profile}")
    print(f"Active cache: {manifest['active_root']}")
    print(f"Config snippet: {CONFIG_ROOT / args.agent_id / (args.profile + '.json')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
