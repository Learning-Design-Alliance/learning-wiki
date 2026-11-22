---
type: claim
title: "An unconstrained OTR recommends 82% of ninth graders to the highest-level math course, attaining an estimated value of 3.260 versus an observed mean of 2.609, but the recommendations are infeasible"
description: "An unconstrained OTR recommends 82% of ninth graders to the highest-level math course, attaining an estimated value of 3.260 versus an observed mean of 2.609, but the recommendations are infeasible"
id: unconstrained-otr-infeasible-high-value
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

# An unconstrained OTR recommends 82% of ninth graders to the highest-level math course, attaining an estimated value of 3.260 versus an observed mean of 2.609, but the recommendations are infeasible

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Under a standard OTR without feasibility constraints, 82% of students are recommended the highest-level math course, with an estimated value of 3.260 (SE = 0.025) versus an observed mean of 2.609, but most ninth graders would be placed directly into Advanced Math by skipping mandatory courses. [→ Chenguang Pan 2026](#chenguang-pan-2026)

## Evidence

### Chenguang Pan 2026

Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk. (2026). Estimating Optimal Dynamic Treatment Regimes for Personalized Education: A Tutorial and Applications with Machine Learning. [doi:10.48550/arXiv.2610.10843](https://doi.org/10.48550/arXiv.2610.10843)

`q2 · i?` · `associational · r2`

Secondary analysis of HSLS:09 transcript data (12,640 students in 800 schools) estimating a single-decision OTR with TMLE and Super Learner. The unconstrained rule "attain[ed] the largest expected grade-9 math GPA" of 3.260 (SE = 0.025) versus the observed mean of 2.609.

> "These recommended course-taking plans attain the largest expected grade-9 math GPA (i.e., the value under OTR) of 3.260 with an SE of 0.025, which is notably higher than the observed mean of 2.609."

## Discussion


## Related Claims
- [Feasibility constraints reduce the estimated OTR value (3.260 to about 2.75) while producing realistic course placements, with Algebra II rising from 7% observed to 20% recommended](feasible-otr-value-feasibility-tradeoff.md) — related
- [Feasibility constraints raise empirical support rates for recommended course sequences (92.7% vs 53.7% for math achievement; 94.1% vs 56.2% for college enrollment) and expert-alignment rates (28.9% to 43.9%; 23.5% to 38.7%)](feasibility-constraints-improve-support-and-alignment.md) — related
- [Feasibility-constrained ODTRs yield estimated values exceeding observed outcomes (cumulative weighted math GPA 2.826 vs 2.770; college enrollment probability 0.392 vs 0.369), with the college model recommending more calculus-related courses](feasible-odtr-exceeds-observed-outcomes.md) — related
