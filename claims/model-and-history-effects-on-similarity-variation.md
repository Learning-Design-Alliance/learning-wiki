---
type: claim
title: GPT-5.4 showed higher variation in pairwise reply similarity than GPT-4o mini, GPT-5.4 nano significantly lower, and with-history increased variation for the reference model
description: GPT-5.4 showed higher variation in pairwise reply similarity than GPT-4o mini, GPT-5.4 nano significantly lower, and with-history increased variation for the reference model
id: model-and-history-effects-on-similarity-variation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jiangang-hao-2026
    resource: "https://arxiv.org/abs/2608.24920"
    title: "Jiangang Hao. (2026). Semantic Variability of LLM-Generated Replies Across LLMs: Implications for Designing Conversation-Based Assessment. Accepted to AI in Measurement and Education Conference – AIME 2026. https://arxiv.org/abs/2608.24920"
    author: Jiangang Hao
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# GPT-5.4 showed higher variation in pairwise reply similarity than GPT-4o mini, GPT-5.4 nano significantly lower, and with-history increased variation for the reference model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` In the Similarity Variation Model, GPT-5.4 showed higher variation than GPT-4o mini (estimate 0.0202, p = 0.002), GPT-5.4 nano significantly lower (estimate -0.0372, p < .001), and With History increased variation for GPT-4o mini (estimate 0.0162, p = 0.011). [→ Jiangang Hao 2026](#jiangang-hao-2026)

## Evidence

### Jiangang Hao 2026

Jiangang Hao. (2026). Semantic Variability of LLM-Generated Replies Across LLMs: Implications for Designing Conversation-Based Assessment. Accepted to AI in Measurement and Education Conference – AIME 2026. https://arxiv.org/abs/2608.24920

`q2 · i?` · `causal · r1`

Linear mixed-effects model on the standard deviation of pairwise similarities (Table 2; N = 488, 61 focal messages). "GPT-5.4 nano showed sig- nificantly lower variation."

> "For the Similarity Variation Model, GPT-5.4 showed higher variation in pairwise similarity than GPT-4o mini, whereas GPT-5.4 nano showed sig- nificantly lower variation. The with-history con- dition increased variation for the reference model, GPT-4o mini."

## Discussion


## Related Claims
- [GPT-5.4 showed the highest within-model reply similarity, and models within the GPT-5.4 family were more similar to one another than to GPT-4o mini](gpt54-family-lineage-response-consistency.md) — related
- [Chat history lowered mean pairwise reply similarity for GPT-4o mini, but GPT-5.4 and GPT-5.4 mini were less negatively affected, indicating the effect of history differs across models](history-effect-on-mean-similarity-varies-by-model.md) — related
