---
type: claim
title: Hypothesis-based predictors match or beat black-box difficulty regressors on unseen questions
description: Hypothesis-based predictors match or beat black-box difficulty regressors on unseen questions
id: hypothesis-predictor-matches-black-box-regressors
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

# Hypothesis-based predictors match or beat black-box difficulty regressors on unseen questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` An OLS regressor on hypothesis-match features achieves the best out-of-sample R² on GSM8K and WinoGrande and second best on BBH-structured against finetuned, embedding-based, and few-shot baselines. [→ Peng Cui 2026](#peng-cui-2026)

## Evidence

### Peng Cui 2026

Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627

`q2 · i?` · `causal · r1`

Out-of-sample evaluation (Table 2): an OLS regressor trained on G∪V with hypothesis-match features is tested on T against RoBERTa-base finetuned, frozen embeddings, and 10-shot prompting of frontier LLMs. The article reports "the best performance on two datasets, GSM8K and WinoGrande".

> "Overall, our model achieves the best performance on two datasets, GSM8K and WinoGrande, and the second best on BBH-structured, showing that these features alone already constitute a strong difficulty predictor."

## Discussion


## Related Claims
- [Generated hypotheses discriminate hard from easy questions, mostly with medium-to-large effects](hypotheses-discriminate-difficulty-effect-sizes.md) — related
- [Adding generated hypotheses as features improves black-box difficulty predictors](hypothesis-features-improve-difficulty-predictors.md) — related
- [Editing questions according to a hypothesis shifts measured difficulty in the expected direction](hypothesis-guided-editing-shifts-difficulty-causally.md) — related
