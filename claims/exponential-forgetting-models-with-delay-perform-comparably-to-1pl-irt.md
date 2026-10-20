---
type: claim
title: In Mnemosyne log data, exponential forgetting curve models that include a delay term perform comparably to 1PL-IRT, the best-performing benchmark model.
description: In Mnemosyne log data, exponential forgetting curve models that include a delay term perform comparably to 1PL-IRT, the best-performing benchmark model.
id: exponential-forgetting-models-with-delay-perform-comparably-to-1pl-irt
status: review
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
    kind: causal
    rigour: "?"
---

# In Mnemosyne log data, exponential forgetting curve models that include a delay term perform comparably to 1PL-IRT, the best-performing benchmark model.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`

## Subclaims
`q2 i?` Exponential forgetting models 5, 8, 10 and 13, which include the delay term, performed comparably to 1PL-IRT (model 3), the best benchmark among 0PL-IRT, 1PL-IRT and logistic regression; comparable performance was read from AUC curves and equivalence was not tested. [→ Reddy 2016](#reddy-2016)

## Evidence

### Reddy 2016

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q2 · i?` · `causal · r?`

Observational study of Mnemosyne flashcard log data, comparing memory models by cross-validated validation AUC against benchmark models. Models including the delay term "perform comparably to 1PL-IRT (model 3), which is the best-performing benchmark model"; no AUC values are printed.

> "Exponential for- getting models that include the delay term (models 5, 8, 10, and 13) perform comparably to 1PL-IRT (model 3), which is the best-performing benchmark model"

## Discussion

## Related Claims

- [The survey reports, citing Pavlik et al., that no single knowledge tracing model was always the best, and that a better model must consider multiple student features and the learning context.](no-single-knowledge-tracing-model-is-always-best.md) — the general claim this finding bears on, with the studies behind it

- [Memory-decay-based models fit fact-learning datasets better than models insensitive to memory decay](memory-features-improve-fit-for-fact-learning-datasets.md) — the general claim this finding bears on, with the studies behind it
- [In Mnemosyne flashcard log data, adding a delay term improves the recall-prediction performance of exponential forgetting curve memory models.](delay-term-improves-exponential-forgetting-curve-recall-prediction.md) — related
- [In Mnemosyne log data, item-specific difficulty parameters outperform a global difficulty for lower and higher Leitner decks, while global difficulty performs better for intermediate decks.](item-specific-difficulty-helps-only-at-low-and-high-leitner-decks.md) — related
- [In Mnemosyne log data, setting memory strength equal to an item's Leitner deck position predicts recall better than number of past reviews, which beats constant strength.](leitner-deck-position-predicts-recall-better-than-review-count.md) — related
