---
type: claim
title: Chatbot answers showed only moderate cross-language agreement and imperfect consistency across repeated measurements
description: Chatbot answers showed only moderate cross-language agreement and imperfect consistency across repeated measurements
id: chatbot-response-consistency-varies-by-language-and-measurement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: wójcik-2025
    resource: "https://doi.org/10.1038/s41598-025-17030-0"
    title: "Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L. (2025). Comparing the performance of ChatGPT, Gemini, and Claude in English and Polish on medical examinations. Scientific Reports 15, 33083. https://doi.org/10.1038/s41598-025-17030-0"
    author: "Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L."
    q: 2
    i: "?"
    kind: causal
    rigour: "?"
  - id: wójcik-2025-2
    resource: "https://doi.org/10.1038/s41598-025-17030-0"
    title: "Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L. (2025). Comparing the performance of ChatGPT, Gemini, and Claude in English and Polish on medical examinations. Scientific Reports 15, 33083. https://doi.org/10.1038/s41598-025-17030-0"
    author: "Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Chatbot answers showed only moderate cross-language agreement and imperfect consistency across repeated measurements

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Agreement between English and Polish answers was moderate for ChatGPT-4 (κ = 0.45) and Claude (κ = 0.59) and weak for Gemini (κ = 0.39). [→ Wójcik 2025](#wojcik-2025)
`q2 i?` Agreement across three repeated measurements differed by chatbot and language, with the best consistency for Claude in Polish (Fleiss' κ = 0.78) and the weakest for Gemini in English (κ = 0.40). [→ Wójcik 2025 (2)](#wojcik-2025-2)

## Evidence

### Wójcik 2025

Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L. (2025). Comparing the performance of ChatGPT, Gemini, and Claude in English and Polish on medical examinations. Scientific Reports 15, 33083. https://doi.org/10.1038/s41598-025-17030-0

`q2 · i?` · `causal · r?`

Cohen's Kappa analysis of answer agreement across prompt languages (Table 5, N = 1188): ChatGPT-4 κ = 0.45, Gemini κ = 0.39, Claude κ = 0.59, all p < 0.001. Kappa values are reliability coefficients, not standardized effect sizes, so no impact magnitude is coded.

> "The Cohen's Kappa coefficient (Table 5) shows that ChatGPT-4 and Claude indicated moderate agreement between the responses in English and Polish. Gemini showed weak agreement between the responses in English and Polish."

### Wójcik 2025 (2)

Wójcik, D., Adamiak, O., Czerepak, G., Tokarczuk, O. & Szalewski, L. (2025). Comparing the performance of ChatGPT, Gemini, and Claude in English and Polish on medical examinations. Scientific Reports 15, 33083. https://doi.org/10.1038/s41598-025-17030-0

`q2 · i?` · `causal · r2`

Fleiss' Kappa across three measurements (Table 6, N = 594): Claude Polish κ = 0.78 (excellent), Gemini English κ = 0.40 (weakest); the authors note kappa reflects consistency between outputs, not correctness.

> "Analysis of the agreement of the three chatbot answers to the same questions using Fleiss' kappa coefficient (Table 6) revealed differences depending on the chatbot model and the prompt language."

## Discussion


## Related Claims
- [Only Gemini showed significantly higher accuracy in English than in Polish prompts](gemini-accuracy-lower-in-polish-prompts.md) — related
- [Temporal reliability over a 1-week interval varied across LLMs: Claude 4.5 Sonnet showed very good consistency (kappa = 0.872) while Grok-4 and ChatGPT-5 showed moderate agreement](claude-sonnet-superior-temporal-reliability-radiology-questions.md) — related
- [Claude outperformed ChatGPT-4 and Gemini in accuracy on Polish/English medical-dental exam questions in both prompt languages](claude-highest-accuracy-ldek-exam-questions.md) — related
- [All three chatbots answered integrated-medicine questions more accurately than dentistry questions in both languages](integrated-medicine-higher-accuracy-than-dentistry.md) — related
