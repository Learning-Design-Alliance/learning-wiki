---
type: claim
title: "Mistral-7B reward model outperforms GPT2-XL on Hit@k ranking and Pairwise Accuracy for proxy preference discrimination, at higher computational cost"
description: "Mistral-7B reward model outperforms GPT2-XL on Hit@k ranking and Pairwise Accuracy for proxy preference discrimination, at higher computational cost"
id: mistral-reward-model-beats-gpt2-xl
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: zhenxin-zhang-2026
    resource: "https://doi.org/10.1186/s41239-026-00607-8"
    title: "Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang. (2026). RACES: reward-aligned consistent essay scoring with large language models. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00607-8"
    author: Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Mistral-7B reward model outperforms GPT2-XL on Hit@k ranking and Pairwise Accuracy for proxy preference discrimination, at higher computational cost

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Mistral-7B achieves higher Hit@k than GPT2-XL (Hit@1 about 4.5% higher) and maintains about 5.4% higher Pairwise Accuracy after roughly 350 steps, while GPT2-XL remains useful in resource-constrained settings. [→ Zhenxin Zhang 2026](#zhenxin-zhang-2026)

## Evidence

### Zhenxin Zhang 2026

Zhenxin Zhang, Ziyu Ding, Mengyun Liu and Haiwei Sang. (2026). RACES: reward-aligned consistent essay scoring with large language models. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00607-8

`q2 · i?` · `design · r2`

Comparative numerical analysis of two reward models (Figs. 3–4) on essay scoring and proxy response discrimination; both converged rapidly, reaching 73.9% and 63.1% Pairwise Accuracy within about 50 training steps. The article frames this as "a trade-off between reward-model accuracy and computational efficiency".

> "Mistral-7B achieves higher Hit@k performance than GPT2-XL, with its Hit@1 score approximately 4.5% higher. This difference may be attributed to the stronger contextual representation capacity of Mistral-7B"

## Discussion


## Related Claims
- [RACES configurations improve QWK essay-scoring agreement over evaluated pretrained baselines on ASAP 2.0, with LLaMA2-7B-based configurations slightly outperforming Qwen2.5-Instruct-7B-based ones](races-improves-qwk-over-evaluated-baselines.md) — related
- [Both reward models converge rapidly, reaching stable Hit@k performance around 200–250 training steps and above-baseline Hit@3 within about 50 steps](races-reward-models-rapid-convergence.md) — related
