---
type: claim
title: Disability-aware training does not degrade out-of-domain educational knowledge on OpenLearnLM
description: Disability-aware training does not degrade out-of-domain educational knowledge on OpenLearnLM
id: sped-training-no-ood-knowledge-cost
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# Disability-aware training does not degrade out-of-domain educational knowledge on OpenLearnLM

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All thinking-enabled models cluster in the 8.51-8.54 range on the OpenLearnLM overall average, and M7 reaches 8.53, essentially tied with the best variant, indicating the SPED axis does not meaningfully trade off broad educational knowledge. [→ Unggi Lee 2026](#unggi-lee-2026)

## Evidence

### Unggi Lee 2026

Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670 [doi:10.48550/arxiv.2605.30670](https://doi.org/10.48550/arxiv.2605.30670)

`q2 · i?` · `design · r2`

Out-of-domain evaluation on the OpenLearnLM benchmark (N=3,714) across Skills, Content, Pedagogical, and Attitude categories, scored by LLM judge or accuracy. The article notes this is consistent with prior findings that dialogue-based RL preserves base-model knowledge.

> "The SPED axis does not meaningfully trade off broad educational knowledge: M7 reaches 8.53, essentially tied with the best variant (M5 / M6 at 8.54) and 0.77 points above M1."

## Discussion


## Related Claims
- [The full Special-R1 model raises persona-aware Fit from 6.75 to 8.40 and SPED-rubric Helpfulness from 0.720 to 0.768 over a non-disability-aware baseline](special-r1-raises-persona-fit-and-sped-helpfulness.md) — related
- [Prompt style is the largest driver of disability-aware Fit gains, and the Thinking Reward becomes effective only in combination with adaptive prompting](thinking-reward-effective-only-with-adaptive-prompting.md) — related
- [Practical educational skill does not follow from knowledge scores: Claude-Opus-4.5 achieves the highest Skills average (8.82) despite the lowest Content Knowledge](skills-independent-of-knowledge-scores-llms.md) — related
- [Knowledge, Skills, and Attitude scores are largely independent across frontier LLMs, with Knowledge–Skills correlation r=−0.51 and Knowledge–Attitude r=−0.63](ksa-dimensions-weakly-negative-correlated-llms.md) — related
