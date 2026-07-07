#!/usr/bin/env python3
"""Rename YYYY-MM-DD-slug.md -> slug.md for topic notes; keep daily YYYY-MM-DD.md."""
from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATED_TOPIC = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")
DATED_DAILY = re.compile(r"^(\d{4})-(\d{2})-(\d{2})\.md$")

SKIP_NAMES = {
    "Home.md",
    "My Stack.md",
    "Daily Workflow.md",
    "Tag Taxonomy.md",
    "daily-note.md",
    "Uncategorized.md",
}

SKIP_PREFIXES = ("MOC - ",)

HUB_NAMES = {
    "05-Software-Engineering.md",
    "06-Design-Creative.md",
    "07-Productivity-Work.md",
    "08-Career-Presentations.md",
    "09-Personal.md",
}

# Slug collisions resolved with distinct semantic names
TARGET_OVERRIDES: dict[str, str] = {
    "03-AI-Agents/2026-05-21-ai-workflow.md": "ai-workflow.md",
    "03-AI-Agents/2026-05-22-ai-workflow.md": "ai-workflow-v2.md",
    "03-AI-Agents/Harness-DevSecOps/2026-06-10-harness.md": "harness.md",
    "03-AI-Agents/Harness-DevSecOps/2026-06-11-harness.md": "harness-v2.md",
    "04-Dev-Environment/Python/2026-05-20-python-venv.md": "python-venv.md",
    "04-Dev-Environment/Python/2026-05-21-python-venv.md": "python-venv-v2.md",
    "04-Dev-Environment/VS-Code/2026-05-20-vscode-tips.md": "vscode-tips.md",
    "04-Dev-Environment/VS-Code/2026-05-22-vscode-tips.md": "vscode-tips-v2.md",
}

WIKILINK = re.compile(r"\[\[([^\]|#]+)(#[^\]]+)?(\|[^\]]+)?\]\]")


def target_name(rel_posix: str, old_name: str) -> str | None:
    if rel_posix in TARGET_OVERRIDES:
        return TARGET_OVERRIDES[rel_posix]
    if DATED_DAILY.match(old_name):
        return None
    m = DATED_TOPIC.match(old_name)
    if not m:
        return None
    if old_name in SKIP_NAMES or old_name in HUB_NAMES:
        return None
    if any(old_name.startswith(p) for p in SKIP_PREFIXES):
        return None
    return f"{m.group(4)}.md"


def collect_renames() -> list[tuple[Path, Path]]:
    renames: list[tuple[Path, Path]] = []
    seen_targets: dict[Path, str] = {}
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if ".git" in rel.parts or ".obsidian" in rel.parts:
            continue
        rel_posix = rel.as_posix()
        new_name = target_name(rel_posix, path.name)
        if not new_name or new_name == path.name:
            continue
        dst = path.with_name(new_name)
        if dst.exists() and dst != path:
            raise RuntimeError(f"Target exists: {dst}")
        if dst in seen_targets:
            raise RuntimeError(f"Duplicate target {dst} from {seen_targets[dst]} and {rel_posix}")
        seen_targets[dst] = rel_posix
        renames.append((path, dst))
    renames.sort(key=lambda x: len(x[0].as_posix()), reverse=True)
    return renames


def git_mv(src: Path, dst: Path) -> None:
    subprocess.run(
        ["git", "mv", src.as_posix(), dst.as_posix()],
        cwd=ROOT,
        check=True,
    )


def build_link_map(renames: list[tuple[Path, Path]]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for src, dst in renames:
        old_stem = src.stem
        new_stem = dst.stem
        mapping[old_stem] = new_stem
        mapping[src.name] = dst.name
        old_rel = src.relative_to(ROOT).with_suffix("").as_posix()
        new_rel = dst.relative_to(ROOT).with_suffix("").as_posix()
        mapping[old_rel] = new_rel
        mapping[f"{src.parent.name}/{old_stem}"] = f"{dst.parent.name}/{new_stem}"
    return mapping


def replace_wikilinks(text: str, link_map: dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group(1)
        suffix = (match.group(2) or "") + (match.group(3) or "")
        if target in link_map:
            return f"[[{link_map[target]}{suffix}]]"
        base = Path(target).name
        parent = str(Path(target).parent)
        if base.endswith(".md"):
            base = base[:-3]
        stem = Path(target).stem
        for key in (target, stem, base, f"{parent}/{stem}" if parent != "." else stem):
            if key in link_map:
                return f"[[{link_map[key]}{suffix}]]"
        return match.group(0)

    return WIKILINK.sub(repl, text)


def main() -> None:
    os.chdir(ROOT)
    renames = collect_renames()
    print(f"Renaming {len(renames)} topic notes to semantic slugs...")
    for src, dst in renames:
        print(f"  {src.relative_to(ROOT)} -> {dst.name}")
        git_mv(src, dst)

    link_map = build_link_map(renames)
    md_files = [
        p
        for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and ".obsidian" not in p.parts
    ]
    updated = 0
    for path in md_files:
        text = path.read_text(encoding="utf-8")
        new_text = replace_wikilinks(text, link_map)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8", newline="\n")
            updated += 1
    print(f"Updated wikilinks in {updated} files.")


if __name__ == "__main__":
    main()
