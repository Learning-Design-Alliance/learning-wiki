---
type: claim
title: Multi-strategy adversarial evaluation lowers RPLA robustness scores by 0.174–0.203 points relative to a single-strategy baseline across three personas
description: Multi-strategy adversarial evaluation lowers RPLA robustness scores by 0.174–0.203 points relative to a single-strategy baseline across three personas
id: multi-strategy-adversarial-testing-lowers-rpla-robustness
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
---

# Multi-strategy adversarial evaluation lowers RPLA robustness scores by 0.174–0.203 points relative to a single-strategy baseline across three personas

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` Transitioning from single-strategy (Role Drift only) to multi-strategy adversarial evaluation produced a consistent decline in overall robustness scores for all three evaluated personas, with the Healthcare Assistant declining most (0.837 to 0.634). [→ Saqib Shouqi 2026](#saqib-shouqi-2026)

## Evidence

### Saqib Shouqi 2026

Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis. (2026). Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation. ADScAI Conference, University of Moratuwa, Sri Lanka. https://arxiv.org/abs/2608.03166

`q2 · i?` · `causal · r1`

Automated multi-agent experiments comparing a single-strategy baseline (Role Drift only) against a full six-strategy configuration across three personas over 10-turn dialogues. The Healthcare Assistant showed "the most severe degradation (0.837→ 0.634, a decline of 0.203)"; the Customer Support Agent declined 0.174 and the Financial Advisor 0.189. The authors state these results "confirm that single-strategy evaluation meaningfully overestimates agent robustness."

> "The Healthcare Assistant exhibited the most severe degradation (0.837→ 0.634, a decline of 0.203), consistent with the sensitivity of its domain and the difficulty of maintaining strict medical boundaries under sustained emotional and authority-based pressure."

## Discussion


## Related Claims
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
- [Consistency degrades under multi-strategy evaluation for all personas, driven mainly by tone instability rather than logical contradiction](consistency-degradation-tone-instability.md) — related
- [Authority Challenge and Emotional Manipulation are the most effective attack strategies, with consistent rank ordering across three LLM families](authority-challenge-emotional-manipulation-most-effective.md) — related
- [Cross-model validation shows consistent degradation under multi-strategy attack across Llama-3.3-70B, GPT-4o-mini, and Claude-3.5-Haiku, with significant differences between models](cross-model-rpla-degradation-consistent.md) — related
- [RPLA failures are temporally distributed: ethical violations are rare in the first three turns and become significantly more frequent after turn 6](rpla-failure-onset-second-half-of-dialogue.md) — related
- [Passive backdoor defense (SBD) effectiveness is distillation-dependent, degrading under persona-centric abstraction](passive-sbd-defense-distillation-dependent.md) — related
