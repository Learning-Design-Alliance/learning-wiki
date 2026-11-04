---
type: claim
title: "An ML ensemble model predicts MCAT scores with limited accuracy, explaining 36% of variance"
description: "An ML ensemble model predicts MCAT scores with limited accuracy, explaining 36% of variance"
id: ml-mcat-prediction-limited-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: michele-cherfane-2026
    resource: "https://doi.org/10.2196/94197"
    title: "Michele Cherfane, Marc Ghanem, Georges Choueiry, Selim M Nasser, Tamina Elias-Rizk, Sola Aoun Bahous. (2026). Evaluating the Influence of MCAT Scores on Medical Student Selection and Performance Using a Machine Learning Approach: Retrospective Cohort Study. JMIR Medical Education. https://doi.org/10.2196/94197"
    author: Michele Cherfane, Marc Ghanem, Georges Choueiry, Selim M Nasser, Tamina Elias-Rizk, Sola Aoun Bahous
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# An ML ensemble model predicts MCAT scores with limited accuracy, explaining 36% of variance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The ensemble model achieved R²=0.36 and RMSE=0.10 on the normalized scale, corresponding to approximately 10% of the score range. [→ Michele Cherfane 2026](#michele-cherfane-2026)

## Evidence

### Michele Cherfane 2026

Michele Cherfane, Marc Ghanem, Georges Choueiry, Selim M Nasser, Tamina Elias-Rizk, Sola Aoun Bahous. (2026). Evaluating the Influence of MCAT Scores on Medical Student Selection and Performance Using a Machine Learning Approach: Retrospective Cohort Study. JMIR Medical Education. https://doi.org/10.2196/94197

`q2 · i?` · `associational · r2`

Ensemble of five ML models (LASSO, kernel ridge, gradient boosting, elastic net, LightGBM) trained on 1583 applicants using core GPA, cumulative GPA, interview score, merit points, and honors participation to predict MCAT scores.

> "The model achieved an out-of-sample R² of 0.36 (95% CI 0.32-0.41) and an RMSE of 0.10 on the normalized scale, meaning it explained 36% of the variability in MCAT scores and predicted them with an average error of 0.1."

## Discussion


## Related Claims
- [Using ML-predicted MCAT scores would have changed 6.3% to 9.4% of admission decisions despite strong rank agreement](predicted-mcat-changes-admission-decisions.md) — related
- [Incorporating ML-predicted MCAT scores into admissions composites reduces correlations with subsequent medical school performance](predicted-mcat-reduces-performance-correlations.md) — related
- [An ensemble learner outperforms every individual base learner for predicting final exam score and course grade in a large introductory statistics course](ensemble-outperforms-base-learners-exam-grade.md) — a broader claim this one bears on
- [Machine learning on pre-pandemic platform click data explains up to 77% of the variance in academic resilience](ml-platform-data-explains-resilience-variance.md) — related
