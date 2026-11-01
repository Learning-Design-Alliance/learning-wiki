---
type: claim
title: "Identical student essays attributed to a \"White\" versus \"Black\" student receive different scores and feedback from ChatGPT, with the \"White\" student scored higher"
description: "Identical student essays attributed to a \"White\" versus \"Black\" student receive different scores and feedback from ChatGPT, with the \"White\" student scored higher"
id: chatgpt-racial-bias-autoscoring-example
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: michael-hardy-2026
    resource: "https://arxiv.org/abs/2603.04820"
    title: "Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820"
    author: Michael Hardy
    q: 1
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# Identical student essays attributed to a "White" versus "Black" student receive different scores and feedback from ChatGPT, with the "White" student scored higher

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` In a demonstration experiment, one-word perturbation of student identity from "White" to "Black" changed ChatGPT's assigned score (1 vs. 0 out of 2) and feedback content on identical 3rd-grade essay work. [→ Michael Hardy 2026](#michael-hardy-2026)

## Evidence

### Michael Hardy 2026

Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820

`q1 · i?` · `quant-synthesis · r2`

Demonstration experiment using OpenAI's chat interface with identical prompts differing only in the one-word perturbation of "White" to "Black". Table 1 shows the "White" student received a score of 1 (out of 2) while the "Black" student received 0 (out of 2), with differing feedback. Single illustrative case; no statistical test reported.

> "Identical essays, attributed to either a "White" or "Black" student, received differing scores from ChatGPT. The “White” student received a higher score."

## Discussion


## Learner Variables
- [Identity](../learner-variables/identity.md) — predictor: learners who differ on it differ in outcomes

## Related Claims
- [Race prompts elicit culturally stereotyped feedback: Black, Hispanic, and Asian students are positioned through cultural or linguistic stereotypes while White students receive argument-structure feedback](race-prompts-cultural-stereotype-feedback.md) — a broader claim this one bears on
- [Names alone elicit weaker, less consistent identity-marked feedback language than explicit attribute prompts](names-alone-elicit-weaker-marked-language.md) — related
- [Explicitly prompting a student attribute produces large, systematic increases in the concentration of stereotype-aligned marked words in LLM-generated writing feedback](prompted-attributes-increase-marked-pedagogy-concentration.md) — related
- [LLM feedback for students marked by race, language, disability, gender, or motivation shows positive feedback bias and feedback withholding bias — more praise and less substantive critique than for unmarked counterparts](marked-students-praise-withholding-bias.md) — related
