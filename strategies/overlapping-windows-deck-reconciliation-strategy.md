---
type: strategy
id: overlapping-windows-deck-reconciliation-strategy
title: Use overlapping multi-slide windows and deck-level reconciliation rather than per-slide generation
description: The article recommends processing slide decks with a sliding-window chunking strategy that stitches rendered thumbnails into multi-slide contact sheets to retain transitional context, followed by a dynamic reconciliat...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: salsman-2026
    resource: "https://arxiv.org/abs/2605.26428"
    title: "Salsman, J. (2026). Slide Deck Q&A Quality Assurance App: A Multi-Stage Pipeline for Pedagogical Question Generation. https://arxiv.org/abs/2605.26428"
    author: Salsman, J
---

# Use overlapping multi-slide windows and deck-level reconciliation rather than per-slide generation

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends processing slide decks with a sliding-window chunking strategy that stitches rendered thumbnails into multi-slide contact sheets to retain transitional context, followed by a dynamic reconciliation phase that balances question budgets across heterogeneous slide types. This addresses gaps in existing systems that "process documents in single large chunks or disjointed pages, ignoring structural flow and relying on brittle OCR."

## Design Implications

### Context
#### Requirements
- A multimodal LLM capable of processing contact-sheet images of slide windows
#### Constraints
- The multi-pass architecture incurs substantial LLM inference latency and API costs on large decks

### Target Learners
- undergraduate and graduate students in technical lecture courses

### Target Learning Goals
- pedagogically scaffolded question sets that follow the narrative flow of a presentation

### Affordances
- [Four Stage Windowed Question Pipeline](../designs/four-stage-windowed-question-pipeline.md)

## Related Strategies

- [Before learners see a generated lecture video, run a short instructor review pass targeting voice timing, slide–narration sync, and slide rendering](instructor-review-pass-voice-reveal-rendering.md)
- [Deploy LLM-based slide feedback dashboards before oral presentations so students can iteratively revise slides when teacher feedback is infeasible at scale](deploy-llm-slide-feedback-before-presentations.md)

## Examples
-

## Key Sources
- Salsman, J. (2026). Slide Deck Q&A Quality Assurance App: A Multi-Stage Pipeline for Pedagogical Question Generation. https://arxiv.org/abs/2605.26428. [doi:10.48550/arxiv.2605.26428](https://doi.org/10.48550/arxiv.2605.26428)
