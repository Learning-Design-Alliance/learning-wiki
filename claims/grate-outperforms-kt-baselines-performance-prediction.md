---
type: claim
title: GRATE outperforms state-of-the-art knowledge tracing baselines in student performance prediction on three real-world datasets
description: GRATE outperforms state-of-the-art knowledge tracing baselines in student performance prediction on three real-world datasets
id: grate-outperforms-kt-baselines-performance-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
sources:
  - id: chunpai-wang-2021
    title: Chunpai Wang 2021
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GRATE outperforms state-of-the-art knowledge tracing baselines in student performance prediction on three real-world datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` GRATE achieves lower RMSE than six baselines on MORF and CSIntro and higher AUC on MasteryGrids, with most improvements statistically significant. [→ Chunpai Wang 2021](#chunpai-wang-2021)

## Evidence

### Chunpai Wang 2021

Chunpai Wang, Shaghayegh Sahebi, Siqian Zhao, Peter Brusilovsky, and Laura O. Moraes. 2021. Knowledge Tracing for Complex Problem Solving: Granular Rank-Based Tensor Factorization. In Proceedings of the 29th ACM Conference on User Modeling, Adaptation and Personalization (UMAP '21). https://doi.org/10.1145/3450613.3456831

`q2 · i?` · `design · r2`

Performance prediction experiments on three datasets (MORF, CSIntro, MasteryGrids) using 5-fold nested student-stratified cross validation, evaluating RMSE for real-valued scores and AUC for binary scores; GRATE scored RMSE 0.2033 (MORF), 0.3726 (CSIntro), AUC 0.7035 (MasteryGrids), and the article reports it "significantly outperforms most of the baselines".

> "As we can see, our proposed method significantly outperforms most of the baselines. The aggregation and ranked constraint not only do not harm the results, but can improve them too."

## Discussion


## Related Claims
- [Both adaptive aggregation and the rank-based constraint are necessary for GRATE's performance](grate-ablation-both-components-necessary.md) — related
- [TSDR improves the AUC of six state-of-the-art KT backbones across nine real-world benchmark datasets](tsdr-improves-kt-backbone-auc-benchmarks.md) — related
- [TSDR consistently improves calibration (ACC and RMSE) even on datasets where AUC gains plateau](tsdr-improves-calibration-acc-rmse.md) — related
- [Under controlled synthetic MNAR bias, TSDR-equipped models improve across the entire bias spectrum, with the RMSE advantage diminishing beyond gamma > 0.8](tsdr-robust-across-mnar-spectrum.md) — related
- [In ablations, temporal smoothness works best on the imputation branch, and the full TSDR variant achieves the best AUC and ACC on all six backbones](tsdr-ablation-smoothness-on-imputation-branch.md) — related
- [CogEvolution performs comparably to the KT-based PEERS model on mastery prediction (AUC 0.80 vs 0.82) while achieving higher mistake precision (76.8%) on CogMath-948](cogevolution-mistake-precision-beats-kt-baseline.md) — related
- [TSDR is robust to the smoothness coefficient, with a stable sweet spot for lambda in (0.3, 1.0)](tsdr-lambda-sweet-spot-robustness.md) — related
- [TSDR's AUC gains are largest on open-ended platforms and limited on EdNet, whose mandatory bundle completion policy constrains selection bias](tsdr-gain-magnitude-depends-on-collection-mechanism.md) — related
