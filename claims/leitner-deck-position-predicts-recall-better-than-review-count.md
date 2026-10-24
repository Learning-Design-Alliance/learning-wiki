---
type: claim
title: "In Mnemosyne log data, setting memory strength equal to an item's Leitner deck position predicts recall better than number of past reviews, which beats constant strength."
description: "In Mnemosyne log data, setting memory strength equal to an item's Leitner deck position predicts recall better than number of past reviews, which beats constant strength."
id: leitner-deck-position-predicts-recall-better-than-review-count
status: review
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: moderate
newest_evidence: 2016
recheck_by: 2019
sources:
  - id: reddy-2016
    resource: "https://doi.org/10.1145/2939672.2939850"
    title: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850"
    author: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# In Mnemosyne log data, setting memory strength equal to an item's Leitner deck position predicts recall better than number of past reviews, which beats constant strength.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Memory strength set to Leitner deck position outperformed strength proportional to the number of past reviews, which in turn outperformed a constant strength, by validation and test AUC; no AUC values are printed in the text. [→ Reddy 2016](#reddy-2016)

## Evidence

### Reddy 2016

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q2 · i?` · `associational · r2`

Observational study of Mnemosyne flashcard log data, comparing memory models by cross-validated validation AUC and a held-out test set. Setting strength to the "Leitner deck position qij performs better than setting it to be proportional to the number of past reviews nij", itself better than constant s (Fig. 3); no numbers printed.

> "Setting the mem- ory strength s to be equal to the Leitner deck position qij performs better than setting it to be proportional to the number of past reviews nij, which in turn is better than using a constant s"

## Discussion

## Related Claims

- [Memory-decay-based models fit fact-learning datasets better than models insensitive to memory decay](memory-features-improve-fit-for-fact-learning-datasets.md) — the general claim this finding bears on, with the studies behind it

- [Under the Leitner Queue Network model, raising the rate of new-item introduction beyond a threshold causes a phase transition in learning rate, which a Mechanical Turk vocabulary experiment reproduced.](leitner-queue-network-phase-transition-in-learning-rate.md) — the general claim this finding bears on, with the studies behind it
- [In Mnemosyne flashcard log data, adding a delay term improves the recall-prediction performance of exponential forgetting curve memory models.](delay-term-improves-exponential-forgetting-curve-recall-prediction.md) — related
- [In Mnemosyne log data, item-specific difficulty parameters outperform a global difficulty for lower and higher Leitner decks, while global difficulty performs better for intermediate decks.](item-specific-difficulty-helps-only-at-low-and-high-leitner-decks.md) — related
- [In Mnemosyne log data, exponential forgetting curve models that include a delay term perform comparably to 1PL-IRT, the best-performing benchmark model.](exponential-forgetting-models-with-delay-perform-comparably-to-1pl-irt.md) — related
