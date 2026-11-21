---
type: claim
title: Explicit prompt-level anti-bias instructions fail to prevent style-based grading bias in LLMs
description: Explicit prompt-level anti-bias instructions fail to prevent style-based grading bias in LLMs
id: prompt-instructions-fail-to-debias-llm-grading
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: rudra-jadhav-2026
    resource: "https://doi.org/10.48550/arXiv.2603.18765"
    title: "Rudra Jadhav, Janhavi Danve, and Sonalika Shaw. (2026). Implicit Grading Bias in Large Language Models: How Writing Style Affects Automated Assessment Across Math, Programming, and Essay Tasks. Preprint. [doi:10.48550/arXiv.2603.18765](https://doi.org/10.48550/arXiv.2603.18765)"
    author: Rudra Jadhav, Janhavi Danve, and Sonalika Shaw
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Explicit prompt-level anti-bias instructions fail to prevent style-based grading bias in LLMs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Despite grading prompts explicitly instructing models not to penalize grammar, style, or non-standard English, both models showed statistically significant bias with medium-to-very-large effect sizes. [→ Rudra Jadhav 2026](#rudra-jadhav-2026)

## Evidence

### Rudra Jadhav 2026

Rudra Jadhav, Janhavi Danve, and Sonalika Shaw. (2026). Implicit Grading Bias in Large Language Models: How Writing Style Affects Automated Assessment Across Math, Programming, and Essay Tasks. Preprint. [doi:10.48550/arXiv.2603.18765](https://doi.org/10.48550/arXiv.2603.18765)

`q2 · i?` · `causal · r2`

The grading prompt included two explicit anti-bias instructions ("Do NOT penalize for grammar , spelling, punctuation, or writing style"). The article reports that "both models showed statistically significant bias" nonetheless, suggesting bias operates at a representational level deeper than prompt-accessible instruction following.

> "Despite these instructions, both models showed statistically significant bias with effect sizes ranging from medium to very large."

## Discussion


## Related Claims
- [LLMs show statistically significant grading bias for Essay/Writing tasks across all writing-style perturbation types, with large effect sizes](llm-essay-grading-style-bias.md) — related
- [LLMs overrate short underdeveloped essays and over-penalize minor language errors in well-developed essays](llm-overrate-short-essays-overpenalize-errors.md) — related
- [Automated grading systems may produce systematically inequitable outcomes for international and non-Western students](automated-grading-bias-non-native-english.md) — a broader claim this one bears on
- [Feedback prompted with ELL status narrows to surface-level grammar and mechanics corrections, assuming limited language competency rather than addressing argument and reasoning](ell-feedback-language-inadequacy-pedagogy.md) — related
- [Prompt-level interventions to reduce cognates mostly failed, while lower sampling temperature and model self-checking offered partial mitigation](prompt-interventions-cognate-mitigation.md) — related
