---
type: claim
title: LLM-as-a-judge ratings found only small, incremental differences between systems, with ceiling effects on several criteria
description: LLM-as-a-judge ratings found only small, incremental differences between systems, with ceiling effects on several criteria
id: llm-judge-small-incremental-differences-ceiling
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
sources:
  - id: jiayi-wang-2025
    resource: "https://arxiv.org/abs/2508.16659"
    title: "Jiayi Wang, Ruiwei Xiao, Xinying Hou, John Stamper. (2025). Enabling Multi-Agent Systems as Learning Designers: Applying Learning Sciences to AI Instructional Design. https://arxiv.org/abs/2508.16659"
    author: Jiayi Wang, Ruiwei Xiao, Xinying Hou, John Stamper
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM-as-a-judge ratings found only small, incremental differences between systems, with ceiling effects on several criteria

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across automatic evaluations on the QM and Integrated Learning Sciences rubrics, the largest gap between systems within a model was ≤ 0.7 points (< 7% of scale), and Foundational Alignment and Inclusivity dimensions saturated near their maxima. [→ Jiayi Wang 2025](#jiayi-wang-2025)

## Evidence

### Jiayi Wang 2025

Jiayi Wang, Ruiwei Xiao, Xinying Hou, John Stamper. (2025). Enabling Multi-Agent Systems as Learning Designers: Applying Learning Sciences to AI Instructional Design. https://arxiv.org/abs/2508.16659

`q2 · i?` · `design · r2`

LLM-as-a-judge evaluation of 120 learning activities across four Gemini models and three systems, reported descriptively. The strongest QM total was gemini-2.5-flash + MAS-CMD (M = 10.6, SD = 0.52); the judge showed "incremental gains rather than large separations".

> "Importantly, the largest gap between systems within a model was≤ 0.7 points (< 7% of scale), indicating incremental gains rather than large separations."

## Discussion


## Related Claims
- [Automated judging aligns strongly with three domain experts (r = 0.82 for role fidelity) but exhibits a conservative bias, scoring ethical deviation 0.08 points lower than humans](automated-judge-human-alignment-conservative-bias.md) — related
- [Small language models used as automated judges exhibit severe leniency bias against tutoring responses](slm-judges-show-severe-leniency-bias.md) — related
- [MAS-CMD was rated significantly higher than MAS-Roles on QM criterion 5.2C active learning by 20 expert teachers, with a large effect size](mas-cmd-higher-active-learning-rating-than-mas-roles.md) — related
- [Within-judge variance of the repeated LLM-judge rubric is negligible, but cross-model-family agreement remains untested](within-judge-stability-llm-rubric.md) — related
- [Independent LLM evaluators agreed on agent rankings but differed markedly in leniency, with ceiling effects compressing between-agent discrimination](llm-evaluator-leniency-ceiling-effects.md) — related
