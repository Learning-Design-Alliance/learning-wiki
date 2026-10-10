---
type: design
id: segment-structure-transcript-format
title: Segment-structure transcript format with boldface labels replacing bracketed nonverbal insertions
description: The v6m system instructions organize transcripts into distinct verbal and descriptive segments marked by boldface labels rather than square brackets, with both segment types able to contain math.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: looney-2026
    title: "Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs."
    author: "Looney, C. W., & Duston, C. L"
---

# Segment-structure transcript format with boldface labels replacing bracketed nonverbal insertions

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The v6m system instructions organize transcripts into distinct verbal and descriptive segments marked by boldface labels rather than square brackets, with both segment types able to contain math. Early tests showed that closing display math at the end of a square-bracketed descriptive segment caused numerous compilation failures; the authors report that "Abandoning square brackets and adopting the segment structure delivered an immediate and substantial improvement in stability and overall performance". The labels also provide a less-ambiguous transition signal for screen reader users than bracketed text.

## Design Implications

### Context
#### Requirements
- A prewritten LuaLaTeX preamble compatible with the segment structure
- System instructions that define and enforce the segment labels
#### Constraints
- Brief bracketed insertions of nonverbal description cannot be injected directly into the verbal flow

### Target Learners
- blind and low-vision students using screen readers

### Learning Goals
- accessible comprehension of spoken and board-written mathematical content in lecture videos

### Claims
- V6M Gemini Lualatex Transcription Workflow [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs.
