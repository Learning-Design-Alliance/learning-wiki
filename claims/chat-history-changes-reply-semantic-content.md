---
type: claim
title: Replies generated with chat history were only moderately similar to replies generated without history (median cross-history similarity around 0.40 to 0.45)
description: Replies generated with chat history were only moderately similar to replies generated without history (median cross-history similarity around 0.40 to 0.45)
id: chat-history-changes-reply-semantic-content
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

# Replies generated with chat history were only moderately similar to replies generated without history (median cross-history similarity around 0.40 to 0.45)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Median cross-history similarity was around 0.40 to 0.45 for all models, indicating adding chat history meaningfully changed the semantic content of generated replies. [→ Jiangang Hao 2026](#jiangang-hao-2026)

## Evidence

### Jiangang Hao 2026

Jiangang Hao. (2026). Semantic Variability of LLM-Generated Replies Across LLMs: Implications for Designing Conversation-Based Assessment. Accepted to AI in Measurement and Education Conference – AIME 2026. https://arxiv.org/abs/2608.24920

`q2 · i?` · `causal · r2`

Exploratory analysis (Fig. 4) comparing each model's 100 with-history replies to its 100 no-history replies for the same focal messages. "Median cross-history similarity was around 0.40 to 0.45 for all models."

> "Median cross-history similarity was around 0.40 to 0.45 for all models, indicating that replies generated with history were only moderately similar to replies generated without history."

## Discussion


## Related Claims
- [Without chat history, semantically similar focal messages elicited similar LLM replies; this positive relationship was weaker when history was included](focal-message-similarity-predicts-reply-similarity-no-history.md) — related
- [Chat history lowered mean pairwise reply similarity for GPT-4o mini, but GPT-5.4 and GPT-5.4 mini were less negatively affected, indicating the effect of history differs across models](history-effect-on-mean-similarity-varies-by-model.md) — related
- [LLM-generated replies were consistently not similar to human replies, though including chat history slightly improved alignment](llm-replies-low-alignment-with-human-replies.md) — related
