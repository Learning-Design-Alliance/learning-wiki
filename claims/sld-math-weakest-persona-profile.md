---
type: claim
title: Specific learning disability in mathematics is the weakest persona profile across all GRPO-trained models
description: Specific learning disability in mathematics is the weakest persona profile across all GRPO-trained models
id: sld-math-weakest-persona-profile
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: unggi-lee-2026
    resource: "https://doi.org/10.48550/arxiv.2605.30670"
    title: "Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670 [doi:10.48550/arxiv.2605.30670](https://doi.org/10.48550/arxiv.2605.30670)"
    author: Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Specific learning disability in mathematics is the weakest persona profile across all GRPO-trained models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Breaking persona-aware Fit by disability type shows specific learning disability in mathematics is the weakest profile across every GRPO-trained model; even M7 drops below 7.8 on sld_math overall Fit. [→ Unggi Lee 2026](#unggi-lee-2026)

## Evidence

### Unggi Lee 2026

Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670 [doi:10.48550/arxiv.2605.30670](https://doi.org/10.48550/arxiv.2605.30670)

`q2 · i?` · `design · r2`

Per-disability-type breakdown of persona-aware Fit scores on SPED-Tutor-Mix reported in the results section. The authors attribute the weakness to a comparatively small number of LD-appropriate mathematics items and a rubric emphasizing alternative representations a text-only tutor cannot deliver.

> "Breaking the persona-aware Fit score by disability type reveals thatspecific learning disability in mathematics( sld_math) is the weakest profile across every GRPO-trained model. Even M7, which leads on every other profile, drops below 7.8 on sld_math overall Fit."

## Discussion


## Related Claims
- [The full Special-R1 model raises persona-aware Fit from 6.75 to 8.40 and SPED-rubric Helpfulness from 0.720 to 0.768 over a non-disability-aware baseline](special-r1-raises-persona-fit-and-sped-helpfulness.md) — related
- [Prompt style is the largest driver of disability-aware Fit gains, and the Thinking Reward becomes effective only in combination with adaptive prompting](thinking-reward-effective-only-with-adaptive-prompting.md) — related
