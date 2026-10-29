---
type: claim
title: A Random Forest Classifier embedded in the MLADs achieved an F1-score of 0.82 and AUC of 0.89 for course-completion-risk alerts under five-fold cross-validation
description: A Random Forest Classifier embedded in the MLADs achieved an F1-score of 0.82 and AUC of 0.89 for course-completion-risk alerts under five-fold cross-validation
id: random-forest-early-alert-f1-082-auc-089
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-29
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: zeynab-artemis-mohseni-2026
    resource: "https://doi.org/10.1007/s11423-025-10577-9"
    title: "Zeynab (Artemis) Mohseni, Italo Masiello. (2026). Co-designing, developing, and implementing multiple learning analytics dashboards for data-driven decision-making in education: a design-based research approach. Education Tech Research Dev. https://doi.org/10.1007/s11423-025-10577-9"
    author: Zeynab (Artemis) Mohseni, Italo Masiello
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# A Random Forest Classifier embedded in the MLADs achieved an F1-score of 0.82 and AUC of 0.89 for course-completion-risk alerts under five-fold cross-validation

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The Random Forest Classifier generating early alerts about course completion risk yielded F1 = 0.82 and AUC = 0.89, judged satisfactory for formative use. [→ Zeynab (Artemis) Mohseni 2026](#zeynab-artemis-mohseni-2026)

## Evidence

### Zeynab (Artemis) Mohseni 2026

Zeynab (Artemis) Mohseni, Italo Masiello. (2026). Co-designing, developing, and implementing multiple learning analytics dashboards for data-driven decision-making in education: a design-based research approach. Education Tech Research Dev. https://doi.org/10.1007/s11423-025-10577-9

`q2 · i?` · `design · r3`

The MLADs' predictive component, a Random Forest Classifier analyzing aggregated attendance, DLM activity and assessment patterns, was trained on 70% of historical data and validated on 30% with five-fold cross-validation, yielding "an F1-score of 0.82" and AUC of 0.89.

> "The model was trained on 70% of the available historical data and validated on the remaining 30% using five-fold cross-validation. The evaluation yielded an F1-score of 0.82 and an area under the ROC curve (AUC) of 0.89, which were considered satisfactory for the intended formative use"

## Discussion


## Related Claims
- [CatBoost achieved the best classification performance among tested algorithms for predicting course completion risk (F-measure .77, accuracy 78%, AUC .87)](catboost-best-performing-risk-classifier.md) — reports the opposite
- [CatBoost is the best-performing algorithm for predicting programme non-completion, with F1-measure of 94.5±0.6, slightly better than Random Forest](catboost-best-f1-programme-completion.md) — related
