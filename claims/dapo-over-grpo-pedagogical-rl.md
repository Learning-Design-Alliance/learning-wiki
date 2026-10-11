---
type: claim
title: DAPO was selected over GRPO for the RL stage because its decoupled policy update gave more stable gradients and superior CDPK performance
description: DAPO was selected over GRPO for the RL stage because its decoupled policy update gave more stable gradients and superior CDPK performance
id: dapo-over-grpo-pedagogical-rl
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: singh-2026
    resource: "https://arxiv.org/abs/2604.06385"
    title: "Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R. (2026). Application-Driven Pedagogical Knowledge Optimization of Open-Source LLMs via Reinforcement Learning and Supervised Fine-Tuning. Preprint. https://arxiv.org/abs/2604.06385"
    author: "Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# DAPO was selected over GRPO for the RL stage because its decoupled policy update gave more stable gradients and superior CDPK performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In ablation studies, DAPO's decoupling of the policy update from advantage estimation provided more stable gradients on multi-step pedagogical reasoning chains and yielded superior CDPK performance compared with GRPO. [→ Singh 2026](#singh-2026)

## Evidence

### Singh 2026

Singh, N. P., Wang, X., Garikipati, A., Ciobanu, M., Mao, Q., & Das, R. (2026). Application-Driven Pedagogical Knowledge Optimization of Open-Source LLMs via Reinforcement Learning and Supervised Fine-Tuning. Preprint. https://arxiv.org/abs/2604.06385

`q2 · i?` · `design · r2`

Ablation study comparing Group Relative Policy Optimization (GRPO) and Decoupled Advantage Policy Optimization (DAPO) during the first RL stage; the authors report DAPO yielded "superior performance on the CDPK Benchmark". No effect size or accuracy for the ablation is printed.

> "We found that DAPO's ability to decouple the policy update from the advantage estimation provided more stable gradients when training on the complex, multi-step reasoning chains required for pedagogical scaffolding, ultimately yielding superior performance on the CDPK Benchmark, and was therefore selected as our primary RL algorithm."

## Discussion


## Related Claims
- [Both RL stages are needed: removing DPO and GRPO training causes the largest performance drop in student simulation](rl-stages-needed-faithful-student-simulation.md) — related
- [GRPO training shifts profiles from broad summaries toward diagnostic, behaviorally grounded representations that better support simulation](grpo-refines-profiles-toward-diagnostic-representations.md) — related
