Measured with today's `scripts/` against each tree (see scripts/health_scorecard.py). Δ is against the column to its left; ✓/✗ says whether it moved the better way.

`d62f4f6a0~1` = `b70c9737a` · `origin/main` = `29723b1db` · `e93f1f46f` = `e93f1f46f` · `HEAD` = `daa6cfed2`

| metric | better | before batches | batches 1-3 | Δ | batch 4 | Δ | DOI sweep + gap-fill | Δ |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Content pages |  | 4,002 | 4,844 | +842 | 5,398 | +554 | 5,398 | · |
| Claim pages |  | 578 | 1,004 | +426 | 1,323 | +319 | 1,323 | · |
| Lint issues | ↓ | 0 | 0 | · | 0 | · | 0 | · |
|   broken links | ↓ | 0 | 0 | · | 0 | · | 0 | · |
|   dead anchors | ↓ | 0 | 0 | · | 0 | · | 0 | · |
| Claims with coded evidence | ↑ | 274 | 700 | +426 ✓ | 1,019 | +319 ✓ | 1,024 | +5 ✓ |
| Claims with no coded evidence | ↓ | 304 | 304 | · | 304 | · | 299 | -5 ✓ |
| Claims with coded evidence, % | ↑ | 47.4 | 69.7 | +22.3 ✓ | 77.0 | +7.3 ✓ | 77.4 | +0.4 ✓ |
| Claims missing the evidence header line | ↓ | 0 | 0 | · | 0 | · | 0 | · |
| Claim citations with no [±~][SMW] marker | ↓ | 253 | 253 | · | 253 | · | 253 | · |
| Structured study records | ↑ | 19 | 19 | · | 19 | · | 19 | · |
| Observations in those records | ↑ | 107 | 107 | · | 107 | · | 107 | · |
| Sources ingested (manifest) | ↑ | 171 | 297 | +126 ✓ | 370 | +73 ✓ | 370 | · |
| Sources rejected (manifest) |  | 29 | 45 | +16 | 50 | +5 | 50 | · |
| Citation conflicts (one paper, 2+ DOIs) | ↓ | 64 | 64 | · | 53 | -11 ✓ | 44 | -9 ✓ |
| DOI collisions (one DOI, 2+ papers) | ↓ | 9 | 9 | · | 9 | · | 9 | · |
| Invented journal metadata | ↓ | 9 | 9 | · | 8 | -1 ✓ | 8 | · |
| Invented titles | ↓ | 100 | 100 | · | 99 | -1 ✓ | 99 | · |
| DOIs whose majority citation contradicts the DOI | ↓ | 2 | 2 | · | 1 | -1 ✓ | 1 | · |
| Distinct DOIs resolved against Crossref |  | 2,370 | 2,375 | +5 | 2,360 | -15 | 2,216 | -144 |
|   DOIs Crossref has no record of | ↓ | 137 | 138 | +1 ✗ | 107 | -31 ✓ | 5 | -102 ✓ |
|   DOIs resolving to a different title | ↓ | 130 | 131 | +1 ✗ | 131 | · | 85 | -46 ✓ |
|   DOI lookups that failed (not a verdict) | ↓ | 0 | 0 | · | 0 | · | 0 | · |
| Near-duplicate titles (same folder) | ↓ | 914 | 916 | +2 ✗ | 919 | +3 ✗ | 919 | · |
| Cross-folder slug collisions needing judgment | ↓ | 69 | 69 | · | 69 | · | 69 | · |
| Pages at status: draft |  | 881 | 1,723 | +842 | 2,277 | +554 | 2,277 | · |
| Pages at status: draft, % | ↓ | 22.0 | 35.6 | +13.6 ✗ | 42.2 | +6.6 ✗ | 42.2 | · |
| Pages with unfilled TODOs | ↓ | 306 | 306 | · | 306 | · | 302 | -4 ✓ |
| Incomplete pages (draft or TODO; the dashboard tile) | ↓ | 885 | 1,727 | +842 ✗ | 2,281 | +554 ✗ | 2,281 | · |
