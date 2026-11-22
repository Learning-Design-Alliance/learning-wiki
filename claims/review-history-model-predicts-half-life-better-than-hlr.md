---
type: claim
title: In vocabulary-app review logs, a memory model that tracks each item's review history predicted memory half-life after a review with less error than half-life regression
description: Fitted to 220 million review logs from a vocabulary app, a memory model whose state carries each word's difficulty, last half-life and recall probability at review predicted the half-life after a successful or failed recall with smaller errors than half-life regression, which uses only counts of past successes and failures.
id: review-history-model-predicts-half-life-better-than-hlr
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-22
evidence_strength: weak
newest_evidence: 2022
sources:
  - id: ye-et-al-2022
    resource: "https://doi.org/10.1145/3534678.3539081"
    title: "Ye, J., Su, J., & Cao, Y. (2022). A stochastic shortest path algorithm for optimizing spaced repetition scheduling. In *Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '22)* (pp. 4381–4390). ACM. [doi:10.1145/3534678.3539081](https://doi.org/10.1145/3534678.3539081)"
    author: "Ye, J., Su, J., & Cao, Y."
    q: 2
    i: "?"
    n: 220 million review logs from 828 thousand app users
    kind: associational
    rigour: 2
---

# In vocabulary-app review logs, a memory model that tracks each item's review history predicted memory half-life after a review with less error than half-life regression

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2` · n=220 million review logs from 828 thousand app users
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

This bears on what an adaptive review scheduler should keep about each item: the order of past successes and failures and the gaps between reviews, not only how many of each there were. Half-life here is the delay at which the predicted chance of recalling an item falls to one half.

## Subclaims
`q2 i?` On one month of logs from the MaiMemo vocabulary app, the DHP model (difficulty, half-life and recall probability as state) predicted half-life after a successful recall with a mean absolute error of 11.93 (26.16%) against 41.70 (45.75%) for half-life regression, and after a failed recall with 0.44 (31.99%) against 7.08 (112.7%). [→ Ye et al. 2022](#ye-et-al-2022)

`q2 i?` The authors attribute the gap to half-life regression's use of success and failure counts only, which cannot tell a recall followed by a failure from a failure followed by a recall. [→ Ye et al. 2022](#ye-et-al-2022)

## Evidence

### Ye et al. 2022

Ye, J., Su, J., & Cao, Y. (2022). A stochastic shortest path algorithm for optimizing spaced repetition scheduling. In *Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '22)* (pp. 4381–4390). ACM. [doi:10.1145/3534678.3539081](https://doi.org/10.1145/3534678.3539081)

`q2 · observational log data, model comparison` · `i? · errors in half-life units, no standardised effect size` · `n=220 million review logs from 828 thousand app users` · `associational · r2`

The authors collected one month of review logs (220 million review events from 828 thousand users) from MaiMemo, an app for memorising English vocabulary with [flashcards](../strategies/flashcard-drill.md), and dropped histories whose first review was already a success, to exclude words known before the app. Words were grouped into ten difficulty levels by the share of learners who recalled them the day after first learning them, and the recall probability of a group of learners sharing a word difficulty and a review history was taken as the share who recalled; exponential forgetting curves fitted to these groups gave a half-life for each. A model whose state is each word's difficulty, last half-life and recall probability at the review (the DHP model, eq. 8, p. 4384) was compared with half-life regression (Settles & Meeder, 2016) on predicted half-life after a recall and after a failure (Table 3, p. 4386): mean absolute error 11.93 against 41.70 after a recall, and 0.44 against 7.08 after a failure; percentage errors 26.16% against 45.75%, and 31.99% against 112.7%. The paper does not report a held-out test set for this comparison, nor the learners' ages or other characteristics, and the review intervals in the logs were those learners took in the app, not ones the study assigned.

## Discussion

Both models were fitted to grouped log data from one app and one kind of material (English words), so the result says which model describes these data better, not how much a scheduler built on either would change what learners remember. The same authors' extended journal version of this work refits the comparison on the same app's logs with cross-validation and adds recurrent-network models. For [spaced repetition](../elements/spaced-repetition.md) design, the practical point is that an item's history of outcomes and gaps carried information about its next half-life that outcome counts alone missed.

## Related Claims
- [In Mnemosyne flashcard log data, adding a delay term improves the recall-prediction performance of exponential forgetting curve memory models.](delay-term-improves-exponential-forgetting-curve-recall-prediction.md) — related: another log-data comparison of forgetting-curve models
- [The exponential forgetting curve model outperforms the power-law model on MAE and half-life correlation, while the power-law model performs slightly better on AUC](exponential-model-outperforms-power-law-mae-corh.md) — related
- [In vocabulary-app review logs, a successful recall lengthened memory half-life more when the review came at a lower recall probability, less as the memory strengthened, and less for harder words](recall-at-lower-probability-lengthens-half-life-more.md) — the fitted rules of the same model
- [In a simulation built on vocabulary-app review logs, a scheduler that minimises expected review time brought 6,000 words to a one-year half-life in fewer days than Anki-style, threshold and MEMORIZE schedules](cost-minimizing-scheduler-fewer-review-days-simulation.md) — the scheduler built on this model
