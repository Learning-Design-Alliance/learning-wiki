---
type: claim
title: In Mnemosyne log data, item-specific difficulty parameters outperform a global difficulty for lower and higher Leitner decks, while global difficulty performs better for intermediate decks.
description: In Mnemosyne log data, item-specific difficulty parameters outperform a global difficulty for lower and higher Leitner decks, while global difficulty performs better for intermediate decks.
id: item-specific-difficulty-helps-only-at-low-and-high-leitner-decks
status: review
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: mixed
newest_evidence: 2016
source_checked: 2026-10-20
recheck_by: 2019
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

# In Mnemosyne log data, item-specific difficulty parameters outperform a global difficulty for lower and higher Leitner decks, while global difficulty performs better for intermediate decks.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r?` · `q2`
> **Currency** · newest study 2016 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Item-specific difficulties outperformed a global item difficulty for decks q ≤ 2 and q > 5, but the global difficulty performed better for intermediate decks; no numeric AUC values are printed. [→ Reddy 2016](#reddy-2016)

## Evidence

### Reddy 2016

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q2 · i?` · `causal · r?`

Observational study of Mnemosyne flashcard log data, comparing memory models by cross-validated validation AUC per deck bin. "Item-speciﬁc diﬃculties θi outperform global item diﬃculty θ for lower decks" and higher decks, but the global parameter did better for intermediate decks (models 5 vs. 10, 8 vs. 13).

> "Item-speciﬁc diﬃculties θi outperform global item diﬃculty θ for lower decks (qij≤ 2) and higher decks ( qij > 5), but the global dif- ﬁculty performs better for intermediate decks (model 5 vs. 10, 8 vs. 13)"

## Discussion

## Related Claims

- [Memory-decay-based models fit fact-learning datasets better than models insensitive to memory decay](memory-features-improve-fit-for-fact-learning-datasets.md) — the general claim this finding bears on, with the studies behind it

- [Under the Leitner Queue Network model, raising the rate of new-item introduction beyond a threshold causes a phase transition in learning rate, which a Mechanical Turk vocabulary experiment reproduced.](leitner-queue-network-phase-transition-in-learning-rate.md) — the general claim this finding bears on, with the studies behind it
- [In Mnemosyne flashcard log data, adding a delay term improves the recall-prediction performance of exponential forgetting curve memory models.](delay-term-improves-exponential-forgetting-curve-recall-prediction.md) — related
- [In Mnemosyne log data, setting memory strength equal to an item's Leitner deck position predicts recall better than number of past reviews, which beats constant strength.](leitner-deck-position-predicts-recall-better-than-review-count.md) — related
- [In Mnemosyne log data, exponential forgetting curve models that include a delay term perform comparably to 1PL-IRT, the best-performing benchmark model.](exponential-forgetting-models-with-delay-perform-comparably-to-1pl-irt.md) — related
- Correlation between log response time and response likelihood is negative for almost all items, and its magnitude depends on the item difficulty parameter — related
- [A one-parameter IRT model outperforms global and per-pitch baselines on AUC, BCE and Brier score but not on threshold accuracy for held-out singing attempts](irt-outperforms-baselines-discrimination-not-accuracy.md) — related
- [Item difficulty was best predicted using signal from the item stem](difficulty-best-predicted-from-item-stem.md) — related
- [All models predict performance worst for students of intermediate overall ability, with best performance for high and low performing students](mid-ability-students-hardest-to-predict.md) — related
