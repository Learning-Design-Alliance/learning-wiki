---
type: claim
title: "Users' baseline ranking accuracy significantly predicts the quality of the AI assistant's advice"
description: "Users' baseline ranking accuracy significantly predicts the quality of the AI assistant's advice"
id: baseline-accuracy-predicts-advice-quality
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: cansu-koyuturk-2026
    resource: "https://arxiv.org/abs/2605.18372"
    title: "Cansu Koyuturk, Sabrina Guidotti, and Dimitri Ognibene. (2026). The Hidden Cost of Contextual Sycophancy: an AI Literacy Intervention in Human–AI Collaboration. https://arxiv.org/abs/2605.18372"
    author: Cansu Koyuturk, Sabrina Guidotti, and Dimitri Ognibene
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Users' baseline ranking accuracy significantly predicts the quality of the AI assistant's advice

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` Baseline ranking accuracy significantly predicted AI advice quality (b = 0.478, p = .008), indicating lower-quality initial responses lead to poorer AI advice. [→ Cansu Koyuturk 2026](#cansu-koyuturk-2026)

## Evidence

### Cansu Koyuturk 2026

Cansu Koyuturk, Sabrina Guidotti, and Dimitri Ognibene. (2026). The Hidden Cost of Contextual Sycophancy: an AI Literacy Intervention in Human–AI Collaboration. https://arxiv.org/abs/2605.18372

`q3 · i?` · `causal · r2`

Regression of AI advice quality (NDCG@6 of the assistant's top-6 recommendations, extracted via an LLM-as-judge pipeline) on baseline ranking accuracy and condition in the 60-participant experiment. The article reports "b = 0.478, SE = 0.180, z = 2.65, p = .008, 95% CI [0.125, 0.831]".

> "Baseline accuracy significantly predicted advice quality, b = 0.478, SE = 0.180, z = 2.65, p = .008, 95% CI [0.125, 0.831]."

## Discussion


## Related Claims
- [Carryover of user errors into AI advice reduces both advice quality and final ranking accuracy](error-carryover-reduces-advice-quality-and-performance.md) — related
- [Users' baseline ranking accuracy significantly predicts their final ranking accuracy after AI collaboration, with no other significant effects](baseline-accuracy-predicts-final-ranking-accuracy.md) — related
