---
type: goal-map
title: "ExploreSEL — Entrepreneurship Competency Search Fragment (Unresolved)"
description: A small, unpaired competency-search result set for "entrepreneurship," distinct from the main ExploreSEL graph ingest, kept for provenance rather than treated as a standard.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-30
source:
  framework: "unidentified — partial search result, not a named standard"
  kind: search-fragment
---

# ExploreSEL — Entrepreneurship Competency Search Fragment (Unresolved)

> **This is not a framework goal-map** — it's a smaller, separate scrape (`caa7397e-records.json`) from the same session as the main ExploreSEL ingest, and it doesn't have the same shape. Flagging what it actually is rather than forcing it into the `nodes`/`relationships` schema the other `goals/exploresel-*` pages use.

## What this actually is
165 nodes with no relationship data at all in the export — just a flat list, in no meaningful order (checked: not grouped by anchor). Two kinds, distinguished by Neo4j label:

- **13 "anchor" nodes** (label `Competency`, no `Embedded`) — competency statements about entrepreneurship. Only one is traceable to anything else in this wiki: `term_661` ("introduction to entrepreneurship"), which is a real ExploreSEL term already ingested under [EDC Work Ready Now! Framework](exploresel-fw-edc-work-ready-now-framework.md). The other 12 have no `originalID` at all (or, in one case, a bare GUID from an unidentified source) — there's no way to trace them back to a named standard from this file alone.
- **152 "matched" nodes** (label `Competency, Embedded`) — competency statements from U.S. state CTE (Career & Technical Education) systems, identifiable only by their `notation` codes: Georgia CTAE (`CTAE-FS-*`, `9.CAT.*`), Pennsylvania (`PA.BIT.*`), and others not confidently identifiable (`NE.*`, `MKT-EN-*`, `IT-IDT/WD/DD/CSP *`, `FCC*`). A `depth` field (0 or 1) suggests these came from a similarity/embedding search anchored on the 13 competencies above, but **the actual anchor→match pairing isn't recoverable from this export** — there's no edge data, and the flat node order doesn't cluster by anchor.

## Where the data lives
[`goals/data/exploresel-entrepreneurship-search-fragment.ndjson`](data/exploresel-entrepreneurship-search-fragment.ndjson) — one JSON object per line, `kind: "anchor"` or `kind: "matched"`, carrying whatever identifying fields the source had (`identity`, `original_id`, `notation`, `name`, `depth`). No `nodes:`/`relationships:` frontmatter here, unlike the other `goals/exploresel-*` pages — there's nothing resolved enough yet to justify that shape.

## What it would take to actually use this
To turn this into a real goal-map (or a crosswalk like the main ExploreSEL ingest), someone would need to either re-run the original search/scrape with edge data intact, or identify which U.S. state CTE frameworks the `notation` codes belong to and re-derive the anchor-to-match pairing from the original tool. Neither is possible from the file alone.
