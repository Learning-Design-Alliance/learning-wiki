---
type: claim
title: Training sequences sampled from an optimized time-varying word distribution yield significantly higher generalization accuracy than frequency-based and uniform baselines in a connectionist reading model
description: Training sequences sampled from an optimized time-varying word distribution yield significantly higher generalization accuracy than frequency-based and uniform baselines in a connectionist reading model
id: optimized-word-sequence-beats-frequency-baselines-reading-ann
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
sources:
  - id: ayon-sen-2020
    resource: "https://doi.org/10.48550/arXiv.2006.16470"
    title: "Ayon Sen, Christopher R. Cox, Matthew Cooper Borkenhagen, Mark S. Seidenberg, Xiaojin Zhu. (2020). Learning to Read through Machine Teaching. Preprint. Under review. [doi:10.48550/arXiv.2006.16470](https://doi.org/10.48550/arXiv.2006.16470)"
    author: Ayon Sen, Christopher R. Cox, Matthew Cooper Borkenhagen, Mark S. Seidenberg, Xiaojin Zhu
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Training sequences sampled from an optimized time-varying word distribution yield significantly higher generalization accuracy than frequency-based and uniform baselines in a connectionist reading model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In simulation, the average test accuracy of sequences drawn from the optimal time-varying distribution (P*,Q*) was statistically better than that of the static optimized distribution and all frequency/uniform baselines (p < 0.001, student's t-test), and the optimal sequence drawn from (P*,Q*) was always the best. [→ Ayon Sen 2020](#ayon-sen-2020)

## Evidence

### Ayon Sen 2020

Ayon Sen, Christopher R. Cox, Matthew Cooper Borkenhagen, Mark S. Seidenberg, Xiaojin Zhu. (2020). Learning to Read through Machine Teaching. Preprint. Under review. [doi:10.48550/arXiv.2006.16470](https://doi.org/10.48550/arXiv.2006.16470)

`q2 · i?` · `causal · r2`

Simulation study comparing optimized time-varying distributions against baselines (CHILDES child-directed speech, child text frequency, AOA, COCA adult text frequency, SUBTLEXus, uniform sampling) over 1000 sampled sequences per condition. The article reports the optimized distributions were "significantly better than the baselines" with p <0.001; no effect size is printed.

> "But in all cases the average test accuracy for (P∗,Q∗) is statistically better than that of ¯P∗ and the other baselines (p <0.001 for student’s t-test)."

## Discussion


## Related Claims
- [Optimized-sequence gains over baselines are larger for a 200-word training pool than a 1000-word pool, though overall test accuracy is lower with the smaller pool](sequence-optimization-gains-larger-small-pool.md) — a narrower finding that bears on this claim
- [The PPO-driven policy substantially outperformed a random policy baseline, with cumulative reward of 95.12 ± 1.23 versus 12.3 ± 4.7](ppo-outperforms-random-baseline-reward.md) — related
- [Curriculum strategies in AI training often yield faster convergence and better generalization, but difficulty in ML reflects optimization rather than learner readiness](curriculum-learning-sequencing-gains-and-limits.md) — a broader claim this one bears on
- [Moodle's built-in randomization is insufficient for Statistics courses, while moodlequizR provides far greater randomization](moodlequizr-randomization-exceeds-moodle-builtin.md) — related
- [An adaptive curriculum targeting the policy's measured weaknesses raises evaluation income by 18% over uniform sampling, 10% over a static curriculum, and 14% over random targeting at 100 updates](adaptive-curriculum-improves-shift-income.md) — related
