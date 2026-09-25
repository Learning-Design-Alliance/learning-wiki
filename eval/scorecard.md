Measured with today's `scripts/` against each tree (see scripts/health_scorecard.py). Δ is against the column to its left; ✓/✗ says whether it moved the better way.

`origin/main` = `b70c9737a` · `HEAD` = `a462635fa`

| metric | better | main | batches 1-2 | Δ | batch 3 | Δ |
|---|---|---:|---:|---:|---:|---:|
| Content pages |  | 4,002 | 4,642 | +640 | 4,844 | +202 |
| Claim pages |  | 578 | 901 | +323 | 1,004 | +103 |
| Lint issues | ↓ | 0 | 0 | · | 0 | · |
|   broken links | ↓ | 0 | 0 | · | 0 | · |
|   dead anchors | ↓ | 0 | 0 | · | 0 | · |
| Claims with coded evidence | ↑ | 274 | 597 | +323 ✓ | 700 | +103 ✓ |
| Claims with no coded evidence | ↓ | 304 | 304 | · | 304 | · |
| Claims with coded evidence, % | ↑ | 47.4 | 66.3 | +18.9 ✓ | 69.7 | +3.4 ✓ |
| Claims missing the evidence header line | ↓ | 0 | 0 | · | 0 | · |
| Claim citations with no [±~][SMW] marker | ↓ | 253 | 253 | · | 253 | · |
| Structured study records | ↑ | 19 | 19 | · | 19 | · |
| Observations in those records | ↑ | 107 | 107 | · | 107 | · |
| Sources ingested (manifest) | ↑ | 171 | 267 | +96 ✓ | 297 | +30 ✓ |
| Sources rejected (manifest) |  | 29 | 43 | +14 | 45 | +2 |
| Citation conflicts (one paper, 2+ DOIs) | ↓ | 64 | 64 | · | 64 | · |
| DOI collisions (one DOI, 2+ papers) | ↓ | 9 | 9 | · | 9 | · |
| Invented journal metadata | ↓ | 9 | 9 | · | 9 | · |
| Invented titles | ↓ | 100 | 100 | · | 100 | · |
| Near-duplicate titles (same folder) | ↓ | 914 | 916 | +2 ✗ | 916 | · |
| Cross-folder slug collisions needing judgment | ↓ | 69 | 69 | · | 69 | · |
| Pages at status: draft |  | 881 | 1,521 | +640 | 1,723 | +202 |
| Pages at status: draft, % | ↓ | 22.0 | 32.8 | +10.8 ✗ | 35.6 | +2.8 ✗ |
| Pages with unfilled TODOs | ↓ | 306 | 306 | · | 306 | · |
