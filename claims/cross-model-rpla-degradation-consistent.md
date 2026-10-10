---
type: claim
title: Cross-model validation shows consistent degradation under multi-strategy attack across Llama-3.3-70B, GPT-4o-mini, and Claude-3.5-Haiku, with significant differences between models
description: Cross-model validation shows consistent degradation under multi-strategy attack across Llama-3.3-70B, GPT-4o-mini, and Claude-3.5-Haiku, with significant differences between models
id: cross-model-rpla-degradation-consistent
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: saqib-shouqi-2026
    resource: "https://arxiv.org/abs/2608.03166"
    title: "Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis. (2026). Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation. ADScAI Conference, University of Moratuwa, Sri Lanka. https://arxiv.org/abs/2608.03166"
    author: Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Cross-model validation shows consistent degradation under multi-strategy attack across Llama-3.3-70B, GPT-4o-mini, and Claude-3.5-Haiku, with significant differences between models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Under identical multi-strategy adversarial conditions on the Healthcare Assistant persona, Claude-3.5-Haiku scored highest overall (0.712±0.041), GPT-4o-mini intermediate (0.681±0.035), and Llama-3.3-70B lowest (0.634±0.038), with paired t-tests significant between Llama-3.3 and Claude-3.5-Haiku (p<0.01). [→ Saqib Shouqi 2026](#saqib-shouqi-2026)

## Evidence

### Saqib Shouqi 2026

Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis. (2026). Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation. ADScAI Conference, University of Moratuwa, Sri Lanka. https://arxiv.org/abs/2608.03166

`q2 · i?` · `design · r2`

Cross-model validation experiments ran the Healthcare Assistant persona under identical multi-strategy conditions on GPT-4o-mini and Claude-3.5-Haiku, where "Claude-3.5-Haiku exhibited the highest robustness" and Llama-3.3-70B "the most vulnerability." Paired t-tests confirmed significant differences between Llama-3.3 and Claude-3.5-Haiku across all metrics (p<0.01).

> "Claude-3.5-Haiku exhibited the highest robustness (Overall = 0.712± 0.041), followed by GPT-4o-mini (0.681± 0.035), with Llama-3.3-70B showing the most vulnerability to multi-strategy attacks (0.634± 0.038)."

## Discussion


## Related Claims
- [Authority Challenge and Emotional Manipulation are the most effective attack strategies, with consistent rank ordering across three LLM families](authority-challenge-emotional-manipulation-most-effective.md) — related
- [Consistency degrades under multi-strategy evaluation for all personas, driven mainly by tone instability rather than logical contradiction](consistency-degradation-tone-instability.md) — related
- [Prompt settings and temperature settings have significant main effects on correlations among the three LLM chatbots](anova-prompt-temperature-effects-llm-llm-alignment.md) — related
- [Multi-strategy adversarial evaluation lowers RPLA robustness scores by 0.174–0.203 points relative to a single-strategy baseline across three personas](multi-strategy-adversarial-testing-lowers-rpla-robustness.md) — related
- [RPLA failures are temporally distributed: ethical violations are rare in the first three turns and become significantly more frequent after turn 6](rpla-failure-onset-second-half-of-dialogue.md) — related
- [Model selection experiments show newer models are not strict improvements, with component-specific effects on quality metrics](model-migration-component-specific-metric-effects.md) — related
