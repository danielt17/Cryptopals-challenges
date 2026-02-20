from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
MAP_PATH = Path(__file__).resolve().parent / "challenge_map.json"
STARTUP_DELAY_SECONDS = 0.6


def load_map() -> dict:
    """Load map."""
    return json.loads(MAP_PATH.read_text(encoding="utf-8"))


def challenge_dir(set_info: dict, challenge_num: int, challenge: dict) -> Path:
    """Compute challenge dir."""
    set_slug = set_info[str(challenge["set"])]["slug"]
    return (
        SRC
        / "sets"
        / f"set_{challenge['set']:02d}_{set_slug}"
        / f"challenge_{challenge_num:02d}_{challenge['slug']}"
    )


def list_challenges(payload: dict) -> None:
    """List challenges."""
    challenges = payload["challenges"]
    for num in sorted(int(n) for n in challenges.keys()):
        entry = challenges[str(num)]
        scripts = [s["file"] for s in entry.get("scripts", [])]
        if scripts:
            script_list = ", ".join(scripts)
            print(f"{num:02d}: {entry['title']} -> {script_list}")
        else:
            print(f"{num:02d}: {entry['title']} -> (no implementation)")


def build_env() -> dict:
    """Build env."""
    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = str(SRC) + (os.pathsep + existing if existing else "")
    return env


def script_path_for(challenge_num: int, challenge: dict, set_info: dict, script_file: str) -> Path:
    """Compute script path."""
    base = challenge_dir(set_info, challenge_num, challenge)
    return base / script_file


def default_run_sequence(challenge: dict) -> list[dict]:
    """Run default sequence."""
    scripts = [s["file"] for s in challenge.get("scripts", []) if s.get("run")]
    return [{"action": "run", "scripts": [script]} for script in scripts]


def run_sequence(challenge_num: int, challenge: dict, set_info: dict, sequence: list[dict]) -> int:
    """Run sequence."""
    env = build_env()
    started: list[subprocess.Popen] = []
    try:
        for step in sequence:
            action = step["action"]
            scripts = step["scripts"]
            if action == "start":
                for script in scripts:
                    path = script_path_for(challenge_num, challenge, set_info, script)
                    if not path.exists():
                        print(f"Missing script: {path}")
                        return 3
                    proc = subprocess.Popen([sys.executable, str(path)], cwd=ROOT, env=env)
                    started.append(proc)
                time.sleep(STARTUP_DELAY_SECONDS)
            elif action == "run":
                for script in scripts:
                    path = script_path_for(challenge_num, challenge, set_info, script)
                    if not path.exists():
                        print(f"Missing script: {path}")
                        return 3
                    result = subprocess.run([sys.executable, str(path)], cwd=ROOT, env=env)
                    if result.returncode != 0:
                        return result.returncode
            else:
                print(f"Unknown action: {action}")
                return 2
        return 0
    finally:
        for proc in started:
            if proc.poll() is None:
                proc.terminate()
        for proc in started:
            try:
                proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                proc.kill()


def main() -> int:
    """Run the script entry point."""
    parser = argparse.ArgumentParser(
        description="Run a Cryptopals challenge by number.",
    )
    parser.add_argument("challenge", nargs="?", type=int, help="Challenge number (1-66)")
    parser.add_argument("--list", action="store_true", help="List challenges and exit")
    parser.add_argument(
        "--script",
        help="Run a single script for a challenge (overrides the default run sequence).",
    )
    args = parser.parse_args()

    payload = load_map()
    challenges = payload["challenges"]
    set_info = payload["set_info"]

    if args.list:
        list_challenges(payload)
        return 0

    if args.challenge is None:
        parser.error("challenge is required unless --list is used")

    entry = challenges.get(str(args.challenge))
    if entry is None:
        print(f"Unknown challenge: {args.challenge}")
        return 1

    scripts = entry.get("scripts", [])
    if not scripts:
        print(f"No implementation in this repo for challenge {args.challenge}")
        return 1

    if args.script:
        script_name = args.script if args.script.endswith(".py") else f"{args.script}.py"
        allowed = [s["file"] for s in scripts]
        if script_name not in allowed:
            print(f"Script '{script_name}' is not valid for challenge {args.challenge}")
            print(f"Valid scripts: {', '.join(allowed)}")
            return 2
        env = build_env()
        path = script_path_for(args.challenge, entry, set_info, script_name)
        if not path.exists():
            print(f"Missing script: {path}")
            return 3
        result = subprocess.run([sys.executable, str(path)], cwd=ROOT, env=env)
        return result.returncode

    sequence = entry.get("run_sequence") or default_run_sequence(entry)
    return run_sequence(args.challenge, entry, set_info, sequence)


if __name__ == "__main__":
    raise SystemExit(main())
