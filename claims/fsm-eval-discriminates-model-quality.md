---
type: claim
title: FSM-based evaluation discriminates interactive quality across models, with GPT-5 Mini scoring highest and most tiers significantly separated
description: FSM-based evaluation discriminates interactive quality across models, with GPT-5 Mini scoring highest and most tiers significantly separated
id: fsm-eval-discriminates-model-quality
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: xiaozao-wang-2026
    resource: "https://arxiv.org/abs/2606.31012"
    title: "Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012"
    author: Xiaozao Wang, Zhewei Wang, Hongyi Wen
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: xiaozao-wang-2026-2
    resource: "https://arxiv.org/abs/2606.31012"
    title: "Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012"
    author: Xiaozao Wang, Zhewei Wang, Hongyi Wen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# FSM-based evaluation discriminates interactive quality across models, with GPT-5 Mini scoring highest and most tiers significantly separated

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` FSM metrics significantly separate models: GPT-5 Mini achieves the highest overall score (78.85%) and behavioral coherence (33.13%), significantly outperforming GPT-3.5-Turbo (Δµ = 8.54, p < 0.0001). [→ Xiaozao Wang 2026](#xiaozao-wang-2026)
`q2 i?` FSM evaluation reveals content-dependent interaction demands: structured topics yield more stable transitions, whereas procedural topics show greater variance. [→ Xiaozao Wang 2026 (2)](#xiaozao-wang-2026-2)

## Evidence

### Xiaozao Wang 2026

Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012

`q2 · i?` · `design · r2`

Two-sample Student's t-tests over FSM scores for the six-model study of 2497 generated explanations, reported in Results. GPT-5 Mini scored highest, with a significant separation from GPT-3.5-Turbo; GPT-3.5-Turbo and DeepSeek-V3 showed no significant difference (Δµ = 0.18, p = 0.884).

> "FSM metrics clearly separate models: GPT-5 Mini achieves the highest overall score (78.85%) and behavioral coherence (33.13%), significantly outperforming GPT-3.5-Turbo ( ∆µ= 8.54 , p <0.0001 )."

### Xiaozao Wang 2026 (2)

Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012

`q2 · i?` · `design · r2`

Same discriminative-power analysis (RQ2, Fig. 4) reporting that interaction quality varies by content type: structured topics produced more stable transitions while procedural topics showed greater variance in FSM-based scores.

> "FSM evaluation further reveals content-dependent interaction demands: structured topics yield more stable transitions, whereas procedural topics show greater variance."

## Discussion


## Related Claims
- [FSM-based evaluation aligns with human judgments of interactivity, functional correctness, and visual quality more strongly than VLM and unit-test baselines on balanced data](fsm-eval-aligns-with-human-interactivity-judgments.md) — related
- [Under FSM metrics, GPT-3.5-Turbo outperforms GPT-4o-Mini, reversing that model's higher rank on coding-oriented leaderboards](fsm-gpt35-outperforms-gpt4o-mini-reversal.md) — related
