---
type: claim
title: Abandoning preamble coding macros in favor of amsmath, unicode-math, and siunitx enabled successive error-free transcriptions
description: Abandoning preamble coding macros in favor of amsmath, unicode-math, and siunitx enabled successive error-free transcriptions
id: minimalist-preamble-enabled-error-free-transcription
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: looney-2026
    resource: "https://arxiv.org/abs/2608.20733"
    title: "Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733"
    author: "Looney, C. W., & Duston, C. L."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Abandoning preamble coding macros in favor of amsmath, unicode-math, and siunitx enabled successive error-free transcriptions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Only after the authors abandoned preamble coding macros and relied entirely on amsmath, unicode-math, and siunitx for all LaTeX math constructions could three different videos be transcribed in succession without compilation errors. [→ Looney 2026](#looney-2026)

## Evidence

### Looney 2026

Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733

`q2 · i?` · `design · r2`

Developmental-stage testing observation from Section 5.1: the authors report that "abandoning preamble coding macros" and relying on the three basic packages was the turning point for successive error-free transcriptions. No effect size is reported.

> "Only after abandoning preamble coding macros and relying entirely on amsmath, unicode-math, and siunitx for all LaTeX math constructions did it become possible to transcribe three different videos in succession without compilation errors."

## Discussion


## Related Claims
- [The v6m workflow produced compilations passing PDF/UA-2 and ISO 32005 validation in 16 of 17 successive transcription tests across 16 videos](v6m-workflow-16-of-17-validation-passes.md) — related
- [Successful transcriptions of videos using Dirac notation, eigenstate derivations, and vector calculus indicate generalized capability beyond introductory physics](transcription-capability-beyond-introductory-physics.md) — related
- [The v6m subscript framework robustly transcribed a wide range of board-written subscript configurations, with stacked-subscript unstacking less reliable](v6m-subscript-framework-robust-transcription.md) — related
