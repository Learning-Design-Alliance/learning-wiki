---
type: claim
title: Multimodal prompts caused o4-mini to skip numerical integration and produce only qualitative final responses despite recovering much of the analytical structure
description: Multimodal prompts caused o4-mini to skip numerical integration and produce only qualitative final responses despite recovering much of the analytical structure
id: multimodal-prompts-cause-skipped-numerical-integration
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: nikhil-sanjay-borse-2026
    resource: "https://doi.org/10.48550/arxiv.2608.12533"
    title: "Nikhil Sanjay Borse, Amir Bralin, Sean Savage, N. Sanjay Rebello. (2026). Probing AI-generated physics solutions and preparing students to critique them. https://arxiv.org/abs/2608.12533 [doi:10.48550/arxiv.2608.12533](https://doi.org/10.48550/arxiv.2608.12533)"
    author: Nikhil Sanjay Borse, Amir Bralin, Sean Savage, N. Sanjay Rebello
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Multimodal prompts caused o4-mini to skip numerical integration and produce only qualitative final responses despite recovering much of the analytical structure

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Across trials, the multimodal prompt consistently led o4-mini to skip the numerical integration needed for a quantitative height-evolution result, producing qualitative final responses and verbal descriptions instead. [→ Nikhil Sanjay Borse 2026](#nikhil-sanjay-borse-2026)

## Evidence

### Nikhil Sanjay Borse 2026

Nikhil Sanjay Borse, Amir Bralin, Sean Savage, N. Sanjay Rebello. (2026). Probing AI-generated physics solutions and preparing students to critique them. https://arxiv.org/abs/2608.12533 [doi:10.48550/arxiv.2608.12533](https://doi.org/10.48550/arxiv.2608.12533)

`q2 · i?` · `causal · r1`

Phase I numerical results from repeated o4-mini submissions show the multimodal prompt trials "consistently skipped the nu- merical integration needed for a quantitative height-evolution result", yielding only qualitative responses; Table I shows corresponding MAPS scores of 4 on four criteria.

> "The multimodal prompt trials consistently skipped the nu- merical integration needed for a quantitative height-evolution result, instead producing qualitative final responses and ver- bal descriptions."

## Discussion


## Related Claims
- [Only the well-specified text-only prompt produced a correct quantitative result from o4-mini, while underspecified prompts led to numerical errors and misleading final results](prompt-specificity-shapes-lrm-physics-solution-correctness.md) — related
- [MAPS-guided critique preparation led students to identify more expert-aligned weaknesses in an AI solution than independent problem-solving preparation](maps-guided-critique-supports-expert-aligned-evaluation-of-ai-solutions.md) — related
- With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models — related
- [GPT-4o's correctness-labeling errors concentrate on final turns requiring numerical calculation, and its main KC-labeling error is assigning too few standards to a turn.](gpt-4o-annotation-errors-concentrate-on-final-turns-and-too-few-kcs.md) — related
- [Interpretable, well-specified AI mechanisms tend to produce clearer learning benefits than technically sophisticated but pedagogically underspecified ones](interpretable-ai-mechanisms-clearer-benefits.md) — a broader claim this one bears on
