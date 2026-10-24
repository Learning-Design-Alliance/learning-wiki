---
type: claim
title: "TSDR is robust to the smoothness coefficient, with a stable sweet spot for lambda in [0.3, 1.0]"
description: "TSDR is robust to the smoothness coefficient, with a stable sweet spot for lambda in [0.3, 1.0]"
id: tsdr-lambda-sweet-spot-robustness
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: peilin-zhan-2026
    resource: "https://doi.org/10.48550/arxiv.2605.05958"
    title: "Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958 [doi:10.48550/arxiv.2605.05958](https://doi.org/10.48550/arxiv.2605.05958)"
    author: Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# TSDR is robust to the smoothness coefficient, with a stable sweet spot for lambda in [0.3, 1.0]

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the Prob dataset, temporal smoothness outperforms vanilla DR (lambda = 0) within an appropriate range, with a stable sweet spot generally in lambda in [0.3, 1.0]. [→ Peilin Zhan 2026](#peilin-zhan-2026)

## Evidence

### Peilin Zhan 2026

Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958 [doi:10.48550/arxiv.2605.05958](https://doi.org/10.48550/arxiv.2605.05958)

`q2 · i?` · `design · r2`

Sensitivity analysis (RQ3, Figure 4) varying lambda over {0, 0.1, 0.3, 0.5, 0.7, 1, 2} on the Prob dataset across six backbones, measuring AUC and ACC. The article reports "a stable “sweet spot” generally inλ∈[0.3,1.0]."

> "The method exhibits strong robustness, achieving a stable “sweet spot” generally inλ∈[0.3,1.0]."

## Discussion


## Related Claims
- [TSDR's AUC gains are largest on open-ended platforms and limited on EdNet, whose mandatory bundle completion policy constrains selection bias](tsdr-gain-magnitude-depends-on-collection-mechanism.md) — related
- [TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets](tsdr-improves-kt-backbone-auc-benchmarks.md) — a broader claim this one bears on
- [In ablations, temporal smoothness works best on the imputation branch, and the full TSDR variant achieves the best AUC and ACC on all six backbones](tsdr-ablation-smoothness-on-imputation-branch.md) — related
- [Under controlled synthetic MNAR bias, TSDR-equipped models improve across the entire bias spectrum, with the RMSE advantage diminishing beyond gamma > 0.8](tsdr-robust-across-mnar-spectrum.md) — related
