---
type: claim
title: SVM-based regressors outperformed other regressors in the ETF price-delta forecasting benchmark
description: SVM-based regressors outperformed other regressors in the ETF price-delta forecasting benchmark
id: svm-regressors-outperformed-other-regressors
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: freyaa-chawla-2026
    resource: "https://doi.org/10.48550/arxiv.2605.05144"
    title: "Freyaa Chawla, Ahan Chawla, Rishi Singh, Joe Germino, Grigorii Khvatskii. (2026). Human-AI Co-Mentorship in Project-Based Learning: A Case Study in Financial Forecasting. arXiv preprint. https://arxiv.org/abs/2605.05144 [doi:10.48550/arxiv.2605.05144](https://doi.org/10.48550/arxiv.2605.05144)"
    author: Freyaa Chawla, Ahan Chawla, Rishi Singh, Joe Germino, Grigorii Khvatskii
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SVM-based regressors outperformed other regressors in the ETF price-delta forecasting benchmark

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` SVM regressors, especially paired with decision tree or random forest classifiers, consistently outperformed other regressors, while ARIMA regressors generally underperformed. [→ Freyaa Chawla 2026](#freyaa-chawla-2026)

## Evidence

### Freyaa Chawla 2026

Freyaa Chawla, Ahan Chawla, Rishi Singh, Joe Germino, Grigorii Khvatskii. (2026). Human-AI Co-Mentorship in Project-Based Learning: A Case Study in Financial Forecasting. arXiv preprint. https://arxiv.org/abs/2605.05144 [doi:10.48550/arxiv.2605.05144](https://doi.org/10.48550/arxiv.2605.05144)

`q2 · i?` · `design · r2`

Results comparison across regression-model and classifier-model combinations reported in the results section and Table 2, where the best MSE/MAE combination is shown in bold. The article reports SVM regressors "consistently outperformed other regressors"; no effect size is printed.

> "SVM based regressors consistently outperformed other regressors especially when coupled with either decision tree or random forest classifiers suggesting effective capture of temporal dependencies and enhanced predictive stability."

## Discussion


## Related Claims
- [LLM-generated news sentiment features did not improve ETF price-forecasting model performance in this project](sentiment-features-did-not-improve-etf-forecasting.md) — related
- [A support vector machine classifier outperformed decision tree and random forest models in predicting cognitive engagement levels of online discussion posts](svm-outperforms-dt-rf-cognitive-engagement-prediction.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
