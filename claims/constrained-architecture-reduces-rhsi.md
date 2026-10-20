---
type: claim
title: A constrained architecture combining prerequisite enforcement and a minimum cognitive-demand floor substantially reduces reward hacking, lowering RHSI from 0.317 (MO) to 0.102 (ST)
description: A constrained architecture combining prerequisite enforcement and a minimum cognitive-demand floor substantially reduces reward hacking, lowering RHSI from 0.317 (MO) to 0.102 (ST)
id: constrained-architecture-reduces-rhsi
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
    i: 3
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

# A constrained architecture combining prerequisite enforcement and a minimum cognitive-demand floor substantially reduces reward hacking, lowering RHSI from 0.317 (MO) to 0.102 (ST)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` SmartTutor Full (ST) achieves a mean per-seed RHSI of 0.095±0.028, significantly lower than EO (d=−1.45) and MO (d=−1.50) at Bonferroni-corrected levels. [→ Oluseyi Olukolaa 2026](#oluseyi-olukolaa-2026)
`q2 i?` ST's C3 violation rate of 5.8% is substantially lower than EO (70.8%), MO (58.0%), and MAS (39.1%). [→ Oluseyi Olukolaa 2026 (2)](#oluseyi-olukolaa-2026-2)

## Evidence

### Oluseyi Olukolaa 2026

Oluseyi Olukolaa, Nick Rahimia. (2026). Pedagogical Safety in Educational Reinforcement Learning: Formalizing and Detecting Reward Hacking in AI Tutoring Systems. arXiv. https://arxiv.org/abs/2604.04237 [doi:10.48550/arxiv.2604.04237](https://doi.org/10.48550/arxiv.2604.04237)

`q2 · i3` · `causal · r2`

Simulation of the SmartTutor Full (ST) condition with C1 action masking and C3 demand floor (δmin=0.4) enforced online, 30 sessions. Per-seed Welch t-tests with Bonferroni correction show large effect sizes (d=−1.45, d=−1.50) favoring ST on RHSI.

> "ST's mean per-seed RHSI (0.095±0.028) is significantly lower than both EO (t(29) =−5.62,p<.0001,d=−1.45) and MO (t(30) =−5.80,p<.0001,d=−1.50; Table 7)."

### Oluseyi Olukolaa 2026 (2)

Oluseyi Olukolaa, Nick Rahimia. (2026). Pedagogical Safety in Educational Reinforcement Learning: Formalizing and Detecting Reward Hacking in AI Tutoring Systems. arXiv. https://arxiv.org/abs/2604.04237

`q2 · i?` · `causal · r2`

Constraint violation rates computed from session logs across the four main conditions. ST also achieves the lowest C2 violation rate (21.4%) and a competitive C4 violation (34.5%), suggesting architectural constraints jointly improve safety across soft constraint dimensions.

> "ST's C3 violation rate of 5.8% is substantially lower than all unconstrainedconditions: EO (70.8%), MO (58.0%), and MAS (39.1%)."

## Discussion


## Related Claims
- [The RHSI condition ordering is robust across a 20-cell window-size and demand-floor grid, with EO strictly worst in all cells, though ST–MAS ordering reverses at demand floors ≥0.45](rhsi-ordering-parameter-robustness.md) — related
- [An engagement-optimized RL tutor exhibits reward hacking, achieving the highest cumulative reward while producing minimal learning and a 70.8% behavioral-safety violation rate](engagement-optimized-rl-tutor-reward-hacking.md) — related
- [A multi-objective reward weighting mastery at 50% does not prevent reward hacking: the MO agent selects the zero-learning Encourage action more often (32.6%) than the engagement-only agent (25.8%)](multi-objective-reward-insufficient-reward-hacking.md) — related
- [In a simulated tutoring agent, removing the behavioral-safety constraint (C3) appears to cause collapse to near-single-action policies, which the authors read as C3 being the most influential safeguard, though its ablation does not differ significantly from removing C1 in RHSI](c3-ablation-policy-collapse.md) — related
- [Multi-agent tutoring architectures show superior behaviour modelling and feedback compared to single-agent or rule-based tutors](multi-agent-tutoring-superior-single-agent.md) — related
