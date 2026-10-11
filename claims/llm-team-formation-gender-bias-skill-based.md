---
type: claim
title: "Even with skill-based qualifications, LLM team assignment remains gender-biased: when two teams are equally valid, models favor Core Development for male personas over Interface Design"
description: "Even with skill-based qualifications, LLM team assignment remains gender-biased: when two teams are equally valid, models favor Core Development for male personas over Interface Design"
id: llm-team-formation-gender-bias-skill-based
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
    i: 2
    kind: causal
    rigour: 2
  - id: erfan-entezami-2026-2
    resource: "https://arxiv.org/abs/2609.28483"
    title: "Erfan Entezami, Andrew Lan, and Madeline Endres. (2026). Generative AI May Reinforce Social Biases in Software Engineering Education. arXiv preprint. https://arxiv.org/abs/2609.28483"
    author: Erfan Entezami, Andrew Lan, and Madeline Endres
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Even with skill-based qualifications, LLM team assignment remains gender-biased: when two teams are equally valid, models favor Core Development for male personas over Interface Design

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2` · `i2` medium

## Subclaims
`q2 i2` When choosing between Core Development and Interface Design for equally qualified personas, all models significantly favor Core Development for male personas compared to female personas (GPT-4.1 OR=2.53, GPT-5.2 OR=2.81, DeepSeek OR=1.43, p<0.05). [→ Erfan Entezami 2026](#erfan-entezami-2026)
`q2 i?` Skill qualifications guide assignments strongly: 99.2% of all Skill-based assignments matched one of the two ground-truth teams. [→ Erfan Entezami 2026 (2)](#erfan-entezami-2026-2)

## Evidence

### Erfan Entezami 2026

Erfan Entezami, Andrew Lan, and Madeline Endres. (2026). Generative AI May Reinforce Social Biases in Software Engineering Education. arXiv preprint. https://arxiv.org/abs/2609.28483

`q2 · i2` · `causal · r2`

Pairwise binary logistic regressions over Skill-based persona assignments (Table 5), restricted to on-pair predictions; the models systematically prefer the gender-stereotypical assignment between two equally appropriate teams, with printed odds ratios OR=2.53 (GPT-4.1), OR=2.81 (GPT-5.2), and OR=1.43 (DeepSeek).

> "when choosing between theCore DevelopmentandInterface Designteams, all models significantly favor theCore Development team overInterface Designfor male personas compared to female personas (𝑝< 0.05, GPT 4.1: OR=2.53, GPT-5.2: OR=2.81, DeepSeek: OR=1.43)."

### Erfan Entezami 2026 (2)

Erfan Entezami, Andrew Lan, and Madeline Endres. (2026). Generative AI May Reinforce Social Biases in Software Engineering Education. arXiv preprint. https://arxiv.org/abs/2609.28483

`q2 · i?` · `causal · r2`

Distribution of predicted labels across all models for Skill-based personas (Table 4); the article reports this share descriptively, with no effect size or significance test attached to it.

> "the models overwhelmingly assign students to one of these intended teams, with 99.2% of all assignments matching one of the two ground-truth labels."

## Discussion


## Related Claims
- [In LLM-assisted team formation, class standing strongly drives assignments: seniors are far less likely than freshmen to be assigned to Interface Design relative to Core Development](llm-team-formation-class-standing-effect.md) — related
- [In LLM-assisted team formation with name-only personas, male students are significantly less likely than female students to be assigned to Interface Design and Quality Assurance teams relative to Core Development](llm-team-formation-gender-bias-plain-personas.md) — related
- [In LLM-assisted team formation, persona nationality systematically shifts assignments, with Nigerian names favored for Quality Assurance and South Korean names for Interface Design relative to Chinese names](llm-team-formation-nationality-bias.md) — related
