---
type: claim
title: Under the Leitner Queue Network model, raising the rate of new-item introduction beyond a threshold causes a phase transition in learning rate, which a Mechanical Turk vocabulary experiment reproduced.
description: Under the Leitner Queue Network model, raising the rate of new-item introduction beyond a threshold causes a phase transition in learning rate, which a Mechanical Turk vocabulary experiment reproduced.
id: leitner-queue-network-phase-transition-in-learning-rate
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
evidence_strength: moderate
sources:
  - id: reddy-2016
    resource: "https://doi.org/10.1145/2939672.2939850"
    title: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850"
    author: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T"
  - id: reddy-2016-2
    resource: "https://doi.org/10.1145/2939672.2939850"
    title: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850"
    author: "Reddy, S., Labutov, I., Banerjee, S., & Joachims, T"
---

# Under the Leitner Queue Network model, raising the rate of new-item introduction beyond a threshold causes a phase transition in learning rate, which a Mechanical Turk vocabulary experiment reproduced.

> **Claim** · [All claims](index.md)

## Subclaims
`q1 i?` Under the mean-recall approximation, when the arrival rate exceeds the threshold the lowest Leitner deck accumulates items and delays blow up, so the learning rate goes to 0. [→ Reddy 2016](#reddy-2016)
`q2 i?` Empirical learning rates from the MTurk arrival-rate conditions closely agreed with the simulated Leitner Queue Network curve and showed the predicted phase transition. [→ Reddy 2016 (2)](#reddy-2016-2)

## Evidence

### Reddy 2016

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q1 · i?`

Analytical result derived under the mean-recall approximation of the Leitner Queue Network. The article derives that above threshold the lowest deck "experiences packet accumulation and delay blow-up" and the learning rate goes to 0.

> "Moreover, if λext > λt, then the lowest Leitner deck (i.e., Q1) experiences packet accumulation and delay blow-up, and thus the learning rate λout goes to 0."

### Reddy 2016 (2)

Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded Human Learning: Optimal Scheduling for Spaced Repetition. KDD ’16, San Francisco, CA, USA. https://doi.org/10.1145/2939672.2939850

`q2 · i?`

Mechanical Turk vocabulary-learning experiment (Japanese words or American Sign Language gestures) with participants assigned to arrival-rate conditions. "The simulated and empirical curves are in close agreement"; the data show the predicted phase transition (Fig. 14). No test statistic is printed.

> "The simulated and empirical curves are in close agreement; in particular, the MTurk data shows the phase transition in learning rate predicted by our theoretical model."

## Discussion


## Related Claims
- [Spaced Repetition Improves Retention](spaced-repetition-improves-retention.md)
