"""Previews one wiki locally with Gollum, including changes that aren't committed anywhere.

Gollum only shows committed pages, so this renders the wiki into out/<lib>, a throwaway Git repo
ignored by this one, commits everything there, and serves it. The wiki clones in frames/, kuper/
and blueprint/ aren't touched.

Needs Gollum: `gem install gollum`.

Usage:
    python3 scripts/preview.py frames           # render once and serve
    python3 scripts/preview.py frames --watch   # also re-render when templates/, history/ or
                                                # wikis.json change. Refresh the browser to see it
    python3 scripts/preview.py frames --port 4000
"""
import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

from check import check
from render import build

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out"
SOURCES = [ROOT / "templates", ROOT / "history", ROOT / "wikis.json"]
BRANCH = "master"


def git(*args: str, cwd: Path) -> subprocess.CompletedProcess:
    # A fixed identity and no signing: these commits never leave out/, so they don't need a
    # global Git config or a signing prompt on every refresh
    config = ["-c", "user.name=preview", "-c", "user.email=preview@localhost", "-c", "commit.gpgsign=false"]
    return subprocess.run(["git", *config, *args], cwd=cwd, text=True, capture_output=True)


def refresh(lib: str) -> None:
    folder = OUT / lib
    # Delete the old pages first, so pages removed from wikis.json disappear from the preview too
    for page in folder.glob("*.md"):
        page.unlink()
    build(OUT, quiet=True)

    # out/ is inside this repo, so without its own .git every command below would run on this repo
    if not (folder / ".git").exists() and git("init", "-q", "-b", BRANCH, cwd=folder).returncode != 0:
        sys.exit(f"Couldn't create the preview repo in {folder}")
    git("add", "-A", cwd=folder)
    if git("diff", "--cached", "--quiet", cwd=folder).returncode != 0:
        commit = git("commit", "-q", "-m", "preview", cwd=folder)
        if commit.returncode != 0:
            sys.exit(f"Couldn't commit the preview in {folder}:\n{commit.stderr}")

    problems = [problem for problem in check(OUT, None) if problem.startswith(f"{lib}/")]
    status = f"{len(problems)} problem(s) found by check.py" if problems else "no problems"
    print(f"[{time.strftime('%H:%M:%S')}] {lib} rendered, {status}")
    for problem in problems:
        print(f"  {problem}")


def find_gollum() -> str | None:
    if found := shutil.which("gollum"):
        return found
    # Homebrew's Ruby installs gem commands in a folder that isn't on PATH by default
    if shutil.which("ruby"):
        bindir = subprocess.run(["ruby", "-e", "print Gem.bindir"], text=True, capture_output=True).stdout
        if bindir and (candidate := Path(bindir) / "gollum").exists():
            return str(candidate)
    return None


def last_change() -> float:
    files = [path for source in SOURCES for path in ([source] if source.is_file() else source.rglob("*"))]
    return max(path.stat().st_mtime for path in files)


if __name__ == "__main__":
    libs = json.loads((ROOT / "wikis.json").read_text())["libraries"]
    parser = argparse.ArgumentParser()
    parser.add_argument("lib", choices=list(libs))
    parser.add_argument("--watch", action="store_true")
    parser.add_argument("--port", type=int, default=4567)
    args = parser.parse_args()

    if not (gollum := find_gollum()):
        sys.exit("Gollum isn't installed. Install it with `gem install gollum`, then run this again.")

    refresh(args.lib)
    server = subprocess.Popen(
        [gollum, str(OUT / args.lib), "--ref", BRANCH, "--port", str(args.port)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print(f"Previewing {libs[args.lib]['name']} at http://localhost:{args.port}. Press Ctrl+C to stop.")

    try:
        seen = last_change()
        while server.poll() is None:
            time.sleep(1)
            if args.watch and (changed := last_change()) > seen:
                seen = changed
                refresh(args.lib)
        sys.exit(f"Gollum stopped (exit code {server.returncode}). Run `gollum {OUT / args.lib}` to see why.")
    except KeyboardInterrupt:
        server.terminate()
        server.wait()
