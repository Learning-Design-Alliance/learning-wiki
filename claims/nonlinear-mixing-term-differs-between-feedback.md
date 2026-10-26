---
type: claim
title: Under global feedback, learning reflects significant non-linear mixing of color and orientation, while the linear mixing term does not differ between feedback regimes
description: Under global feedback, learning reflects significant non-linear mixing of color and orientation, while the linear mixing term does not differ between feedback regimes
id: nonlinear-mixing-term-differs-between-feedback
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-26
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: behnam-karami-caspar-m-schwiedrzik-2024
    resource: "https://doi.org/10.1038/s41539-024-00226-w"
    title: "Behnam Karami & Caspar M. Schwiedrzik. (2024). Visual perceptual learning of feature conjunctions leverages non-linear mixed selectivity. npj Science of Learning. https://doi.org/10.1038/s41539-024-00226-w"
    author: "Behnam Karami & Caspar M. Schwiedrzik"
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Under global feedback, learning reflects significant non-linear mixing of color and orientation, while the linear mixing term does not differ between feedback regimes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i?` The non-linear mixed learning term (NM×Block) differed significantly between the global and feature-specific feedback experiments, favoring Experiment 1 (β = 0.0244), whereas the linear term did not (β = −0.0061, p = 0.2558). [→ Behnam Karami & Caspar M. Schwiedrzik 2024](#behnam-karami-caspar-m-schwiedrzik-2024)

## Evidence

### Behnam Karami & Caspar M. Schwiedrzik 2024

Behnam Karami & Caspar M. Schwiedrzik. (2024). Visual perceptual learning of feature conjunctions leverages non-linear mixed selectivity. npj Science of Learning. https://doi.org/10.1038/s41539-024-00226-w

`q2 · i?` · `causal · r1`

GLME modeling pooled across Experiments 1 and 2, with experiment as a categorical moderator of linear (sum) and non-linear (product) mixing predictors of accuracy. The "non-linear learning term" showed a significant difference (β = 0.0244, p < 10−8) favoring Experiment 1; the β values are unstandardized GLME coefficients, so no effect size magnitude is coded.

> "The non-linear learning term (NM×Block) signiﬁcantly differed between experiments (NM × Block × Exp: β = 0.0244,p <1 0−8), while the linear learning term did not (LM×Block×Exp: β = −0.0061, p =0 . 2 5 5 8 )"

## Discussion


## Related Claims
- [Conjunction learning transfers partially to new spatial locations, with color showing larger transfer indices than orientation, indicating pure selectivity neurons also participate alongside mixed selectivity](differential-location-transfer-conjunction-learning.md) — related
- [Global conjunction-level feedback yields faster and greater conjunction learning than feature-specific feedback in orientation-color conjunction training](global-feedback-faster-conjunction-learning.md) — related
- [Orientation learning with salient task-irrelevant color (Experiment 4) is smaller than orientation learning under global feedback (Experiment 1) or attended single-feature training (Experiment 3), but not smaller than feature-specific feedback (Experiment 2)](irrelevant-color-impairs-orientation-learning.md) — related
- [Months after conjunction training, the global-feedback group showed significantly larger non-linear mixing on an XOR transfer task than the feature-specific group, though average XOR accuracy did not differ between groups](xor-transfer-nonlinear-mixing-advantage.md) — related
- [Conjunction benefit of global feedback is not due to higher cognitive load of dual feature updates: post-cued single-feature training (Experiment 3) does not match global-feedback conjunction learning](separate-feature-training-does-not-match-global-feedback.md) — related
- [A mixed-channel reinforcement learning model better explains choices after global feedback, and a separate-channel model better explains choices after feature-specific feedback](mixed-channel-rl-model-fit.md) — related
