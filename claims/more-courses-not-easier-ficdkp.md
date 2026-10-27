---
type: claim
title: Increasing the number of courses per semester does not necessarily make FIC/DK-P easier to solve well
description: Increasing the number of courses per semester does not necessarily make FIC/DK-P easier to solve well
id: more-courses-not-easier-ficdkp
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

# Increasing the number of courses per semester does not necessarily make FIC/DK-P easier to solve well

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` While larger S improves initial-population fitness, this intuition does not hold for final populations; greater S in a highly diversified catalog can produce worse solutions than more constrained course loads. [→ Lebis 2024](#lebis-2024)

## Evidence

### Lebis 2024

Lebis, A., Humeau, J., Fleury, A., Lucas, F., & Vermeulen, M. (2024). Fully Individualized Curriculum with Decaying Knowledge, a New Hard Problem: Investigation and Recommendations. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-023-00376-9

`q2 · i?` · `design · r2`

Analysis across configurations varying S (courses per semester) shown in Fig. 7. The intuition that more courses per semester reinforces qualification holds for initial populations but "this intuition does not stand while observing the ﬁnal populations," with greater S sometimes yielding worse solutions.

> "the overall trend of the ﬁtness decreases as S increases. Y et, this intuition does not stand while observing the ﬁnal populations."

## Discussion


## Related Claims
- [Knowledge decay can be compensated with a thoughtful sequence of courses](decay-compensated-by-sequencing.md) — related
- [FIC/DK-P exhibits combinatorial explosion making exact solving intractable beyond small problem sizes](ficdkp-exact-intractable-small-scale.md) — related
- [Problem instance variability strongly affects FIC/DK-P solvability](ficdkp-instance-dependency.md) — related
- [A genetic algorithm can find near-faultless curricula for full-scale FIC/DK-P instances despite intractability of exact methods](ga-near-faultless-curricula-ficdkp.md) — related
