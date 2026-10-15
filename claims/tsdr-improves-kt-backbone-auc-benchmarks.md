---
type: claim
title: TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets
description: TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets
id: tsdr-improves-kt-backbone-auc-benchmarks
status: draft
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
---

# TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Applying TSDR to six KT baselines yields AUC improvements across diverse model architectures on nine real-world datasets. [→ Peilin Zhan 2026](#peilin-zhan-2026)

## Evidence

### Peilin Zhan 2026

Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958 [doi:10.48550/arxiv.2605.05958](https://doi.org/10.48550/arxiv.2605.05958)

`q2 · i?` · `design · r2`

Empirical benchmark study (RQ1, Table 1) applying TSDR to DKT, AKT, simpleKT, FoLiBiKT, SparseKT and DisKT on nine datasets with student-stratified 5-fold cross-validation, evaluated via AUC, ACC and RMSE. The article reports "TSDR yields improvements across diverse model architectures."

> "Regarding the primary evaluation metric of AUC, TSDR yields improvements across diverse model architectures. These gains are particularly notable on datasets characterized by high sparsity or strong student autonomy."

## Discussion


## Related Claims
- [TSDR consistently improves calibration (ACC and RMSE) even on datasets where AUC gains plateau](tsdr-improves-calibration-acc-rmse.md) — related
- [In ablations, temporal smoothness works best on the imputation branch, and the full TSDR variant achieves the best AUC and ACC on all six backbones](tsdr-ablation-smoothness-on-imputation-branch.md) — related
- [TSDR is robust to the smoothness coefficient, with a stable sweet spot for lambda in (0.3, 1.0)](tsdr-lambda-sweet-spot-robustness.md) — a narrower finding that bears on this claim
- [Under controlled synthetic MNAR bias, TSDR-equipped models improve across the entire bias spectrum, with the RMSE advantage diminishing beyond gamma > 0.8](tsdr-robust-across-mnar-spectrum.md) — related
