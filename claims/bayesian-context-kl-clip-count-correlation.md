---
type: claim
title: The Bayesian context layer applies stronger posterior personalization to students with fewer training clips, correlating clip count with KL divergence from the prior (r=-0.748, p=0.001)
description: The Bayesian context layer applies stronger posterior personalization to students with fewer training clips, correlating clip count with KL divergence from the prior (r=-0.748, p=0.001)
id: bayesian-context-kl-clip-count-correlation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: kl-1
    title: kl-1
    q: 2
    i: 3
    kind: design
    rigour: 2
---

# The Bayesian context layer applies stronger posterior personalization to students with fewer training clips, correlating clip count with KL divergence from the prior (r=-0.748, p=0.001)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2` · `i3` large

## Subclaims
`q2 i3` Student identities show higher KL divergence from the population prior (mean KL=14.32) than instructors (mean KL=13.12), and student clip count correlates strongly and negatively with KL divergence (r=-0.748, p=0.001). [→ kl-1](#kl-1)

## Evidence

### kl-1

Alperen Kantarcı, Visvanathan Ramesh, and Gemma Roig. 2026. Mind the Student: Behavioral and Contextual Cues for Automated Engagement Prediction in Online Learning. ICMI '26, Napoli, Italy. https://doi.org/10.1145/3776574.3832485

`q2 · i3` · `design · r2`

Posterior analysis of the Bayesian context layer (Table 5) on CASED data, printing the correlation r=-0.748 (p=0.001). The authors interpret this as aggressive individualized posterior shifts for sparse data and convergence to a regularized population norm for data-rich students.

> "statistical analysis reveals a strong, significant negative correlation between a student’s clip count and their KL divergence from the prior (r=-0.748, p=0.001)."

## Discussion


## Related Claims
- [Consensus calibration shows mild under-dispersion relative to the pooled benchmark, strongest for sparsely observed items, consistent with residual prior over-counting](mild-under-dispersion-low-exposure-items.md) — related
- [Consensus calibration closely reproduces pooled-benchmark item-parameter means and standard deviations on an operational assessment](consensus-posterior-agrees-with-pooled-benchmark.md) — related
- [Between-student differences explain a large fraction of CASED label variance, limiting what any clip-level visual model can learn](between-student-label-variance-limits-clip-models.md) — related
