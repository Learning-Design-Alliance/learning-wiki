---
type: claim
title: Consistency degrades under multi-strategy evaluation for all personas, driven mainly by tone instability rather than logical contradiction
description: Consistency degrades under multi-strategy evaluation for all personas, driven mainly by tone instability rather than logical contradiction
id: consistency-degradation-tone-instability
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
    kind: causal
    rigour: 1
  - id: saqib-shouqi-2026-2
    resource: "https://arxiv.org/abs/2608.03166"
    title: "Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis. (2026). Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation. ADScAI Conference, University of Moratuwa, Sri Lanka. https://arxiv.org/abs/2608.03166"
    author: Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Consistency degrades under multi-strategy evaluation for all personas, driven mainly by tone instability rather than logical contradiction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1` · `q2`

## Subclaims
`q2 i?` Under multi-strategy evaluation, consistency scores declined to 0.614 (Healthcare Assistant), 0.667 (Customer Support Agent), and 0.638 (Financial Advisor), from baseline values above 0.80. [→ Saqib Shouqi 2026](#saqib-shouqi-2026)
`q2 i?` The dominant driver of consistency loss was tone instability: agents shifted between formal and empathetic registers in response to emotional manipulation prompts. [→ Saqib Shouqi 2026 (2)](#saqib-shouqi-2026-2)

## Evidence

### Saqib Shouqi 2026

Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis. (2026). Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation. ADScAI Conference, University of Moratuwa, Sri Lanka. https://arxiv.org/abs/2608.03166

`q2 · i?` · `causal · r1`

Automated scoring of 10-turn dialogues found all personas exhibited CS scores above 0.80 in the baseline condition, while "Under multi-strategy evaluation, CS declined to 0.614 for the Healthcare Assistant, 0.667 for the Customer Support Agent, and 0.638 for the Financial Advisor."

> "Under multi-strategy evaluation, CS declined to 0.614 for the Healthcare Assistant, 0.667 for the Customer Support Agent, and 0.638 for the Financial Advisor."

### Saqib Shouqi 2026 (2)

Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis. (2026). Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation. ADScAI Conference, University of Moratuwa, Sri Lanka. https://arxiv.org/abs/2608.03166

`q2 · i?` · `causal · r1`

Qualitative analysis of consistency losses in the same experiments reports "The dominant driver of consistency loss was tone instability rather than direct logical contradiction," with agents shifting registers under emotional manipulation prompts.

> "The dominant driver of consistency loss was tone instability rather than direct logical contradiction; agents frequently shifted between formal and empathetic registers in response to emotional manipulation prompts, producing behavioral patterns inconsistent with their defined personas."

## Discussion


## Related Claims
- [Multi-strategy adversarial evaluation lowers RPLA robustness scores by 0.174–0.203 points relative to a single-strategy baseline across three personas](multi-strategy-adversarial-testing-lowers-rpla-robustness.md) — related
- [Cross-model validation shows consistent degradation under multi-strategy attack across Llama-3.3-70B, GPT-4o-mini, and Claude-3.5-Haiku, with significant differences between models](cross-model-rpla-degradation-consistent.md) — related
- [Passive backdoor defense (SBD) effectiveness is distillation-dependent, degrading under persona-centric abstraction](passive-sbd-defense-distillation-dependent.md) — related
