---
type: claim
title: HMM modeling of problem sequences yields four latent states with strong self-transition persistence in three of them
description: HMM modeling of problem sequences yields four latent states with strong self-transition persistence in three of them
id: hmm-four-latent-problem-solving-states
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
sources:
  - id: shan-zhang-2026
    title: Shan Zhang 2026
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: shan-zhang-2026-2
    title: Shan Zhang 2026 (2)
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# HMM modeling of problem sequences yields four latent states with strong self-transition persistence in three of them

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 associational `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` HMMs with BIC-based selection identified four latent states: Mixed, Incomplete-dominant, Optimal-ending, and Replay-dominant, with strong persistence in the latter three. [→ Shan Zhang 2026](#shan-zhang-2026)

## Evidence

### Shan Zhang 2026

Shan Zhang, Siddhartha Pradhan, Ji-Eun Lee, Ashish Gurung, and Anthony F. Botelho. 2026. Let Me Try Again: Examining Replay Behavior by Tracing Students' Latent Problem-Solving Pathways. LAK26: 16th International Learning Analytics and Knowledge Conference. https://doi.org/10.1145/3785022.3785093

`q2 · i?` · `associational · r2`

Hidden Markov Model analysis of FH2T attempt sequences (hmmlearn, one-hot encoded 12 attempt labels) produced "a four-state solution": State 1 Mixed, State 2 Incomplete-dominant, State 3 Optimal-ending, State 4 Replay-dominant.

> "We applied HMMs with 5-fold cross-validation and BIC-based model selection, resulting in a four-state solution (Table 1)."

### Shan Zhang 2026 (2)

Shan Zhang, Siddhartha Pradhan, Ji-Eun Lee, Ashish Gurung, and Anthony F. Botelho. 2026. Let Me Try Again: Examining Replay Behavior by Tracing Students' Latent Problem-Solving Pathways. LAK26: 16th International Learning Analytics and Knowledge Conference. https://doi.org/10.1145/3785022.3785093

`q2 · i?` · `associational · r2`

The HMM transition matrix showed self-transition probabilities of 0.87 for incomplete-dominant and optimal-ending states and 0.79 for replay-dominant, while the mixed state was less stable (0.56), frequently transitioning into replay cycles (0.31).

> "The transition matrix (Figure 3b) showed strong persistence in the incomplete-dominant (0.87), optimal-ending (0.87), and replay-dominant states (0.79)."

## Discussion


## Related Claims
- [Across problems, students show strong self-transitions indicating stable strategic pathways](across-problem-stable-strategic-pathways.md) — related
- [Spending more time in the Mixed latent state is not significantly related to any outcome measure](mixed-state-null-association-outcomes.md) — related
- [Type 2 groups showed a communication–behaviour-synergistic transition, Type 1 a behaviour-oriented, and Type 3 a communication-oriented transition in hidden Markov models](hmm-transitional-regularities-pattern-types.md) — related
- [A Hidden Markov Model over knowledge states identifies Analytical Thinking (A5) as the learning bottleneck with the lowest forward transition probability](hmm-identifies-a5-bottleneck.md) — related
- [Replay-dominant and optimal-ending latent states predict higher conceptual knowledge, flexibility, and state test performance relative to the Incomplete-dominant state](replay-dominant-optimal-ending-states-predict-outcomes.md) — related
- [Within problems, students' strongest transitions reflect persistence in ongoing states and immediate replay after successful solutions](within-problem-persistence-and-immediate-replay-transitions.md) — related
