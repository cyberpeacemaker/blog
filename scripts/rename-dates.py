#!/usr/bin/env python3
"""Rename MM-DD-slug.md -> YYYY-MM-DD-slug.md, update wikilinks, add frontmatter."""
from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MM_DD_PATTERN = re.compile(r"^(\d{2})-(\d{2})-(.+)\.md$")
WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(#[^\]]+)?(\|[^\]]+)?\]\]")

SKIP_RENAME = {
    "Home.md",
    "My Stack.md",
    "Daily Workflow.md",
    "Tag Taxonomy.md",
    "daily-note.md",
}

SKIP_RENAME_PREFIXES = ("MOC - ",)

FOLDER_TAGS: dict[str, list[str]] = {
    "00-Meta": ["meta"],
    "01-NSM-Malcolm": ["malcolm", "nsm"],
    "02-Threat-Hunting-DFIR": ["threat-hunting", "dfir"],
    "03-AI-Agents": ["ai", "agents"],
    "04-Dev-Environment": ["dev"],
    "05-Software-Engineering": ["software"],
    "06-Design-Creative": ["design"],
    "07-Productivity-Work": ["productivity"],
    "08-Career-Presentations": ["career"],
    "09-Personal": ["personal"],
    "Uncategorized": ["uncategorized"],
}

FOLDER_TYPE: dict[str, str] = {
    "00-Meta": "reference",
    "Uncategorized": "draft",
}

HUB_BASENAMES = {
    "05-Software-Engineering.md",
    "06-Design-Creative.md",
    "07-Productivity-Work.md",
    "08-Career-Presentations.md",
    "09-Personal.md",
}


def git_year(rel_path: str) -> str:
    result = subprocess.run(
        ["git", "log", "--follow", "--format=%aI", "--", rel_path],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    lines = [ln.strip() for ln in result.stdout.splitlines() if ln.strip()]
    if lines:
        return lines[-1][:4]
    return "2026"


def should_rename(basename: str) -> bool:
    if basename in SKIP_RENAME or basename in HUB_BASENAMES:
        return False
    if any(basename.startswith(p) for p in SKIP_RENAME_PREFIXES):
        return False
    return bool(MM_DD_PATTERN.match(basename))


def new_basename(old_basename: str, year: str) -> str:
    m = MM_DD_PATTERN.match(old_basename)
    if not m:
        return old_basename
    month, day, slug = m.groups()
    return f"{year}-{month}-{day}-{slug}.md"


def has_yaml_frontmatter(text: str) -> bool:
    if not text.startswith("---\n"):
        return False
    end = text.find("\n---\n", 4)
    if end == -1:
        return False
    block = text[4:end]
    return "created:" in block or "tags:" in block or "type:" in block


def infer_lang(text: str) -> str:
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text[:2000]))
    return "zh" if cjk > 40 else "en"


def infer_type(rel: Path, basename: str) -> str:
    if basename in HUB_BASENAMES or basename.startswith("MOC - "):
        return "hub"
    top = rel.parts[0] if rel.parts else ""
    if basename == "daily-note.md":
        return "template"
    if "daily" in rel.parts and re.match(r"^\d{4}-\d{2}-\d{2}\.md$", basename):
        return "daily"
    return FOLDER_TYPE.get(top, "reference")


def folder_tags(rel: Path) -> list[str]:
    top = rel.parts[0] if rel.parts else "Uncategorized"
    tags = list(FOLDER_TAGS.get(top, ["uncategorized"]))
    name = rel.stem.lower()
    keyword_map = {
        "malcolm": "malcolm",
        "opensearch": "opensearch",
        "arkime": "arkime",
        "zeek": "zeek",
        "suricata": "suricata",
        "mitre": "mitre",
        "claude": "claude",
        "cursor": "cursor",
        "harness": "harness",
        "git": "git",
        "python": "python",
        "obsidian": "obsidian",
    }
    for key, tag in keyword_map.items():
        if key in name and tag not in tags:
            tags.append(tag)
    return tags[:6]


def build_frontmatter(created: str, tags: list[str], note_type: str, lang: str) -> str:
    tag_str = ", ".join(tags)
    return (
        f"---\n"
        f"created: {created}\n"
        f"tags: [{tag_str}]\n"
        f"type: {note_type}\n"
        f"lang: {lang}\n"
        f"status: draft\n"
        f"---\n\n"
    )


def parse_created_from_name(basename: str) -> str | None:
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})-", basename)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = MM_DD_PATTERN.match(basename)
    if m:
        return f"2026-{m.group(1)}-{m.group(2)}"
    return None


def update_frontmatter_created(text: str, created: str) -> str:
    if not has_yaml_frontmatter(text):
        return text
    return re.sub(
        r"(?m)^created:\s*.+$",
        f"created: {created}",
        text,
        count=1,
    )


def collect_renames() -> list[tuple[Path, Path]]:
    renames: list[tuple[Path, Path]] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        parts = rel.parts
        if ".git" in parts or ".obsidian" in parts:
            continue
        basename = path.name
        if not should_rename(basename):
            continue
        rel_posix = rel.as_posix()
        year = git_year(rel_posix)
        new_name = new_basename(basename, year)
        if new_name == basename:
            continue
        renames.append((path, path.with_name(new_name)))
    renames.sort(key=lambda x: len(x[0].as_posix()), reverse=True)
    return renames


def git_mv(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["git", "mv", src.as_posix(), dst.as_posix()],
        cwd=ROOT,
        check=True,
    )


def build_link_map(renames: list[tuple[Path, Path]]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for src, dst in renames:
        old = src.stem
        new = dst.stem
        mapping[old] = new
        mapping[src.as_posix().replace(".md", "")] = dst.as_posix().replace(".md", "")
        mapping[src.name] = dst.name
    return mapping


def replace_wikilinks(text: str, link_map: dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group(1)
        suffix = (match.group(2) or "") + (match.group(3) or "")
        if target in link_map:
            return f"[[{link_map[target]}{suffix}]]"
        base = Path(target).name
        if base.endswith(".md"):
            base = base[:-3]
        if base in link_map:
            parent = str(Path(target).parent)
            if parent and parent != ".":
                new_target = f"{parent}/{link_map[base]}"
            else:
                new_target = link_map[base]
            return f"[[{new_target}{suffix}]]"
        stem = Path(target).stem
        if stem in link_map:
            parent = str(Path(target).parent)
            if parent and parent != ".":
                new_target = f"{parent}/{link_map[stem]}"
            else:
                new_target = link_map[stem]
            return f"[[{new_target}{suffix}]]"
        return match.group(0)

    return WIKILINK_PATTERN.sub(repl, text)


def process_frontmatter(path: Path) -> None:
    if path.name == "daily-note.md" and "templates" in path.parts:
        return
    text = path.read_text(encoding="utf-8")
    created = parse_created_from_name(path.name)
    rel = path.relative_to(ROOT)
    tags = folder_tags(rel)
    note_type = infer_type(rel, path.name)
    lang = infer_lang(text)

    if has_yaml_frontmatter(text):
        if created:
            text = update_frontmatter_created(text, created)
        path.write_text(text, encoding="utf-8", newline="\n")
        return

    if created is None and path.name in {"Home.md", "My Stack.md", "Daily Workflow.md", "Tag Taxonomy.md"}:
        created = "2026-07-07"
        note_type = "hub" if path.name == "Home.md" else "reference"
        if path.name == "Home.md":
            note_type = "hub"
        if path.name in {"My Stack.md", "Tag Taxonomy.md"}:
            note_type = "hub" if path.name == "My Stack.md" else "reference"
        if path.name == "Daily Workflow.md":
            note_type = "reference"
            tags = ["meta", "workflow"]

    if created is None:
        created = "2026-07-07"

    fm = build_frontmatter(created, tags, note_type, lang)
    path.write_text(fm + text.lstrip("\n"), encoding="utf-8", newline="\n")


def main() -> None:
    os.chdir(ROOT)
    renames = collect_renames()
    print(f"Renaming {len(renames)} files...")
    for src, dst in renames:
        print(f"  {src.as_posix()} -> {dst.name}")
        git_mv(src, dst)

    link_map = build_link_map(renames)
    md_files = [
        p
        for p in ROOT.rglob("*.md")
        if ".git" not in p.parts and ".obsidian" not in p.parts
    ]

    print(f"Updating wikilinks in {len(md_files)} files...")
    for path in md_files:
        text = path.read_text(encoding="utf-8")
        updated = replace_wikilinks(text, link_map)
        if updated != text:
            path.write_text(updated, encoding="utf-8", newline="\n")

    print("Adding/updating frontmatter...")
    for path in md_files:
        process_frontmatter(path)

    print("Done.")


if __name__ == "__main__":
    main()
