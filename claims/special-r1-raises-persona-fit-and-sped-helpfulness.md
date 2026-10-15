---
type: claim
title: The full Special-R1 model raises persona-aware Fit from 6.75 to 8.40 and SPED-rubric Helpfulness from 0.720 to 0.768 over a non-disability-aware baseline
description: The full Special-R1 model raises persona-aware Fit from 6.75 to 8.40 and SPED-rubric Helpfulness from 0.720 to 0.768 over a non-disability-aware baseline
id: special-r1-raises-persona-fit-and-sped-helpfulness
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
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

# The full Special-R1 model raises persona-aware Fit from 6.75 to 8.40 and SPED-rubric Helpfulness from 0.720 to 0.768 over a non-disability-aware baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On a persona-augmented test set of 690 multi-turn dialogues, the full model (M7) raises persona-aware Fit from 6.75 (generic baseline) to 8.40 and SPED-rubric Helpfulness from 0.720 to 0.768. [→ Unggi Lee 2026](#unggi-lee-2026)

## Evidence

### Unggi Lee 2026

Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670 [doi:10.48550/arxiv.2605.30670](https://doi.org/10.48550/arxiv.2605.30670)

`q2 · i?` · `design · r2`

Evaluation of seven trained tutor configurations on the SPED-Tutor-Mix conversational test set (N=690), with LLM-judge scores macro-averaged across disability types. The full model M7 leads the four-component Total at 2.911, "+0.064 over the runner-up" M6, and leads all four persona dimensions simultaneously.

> "On a persona-augmented test set of 690 multi-turn dialogues, our full model raises persona-aware Fit from 6.75 (generic baseline) to 8.40 (+1.65) and SPED-rubric Helpfulness from 0.720 to 0.768"

## Discussion


## Related Claims
- [Specific learning disability in mathematics is the weakest persona profile across all GRPO-trained models](sld-math-weakest-persona-profile.md) — related
- [Prompt style is the largest driver of disability-aware Fit gains, and the Thinking Reward becomes effective only in combination with adaptive prompting](thinking-reward-effective-only-with-adaptive-prompting.md) — related
- [SPED-adaptive prompting shifts tutor behavior toward We-Do scaffolding, naturalistic language support, and participation-affirming feedback across three codebooks](sped-adaptive-shifts-tutor-behavior-codebooks.md) — related
- [Disability-aware training does not degrade out-of-domain educational knowledge on OpenLearnLM](sped-training-no-ood-knowledge-cost.md) — related
