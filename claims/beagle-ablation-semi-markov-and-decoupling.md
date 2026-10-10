---
type: claim
title: Ablations show the semi-Markov controller is the primary driver of behavioral fidelity (removal pushes DKL to 6.81) and Strategist/Executor separation is essential for epistemic fidelity and realism
description: Ablations show the semi-Markov controller is the primary driver of behavioral fidelity (removal pushes DKL to 6.81) and Strategist/Executor separation is essential for epistemic fidelity and realism
id: beagle-ablation-semi-markov-and-decoupling
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
  - id: hanchen-david-wang-2026-2
    resource: "https://arxiv.org/abs/2602.13280"
    title: "Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280"
    author: Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Ablations show the semi-Markov controller is the primary driver of behavioral fidelity (removal pushes DKL to 6.81) and Strategist/Executor separation is essential for epistemic fidelity and realism

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Removing the semi-Markov controller causes catastrophic divergence from real student distributions (DKL rises to 6.81, versus ≤0.32 for all other ablations). [→ Hanchen David Wang 2026](#hanchen-david-wang-2026)
`q2 i?` Merging Strategist/Executor into a Combined Agent produces the largest realism drop (2.44→1.88) and reduces error recurrence by 21% (86.2%→65.3%). [→ Hanchen David Wang 2026 (2)](#hanchen-david-wang-2026-2)

## Evidence

### Hanchen David Wang 2026

Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280

`q2 · i?` · `design · r2`

Ablation study (N=50, T=30, Gemini 2.0 Flash, Table 2) removing individual BEAGLE modules. The semi-Markov ablation's DKL of 6.81 dwarfs all other variants (0.26–0.32), identifying it as the primary driver of behavioral fidelity.

> "Its removal causes catastrophic divergence from real student distributions ( DKL rises to 6.81, compared to ≤0.32 for all other ablations), confirming that standard LLMs inherently default to linear construction."

### Hanchen David Wang 2026 (2)

Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma. (2026). BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation. Preprint. https://arxiv.org/abs/2602.13280

`q2 · i?` · `design · r2`

Same ablation study (Table 2): the Combined Agent variant, which merges the two LLM stages, shows that without task framing the LLM reverts to skilled error resolution, silently correcting mistakes instead of exhibiting diagnostic incompetence.

> "Merging Strategist/Executor into a Combined Agent produces the largest realism drop (2.44→1.88 ) and reduces error recurrence by 21% (86.2%→65.3% )."

## Discussion


## Related Claims
- [BEAGLE's error recurrence rate (86.2%) falls within the realistic novice envelope, far above vanilla LLMs (7.8%) and below rule-based SimStudent's mechanical saturation (92.0%)](beagle-error-recurrence-novice-envelope.md) — related
- [BEAGLE achieves higher behavioral fidelity to real student cognitive-behavior distributions than LLM prompting and agent baselines on a Particle Simulator task (DKL = 0.31 vs. baselines ≥ 0.53)](beagle-behavioral-fidelity-beats-baselines.md) — related
- [BEAGLE generalizes across tasks and LLM backbones: on the out-of-distribution Gradient Descent task it still shrinks DKL by ≥3×, raises error recurrence to ≥79%, and improves all three perceptual scores](beagle-cross-task-cross-backbone-generalization.md) — related
