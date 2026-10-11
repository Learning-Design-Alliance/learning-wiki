---
type: claim
title: In LLM-assisted team formation with name-only personas, male students are significantly less likely than female students to be assigned to Interface Design and Quality Assurance teams relative to Core Development
description: In LLM-assisted team formation with name-only personas, male students are significantly less likely than female students to be assigned to Interface Design and Quality Assurance teams relative to Core Development
id: llm-team-formation-gender-bias-plain-personas
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: erfan-entezami-2026
    resource: "https://arxiv.org/abs/2609.28483"
    title: "Erfan Entezami, Andrew Lan, and Madeline Endres. (2026). Generative AI May Reinforce Social Biases in Software Engineering Education. arXiv preprint. https://arxiv.org/abs/2609.28483"
    author: Erfan Entezami, Andrew Lan, and Madeline Endres
    q: 2
    i: 3
    kind: causal
    rigour: 2
---

# In LLM-assisted team formation with name-only personas, male students are significantly less likely than female students to be assigned to Interface Design and Quality Assurance teams relative to Core Development

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Across three LLMs assigning name-only student personas, men are at least 80% less likely than women to be assigned to Interface Design, with the largest bias for GPT-5.2 (OR<0.01). [→ Erfan Entezami 2026](#erfan-entezami-2026)

## Evidence

### Erfan Entezami 2026

Erfan Entezami, Andrew Lan, and Madeline Endres. (2026). Generative AI May Reinforce Social Biases in Software Engineering Education. arXiv preprint. https://arxiv.org/abs/2609.28483

`q2 · i3` · `causal · r2`

Controlled experiment in which GPT-4.1, GPT-5.2, and DeepSeek V3.2 assigned 1400 plain-persona assignments each; multinomial logistic regression with female and China as reference categories found "men are at least 80% less likely to be assigned toInterface Designteam than women", with the printed odds ratio OR<0.01 for GPT-5.2.

> "Across all models, men are at least 80% less likely to be assigned toInterface Designteam than women, with GPT 5.2 demonstrating the largest bias (OR<0.01)."

## Discussion


## Related Claims
- [In LLM-assisted team formation, class standing strongly drives assignments: seniors are far less likely than freshmen to be assigned to Interface Design relative to Core Development](llm-team-formation-class-standing-effect.md) — related
- [Even with skill-based qualifications, LLM team assignment remains gender-biased: when two teams are equally valid, models favor Core Development for male personas over Interface Design](llm-team-formation-gender-bias-skill-based.md) — related
- [In LLM-assisted team formation, persona nationality systematically shifts assignments, with Nigerian names favored for Quality Assurance and South Korean names for Interface Design relative to Chinese names](llm-team-formation-nationality-bias.md) — related
