---
type: claim
title: Ped. Think Reward achieves the best tutoring performance among trained models, and Thinking Reward is most effective when combined with pedagogical prompting
description: Ped.
id: thinking-reward-needs-pedagogical-prompting
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: unggi-lee-2026
    resource: "https://doi.org/10.48550/arXiv.2601.14560"
    title: "Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee. (2026). Rewarding How Models Think Pedagogically: Integrating Pedagogical Reasoning and Thinking Rewards for LLMs in Education. arXiv. [doi:10.48550/arXiv.2601.14560](https://doi.org/10.48550/arXiv.2601.14560)"
    author: Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee
    q: 2
    i: "?"
    kind: causal
    rigour: 1
  - id: unggi-lee-2026-2
    resource: "https://doi.org/10.48550/arXiv.2601.14560"
    title: "Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee. (2026). Rewarding How Models Think Pedagogically: Integrating Pedagogical Reasoning and Thinking Rewards for LLMs in Education. arXiv. [doi:10.48550/arXiv.2601.14560](https://doi.org/10.48550/arXiv.2601.14560)"
    author: Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Ped. Think Reward achieves the best tutoring performance among trained models, and Thinking Reward is most effective when combined with pedagogical prompting

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Ped. Think Reward achieved the highest Delta Solve Rate (0.294), lowest Leak Rate (0.172), and highest Helpful Rate (0.776) among the trained models. [→ Unggi Lee 2026](#unggi-lee-2026)
`q2 i?` Adding Thinking Reward to pedagogical prompting improved Delta Solve Rate by 6.9% and reduced Leak Rate by 19.6% relative to pedagogical prompting alone. [→ Unggi Lee 2026 (2)](#unggi-lee-2026-2)

## Evidence

### Unggi Lee 2026

Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee. (2026). Rewarding How Models Think Pedagogically: Integrating Pedagogical Reasoning and Thinking Rewards for LLMs in Education. arXiv. [doi:10.48550/arXiv.2601.14560](https://doi.org/10.48550/arXiv.2601.14560)

`q2 · i?` · `causal · r1`

Results table comparison across five RL-trained conditions on BigMath with a simulated student; the article reports "highest Delta Solve Rate (0.294), lowest Leak Rate (0.172), and highest Helpful Rate (0.776)" for Ped. Think Reward. No standardized effect size is printed.

> "Ped. Think Reward achieves the best performance among our trained models across all three metrics: highest Delta Solve Rate (0.294), lowest Leak Rate (0.172), and highest Helpful Rate (0.776)."

### Unggi Lee 2026 (2)

Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee. (2026). Rewarding How Models Think Pedagogically: Integrating Pedagogical Reasoning and Thinking Rewards for LLMs in Education. arXiv. [doi:10.48550/arXiv.2601.14560](https://doi.org/10.48550/arXiv.2601.14560)

`q2 · i?` · `causal · r2`

Ablation comparison between the pedagogical prompting condition with and without Thinking Reward in the same RL training setup; the article reports "a 6.9% improvement in Delta Solve Rate and a 19.6% reduction in Leak Rate". No standardized effect size is printed.

> "comparing Ped. Think NoReward to Ped. Think Reward shows a 6.9% improvement in Delta Solve Rate and a 19.6% reduction in Leak Rate."

## Discussion


## Related Claims
- [Pedagogical prompting increases mathematical problem-solving content and reduces excessive praise in tutor responses](pedagogical-prompting-shifts-tutor-behavior.md) — related
- [Enabling internal thinking dramatically improves LLM tutor performance in simulated mathematics tutoring (+134% Delta Solve Rate, +306% Helpful Rate)](thinking-capability-improves-llm-tutoring.md) — related
- [Thinking reward combined with pedagogical prompting produces more focused reasoning traces and responsive-teaching patterns in tutor thinking](thinking-reward-reshapes-reasoning-structure.md) — related
- [Prompt style is the largest driver of disability-aware Fit gains, and the Thinking Reward becomes effective only in combination with adaptive prompting](thinking-reward-effective-only-with-adaptive-prompting.md) — related
- [Thinking reward does not independently affect praise frequency; the praise reduction is driven by pedagogical prompting](thinking-reward-no-independent-praise-effect.md) — related
- [Reasoning-mode effects are task-dependent: thinking improves MathTutorBench but degrades OpenLearnLM and sharply degrades in-domain leak control, across both training-free and RL paradigms](task-dependent-reasoning-mode-effect-tutoring.md) — related
