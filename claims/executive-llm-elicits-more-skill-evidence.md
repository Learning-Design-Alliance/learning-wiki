---
type: claim
title: An Executive LLM focused on a skill elicits significantly more skill-related evidence than Independent Agents, with a crossover effect between skills
description: An Executive LLM focused on a skill elicits significantly more skill-related evidence than Independent Agents, with a crossover effect between skills
id: executive-llm-elicits-more-skill-evidence
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: globerson-2026
    resource: "https://arxiv.org/abs/2609.15864"
    title: "Globerson, A., Keeling, A., Choudhury, A., et al. (2026). Towards Scalable Measurement of Durable Skills. https://arxiv.org/abs/2609.15864"
    author: Globerson, A., Keeling, A., Choudhury, A., et al
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: globerson-2026-2
    resource: "https://arxiv.org/abs/2609.15864"
    title: "Globerson, A., Keeling, A., Choudhury, A., et al. (2026). Towards Scalable Measurement of Durable Skills. https://arxiv.org/abs/2609.15864"
    author: Globerson, A., Keeling, A., Choudhury, A., et al
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# An Executive LLM focused on a skill elicits significantly more skill-related evidence than Independent Agents, with a crossover effect between skills

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` At turn and conversation levels, a skill-matched Executive LLM elicited significantly more evidence for that skill than Independent Agents (Fisher exact test, p≤0.05), with conversation-level evidence rates of 92.4% for PM and 85% for CR. [→ Globerson 2026](#globerson-2026)
`q2 i?` Steering toward one sub-skill reduces evidence of the other (crossover), except for PM at the conversation level where both Executive LLM versions yielded similar rates. [→ Globerson 2026 (2)](#globerson-2026-2)

## Evidence

### Globerson 2026

Globerson, A., Keeling, A., Choudhury, A., et al. (2026). Towards Scalable Measurement of Durable Skills. https://arxiv.org/abs/2609.15864

`q2 · i?` · `causal · r2`

Randomized comparison of three protocols (CR Executive LLM, PM Executive LLM, Independent Agents) in 373 human conversations; starred brackets denote statistically significant differences (p≤0.05) using the Fisher exact test in Figures 6 and 7. "an Executive LLM focused on a skill always elicits significantly more evidence"; the skill-matched conversation-level rate was 92.4% for PM and 85% for CR.

> "First, it can be seen that an Executive LLM focused on a skill always elicits significantly more evidence for that skill than the Independent Agents."

### Globerson 2026 (2)

Globerson, A., Keeling, A., Choudhury, A., et al. (2026). Towards Scalable Measurement of Durable Skills. https://arxiv.org/abs/2609.15864

`q2 · i?` · `causal · r2`

Same randomized human-conversation comparison: a crossover effect in which each Executive LLM version raises its matched skill's evidence and lowers the mismatched skill's, significant in three of four comparisons; PM at conversation level showed no significant difference between versions.

> "That is, steering the conversation towards CR increases evidence of CR but reduces evidence of PM and vice versa. This results in a significant difference in three of the four figures, except for measuring PM at the conversation level (Figure 7, Right), where similar information levels are obtained for both Executive LLM versions."

## Discussion


## Related Claims
- [Telling subjects to focus on a skill had no significant effect on conversation informativeness in either protocol](subject-focus-instructions-no-effect.md) — related
- [In LLM-simulated subjects with known skill levels, the Executive LLM yields better skill-level recovery (lower MAE) than Independent Agents](executive-llm-improves-skill-recovery-simulation.md) — related
