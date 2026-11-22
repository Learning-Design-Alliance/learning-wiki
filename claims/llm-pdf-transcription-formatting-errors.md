---
type: claim
title: LLM transcription of the FCI PDF omitted question parts, misnumbered items, and introduced formatting inconsistencies requiring manual correction
description: LLM transcription of the FCI PDF omitted question parts, misnumbered items, and introduced formatting inconsistencies requiring manual correction
id: llm-pdf-transcription-formatting-errors
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

# LLM transcription of the FCI PDF omitted question parts, misnumbered items, and introduced formatting inconsistencies requiring manual correction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Automated transcription of the FCI PDF with GPT-4o-mini occasionally omitted parts of questions, misnumbered items, or introduced formatting inconsistencies such as missing subscripts, and all transcriptions required manual review and correction. [→ Marina Babayeva 2025](#marina-babayeva-2025)

## Evidence

### Marina Babayeva 2025

Marina Babayeva, Justin Dunlap, Marie Snětinová, Ralf Widenhorn. (2025). Translating the Force Concept Inventory in the age of AI. [doi:10.21203/rs.3.rs-7410179/v1](https://doi.org/10.21203/rs.3.rs-7410179/v1)

`q2 · i?` · `design · r2`

Method-section report on the transcription step using OpenAI's GPT-4o-mini (chosen for cost reasons), followed by manual corrections and edits making each question self-contained; final texts were stored as UTF-8 CSV files with PNG figures.

> "While generally successful, the model occasionally omitted parts of questions, misnumbered items, or introduced formatting inconsistencies (e.g., missing subscripts). All transcriptions were manually reviewed and corrected to correspond to the original document."

## Discussion


## Related Claims
- [Transcribing one TUG-K graph item into text raised ChatGPT's correctness from 10% to 100%](graph-transcription-bypasses-vision-failure.md) — related
- [A RAG-augmented LLM translation pipeline raised pre-human-review translation accuracy from approximately 80% to over 95%](rag-llm-translation-accuracy-above-95-percent.md) — related
