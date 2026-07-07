#!/usr/bin/env python3
"""Scan vault markdown, build graph metrics, emit JSON / Cursor / Obsidian canvases."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent
CURSOR_CANVAS_DIR = Path.home() / ".cursor" / "projects" / "c-Users-ydnaa-Documents-Github-blog" / "canvases"
OBSIDIAN_CANVAS = ROOT / "00-Meta" / "Vault Map.canvas"

SKIP_PARTS = {".git", ".obsidian", "node_modules", "__pycache__"}
DATED_TOPIC = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]]+)?(?:\|[^\]]+)?\]\]")
FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

HOME_REL = "00-Meta/Home.md"
AREA_HUB_STEMS = {
    "05-Software-Engineering",
    "06-Design-Creative",
    "07-Productivity-Work",
    "08-Career-Presentations",
    "09-Personal",
    "Uncategorized",
}

WORK_MOCS = [
    "00-Meta/MOC - Malcolm & NSM.md",
    "00-Meta/MOC - OpenSearch Querying.md",
    "00-Meta/MOC - Threat Hunting.md",
    "00-Meta/MOC - AI Agents.md",
]
TOOL_HUBS = [
    "00-Meta/My Stack.md",
    "00-Meta/MOC - Claude & Cursor.md",
    "00-Meta/MOC - Dev Environment.md",
    "00-Meta/Daily Workflow.md",
]
OTHER_HUBS = [
    "05-Software-Engineering/05-Software-Engineering.md",
    "06-Design-Creative/06-Design-Creative.md",
    "07-Productivity-Work/07-Productivity-Work.md",
    "08-Career-Presentations/08-Career-Presentations.md",
    "09-Personal/09-Personal.md",
    "Uncategorized/Uncategorized.md",
]


@dataclass
class Note:
    id: str
    title: str
    path: str
    folder: str
    note_type: str
    tags: list[str]
    status: str
    lang: str
    created: str
    outbound: list[str] = field(default_factory=list)
    is_hub: bool = False


def should_skip(path: Path) -> bool:
    return any(part in SKIP_PARTS for part in path.parts)


def parse_frontmatter(text: str) -> dict[str, str | list[str]]:
    m = FRONTMATTER.match(text)
    if not m:
        return {}
    block = m.group(1)
    result: dict[str, str | list[str]] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        key = key.strip()
        raw = raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            if not inner:
                result[key] = []
            else:
                result[key] = [t.strip().strip("'\"") for t in inner.split(",")]
        else:
            result[key] = raw.strip("'\"")
    return result


def note_id(rel: Path) -> str:
    return rel.with_suffix("").as_posix()


def top_folder(rel: Path) -> str:
    parts = rel.parts
    return parts[0] if parts else "root"


def is_dated_duplicate(path: Path) -> bool:
    m = DATED_TOPIC.match(path.name)
    if not m:
        return False
    return path.with_name(f"{m.group(4)}.md").exists()


def title_from_text(text: str, stem: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return stem


def stable_id(seed: str) -> str:
    return hashlib.md5(seed.encode()).hexdigest()[:16]


def scan_vault() -> tuple[dict[str, Note], list[tuple[str, str, str]]]:
    """Return canonical notes by id and raw broken link triples (source_id, target, source_path)."""
    raw_files: list[Path] = []
    for path in ROOT.rglob("*.md"):
        if should_skip(path):
            continue
        raw_files.append(path)

    canonical_paths: list[Path] = []
    for path in raw_files:
        if is_dated_duplicate(path):
            continue
        canonical_paths.append(path)

    stem_index: dict[str, list[str]] = defaultdict(list)
    path_index: dict[str, Path] = {}
    for path in canonical_paths:
        rel = path.relative_to(ROOT)
        nid = note_id(rel)
        path_index[nid] = path
        stem_index[path.stem].append(nid)
        stem_index[rel.with_suffix("").name].append(nid)

    def resolve_target(raw_target: str) -> str | None:
        target = raw_target.strip()
        if not target:
            return None
        if target in path_index:
            return target
        stem = Path(target).stem
        candidates = stem_index.get(stem, [])
        if len(candidates) == 1:
            return candidates[0]
        if len(candidates) > 1:
            parent = str(Path(target).parent)
            if parent and parent != ".":
                prefixed = f"{parent}/{stem}"
                if prefixed in path_index:
                    return prefixed
            for cid in candidates:
                if cid.endswith(f"/{stem}") or cid == stem:
                    return cid
            return candidates[0]
        m = DATED_TOPIC.match(f"{stem}.md")
        if m:
            slug = m.group(4)
            slug_candidates = stem_index.get(slug, [])
            if slug_candidates:
                return slug_candidates[0]
        return None

    notes: dict[str, Note] = {}
    broken: list[tuple[str, str, str]] = []

    for path in canonical_paths:
        rel = path.relative_to(ROOT)
        nid = note_id(rel)
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        tags = meta.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        note_type = str(meta.get("type", ""))
        is_hub = (
            note_type == "hub"
            or path.name.startswith("MOC - ")
            or path.stem in AREA_HUB_STEMS
            or nid == note_id(Path(HOME_REL))
            or nid in {note_id(Path(p)) for p in WORK_MOCS + TOOL_HUBS + OTHER_HUBS}
        )
        outbound: list[str] = []
        for match in WIKILINK.finditer(text):
            raw = match.group(1)
            resolved = resolve_target(raw)
            if resolved:
                outbound.append(resolved)
            else:
                broken.append((nid, raw, rel.as_posix()))

        notes[nid] = Note(
            id=nid,
            title=title_from_text(text, path.stem),
            path=rel.as_posix(),
            folder=top_folder(rel),
            note_type=note_type,
            tags=list(tags),
            status=str(meta.get("status", "")),
            lang=str(meta.get("lang", "")),
            created=str(meta.get("created", "")),
            outbound=outbound,
            is_hub=is_hub,
        )

    return notes, broken


def build_hub_graph(notes: dict[str, Note]) -> dict:
    home_id = note_id(Path(HOME_REL))
    hub_ids = {nid for nid, n in notes.items() if n.is_hub}
    nodes = []
    for nid in sorted(hub_ids):
        n = notes[nid]
        nodes.append({"id": nid, "label": n.title, "path": n.path, "folder": n.folder})
    edges = []
    seen_edges: set[tuple[str, str]] = set()
    for nid in hub_ids:
        for target in notes[nid].outbound:
            if target in hub_ids:
                key = (nid, target)
                if key not in seen_edges:
                    seen_edges.add(key)
                    edges.append({"from": nid, "to": target})
    if home_id in hub_ids and not any(e["from"] == home_id for e in edges):
        for target in notes[home_id].outbound:
            if target in hub_ids:
                key = (home_id, target)
                if key not in seen_edges:
                    seen_edges.add(key)
                    edges.append({"from": home_id, "to": target})
    return {"nodes": nodes, "edges": edges}


def build_metrics(notes: dict[str, Note], broken: list[tuple[str, str, str]]) -> dict:
    inbound: Counter[str] = Counter()
    outbound_count: Counter[str] = Counter()
    for n in notes.values():
        outbound_count[n.id] = len(n.outbound)
        for target in n.outbound:
            if target in notes:
                inbound[target] += 1

    by_folder: Counter[str] = Counter(n.folder for n in notes.values())
    by_type: Counter[str] = Counter(n.note_type or "unknown" for n in notes.values())
    by_status: Counter[str] = Counter(n.status or "unknown" for n in notes.values())

    orphans = [
        {"title": n.title, "path": n.path}
        for n in sorted(notes.values(), key=lambda x: x.path)
        if inbound[n.id] == 0 and n.id != note_id(Path(HOME_REL))
    ]

    top_linked = [
        {"title": notes[nid].title, "path": notes[nid].path, "count": count}
        for nid, count in outbound_count.most_common(15)
        if count > 0
    ]

    broken_rows = [
        {"source": notes[src].title if src in notes else src, "target": tgt, "sourcePath": spath}
        for src, tgt, spath in broken[:30]
    ]

    folders = sorted({n.folder for n in notes.values()})

    return {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "stats": {
            "totalNotes": len(notes),
            "hubs": sum(1 for n in notes.values() if n.is_hub),
            "drafts": sum(1 for n in notes.values() if n.status == "draft"),
            "brokenLinks": len(broken),
            "orphans": len(orphans),
        },
        "byFolder": [{"label": k, "value": v} for k, v in by_folder.most_common()],
        "byType": [{"label": k, "value": v} for k, v in by_type.most_common()],
        "byStatus": [{"label": k, "value": v} for k, v in by_status.most_common()],
        "topLinked": top_linked[:10],
        "orphans": orphans[:20],
        "brokenLinks": broken_rows,
        "hubGraph": build_hub_graph(notes),
        "folders": ["all"] + folders,
    }


def emit_json(data: dict) -> Path:
    out = SCRIPTS / "vault-graph.json"
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out


def edge_sides(from_x: float, from_y: float, to_x: float, to_y: float) -> tuple[str, str]:
    dx = to_x - from_x
    dy = to_y - from_y
    if abs(dx) >= abs(dy):
        return ("right", "left") if dx >= 0 else ("left", "right")
    return ("bottom", "top") if dy >= 0 else ("top", "bottom")


def emit_obsidian(notes: dict[str, Note], hub_graph: dict) -> Path:
    node_w, node_h, gap_x, gap_y = 400, 200, 120, 80
    columns = [
        ("Work", WORK_MOCS, -1400),
        ("Tools", TOOL_HUBS, -450),
        ("Home", [HOME_REL], 0),
        ("Other", OTHER_HUBS, 500),
    ]

    nodes: list[dict] = []
    positions: dict[str, tuple[float, float]] = {}

    for _label, paths, base_x in columns:
        for i, rel_path in enumerate(paths):
            nid = note_id(Path(rel_path))
            if nid not in notes:
                continue
            x = base_x
            y = i * (node_h + gap_y)
            if rel_path == HOME_REL:
                y = 280
            positions[nid] = (x, y)
            nodes.append(
                {
                    "id": stable_id(nid),
                    "type": "file",
                    "x": int(x),
                    "y": int(y),
                    "width": node_w,
                    "height": node_h,
                    "file": rel_path,
                }
            )

    edges: list[dict] = []
    home_nid = note_id(Path(HOME_REL))
    home_pos = positions.get(home_nid)
    for edge in hub_graph["edges"]:
        src, tgt = edge["from"], edge["to"]
        if src not in positions or tgt not in positions:
            continue
        if src == tgt:
            continue
        sx, sy = positions[src]
        tx, ty = positions[tgt]
        from_side, to_side = edge_sides(sx, sy, tx, ty)
        edges.append(
            {
                "id": stable_id(f"edge:{src}->{tgt}"),
                "fromNode": stable_id(src),
                "fromSide": from_side,
                "fromEnd": "none",
                "toNode": stable_id(tgt),
                "toSide": to_side,
                "toEnd": "arrow",
            }
        )

    payload = {"nodes": nodes, "edges": edges}
    OBSIDIAN_CANVAS.parent.mkdir(parents=True, exist_ok=True)
    OBSIDIAN_CANVAS.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return OBSIDIAN_CANVAS


CURSOR_TEMPLATE = '''// Generated by scripts/build-vault-canvas.py — do not edit by hand.
import {
  Card,
  CardBody,
  CardHeader,
  computeDAGLayout,
  Divider,
  Grid,
  H1,
  H2,
  PieChart,
  Row,
  Select,
  Stack,
  Stat,
  Table,
  Text,
  useCanvasState,
  useHostTheme,
} from "cursor/canvas";

const VAULT_GRAPH = __GRAPH_JSON__ as {
  generated: string;
  stats: { totalNotes: number; hubs: number; drafts: number; brokenLinks: number; orphans: number };
  byFolder: { label: string; value: number }[];
  topLinked: { title: string; path: string; count: number }[];
  orphans: { title: string; path: string }[];
  brokenLinks: { source: string; target: string; sourcePath: string }[];
  hubGraph: { nodes: { id: string; label: string; path: string; folder: string }[]; edges: { from: string; to: string }[] };
  folders: string[];
};

function MocGraph({ folderFilter }: { folderFilter: string }) {
  const theme = useHostTheme();
  const { nodes, edges } = VAULT_GRAPH.hubGraph;
  const layout = computeDAGLayout({
    nodes: nodes.map((n) => ({ id: n.id })),
    edges: edges.map((e) => ({ from: e.from, to: e.to })),
    direction: "horizontal",
    nodeWidth: 168,
    nodeHeight: 36,
    rankGap: 72,
    nodeGap: 24,
    padding: 32,
  });

  const nodeMeta = new Map(nodes.map((n) => [n.id, n]));
  const labelFor = (id: string) => nodeMeta.get(id)?.label ?? id.split("/").pop() ?? id;
  const dimmed = (id: string) =>
    folderFilter !== "all" && nodeMeta.get(id)?.folder !== folderFilter;

  return (
    <div style={{ overflowX: "auto" }}>
      <svg
        width={layout.width}
        height={layout.height}
        style={{ display: "block", minWidth: layout.width }}
      >
        {layout.edges.map((e, i) => (
          <line
            key={i}
            x1={e.sourceX}
            y1={e.sourceY}
            x2={e.targetX}
            y2={e.targetY}
            stroke={e.isBackEdge ? theme.stroke.secondary : theme.stroke.primary}
            strokeWidth={1}
            strokeDasharray={e.isBackEdge ? "4 3" : undefined}
          />
        ))}
        {layout.nodes.map((n) => {
          const muted = dimmed(n.id);
          return (
            <g key={n.id}>
              <rect
                x={n.x}
                y={n.y}
                width={168}
                height={36}
                rx={4}
                fill={muted ? theme.fill.tertiary : theme.fill.secondary}
                stroke={theme.stroke.tertiary}
              />
              <text
                x={n.x + 8}
                y={n.y + 22}
                fill={muted ? theme.text.tertiary : theme.text.primary}
                fontSize={11}
              >
                {labelFor(n.id).length > 22 ? `${labelFor(n.id).slice(0, 20)}…` : labelFor(n.id)}
              </text>
            </g>
          );
        })}
      </svg>
      <Text style={{ color: theme.text.tertiary, fontSize: 11, marginTop: 4 }}>
        Source: vault wikilinks · hub-level MOC graph · {VAULT_GRAPH.generated}
      </Text>
    </div>
  );
}

export default function VaultMapCanvas() {
  const theme = useHostTheme();
  const [folderFilter, setFolderFilter] = useCanvasState("folderFilter", "all");
  const { stats } = VAULT_GRAPH;

  const folderOptions = VAULT_GRAPH.folders.map((f) => ({
    value: f,
    label: f === "all" ? "All folders" : f,
  }));

  return (
    <Stack gap={20} style={{ padding: 16, color: theme.text.primary }}>
      <Row align="center" justify="space-between" wrap>
        <H1>Vault Map</H1>
        <Select
          value={folderFilter}
          onChange={setFolderFilter}
          options={folderOptions}
          style={{ minWidth: 200 }}
        />
      </Row>

      <Grid columns={5} gap={12}>
        <Stat value={stats.totalNotes} label="Canonical notes" />
        <Stat value={stats.hubs} label="Hub pages" />
        <Stat value={stats.drafts} label="Drafts" tone="warning" />
        <Stat value={stats.orphans} label="Orphans" tone="info" />
        <Stat value={stats.brokenLinks} label="Broken links" tone={stats.brokenLinks > 0 ? "danger" : "success"} />
      </Grid>

      <Card>
        <CardHeader title="MOC hub graph" />
        <CardBody>
          <MocGraph folderFilter={folderFilter} />
        </CardBody>
      </Card>

      <Grid columns={2} gap={16}>
        <Card>
          <CardHeader title="Notes by folder" />
          <CardBody>
            <PieChart data={VAULT_GRAPH.byFolder} size={220} />
            <Text style={{ color: theme.text.tertiary, fontSize: 11, marginTop: 8 }}>
              Source: vault scan · count of canonical markdown files per top-level folder
            </Text>
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Most outbound links" />
          <CardBody style={{ padding: 0 }}>
            <Table
              headers={["Note", "Links"]}
              rows={VAULT_GRAPH.topLinked.map((r) => [r.title, String(r.count)])}
            />
          </CardBody>
        </Card>
      </Grid>

      <Divider />

      <H2>Maintenance</H2>
      <Grid columns={2} gap={16}>
        <Card>
          <CardHeader title="Orphan notes (no inbound links)" />
          <CardBody style={{ padding: 0 }}>
            <Table
              headers={["Note", "Path"]}
              rows={VAULT_GRAPH.orphans.map((r) => [r.title, r.path])}
            />
          </CardBody>
        </Card>

        <Card>
          <CardHeader title="Broken wikilinks" />
          <CardBody style={{ padding: 0 }}>
            <Table
              headers={["Source", "Target"]}
              rows={VAULT_GRAPH.brokenLinks.map((r) => [r.source, r.target])}
              rowTone={VAULT_GRAPH.brokenLinks.map(() => "danger" as const)}
            />
          </CardBody>
        </Card>
      </Grid>
    </Stack>
  );
}
'''


def emit_cursor(data: dict) -> Path:
    graph_json = json.dumps(data, ensure_ascii=False)
    content = CURSOR_TEMPLATE.replace("__GRAPH_JSON__", graph_json)
    CURSOR_CANVAS_DIR.mkdir(parents=True, exist_ok=True)
    out = CURSOR_CANVAS_DIR / "vault-map.canvas.tsx"
    out.write_text(content, encoding="utf-8", newline="\n")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Build vault graph and canvas outputs.")
    parser.add_argument("--json", action="store_true", help="Write scripts/vault-graph.json")
    parser.add_argument("--cursor", action="store_true", help="Write Cursor vault-map.canvas.tsx")
    parser.add_argument("--obsidian", action="store_true", help="Write 00-Meta/Vault Map.canvas")
    parser.add_argument("--all", action="store_true", help="Write all outputs")
    args = parser.parse_args()

    if not (args.json or args.cursor or args.obsidian or args.all):
        parser.error("Specify at least one of --json, --cursor, --obsidian, or --all")

    notes, broken = scan_vault()
    data = build_metrics(notes, broken)

    if args.json or args.all:
        path = emit_json(data)
        print(f"Wrote {path}")

    if args.cursor or args.all:
        path = emit_cursor(data)
        print(f"Wrote {path}")

    if args.obsidian or args.all:
        path = emit_obsidian(notes, data["hubGraph"])
        print(f"Wrote {path}")

    print(
        f"Scanned {data['stats']['totalNotes']} canonical notes, "
        f"{data['stats']['hubs']} hubs, {data['stats']['brokenLinks']} broken links."
    )


if __name__ == "__main__":
    main()
