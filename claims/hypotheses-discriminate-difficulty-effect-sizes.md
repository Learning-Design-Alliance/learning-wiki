---
type: claim
title: Generated hypotheses discriminate hard from easy questions, mostly with medium-to-large effects
description: Generated hypotheses discriminate hard from easy questions, mostly with medium-to-large effects
id: hypotheses-discriminate-difficulty-effect-sizes
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: peng-cui-2026
    resource: "https://arxiv.org/abs/2610.01627"
    title: "Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627"
    author: Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Generated hypotheses discriminate hard from easy questions, mostly with medium-to-large effects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` On GSM8K and BBH-structured, 9/10 top hypotheses reach at least a medium effect separating matched from unmatched items, and half reach a large effect; on Winogrande the effects are weaker. [→ Peng Cui 2026](#peng-cui-2026)

## Evidence

### Peng Cui 2026

Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627

`q2 · i?` · `causal · r1`

Numerical evaluation of top hypotheses on three benchmarks (Table 1), reporting SEP with 95% bootstrap CIs and Cohen's d between matched and unmatched test items. The article reports "the 95% CI of SEP has a lower bound above zero for 13/15 hypotheses" and medium-to-large effects outside WinoGrande.

> "the 95% CI of SEP has a lower bound above zero for 13/15 hypotheses, showing that they genuinely discriminate between hard and easy items. Except on Winogrande, whose difficulty is known to be hard to perceive even for humans (Ding et al., 2024), 9/10 hypotheses on the two other datasets reach at least a medium effect†, and half of them reach a large effect‡."

## Discussion


## Related Claims
- [Hypothesis-based predictors match or beat black-box difficulty regressors on unseen questions](hypothesis-predictor-matches-black-box-regressors.md) — related
- [Mixing group-wise and pair-wise contrastive sampling yields better hypotheses than either alone](mixing-group-and-pair-sampling-beats-either-alone.md) — related
- [The benefit of high- versus low-contrast sampling depends on the dataset](contrast-strength-benefit-is-dataset-dependent.md) — related
- [Editing questions according to a hypothesis shifts measured difficulty in the expected direction](hypothesis-guided-editing-shifts-difficulty-causally.md) — related
- [Adding generated hypotheses as features improves black-box difficulty predictors](hypothesis-features-improve-difficulty-predictors.md) — related
