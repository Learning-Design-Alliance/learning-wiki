---
type: claim
title: "GPT-4o scores 75% on LLM-translated FCI versions across 53 languages, 76% on back-translations, and 77% in English, with GPT-o1 reaching 84% in English"
description: "GPT-4o scores 75% on LLM-translated FCI versions across 53 languages, 76% on back-translations, and 77% in English, with GPT-o1 reaching 84% in English"
id: fci-gpt4o-translation-overall-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: marina-babayeva-2025
    resource: "https://doi.org/10.21203/rs.3.rs-7410179/v1"
    title: "Marina Babayeva, Justin Dunlap, Marie Snětinová, Ralf Widenhorn. (2025). Translating the Force Concept Inventory in the age of AI. [doi:10.21203/rs.3.rs-7410179/v1](https://doi.org/10.21203/rs.3.rs-7410179/v1)"
    author: Marina Babayeva, Justin Dunlap, Marie Snětinová, Ralf Widenhorn
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o scores 75% on LLM-translated FCI versions across 53 languages, 76% on back-translations, and 77% in English, with GPT-o1 reaching 84% in English

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Average correct-answer performance on the 53 LLM-translated FCI versions was 75% with GPT-4o, slightly below the 77% English baseline, while GPT-o1 in English reached 84%. [→ Marina Babayeva 2025](#marina-babayeva-2025)

## Evidence

### Marina Babayeva 2025

Marina Babayeva, Justin Dunlap, Marie Snětinová, Ralf Widenhorn. (2025). Translating the Force Concept Inventory in the age of AI. [doi:10.21203/rs.3.rs-7410179/v1](https://doi.org/10.21203/rs.3.rs-7410179/v1)

`q2 · i?` · `design · r2`

Automated problem-solving evaluation of the full 30-question FCI: 53 LLM translations plus back-translations solved with gpt-4o-2024-11-20, and the English version solved five times each with GPT-4o and GPT-o1. The study reports "an average score of 77% across five repetitions" in English and 75% on translations.

> "The average performance on the translated versions using GPT-4o was 75%, and the back-translations scored slightly higher at 76%. When tested in English, GPT-4o achieved an average score of 77% across five repetitions. Additionally, the English FCIs solved with GPT-o1 outperformed all other variants with 84%."

## Discussion


## Related Claims
- [GPT-4o answered question 29 correctly 3 out of 3 times when given a physicist's Czech translation but answered the LLM's Czech translation incorrectly](expert-translation-outperforms-llm-translation-q29.md) — related
- [The majority of the 53 translated language versions score 70% or more correct answers, comparable to the original English version](majority-languages-70-percent-comparable.md) — related
- [GPT-4o accuracy on image-required FCI questions (36–38%) is substantially weaker than on text-only and image-optional questions (97–100%)](image-required-questions-low-llm-accuracy.md) — related
- [OpenAI o1 achieved the highest aggregated mean score among the five LLMs, followed by Copilot, DeepSeek, Gemini, and GPT-4o](openai-o1-highest-aggregated-mean-five-llms.md) — related
- [Translation and back-translation subtly shift FCI terminology, with \"speed\" appearing 1,514 times and \"velocity\" 702 times in back-translations](speed-velocity-terminology-shift-back-translation.md) — related
