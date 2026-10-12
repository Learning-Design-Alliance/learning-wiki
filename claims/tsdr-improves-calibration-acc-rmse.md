---
type: claim
title: TSDR consistently improves calibration (ACC and RMSE) even on datasets where AUC gains plateau
description: TSDR consistently improves calibration (ACC and RMSE) even on datasets where AUC gains plateau
id: tsdr-improves-calibration-acc-rmse
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: peilin-zhan-2026
    resource: "https://arxiv.org/abs/2605.05958"
    title: "Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958"
    author: Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# TSDR consistently improves calibration (ACC and RMSE) even on datasets where AUC gains plateau

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On Linux and Database, where AUC gains plateau, TSDR frequently reduces RMSE and improves ACC, including a 1.70% RMSE reduction for SparseKT on Linux. [→ Peilin Zhan 2026](#peilin-zhan-2026)

## Evidence

### Peilin Zhan 2026

Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958

`q2 · i?` · `design · r2`

Secondary-metric analysis (RQ1, Table 1) of ACC and RMSE across the nine benchmark datasets. The article reports TSDR "frequently reduces RMSE and improves ACC" with a "1.70% reduction for SparseKT on Linux."

> "Even on datasets where AUC gains plateau, such as Linux and Database, TSDR fre- quently reduces RMSE and improves ACC. A specific exam- ple is the 1.70% reduction for SparseKT on Linux."

## Discussion


## Related Claims
- [TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets](tsdr-improves-kt-backbone-auc-benchmarks.md) — related
- [Under controlled synthetic MNAR bias, TSDR-equipped models improve across the entire bias spectrum, with the RMSE advantage diminishing beyond gamma > 0.8](tsdr-robust-across-mnar-spectrum.md) — related
- [In ablations, temporal smoothness works best on the imputation branch, and the full TSDR variant achieves the best AUC and ACC on all six backbones](tsdr-ablation-smoothness-on-imputation-branch.md) — related
