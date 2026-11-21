---
type: claim
title: The same v–t graph is interpreted correctly in a native Google Doc but fails to parse when exported to default PDF
description: The same v–t graph is interpreted correctly in a native Google Doc but fails to parse when exported to default PDF
id: notebooklm-graph-parsing-docs-vs-pdf
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: eugenio-tufino-2025
    resource: "https://doi.org/10.1142/s2661339525500143"
    title: "Eugenio Tufino. (2025). NotebookLM as a Socratic physics tutor: Design and preliminary observations of a RAG-based tool. arXiv preprint. [doi:10.1142/s2661339525500143](https://doi.org/10.1142/s2661339525500143)"
    author: Eugenio Tufino
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The same v–t graph is interpreted correctly in a native Google Doc but fails to parse when exported to default PDF

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In a two-condition format test, NotebookLM correctly interpreted a Python-generated velocity–time graph in a Google Docs document, while the same document exported to PDF with default settings returned a no-image-detected response. [→ Eugenio Tufino 2025](#eugenio-tufino-2025)

## Evidence

### Eugenio Tufino 2025

Eugenio Tufino. (2025). NotebookLM as a Socratic physics tutor: Design and preliminary observations of a RAG-based tool. arXiv preprint. [doi:10.1142/s2661339525500143](https://doi.org/10.1142/s2661339525500143)

`q2 · i?` · `design · r2`

Format-sensitivity test on the same Python-generated v–t graph of a bouncing ball in two conditions. The Google Docs version was read correctly; the default PDF export "led the system to fail to parse the figure". The author attributes the difference to an export-pipeline artifact, not intrinsic PDF limitations.

> "In a Google Docs document, NotebookLM correctly interpreted the graph’s key features (Figure 3b). In contrast, exporting the same document to PDF with default settings led the system to fail to parse the figure, returning “no-image-detected” (Figure 3c)."

## Discussion


## Related Claims
- [Transcribing one TUG-K graph item into text raised ChatGPT's correctness from 10% to 100%](graph-transcription-bypasses-vision-failure.md) — related
