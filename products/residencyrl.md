---
type: product
id: residencyrl
title: ResidencyRL
description: ResidencyRL is an online multi-turn reinforcement-learning environment developed for training and evaluating clinical AI agents in simulated patient encounters using an LLM patient simulator, documentation API, and structured autorater.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# ResidencyRL

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
ResidencyRL is an online multi-turn reinforcement-learning environment developed for training and evaluating clinical AI agents in simulated patient encounters using an LLM patient simulator, documentation API, and structured autorater.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **ResidencyRL simulated clinical training environment with documentation API, LLM patient simulator, and structured autorater**: ResidencyRL is an online multi-turn reinforcement learning training environment in which a clinical AI agent conducts complete simulated patient encounters. The environment exposes "an LLM-driven patient simulator and a structured API allowing the agent to document the encounter (e.g., diagnosis, management plan)", with rollouts scaling to 60 dialogue turns and 8 tool calls. An LLM autorater processes the encounter transcript and tool calls to yield a structured reward heavily weighted by clinical accuracy rubrics and critical safety flags. The patient simulator adapts health literacy, information disclosure, and pacing to each scenario's demographic and clinical profile. (ResidencyRL: Reinforcement Learning in Simulated Clinical Environments)

### Claims
- [Multi-turn RL training in simulated clinical encounters improves diagnostic accuracy under adversarial conditions, raising rubric-based accuracy from 81.0% to 88.0%](../claims/residencyrl-improves-adversarial-diagnostic-accuracy.md) [+M]
- [RL training reduces missed red flag rates by approximately one third under adversarial conditions, mitigating premature closure](../claims/residencyrl-reduces-missed-red-flags.md) [+M]
- [Blinded board-certified clinicians prefer the RL-trained agent in 87.6% of side-by-side comparisons for overall clinical impression](../claims/residencyrl-clinician-preference-side-by-side.md) [+M]
- [Procedural competencies from simulation-based RL training generalize to out-of-domain benchmarks including AMIE Mx, AgentClinic, and CRAFT-MD](../claims/residencyrl-generalizes-out-of-domain.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Liévin, V., Schmidgall, S., Strother, T., Bijamov, A., Goel, A., Palepu, A., Park, C., Balazadeh, V., Sun, M. W., Guerard, M., Chen, J., Steiner, D., Dhillon, V., Azar, I., Mehta, A., Spetsieris, N., Shah, S., Abdelrahim, M., Dahiya, A., Liu, Y., Chou, K., Matias, Y., Hassidim, A., Webster, D. R., Le, Q. V., Hadsell, R., Barral, J., Radebaugh, C., Faust, A., Azizi, S., Schaekermann, M., Chen, P.-H. C., Tu, T., Racz, D., & Yang, L. (2026). ResidencyRL: Reinforcement Learning in Simulated Clinical Environments. arXiv. https://arxiv.org/abs/2608.07418
