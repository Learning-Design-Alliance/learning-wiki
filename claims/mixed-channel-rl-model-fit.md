---
type: claim
title: A mixed-channel reinforcement learning model better explains choices after global feedback, and a separate-channel model better explains choices after feature-specific feedback
description: A mixed-channel reinforcement learning model better explains choices after global feedback, and a separate-channel model better explains choices after feature-specific feedback
id: mixed-channel-rl-model-fit
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
    i: 3
    kind: causal
    rigour: 2
---

# A mixed-channel reinforcement learning model better explains choices after global feedback, and a separate-channel model better explains choices after feature-specific feedback

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i3` large
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i3` MRL had smaller deviance from subjects' choices than SRL in Experiment 1 (p = 0.0003, d = 2.0030), and SRL fit better in Experiment 2 (p = 0.0038, d = −0.9100). [→ Behnam Karami & Caspar M. Schwiedrzik 2024](#behnam-karami-caspar-m-schwiedrzik-2024)

## Evidence

### Behnam Karami & Caspar M. Schwiedrzik 2024

Behnam Karami & Caspar M. Schwiedrzik. (2024). Visual perceptual learning of feature conjunctions leverages non-linear mixed selectivity. npj Science of Learning. https://doi.org/10.1038/s41539-024-00226-w

`q2 · i3` · `causal · r2`

Model-comparison analysis fitting two reinforcement learning models (mixed-channel MRL vs. separate-channel SRL) to trial-by-trial choices during training in Experiments 1 and 2, evaluated against Test-day subject performance. Signed-rank tests of "deviance" from subjects' choices support the "MRL had smaller deviance" result in Experiment 1 (d = 2.0030) and the reverse in Experiment 2 (d = −0.9100).

> "MRL had smaller deviance as compared to SRL in Experiment 1 and vice versa in Experiment 2 (signed-rank test, MRL vs. SRL, Experiment 1: p = 0.0003,d = 2.0030, Experiment 2: p = 0.0038,d = −0.9100)"

## Discussion


## Related Claims
- [Global conjunction-level feedback yields faster and greater conjunction learning than feature-specific feedback in orientation-color conjunction training](global-feedback-faster-conjunction-learning.md) — related
- [Months after conjunction training, the global-feedback group showed significantly larger non-linear mixing on an XOR transfer task than the feature-specific group, though average XOR accuracy did not differ between groups](xor-transfer-nonlinear-mixing-advantage.md) — possibly the same claim (merge candidate)
- [Under global feedback, learning reflects significant non-linear mixing of color and orientation, while the linear mixing term does not differ between feedback regimes](nonlinear-mixing-term-differs-between-feedback.md) — related
- [Conjunction benefit of global feedback is not due to higher cognitive load of dual feature updates: post-cued single-feature training (Experiment 3) does not match global-feedback conjunction learning](separate-feature-training-does-not-match-global-feedback.md) — related
