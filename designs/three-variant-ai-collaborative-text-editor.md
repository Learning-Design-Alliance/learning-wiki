---
type: design
id: three-variant-ai-collaborative-text-editor
title: Three-variant AI-assisted collaborative writing text editor
description: A custom web-based text editor in which an LLM-backed artificial agent acts as a peer editor offering replacement suggestions and comments in an Editing Pane.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: michael-yin-2026
    resource: "https://arxiv.org/abs/2605.24729"
    title: "Michael Yin, Angela Chiang, Samuel Rhys Cox, and Robert Xiao. (2026). \"It Felt a Bit Eerie\": Exploring Humanlike Interactions During Collaborative Writing with an Artificial Agent. arXiv. https://arxiv.org/abs/2605.24729"
    author: Michael Yin, Angela Chiang, Samuel Rhys Cox, and Robert Xiao
---

# Three-variant AI-assisted collaborative writing text editor

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A custom web-based text editor in which an LLM-backed artificial agent acts as a peer editor offering replacement suggestions and comments in an Editing Pane. The authors "built three variants of an AI-assisted text editor along a spectrum of simulated humanlike interaction (synchronous and with a cursor) to machinelike interaction (asynchronous and without a cursor)". The suggestion suite was constant across variants; variants differed only in temporal and visual humanlikeness. It was built with React and ProseMirror on the front end and a Python Flask back end calling the OpenAI gpt-4o API.

## Design Implications

### Context
#### Requirements
- An LLM backend (OpenAI gpt-4o API calls) generating replacement and comment suggestions from the chunked text and previous suggestions
#### Constraints
- Humanlike behaviour heuristics (suggestion timing, cursor motion, typing speed) were tweaked subjectively and based on averages; the authors note "there is no 'average' human"

### Target Learners
- adult writers in a lab study (18+, fluent in English)

### Learning Goals
- collaborative writing and revision with AI support

### Claims
- [Synchronous Suggestions Efficiency And Distraction](../claims/synchronous-suggestions-efficiency-and-distraction.md) [+M]
- [Agentic Cursor Evokes Surveillance And Eeriness](../claims/agentic-cursor-evokes-surveillance-and-eeriness.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Michael Yin, Angela Chiang, Samuel Rhys Cox, and Robert Xiao. (2026). "It Felt a Bit Eerie": Exploring Humanlike Interactions During Collaborative Writing with an Artificial Agent. arXiv. https://arxiv.org/abs/2605.24729
