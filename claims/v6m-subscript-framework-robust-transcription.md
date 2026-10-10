---
type: claim
title: The v6m subscript framework robustly transcribed a wide range of board-written subscript configurations, with stacked-subscript unstacking less reliable
description: The v6m subscript framework robustly transcribed a wide range of board-written subscript configurations, with stacked-subscript unstacking less reliable
id: v6m-subscript-framework-robust-transcription
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: looney-2026
    resource: "https://arxiv.org/abs/2608.20733"
    title: "Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733"
    author: "Looney, C. W., & Duston, C. L."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: looney-2026-2
    resource: "https://arxiv.org/abs/2608.20733"
    title: "Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733"
    author: "Looney, C. W., & Duston, C. L."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The v6m subscript framework robustly transcribed a wide range of board-written subscript configurations, with stacked-subscript unstacking less reliable

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` The v6m subscript system enabled Gemini to robustly and accessibly transcribe a reasonably wide range of board-written subscript configurations, with only one observed deviation (a subscript-order reversal in video 3) across all 17 test PDFs. [→ Looney 2026](#looney-2026)
`q2 i?` Board-written stacked subscripts were correctly unstacked in test videos, but unstacking order varied between two transcriptions of video 9, indicating the unstacking rules are likely less reliable than the rest of the subscript system. [→ Looney 2026 (2)](#looney-2026-2)

## Evidence

### Looney 2026

Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733

`q2 · i?` · `design · r2`

Qualitative inspection of all 17 v6m test PDFs and source files in Section 5.5: the authors report the subscript system "enabled Gemini to robustly and accessibly transcribe a reasonably wide range of board-written subscript configurations". No effect size is reported.

> "Overall, our v6m subscript system has enabled Gemini to robustly and accessibly transcribe a reasonably wide range of board-written subscript configurations."

### Looney 2026 (2)

Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733

`q2 · i?` · `design · r2`

Section 5.5 analysis of video 9's stacked subscripts: in the first transcription the unpacking order matched the instructions while in the second it was reversed, though subscript information was accessibly preserved in both. No effect size is reported.

> "These tests indicate that the unstacking rules, while likely less reliable than the rest of our subscript system, should at least give Gemini a fighting chance to preserve the information in board-written stacked subscripts in real instructional videos."

## Discussion


## Related Claims
- [Gemini frequently corrects board-written math errors with correction logs, but still shows case-consistency and notation-substitution failures](gemini-error-correction-with-case-consistency-failures.md) — related
- [Successful transcriptions of videos using Dirac notation, eigenstate derivations, and vector calculus indicate generalized capability beyond introductory physics](transcription-capability-beyond-introductory-physics.md) — a broader claim this one bears on
- [The v6m workflow produced compilations passing PDF/UA-2 and ISO 32005 validation in 16 of 17 successive transcription tests across 16 videos](v6m-workflow-16-of-17-validation-passes.md) — related
- [Abandoning preamble coding macros in favor of amsmath, unicode-math, and siunitx enabled successive error-free transcriptions](minimalist-preamble-enabled-error-free-transcription.md) — related
