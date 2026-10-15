---
type: claim
title: Dialogue act features raise regression R² but do not significantly improve outcome prediction over a prior-performance baseline
description: Dialogue act features raise regression R² but do not significantly improve outcome prediction over a prior-performance baseline
id: da-features-not-significant-over-baseline
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: reg-null
    title: reg-null
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Dialogue act features raise regression R² but do not significantly improve outcome prediction over a prior-performance baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Adding broad and specific dialogue act count features increased mean R² substantially, but F-tests did not indicate statistically significant improvements for most assessments. [→ reg-null](#reg-null)

## Evidence

### reg-null

Hunter McNichols, Fareya Ikram, and Andrew Lan. 2026. The StudyChat Dataset: Analyzing Student Dialogues With ChatGPT in an Artificial Intelligence Course. In LAK26: 16th International Learning Analytics and Knowledge Conference (LAK 2026). https://doi.org/10.1145/3785022.3785029

`q2 · i?` · `associational · r2`

Regression series predicting normalized assessment scores from a prior-score baseline, total utterance counts, and 8 broad or 31 specific DA counts across 9 assessments in both semesters. Specific-DA models raised mean R² to 0.4868 (fall) and 0.4012 (spring), but the authors report the models are likely overfitting or statistically underpowered by a limited sample size.

> "F-Tests conducted for each regression do not indicate results that are statistically significant, with the highest 𝑅2 improvement of0.19and resulting F-Score of 𝐹= 1.81,𝑝= 0.09."

## Discussion


## Related Claims
- [Students' conceptual-question and editing-request LLM usage is positively correlated with exam outcomes in the spring semester](conceptual-questions-editing-positive-exam-outcomes.md) — related
- [PTA traits show stronger statistical explanatory power than dialogue-act and Bloom's taxonomy coded baselines on StudyChat](pta-traits-beat-dialogue-act-bloom-baselines.md) — related
- Ablation of feature-vector models: time-window features add no predictive power to logistic regression but boost a feedforward network, and total count features substantially boost performance on all datasets — related
- [Conceptual Questions about mathematics are a strong negative indicator of assignment 6 scores](math-conceptual-questions-negative-a6.md) — related
