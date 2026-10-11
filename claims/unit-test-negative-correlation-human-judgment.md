---
type: claim
title: Unit-test-based evaluation shows consistently negative correlations with human judgment, disproportionately penalizing complex high-quality interactive designs
description: Unit-test-based evaluation shows consistently negative correlations with human judgment, disproportionately penalizing complex high-quality interactive designs
id: unit-test-negative-correlation-human-judgment
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: xiaozao-wang-2026
    resource: "https://arxiv.org/abs/2606.31012"
    title: "Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012"
    author: Xiaozao Wang, Zhewei Wang, Hongyi Wen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Unit-test-based evaluation shows consistently negative correlations with human judgment, disproportionately penalizing complex high-quality interactive designs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The unit test baseline correlates negatively with human ratings across all dimensions (interactivity r = −0.600), suggesting brittle test scripts penalize complex but high-quality interactive designs. [→ Xiaozao Wang 2026](#xiaozao-wang-2026)

## Evidence

### Xiaozao Wang 2026

Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012

`q2 · i?` · `design · r2`

Authors' interpretation of the balanced-dataset results in the paper, where the unit test baseline using LLM-generated Playwright tests showed negative correlations with human judgments on all four dimensions, including r = −0.600 on interactivity per Table 1.

> "Unit testing shows consistently negative correlations, suggesting that brittle test scripts disproportionately penalize complex but high-quality interactive designs."

## Discussion


## Related Claims
- [FSM-based evaluation aligns with human judgments of interactivity, functional correctness, and visual quality more strongly than VLM and unit-test baselines on balanced data](fsm-eval-aligns-with-human-interactivity-judgments.md) — related
