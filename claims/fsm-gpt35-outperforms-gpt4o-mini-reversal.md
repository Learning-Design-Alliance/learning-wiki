---
type: claim
title: "Under FSM metrics, GPT-3.5-Turbo outperforms GPT-4o-Mini, reversing that model's higher rank on coding-oriented leaderboards"
description: "Under FSM metrics, GPT-3.5-Turbo outperforms GPT-4o-Mini, reversing that model's higher rank on coding-oriented leaderboards"
id: fsm-gpt35-outperforms-gpt4o-mini-reversal
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
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

# Under FSM metrics, GPT-3.5-Turbo outperforms GPT-4o-Mini, reversing that model's higher rank on coding-oriented leaderboards

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` GPT-3.5-Turbo consistently outperforms GPT-4o-Mini under FSM metrics despite GPT-4o-Mini ranking above it (Z-score 0.30 vs −2.98) on the APXML coding leaderboard. [→ Xiaozao Wang 2026](#xiaozao-wang-2026)

## Evidence

### Xiaozao Wang 2026

Xiaozao Wang, Zhewei Wang, Hongyi Wen. (2026). Evaluating Interactivity: Toward Automated Assessment of AI-Generated Explorable Explanations. https://arxiv.org/abs/2606.31012

`q2 · i?` · `design · r2`

Results-section comparison across the six generated-model corpus. The authors attribute the reversal to GPT-4o-Mini producing functionally correct interfaces that under-specify interaction states, while GPT-3.5-Turbo more consistently externalizes interaction structure, yielding higher FSM coverage and behavioral coherence.

> "Under FSM metrics, however, GPT-3.5-Turbo consistently outperforms GPT-4o-Mini despite its lower nominal capacity."

## Discussion


## Related Claims
- [FSM-based evaluation discriminates interactive quality across models, with GPT-5 Mini scoring highest and most tiers significantly separated](fsm-eval-discriminates-model-quality.md) — related
- [Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics](model-migration-component-specific-metric-effects.md) — a broader claim this one bears on
