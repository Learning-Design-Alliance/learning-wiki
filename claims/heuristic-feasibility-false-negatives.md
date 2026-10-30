---
type: claim
title: The heuristic feasibility estimation used during planning can produce false negatives by overestimating displacement time
description: The heuristic feasibility estimation used during planning can produce false negatives by overestimating displacement time
id: heuristic-feasibility-false-negatives
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: noemi-mauro-2024
    resource: "https://doi.org/10.1007/s40593-023-00366-x"
    title: "Noemi Mauro, Liliana Ardissono, Federica Cena, Livio Scarpinati, Gianluca Torta. (2024). An Intelligent Support System to Help Teachers Plan Field Trips. Int J Artif Intell Educ 34, 793–824. https://doi.org/10.1007/s40593-023-00366-x"
    author: Noemi Mauro, Liliana Ardissono, Federica Cena, Livio Scarpinati, Gianluca Torta
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The heuristic feasibility estimation used during planning can produce false negatives by overestimating displacement time

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Because the heuristic does not optimize the revised itinerary's schedule, it may overestimate the displacement time needed to accommodate an item, producing false negatives. [→ Noemi Mauro 2024](#noemi-mauro-2024)

## Evidence

### Noemi Mauro 2024

Noemi Mauro, Liliana Ardissono, Federica Cena, Livio Scarpinati, Gianluca Torta. (2024). An Intelligent Support System to Help Teachers Plan Field Trips. Int J Artif Intell Educ 34, 793–824. https://doi.org/10.1007/s40593-023-00366-x

`q1 · i?` · `design · r2`

Analytical description of the heuristic feasibility procedure (type a/d), which estimates T*NEXT = TNOW + t(item) + 2 × td(i,j) and marks an item green only if T*NEXT ≤ TMAX; the article states the approach "might generate some false negatives".

> "This approach might generate some false negatives because it does not optimize the schedule of the revised itinerary; therefore, it might overestimate the displacement time needed to accommodate item into the itinerary."

## Discussion


## Related Claims
- [People overestimate how much mental effort AI assistance alleviates (offloading illusion), driven by overestimating the effort of independent completion while AI-assisted effort is accurately estimated](offloading-illusion-ai-effort-savings.md) — related
- [Participants more averse to thinking are more susceptible to the speedup illusion; AI familiarity measures do not predict calibration error](thinking-aversion-predicts-speedup-illusion.md) — related
