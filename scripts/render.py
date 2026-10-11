"""Builds the Markdown pages of each wiki from templates/, history/ and wikis.json.

Usage:
    python3 scripts/render.py            # writes into the wiki clones: frames/, kuper/, blueprint/
    python3 scripts/render.py --out out  # writes to out/<lib>/ instead, to try changes
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ONLY_START = re.compile(r"\s*<!--only:([\w,]+)-->\s*$")
ONLY_END = re.compile(r"\s*<!--/only-->\s*$")


def render(text: str, lib: str, name: str) -> str:
    lines, keep = [], [True]
    for line in text.split("\n"):
        start = ONLY_START.match(line)
        if start:
            keep.append(keep[-1] and lib in start.group(1).split(","))
            continue
        if ONLY_END.match(line):
            keep.pop()
            continue
        if keep[-1]:
            lines.append(line)
    if len(keep) != 1:
        raise ValueError("unbalanced <!--only--> blocks")
    out = "\n".join(lines).replace("{{Lib}}", name).replace("{{lib}}", lib)
    if "{{" in out:
        raise ValueError(f"unknown placeholder: {re.search(r'{{[^}]*}}', out).group(0)}")
    return re.sub(r"\n{3,}", "\n\n", out).strip() + "\n"


def title(page: str) -> str:
    return page.replace("-", " ")


def relink(text: str, names: dict[str, str]) -> str:
    """Points links at a page's name in this wiki, when it differs from its template name."""
    for template, name in names.items():
        if template == name:
            continue
        link = re.compile(r"\[([^\]]*)\]\(" + re.escape(template) + r"(#[^)]*)?\)")
        text = link.sub(
            lambda m: f"[{title(name) if m.group(1) == title(template) else m.group(1)}]({name}{m.group(2) or ''})",
            text,
        )
    return text


def build(out_dir: Path, quiet: bool = False) -> None:
    config = json.loads((ROOT / "wikis.json").read_text())
    for lib, info in config["libraries"].items():
        name = info["name"]
        pages: dict[str, str] = {}

        # A page is either a list of wikis, or a map of wiki to the page's name in that wiki
        names = {
            page: wikis[lib] if isinstance(wikis, dict) else page
            for page, wikis in config["pages"].items()
            if lib in wikis
        }
        for page, page_name in names.items():
            template = (ROOT / "templates" / f"{page}.md").read_text()
            pages[page_name] = render(template, lib, name)

        intro = render((ROOT / "templates" / "_Update.md").read_text(), lib, name)
        history = (ROOT / "history" / f"{lib}.md").read_text()
        pages[f"Update-{name}"] = re.sub(r"\n{3,}", "\n\n", f"{intro}\n{history}").strip() + "\n"

        for old, new in config["moved"].get(lib, {}).items():
            links = " and ".join(f"[{title(n)}]({n})" for n in (names.get(n, n) for n in new))
            pages[old] = f"This page moved. 📦\n\nYou can now find it in {links}.\n"
        pages.update(config["custom_stubs"].get(lib, {}))

        pages = {page: relink(content, names) for page, content in pages.items()}

        target = out_dir / lib
        target.mkdir(parents=True, exist_ok=True)
        for page, content in pages.items():
            (target / f"{page}.md").write_text(content)
        for leftover in sorted(set(f.stem for f in target.glob("*.md")) - set(pages)):
            print(f"{name}: {leftover}.md isn't generated anymore. Delete it, or add it to 'moved' in wikis.json")
        if not quiet:
            print(f"{name}: {len(pages)} pages -> {target}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=ROOT)
    build(parser.parse_args().out.resolve())
