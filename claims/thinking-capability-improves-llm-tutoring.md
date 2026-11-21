---
type: claim
title: "Enabling internal thinking dramatically improves LLM tutor performance in simulated mathematics tutoring (+134% Delta Solve Rate, +306% Helpful Rate)"
description: "Enabling internal thinking dramatically improves LLM tutor performance in simulated mathematics tutoring (+134% Delta Solve Rate, +306% Helpful Rate)"
id: thinking-capability-improves-llm-tutoring
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
---

# Enabling internal thinking dramatically improves LLM tutor performance in simulated mathematics tutoring (+134% Delta Solve Rate, +306% Helpful Rate)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Compared to a non-thinking baseline, enabling thinking improved Delta Solve Rate from 0.120 to 0.281 and Helpful Rate from 0.180 to 0.730 in simulated tutoring dialogues. [→ Unggi Lee 2026](#unggi-lee-2026)

## Evidence

### Unggi Lee 2026

Unggi Lee, Jiyeong Bae, Jaehyeon Park, Haeun Park, Taejun Park, Younghoon Jeon, Sungmin Cho, Junbo Koh, Yeil Jeong, Gyeonggeon Lee. (2026). Rewarding How Models Think Pedagogically: Integrating Pedagogical Reasoning and Thinking Rewards for LLMs in Education. arXiv. [doi:10.48550/arXiv.2601.14560](https://doi.org/10.48550/arXiv.2601.14560)

`q2 · i?` · `causal · r1`

RL training experiment on the BigMath tutoring task with a Llama-3.1-8B-Instruct student simulator, comparing the Qwen2.5-7B NoThink baseline to the Qwen3-8B thinking condition. The article reports "+134% improvement in Delta Solve Rate (0.120→0.281)" and +306% Helpful Rate; no standardized effect size is printed.

> "First, enabling thinking dramatically improves performance: comparing No- Think to Think NoReward, we observe a +134% improve- ment in Delta Solve Rate (0.120→0.281) and a +306% im- provement in Helpful Rate (0.180→0.730)."

## Discussion


## Related Claims
- [Pedagogical prompting increases mathematical problem-solving content and reduces excessive praise in tutor responses](pedagogical-prompting-shifts-tutor-behavior.md) — related
- [Ped. Think Reward achieves the best tutoring performance among trained models, and Thinking Reward is most effective when combined with pedagogical prompting](thinking-reward-needs-pedagogical-prompting.md) — related
- [GRPO pedagogical alignment of a reasoning LLM lowers actual student learning while raising judge-rated helpfulness (a multi-dimensional alignment tax)](grpo-pedagogical-alignment-tax-lowers-learning.md) — related
- [On the same frozen base, TEI@4 beats both DTR@4 and Greedy on Δ Solve Rate, leak rate, and composite R_total at no training cost](tei4-beats-dtr4-and-greedy-same-base.md) — related
- [DTR (Deep-Thinking Ratio) does not predict tutoring quality despite predicting math accuracy](dtr-does-not-predict-tutoring-quality.md) — related
- [The positive correlation between tutor Praise rate and total reward is concentrated in NoThink dialogs and localized to closing turns, with null or negative effects under Think variants](praise-reward-correlation-nothink-late-turns.md) — related
