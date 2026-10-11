---
type: claim
title: "In LLM-assisted team formation, class standing strongly drives assignments: seniors are far less likely than freshmen to be assigned to Interface Design relative to Core Development"
description: "In LLM-assisted team formation, class standing strongly drives assignments: seniors are far less likely than freshmen to be assigned to Interface Design relative to Core Development"
id: llm-team-formation-class-standing-effect
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

# In LLM-assisted team formation, class standing strongly drives assignments: seniors are far less likely than freshmen to be assigned to Interface Design relative to Core Development

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Seniors are much less likely to be assigned to Interface Design compared to Freshmen (GPT-4.1 OR=0.0004, GPT-5.2 OR=0.004, DeepSeek OR=0.001), with juniors and seniors tending toward Core Development. [→ Erfan Entezami 2026](#erfan-entezami-2026)

## Evidence

### Erfan Entezami 2026

Erfan Entezami, Andrew Lan, and Madeline Endres. (2026). Generative AI May Reinforce Social Biases in Software Engineering Education. arXiv preprint. https://arxiv.org/abs/2609.28483

`q2 · i3` · `causal · r2`

Level-based persona experiment (Table 3) with academic year as an additional predictor; the article reports seniors and juniors tend to be assigned to Core Development while freshmen tend toward Interface Design, with printed odds ratios as extreme as OR=0.0004 (GPT-4.1).

> "Seniors are much less likely to be assigned to theInterface DesignTeam compared to Freshmen (GPT 4.1: OR=0.0004, GPT-5.2: OR=0.004, DeepSeek: OR=0.001)."

## Discussion


## Related Claims
- [In LLM-assisted team formation with name-only personas, male students are significantly less likely than female students to be assigned to Interface Design and Quality Assurance teams relative to Core Development](llm-team-formation-gender-bias-plain-personas.md) — related
- [Even with skill-based qualifications, LLM team assignment remains gender-biased: when two teams are equally valid, models favor Core Development for male personas over Interface Design](llm-team-formation-gender-bias-skill-based.md) — related
- [In LLM-assisted team formation, persona nationality systematically shifts assignments, with Nigerian names favored for Quality Assurance and South Korean names for Interface Design relative to Chinese names](llm-team-formation-nationality-bias.md) — related
