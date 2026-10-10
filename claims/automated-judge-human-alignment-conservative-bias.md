---
type: claim
title: Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans
description: Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans
id: automated-judge-human-alignment-conservative-bias
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
    i: 3
    kind: design
    rigour: 2
---

# Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Pearson correlations between mean human scores and automated scores were r = 0.82 for RF, r = 0.78 for ED, and r = 0.75 for CS (all p < 0.001), with inter-annotator agreement of Fleiss' kappa = 0.71. [→ Saqib Shouqi 2026](#saqib-shouqi-2026)

## Evidence

### Saqib Shouqi 2026

Saqib Shouqi, Abdullah Nazly, Januki Wanniarachchi, Ravisha De Alwis. (2026). Adversarial Stress Testing of Role-Playing Language Agents using Multi-Agent Evaluation. ADScAI Conference, University of Moratuwa, Sri Lanka. https://arxiv.org/abs/2608.03166

`q2 · i3` · `design · r2`

A human validation study had three domain experts independently score a stratified sample of 60 conversation turns (20 per persona) on RF, ED, and CS using the same rubrics as the automated judge; the printed correlation was "r = 0.82 for RF," with Fleiss' kappa = 0.71 among humans.

> "Pearson correlation between mean human scores and automated scores was 𝑟= 0.82for RF ( 𝑝< 0.001),𝑟= 0.78for ED ( 𝑝< 0.001), and𝑟= 0.75for CS (𝑝< 0.001), indicating strong alignment."

## Discussion


## Related Claims
- [Claude showed the highest alignment with human BREQ responses, and interview-containing prompts aligned better than baseline prompts](claude-highest-human-alignment-interview-prompts.md) — related
- [Multi-strategy adversarial evaluation lowers RPLA robustness scores by 0.174–0.203 points relative to a single-strategy baseline across three personas](multi-strategy-adversarial-testing-lowers-rpla-robustness.md) — related
- [RPLA failures are temporally distributed: ethical violations are rare in the first three turns and become significantly more frequent after turn 6](rpla-failure-onset-second-half-of-dialogue.md) — related
