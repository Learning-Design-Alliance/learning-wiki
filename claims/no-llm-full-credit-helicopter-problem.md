---
type: claim
title: "On the Helicopter on Mars problem, none of the LLM-generated solutions received full credit although some student solutions did, despite o1-preview's highly consistent high scores"
description: "On the Helicopter on Mars problem, none of the LLM-generated solutions received full credit although some student solutions did, despite o1-preview's highly consistent high scores"
id: no-llm-full-credit-helicopter-problem
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: tschisgale-2025
    resource: "https://doi.org/10.1103/6fmx-bsnl"
    title: "Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P. (2025). Evaluating GPT- and Reasoning-based Large Language Models on Physics Olympiad Problems: Surpassing Human Performance and Implications for Educational Assessment. [doi:10.1103/6fmx-bsnl](https://doi.org/10.1103/6fmx-bsnl)"
    author: "Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# On the Helicopter on Mars problem, none of the LLM-generated solutions received full credit although some student solutions did, despite o1-preview's highly consistent high scores

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` o1-preview achieved a remarkably consistent score of 9 out of 10 across all 20 generated solutions on the Helicopter problem, yet none of the LLM-generated responses received full credit whereas some student solutions did. [→ Tschisgale 2025](#tschisgale-2025)

## Evidence

### Tschisgale 2025

Tschisgale, P., Maus, H., Kieser, F., Kroehs, B., Petersen, S., & Wulff, P. (2025). Evaluating GPT- and Reasoning-based Large Language Models on Physics Olympiad Problems: Surpassing Human Performance and Implications for Educational Assessment. [doi:10.1103/6fmx-bsnl](https://doi.org/10.1103/6fmx-bsnl)

`q2 · i?` · `design · r2`

Problem-wise scoring analysis of the Helicopter on Mars problem using the official Olympiad scheme; o1-preview scored 9/10 on all 20 solutions, and Mann-Whitney tests showed it differed significantly from all other LLMs and participants on this problem.

> "achieving a remarkably consistent score of 9 out of 10 across all 20 generated solutions. Notably, none of the LLM-generated responses received full credit, whereas some student solutions did."

## Discussion


## Related Claims
- [LLM-generated Olympiad solutions show characteristic errors: assuming rather than deriving key relations, misrepresenting problem geometry in energy analyses, and omitting solution evaluation](llm-characteristic-errors-olympiad-solutions.md) — related
- [The reasoning model o1-preview with general prompting outperformed all GPT-4o prompting setups and Physics Olympiad participants on aggregated Olympiad problem scores, with very large to huge effect sizes](o1-preview-outperforms-gpt4o-and-olympiad-participants.md) — a broader claim this one bears on
- [Score variance differed markedly: Olympiad participants' scores showed substantially higher variance than LLM scores, with o1-preview's scores the most narrowly distributed](score-variance-students-higher-than-llms.md) — a broader claim this one bears on
- [Fewer than 20% of interviewed students could explain why a paper helicopter initially at rest starts to rotate, most not invoking torque](helicopter-rotation-torque-explanation-rare.md) — related
