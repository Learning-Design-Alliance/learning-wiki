---
type: claim
title: "Optimal AI allocation concentrates resources on components above a common residual-gap threshold, yielding over 14% greater gain than proportional allocation"
description: "Optimal AI allocation concentrates resources on components above a common residual-gap threshold, yielding over 14% greater gain than proportional allocation"
id: optimal-ai-allocation-exceeds-proportional
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: bo-yuan-and-jiazi-hu-2025
    resource: "https://doi.org/10.48550/arXiv.2507.14266"
    title: "Bo Yuan and Jiazi Hu. (2025). Bridging MOOCs, Smart Teaching, and AI-Assisted Learning: A Unified Quantitative Model. Originally published 2024. [doi:10.48550/arXiv.2507.14266](https://doi.org/10.48550/arXiv.2507.14266)"
    author: Bo Yuan and Jiazi Hu
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
  - id: bo-yuan-and-jiazi-hu-2025-2
    resource: "https://doi.org/10.48550/arXiv.2507.14266"
    title: "Bo Yuan and Jiazi Hu. (2025). Bridging MOOCs, Smart Teaching, and AI-Assisted Learning: A Unified Quantitative Model. Originally published 2024. [doi:10.48550/arXiv.2507.14266](https://doi.org/10.48550/arXiv.2507.14266)"
    author: Bo Yuan and Jiazi Hu
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
---

# Optimal AI allocation concentrates resources on components above a common residual-gap threshold, yielding over 14% greater gain than proportional allocation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · theoretical `r3` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Under the model's assumptions, the unique globally optimal AI allocation equalizes residual mastery gaps of supported components and assigns zero resources to components below a threshold. [→ Bo Yuan and Jiazi Hu 2025](#bo-yuan-and-jiazi-hu-2025)
`q1 i?` In a controlled single-student comparison, optimal allocation yields 0.0985 average mastery increment versus 0.0864 under proportional allocation, a relative improvement of over 14%. [→ Bo Yuan and Jiazi Hu 2025 (2)](#bo-yuan-and-jiazi-hu-2025-2)

## Evidence

### Bo Yuan and Jiazi Hu 2025

Bo Yuan and Jiazi Hu. (2025). Bridging MOOCs, Smart Teaching, and AI-Assisted Learning: A Unified Quantitative Model. Originally published 2024. [doi:10.48550/arXiv.2507.14266](https://doi.org/10.48550/arXiv.2507.14266)

`q1 · i?` · `theoretical · r3`

Analytical derivation under the model's assumptions (Section VI-B). KKT conditions establish that "the allocation satisfying the KKT conditions is the unique global optimum," with all supported components reaching the same residual mastery gap.

> "Its Hessian is negative definite, making the objective strictly concave. Since the feasible set is convex, the allocation satisfying the KKT conditions is the unique global optimum"

### Bo Yuan and Jiazi Hu 2025 (2)

Bo Yuan and Jiazi Hu. (2025). Bridging MOOCs, Smart Teaching, and AI-Assisted Learning: A Unified Quantitative Model. Originally published 2024. [doi:10.48550/arXiv.2507.14266](https://doi.org/10.48550/arXiv.2507.14266)

`q1 · i?` · `theoretical · r3`

Controlled single-student numerical comparison with d=10 components, receptivity 0.8, and AI budget 2 (Fig. 6). "The average mastery increment is 0.0864 under proportional allocation and 0.0985 under optimal allocation."

> "The average mastery increment is 0.0864 under proportional allocation and 0.0985 under optimal allocation, corresponding to an absolute increase of 0.0121 and a relative improvement of over 14%"

## Discussion


## Related Claims
- [Additional AI-assisted learning budget yields diminishing returns in final mastery](diminishing-returns-ai-budget.md) — related
- [Knowledge-tracing mastery decisions are more equitable than fixed practice but can still under-serve some students when the learner model is fit to the aggregate population or makes wrong assumptions](knowledge-tracing-equity-depends-on-model-accuracy.md) — related
- [Smart Teaching allocation jointly reflects class-level knowledge gaps and predefined course-content emphasis](st-allocation-balances-gaps-and-emphasis.md) — related
