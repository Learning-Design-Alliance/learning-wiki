---
type: claim
title: On the CASED challenge test set, all participating engagement-prediction methods converge near random-chance performance, with the best F1 Macro at 0.52
description: On the CASED challenge test set, all participating engagement-prediction methods converge near random-chance performance, with the best F1 Macro at 0.52
id: cased-challenge-methods-near-random-chance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: leaderboard-1
    title: leaderboard-1
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On the CASED challenge test set, all participating engagement-prediction methods converge near random-chance performance, with the best F1 Macro at 0.52

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` All participating methods on the CASED classification and regression tracks perform near random chance, with the best method reaching F1 Macro 0.52 and all submissions obtaining near-zero or negative R2, Pearson, and CCC in regression. [→ leaderboard-1](#leaderboard-1)

## Evidence

### leaderboard-1

Alperen Kantarcı, Visvanathan Ramesh, and Gemma Roig. 2026. Mind the Student: Behavioral and Contextual Cues for Automated Engagement Prediction in Online Learning. ICMI '26, Napoli, Italy. https://doi.org/10.1145/3776574.3832485

`q2 · i?` · `design · r2`

Official CASED challenge leaderboard results (Tables 1 and 2) reported by the authors. In regression, "all submissions obtained near-zero or negative values for 𝑅2, Pearson correlation, and CCC", indicating no method reliably captured the engagement signal.

> "Best-performing method obtained a F1 Macro of 0.52, suggesting that all approaches face with similar limitations imposed by the dataset and the task."

## Discussion


## Related Claims
- [Random forest algorithms yielded the best classification performance in K–8 MMLA studies comparing multiple machine learning models](mmla-k8-random-forest-best-performance.md) — related
- [Random Forest is the most commonly used NLP-supporting algorithm in LA, while deep learning models (LSTM, BERT) have been widely adopted since 2021](nlp-la-algorithm-adoption-random-forest-to-deep-learning.md) — related
- [A random forest classified flagged versus non-flagged word problems with the best accuracy of five tested models (AUC = 0.75)](random-forest-best-auc-flagged-problems.md) — related
- [Secondary outcomes differed in predictability: near-term related-task performance was hardest while 7–28-day performance showed a longitudinal signal](secondary-outcomes-varied-predictability.md) — related
