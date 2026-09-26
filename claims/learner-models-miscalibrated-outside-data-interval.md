---
type: claim
title: Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models
description: Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models
id: learner-models-miscalibrated-outside-data-interval
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
evidence_strength: moderate
sources:
  - id: theophile-gervet-2020
    resource: "https://github.com/theophilee/learner-performance-prediction"
    title: "Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction"
    author: Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell
    q: 2
    i: 2
  - id: theophile-gervet-2020-2
    resource: "https://github.com/theophilee/learner-performance-prediction"
    title: "Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction"
    author: Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell
    q: 2
    i: 1
---

# Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q2` quasi-experiment · `i1`–`i2`

## Subclaims
`q2 i?` On assistments09, both Best-LR and DKT severely overestimate learners when the probability of correct answer is low and underestimate when it is high. [→ Theophile Gervet 2020](#theophile-gervet-2020)
`q2 i?` In general, models are calibrated only in the interval containing most of the data; on large datasets like squirrel both models are close to perfectly calibrated. [→ Theophile Gervet 2020 (2)](#theophile-gervet-2020-2)

## Evidence

### Theophile Gervet 2020

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i2`

Calibration analysis (Figure 9) of Best-LR and DKT binned by item-wise observed frequency of correctness. "both models severely overestimate learners when the probability of correct answer is low"; no standard technique can correct these biases.

> "on the assistments09 dataset, both models severely overestimate learners when the probability of correct answer is low, and underestimate learners when the probability of correct answer is high"

### Theophile Gervet 2020 (2)

Theophile Gervet, Ken Koedinger, Jeff Schneider, Tom Mitchell (2020). When is Deep Learning the Best Approach to Knowledge Tracing? Journal of Educational Data Mining, Volume 12, No 3. https://github.com/theophilee/learner-performance-prediction

`q2 · i1`

Section 8 calibration analysis with reliability diagrams binned by predicted and observed probabilities; calibration plots binned by predicted probabilities revealed no biases, while observed-probability bins revealed systematic ones.

> "In general, models are calibrated only in the interval containing most of the data."

## Discussion


## Related Claims
-
