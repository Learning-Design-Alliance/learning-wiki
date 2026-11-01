---
type: claim
title: On the ASSISTments experiment, RCN has lower policy risk than the Treated-All and Not-Treated policies and CFR, and lower ATT error than CFR
description: On the ASSISTments experiment, RCN has lower policy risk than the Treated-All and Not-Treated policies and CFR, and lower ATT error than CFR
id: rcn-outperforms-ta-nt-cfr-assistments
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
newest_evidence: 2016
source_checked: 2026-11-01
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

# On the ASSISTments experiment, RCN has lower policy risk than the Treated-All and Not-Treated policies and CFR, and lower ATT error than CFR

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · checked against its sources 2026-11-01 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` RCN achieves lower policy risk (0.08) than TA (0.14), NT (0.27) and CFR (0.14), and lower ATT error (0.03) than CFR (0.08) on the ASSISTments dataset. [→ Siyuan Zhao and Neil Heffernan 2016](#siyuan-zhao-and-neil-heffernan-2016)

## Evidence

### Siyuan Zhao and Neil Heffernan 2016

Siyuan Zhao and Neil Heffernan. (2016). Estimating Individual Treatment Effect from Educational Studies with Residual Counterfactual Networks. Proceedings of the 10th International Conference on Educational Data Mining. https://eric.ed.gov/?id=ED596589

`q2 · i?` · `design · r2`

Results on the real-world ASSISTments randomized experiment (Table 3, lambda = 0): RCN RPOL 0.08 and epsilon ATT 0.03 versus CFR RPOL 0.14 and epsilon ATT 0.08; TA RPOL 0.14 and NT RPOL 0.27 (no ATT error is reported for TA or NT, so the ATT comparison is with CFR only). The article reports "the RCN performs better than the CFR does in terms of risk policy and ATT".

> "The comparison between the CFR and the RCN suggests that the RCN performs better than the CFR does in terms of risk policy and ATT."

## Discussion


## Related Claims
- [Taking individual treatment effects into account yields better intervention choices than a single uniform assignment](individual-effect-better-intervention-choice.md) — possibly the same claim (merge candidate)
- [Policy risk enables model comparison on real experiments where ground-truth ITE is unavailable](policy-risk-evaluation-without-ground-truth-ite.md) — a broader claim this one bears on
- [RCN performs the best among compared models on the IHDP dataset for estimating ITE, ATE and PEHE](rcn-best-ihdp-ite-ate-pehe.md) — related
- [On real ASSISTments data, TAME and ANOVA agree on which experiments show significant treatment effects](tame-anova-agreement-real-assistments-data.md) — related
