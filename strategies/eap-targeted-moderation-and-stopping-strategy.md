---
type: strategy
id: eap-targeted-moderation-and-stopping-strategy
title: Use EAP-flagged low-agreement pairs to target moderator effort and to set a principled stopping criterion for data collection
description: This strategy uses the EAP reliability metric to concentrate human moderation where it matters and to decide when enough comparisons have been collected.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: andy-gray-2025
    resource: "https://arxiv.org/abs/2503.00479"
    title: "Andy Gray, Alma Rahat, Tom Crick, Stephen Lindsay. (2025). Bayesian Active Learning for Comparative Judgement: Reliability Estimation and Multi-Criteria Evaluation with Applications in Educational Assessment. https://arxiv.org/abs/2503.00479"
    author: Andy Gray, Alma Rahat, Tom Crick, Stephen Lindsay
---

# Use EAP-flagged low-agreement pairs to target moderator effort and to set a principled stopping criterion for data collection

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
This strategy uses the EAP reliability metric to concentrate human moderation where it matters and to decide when enough comparisons have been collected. The article shows that "By flagging item pairs with low agreement (EAP < 50%), the PM could concentrate on the most contentious comparisons and make a judgement on which item should be considered superior." Separately, an assignment owner can set lower and upper bounds on an acceptable agreement range and compute the minimum MAP or EAP threshold required before stopping further data collection, e.g. a 95% threshold equivalent to a 2.5%–97.5% range.

## Design Implications

### Context
#### Requirements
- A chosen confidence level or null-space range from which the MAP/EAP stopping threshold is derived
- A moderator available to adjudicate flagged contentious pairs
#### Constraints
- MAP alone can be overly optimistic because it does not consider the level of existing uncertainty

### Target Learners
- students whose open-ended work is assessed via comparative judgement

### Target Learning Goals
- reliable, efficient assessment and targeted feedback on open-ended work

## Claims

- [In a simulated moderation exercise on DREsS data, flagging low-EAP pairs for a principal moderator corrected two of three misordered pairs](../claims/eap-flagged-moderation-corrects-misordered-pairs.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Andy Gray, Alma Rahat, Tom Crick, Stephen Lindsay. (2025). Bayesian Active Learning for Comparative Judgement: Reliability Estimation and Multi-Criteria Evaluation with Applications in Educational Assessment. https://arxiv.org/abs/2503.00479
