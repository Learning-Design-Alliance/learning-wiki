---
type: claim
title: "BEAGLE's error recurrence rate (86.2%) falls within the realistic novice envelope, far above vanilla LLMs (7.8%) and below rule-based SimStudent's mechanical saturation (92.0%)"
description: "BEAGLE's error recurrence rate (86.2%) falls within the realistic novice envelope, far above vanilla LLMs (7.8%) and below rule-based SimStudent's mechanical saturation (92.0%)"
id: beagle-error-recurrence-novice-envelope
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

# BEAGLE's error recurrence rate (86.2%) falls within the realistic novice envelope, far above vanilla LLMs (7.8%) and below rule-based SimStudent's mechanical saturation (92.0%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On epistemic fidelity, BEAGLE recurs on the same error type in 86.2% of runs versus 7.8% for vanilla LLMs, while SimStudent's 92.0% reflects rigid production rules rather than higher authenticity. [→ Hanchen David Wang 2026](#hanchen-david-wang-2026)

## Evidence

### Hanchen David Wang 2026

Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280

`q2 · i?` · `design · r2`

Epistemic-fidelity evaluation (RQ2) on the Particle Simulator measuring P_recur, the proportion of runs in which the same error type recurs. Mechanisms credited are observation filtering during ENACTING and the Strategist/Executor split; the ablation reports merging them reduces recurrence by 21%.

> "Vanilla LLMs achieve only 7.8% recurrence (Table 1), quickly resolving diverse errors;BEAGLEsits at 86.2%, within the realistic novice envelope bracketed by Vanilla (7.8%, far below) and rule-based SimStudent (92.0%, which saturates the upper anchor through rigid production rules that mechanically repeat errors rather than higher novice authenticity)."

## Discussion


## Related Claims
- [Ablations show the semi-Markov controller is the primary driver of behavioral fidelity (removal pushes DKL to 6.81) and Strategist/Executor separation is essential for epistemic fidelity and realism](beagle-ablation-semi-markov-and-decoupling.md) — related
- [BEAGLE achieves higher behavioral fidelity to real student cognitive-behavior distributions than LLM prompting and agent baselines on a Particle Simulator task (DKL = 0.31 vs. baselines ≥ 0.53)](beagle-behavioral-fidelity-beats-baselines.md) — related
- [BEAGLE generalizes across tasks and LLM backbones: on the out-of-distribution Gradient Descent task it still shrinks DKL by ≥3×, raises error recurrence to ≥79%, and improves all three perceptual scores](beagle-cross-task-cross-backbone-generalization.md) — related
- [In a human Turing test, participants could not reliably distinguish BEAGLE traces from real student data (52.8% accuracy; d′ = 0.15 within the ±0.3 equivalence bound, pTOST = 0.038)](beagle-traces-turing-test-indistinguishable.md) — related
