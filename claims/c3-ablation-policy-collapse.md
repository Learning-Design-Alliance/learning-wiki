---
type: claim
title: Removing the behavioral-safety constraint (C3) causes degenerate policy collapse to near-single-action policies, making C3 the most influential safeguard in the ablation study
description: Removing the behavioral-safety constraint (C3) causes degenerate policy collapse to near-single-action policies, making C3 the most influential safeguard in the ablation study
id: c3-ablation-policy-collapse
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: oluseyi-olukolaa-2026
    resource: "https://doi.org/10.48550/arxiv.2604.04237"
    title: "Oluseyi Olukolaa, Nick Rahimia. (2026). Pedagogical Safety in Educational Reinforcement Learning: Formalizing and Detecting Reward Hacking in AI Tutoring Systems. arXiv. https://arxiv.org/abs/2604.04237 [doi:10.48550/arxiv.2604.04237](https://doi.org/10.48550/arxiv.2604.04237)"
    author: Oluseyi Olukolaa, Nick Rahimia
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: oluseyi-olukolaa-2026-2
    resource: "https://arxiv.org/abs/2604.04237"
    title: "Oluseyi Olukolaa, Nick Rahimia. (2026). Pedagogical Safety in Educational Reinforcement Learning: Formalizing and Detecting Reward Hacking in AI Tutoring Systems. arXiv. https://arxiv.org/abs/2604.04237"
    author: Oluseyi Olukolaa, Nick Rahimia
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Removing the behavioral-safety constraint (C3) causes degenerate policy collapse to near-single-action policies, making C3 the most influential safeguard in the ablation study

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q2`

## Subclaims
`q2 i?` Without the C3 action filter, single actions account for 85–93% of interactions in some seeds, C3 violation rises to 68.3%, and pedagogical appropriateness drops from 1.000 to 0.899. [→ Oluseyi Olukolaa 2026](#oluseyi-olukolaa-2026)
`q2 i?` Removing C1 raises RHSI by +0.138, apparently mediated through C3-related degradation of action diversity rather than direct prerequisite violations. [→ Oluseyi Olukolaa 2026 (2)](#oluseyi-olukolaa-2026-2)

## Evidence

### Oluseyi Olukolaa 2026

Oluseyi Olukolaa, Nick Rahimia. (2026). Pedagogical Safety in Educational Reinforcement Learning: Formalizing and Detecting Reward Hacking in AI Tutoring Systems. arXiv. https://arxiv.org/abs/2604.04237 [doi:10.48550/arxiv.2604.04237](https://doi.org/10.48550/arxiv.2604.04237)

`q2 · i?` · `causal · r2`

Ablation simulation (No-C3 condition, 30 sessions under identical protocol). The No-C3 ablation's C3 violation rate of 68.3% approaches EO's 70.8%; inappropriate actions rise from 0 to 15–18 per session. ST vs. No-C3 RHSI difference is Bonferroni-significant (d=−1.42).

> "Removing C3 appears to cause degenerate policy collapse.Without the action filter, the agent does not merely "hack slightly"—it collapses to near-single-actionpolicies."

### Oluseyi Olukolaa 2026 (2)

Oluseyi Olukolaa, Nick Rahimia. (2026). Pedagogical Safety in Educational Reinforcement Learning: Formalizing and Detecting Reward Hacking in AI Tutoring Systems. arXiv. https://arxiv.org/abs/2604.04237

`q2 · i?` · `causal · r2`

No-C1 ablation (30 sessions): mastery gains comparable to full framework and pedagogical appropriateness of 1.000, but RHSI degradation of +0.138. The two ablations do not differ significantly from each other (t(47)=−1.08, p=.285).

> "The C3 violation rate rises to 60.4% not because the agent exploits prerequisite violations, but apparently because without the knowledge graph structuring exploration, the agent’s action diversity degrades."

## Discussion


## Related Claims
- [An engagement-optimized RL tutor exhibits reward hacking, achieving the highest cumulative reward while producing minimal learning and a 70.8% behavioral-safety violation rate](engagement-optimized-rl-tutor-reward-hacking.md) — related
- [Ablations show the semi-Markov controller is the primary driver of behavioral fidelity (removal pushes DKL to 6.81) and Strategist/Executor separation is essential for epistemic fidelity and realism](beagle-ablation-semi-markov-and-decoupling.md) — related
- [A constrained architecture combining prerequisite enforcement and a minimum cognitive-demand floor substantially reduces reward hacking, lowering RHSI from 0.317 (MO) to 0.102 (ST)](constrained-architecture-reduces-rhsi.md) — related
- [A multi-objective reward weighting mastery at 50% does not prevent reward hacking: the MO agent selects the zero-learning Encourage action more often (32.6%) than the engagement-only agent (25.8%)](multi-objective-reward-insufficient-reward-hacking.md) — related
