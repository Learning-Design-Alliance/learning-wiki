---
type: claim
title: "Feasibility constraints reduce the estimated OTR value (3.260 to about 2.75) while producing realistic course placements, with Algebra II rising from 7% observed to 20% recommended"
description: "Feasibility constraints reduce the estimated OTR value (3.260 to about 2.75) while producing realistic course placements, with Algebra II rising from 7% observed to 20% recommended"
id: feasible-otr-value-feasibility-tradeoff
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
    rigour: 2
---

# Feasibility constraints reduce the estimated OTR value (3.260 to about 2.75) while producing realistic course placements, with Algebra II rising from 7% observed to 20% recommended

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A feasible OTR with a priori constraints and a propensity-score cutoff of 0.03 retains Algebra I, Geometry, and Algebra II as dominant courses, with Algebra II increasing from 7% observed to 20%, at an estimated value of 2.747 (SE = 0.0288); a stricter cutoff of 0.05 yields 2.746 (SE = 0.0290). [→ Chenguang Pan 2026](#chenguang-pan-2026)

## Evidence

### Chenguang Pan 2026

Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk. (2026). Estimating Optimal Dynamic Treatment Regimes for Personalized Education: A Tutorial and Applications with Machine Learning. [doi:10.48550/arXiv.2610.10843](https://doi.org/10.48550/arXiv.2610.10843)

`q2 · i?` · `associational · r2`

Single-decision OTR analysis of HSLS:09 data comparing feasible regimes under propensity-score cutoffs of 0.03 and 0.05. The lenient cutoff gave "an estimated value" of 2.747 (SE = 0.0288); the stricter cutoff shifted recommendations toward more conservative placements.

> "The corresponding estimated value is 2.747 (SE = 0.0288). Under the more stringent cutoff (0.05; bottom panel), recommendations shift toward more conservative placements, with increased allocations to Algebra I and Geometry and fewer recommendations to Algebra II."

## Discussion


## Related Claims
- [An unconstrained OTR recommends 82% of ninth graders to the highest-level math course, attaining an estimated value of 3.260 versus an observed mean of 2.609, but the recommendations are infeasible](unconstrained-otr-infeasible-high-value.md) — related
- [Feasibility-constrained ODTRs yield estimated values exceeding observed outcomes (cumulative weighted math GPA 2.826 vs 2.770; college enrollment probability 0.392 vs 0.369), with the college model recommending more calculus-related courses](feasible-odtr-exceeds-observed-outcomes.md) — related
- [Feasibility constraints raise empirical support rates for recommended course sequences (92.7% vs 53.7% for math achievement; 94.1% vs 56.2% for college enrollment) and expert-alignment rates (28.9% to 43.9%; 23.5% to 38.7%)](feasibility-constraints-improve-support-and-alignment.md) — related
