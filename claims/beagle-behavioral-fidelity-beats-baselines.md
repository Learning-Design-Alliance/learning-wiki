---
type: claim
title: BEAGLE achieves higher behavioral fidelity to real student cognitive-behavior distributions than LLM prompting and agent baselines on a Particle Simulator task (DKL = 0.31 vs. baselines ≥ 0.53)
description: BEAGLE achieves higher behavioral fidelity to real student cognitive-behavior distributions than LLM prompting and agent baselines on a Particle Simulator task (DKL = 0.31 vs.
id: beagle-behavioral-fidelity-beats-baselines
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: hanchen-david-wang-2026
    resource: "https://arxiv.org/abs/2602.13280"
    title: "Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280"
    author: Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# BEAGLE achieves higher behavioral fidelity to real student cognitive-behavior distributions than LLM prompting and agent baselines on a Particle Simulator task (DKL = 0.31 vs. baselines ≥ 0.53)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the Particle Simulator task, BEAGLE reaches DKL = 0.31 and Ddebug = 0.02 against real student trajectories, while all baselines score DKL ≥ 0.53 and Ddebug 0.06–0.52. [→ Hanchen David Wang 2026](#hanchen-david-wang-2026)

## Evidence

### Hanchen David Wang 2026

Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280

`q2 · i?` · `design · r2`

Main evaluation on the Particle Simulator (N=50 simulations, T=30 steps, Gemini 2.0 Flash) comparing BEAGLE against nine baselines including Vanilla, CoT, Few-Shot, SimStudent, LLM-SS, and CoderAgent. The paper reports "DKL = 0.31 (vs. baselines≥0.53 )" for behavioral divergence vs. the combined Real evaluation set.

> "BEAGLEachieves DKL = 0.31 (vs. baselines≥0.53 ) and Ddebug = 0.02 (vs. 0.06–0.52)."

## Discussion


## Related Claims
- [Ablations show the semi-Markov controller is the primary driver of behavioral fidelity (removal pushes DKL to 6.81) and Strategist/Executor separation is essential for epistemic fidelity and realism](beagle-ablation-semi-markov-and-decoupling.md) — related
- [BEAGLE generalizes across tasks and LLM backbones: on the out-of-distribution Gradient Descent task it still shrinks DKL by ≥3×, raises error recurrence to ≥79%, and improves all three perceptual scores](beagle-cross-task-cross-backbone-generalization.md) — related
- [BEAGLE's error recurrence rate (86.2%) falls within the realistic novice envelope, far above vanilla LLMs (7.8%) and below rule-based SimStudent's mechanical saturation (92.0%)](beagle-error-recurrence-novice-envelope.md) — related
- [In a human Turing test, participants could not reliably distinguish BEAGLE traces from real student data (52.8% accuracy; d′ = 0.15 within the ±0.3 equivalence bound, pTOST = 0.038)](beagle-traces-turing-test-indistinguishable.md) — related
- [BEAGLE's HIGH and LOW performer profiles differentiate by SRL strategy: HIGH performers allocate 72% of steps to PLANNING and MONITORING while LOW performers spend 50.8% trapped in ENACTING](beagle-profile-strategy-differentiation.md) — related
