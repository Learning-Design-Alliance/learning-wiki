---
type: claim
title: "Engineered practice-balance features outperform raw activity counts: the Intensity Ratio ranks third among Codeforces predictors, and upsolving habit dominates the survey model"
description: "Engineered practice-balance features outperform raw activity counts: the Intensity Ratio ranks third among Codeforces predictors, and upsolving habit dominates the survey model"
id: intensity-ratio-and-upsolving-habit-top-feature-importance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: azuad-islam-ruhan-2026
    resource: "https://doi.org/10.48550/arxiv.2608.28618"
    title: "Azuad Islam Ruhan, Golam Mostofa Naeem, Rakibul Islam Rafi, Sherin Afrin Mim, Nazira Bani Opi, Dewan Fahad Chowdhury, and Md. Rejaul Korim Sadi. (2026). Predicting Student Attrition in Competitive Programming: A Large-Scale Study Integrating Survey Insights and Global Behavioral Logs. https://arxiv.org/abs/2608.28618 [doi:10.48550/arxiv.2608.28618](https://doi.org/10.48550/arxiv.2608.28618)"
    author: Azuad Islam Ruhan, Golam Mostofa Naeem, Rakibul Islam Rafi, Sherin Afrin Mim, Nazira Bani Opi, Dewan Fahad Chowdhury, and Md. Rejaul Korim Sadi
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: azuad-islam-ruhan-2026-2
    resource: "https://arxiv.org/abs/2608.28618"
    title: "Azuad Islam Ruhan, Golam Mostofa Naeem, Rakibul Islam Rafi, Sherin Afrin Mim, Nazira Bani Opi, Dewan Fahad Chowdhury, and Md. Rejaul Korim Sadi. (2026). Predicting Student Attrition in Competitive Programming: A Large-Scale Study Integrating Survey Insights and Global Behavioral Logs. https://arxiv.org/abs/2608.28618"
    author: Azuad Islam Ruhan, Golam Mostofa Naeem, Rakibul Islam Rafi, Sherin Afrin Mim, Nazira Bani Opi, Dewan Fahad Chowdhury, and Md. Rejaul Korim Sadi
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Engineered practice-balance features outperform raw activity counts: the Intensity Ratio ranks third among Codeforces predictors, and upsolving habit dominates the survey model

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 associational `r1`–`r2` · `q2`

## Subclaims
`q2 i?` The engineered Intensity Ratio (11.3% importance) ranked third on the behavioral dataset, above raw problem counts. [→ Azuad Islam Ruhan 2026](#azuad-islam-ruhan-2026)
`q2 i?` In the survey model, upsolving habit (28.81%) and peer circle density (21.01%) together account for roughly half of predictive weight, far exceeding academic grades. [→ Azuad Islam Ruhan 2026 (2)](#azuad-islam-ruhan-2026-2)

## Evidence

### Azuad Islam Ruhan 2026

Azuad Islam Ruhan, Golam Mostofa Naeem, Rakibul Islam Rafi, Sherin Afrin Mim, Nazira Bani Opi, Dewan Fahad Chowdhury, and Md. Rejaul Korim Sadi. (2026). Predicting Student Attrition in Competitive Programming: A Large-Scale Study Integrating Survey Insights and Global Behavioral Logs. https://arxiv.org/abs/2608.28618 [doi:10.48550/arxiv.2608.28618](https://doi.org/10.48550/arxiv.2608.28618)

`q2 · i?` · `associational · r2`

Random Forest feature importance on the Codeforces dataset (Fig. 12): account tenure (14.31%) ranked first and contest frequency (12.41%) second, with the engineered Intensity Ratio third at 11.3%, above raw problem counts.

> "Notably, our engineered Intensity Ratio (intensity_ratio, 11.3%) ranked third–above raw problem counts—validating the hypothesis that the balance between independent practice and contest participation captures attrition-relevant behavioral signal not expressed by either metric alone."

### Azuad Islam Ruhan 2026 (2)

Azuad Islam Ruhan, Golam Mostofa Naeem, Rakibul Islam Rafi, Sherin Afrin Mim, Nazira Bani Opi, Dewan Fahad Chowdhury, and Md. Rejaul Korim Sadi. (2026). Predicting Student Attrition in Competitive Programming: A Large-Scale Study Integrating Survey Insights and Global Behavioral Logs. https://arxiv.org/abs/2608.28618

`q2 · i?` · `associational · r1`

Random Forest feature importance for the survey-based psychographic model (Fig. 8). The authors read the primacy of behavioral consistency and social environment over grades as showing retention in CP is a practice discipline and community problem, not a cognitive capability problem.

> "upsolving habit emerged as the dominant predictor of attrition risk (28.81%), followed by peer circle density (21.01%), DSA course grade (10.81%), and data structure understanding (9.0%)."

## Discussion


## Related Claims
- [True attrition in competitive programming is preceded by an 83.71% reduction in monthly contest participation](contest-participation-decline-precedes-cp-attrition.md) — related
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
- [Academic word list count, word count, and Flesch-Kincaid grade level are the most important features for predicting cognitive engagement in discussion posts](awl-count-word-count-feature-importance-engagement.md) — related
- [SHAP analysis identifies Hapax Ratio as the most influential stylometric feature in Random Forest predictions, followed by NSR, Noun Ratio, Adverb Ratio, and TTR](shap-hapax-ratio-most-influential-feature.md) — a narrower finding that bears on this claim
- [Random Forest reaches CV F1 = 0.924 on the psychographic survey dataset, but the article presents this only as a localized exploratory pilot](random-forest-survey-pilot-f1-0924.md) — related
- [The Skill-Application Paradox: stopped competitive programmers self-report higher theoretical confidence than active peers yet show significantly weaker practice habits and peer support](skill-application-paradox-cp-attrition.md) — related
- [A Soft-Voting Ensemble achieves the best behavioral-dataset attrition prediction (CV F1 = 0.737, test recall = 0.769)](soft-voting-ensemble-behavioral-attrition-f1.md) — related
- [Feature-based model predictive power derives from a large and varied set of features rather than a few dominant variables](feature-importance-spread-across-many-features.md) — related
