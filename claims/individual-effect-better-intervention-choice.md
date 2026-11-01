---
type: claim
title: Taking individual treatment effects into account yields better intervention choices than a single uniform assignment
description: Taking individual treatment effects into account yields better intervention choices than a single uniform assignment
id: individual-effect-better-intervention-choice
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
newest_evidence: 2016
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

# Taking individual treatment effects into account yields better intervention choices than a single uniform assignment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On the ASSISTments data, the model that considers individual treatment effects (RCN) outperforms both uniform policies of treating all students (TA) or none (NT). [→ Siyuan Zhao and Neil Heffernan 2016](#siyuan-zhao-and-neil-heffernan-2016)

## Evidence

### Siyuan Zhao and Neil Heffernan 2016

Siyuan Zhao and Neil Heffernan. (2016). Estimating Individual Treatment Effect from Educational Studies with Residual Counterfactual Networks. Proceedings of the 10th International Conference on Educational Data Mining. https://eric.ed.gov/?id=ED596589

`q2 · i?` · `design · r2`

Results-section comparison on the ASSISTments dataset: RCN (RPOL 0.08) versus TA (RPOL 0.14) and NT (RPOL 0.27). The authors interpret that "taking the individual eﬀect into account helps make a better choice of interventions".

> "This indicates that taking the individual eﬀect into account helps make a better choice of interventions."

## Discussion


## Related Claims
- [On the ASSISTments experiment, RCN outperforms the Treated-All and Not-Treated policies and CFR on policy risk and ATT error](rcn-outperforms-ta-nt-cfr-assistments.md) — possibly the same claim (merge candidate)
- [RITA outperforms an RCT-derived ATE baseline in simulated worlds with heterogeneous treatment effects](rita-outperforms-rct-baseline-under-heterogeneity.md) — related
- [RCN performs the best among compared models on the IHDP dataset for estimating ITE, ATE and PEHE](rcn-best-ihdp-ite-ate-pehe.md) — related
- [The baseline RCT-derived ATE model outperforms RITA when no heterogeneity exists and one intervention is uniformly more effective](baseline-outperforms-rita-no-heterogeneity.md) — reports the opposite
