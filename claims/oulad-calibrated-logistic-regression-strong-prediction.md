---
type: claim
title: A calibrated logistic-regression model predicts next-assessment pass/fail strongly on OULAD at both decision horizons
description: A calibrated logistic-regression model predicts next-assessment pass/fail strongly on OULAD at both decision horizons
id: oulad-calibrated-logistic-regression-strong-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
sources:
  - id: ngoc-luyen-le-2026
    resource: "https://doi.org/10.48550/arxiv.2608.17618"
    title: "Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618 [doi:10.48550/arxiv.2608.17618](https://doi.org/10.48550/arxiv.2608.17618)"
    author: Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: ngoc-luyen-le-2026-2
    resource: "https://arxiv.org/abs/2608.17618"
    title: "Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618"
    author: Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A calibrated logistic-regression model predicts next-assessment pass/fail strongly on OULAD at both decision horizons

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The calibrated logistic-regression baseline achieves AUC 0.884 at d-14 and 0.889 at d-7 on held-out test presentations. [→ Ngoc Luyen Le 2026](#ngoc-luyen-le-2026)
`q2 i?` Brier scores of 0.128 (d-14) and 0.122 (d-7) indicate usable calibration for downstream recourse generation. [→ Ngoc Luyen Le 2026 (2)](#ngoc-luyen-le-2026-2)

## Evidence

### Ngoc Luyen Le 2026

Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618 [doi:10.48550/arxiv.2608.17618](https://doi.org/10.48550/arxiv.2608.17618)

`q2 · i?` · `design · r2`

Offline evaluation on OULAD with a frozen module-presentation-level split (15 train, 2 validation, 5 test presentations), reporting held-out test performance. AUC values are 0.884 (d-14) and 0.889 (d-7); the article notes that "the later snapshot benefits from more recent learner evidence".

> "The calibrated logistic-regression baseline provides strong perfor- mance, with AUC values of0.884atd−14and0.889atd−7. F1 and average precision follow the same pattern, indicating that the later snapshot benefits from more recent learner evidence."

### Ngoc Luyen Le 2026 (2)

Ngoc Luyen Le, Marie-Hélène Abel, Bertrand Laforge. (2026). From Student Risk Prediction to SC2R: Semantics-Constrained Counterfactual Recourse for Educational Decision Support. arXiv preprint. https://arxiv.org/abs/2608.17618

`q2 · i?` · `design · r2`

Same offline OULAD evaluation of the calibrated logistic-regression pipeline. The printed Brier scores are 0.128 and 0.122, which the article says "indicate usable calibration for downstream recourse generation"; no effect size is reported.

> "F1 and average precision follow the same pattern, indicating that the later snapshot benefits from more recent learner evidence. The Brier scores are0.128and0.122, which indicate usable calibration for downstream recourse generation."

## Discussion


## Related Claims
- [Integer-programming recourse generates compact, model-valid, SHACL-conformant intervention plans at scale on OULAD](ip-recourse-compact-plans-at-scale.md) — related
- [Supplementary nonlinear models yield only modest AUC gains over the calibrated logistic baseline](nonlinear-models-modest-auc-gains-over-logistic-baseline.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
- [Explainable models including logistic regression, kNN and a Bernoulli Mixture Model all reach around 78% accuracy in predicting question-level pass/fail, with well-calibrated probabilities](explainable-models-78-percent-accuracy-calibrated.md) — related
- [Machine learning methods outperformed logistic regression in classification accuracy across reviewed studies](ml-outperforms-logistic-regression-aied.md) — reports the opposite
- [The scheduling model fit the experimental data well, correlating strongly with actual final-test performance (r = 0.775) with AUC = 0.871](model-fit-recall-prediction-accuracy.md) — related
