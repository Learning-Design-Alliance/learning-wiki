---
type: design
id: four-stage-windowed-question-pipeline
title: Four-stage windowed pipeline architecture for deck-level question generation
description: "The article's organizing architecture is a multi-pass generative pipeline: a Window Planner that \"Analyzes overlapping windows of slides, creating a contact sheet image to infer titles, summaries, modalities, roles, a..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: salsman-2026
    resource: "https://arxiv.org/abs/2605.26428"
    title: "Salsman, J. (2026). Slide Deck Q&A Quality Assurance App: A Multi-Stage Pipeline for Pedagogical Question Generation. https://arxiv.org/abs/2605.26428"
    author: Salsman, J
---

# Four-stage windowed pipeline architecture for deck-level question generation

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article's organizing architecture is a multi-pass generative pipeline: a Window Planner that "Analyzes overlapping windows of slides, creating a contact sheet image to infer titles, summaries, modalities, roles, and a provisional question budget"; a Deck Synthesis phase merging window analyses into one coherent deck plan; a Slide Annotator generating questions per slide using deck context; and a Reconciliation phase evaluating the full-deck annotation for redundancies and unbalanced coverage. The windowed design is intended to mitigate LLM context limits while preserving the presentation's narrative flow.

## Design Implications

### Context
#### Requirements
- All outputs must conform to strongly typed JSON schemas (Pydantic models SlidePlan, SlideAnnotationModel, ReconciliationModel) to ensure data integrity
#### Constraints
- The multi-pass architecture incurs substantial LLM inference latency and API costs on large decks

### Target Learners
- undergraduate and graduate students in technical lecture courses

### Learning Goals
- deck-level pedagogical scaffolding of comprehension questions across a full presentation

### Claims
- [Reconciliation Zero Budgets Structural Slides](../claims/reconciliation-zero-budgets-structural-slides.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Salsman, J. (2026). Slide Deck Q&A Quality Assurance App: A Multi-Stage Pipeline for Pedagogical Question Generation. https://arxiv.org/abs/2605.26428. [doi:10.48550/arxiv.2605.26428](https://doi.org/10.48550/arxiv.2605.26428)
