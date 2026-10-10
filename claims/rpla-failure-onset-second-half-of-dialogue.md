---
type: claim
title: "RPLA failures are temporally distributed: ethical violations are rare in the first three turns and become significantly more frequent after turn 6"
description: "RPLA failures are temporally distributed: ethical violations are rare in the first three turns and become significantly more frequent after turn 6"
id: rpla-failure-onset-second-half-of-dialogue
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
    rigour: 2
---

# RPLA failures are temporally distributed: ethical violations are rare in the first three turns and become significantly more frequent after turn 6

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Across all personas, ethical violations were rarely observed in the first three turns and became significantly more frequent after turn 6, suggesting sustained adversarial pressure is necessary to expose constraint weaknesses. [→ Saqib Shouqi 2026](#saqib-shouqi-2026)

## Evidence

### Saqib Shouqi 2026

Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis. (2026). Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation. ADScAI Conference, University of Moratuwa, Sri Lanka. https://arxiv.org/abs/2608.03166

`q2 · i?` · `causal · r2`

Analysis of 10-turn adversarial dialogues across three personas found "ethical violations were rarely observed in the first three turns and became significantly more frequent after turn 6." The authors conclude short or single-turn evaluations produce systematically optimistic robustness assessments.

> "Across all personas, ethical violations were rarely observed in the first three turns and became significantly more frequent after turn 6, suggesting that sustained adversarial pressure is necessary to expose constraint weaknesses."

## Discussion


## Related Claims
- [Multi-strategy adversarial evaluation lowers RPLA robustness scores by 0.174–0.203 points relative to a single-strategy baseline across three personas](multi-strategy-adversarial-testing-lowers-rpla-robustness.md) — related
- [Cross-model validation shows consistent degradation under multi-strategy attack across Llama-3.3-70B, GPT-4o-mini, and Claude-3.5-Haiku, with significant differences between models](cross-model-rpla-degradation-consistent.md) — related
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
