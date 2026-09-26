---
type: claim
title: In Mnemosyne flashcard log data, adding a delay term improves the recall-prediction performance of exponential forgetting curve memory models.
description: In Mnemosyne flashcard log data, adding a delay term improves the recall-prediction performance of exponential forgetting curve memory models.
id: delay-term-improves-exponential-forgetting-curve-recall-prediction
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: moderate
sources:
  - id: reddy-2016
    resource: "https://doi.org/10.1145/2939672.2939850"
    title: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850"
    author: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T."
    q: 2
    i: "?"
---

# In Mnemosyne flashcard log data, adding a delay term improves the recall-prediction performance of exponential forgetting curve memory models.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` Across paired exponential forgetting curve models with and without a delay term, incorporating the delay term improved predictive performance on Mnemosyne log data; no numeric AUC values are printed in the text. [→ Reddy 2016](#reddy-2016)

## Evidence

### Reddy 2016

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q2 · i?`

Observational study of Mnemosyne flashcard log data, comparing memory models by cross-validated validation AUC. The first of four observations is that "Incorporating a delay term improves the performance of the memory model", shown by paired models in Fig. 2; the text prints no AUC values.

> "Positive impact of delay term: Incorporating a delay term improves the performance of the memory model."

## Discussion


## Related Claims
- [Spaced Repetition Improves Retention](spaced-repetition-improves-retention.md)
- [In Mnemosyne log data, exponential forgetting curve models that include a delay term perform comparably to 1PL-IRT, the best-performing benchmark model.](exponential-forgetting-models-with-delay-perform-comparably-to-1pl-irt.md) — related
- [In Mnemosyne log data, setting memory strength equal to an item's Leitner deck position predicts recall better than number of past reviews, which beats constant strength.](leitner-deck-position-predicts-recall-better-than-review-count.md) — related
- [In Mnemosyne log data, item-specific difficulty parameters outperform a global difficulty for lower and higher Leitner decks, while global difficulty performs better for intermediate decks.](item-specific-difficulty-helps-only-at-low-and-high-leitner-decks.md) — related
- [Repeated retrieval practice alters the rate at which learned items are forgotten, according to learn-to-criterion studies and forgetting-curve analyses the chapter reviews](repeated-retrieval-alters-the-rate-of-forgetting.md) — related
