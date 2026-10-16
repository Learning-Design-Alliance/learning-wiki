---
type: claim
title: Only the well-specified text-only prompt produced a correct quantitative result from o4-mini, while underspecified prompts led to numerical errors and misleading final results
description: Only the well-specified text-only prompt produced a correct quantitative result from o4-mini, while underspecified prompts led to numerical errors and misleading final results
id: prompt-specificity-shapes-lrm-physics-solution-correctness
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

# Only the well-specified text-only prompt produced a correct quantitative result from o4-mini, while underspecified prompts led to numerical errors and misleading final results

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Across five trials per prompt, only the well-specified text-only prompt elicited a correct quantitative height-evolution result; underspecified prompts typically showed numerical issues producing incorrect or misleading final results. [→ Nikhil Sanjay Borse 2026](#nikhil-sanjay-borse-2026)

## Evidence

### Nikhil Sanjay Borse 2026

Nikhil Sanjay Borse, Amir Bralin, Sean Savage, N. Sanjay Rebello. (2026). Probing AI-generated physics solutions and preparing students to critique them. https://arxiv.org/abs/2608.12533 [doi:10.48550/arxiv.2608.12533](https://doi.org/10.48550/arxiv.2608.12533)

`q2 · i?` · `causal · r1`

Phase I analysis of o4-mini outputs to three prompt variants (five submissions each via the OpenAI API) found that "only the well-specified prompt produced a correct quantitative result" among text-only prompts, with MAPS scores revealing reasoning-quality differences beyond final accuracy.

> "Across pure text-only prompts, only the well-specified prompt produced a correct quantitative result. The MAPS scores, however, revealed differences in reasoning quality beyond final accuracy."

## Discussion


## Related Claims
- [Multimodal prompts caused o4-mini to skip numerical integration and produce only qualitative final responses despite recovering much of the analytical structure](multimodal-prompts-cause-skipped-numerical-integration.md) — related
- [GPT-4o's correctness-labeling errors concentrate on final turns requiring numerical calculation, and its main KC-labeling error is assigning too few standards to a turn.](gpt-4o-annotation-errors-concentrate-on-final-turns-and-too-few-kcs.md) — related
- With images provided, reasoning models achieve higher majority-correct accuracy on image-Required middle-school math items than non-reasoning models — related
- [Interpretable, well-specified AI mechanisms tend to produce clearer learning benefits than technically sophisticated but pedagogically underspecified ones](interpretable-ai-mechanisms-clearer-benefits.md) — related
- [Prompt-writing ability is a new feedback-eliciting capacity that shapes GenAI feedback engagement](prompt-writing-new-feedback-literacy-capacity.md) — related
