---
type: claim
title: ChatGPT4.0 and Gemini-1.5-flash showed the most consistent response lengths, while ChatGPT3.5 was the most variable across repeated prompts
description: ChatGPT4.0 and Gemini-1.5-flash showed the most consistent response lengths, while ChatGPT3.5 was the most variable across repeated prompts
id: llm-response-consistency-cv
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: keisuke-sato-2024
    resource: "https://doi.org/10.48550/arXiv.2407.05308"
    title: "Keisuke Sato. (2024). Exploring the Educational Landscape of AI: Large Language Models' Approaches to Explaining Conservation of Momentum in Physics. A Preprint. [doi:10.48550/arXiv.2407.05308](https://doi.org/10.48550/arXiv.2407.05308)"
    author: Keisuke Sato
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ChatGPT4.0 and Gemini-1.5-flash showed the most consistent response lengths, while ChatGPT3.5 was the most variable across repeated prompts

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Measured by coefficient of variation for character count, Gemini-1.5-flash was most consistent (CV 9.93%) and ChatGPT3.5 least consistent (CV 24.05%). [→ Keisuke Sato 2024](#keisuke-sato-2024)

## Evidence

### Keisuke Sato 2024

Keisuke Sato. (2024). Exploring the Educational Landscape of AI: Large Language Models' Approaches to Explaining Conservation of Momentum in Physics. A Preprint. [doi:10.48550/arXiv.2407.05308](https://doi.org/10.48550/arXiv.2407.05308)

`q2 · i?` · `design · r2`

The study computed the coefficient of variation for character count across each model's 50 responses to compare consistency despite differing lengths. The article reports "Gemini-1.5-ﬂash demonstrates the highest consistency i n response length, with a CV of 9.93%", while ChatGPT3.5 showed the highest variability (CV 24.05%).

> "Gemini-1.5-ﬂash demonstrates the highest consistency i n response length, with a CV of 9.93%."

## Discussion


## Related Claims
- [Six LLMs differed substantially in response length and structure when explaining conservation of momentum, with Gemini-1.5-pro longest and ChatGPT3.5 shortest](llm-response-length-variability-momentum.md) — related
- [Gemini-1.5-flash and Coral were the most semantically consistent across repeated prompts, and ChatGPT4.0 the most lexically consistent by cosine similarity](llm-response-similarity-measures.md) — related
- [Chatbots differ significantly in response time and word count, with Gemini 1.5 fastest and DeepSeek slowest and least accurate](chatbot-response-time-length-differences.md) — related
