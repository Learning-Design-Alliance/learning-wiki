---
type: claim
title: A Soft-Voting Ensemble achieves the best behavioral-dataset attrition prediction (CV F1 = 0.737, test recall = 0.769)
description: A Soft-Voting Ensemble achieves the best behavioral-dataset attrition prediction (CV F1 = 0.737, test recall = 0.769)
id: soft-voting-ensemble-behavioral-attrition-f1
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
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
    rigour: 2
---

# A Soft-Voting Ensemble achieves the best behavioral-dataset attrition prediction (CV F1 = 0.737, test recall = 0.769)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the balanced Codeforces dataset, the Soft-Voting Ensemble led nine classifiers with cross-validation F1 of 0.737 and held-out recall of 0.769. [→ Azuad Islam Ruhan 2026](#azuad-islam-ruhan-2026)

## Evidence

### Azuad Islam Ruhan 2026

Azuad Islam Ruhan, Golam Mostofa Naeem, Rakibul Islam Rafi, Sherin Afrin Mim, Nazira Bani Opi, Dewan Fahad Chowdhury, and Md. Rejaul Korim Sadi. (2026). Predicting Student Attrition in Competitive Programming: A Large-Scale Study Integrating Survey Insights and Global Behavioral Logs. https://arxiv.org/abs/2608.28618 [doi:10.48550/arxiv.2608.28618](https://doi.org/10.48550/arxiv.2608.28618)

`q2 · i?` · `associational · r2`

Benchmark of nine classifiers under 5-fold stratified cross-validation on the balanced behavioral dataset (n= 1,816) with an 80/20 stratified split and F1 as the primary metric. SVM (0.732) and Random Forest (0.731) performed comparably; all models fell between 0.621 and 0.737.

> "The Soft-Voting Ensemble achieved the highest cross-validation F1-score of 0.737 and test recall of 0.769, correctly identifying approximately 77% of true attrition cases in the held-out set."

## Discussion


## Related Claims
- [True attrition in competitive programming is preceded by an 83.71% reduction in monthly contest participation](contest-participation-decline-precedes-cp-attrition.md) — related
- [Engineered practice-balance features outperform raw activity counts: the Intensity Ratio ranks third among Codeforces predictors, and upsolving habit dominates the survey model](intensity-ratio-and-upsolving-habit-top-feature-importance.md) — related
- [A stacking ensemble of LG, SVM, NB, KNN and XGB achieved the best fine-tuning F1-score (0.88), outperforming individual models such as SVM (0.86)](stacking-ensemble-best-finetuning-f1.md) — a narrower finding that bears on this claim
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
- [The generalised plait ensemble outperforms single classifiers, majority-vote and stacking ensembles, substantially improving perceived task-difficulty classification (e.g., SVM plait error 14.54%, KNN plait 12.84%).](plait-ensemble-outperforms-single-and-standard-ensembles.md) — related
