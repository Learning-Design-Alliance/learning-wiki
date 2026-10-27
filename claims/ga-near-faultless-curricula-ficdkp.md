---
type: claim
title: A genetic algorithm can find near-faultless curricula for full-scale FIC/DK-P instances despite intractability of exact methods
description: A genetic algorithm can find near-faultless curricula for full-scale FIC/DK-P instances despite intractability of exact methods
id: ga-near-faultless-curricula-ficdkp
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

# A genetic algorithm can find near-faultless curricula for full-scale FIC/DK-P instances despite intractability of exact methods

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A genetic algorithm across 124740 runs always obtained better solutions than the initial pseudo-randomized population, in some cases approaching full constraint satisfaction with f ≈ 0.1. [→ Lebis 2024](#lebis-2024)

## Evidence

### Lebis 2024

Lebis, A., Humeau, J., Fleury, A., Lucas, F., & Vermeulen, M. (2024). Fully Individualized Curriculum with Decaying Knowledge, a New Hard Problem: Investigation and Recommendations. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00376-9

`q2 · i?` · `design · r2`

Metaheuristic experiment using a GA implemented in C++ with the Paradiseo library across 124740 simulated FIC/DK-P instances on a cluster. "we always obtained better solutions than the initial, pseudo-randomized, population," with some cases reaching f ≈ 0.1.

> "Fitness-wise, considering the entirety of the experiments we conduct, we always obtained better solutions than the initial, pseudo-randomized, population, as presented in Fig. 6. In some cases, we were even close to fully solving FIC/DK-P , with f ≈ 0.1."

## Discussion


## Related Claims
- [Knowledge decay can be compensated with a thoughtful sequence of courses](decay-compensated-by-sequencing.md) — related
- [FIC/DK-P exhibits combinatorial explosion making exact solving intractable beyond small problem sizes](ficdkp-exact-intractable-small-scale.md) — related
- [Problem instance variability strongly affects FIC/DK-P solvability](ficdkp-instance-dependency.md) — related
- [Meeting the requisites of the student objective is the hardest constraint to satisfy in FIC/DK-P](objective-requisites-hardest-constraint.md) — related
- [Increasing the number of courses per semester does not necessarily make FIC/DK-P easier to solve well](more-courses-not-easier-ficdkp.md) — related
