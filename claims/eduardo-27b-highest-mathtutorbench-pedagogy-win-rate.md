---
type: claim
title: EDUARDO-27B attains the highest MathTutorBench pedagogical reward-model score and win rate over human teachers on MathDial among all tested tutors, including frontier models, with fewer thinking tokens
description: EDUARDO-27B attains the highest MathTutorBench pedagogical reward-model score and win rate over human teachers on MathDial among all tested tutors, including frontier models, with fewer thinking tokens
id: eduardo-27b-highest-mathtutorbench-pedagogy-win-rate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jakub-macina-2026
    resource: "https://doi.org/10.48550/arXiv.2610.06446"
    title: "Jakub Macina, Manu Kapur, Mrinmaya Sachan. (2026). The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning. [doi:10.48550/arXiv.2610.06446](https://doi.org/10.48550/arXiv.2610.06446)"
    author: Jakub Macina, Manu Kapur, Mrinmaya Sachan
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# EDUARDO-27B attains the highest MathTutorBench pedagogical reward-model score and win rate over human teachers on MathDial among all tested tutors, including frontier models, with fewer thinking tokens

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` EDUARDO improves Ped-RM and win rate at 4B, 9B and 27B on MathDial, and Eduardo-27B reaches the highest Ped-RM (9.04) and win rate (89.2%) of any tested tutor while thinking less than its base (501→289 tokens per turn). [→ Jakub Macina 2026](#jakub-macina-2026)

## Evidence

### Jakub Macina 2026

Jakub Macina, Manu Kapur, Mrinmaya Sachan. (2026). The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning. [doi:10.48550/arXiv.2610.06446](https://doi.org/10.48550/arXiv.2610.06446)

`q1 · i?` · `design · r2`

Zero-shot out-of-domain evaluation on MathDial (n=500 middle-turn completions) reported in Table 1 and Section 5.1. The model scores are reward-model and win-rate metrics with no printed effect size. Thinking tokens fell from 501 to 289 per turn at 27B.

> "EDUARDO improves Ped-RM and win rate at 4B (2.08→7.92;30%→78%), 9B (3.02→8.29;38%→82%) and 27B (8.34→9.04;82%→89%), and Eduardo-27B attains the highest Ped-RM and win rate of any tutor, including the frontier models."

## Discussion


## Related Claims
- [EDUARDO-27B is the strongest TutorMoments tutor under a plain prompt, but frontier models overtake it when given the evaluation-aware rubric prompt](eduardo-strongest-plain-prompt-frontier-overtake-with-rubric.md) — related
- [Ped. Think Reward achieves the best tutoring performance among trained models, and Thinking Reward is most effective when combined with pedagogical prompting](thinking-reward-needs-pedagogical-prompting.md) — related
- [The binary reward gates govern whether the tutor tells while the masked near-transfer post-test shapes how it teaches](gates-decide-whether-tutor-tells-transfer-shapes-how.md) — related
- [RL-trained tutors discover pedagogical moves not named in the reward: push-for-justification more than doubles while support fading is trained out](rl-discovery-push-for-justification-doubles-support-fading-trained-out.md) — related
- [SHERPA training transfers to the external MathTutorBench benchmark, raising the pedagogy average from 52.5% to 79.2% and beating PedagogicalRL on all four response-generation metrics](sherpa-transfers-mathtutorbench-pedagogy.md) — related
- [Leakage is held, not reduced, for the Qwen3.5/3.8 family, and reduced substantially only for Qwen3-14B](leakage-held-not-reduced-qwen-family-eduardo.md) — related
- [Reasoning-mode effects are task-dependent: thinking improves MathTutorBench but degrades OpenLearnLM and sharply degrades in-domain leak control, across both training-free and RL paradigms](task-dependent-reasoning-mode-effect-tutoring.md) — related
- [LLM tutors can improve learning, but gains depend conditionally on pedagogical structure, engagement, comparison, and measurement horizon](conditional-yes-llm-tutors-improve-learning.md) — related
