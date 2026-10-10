---
type: claim
title: Gemini frequently corrects board-written math errors with correction logs, but still shows case-consistency and notation-substitution failures
description: Gemini frequently corrects board-written math errors with correction logs, but still shows case-consistency and notation-substitution failures
id: gemini-error-correction-with-case-consistency-failures
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: looney-2026
    resource: "https://arxiv.org/abs/2608.20733"
    title: "Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733"
    author: "Looney, C. W., & Duston, C. L."
    q: 2
    i: "?"
    kind: design
    rigour: 3
  - id: looney-2026-2
    resource: "https://arxiv.org/abs/2608.20733"
    title: "Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733"
    author: "Looney, C. W., & Duston, C. L."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Gemini frequently corrects board-written math errors with correction logs, but still shows case-consistency and notation-substitution failures

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2`–`r3` · `q2`

## Subclaims
`q2 i?` Gemini often corrects obvious board-written physics or math errors on its own, with correction logs appended as comments, yet in the v6m transcription of video 1 it consistently used uppercase V rather than lowercase v for velocity despite an explicit contextual case-consistency directive. [→ Looney 2026](#looney-2026)
`q2 i?` Gemini occasionally makes systematic notation substitutions, such as transcribing the volume element dτ as dV in every transcription of video 10, presumably due to dominance in its training data. [→ Looney 2026 (2)](#looney-2026-2)

## Evidence

### Looney 2026

Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733

`q2 · i?` · `design · r3`

Qualitative evaluation of transcribed mathematics in Section 5.4: the authors report that "Gemini will often correct obvious board-written physics or math errors on its own", with correction logs preserved in the transcripts of videos 1, 3, 6, 8, 9 (test 2), 10, and 13. No effect size is reported.

> "We have found that Gemini will often correct obvious board-written physics or math errors on its own."

### Looney 2026 (2)

Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733

`q2 · i?` · `design · r2`

Qualitative evaluation in Section 5.4 of recurring notation substitution: the authors report Gemini "has made this exact same substitution every single time" for video 10, attributing it to training-data dominance. No effect size is reported.

> "in the v6m transcription of video 10, Gemini transcribed the board-written volume element 𝑑𝜏 as 𝑑𝑉 . Versions of this video have been transcribed several times by multiple iterations of the system instructions, and Gemini has made this exact same substitution every single time, presumably due to the dominance of 𝑑𝑉 in Gemini’s training data."

## Discussion


## Related Claims
- [The v6m subscript framework robustly transcribed a wide range of board-written subscript configurations, with stacked-subscript unstacking less reliable](v6m-subscript-framework-robust-transcription.md) — related
- [Successful transcriptions of videos using Dirac notation, eigenstate derivations, and vector calculus indicate generalized capability beyond introductory physics](transcription-capability-beyond-introductory-physics.md) — related
- [The v6m workflow produced compilations passing PDF/UA-2 and ISO 32005 validation in 16 of 17 successive transcription tests across 16 videos](v6m-workflow-16-of-17-validation-passes.md) — related
