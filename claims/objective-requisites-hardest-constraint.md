---
type: claim
title: Meeting the requisites of the student objective is the hardest constraint to satisfy in FIC/DK-P
description: Meeting the requisites of the student objective is the hardest constraint to satisfy in FIC/DK-P
id: objective-requisites-hardest-constraint
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

# Meeting the requisites of the student objective is the hardest constraint to satisfy in FIC/DK-P

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The fitness metric ν2 (mastery lacking to match objective requisites) shows the poorest performance, with more than 70% of initial-population individuals at zero and only about 19% of final-population individuals at zero. [→ Lebis 2024](#lebis-2024)

## Evidence

### Lebis 2024

Lebis, A., Humeau, J., Fleury, A., Lucas, F., & Vermeulen, M. (2024). Fully Individualized Curriculum with Decaying Knowledge, a New Hard Problem: Investigation and Recommendations. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00376-9

`q2 · i?` · `design · r2`

Cumulative distribution analysis of the four fitness metrics across GA runs (Fig. 8). The ν2 metric shows "more than 70% of the individuals are such that ν2 = 0" in the initial population, improving to "no more than about 19%" after optimization.

> "the initial population performed very poorly: more than 70% of the individuals are such that ν2 = 0. The final population shows a significant improvement, where no more than about 19% of the individuals obtain zero to the metric – which is still not ideal for real-life context scenarios."

## Discussion


## Related Claims
- [Knowledge decay can be compensated with a thoughtful sequence of courses](decay-compensated-by-sequencing.md) — related
- [A genetic algorithm can find near-faultless curricula for full-scale FIC/DK-P instances despite intractability of exact methods](ga-near-faultless-curricula-ficdkp.md) — related
- [Problem instance variability strongly affects FIC/DK-P solvability](ficdkp-instance-dependency.md) — related
- [Rating-based relevance is the most popular target metric in educational recommender systems, with only 12 of 28 reviewed papers optimizing learning-centered metrics](ers-rating-relevance-dominant-target-metric.md) — related
