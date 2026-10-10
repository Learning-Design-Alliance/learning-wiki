---
type: strategy
id: accessible-subscript-transcription-rules
title: "Accessible subscript transcription rules: math-code single elements, text-code multi-letter labels, unstack stacked subscripts"
description: "The v6m system instructions encode subscript elements semantically: bare numbers, single symbols, and single letters are coded as math so a screen reader reads them separately, while multi-letter labels are coded as t..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: looney-2026
    resource: "https://arxiv.org/abs/2608.20733"
    title: "Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733"
    author: "Looney, C. W., & Duston, C. L"
---

# Accessible subscript transcription rules: math-code single elements, text-code multi-letter labels, unstack stacked subscripts

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The v6m system instructions encode subscript elements semantically: bare numbers, single symbols, and single letters are coded as math so a screen reader reads them separately, while multi-letter labels are coded as text so they are read as words. The instructions state that "All subscript elements consisting of multi-letter labels are coded as text, so that they will be read out as words rather than as individual letters". Subscripts are transcribed in board-written order without artificially injected commas, and vertically stacked subscripts are identified and rearranged into unstacked configurations, which are more robust and simpler for screen readers.

## Design Implications

### Context
#### Requirements
- A screen reader up to spec for reading distinct subscript elements separately
- System instructions enforcing the math/text coding distinction
#### Constraints
- Adjacent bare-number subscripts are not semantically separated, since comma injection would violate notation standards such as Miller indices or change meaning for tensor subscripts; users can set modern screen readers to read successive numeric subscripts digit by digit

### Target Learners
- blind and low-vision students reading math-accessible PDFs with screen readers

### Target Learning Goals
- accurate auditory reconstruction of multi-subscript mathematical notation

## Related Strategies

- [Inject LaTeX transcriptions of pointed-to math in place of ambiguous verbal references](inject-pointed-to-math-into-verbal-flow.md)

## Examples
-

## Key Sources
- Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733
