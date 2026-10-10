---
type: strategy
id: accent-fair-threshold-calibration
title: Calibrate coaching thresholds per L1 cohort and avoid penalizing identity-marking accent features
description: "In its ethics statement, the survey sets out accent-fairness principles for deployed coaching systems: \"Calibrate thresholds per L1 cohort to account for systematic phonetic differences\"; report subgroup metrics such..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: wen-liang-2026
    resource: "https://arxiv.org/abs/2606.27380"
    title: "Wen Liang, Li Siyan, Zackary Rackauckas, and Julia Hirschberg. (2026). A Survey of Automated Presentation Coaching: Systems, Methods, and Open Challenges. https://arxiv.org/abs/2606.27380"
    author: Wen Liang, Li Siyan, Zackary Rackauckas, and Julia Hirschberg
---

# Calibrate coaching thresholds per L1 cohort and avoid penalizing identity-marking accent features

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
In its ethics statement, the survey sets out accent-fairness principles for deployed coaching systems: "Calibrate thresholds per L1 cohort to account for systematic phonetic differences"; report subgroup metrics such as precision and recall by L1 to identify potential biases; and avoid penalizing identity-marking phonetic features when intelligibility is unaffected. Systems should help learners improve clarity without erasing accent identity, presenting prosodic feedback as optional stylistic guidance rather than prescriptive judgments.

## Design Implications

### Context
#### Requirements
- Per-L1 threshold calibration on rated sets, subgroup metric reporting by L1, and feedback framed as optional stylistic guidance.
#### Constraints
- The survey states that practical implementation of accent-fair thresholds and privacy-preserving systems requires more extensive validation in deployed settings.

### Target Learners
- L2 English speakers from diverse L1 backgrounds using automated coaching systems

### Target Learning Goals
- Fair, non-biased pronunciation and prosody feedback that preserves accent identity while improving intelligibility

## Related Strategies

- [Mitigating Racial Bias in Edtech Products](mitigating_racial_bias_in_edtech_products.md)
- [Create small controlled presentation mini-sets as a near-term community benchmark](presentation-mini-sets-community-benchmark.md)

## Examples
-

## Key Sources
- Wen Liang, Li Siyan, Zackary Rackauckas, and Julia Hirschberg. (2026). A Survey of Automated Presentation Coaching: Systems, Methods, and Open Challenges. https://arxiv.org/abs/2606.27380
