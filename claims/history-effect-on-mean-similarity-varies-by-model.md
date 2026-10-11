---
type: claim
title: Chat history lowered mean pairwise reply similarity for GPT-4o mini, but GPT-5.4 and GPT-5.4 mini were less negatively affected, indicating the effect of history differs across models
description: Chat history lowered mean pairwise reply similarity for GPT-4o mini, but GPT-5.4 and GPT-5.4 mini were less negatively affected, indicating the effect of history differs across models
id: history-effect-on-mean-similarity-varies-by-model
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
    rigour: 2
---

# Chat history lowered mean pairwise reply similarity for GPT-4o mini, but GPT-5.4 and GPT-5.4 mini were less negatively affected, indicating the effect of history differs across models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` In the mixed-effects Similarity Mean Model, the With History fixed effect was negative for the reference model GPT-4o mini (estimate -0.0415, p = 0.006), while the GPT-5.4×With History (0.0534, p = 0.012) and GPT-5.4 mini×With History (0.0505, p = 0.017) interactions were positive and statistically significant. [→ Jiangang Hao 2026](#jiangang-hao-2026)

## Evidence

### Jiangang Hao 2026

Jiangang Hao. (2026). Semantic Variability of LLM-Generated Replies Across LLMs: Implications for Designing Conversation-Based Assessment. Accepted to AI in Measurement and Education Conference – AIME 2026. https://arxiv.org/abs/2608.24920

`q2 · i?` · `causal · r2`

Linear mixed-effects model (Table 1; N = 488, 61 focal messages, random intercept for focal message) with LLM type, history condition, their interaction, and LLM-human similarity as fixed effects. "the interaction terms for GPT-5.4 and GPT-5.4 mini were positive and statistically significant."

> "For the Similarity Mean Model, the with-history condition was associated with lower mean pairwise similarity for the reference model, GPT-4o mini. However, the interaction terms for GPT-5.4 and GPT-5.4 mini were positive and statistically significant."

## Discussion


## Related Claims
- [Replies generated with chat history were only moderately similar to replies generated without history (median cross-history similarity around 0.40 to 0.45)](chat-history-changes-reply-semantic-content.md) — related
- [Without chat history, semantically similar focal messages elicited similar LLM replies; this positive relationship was weaker when history was included](focal-message-similarity-predicts-reply-similarity-no-history.md) — related
- [GPT-5.4 showed the highest within-model reply similarity, and models within the GPT-5.4 family were more similar to one another than to GPT-4o mini](gpt54-family-lineage-response-consistency.md) — related
- [GPT-5.4 showed higher variation in pairwise reply similarity than GPT-4o mini, GPT-5.4 nano significantly lower, and with-history increased variation for the reference model](model-and-history-effects-on-similarity-variation.md) — related
- [LLM-generated replies were consistently not similar to human replies, though including chat history slightly improved alignment](llm-replies-low-alignment-with-human-replies.md) — related
