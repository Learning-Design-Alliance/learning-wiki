---
type: claim
title: Problem instance variability strongly affects FIC/DK-P solvability
description: Problem instance variability strongly affects FIC/DK-P solvability
id: ficdkp-instance-dependency
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

# Problem instance variability strongly affects FIC/DK-P solvability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For the same dataset configuration (C = 400, K = 400, S = 10), different random-seed problem instances yield different fitness outcomes, indicating difficulty depends on both course catalog and student objective. [→ Lebis 2024](#lebis-2024)

## Evidence

### Lebis 2024

Lebis, A., Humeau, J., Fleury, A., Lucas, F., & Vermeulen, M. (2024). Fully Individualized Curriculum with Decaying Knowledge, a New Hard Problem: Investigation and Recommendations. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00376-9

`q2 · i?` · `design · r2`

Dependency study across 10 problem instances from the same configuration (C = 400, K = 400, S = 10, P = 4), each with 30 GA runs, presented in Fig. 5. Results confirm "solving FIC/DK-P seems to be strongly dependent on the problem instance."

> "solving FIC/DK-P seems to be strongly dependent on the problem instance. For the same data-set configuration, C = 400, K = 400, S = 10, we produce 10 different problem instances by changing the random seed and then performing for each one 30 different runs."

## Discussion


## Related Claims
- [FIC/DK-P exhibits combinatorial explosion making exact solving intractable beyond small problem sizes](ficdkp-exact-intractable-small-scale.md) — related
- [Increasing the number of courses per semester does not necessarily make FIC/DK-P easier to solve well](more-courses-not-easier-ficdkp.md) — related
- [A genetic algorithm can find near-faultless curricula for full-scale FIC/DK-P instances despite intractability of exact methods](ga-near-faultless-curricula-ficdkp.md) — related
- [Meeting the requisites of the student objective is the hardest constraint to satisfy in FIC/DK-P](objective-requisites-hardest-constraint.md) — related
