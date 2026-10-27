---
type: claim
title: Using decay prediction as a search heuristic improves computational efficiency of exact solving over full evaluation
description: Using decay prediction as a search heuristic improves computational efficiency of exact solving over full evaluation
id: decay-heuristic-improves-solver-efficiency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: lebis-2024
    resource: "https://doi.org/10.1007/s40593-023-00376-9"
    title: "Lebis, A., Humeau, J., Fleury, A., Lucas, F., & Vermeulen, M. (2024). Fully Individualized Curriculum with Decaying Knowledge, a New Hard Problem: Investigation and Recommendations. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00376-9"
    author: "Lebis, A., Humeau, J., Fleury, A., Lucas, F., & Vermeulen, M."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Using decay prediction as a search heuristic improves computational efficiency of exact solving over full evaluation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A solver that prioritizes courses maintaining student mastery above expected levels under decay (Solver 2) requires fewer logical inferences and solves more instances than a full exact solver (Solver 1). [→ Lebis 2024](#lebis-2024)

## Evidence

### Lebis 2024

Lebis, A., Humeau, J., Fleury, A., Lucas, F., & Vermeulen, M. (2024). Fully Individualized Curriculum with Decaying Knowledge, a New Hard Problem: Investigation and Recommendations. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00376-9

`q2 · i?` · `design · r2`

Comparison of two Prolog-based solvers across simulated FIC/DK-P instances measured in logical inferences (LI). Solver 2 uses decay prediction as a course-selection heuristic; "we obtain better results in terms of computation time for all the observed cases with Solver 2."

> "regarding the LI made, we obtain better results in terms of computation time for all the observed cases with Solver 2 which uses the decay as a selection heuristic than Solver 1."

## Discussion


## Related Claims
- [FIC/DK-P exhibits combinatorial explosion making exact solving intractable beyond small problem sizes](ficdkp-exact-intractable-small-scale.md) — related
