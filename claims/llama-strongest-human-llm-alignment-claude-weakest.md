---
type: claim
title: Llama 4 Maverick shows the strongest human-LLM alignment, while Claude Sonnet 4 performs weakest with poor calibration
description: Llama 4 Maverick shows the strongest human-LLM alignment, while Claude Sonnet 4 performs weakest with poor calibration
id: llama-strongest-human-llm-alignment-claude-weakest
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: tongxi-liu-2026
    resource: "https://doi.org/10.1016/j.caeai.2026.100565"
    title: "Tongxi Liu, Luyao Ye, Wei Yan. (2026). A framework for evaluation of large language models in essay assessment: Reliability, alignment, and causal reasoning. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100565"
    author: Tongxi Liu, Luyao Ye, Wei Yan
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Llama 4 Maverick shows the strongest human-LLM alignment, while Claude Sonnet 4 performs weakest with poor calibration

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`

## Subclaims
`q2 i?` Llama 4 Maverick achieved the strongest correspondence with human ratings (r = 0.45-0.63; MAE = 0.67-1.11) with minimal mean bias, whereas Claude Sonnet 4 performed weakest (r = 0.22-0.47; MAE up to 1.52) with generally negative biases. [→ Tongxi Liu 2026](#tongxi-liu-2026)

## Evidence

### Tongxi Liu 2026

Tongxi Liu, Luyao Ye, Wei Yan. (2026). A framework for evaluation of large language models in essay assessment: Reliability, alignment, and causal reasoning. Computers and Education: Artificial Intelligence. https://doi.org/10.1016/j.caeai.2026.100565

`q2 · i?` · `associational · r1`

Human-LLM alignment analysis (Pearson r, MAE, Bland-Altman bias) of five LLMs against three calibrated expert raters on 60 essays, reported in Results §4.3. The article names Claude Sonnet 4 as weakest with the printed correlation, error, and bias values.

> "Claude Sonnet 4 performed weakest (r = 0.22-0.47; MAE up to 1.52) with generally negative biases (e.g.,  0.79 for Coherence Cohesion), indicating poor calibration and low discriminative power."

## Discussion


## Related Claims
- [In one study of repeated LLM scoring of 60 IELTS essays, Gemini 2.5 Flash was moderately reliable (ICC 0.63-0.75) while Claude Sonnet 4 and DeepSeek R1 stayed below 0.70 in most dimensions](llm-essay-scoring-reliability-stratification.md) — related
- [Grammatical Accuracy is the most stable and objective scoring dimension for LLMs, while Task Response is the most challenging](grammatical-accuracy-most-stable-llm-scoring-dimension.md) — related
