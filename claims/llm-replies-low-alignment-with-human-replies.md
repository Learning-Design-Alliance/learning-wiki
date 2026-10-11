---
type: claim
title: LLM-generated replies were consistently not similar to human replies, though including chat history slightly improved alignment
description: LLM-generated replies were consistently not similar to human replies, though including chat history slightly improved alignment
id: llm-replies-low-alignment-with-human-replies
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

# LLM-generated replies were consistently not similar to human replies, though including chat history slightly improved alignment

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across models and context conditions, LLM-generated replies showed consistently low similarity to the human teammate's replies, with chat history providing slight improvement. [→ Jiangang Hao 2026](#jiangang-hao-2026)

## Evidence

### Jiangang Hao 2026

Jiangang Hao. (2026). Semantic Variability of LLM-Generated Replies Across LLMs: Implications for Designing Conversation-Based Assessment. Accepted to AI in Measurement and Education Conference – AIME 2026. https://arxiv.org/abs/2608.24920

`q2 · i?` · `causal · r2`

Exploratory analysis (Fig. 1, bottom panel) of mean similarity between LLM-generated replies and the retained human replies for the 61 focal messages. "The LLM-generated replies are consistently not similar with human replies."

> "The LLM-generated replies are consistently not similar with human replies, though including chat history can slightly improve the situation."

## Discussion


## Related Claims
- [Chat history lowered mean pairwise reply similarity for GPT-4o mini, but GPT-5.4 and GPT-5.4 mini were less negatively affected, indicating the effect of history differs across models](history-effect-on-mean-similarity-varies-by-model.md) — related
- [Without chat history, semantically similar focal messages elicited similar LLM replies; this positive relationship was weaker when history was included](focal-message-similarity-predicts-reply-similarity-no-history.md) — related
- [Replies generated with chat history were only moderately similar to replies generated without history (median cross-history similarity around 0.40 to 0.45)](chat-history-changes-reply-semantic-content.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
