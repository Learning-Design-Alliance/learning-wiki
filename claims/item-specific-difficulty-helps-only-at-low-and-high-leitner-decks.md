---
type: claim
title: In Mnemosyne log data, item-specific difficulty parameters outperform a global difficulty for lower and higher Leitner decks, while global difficulty performs better for intermediate decks.
description: In Mnemosyne log data, item-specific difficulty parameters outperform a global difficulty for lower and higher Leitner decks, while global difficulty performs better for intermediate decks.
id: item-specific-difficulty-helps-only-at-low-and-high-leitner-decks
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: mixed
sources:
  - id: reddy-2016
    resource: "https://doi.org/10.1145/2939672.2939850"
    title: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850"
    author: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T"
---

# In Mnemosyne log data, item-specific difficulty parameters outperform a global difficulty for lower and higher Leitner decks, while global difficulty performs better for intermediate decks.

> **Claim** · [All claims](index.md)

## Subclaims
`q2 i?` Item-specific difficulties outperformed a global item difficulty for decks q ≤ 2 and q > 5, but the global difficulty performed better for intermediate decks; no numeric AUC values are printed. [→ Reddy 2016](#reddy-2016)

## Evidence

### Reddy 2016

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q2 · i?`

Observational study of Mnemosyne flashcard log data, comparing memory models by cross-validated validation AUC per deck bin. "Item-speciﬁc diﬃculties θi outperform global item diﬃculty θ for lower decks" and higher decks, but the global parameter did better for intermediate decks (models 5 vs. 10, 8 vs. 13).

> "Item-speciﬁc diﬃculties θi outperform global item diﬃculty θ for lower decks (qij≤ 2) and higher decks ( qij > 5), but the global dif- ﬁculty performs better for intermediate decks (model 5 vs. 10, 8 vs. 13)"

## Discussion


## Related Claims
-
