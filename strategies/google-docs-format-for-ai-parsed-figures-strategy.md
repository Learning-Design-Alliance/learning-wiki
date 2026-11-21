---
type: strategy
id: google-docs-format-for-ai-parsed-figures-strategy
title: Use native Google Docs for materials with critical figures, and tagged high-quality PDFs when PDF distribution is required
description: "Because accurate graph interpretation is central to physics problem-solving and default PDF export caused the tutor to fail to parse a figure, the author recommends that \"Google Docs are currently the most reliable an..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: eugenio-tufino-2025
    resource: "https://arxiv.org/abs/2504.09720"
    title: "Eugenio Tufino. (2025). NotebookLM as a Socratic physics tutor: Design and preliminary observations of a RAG-based tool. arXiv preprint. https://arxiv.org/abs/2504.09720"
    author: Eugenio Tufino
---

# Use native Google Docs for materials with critical figures, and tagged high-quality PDFs when PDF distribution is required

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
Because accurate graph interpretation is central to physics problem-solving and default PDF export caused the tutor to fail to parse a figure, the author recommends that "Google Docs are currently the most reliable and convenient format for materials with critical figures". When PDF distribution is required, the article advises using a tagged, high-quality PDF with embedded fonts and vector or high-resolution figures to ensure accurate AI interpretation.

## Design Implications

### Context
#### Requirements
- Access to Google Docs for preparing visual materials
- Awareness of which source formats the platform parses via structure-preserving APIs
#### Constraints
- Video analysis effectiveness depends on transcript availability and quality, which may be unreliable for specialized content or poor audio

### Target Learners
- educators curating source materials for RAG-based AI tutors

### Target Learning Goals
- reliable AI interpretation of graphs and visual content in learning materials

## Claims

- [The same v–t graph is interpreted correctly in a native Google Doc but fails to parse when exported to default PDF](../claims/notebooklm-graph-parsing-docs-vs-pdf.md) [+W]
- [Transcribing one TUG-K graph item into text raised ChatGPT's correctness from 10% to 100%](../claims/graph-transcription-bypasses-vision-failure.md) [+W]

## Related Strategies

- [Mitigate extraction errors by requiring high-resolution PDFs, equation-editor equations, and legible graph axes, units, and legends](report-submission-practices-to-support-ai-evidence-retrieval.md)

## Examples
-

## Key Sources
- Eugenio Tufino. (2025). NotebookLM as a Socratic physics tutor: Design and preliminary observations of a RAG-based tool. arXiv preprint. https://arxiv.org/abs/2504.09720
