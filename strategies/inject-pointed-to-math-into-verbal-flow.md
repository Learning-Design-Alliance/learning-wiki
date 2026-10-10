---
type: strategy
id: inject-pointed-to-math-into-verbal-flow
title: Inject LaTeX transcriptions of pointed-to math in place of ambiguous verbal references
description: "The v6m system instructions direct Gemini to replace ambiguous verbal references such as \"this equation\" with LaTeX renderings of the pointed-to math, injected in place of or immediately after the reference, and to us..."
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

# Inject LaTeX transcriptions of pointed-to math in place of ambiguous verbal references

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The v6m system instructions direct Gemini to replace ambiguous verbal references such as "this equation" with LaTeX renderings of the pointed-to math, injected in place of or immediately after the reference, and to use nonverbal ACTION segments for more complicated interactions with equations, graphs, and diagrams. The authors report that the instructions "direct Gemini to inject LaTeX transcriptions of pointed-to math in place of – or immediately following – ambiguous verbal references (e.g., "this equation") whenever possible". They found no examples of Gemini hallucinating incorrect LaTeX injections into the verbal flow.

## Design Implications

### Context
#### Requirements
- System instructions empowering math injection while forbidding bracketed insertions in the verbal flow
- Sufficient video context for Gemini to resolve gestural referents
#### Constraints
- Ambiguous references remain when gestures are too short to resolve at the default one-frame-per-second sampling rate, when gestures are ambiguous, or when no gesture accompanies the reference

### Target Learners
- blind and low-vision students using screen readers

### Target Learning Goals
- coherent single-channel reconstruction of multi-channel mathematical presentations

## Related Strategies

- [Accessible subscript transcription rules: math-code single elements, text-code multi-letter labels, unstack stacked subscripts](accessible-subscript-transcription-rules.md)

## Examples
-

## Key Sources
- Looney, C. W., & Duston, C. L. (2026). Using Gemini and LuaLaTeX to transcribe physics videos into PDF/UA-2 and ISO 32005 math-accessible PDFs. https://arxiv.org/abs/2608.20733
