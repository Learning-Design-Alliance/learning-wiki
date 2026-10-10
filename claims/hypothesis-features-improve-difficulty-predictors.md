---
type: claim
title: Adding generated hypotheses as features improves black-box difficulty predictors
description: Adding generated hypotheses as features improves black-box difficulty predictors
id: hypothesis-features-improve-difficulty-predictors
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
    kind: associational
    rigour: 2
---

# Adding generated hypotheses as features improves black-box difficulty predictors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`

## Subclaims
`q2 i?` Supplying hypothesis-match vectors as additional features raises test R² of RoBERTa-base and frozen-embedding regressors, with the largest gains on GSM8K (+0.19, +0.18, and +0.11 over finetuned RoBERTa). [→ Peng Cui 2026](#peng-cui-2026)

## Evidence

### Peng Cui 2026

Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627

`q2 · i?` · `associational · r2`

Feature-augmentation experiment (Figure 3): hypothesis-match vectors are added as a second feature block to three semantic predictors. The article reports gains "largest on GSM8K:+0.19and+0.18over the two frozen embeddings, and+0.11even over the fine-tuned RoBERTa".

> "The gains are largest on GSM8K:+0.19and+0.18over the two frozen embeddings, and+0.11even over the fine-tuned RoBERTa (0.362→0.468), by far the strongest baseline there."

## Discussion


## Related Claims
- [Baseline hypothesis generators saturate after 5–10 effective hypotheses while the proposed method keeps improving](baseline-generators-saturate-proposed-method-keeps-improving.md) — related
- [Generated hypotheses discriminate hard from easy questions, mostly with medium-to-large effects](hypotheses-discriminate-difficulty-effect-sizes.md) — related
- [Hypothesis-based predictors match or beat black-box difficulty regressors on unseen questions](hypothesis-predictor-matches-black-box-regressors.md) — related
- [Editing questions according to a hypothesis shifts measured difficulty in the expected direction](hypothesis-guided-editing-shifts-difficulty-causally.md) — related
