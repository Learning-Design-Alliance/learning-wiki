---
type: claim
title: Optimizing pedagogical parameters on proxy measures risks trading learning for engagement, and simulated students carry their own accuracy limits
description: Optimizing pedagogical parameters on proxy measures risks trading learning for engagement, and simulated students carry their own accuracy limits
id: proxy-optimization-engagement-trap
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: weak
sources:
  - id: pelánek-2025
    resource: "https://doi.org/10.1007/s40593-024-00400-6"
    title: "Pelánek, R. (2025). Adaptive Learning is Hard: Challenges, Nuances, and Trade-offs in Modeling. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00400-6"
    author: Pelánek, R.
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
  - id: pelánek-2025-2
    resource: "https://doi.org/10.1007/s40593-024-00400-6"
    title: "Pelánek, R. (2025). Adaptive Learning is Hard: Challenges, Nuances, and Trade-offs in Modeling. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00400-6"
    author: Pelánek, R.
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
---

# Optimizing pedagogical parameters on proxy measures risks trading learning for engagement, and simulated students carry their own accuracy limits

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · theoretical `r3` · `q1`

## Subclaims
`q1 i?` Straightforwardly optimizing a system on a proxy measure such as engagement can produce an environment that appears engaging but sacrifices learning outcomes. [→ Pelánek 2025](#pelanek-2025)
`q1 i?` Parameter tuning via simulated students is limited because simulated students are simplifications and simulation accuracy depends on the simplifying assumptions employed. [→ Pelánek 2025 (2)](#pelanek-2025-2)

## Evidence

### Pelánek 2025

Pelánek, R. (2025). Adaptive Learning is Hard: Challenges, Nuances, and Trade-offs in Modeling. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00400-6

`q1 · i?` · `theoretical · r3`

The author's argument in the Parameter Setting section: lifelong learning is distant and indirectly measurable, proxies like engagement or short-term gains are hard to quantify due to data biases, and the "trap of optimizing for engagement" risks sacrificing learning.

> "it is easy to fall into the trap of optimizing for engagement, which is relatively easy to measure – we may inadvertently create a learning environment that appears fun and engaging but sacriﬁces actual learning outcomes in the process."

### Pelánek 2025 (2)

Pelánek, R. (2025). Adaptive Learning is Hard: Challenges, Nuances, and Trade-offs in Modeling. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-024-00400-6

`q1 · i?` · `theoretical · r3`

The article's stated drawback of the simulation alternative for parameter setting: "Simulated students are, by necessity, simpliﬁcations of real students", so results depend on the simplifying assumptions used.

> "Simulated students are, by necessity, simpliﬁcations of real students, and the accuracy of simulation results depends on the simplifying assumptions employed."

## Discussion


## Related Claims
- [An engagement-optimized RL tutor exhibits reward hacking, achieving the highest cumulative reward while producing minimal learning and a 70.8% behavioral-safety violation rate](engagement-optimized-rl-tutor-reward-hacking.md) — a narrower finding that bears on this claim
- [An analytical chapter identifies reward hacking, engagement optimization over learning, and scaffolding dependency as risks of RL policies with poorly specified rewards](rl-reward-misalignment-failure-modes.md) — a broader claim this one bears on
- [Edu-QuRater rewards alone raise pedagogical-quality win rate (77.70%) but fall below parity on instruction following (40.54%), consistent with over-optimizing a proxy reward](edu-qurater-rewards-alone-below-parity-instruction-following.md) — a narrower finding that bears on this claim
- [In a simulated tutoring agent, removing the behavioral-safety constraint (C3) appears to cause collapse to near-single-action policies, which the authors read as C3 being the most influential safeguard, though its ablation does not differ significantly from removing C1 in RHSI](c3-ablation-policy-collapse.md) — related
- [Reviewed literature reports risks of overreliance, AI errors in complex tasks, and students' uncritical acceptance of AI-generated outputs](ai-math-risks-overreliance-errors-uncritical-trust.md) — related
- [Persistent challenges include feedback inaccuracy, learner overreliance, and limited transparency](customized-ai-writing-persistent-challenges.md) — related
