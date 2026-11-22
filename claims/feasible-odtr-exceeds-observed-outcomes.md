---
type: claim
title: Feasibility-constrained ODTRs yield estimated values exceeding observed outcomes (cumulative weighted math GPA 2.826 vs 2.770; college enrollment probability 0.392 vs 0.369), with the college model recommending more calculus-related courses
description: Feasibility-constrained ODTRs yield estimated values exceeding observed outcomes (cumulative weighted math GPA 2.826 vs 2.770; college enrollment probability 0.392 vs 0.369), with the college model recommending more c...
id: feasible-odtr-exceeds-observed-outcomes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: chenguang-pan-2026
    resource: "https://doi.org/10.48550/arXiv.2610.10843"
    title: "Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk. (2026). Estimating Optimal Dynamic Treatment Regimes for Personalized Education: A Tutorial and Applications with Machine Learning. [doi:10.48550/arXiv.2610.10843](https://doi.org/10.48550/arXiv.2610.10843)"
    author: Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk
    q: 2
    i: "?"
    kind: associational
    rigour: 3
  - id: chenguang-pan-2026-2
    resource: "https://doi.org/10.48550/arXiv.2610.10843"
    title: "Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk. (2026). Estimating Optimal Dynamic Treatment Regimes for Personalized Education: A Tutorial and Applications with Machine Learning. [doi:10.48550/arXiv.2610.10843](https://doi.org/10.48550/arXiv.2610.10843)"
    author: Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Feasibility-constrained ODTRs yield estimated values exceeding observed outcomes (cumulative weighted math GPA 2.826 vs 2.770; college enrollment probability 0.392 vs 0.369), with the college model recommending more calculus-related courses

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2`–`r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The feasible math achievement ODTR attains an estimated value of 2.826 (SE = 0.043) versus an observed mean cumulative weighted math GPA of 2.770, and the college enrollment model attains 0.392 (SE = 0.029) versus an observed rate of 0.369. [→ Chenguang Pan 2026](#chenguang-pan-2026)
`q2 i?` The college enrollment model recommends more calculus-related courses in Grades 11 and 12 than the math achievement model, described as important milestones for college preparation. [→ Chenguang Pan 2026 (2)](#chenguang-pan-2026-2)

## Evidence

### Chenguang Pan 2026

Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk. (2026). Estimating Optimal Dynamic Treatment Regimes for Personalized Education: A Tutorial and Applications with Machine Learning. [doi:10.48550/arXiv.2610.10843](https://doi.org/10.48550/arXiv.2610.10843)

`q2 · i?` · `associational · r3`

Multi-stage ODTR value estimation via longitudinal cross-validated TMLE on HSLS:09 data. The math model "attains an estimated value of 2.826 (SE = 0.043)" and the enrollment model 0.392 (SE = 0.029), both above observed values.

> "The math achievement model attains an estimated value of 2.826 (SE = 0.043) under the feasible ODTRs, which exceeds the observed mean cumulative weighted math GPA of 2.770. The college enrollment model attains an estimated probability of 0.392 (SE = 0.029), compared with an observed enrollment rate of 0.369 in the analytic sample."

### Chenguang Pan 2026 (2)

Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk. (2026). Estimating Optimal Dynamic Treatment Regimes for Personalized Education: A Tutorial and Applications with Machine Learning. [doi:10.48550/arXiv.2610.10843](https://doi.org/10.48550/arXiv.2610.10843)

`q2 · i?` · `associational · r2`

Figure 2 comparison of marginal course allocations across grades under the observed data and the two feasible ODTR models. The college enrollment model "recommends more calculus-related courses in Grades 11 and 12".

> "A key difference between the two models is that the college enrollment model recommends more calculus-related courses in Grades 11 and 12, which are important milestones for college preparation."

## Discussion


## Related Claims
- [Feasibility constraints raise empirical support rates for recommended course sequences (92.7% vs 53.7% for math achievement; 94.1% vs 56.2% for college enrollment) and expert-alignment rates (28.9% to 43.9%; 23.5% to 38.7%)](feasibility-constraints-improve-support-and-alignment.md) — related
- [Feasibility constraints reduce the estimated OTR value (3.260 to about 2.75) while producing realistic course placements, with Algebra II rising from 7% observed to 20% recommended](feasible-otr-value-feasibility-tradeoff.md) — related
- [An unconstrained OTR recommends 82% of ninth graders to the highest-level math course, attaining an estimated value of 3.260 versus an observed mean of 2.609, but the recommendations are infeasible](unconstrained-otr-infeasible-high-value.md) — related
