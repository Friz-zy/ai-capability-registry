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


def verify_pins(bundle: dict[str, Any]) -> None:
    pins = bundle["source_pins"]
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


def install_payload(bundle: dict[str, Any], agent_id: str, profile: str, dry_run: bool) -> dict[str, Any]:
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


def requested_profiles(bundle: dict[str, Any], raw_profiles: list[list[str]] | None, all_profiles: bool) -> list[str]:
    available = bundle["profiles"]
    if all_profiles:
        return sorted(available)

    profiles: list[str] = []
    for group in raw_profiles or []:
        for value in group:
            profiles.extend(item.strip() for item in value.split(",") if item.strip())

    if not profiles:
        profiles = [
            profile_id
            for profile_id, profile_bundle in available.items()
            if profile_bundle.get("profile", {}).get("default")
        ]
        if not profiles:
            profiles = [next(iter(available))]

    unknown = [profile for profile in profiles if profile not in available]
    if unknown:
        known = ", ".join(sorted(available))
        raise SystemExit(f"Unknown profile(s): {', '.join(unknown)}\nKnown profiles: {known}")
    return list(dict.fromkeys(profiles))


def main() -> int:
    parser = argparse.ArgumentParser(description="Install generated profiles into the repo-local active cache.")
    parser.add_argument("agent_id")
    parser.add_argument(
        "--profile",
        dest="profiles",
        action="append",
        nargs="+",
        help="Profile(s) to install. May be repeated, space-separated, or comma-separated.",
    )
    parser.add_argument("--all-profiles", action="store_true", help="Install every generated profile for this agent.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-pin-check", action="store_true", help="Do not use except for local debugging.")
    args = parser.parse_args()

    bundle = load_json(GENERATED / "install-bundle.json")
    profiles = requested_profiles(bundle, args.profiles, args.all_profiles)

    if not args.skip_pin_check:
        verify_pins(bundle)

    total = 0
    for profile in profiles:
        manifest = install_payload(bundle, args.agent_id, profile, args.dry_run)
        config = bundle["profiles"][profile]["agents"][args.agent_id]["config"]
        role_instruction = bundle["profiles"][profile]["role_instruction"]
        write_json(CONFIG_ROOT / args.agent_id / f"{profile}.json", config, args.dry_run)
        role_path = CONFIG_ROOT / args.agent_id / f"{profile}.md"
        if args.dry_run:
            print(f"DRY-RUN write {role_path}")
        else:
            role_path.parent.mkdir(parents=True, exist_ok=True)
            role_path.write_text(role_instruction.rstrip() + "\n", encoding="utf-8")

        count = len(manifest.get("capabilities", []))
        total += count
        print(f"Installed {count} capabilities for {args.agent_id} profile {profile}")
        print(f"Active cache: {manifest['active_root']}")
        print(f"Config snippet: {CONFIG_ROOT / args.agent_id / (profile + '.json')}")

    print(f"Installed {len(profiles)} profile(s), {total} total capabilities for {args.agent_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
