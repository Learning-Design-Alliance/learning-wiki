---
type: claim
title: Optimized-sequence gains over baselines are larger for a 200-word training pool than a 1000-word pool, though overall test accuracy is lower with the smaller pool
description: Optimized-sequence gains over baselines are larger for a 200-word training pool than a 1000-word pool, though overall test accuracy is lower with the smaller pool
id: sequence-optimization-gains-larger-small-pool
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

# Optimized-sequence gains over baselines are larger for a 200-word training pool than a 1000-word pool, though overall test accuracy is lower with the smaller pool

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The improvement of optimized time-varying distributions over baselines was higher for K = 200 than K = 1000, while overall test accuracy with K = 200 was significantly lower than with K = 1000. [→ Ayon Sen 2020](#ayon-sen-2020)

## Evidence

### Ayon Sen 2020

Ayon Sen, Christopher R. Cox, Matthew Cooper Borkenhagen, Mark S. Seidenberg, Xiaojin Zhu. (2020). Learning to Read through Machine Teaching. Preprint. Under review. [doi:10.48550/arXiv.2006.16470](https://doi.org/10.48550/arXiv.2006.16470)

`q2 · i?` · `causal · r2`

Simulation results across four conditions (child/adult vocabularies crossed with K = 200 and K = 1000 training pools), shown in Figure 3. The article attributes the lower K = 200 accuracy to more irregular words entering the K = 1000 pool, leaving the generalization set. No effect size is printed.

> "The gains are higher for K = 200 thanK = 1000. It should also be noted that the overall test accuracy values found using K = 200 are signiﬁcantly lower than that ofK = 1000."

## Discussion


## Related Claims
- [Training sequences sampled from an optimized time-varying word distribution yield significantly higher generalization accuracy than frequency-based and uniform baselines in a connectionist reading model](optimized-word-sequence-beats-frequency-baselines-reading-ann.md) — a broader claim this one bears on
- [Curriculum strategies in AI training often yield faster convergence and better generalization, but difficulty in ML reflects optimization rather than learner readiness](curriculum-learning-sequencing-gains-and-limits.md) — a broader claim this one bears on
