---
type: claim
title: Prompt style is the largest driver of disability-aware Fit gains, and the Thinking Reward becomes effective only in combination with adaptive prompting
description: Prompt style is the largest driver of disability-aware Fit gains, and the Thinking Reward becomes effective only in combination with adaptive prompting
id: thinking-reward-effective-only-with-adaptive-prompting
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
    kind: causal
    rigour: 1
  - id: unggi-lee-2026-2
    resource: "https://arxiv.org/abs/2605.30670"
    title: "Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670"
    author: Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Prompt style is the largest driver of disability-aware Fit gains, and the Thinking Reward becomes effective only in combination with adaptive prompting

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r1`–`r2` · `q2`

## Subclaims
`q2 i?` Switching the prompt from Normal to SPED-static adds +1.08 on persona-aware Fit (the single largest effect), adaptivity adds +0.45, and activating the Thinking Reward in the adaptive condition adds a further +0.09 on Fit. [→ Unggi Lee 2026](#unggi-lee-2026)
`q2 i?` The Thinking Reward is near-inert in Normal and SPED-static conditions but becomes productive in the adaptive condition, where moving from M6 to M7 raises Total from 2.847 to 2.911 and lowers the leak rate from 11.2% to 8.3%. [→ Unggi Lee 2026 (2)](#unggi-lee-2026-2)

## Evidence

### Unggi Lee 2026

Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670 [doi:10.48550/arxiv.2605.30670](https://doi.org/10.48550/arxiv.2605.30670)

`q2 · i?` · `causal · r1`

Ablation decomposition across the seven trained configurations on SPED-Tutor-Mix, reported in the results section. The article concludes the prompt-style axis does most of the heavy lifting for persona-aware Fit while the Thinking Reward acts as a small multiplier requiring adaptive prompting.

> "Switching the prompt from Normal to SPED-static (M2 vs. M4) adds+0.215on Total and +1.08on Fit, the single largest effect on both axes."

### Unggi Lee 2026 (2)

Unggi Lee, Jihoi Na, Yeil Jeong, Haeun Park, Yeonju Jang. (2026). Reinforcement Learning for Special Education: Aligning LLM Tutors to Diverse Learners through Disability-Adaptive Training. https://arxiv.org/abs/2605.30670

`q2 · i?` · `causal · r2`

Results section comparison of adjacent model configurations on SPED-Tutor-Mix. The authors interpret this as the Thinking Reward needing the structural room opened by adaptive prompting to steer the reasoning distribution.

> "the Thinking Reward is near-inert in the Normal and SPED-static conditions (M3 vs. M2, M5 vs. M4) but becomes productive in the adaptive condition: moving from M6 to M7 raises Total from 2.847 to 2.911, lowers the leak rate from 11.2% to 8.3%"

## Discussion


## Related Claims
- [Specific learning disability in mathematics is the weakest persona profile across all GRPO-trained models](sld-math-weakest-persona-profile.md) — related
- [The full Special-R1 model raises persona-aware Fit from 6.75 to 8.40 and SPED-rubric Helpfulness from 0.720 to 0.768 over a non-disability-aware baseline](special-r1-raises-persona-fit-and-sped-helpfulness.md) — related
- [SPED-adaptive prompting shifts tutor behavior toward We-Do scaffolding, naturalistic language support, and participation-affirming feedback across three codebooks](sped-adaptive-shifts-tutor-behavior-codebooks.md) — related
- [Disability-aware training does not degrade out-of-domain educational knowledge on OpenLearnLM](sped-training-no-ood-knowledge-cost.md) — related
