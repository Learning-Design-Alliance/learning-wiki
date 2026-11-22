---
type: claim
title: EDUARDO-27B is the strongest TutorMoments tutor under a plain prompt, but frontier models overtake it when given the evaluation-aware rubric prompt
description: EDUARDO-27B is the strongest TutorMoments tutor under a plain prompt, but frontier models overtake it when given the evaluation-aware rubric prompt
id: eduardo-strongest-plain-prompt-frontier-overtake-with-rubric
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: mixed
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jakub-macina-2026
    resource: "https://doi.org/10.48550/arXiv.2610.06446"
    title: "Jakub Macina, Manu Kapur, Mrinmaya Sachan. (2026). The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning. [doi:10.48550/arXiv.2610.06446](https://doi.org/10.48550/arXiv.2610.06446)"
    author: Jakub Macina, Manu Kapur, Mrinmaya Sachan
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# EDUARDO-27B is the strongest TutorMoments tutor under a plain prompt, but frontier models overtake it when given the evaluation-aware rubric prompt

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Under the plain prompt Eduardo-27B scores highest on Scaffolding (0.96) and Avoids-Over-help (0.76) and is second on rigour (0.44 vs. 0.48 for Claude Opus 4.8); given the rubric, frontier models overtake it on rigour and Avoids-Over-help. [→ Jakub Macina 2026](#jakub-macina-2026)

## Evidence

### Jakub Macina 2026

Jakub Macina, Manu Kapur, Mrinmaya Sachan. (2026). The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning. [doi:10.48550/arXiv.2610.06446](https://doi.org/10.48550/arXiv.2610.06446)

`q1 · i?` · `causal · r2`

Simulated dialog replays on TutorMoments (n=100) with an independent Gemini-3.7-Flash student and Gemini-3.1-Pro judge, reported in Table 3 and Section 5.3. Judge scores are in [0,1]; Eduardo uses 2.4–6.2× fewer thinking tokens than baselines.

> "Under the plain prompt, EDUARDO-27B is the strongest tutor: it has the highest Scaffolding (0.96) and Avoids-Over-help (0.76) and is second on rigour (0.44 vs. 0.48 for Claude Opus 4.8), while its base is the weakest."

## Discussion


## Related Claims
- [EDUARDO-27B attains the highest MathTutorBench pedagogical reward-model score and win rate over human teachers on MathDial among all tested tutors, including frontier models, with fewer thinking tokens](eduardo-27b-highest-mathtutorbench-pedagogy-win-rate.md) — related
- [RL-trained tutors discover pedagogical moves not named in the reward: push-for-justification more than doubles while support fading is trained out](rl-discovery-push-for-justification-doubles-support-fading-trained-out.md) — related
- [Leakage is held, not reduced, for the Qwen3.5/3.8 family, and reduced substantially only for Qwen3-14B](leakage-held-not-reduced-qwen-family-eduardo.md) — related
- [Ped. Think Reward achieves the best tutoring performance among trained models, and Thinking Reward is most effective when combined with pedagogical prompting](thinking-reward-needs-pedagogical-prompting.md) — related
