---
type: claim
title: In ablations, temporal smoothness works best on the imputation branch, and the full TSDR variant achieves the best AUC and ACC on all six backbones
description: In ablations, temporal smoothness works best on the imputation branch, and the full TSDR variant achieves the best AUC and ACC on all six backbones
id: tsdr-ablation-smoothness-on-imputation-branch
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: peilin-zhan-2026
    resource: "https://doi.org/10.48550/arxiv.2605.05958"
    title: "Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958 [doi:10.48550/arxiv.2605.05958](https://doi.org/10.48550/arxiv.2605.05958)"
    author: Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: peilin-zhan-2026-2
    resource: "https://arxiv.org/abs/2605.05958"
    title: "Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958"
    author: Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In ablations, temporal smoothness works best on the imputation branch, and the full TSDR variant achieves the best AUC and ACC on all six backbones

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` Applying temporal smoothness to the imputation branch consistently achieves the best or near-best results across backbones, whereas imposing it on the KT backbone often leads to inferior performance. [→ Peilin Zhan 2026](#peilin-zhan-2026)
`q2 i?` The full variant (DR with joint learning and temporal smoothness on the imputation branch) obtains the best AUC and ACC on all six backbones, verifying the design is backbone-agnostic. [→ Peilin Zhan 2026 (2)](#peilin-zhan-2026-2)

## Evidence

### Peilin Zhan 2026

Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958 [doi:10.48550/arxiv.2605.05958](https://doi.org/10.48550/arxiv.2605.05958)

`q2 · i?` · `design · r2`

Ablation study (Appendix D, Table 5) across six representative KT backbones comparing DR alone, joint learning, and smoothness placement. The article reports smoothness on the imputation branch "consistently achieves the best or near-best results across different backbones."

> "Moreover, ap- plying temporal smoothness to the imputation branch consis- tently achieves the best or near-best results across different backbones. In contrast, directly imposing temporal smooth- ness on the KT backbone often leads to inferior performance."

### Peilin Zhan 2026 (2)

Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958

`q2 · i?` · `design · r2`

Ablation study (Appendix D, Table 5) of the full TSDR variant versus its components across six backbones. The article reports the full variant "obtains the best AUC and ACC on all six backbones," verifying the design is backbone-agnostic.

> "Overall, the full variant, i.e., DR with joint learning and temporal smoothness on the imputation branch, obtains the best AUC and ACC on all six backbones."

## Discussion


## Related Claims
- [Meta-behavioral pattern extraction outperforms knowledge-concept-based collaborative extraction, which fails to consistently boost performance due to data sparsity](meta-behavioral-extraction-beats-kc-based-variants.md) — related
- [TSDR consistently improves calibration (ACC and RMSE) even on datasets where AUC gains plateau](tsdr-improves-calibration-acc-rmse.md) — related
- [TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets](tsdr-improves-kt-backbone-auc-benchmarks.md) — related
