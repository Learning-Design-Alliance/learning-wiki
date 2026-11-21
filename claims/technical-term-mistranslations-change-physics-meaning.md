---
type: claim
title: Mistranslations of technical physics terms changed the physical meaning of specific FI questions, causing incorrect LLM answers despite sound reasoning
description: Mistranslations of technical physics terms changed the physical meaning of specific FI questions, causing incorrect LLM answers despite sound reasoning
id: technical-term-mistranslations-change-physics-meaning
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

# Mistranslations of technical physics terms changed the physical meaning of specific FI questions, causing incorrect LLM answers despite sound reasoning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Translation errors such as rendering "arithmetic sum" as "vector sum" in eight languages for question 9, "perpendicular" as "opposing" in Somali for question 22, and adding "smooth" to question 27 in Somali altered the physics of problems and produced wrong multiple-choice selections. [→ Marina Babayeva 2025](#marina-babayeva-2025)

## Evidence

### Marina Babayeva 2025

Marina Babayeva, Justin Dunlap, Marie Snětinová, Ralf Widenhorn. (2025). Translating the Force Concept Inventory in the age of AI. [doi:10.21203/rs.3.rs-7410179/v1](https://doi.org/10.21203/rs.3.rs-7410179/v1)

`q2 · i?` · `design · r2`

Qualitative analysis of back-translations identifying translation mistakes. For question 9 the error "completely changed the meaning of the question and a different multiple-choice option was correct," yet the LLM selected the answer correct for the translated choices, indicating the error lay in the translation process.

> "Looking at the back-translations for question 9, the original phrase “arithmetic sum” was incorrectly translated as “vector sum” in two of the multiple-choice options in the following languages: Bengali, Kannada, Malayalam, Punjabi, Swahili, Tamil, Telugu, and Urdu."

## Discussion


## Related Claims
- [GPT-4o answered question 29 correctly 3 out of 3 times when given a physicist's Czech translation but answered the LLM's Czech translation incorrectly](expert-translation-outperforms-llm-translation-q29.md) — related
- [General-purpose LLMs show accuracy and reliability limits, including hallucinations and task-specific accuracy below perfect, making them risky as expert advice sources](llm-accuracy-hallucination-coaching-risk.md) — related
