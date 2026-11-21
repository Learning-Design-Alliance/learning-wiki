---
type: claim
title: Domain vocabulary prompting substantially improved recognition of specialized thermodynamics terms in lecture transcription
description: Domain vocabulary prompting substantially improved recognition of specialized thermodynamics terms in lecture transcription
id: domain-vocabulary-prompting-whisper-technical-terms
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: eric-m-furst-and-vasudevan-venkateshwaran-2026
    resource: "https://doi.org/10.48550/arXiv.2603.04657"
    title: "Eric M. Furst and Vasudevan Venkateshwaran. (2026). Stan: An LLM-based thermodynamics course assistant. [doi:10.48550/arXiv.2603.04657](https://doi.org/10.48550/arXiv.2603.04657)"
    author: Eric M. Furst and Vasudevan Venkateshwaran
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Domain vocabulary prompting substantially improved recognition of specialized thermodynamics terms in lecture transcription

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Supplying Whisper's initial prompt parameter with key thermodynamic terms improved recognition of domain vocabulary, correcting previously garbled terms such as fugacity. [→ Eric M. Furst and Vasudevan Venkateshwaran 2026](#eric-m-furst-and-vasudevan-venkateshwaran-2026)

## Evidence

### Eric M. Furst and Vasudevan Venkateshwaran 2026

Eric M. Furst and Vasudevan Venkateshwaran. (2026). Stan: An LLM-based thermodynamics course assistant. [doi:10.48550/arXiv.2603.04657](https://doi.org/10.48550/arXiv.2603.04657)

`q2 · i?` · `design · r2`

Transcription-pipeline analysis of the lecture corpus: without prompting, fugacity was consistently rendered as "GASB" and other terms were garbled; with the vocabulary prompt, "fugacity" was correctly recognized throughout the transcript. No effect size is printed; some terms remained occasionally garbled.

> "By supplying a prompt containing key thermodynamic terms (fugacity, Clausius-Clapeyron, Peng-Robinson, Poynting correction, etc.), we found that recognition of domain vocabulary improved substantially. With prompting, "fugacity" was correctly recognized throughout the transcript."

## Discussion


## Related Claims
- [Domain-prompted Whisper and institutional Kaltura transcripts were similar in aggregate word counts but differed in contextual fidelity](kaltura-whisper-transcript-comparison-contextual-fidelity.md) — related
- [Prompting strategy materially affects gpt-4o accuracy on thermodynamics text items, with elimination-style prompts underperforming and a two-phase format yielding no significant gain](prompting-strategy-effects-thermodynamics-llm.md) — related
