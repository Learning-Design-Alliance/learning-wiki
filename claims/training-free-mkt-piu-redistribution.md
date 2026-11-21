---
type: claim
title: Training-free tutors rely on teaching-knowledge patterns at 2–3× the rate of RL-trained models with a ~10 percentage-point deficit in intent-level scaffolding
description: Training-free tutors rely on teaching-knowledge patterns at 2–3× the rate of RL-trained models with a ~10 percentage-point deficit in intent-level scaffolding
id: training-free-mkt-piu-redistribution
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
    kind: design
    rigour: 2
---

# Training-free tutors rely on teaching-knowledge patterns at 2–3× the rate of RL-trained models with a ~10 percentage-point deficit in intent-level scaffolding

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` At the category level, training-free methods show 2–3× elevation of Mathematical Knowledge for Teaching (19–23% vs. RL 7–8%) and a ~10pp deficit in Pedagogical Intent Utterance (46–55% vs. RL 60–65%). [→ Unggi Lee 2026](#unggi-lee-2026)

## Evidence

### Unggi Lee 2026

Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon. (2026). LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring. arXiv preprint. [doi:10.48550/arXiv.2605.27088](https://doi.org/10.48550/arXiv.2605.27088)

`q2 · i?` · `design · r2`

Behavioral comparison (§4.2): 415,775 tutor sentences across 60 method-condition configurations labeled with GPT-4o-mini using an 82-code educational codebook. The article reports training-free methods redistribute behavior "toward content delivery rather than explicit scaffolding".

> "this manifests as a 2-3 × elevation of Mathemat-ical Knowledge for Teaching (training-free 19-23% vs. RL 7-8%) and a ∼10pp deficit in Pedagogical Intent Utterance (training-free 46-55% vs. RL 60-65%)"

## Discussion


## Related Claims
- [Dialogue-based RL training on mathematics tutoring dialogues generalizes to unseen educational benchmarks while largely preserving factual knowledge](dialogue-rl-out-of-distribution-generalization.md) — related
- [GRPO alignment collapses Mathematical-Knowledge-for-Teaching utterances and surges Socratic-style Exploratory questions in tutor output](alignment-shifts-mkt-collapse-exploratory-surge.md) — related
- [An analytical chapter identifies reward hacking, engagement optimization over learning, and scaffolding dependency as risks of RL policies with poorly specified rewards](rl-reward-misalignment-failure-modes.md) — related
- [Reasoning-mode effects are task-dependent: thinking improves MathTutorBench but degrades OpenLearnLM and sharply degrades in-domain leak control, across both training-free and RL paradigms](task-dependent-reasoning-mode-effect-tutoring.md) — related
