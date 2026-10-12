"""Checks the rendered wikis for broken links and style rule violations.

Run scripts/render.py first. Exits with 1 if anything is found.

Usage:
    python3 scripts/check.py                       # checks frames/, kuper/ and blueprint/
    python3 scripts/check.py --samples ../samples  # also checks that file paths exist in the
                                                   # sample projects (<dir>/Frames, <dir>/Kuper, ...)
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
# Word boundaries so "Dropbox" and "dropdown" don't count
DROP = re.compile(r"\bdrop(s|ped|ping)?\b", re.I)
OLD_NOTE = re.compile(r"> \*\*(Note|Tip|New to|Why|Need a hand|⚠️)")
UK_SPELLINGS = ["colour", "customis", "behaviour", "optimis", "licence", "favourite", "organis"]
# Paths in examples that don't exist in the samples on purpose
EXAMPLE_PATH = re.compile(r"yourname|assets/(folder|wallpaper\.jpg|wallpapers\.json)|drawable-nodpi$")


def anchors(markdown: str) -> set[str]:
    return {
        re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")
        for heading in re.findall(r"^#+ (.*)$", markdown, re.M)
    }


def check(out_dir: Path, samples: Path | None) -> list[str]:
    config = json.loads((ROOT / "wikis.json").read_text())
    problems = []
    for lib, info in config["libraries"].items():
        files = {f.stem: f.read_text() for f in (out_dir / lib).glob("*.md")}
        for page, text in files.items():
            where = f"{lib}/{page}.md"
            prose = re.sub(r"```.*?```", "", text, flags=re.S)

            for target, anchor in re.findall(r"\]\(([^)#\s]*)(?:#([^)\s]+))?\)", text):
                if "://" in target or target.startswith("mailto:"):
                    continue
                linked = files.get(target or page)
                if linked is None:
                    problems.append(f"{where}: link to missing page '{target}'")
                elif anchor and anchor not in anchors(linked):
                    problems.append(f"{where}: link to missing section '{target}#{anchor}'")

            for number, line in enumerate(text.split("\n"), 1):
                if len(EMOJI.findall(line)) > 1:
                    problems.append(f"{where}:{number}: more than one emoji in a line")
            lines = text.split("\n")
            for number, line in enumerate(lines, 1):
                # A bold line right after "> [!TYPE]" is an alert's title, which is fine
                is_alert_title = number > 1 and lines[number - 2].startswith("> [!")
                if OLD_NOTE.match(line) and not is_alert_title:
                    problems.append(f"{where}:{number}: old note format, use a GitHub alert like > [!NOTE]")
            if re.search(r"^## Common problems\n\n\*\*", text, re.M):
                problems.append(f"{where}: 'Common problems' should be a list, like in Set-Package-Name")
            if "—" in text or "–" in prose:
                problems.append(f"{where}: em or en dash")
            if DROP.search(prose):
                problems.append(f"{where}: 'drop' as a verb, say what actually happens")
            for spelling in UK_SPELLINGS:
                if spelling in prose.lower():
                    problems.append(f"{where}: UK spelling '{spelling}', use USA spelling")

            if samples and not page.startswith("Update-"):
                sample = samples / info["name"]
                for path in set(re.findall(r"`((?:app|buildSrc)/[\w./\-]+)`", text)):
                    if EXAMPLE_PATH.search(path):
                        continue
                    real = path.replace("com/yourname/yourapp", f"dev/jahir/{lib}/app").rstrip("/")
                    if not (sample / real).exists():
                        problems.append(f"{where}: '{path}' doesn't exist in the {info['name']} sample")
    return problems


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=ROOT)
    parser.add_argument("--samples", type=Path)
    args = parser.parse_args()
    found = check(args.out.resolve(), args.samples.resolve() if args.samples else None)
    print("\n".join(found) or "No problems found.")
    sys.exit(1 if found else 0)
