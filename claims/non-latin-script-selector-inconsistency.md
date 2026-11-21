---
type: claim
title: "LLM choice of Latin versus non-Latin script for multiple-choice selectors is inconsistent and influenced by the prompt's example letter"
description: "LLM choice of Latin versus non-Latin script for multiple-choice selectors is inconsistent and influenced by the prompt's example letter"
id: non-latin-script-selector-inconsistency
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
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

# LLM choice of Latin versus non-Latin script for multiple-choice selectors is inconsistent and influenced by the prompt's example letter

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In 17 non-Latin languages the LLM sometimes used local-script letters as multiple-choice selectors, inconsistently even within one language, and the example letter in the answer prompt shifted the script of responses (e.g. Bulgarian responses moved from two questions in non-Latin selectors to all responses in Cyrillic). [→ Marina Babayeva 2025](#marina-babayeva-2025)

## Evidence

### Marina Babayeva 2025

Marina Babayeva, Justin Dunlap, Marie Snětinová, Ralf Widenhorn. (2025). Translating the Force Concept Inventory in the age of AI. [doi:10.21203/rs.3.rs-7410179/v1](https://doi.org/10.21203/rs.3.rs-7410179/v1)

`q2 · i?` · `design · r2`

Observational analysis of translation and problem-solving outputs (Table 1) showing which languages used non-Latin selectors. The discussion reports that for seven languages the prompt example used a local-script letter, increasing non-Latin responses, while for Thai non-Latin responses decreased from 9 questions to 2 when the Latin "B" was used.

> "This increased the non-Latin responses for those languages, e.g. with Bulgarian going from two questions in non-Latin multiple-choice selector script to all responses in the Bulgarian Cyrillic alphabet."

## Discussion


## Related Claims
- [Prompt design significantly influences LLM accuracy on IVDA MCQs, with slide context reducing smaller-model accuracy but improving GPT models, while persona effects are inconsistent](prompt-design-affects-mcq-accuracy-asymmetrically.md) — a broader claim this one bears on
