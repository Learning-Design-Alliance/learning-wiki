---
type: claim
title: FIC/DK-P exhibits combinatorial explosion making exact solving intractable beyond small problem sizes
description: FIC/DK-P exhibits combinatorial explosion making exact solving intractable beyond small problem sizes
id: ficdkp-exact-intractable-small-scale
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: lebis-2024
    resource: "https://doi.org/10.1007/s40593-023-00376-9"
    title: "Lebis, A., Humeau, J., Fleury, A., Lucas, F., & Vermeulen, M. (2024). Fully Individualized Curriculum with Decaying Knowledge, a New Hard Problem: Investigation and Recommendations. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00376-9"
    author: "Lebis, A., Humeau, J., Fleury, A., Lucas, F., & Vermeulen, M."
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# FIC/DK-P exhibits combinatorial explosion making exact solving intractable beyond small problem sizes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Exact constraint-based solving of FIC/DK-P becomes generally not tractable in reasonable time as the pool of available courses per semester increases, with course-per-semester count S and number of academic terms T having strong effects on difficulty. [→ Lebis 2024](#lebis-2024)

## Evidence

### Lebis 2024

Lebis, A., Humeau, J., Fleury, A., Lucas, F., & Vermeulen, M. (2024). Fully Individualized Curriculum with Decaying Knowledge, a New Hard Problem: Investigation and Recommendations. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00376-9

`q2 · i?` · `theoretical · r3`

Exact solving experiment using two Prolog constraint-based solvers on reduced simulated datasets (C ∈ [24;100], K ∈ {10;20;30}, S ∈ {2;3}), with a 12-hour time limit per instance. Results show combinatorial explosion: "around N = 15, FIC/DK-P becomes generally not tractable in a reasonable time."

> "we quickly observe a combinatorial explosion: around N = 15, FIC/DK-P becomes generally not tractable in a reasonable time."

## Discussion


## Related Claims
- [A genetic algorithm can find near-faultless curricula for full-scale FIC/DK-P instances despite intractability of exact methods](ga-near-faultless-curricula-ficdkp.md) — related
- [Increasing the number of courses per semester does not necessarily make FIC/DK-P easier to solve well](more-courses-not-easier-ficdkp.md) — related
- [Problem instance variability strongly affects FIC/DK-P solvability](ficdkp-instance-dependency.md) — related
- [Using decay prediction as a search heuristic improves computational efficiency of exact solving over full evaluation](decay-heuristic-improves-solver-efficiency.md) — related
