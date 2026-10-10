---
type: claim
title: In LLM-simulated subjects with known skill levels, the Executive LLM yields better skill-level recovery (lower MAE) than Independent Agents
description: In LLM-simulated subjects with known skill levels, the Executive LLM yields better skill-level recovery (lower MAE) than Independent Agents
id: executive-llm-improves-skill-recovery-simulation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: globerson-2026
    resource: "https://arxiv.org/abs/2609.15864"
    title: "Globerson, A., Keeling, A., Choudhury, A., et al. (2026). Towards Scalable Measurement of Durable Skills. https://arxiv.org/abs/2609.15864"
    author: Globerson, A., Keeling, A., Choudhury, A., et al
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# In LLM-simulated subjects with known skill levels, the Executive LLM yields better skill-level recovery (lower MAE) than Independent Agents

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`

## Subclaims
`q1 i?` Recovery error measured as mean absolute difference between true and inferred skill scores was lower for Executive LLM protocols than Independent Agents (Student's t-test, significant), with simulated conversation evidence rates qualitatively similar to human ones. [→ Globerson 2026](#globerson-2026)

## Evidence

### Globerson 2026

Globerson, A., Keeling, A., Choudhury, A., et al. (2026). Towards Scalable Measurement of Durable Skills. https://arxiv.org/abs/2609.15864

`q1 · i?` · `causal · r2`

Simulation study: Gemini simulated a subject at a specified rubric level (1-4), each level repeated 100 times per protocol, conversations autorated, and mean absolute error computed (Figure 8). "Executive LLM results in overall improved recovery rates, relative to Independent Agents"; simulated evidence rates were qualitatively similar to human results but approached 100%.

> "It can be seen that Executive LLM results in overall improved recovery rates, relative to Independent Agents."

## Discussion


## Related Claims
- [An Executive LLM focused on a skill elicits significantly more skill-related evidence than Independent Agents, with a crossover effect between skills](executive-llm-elicits-more-skill-evidence.md) — related
- [Under persona simulation with hidden ground-truth mastery, Adaptive sessions yield lower final-belief mastery MAE (0.12) than Random-topic (0.16) and Frozen (0.20) controls, and belief updates shrink as estimates converge](collearn-adaptive-mastery-mae-convergence.md) — related
- [Telling subjects to focus on a skill had no significant effect on conversation informativeness in either protocol](subject-focus-instructions-no-effect.md) — related
