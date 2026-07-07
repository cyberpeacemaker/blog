#!/usr/bin/env python3
"""Replace [[2026-MM-DD-slug]] wikilinks with [[slug]] using on-disk filenames."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATED_TOPIC = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(#[^\]]+)?(\|[^\]]+)?\]\]")


def build_map() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or ".obsidian" in path.parts:
            continue
        m = DATED_TOPIC.match(path.name)
        if not m:
            continue
        old_stem = path.stem
        slug = m.group(4)
        new_path = path.with_name(f"{slug}.md")
        if new_path.exists():
            mapping[old_stem] = slug
            rel_old = path.relative_to(ROOT).with_suffix("").as_posix()
            rel_new = new_path.relative_to(ROOT).with_suffix("").as_posix()
            mapping[rel_old] = rel_new
    # Also map dated -> semantic for files already renamed (scan semantic files)
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or ".obsidian" in path.parts:
            continue
        if DATED_TOPIC.match(path.name):
            continue
        stem = path.stem
        # reverse: any dated link target that ends with -stem might map to stem
        mapping.setdefault(stem, stem)
    return mapping


def replace_all(text: str, mapping: dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group(1)
        suffix = (match.group(2) or "") + (match.group(3) or "")
        if target in mapping:
            return f"[[{mapping[target]}{suffix}]]"
        stem = Path(target).stem
        if stem in mapping:
            parent = str(Path(target).parent)
            if parent and parent != ".":
                return f"[[{parent}/{mapping[stem]}{suffix}]]"
            return f"[[{mapping[stem]}{suffix}]]"
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})-(.+)$", stem)
        if m:
            slug = m.group(4)
            return f"[[{slug}{suffix}]]"
        return match.group(0)

    return WIKILINK.sub(repl, text)


def main() -> None:
    mapping = build_map()
    updated = 0
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or ".obsidian" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        new_text = replace_all(text, mapping)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8", newline="\n")
            updated += 1
    print(f"Fixed wikilinks in {updated} files.")


if __name__ == "__main__":
    main()
