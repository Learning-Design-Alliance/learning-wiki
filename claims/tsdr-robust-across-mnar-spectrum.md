---
type: claim
title: "Under controlled synthetic MNAR bias, TSDR-equipped models improve across the entire bias spectrum, with the RMSE advantage diminishing beyond gamma > 0.8"
description: "Under controlled synthetic MNAR bias, TSDR-equipped models improve across the entire bias spectrum, with the RMSE advantage diminishing beyond gamma > 0.8"
id: tsdr-robust-across-mnar-spectrum
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

# Under controlled synthetic MNAR bias, TSDR-equipped models improve across the entire bias spectrum, with the RMSE advantage diminishing beyond gamma > 0.8

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` On six synthetic datasets with MNAR degree gamma from 0.0 to 0.999, TSDR consistently yields improvements across the entire spectrum as baselines degrade. [→ Peilin Zhan 2026](#peilin-zhan-2026)
`q2 i?` For RMSE, TSDR is highly effective at reducing error when MNAR is low, though this advantage diminishes slightly beyond gamma > 0.8; positive results at gamma = 0.0 indicate the framework is safe. [→ Peilin Zhan 2026 (2)](#peilin-zhan-2026-2)

## Evidence

### Peilin Zhan 2026

Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958 [doi:10.48550/arxiv.2605.05958](https://doi.org/10.48550/arxiv.2605.05958)

`q2 · i?` · `design · r2`

Simulation study (RQ2, Figure 3) on six synthetic datasets with controllable MNAR mechanism, gamma in {0, 0.2, 0.4, 0.6, 0.8, 0.999}, all six backbones with and without TSDR. The article reports TSDR "consistently yields improvements across the entire spectrum."

> "we observe varying degrees of performance degradation across all baselines as the bias severity increases, particularly visible in AUC. However, equipping SOTA mod- els with TSDR consistently yields improvements across the entire spectrum."

### Peilin Zhan 2026 (2)

Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958

`q2 · i?` · `design · r2`

Simulation study (RQ2) RMSE analysis across MNAR degrees. The article reports TSDR "is highly effective at reducing error when MNAR is low, although this advantage diminishes slightly beyondγ >0.8."

> "Specifically for RMSE, with the exception of DKT, TSDR is highly effective at reducing error when MNAR is low, although this advantage diminishes slightly beyondγ >0.8."

## Discussion


## Related Claims
- [TSDR consistently improves calibration (ACC and RMSE) even on datasets where AUC gains plateau](tsdr-improves-calibration-acc-rmse.md) — related
- [TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets](tsdr-improves-kt-backbone-auc-benchmarks.md) — related
- [TSDR's AUC gains are largest on open-ended platforms and limited on EdNet, whose mandatory bundle completion policy constrains selection bias](tsdr-gain-magnitude-depends-on-collection-mechanism.md) — related
