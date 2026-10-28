---
type: claim
title: Integrating LECTOR topic preferences into at-risk prediction shows a tendency to improve performance, with significant AUC gains only in some cases
description: Integrating LECTOR topic preferences into at-risk prediction shows a tendency to improve performance, with significant AUC gains only in some cases
id: topic-preferences-at-risk-prediction-mixed
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: mixed
newest_evidence: 2025
sources:
  - id: erwin-daniel-lópez-zapata-2025
    resource: "https://doi.org/10.1007/s40593-025-00478-6"
    title: "Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6"
    author: Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: erwin-daniel-lópez-zapata-2025-2
    resource: "https://doi.org/10.1007/s40593-025-00478-6"
    title: "Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6"
    author: Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Integrating LECTOR topic preferences into at-risk prediction shows a tendency to improve performance, with significant AUC gains only in some cases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In week 1 of course A-2019, out-of-class topic preferences achieved a significantly higher AUC than traditional representations, while in-class AUC and both F-score comparisons showed no significant difference. [→ Erwin Daniel López Zapata 2025](#erwin-daniel-lopez-zapata-2025)
`q2 i?` Across the 60 prediction cases, results showed a tendency for topic preferences to improve predictive performance rather than a uniform significant advantage. [→ Erwin Daniel López Zapata 2025 (2)](#erwin-daniel-lopez-zapata-2025-2)

## Evidence

### Erwin Daniel López Zapata 2025

Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6

`q2 · i?` · `design · r2`

Logistic Regression predictions on first-week course A-2019 data with 3-fold cross-validation: out-of-class AUC was 0.738±0.099 for T versus 0.613±0.178 for F (p-value 6.21E-6); "in the other cases there was no signiﬁcant difference".

> "out of class, topic preferences (T) achieved a signiﬁcantly higher AUC than traditional representations (F), while in the other cases there was no signiﬁcant difference ( p < 0.05)."

### Erwin Daniel López Zapata 2025 (2)

Erwin Daniel López Zapata, Cheng Tang, Valdemar Švábenský, Fumiya Okubo, Atsushi Shimada. (2025). LECTOR: Summarizing E-book Reading Content for Personalized Student Support. Int J Artif Intell Educ 35. https://doi.org/10.1007/s40593-025-00478-6

`q2 · i?` · `design · r2`

Summary of the 60 prediction cases (about 14 datasets per course, courses A-2019 to A-2022, 600,712 logs from 218 students): the article characterizes the overall effect as "a tendency to improve the predictive performance by integrating LECTOR".

> "The results showed a tendency to improve the predictive performance by integrating LECTOR."

## Discussion


## Related Claims
- [Topic-preference features separate grade groups better than Reading Time in all analyzed cases](topic-preference-fdr-beats-reading-time.md) — related
- [Predictive models trained on one semester's offering of a course identified at-risk students in the subsequent semester with high prediction accuracy](cross-semester-at-risk-prediction-high-accuracy.md) — related
- [Random-forest models trained on a prior semester showed significantly lower AUC when tested on a new semester's data without retraining](cross-semester-auc-decline-without-retraining.md) — related
