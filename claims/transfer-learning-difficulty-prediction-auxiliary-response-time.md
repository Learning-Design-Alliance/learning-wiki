---
type: claim
title: Transfer learning improves prediction of item difficulty when response time is used as an auxiliary task, but not the other way around
description: Transfer learning improves prediction of item difficulty when response time is used as an auxiliary task, but not the other way around
id: transfer-learning-difficulty-prediction-auxiliary-response-time
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: kang-xue-2020
    resource: "https://www.nwea.org/research/publication/predicting-the-difficulty-and-response-time-of-multiple-choice-questions-using-transfer-learning/"
    title: "Kang Xue, Victoria Yaneva, Christopher Runyon, Peter Baldwin. (2020). Predicting the difficulty and response time of multiple choice questions using transfer learning. 15th Workshop on Innovative Use of NLP for Building Educational Applications. https://www.nwea.org/research/publication/predicting-the-difficulty-and-response-time-of-multiple-choice-questions-using-transfer-learning/"
    author: Kang Xue, Victoria Yaneva, Christopher Runyon, Peter Baldwin
    q: 2
    i: "?"
    kind: associational
    rigour: "?"
  - id: kang-xue-2020-2
    resource: "https://www.nwea.org/research/publication/predicting-the-difficulty-and-response-time-of-multiple-choice-questions-using-transfer-learning/"
    title: "Kang Xue, Victoria Yaneva, Christopher Runyon, Peter Baldwin. (2020). Predicting the difficulty and response time of multiple choice questions using transfer learning. 15th Workshop on Innovative Use of NLP for Building Educational Applications. https://www.nwea.org/research/publication/predicting-the-difficulty-and-response-time-of-multiple-choice-questions-using-transfer-learning/"
    author: Kang Xue, Victoria Yaneva, Christopher Runyon, Peter Baldwin
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Transfer learning improves prediction of item difficulty when response time is used as an auxiliary task, but not the other way around

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`

## Subclaims
`q2 i?` For the medical exam sample, transfer learning improved difficulty prediction when response time was the auxiliary task, but transfer in the reverse direction did not help. [→ Kang Xue 2020 (2)](#kang-xue-2020-2)

## Evidence

### Kang Xue 2020

Kang Xue, Victoria Yaneva, Christopher Runyon, Peter Baldwin. (2020). Predicting the difficulty and response time of multiple choice questions using transfer learning. 15th Workshop on Innovative Use of NLP for Building Educational Applications. https://www.nwea.org/research/publication/predicting-the-difficulty-and-response-time-of-multiple-choice-questions-using-transfer-learning/

`q2 · i?` · `associational · r?`

Modeling study of approximately 18,000 multiple-choice questions from a high-stakes medical exam; the authors report that "transferlearning can improve the prediction of item difficulty when response time is used as an auxiliary task but not the other way around."

> "Theresults indicate that, for our sample, transferlearning can improve the prediction of item difficulty when response time is used as an auxiliary task but not the other way around."

### Kang Xue 2020 (2)

Kang Xue, Victoria Yaneva, Christopher Runyon, Peter Baldwin. (2020). Predicting the difficulty and response time of multiple choice questions using transfer learning. 15th Workshop on Innovative Use of NLP for Building Educational Applications. https://www.nwea.org/research/publication/predicting-the-difficulty-and-response-time-of-multiple-choice-questions-using-transfer-learning/

`q2 · i?` · `associational · r2`

The same modeling study reports the asymmetry: the benefit held for difficulty prediction with response time as auxiliary task, and "not the other way around," so response time prediction did not gain from difficulty as an auxiliary task.

> "Theresults indicate that, for our sample, transferlearning can improve the prediction of item difficulty when response time is used as an auxiliary task but not the other way around."

## Discussion


## Related Claims
- [All parts of the item were important for predicting response time](all-item-parts-important-response-time-prediction.md) — related
- [Item difficulty was best predicted using signal from the item stem](difficulty-best-predicted-from-item-stem.md) — related
