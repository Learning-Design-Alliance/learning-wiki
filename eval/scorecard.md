Measured with today's `scripts/` against each tree (see scripts/health_scorecard.py). Δ is against the column to its left; ✓/✗ says whether it moved the better way.

`2f06ca4` = `2f06ca4` · `57ef392` = `57ef392`

| metric | better | main (start) | after ingest | Δ | after codes+headers | Δ |
|---|---|---:|---:|---:|---:|---:|
| Content pages |  | 3,765 | 4,002 | +237 | 4,002 | · |
| Claim pages |  | 434 | 578 | +144 | 578 | · |
| Lint issues | ↓ | 0 | 0 | · | 0 | · |
|   broken links | ↓ | 0 | 0 | · | 0 | · |
|   dead anchors | ↓ | 0 | 0 | · | 0 | · |
| Claims with coded evidence | ↑ | 130 | 130 | · | 274 | +144 ✓ |
| Claims with no coded evidence | ↓ | 304 | 448 | +144 ✗ | 304 | -144 ✓ |
| Claims with coded evidence, % | ↑ | 30.0 | 22.5 | -7.5 ✗ | 47.4 | +24.9 ✓ |
| Claims missing the evidence header line | ↓ | 0 | 144 | +144 ✗ | 0 | -144 ✓ |
| Claim citations with no [±~][SMW] marker | ↓ | 245 | 253 | +8 ✗ | 253 | · |
| Structured study records | ↑ | 9 | 19 | +10 ✓ | 19 | · |
| Observations in those records | ↑ | 36 | 107 | +71 ✓ | 107 | · |
| Sources ingested (manifest) | ↑ | 154 | 171 | +17 ✓ | 171 | · |
| Sources rejected (manifest) |  | 27 | 29 | +2 | 29 | · |
| Citation conflicts (one paper, 2+ DOIs) | ↓ | 64 | 64 | · | 64 | · |
| DOI collisions (one DOI, 2+ papers) | ↓ | 9 | 9 | · | 9 | · |
| Invented journal metadata | ↓ | 9 | 9 | · | 9 | · |
| Invented titles | ↓ | 100 | 100 | · | 100 | · |
| Near-duplicate titles (same folder) | ↓ | 908 | 914 | +6 ✗ | 914 | · |
| Cross-folder slug collisions needing judgment | ↓ | 69 | 69 | · | 69 | · |
| Pages at status: draft |  | 644 | 881 | +237 | 881 | · |
| Pages at status: draft, % | ↓ | 17.1 | 22.0 | +4.9 ✗ | 22.0 | · |
| Pages with unfilled TODOs | ↓ | 306 | 306 | · | 306 | · |
