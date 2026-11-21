---
type: claim
title: Random Forest performs best at the earliest cutoffs (days 7 and 14) while Gradient Boosting dominates from day 21 onward on OULAD under strict LEAP
description: Random Forest performs best at the earliest cutoffs (days 7 and 14) while Gradient Boosting dominates from day 21 onward on OULAD under strict LEAP
id: leap-model-rankings-by-cutoff
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: ngoc-luyen-lê-2026
    resource: "https://doi.org/10.1007/978-3-032-31660-8_11"
    title: "Ngoc Luyen Lê, Marie-Hélène Abel, and Bertrand Laforge. (2026). When Can We Trust Early Warnings? Leakage-Excluded Early Outcome Prediction from LMS Interaction Logs. arXiv preprint. [doi:10.1007/978-3-032-31660-8_11](https://doi.org/10.1007/978-3-032-31660-8_11)"
    author: Ngoc Luyen Lê, Marie-Hélène Abel, and Bertrand Laforge
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Random Forest performs best at the earliest cutoffs (days 7 and 14) while Gradient Boosting dominates from day 21 onward on OULAD under strict LEAP

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` RF is the best ROC-AUC model at t=7 and t=14; GBDT is best from t=21 through t=56, reaching ROC-AUC 0.8602±0.0028 at t=56. [→ Ngoc Luyen Lê 2026](#ngoc-luyen-le-2026)

## Evidence

### Ngoc Luyen Lê 2026

Ngoc Luyen Lê, Marie-Hélène Abel, and Bertrand Laforge. (2026). When Can We Trust Early Warnings? Leakage-Excluded Early Outcome Prediction from LMS Interaction Logs. arXiv preprint. [doi:10.1007/978-3-032-31660-8_11](https://doi.org/10.1007/978-3-032-31660-8_11)

`q2 · i?` · `associational · r2`

Benchmark comparison of ten scikit-learn classifiers trained per cutoff on OULAD under strict LEAP, mean±std over five seeds; the article reports "RF is strongest in the earliest windows (t=7andt=14)". No effect size is printed.

> "RF is strongest in the earliest windows (t=7andt=14), whereas GBDT becomes dominant fromt=21onward and remains best throught=56."

## Discussion


## Related Claims
- [Temporal leakage, especially through post-cutoff assessment information, severely inflates apparent early-warning performance at early cutoffs](leakage-inflates-early-performance.md) — related
- [The largest single gain in best ROC-AUC under strict LEAP occurs between day 14 and day 21, indicating week 3 adds substantial predictive evidence](leap-week-3-gain.md) — related
- [Under strict early availability, the predictive signal shifts from behavioral engagement at early cutoffs toward assessment evidence by the end of the course](predictive-signal-shift-engagement-to-assessment.md) — related
- [Baseline LR and XGBoost models achieve comparable predictive performance on OULAD, with XGBoost slightly higher AUC-ROC](baseline-model-performance-oulad-lr-xgboost.md) — related
