---
type: claim
title: Editing questions according to a hypothesis shifts measured difficulty in the expected direction
description: Editing questions according to a hypothesis shifts measured difficulty in the expected direction
id: hypothesis-guided-editing-shifts-difficulty-causally
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: peng-cui-2026
    resource: "https://doi.org/10.48550/arxiv.2610.01627"
    title: "Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627 [doi:10.48550/arxiv.2610.01627](https://doi.org/10.48550/arxiv.2610.01627)"
    author: Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Editing questions according to a hypothesis shifts measured difficulty in the expected direction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Hypothesis-guided increase edits reduce mean accuracy by 15.27 and 23.88 percentage points on GSM8K and BBH-structured, while decrease edits improve it by 32.18 and 28.52 points, with directional consistency across most edited questions. [→ Peng Cui 2026](#peng-cui-2026)

## Evidence

### Peng Cui 2026

Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627 [doi:10.48550/arxiv.2610.01627](https://doi.org/10.48550/arxiv.2610.01627)

`q2 · i?` · `causal · r1`

Counterfactual editing experiment (Table 4) on 50 randomly sampled test questions per dataset, re-evaluated on a subset of LLMs under 30B with accuracy as a difficulty proxy. The article reports the printed accuracy shifts and success rates of 70.9% and 92.2% on GSM8K.

> "Increase-difficulty edits reduce mean accuracy by 15.27 and 23.88 percentage points on GSM8K and BBH-structured, respectively, while decrease-difficulty edits improve it by 32.18 and 28.52 points."

## Discussion


## Related Claims
- [Generated hypotheses discriminate hard from easy questions, mostly with medium-to-large effects](hypotheses-discriminate-difficulty-effect-sizes.md) — related
- [Hypothesis-based predictors match or beat black-box difficulty regressors on unseen questions](hypothesis-predictor-matches-black-box-regressors.md) — related
- [The benefit of high- versus low-contrast sampling depends on the dataset](contrast-strength-benefit-is-dataset-dependent.md) — related
- [Mixing group-wise and pair-wise contrastive sampling yields better hypotheses than either alone](mixing-group-and-pair-sampling-beats-either-alone.md) — related
- [Adding generated hypotheses as features improves black-box difficulty predictors](hypothesis-features-improve-difficulty-predictors.md) — related
- [LLM difficulty labels track structural question features: stem length, option length, and digits in stems rise monotonically across Easy, Medium, and Hard labels](llm-difficulty-labels-track-structural-item-features.md) — related
- [Success rates decrease monotonically from easy to medium to hard difficulty levels across all models](monotonic-difficulty-decline-turtleai.md) — related
