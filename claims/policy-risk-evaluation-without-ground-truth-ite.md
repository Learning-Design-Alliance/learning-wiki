---
type: claim
title: Policy risk enables model comparison on real experiments where ground-truth ITE is unavailable
description: Policy risk enables model comparison on real experiments where ground-truth ITE is unavailable
id: policy-risk-evaluation-without-ground-truth-ite
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: weak
newest_evidence: 2016
recheck_by: 2019
sources:
  - id: siyuan-zhao-and-neil-heffernan-2016
    resource: "https://eric.ed.gov/?id=ED596589"
    title: "Siyuan Zhao and Neil Heffernan. (2016). Estimating Individual Treatment Effect from Educational Studies with Residual Counterfactual Networks. Proceedings of the 10th International Conference on Educational Data Mining. https://eric.ed.gov/?id=ED596589"
    author: Siyuan Zhao and Neil Heffernan
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Policy risk enables model comparison on real experiments where ground-truth ITE is unavailable

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Because counterfactual outcomes cannot be gathered from RCTs or observational studies, epsilon ITE and PEHE cannot be computed on real datasets, so policy risk is used instead. [→ Siyuan Zhao and Neil Heffernan 2016](#siyuan-zhao-and-neil-heffernan-2016)

## Evidence

### Siyuan Zhao and Neil Heffernan 2016

Siyuan Zhao and Neil Heffernan. (2016). Estimating Individual Treatment Effect from Educational Studies with Residual Counterfactual Networks. Proceedings of the 10th International Conference on Educational Data Mining. https://eric.ed.gov/?id=ED596589

`q1 · i?` · `design · r2`

Methodological statement in the Experiments section: ground-truth ITE is unobservable, so the authors adopt the policy risk measure (following prior work), computed on the subset of participants whose model recommendation matches the experimental treatment assignment.

> "We cannot gather the counterfactual outcomes from RCTs and observational studies, and thus do not have the ITE of each participant. We cannot evaluate ϵIT E and PEHE on these datasets."

## Discussion


## Related Claims
- [RCN performs the best among compared models on the IHDP dataset for estimating ITE, ATE and PEHE](rcn-best-ihdp-ite-ate-pehe.md) — related
- [On the ASSISTments experiment, RCN has lower policy risk than the Treated-All and Not-Treated policies and CFR, and lower ATT error than CFR](rcn-outperforms-ta-nt-cfr-assistments.md) — a narrower finding that bears on this claim
