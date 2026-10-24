---
type: claim
title: Random Forest reaches CV F1 = 0.924 on the psychographic survey dataset, but the article presents this only as a localized exploratory pilot
description: Random Forest reaches CV F1 = 0.924 on the psychographic survey dataset, but the article presents this only as a localized exploratory pilot
id: random-forest-survey-pilot-f1-0924
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: azuad-islam-ruhan-2026
    resource: "https://doi.org/10.48550/arxiv.2608.28618"
    title: "Azuad Islam Ruhan, Golam Mostofa Naeem, Rakibul Islam Rafi, Sherin Afrin Mim, Nazira Bani Opi, Dewan Fahad Chowdhury, and Md. Rejaul Korim Sadi. (2026). Predicting Student Attrition in Competitive Programming: A Large-Scale Study Integrating Survey Insights and Global Behavioral Logs. https://arxiv.org/abs/2608.28618 [doi:10.48550/arxiv.2608.28618](https://doi.org/10.48550/arxiv.2608.28618)"
    author: Azuad Islam Ruhan, Golam Mostofa Naeem, Rakibul Islam Rafi, Sherin Afrin Mim, Nazira Bani Opi, Dewan Fahad Chowdhury, and Md. Rejaul Korim Sadi
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Random Forest reaches CV F1 = 0.924 on the psychographic survey dataset, but the article presents this only as a localized exploratory pilot

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Random Forest led the survey dataset with cross-validation F1 of 0.924, which the authors caution should not be treated as a generalizable predictor. [→ Azuad Islam Ruhan 2026](#azuad-islam-ruhan-2026)

## Evidence

### Azuad Islam Ruhan 2026

Azuad Islam Ruhan, Golam Mostofa Naeem, Rakibul Islam Rafi, Sherin Afrin Mim, Nazira Bani Opi, Dewan Fahad Chowdhury, and Md. Rejaul Korim Sadi. (2026). Predicting Student Attrition in Competitive Programming: A Large-Scale Study Integrating Survey Insights and Global Behavioral Logs. https://arxiv.org/abs/2608.28618 [doi:10.48550/arxiv.2608.28618](https://doi.org/10.48550/arxiv.2608.28618)

`q2 · i?` · `associational · r1`

Classifier benchmark on the survey modeling subset (n= 64; test set n≈15). The article warns that complex ensembles risk memorizing sample-specific patterns and that convergent test scores reflect "the limited resolution of a very small test set rather than true model superiority."

> "Random Forest achieved a cross-validation F1-score of 0.924 on the survey dataset (Fig. 11). We caution strongly that this result should be interpreted as alocalized exploratory pilotrather than a robust, generalizable predictor."

## Discussion


## Related Claims
- [Engineered practice-balance features outperform raw activity counts: the Intensity Ratio ranks third among Codeforces predictors, and upsolving habit dominates the survey model](intensity-ratio-and-upsolving-habit-top-feature-importance.md) — related
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — a broader claim this one bears on
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
