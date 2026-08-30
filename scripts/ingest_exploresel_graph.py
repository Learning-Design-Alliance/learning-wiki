#!/usr/bin/env python3
"""
ingest_exploresel_graph.py — One-off ingest of a scraped ExploreSEL/EASEL Lab
graph export (nodes + relationships, Neo4j-style) into this wiki's goal-map
schema (see goals/ and the "goal-map" discussion in project history).

Source data has four node labels (Competency, Skill, Standard, Jurisdiction)
and four relationship types, two of which turned out to be semantically
overloaded once inspected:

  HAS_CHILD  — used for THREE different things depending on which node types
               it connects:
                 (a) canonical-taxonomy internal tree (domain -> subdomain ->
                     skill descriptor) — a true hierarchy, ~200 edges
                 (b) a framework's own internal hierarchy (competency ->
                     sub-competency within the SAME framework) — a true
                     hierarchy, ~496 edges
                 (c) framework term -> canonical taxonomy node — NOT a real
                     hierarchy edge, it's a crosswalk/alignment mapping
                     mislabeled with the same relationship type — ~6506 edges
  RELATED_TO — cross-framework (and a little same-framework) similarity
               matches, ~8136 edges. Never touches the canonical taxonomy.
  DESCRIBES  — Standard (framework) -> its own top-level term(s), ~222 edges
  PUBLISHES  — Jurisdiction (publisher/org) -> Standard, ~40 edges

Only (a) and (b) are real parent/child hierarchy — those become `type:
default` relationships embedded in a goal-map page's frontmatter. (c) and
RELATED_TO are large many-to-many alignment graphs that do NOT fit embedded
per-page frontmatter at this scale; they're written out as separate
structured ndjson datasets instead, keyed by the same term_NNN ids used in
the goal-map pages.

Usage:
    python3 scripts/ingest_exploresel_graph.py <path-to-raw-export.json>
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import okf_lib as ok
import yaml

WIKI_ROOT = ok.WIKI_ROOT
GOALS_DIR = WIKI_ROOT / "goals"
DATA_DIR = GOALS_DIR / "data"


def load(path: str) -> dict:
    with open(path, encoding="utf-8-sig") as f:
        text = f.read()
    return json.loads(text, strict=False)  # strict=False tolerates literal
    # control characters (unescaped newlines) inside string values, present
    # in this export because of multi-line source competency statements.


def yaml_block(value) -> str:
    return yaml.safe_dump(value, sort_keys=False, allow_unicode=True, default_flow_style=False).rstrip("\n")


def node_to_dict(n: dict) -> dict:
    out = {
        "id": n["originalID"],
        "label": n["name"],
        "competency_framework": n.get("frameworkName", "ExploreSEL/EASEL Taxonomy"),
    }
    if n.get("label") == "Skill":
        out["kind"] = "skill"  # finer-grained observable-behavior leaf, vs. a named domain/subdomain
    if n.get("eselURL"):
        out["external_id"] = n["eselURL"]
    return out


def make_description(std: dict, fw_name: str) -> str:
    purpose = (std.get("purpose") or "").strip()
    if purpose:
        return purpose.rstrip(".") + "."
    desc = (std.get("description") or "").strip()
    if desc:
        first_sentence = re.split(r"(?<=[.!?])\s+", desc)[0]
        if len(first_sentence) <= 300:
            return first_sentence
        return first_sentence[:300].rsplit(" ", 1)[0] + "…"
    return f"{fw_name}, one of the ~40 SEL/competency frameworks ExploreSEL catalogs against its shared taxonomy."


def write_page(path: Path, frontmatter: dict, body: str):
    fm_text = yaml_block(frontmatter)
    path.write_text(f"---\n{fm_text}\n---\n\n{body}", encoding="utf-8")


def build_taxonomy_page(nodes_by_id: dict, has_child_internal: list):
    taxonomy_ids = [
        nid for nid, n in nodes_by_id.items()
        if n.get("label") in ("Competency", "Skill") and "frameworkName" not in n
    ]
    taxonomy_ids.sort(key=lambda x: int(x.split("_")[1]))
    nodes = [node_to_dict(nodes_by_id[nid]) for nid in taxonomy_ids]
    rels = [
        {"source": s, "target": t, "type": "default"}
        for s, t in has_child_internal
    ]

    fm = {
        "type": "goal-map",
        "title": "ExploreSEL — EASEL Lab Taxonomy Project (Full Depth)",
        "description": "The complete six-domain SEL skill taxonomy from Harvard's EASEL Lab, down to individual observable-behavior leaf nodes, ingested from a real scraped graph export.",
        "status": "draft",
        "generated": {"by": "claude/unspecified", "at": "2026-08-30"},
        "source": {
            "framework": "EASEL Lab Taxonomy Project (ExploreSEL)",
            "kind": "standard",
            "source_url": "https://easel.gse.harvard.edu/taxonomy-project",
            "license": "Confirm EASEL Lab / Wallace Foundation terms before treating status as anything past draft",
        },
        "nodes": nodes,
        "relationships": rels,
    }

    body = f"""# ExploreSEL — EASEL Lab Taxonomy Project (Full Depth)

> **Real data, replacing the earlier reconstructed draft.** This page was regenerated from an actual scraped ExploreSEL/EASEL graph export ({len(nodes)} nodes, {len(rels)} `default` hierarchy edges) rather than web-search-reconstructed domain/subdomain names. It goes one level deeper than the previous draft: six top domains, 23 subdomains, and {len(nodes) - 29} individual observable-behavior "Skill" leaf nodes underneath those (e.g. "Sustains attention by focusing on task at hand" under Attention Control). Leaf nodes carry `kind: skill` in their node entry to distinguish them from the named domain/subdomain level.

## Description
Six top-level domains (Cognitive, Emotion, Social, Values, Perspectives, Identity/Self-Image), each with subdomains, each with individual skill/behavior descriptors — a real three-level hierarchy, all `type: default` (hierarchical) relationships.

## What's tracked separately, not embedded here
Every one of the ~40+ SEL/competency frameworks ExploreSEL catalogs (CASEL, OECD, ACT Holistic Framework, etc.) maps its own competencies onto nodes in this taxonomy — a real crosswalk with roughly 6,500 mapping edges in the source data. That crosswalk is too large and too many-to-many to embed in this page's frontmatter (or any single framework's), so it's kept as a separate dataset: [`goals/data/exploresel-framework-taxonomy-crosswalk.ndjson`](data/exploresel-framework-taxonomy-crosswalk.ndjson), keyed by the same `term_NNN` ids used as node `id`s here and in each framework's own goal-map page (see `goals/exploresel-fw-*.md`).

## Key Sources
- Jones, S. M., Bailey, R., Brush, K., Kahn, J., et al. (2017). *Navigating Social and Emotional Learning from the Inside Out.* Harvard Graduate School of Education / Wallace Foundation.
- EASEL Lab. *Taxonomy Project.* https://easel.gse.harvard.edu/taxonomy-project
- Explore SEL. https://exploresel.gse.harvard.edu/
"""
    write_page(GOALS_DIR / "exploresel-taxonomy.md", fm, body)
    return len(nodes), len(rels)


def build_framework_pages(nodes_by_id, standards, jurisdictions, publishes_by_standard,
                           describes_by_standard, framework_internal_by_fw, crosswalk_count_by_term, related_count_by_term):
    written = []
    for std_id, std in standards.items():
        fw_name = std["name"]
        term_ids = [nid for nid, n in nodes_by_id.items() if n.get("frameworkName") == fw_name]
        if not term_ids:
            continue
        term_id_set = set(term_ids)
        term_ids.sort(key=lambda x: int(x.split("_")[1]))

        nodes = [node_to_dict(nodes_by_id[nid]) for nid in term_ids]
        rels = [
            {"source": s, "target": t, "type": "default"}
            for (s, t) in framework_internal_by_fw.get(fw_name, [])
        ]

        source_block = {
            "framework": fw_name,
            "kind": "standard",
            "framework_full_name": std.get("nameFull") or fw_name,
            "description": std.get("description"),
            "purpose": std.get("purpose"),
            "age_range": std.get("ageRange"),
            "setting": std.get("setting"),
            "source_url": std.get("URL"),
            "eselURL": std.get("eselURL"),
        }
        source_block = {k: v for k, v in source_block.items() if v}

        jur_id = publishes_by_standard.get(std_id)
        if jur_id and jur_id in jurisdictions:
            source_block["publisher"] = jurisdictions[jur_id]["name"]
            source_block["publisher_type"] = jurisdictions[jur_id].get("type")

        fm = {
            "type": "goal-map",
            "title": f"ExploreSEL Framework — {fw_name}",
            "description": make_description(std, fw_name),
            "status": "draft",
            "generated": {"by": "claude/unspecified", "at": "2026-08-30"},
            "source": source_block,
            "nodes": nodes,
            "relationships": rels,
        }

        n_crosswalk = sum(crosswalk_count_by_term.get(t, 0) for t in term_ids)
        n_related = sum(related_count_by_term.get(t, 0) for t in term_ids)

        slug = ok.slugify(fw_name)
        body = f"""# ExploreSEL Framework — {fw_name}

> Ingested from a real scraped ExploreSEL/EASEL graph export. {len(nodes)} of this framework's own competency terms, {len(rels)} internal `default` (hierarchical) edges among them.

## Description
{std.get("description") or "(no description in source export)"}

## Alignment to the shared taxonomy
This framework's terms carry {n_crosswalk} crosswalk edges into the canonical [ExploreSEL taxonomy](exploresel-taxonomy.md) (which of the six domains/23 subdomains/skill descriptors this framework's competencies map onto), plus {n_related} cross-framework similarity edges to other frameworks. Both are kept as separate datasets rather than embedded here — grep them by this page's node ids:

```
grep '"source": "{{term_id}}"' goals/data/exploresel-framework-taxonomy-crosswalk.ndjson
grep '"source": "{{term_id}}"' goals/data/exploresel-cross-framework-similarity.ndjson
```
(paths relative to the wiki root; substitute one of this page's node ids for `{{term_id}}`)

## Key Sources
- ExploreSEL framework profile: {std.get("eselURL") or "(no URL in source export)"}
- Publisher: {jurisdictions.get(jur_id, {}).get("name", "unknown") if jur_id else "not recorded in source export"}
"""
        path = GOALS_DIR / f"exploresel-fw-{slug}.md"
        write_page(path, fm, body)
        written.append(path)
    return written


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    raw_path = sys.argv[1]
    data = load(raw_path)
    nodes = data["nodes"]
    rels = data["relationships"]
    nodes_by_id = {n["originalID"]: n for n in nodes}

    GOALS_DIR.mkdir(exist_ok=True)
    DATA_DIR.mkdir(exist_ok=True)

    # Save a clean, valid-JSON copy of the primary source record.
    (DATA_DIR / "exploresel-graph-raw.json").write_text(
        json.dumps(data, ensure_ascii=False), encoding="utf-8"
    )

    taxonomy_ids = set(
        nid for nid, n in nodes_by_id.items()
        if n.get("label") in ("Competency", "Skill") and "frameworkName" not in n
    )

    def fw(id_):
        return nodes_by_id.get(id_, {}).get("frameworkName")

    has_child_taxonomy_internal = []
    has_child_framework_internal = {}  # fw_name -> [(s,t)]
    crosswalk_edges = []  # framework term -> taxonomy node (mislabeled HAS_CHILD)
    for r in rels:
        if r["type"] != "HAS_CHILD":
            continue
        s, t = r["from"], r["to"]
        if s in taxonomy_ids and t in taxonomy_ids:
            has_child_taxonomy_internal.append((s, t))
        elif fw(s) is not None and fw(s) == fw(t):
            has_child_framework_internal.setdefault(fw(s), []).append((s, t))
        elif fw(s) is not None and t in taxonomy_ids:
            crosswalk_edges.append((s, t))
        # (remaining categories were empty in this export; skip silently)

    similarity_edges = [(r["from"], r["to"]) for r in rels if r["type"] == "RELATED_TO"]

    (DATA_DIR / "exploresel-framework-taxonomy-crosswalk.ndjson").write_text(
        "\n".join(json.dumps({"source": s, "target": t}) for s, t in crosswalk_edges) + "\n",
        encoding="utf-8",
    )
    (DATA_DIR / "exploresel-cross-framework-similarity.ndjson").write_text(
        "\n".join(json.dumps({"source": s, "target": t}) for s, t in similarity_edges) + "\n",
        encoding="utf-8",
    )

    from collections import Counter
    crosswalk_count_by_term = Counter(s for s, t in crosswalk_edges)
    related_count_by_term = Counter()
    for s, t in similarity_edges:
        related_count_by_term[s] += 1
        related_count_by_term[t] += 1

    n_tax_nodes, n_tax_rels = build_taxonomy_page(nodes_by_id, has_child_taxonomy_internal)
    print(f"Taxonomy page: {n_tax_nodes} nodes, {n_tax_rels} relationships")

    standards = {n["originalID"]: n for n in nodes if n.get("label") == "Standard"}
    jurisdictions = {n["originalID"]: n for n in nodes if n.get("label") == "Jurisdiction"}
    publishes_by_standard = {r["to"]: r["from"] for r in rels if r["type"] == "PUBLISHES"}
    describes_by_standard = {}
    for r in rels:
        if r["type"] == "DESCRIBES":
            describes_by_standard.setdefault(r["from"], []).append(r["to"])

    written = build_framework_pages(
        nodes_by_id, standards, jurisdictions, publishes_by_standard,
        describes_by_standard, has_child_framework_internal,
        crosswalk_count_by_term, related_count_by_term,
    )
    print(f"Framework pages written: {len(written)}")
    for p in written:
        print(f"  {p.relative_to(WIKI_ROOT)}")


if __name__ == "__main__":
    main()
