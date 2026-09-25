---
type: claim
title: "In Mnemosyne log data, setting memory strength equal to an item's Leitner deck position predicts recall better than number of past reviews, which beats constant strength."
description: "In Mnemosyne log data, setting memory strength equal to an item's Leitner deck position predicts recall better than number of past reviews, which beats constant strength."
id: leitner-deck-position-predicts-recall-better-than-review-count
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

# In Mnemosyne log data, setting memory strength equal to an item's Leitner deck position predicts recall better than number of past reviews, which beats constant strength.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q2` quasi-experiment

## Subclaims
`q2 i?` Memory strength set to Leitner deck position outperformed strength proportional to the number of past reviews, which in turn outperformed a constant strength, by validation and test AUC; no AUC values are printed in the text. [→ Reddy 2016](#reddy-2016)

## Evidence

### Reddy 2016

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q2 · i?`

Observational study of Mnemosyne flashcard log data, comparing memory models by cross-validated validation AUC and a held-out test set. Setting strength to the "Leitner deck position qij performs better than setting it to be proportional to the number of past reviews nij", itself better than constant s (Fig. 3); no numbers printed.

> "Setting the mem- ory strength s to be equal to the Leitner deck position qij performs better than setting it to be proportional to the number of past reviews nij, which in turn is better than using a constant s"

## Discussion


## Related Claims
-
