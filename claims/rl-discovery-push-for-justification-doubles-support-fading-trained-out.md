---
type: claim
title: "RL-trained tutors discover pedagogical moves not named in the reward: push-for-justification more than doubles while support fading is trained out"
description: "RL-trained tutors discover pedagogical moves not named in the reward: push-for-justification more than doubles while support fading is trained out"
id: rl-discovery-push-for-justification-doubles-support-fading-trained-out
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
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

# RL-trained tutors discover pedagogical moves not named in the reward: push-for-justification more than doubles while support fading is trained out

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Under the plain prompt, prompting for justification (Move G) rises from 9.0% to 21.8% and asking for independent work (Move H) falls to 0.0%, a move whose payoff lies beyond the single-problem dialog episode horizon. [→ Jakub Macina 2026](#jakub-macina-2026)

## Evidence

### Jakub Macina 2026

Jakub Macina, Manu Kapur, Mrinmaya Sachan. (2026). The Assistance Dilemma: Learning to Teach via Multi-Turn Reinforcement Learning. [doi:10.48550/arXiv.2610.06446](https://doi.org/10.48550/arXiv.2610.06446)

`q1 · i?` · `causal · r2`

Move-distribution analysis of TutorMoments dialogs (n=100 moments per model cell), classified by an independent Gemini-3.1-Pro judge against a 13-move taxonomy (Section 5.4, Figure 2b). The optimizer converged on justification eliciting out of all non-handover moves.

> "Discovery fingerprint:Prompting for justification (Move G) more than doubles (9.0%→21.8%), and Guiding questions (Move A) rises (23.2%→41.4%)."

## Discussion


## Related Claims
- [EDUARDO-27B is the strongest TutorMoments tutor under a plain prompt, but frontier models overtake it when given the evaluation-aware rubric prompt](eduardo-strongest-plain-prompt-frontier-overtake-with-rubric.md) — related
- [Dialogue-based RL training on mathematics tutoring dialogues generalizes to unseen educational benchmarks while largely preserving factual knowledge](dialogue-rl-out-of-distribution-generalization.md) — a broader claim this one bears on
- [Fine-tuning frontier LLMs on authentic tutoring data improves performance on all six conversational and pedagogical benchmarks, moving values toward human-tutor levels](fine-tuning-authentic-data-improves-pedagogical-benchmarks.md) — related
- [Ped. Think Reward achieves the best tutoring performance among trained models, and Thinking Reward is most effective when combined with pedagogical prompting](thinking-reward-needs-pedagogical-prompting.md) — related
- [EDUARDO-27B attains the highest MathTutorBench pedagogical reward-model score and win rate over human teachers on MathDial among all tested tutors, including frontier models, with fewer thinking tokens](eduardo-27b-highest-mathtutorbench-pedagogy-win-rate.md) — related
