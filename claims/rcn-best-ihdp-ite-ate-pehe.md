---
type: claim
title: RCN performs the best among compared models on the IHDP dataset for estimating ITE, ATE and PEHE
description: RCN performs the best among compared models on the IHDP dataset for estimating ITE, ATE and PEHE
id: rcn-best-ihdp-ite-ate-pehe
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
newest_evidence: 2016
recheck_by: 2019
sources:
  - id: siyuan-zhao-and-neil-heffernan-2016
    resource: "https://eric.ed.gov/?id=ED596589"
    title: "Siyuan Zhao and Neil Heffernan. (2016). Estimating Individual Treatment Effect from Educational Studies with Residual Counterfactual Networks. Proceedings of the 10th International Conference on Educational Data Mining. https://eric.ed.gov/?id=ED596589"
    author: Siyuan Zhao and Neil Heffernan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# RCN performs the best among compared models on the IHDP dataset for estimating ITE, ATE and PEHE

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the IHDP semi-simulated dataset, RCN achieves the lowest epsilon ITE (1.1), epsilon ATE (0.05) and PEHE (1.4) compared with NN-4, BNN-2-2 and CFR. [→ Siyuan Zhao and Neil Heffernan 2016](#siyuan-zhao-and-neil-heffernan-2016)

## Evidence

### Siyuan Zhao and Neil Heffernan 2016

Siyuan Zhao and Neil Heffernan. (2016). Estimating Individual Treatment Effect from Educational Studies with Residual Counterfactual Networks. Proceedings of the 10th International Conference on Educational Data Mining. https://eric.ed.gov/?id=ED596589

`q2 · i?` · `design · r2`

Numerical comparison in the Results section using Table 2 values at treatment threshold lambda = 0: RCN epsilon ITE 1.1, epsilon ATE 0.05, PEHE 1.4, versus CFR 1.4, 0.2, 1.6. The article reports an especially large improvement on estimating ITE.

> "These results indicate that the residual block ∆f(x) helps accurately predict the value of ITE based on the feature representation Φ(x) for a given participantx."

## Discussion


## Related Claims
- [Taking individual treatment effects into account yields better intervention choices than a single uniform assignment](individual-effect-better-intervention-choice.md) — related
- [Policy risk enables model comparison on real experiments where ground-truth ITE is unavailable](policy-risk-evaluation-without-ground-truth-ite.md) — related
- [On the ASSISTments experiment, RCN has lower policy risk than the Treated-All and Not-Treated policies and CFR, and lower ATT error than CFR](rcn-outperforms-ta-nt-cfr-assistments.md) — related
