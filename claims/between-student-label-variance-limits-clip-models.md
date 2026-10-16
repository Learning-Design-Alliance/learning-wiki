---
type: claim
title: Between-student differences explain a large fraction of CASED label variance, limiting what any clip-level visual model can learn
description: Between-student differences explain a large fraction of CASED label variance, limiting what any clip-level visual model can learn
id: between-student-label-variance-limits-clip-models
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: student-1
    title: student-1
    q: 2
    i: "?"
    kind: associational
    rigour: 1
  - id: skew-1
    title: skew-1
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Between-student differences explain a large fraction of CASED label variance, limiting what any clip-level visual model can learn

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 associational `r1`, 1 design `r2` · `q2`

## Subclaims
`q2 i?` Individual students differ substantially in mean engagement labels — some labeled engaged in over 90% of clips, others below 40% — so a large fraction of label variance reflects between-student differences rather than within-clip behavior. [→ student-1](#student-1)
`q2 i?` The binary label distribution is highly skewed (about 69% engaged, 31% not-engaged), so a majority-class classifier achieves approximately 40–45% macro F1 without learning discriminative features. [→ skew-1](#skew-1)

## Evidence

### student-1

Alperen Kantarcı, Visvanathan Ramesh, and Gemma Roig. 2026. Mind the Student: Behavioral and Contextual Cues for Automated Engagement Prediction in Online Learning. ICMI '26, Napoli, Italy. https://doi.org/10.1145/3776574.3832485

`q2 · i?` · `associational · r1`

Dataset analysis of the CASED corpus (Section 2.1), examining per-student engagement rates. The authors draw the implication for clip-level visual models directly from this between-student variance.

> "Several students are labeled engaged in over 90% of their clips while others fall below 40%. This hints that a large fraction of the label variance is explained by between-student differences rather than within-clip behavioral dynamics, which directly limits what any clip-level visual model can learn."

### skew-1

Alperen Kantarcı, Visvanathan Ramesh, and Gemma Roig. 2026. Mind the Student: Behavioral and Contextual Cues for Automated Engagement Prediction in Online Learning. ICMI '26, Napoli, Italy. https://doi.org/10.1145/3776574.3832485

`q2 · i?` · `design · r2`

Dataset analysis of CASED label distributions (Section 2.1): approximately 69% of clips labeled engaged and 31% not-engaged, with continuous scores compressed (mean 3.7, median 4.0).

> "A majority-class classifier therefore achieves approximately 40–45% macro F1 without learning any discriminative features."

## Discussion


## Related Claims
- [The Bayesian context layer applies stronger posterior personalization to students with fewer training clips, correlating clip count with KL divergence from the prior (r=-0.748, p=0.001)](bayesian-context-kl-clip-count-correlation.md) — related
- [Classroom-level ICCs for elementary test score gains range from 0.02 to 0.15 and school-level ICCs from 0.05 to 0.20, so classroom effects explain about 15 percent of gain-score variance](icc-classroom-effects-gain-scores-15-percent.md) — related
