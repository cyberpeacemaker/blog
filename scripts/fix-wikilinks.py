#!/usr/bin/env python3
"""Fix remaining MM-DD wikilinks to YYYY-MM-DD based on actual filenames."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKILINK = re.compile(r"\[\[([^\]|#]+)(#[^\]]+)?(\|[^\]]+)?\]\]")
OLD_STEM = re.compile(r"^(\d{2})-(\d{2})-(.+)$")


def build_stem_map() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or ".obsidian" in path.parts:
            continue
        stem = path.stem
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})-(.+)$", stem)
        if m:
            year, month, day, slug = m.groups()
            old = f"{month}-{day}-{slug}"
            mapping[old] = stem
            mapping[f"{path.parent.name}/{old}"] = f"{path.parent.name}/{stem}"
            # nested paths
            rel = path.relative_to(ROOT)
            old_rel = "/".join(list(rel.parts[:-1]) + [f"{month}-{day}-{slug}"])
            new_rel = rel.with_suffix("").as_posix()
            mapping[old_rel] = new_rel
    return mapping


def replace_links(text: str, stem_map: dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group(1)
        suffix = (match.group(2) or "") + (match.group(3) or "")
        if target in stem_map:
            return f"[[{stem_map[target]}{suffix}]]"
        base = Path(target).name
        parent = str(Path(target).parent)
        if parent and parent != ".":
            key = f"{parent}/{base}"
            if key in stem_map:
                return f"[[{stem_map[key]}{suffix}]]"
        if base in stem_map:
            if parent and parent != ".":
                return f"[[{parent}/{stem_map[base]}{suffix}]]"
            return f"[[{stem_map[base]}{suffix}]]"
        m = OLD_STEM.match(target)
        if m:
            return f"[[2026-{m.group(1)}-{m.group(2)}-{m.group(3)}{suffix}]]"
        m2 = OLD_STEM.match(base)
        if m2 and parent and parent != ".":
            return f"[[{parent}/2026-{m2.group(1)}-{m2.group(2)}-{m2.group(3)}{suffix}]]"
        return match.group(0)

    return WIKILINK.sub(repl, text)


def main() -> None:
    stem_map = build_stem_map()
    updated_files = 0
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or ".obsidian" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        new_text = replace_links(text, stem_map)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8", newline="\n")
            updated_files += 1
    print(f"Updated wikilinks in {updated_files} files.")


if __name__ == "__main__":
    main()
