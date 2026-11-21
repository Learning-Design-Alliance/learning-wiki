---
type: claim
title: "Localized pre-LLM computation and caching in COTUTOR reduces LLM prompts by 30% with estimated cost savings of 15% for GPT-4o and 42% for Claude 3.7"
description: "Localized pre-LLM computation and caching in COTUTOR reduces LLM prompts by 30% with estimated cost savings of 15% for GPT-4o and 42% for Claude 3.7"
id: cotutor-caching-reduces-llm-prompts-cost
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: yuchen-wang-2025
    resource: "https://doi.org/10.48550/arXiv.2509.23996"
    title: "Yuchen Wang, Pei-Duo Yu, Chee Wei Tan. (2025). Future-Proofing Programmers: Optimal Knowledge Tracing for AI-Assisted Personalized Education. [doi:10.48550/arXiv.2509.23996](https://doi.org/10.48550/arXiv.2509.23996)"
    author: Yuchen Wang, Pei-Duo Yu, Chee Wei Tan
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# Localized pre-LLM computation and caching in COTUTOR reduces LLM prompts by 30% with estimated cost savings of 15% for GPT-4o and 42% for Claude 3.7

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` The article reports that COTUTOR's localized pre-LLM computation and caching mechanism reduces LLM prompts by 30%, with estimated cost savings of 15% for GPT-4o and 42% for Claude 3.7. [→ Yuchen Wang 2025](#yuchen-wang-2025)

## Evidence

### Yuchen Wang 2025

Yuchen Wang, Pei-Duo Yu, Chee Wei Tan. (2025). Future-Proofing Programmers: Optimal Knowledge Tracing for AI-Assisted Personalized Education. [doi:10.48550/arXiv.2509.23996](https://doi.org/10.48550/arXiv.2509.23996)

`q1 · i?` · `design · r1`

Authors' discussion-section report on scalability: the caching mechanism "reduces LLM prompts by 30%", with estimated per-million-token cost savings of 15% for GPT-4o and 42% for Claude 3.7. These are the article's own estimates, not measured deployment data.

> "COTUTOR's scalability is enhanced by its localized pre-LLM computation and caching mechanis,m which reduces LLM prompts by 30%, yielding estimated cost savings of 15% for GPT-4o ($2.50 vs $1.25 per million tokens) and 42% for Claude 3.7 ($3.75 vs $0.3 per million tokens)."

## Discussion


## Related Claims
- [GPT-4o with few-shot learning offers the best balance of performance, cost, and speed for large-scale assessment, far cheaper than human grading](gpt4o-fewshot-preferred-cost-speed.md) — related
