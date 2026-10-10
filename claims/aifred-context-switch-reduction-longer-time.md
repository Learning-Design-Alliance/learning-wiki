---
type: claim
title: "AIfred reduces observed physical-digital context switches by 98% relative to screen-based assistance, while task completion time is longer"
description: "AIfred reduces observed physical-digital context switches by 98% relative to screen-based assistance, while task completion time is longer"
id: aifred-context-switch-reduction-longer-time
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: gregorio-orlando-2026
    resource: "https://arxiv.org/abs/2609.38737"
    title: "Gregorio Orlando, Milan Groshev, Eduardo Castelló Ferrer. (2026). AIfred: Augmented Learning through Functional Robotic Embodiment at the Desk. https://arxiv.org/abs/2609.38737"
    author: Gregorio Orlando, Milan Groshev, Eduardo Castelló Ferrer
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: gregorio-orlando-2026-2
    resource: "https://arxiv.org/abs/2609.38737"
    title: "Gregorio Orlando, Milan Groshev, Eduardo Castelló Ferrer. (2026). AIfred: Augmented Learning through Functional Robotic Embodiment at the Desk. https://arxiv.org/abs/2609.38737"
    author: Gregorio Orlando, Milan Groshev, Eduardo Castelló Ferrer
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# AIfred reduces observed physical-digital context switches by 98% relative to screen-based assistance, while task completion time is longer

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`

## Subclaims
`q2 i?` Participants averaged 1 context switch with AIfred versus 63 with ChatGPT, a 98% reduction. [→ Gregorio Orlando 2026](#gregorio-orlando-2026)
`q2 i?` Mean task completion time was higher with AIfred (349.5 s) than ChatGPT (259.9 s), p=.02. [→ Gregorio Orlando 2026 (2)](#gregorio-orlando-2026-2)

## Evidence

### Gregorio Orlando 2026

Gregorio Orlando, Milan Groshev, Eduardo Castelló Ferrer. (2026). AIfred: Augmented Learning through Functional Robotic Embodiment at the Desk. https://arxiv.org/abs/2609.38737

`q2 · i?` · `causal · r1`

Behavioral video coding counted visual attention shifts between desk and screen across all tasks: "on average 1 switch with AIfred and 63 with ChatGPT". The count is descriptive; no test statistic is printed for switches.

> "Participants performed on average 1 switch with AIfred and 63 with ChatGPT, a 98% reduction."

### Gregorio Orlando 2026 (2)

Gregorio Orlando, Milan Groshev, Eduardo Castelló Ferrer. (2026). AIfred: Augmented Learning through Functional Robotic Embodiment at the Desk. https://arxiv.org/abs/2609.38737

`q2 · i?` · `causal · r1`

Across all tasks, mean completion time was "higher with AIfred (349.5 seconds vs 259.9 seconds;p=.02)". The authors attribute the additional time to sustained physical engagement with task materials. No effect size is printed.

> "Mean task completion time was higher with AIfred (349.5 seconds vs 259.9 seconds;p=.02)."

## Discussion


## Learner Variables
- [Attention](../learner-variables/attention.md) — outcome: instruction changes it
- [Time and Continuity](../learner-variables/time-and-continuity.md) — outcome: instruction changes it

## Related Claims
- [AIfred and ChatGPT produce comparable math scores while assistance is available](aifred-chatgpt-comparable-assisted-math.md) — related
- [The benefit of spatially co-located AI guidance varies by task: it matters most when instructions and task share a unified spatial frame](spatial-colocation-benefit-task-dependent.md) — related
