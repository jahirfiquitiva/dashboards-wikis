"""Commits and pushes the generated pages of each wiki that changed.

Runs check.py first and stops if it finds problems. Shows what changed in each wiki and asks
before committing and pushing.

Usage:
    python3 scripts/push.py                       # all wikis
    python3 scripts/push.py blueprint             # only this one
    python3 scripts/push.py -m "docs: fix typos"  # custom commit message
    python3 scripts/push.py --dry-run             # only show what would be committed
    python3 scripts/push.py --yes                 # don't ask before pushing
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def git(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, text=True, capture_output=True)


def default_message() -> str:
    head = git("rev-parse", "--short", "HEAD")
    if head.returncode != 0:
        return "docs: update wiki"
    dirty = git("status", "--porcelain", "--", "templates", "history", "wikis.json").stdout.strip()
    if dirty:
        print("Warning: this repo has uncommitted changes, so the commit message can't point to them.\n")
    return f"docs: update wiki from dashboards-wikis@{head.stdout.strip()}"


def unpushed_commits(folder: Path) -> int:
    result = git("rev-list", "--count", "@{u}..HEAD", cwd=folder)
    return int(result.stdout.strip()) if result.returncode == 0 else 0


def push(lib: str, message: str, dry_run: bool, ask: bool) -> bool:
    folder = ROOT / lib
    if not (folder / ".git").exists():
        print(f"{lib}: not cloned yet. Run `python3 scripts/pull.py {lib}` first.")
        return False

    changes = git("status", "--short", cwd=folder).stdout.rstrip()
    pending = unpushed_commits(folder)
    if not changes and not pending:
        print(f"{lib}: nothing to push")
        return True

    print(f"{lib}:")
    if changes:
        print(changes)
    if pending:
        print(f"  plus {pending} commit(s) not pushed yet")
    if dry_run:
        return True
    if ask and input(f"Commit and push {lib}? [y/N] ").strip().lower() != "y":
        print(f"{lib}: skipped")
        return True

    if changes:
        git("add", "-A", cwd=folder)
        commit = git("commit", "-m", message, cwd=folder)
        if commit.returncode != 0:
            print(f"{lib}: commit failed\n{commit.stderr or commit.stdout}")
            return False
    result = git("push", cwd=folder)
    if result.returncode != 0:
        print(f"{lib}: push failed. If the wiki changed on GitHub, run `python3 scripts/pull.py {lib}` first.\n{result.stderr}")
        return False
    print(f"{lib}: pushed")
    return True


if __name__ == "__main__":
    config = json.loads((ROOT / "wikis.json").read_text())["libraries"]
    parser = argparse.ArgumentParser()
    parser.add_argument("libs", nargs="*", help=", ".join(config))
    parser.add_argument("-m", "--message")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--yes", action="store_true")
    args = parser.parse_args()
    if unknown := set(args.libs) - set(config):
        parser.error(f"unknown wiki: {', '.join(sorted(unknown))}")

    if subprocess.run([sys.executable, str(ROOT / "scripts" / "check.py")]).returncode != 0:
        print("\nFix the problems above before pushing.")
        sys.exit(1)
    print()

    message = args.message or default_message()
    results = [push(lib, message, args.dry_run, not args.yes) for lib in args.libs or config]
    sys.exit(0 if all(results) else 1)
