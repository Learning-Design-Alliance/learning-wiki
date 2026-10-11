---
type: claim
title: In LLM-assisted team formation, persona nationality systematically shifts assignments, with Nigerian names favored for Quality Assurance and South Korean names for Interface Design relative to Chinese names
description: In LLM-assisted team formation, persona nationality systematically shifts assignments, with Nigerian names favored for Quality Assurance and South Korean names for Interface Design relative to Chinese names
id: llm-team-formation-nationality-bias
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
    i: "?"
    kind: causal
    rigour: 2
---

# In LLM-assisted team formation, persona nationality systematically shifts assignments, with Nigerian names favored for Quality Assurance and South Korean names for Interface Design relative to Chinese names

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Compared to Chinese names, Nigerian names are more likely to be assigned to Quality Assurance, and South Korean names more likely to Interface Design and less likely to Database. [→ Erfan Entezami 2026](#erfan-entezami-2026)

## Evidence

### Erfan Entezami 2026

Erfan Entezami, Andrew Lan, and Madeline Endres. (2026). Generative AI May Reinforce Social Biases in Software Engineering Education. arXiv preprint. https://arxiv.org/abs/2609.28483

`q2 · i?` · `causal · r2`

Multinomial logistic regression over plain-persona assignments (Table 2) shows "Nigerian names are more likely to be assigned toQuality Assurance team" and South Korean names more likely for Interface Design; the article reports significant odds ratios but this quote prints no single effect-size value, so no magnitude is asserted.

> "compared to Chinese names (as the reference nationality), Nigerian names are more likely to be assigned toQuality Assurance team; South Korean names are more likely to be assigned to the Interface Designteam and less likely to be assigned toDatabase team."

## Discussion


## Related Claims
- [In LLM-assisted team formation with name-only personas, male students are significantly less likely than female students to be assigned to Interface Design and Quality Assurance teams relative to Core Development](llm-team-formation-gender-bias-plain-personas.md) — related
- [Even with skill-based qualifications, LLM team assignment remains gender-biased: when two teams are equally valid, models favor Core Development for male personas over Interface Design](llm-team-formation-gender-bias-skill-based.md) — related
- [In LLM-assisted team formation, class standing strongly drives assignments: seniors are far less likely than freshmen to be assigned to Interface Design relative to Core Development](llm-team-formation-class-standing-effect.md) — related
- [Prompting experiments show LLMs perform badly at generating non-US national standard varieties and conflate Nigerian English with Nigerian Pidgin](llms-perform-badly-non-us-standard-varieties.md) — related
