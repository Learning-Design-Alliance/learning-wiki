---
type: claim
title: "Reasoning-mode effects are task-dependent: thinking improves MathTutorBench but degrades OpenLearnLM and sharply degrades in-domain leak control, across both training-free and RL paradigms"
description: "Reasoning-mode effects are task-dependent: thinking improves MathTutorBench but degrades OpenLearnLM and sharply degrades in-domain leak control, across both training-free and RL paradigms"
id: task-dependent-reasoning-mode-effect-tutoring
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: unggi-lee-2026
    resource: "https://doi.org/10.48550/arXiv.2605.27088"
    title: "Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon. (2026). LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring. arXiv preprint. [doi:10.48550/arXiv.2605.27088](https://doi.org/10.48550/arXiv.2605.27088)"
    author: Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Reasoning-mode effects are task-dependent: thinking improves MathTutorBench but degrades OpenLearnLM and sharply degrades in-domain leak control, across both training-free and RL paradigms

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Thinking improves MathTutorBench (+0.87) but hurts OpenLearnLM (−0.44), and in-domain leak control degrades sharply under thinking; the effect appears in both training-free and RL-based paradigms. [→ Unggi Lee 2026](#unggi-lee-2026)

## Evidence

### Unggi Lee 2026

Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon. (2026). LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring. arXiv preprint. [doi:10.48550/arXiv.2605.27088](https://doi.org/10.48550/arXiv.2605.27088)

`q2 · i?` · `causal · r1`

Results section (§3.2, Figure 3): comparison of NoThink vs. Think conditions across the 12 methods shows 1−Leak drops from 0.55 to 0.43 in-domain, while OOD effects split by benchmark. The article attributes the effect to "a fundamental property of reasoning-enabled models".

> "Figure 3leftshows that in-domain leak control degrades sharply under thinking. This task-dependent reasoning mode effect is consistent across both training-free and RL paradigms"

## Discussion


## Related Claims
- [In-domain reward maximization is essentially uncorrelated with out-of-distribution tutoring performance across methods](indomain-reward-uncorrelated-with-ood-tutoring.md) — related
- [Prompt style is the largest driver of disability-aware Fit gains, and the Thinking Reward becomes effective only in combination with adaptive prompting](thinking-reward-effective-only-with-adaptive-prompting.md) — related
- [Ped. Think Reward achieves the best tutoring performance among trained models, and Thinking Reward is most effective when combined with pedagogical prompting](thinking-reward-needs-pedagogical-prompting.md) — related
- [Explicit thinking mechanisms degrade rubric-aligned conversation scoring but improve recommendation acceptability](thinking-degrades-scoring-improves-recommendations.md) — related
- [Training-free tutors rely on teaching-knowledge patterns at 2–3× the rate of RL-trained models with a ~10 percentage-point deficit in intent-level scaffolding](training-free-mkt-piu-redistribution.md) — related
- [EDUARDO-27B attains the highest MathTutorBench pedagogical reward-model score and win rate over human teachers on MathDial among all tested tutors, including frontier models, with fewer thinking tokens](eduardo-27b-highest-mathtutorbench-pedagogy-win-rate.md) — related
- [LLM tutors can improve learning, but gains depend conditionally on pedagogical structure, engagement, comparison, and measurement horizon](conditional-yes-llm-tutors-improve-learning.md) — related
