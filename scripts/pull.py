"""Clones the wiki repos that are missing, and pulls the latest changes into the ones that exist.

Usage:
    python3 scripts/pull.py              # all wikis
    python3 scripts/pull.py frames kuper # only these
    python3 scripts/pull.py --https      # clone with HTTPS instead of SSH
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def git(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, text=True, capture_output=True)


def pull(lib: str, wiki: str, https: bool) -> bool:
    folder = ROOT / lib
    if not folder.exists():
        url = f"https://github.com/{wiki}.git" if https else f"git@github.com:{wiki}.git"
        result = git("clone", url, lib)
        print(f"{lib}: cloned from {url}" if result.returncode == 0 else f"{lib}: clone failed\n{result.stderr}")
        return result.returncode == 0

    if not (folder / ".git").exists():
        print(f"{lib}: the folder exists but isn't a Git repo. Move or delete it, then run this again.")
        return False

    # --ff-only so a wiki edited on GitHub never gets merged silently with local changes
    result = git("pull", "--ff-only", cwd=folder)
    if result.returncode != 0:
        print(f"{lib}: pull failed. Check `git -C {lib} status`.\n{result.stderr}")
        return False
    print(f"{lib}: {result.stdout.strip().splitlines()[-1] if result.stdout.strip() else 'up to date'}")
    return True


if __name__ == "__main__":
    config = json.loads((ROOT / "wikis.json").read_text())["libraries"]
    parser = argparse.ArgumentParser()
    parser.add_argument("libs", nargs="*", help=", ".join(config))
    parser.add_argument("--https", action="store_true")
    args = parser.parse_args()
    if unknown := set(args.libs) - set(config):
        parser.error(f"unknown wiki: {', '.join(sorted(unknown))}")
    results = [pull(lib, config[lib]["wiki"], args.https) for lib in args.libs or config]
    sys.exit(0 if all(results) else 1)
