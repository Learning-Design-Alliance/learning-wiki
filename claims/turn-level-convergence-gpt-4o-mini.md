---
type: claim
title: GPT-4o mini showed progressive turn-level convergence with accumulating context while larger models showed increasing or stable error
description: GPT-4o mini showed progressive turn-level convergence with accumulating context while larger models showed increasing or stable error
id: turn-level-convergence-gpt-4o-mini
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: pascal-riachi-2026
    resource: "https://arxiv.org/abs/2606.17786"
    title: "Pascal Riachi, Sofie Kamber, Stella Brogna, Andrew Gloster, Rafael Wampfler. (2026). Toward Accessible Psychotherapy Training Using AI-Driven Interactive Patient Avatars. https://arxiv.org/abs/2606.17786"
    author: Pascal Riachi, Sofie Kamber, Stella Brogna, Andrew Gloster, Rafael Wampfler
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o mini showed progressive turn-level convergence with accumulating context while larger models showed increasing or stable error

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In partial-transcript evaluation, GPT-4o mini's MAE decreased from 12.76 at turn 5 to 6.12 at turn 20, whereas GPT-5.1, GPT-5.2, and Claude Sonnet 4.5 showed increasing or stable error with additional context. [→ Pascal Riachi 2026](#pascal-riachi-2026)

## Evidence

### Pascal Riachi 2026

Pascal Riachi, Sofie Kamber, Stella Brogna, Andrew Gloster, Rafael Wampfler. (2026). Toward Accessible Psychotherapy Training Using AI-Driven Interactive Patient Avatars. https://arxiv.org/abs/2606.17786

`q2 · i?` · `design · r2`

Turn-level evaluation rating partial transcripts consisting of the first t therapist turns, computing MAE between the model's partial-transcript rating and the human supervisor's full-session rating. GPT-4o mini showed "progressive alignment" with a 6.64-point MAE improvement from turn 5 to turn 20.

> "GPT-4o mini showed progressive alignment, with MAE decreasing from 12.76 at turn 5 to 6.12 at turn 20 (6.64-point improvement)."

## Discussion


## Related Claims
- [Expert evaluation found the virtual patient realistic and immediate ACT feedback increased therapists' awareness of intervention choices](expert-evaluation-realism-and-feedback-awareness.md) — related
- [Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics](model-migration-component-specific-metric-effects.md) — related
- [GPT-4o mini achieved the lowest ACT balance MAE (6.12) in replicating human supervisor ratings across 49 full transcripts](gpt-4o-mini-lowest-act-balance-mae.md) — related
