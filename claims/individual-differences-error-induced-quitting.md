---
type: claim
title: Students differ substantially in their tendency to quit following sequential errors
description: Students differ substantially in their tendency to quit following sequential errors
id: individual-differences-error-induced-quitting
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: johansson-2024
    resource: "https://github.com/ann1ejohansson/three-strikes"
    title: "Johansson, A. M., Savi, A. O., van der Maas, H. L. J., & Hofman, A. D. (2024). Three Strikes and Who is Out? Individual Differences in Error-Induced Quitting. https://github.com/ann1ejohansson/three-strikes"
    author: "Johansson, A. M., Savi, A. O., van der Maas, H. L. J., & Hofman, A. D."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: johansson-2024-2
    resource: "https://github.com/ann1ejohansson/three-strikes"
    title: "Johansson, A. M., Savi, A. O., van der Maas, H. L. J., & Hofman, A. D. (2024). Three Strikes and Who is Out? Individual Differences in Error-Induced Quitting. https://github.com/ann1ejohansson/three-strikes"
    author: "Johansson, A. M., Savi, A. O., van der Maas, H. L. J., & Hofman, A. D."
    q: 2
    i: 1
    kind: associational
    rigour: 2
---

# Students differ substantially in their tendency to quit following sequential errors

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2` · `i1` small
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A mixed-effects logistic regression with a random slope for sequential errors shows large between-user variability in the effect of errors on quitting. [→ Johansson 2024](#johansson-2024)
`q2 i1` Each sequential error multiplies the risk of quitting by about 2.25 (OR), with higher quitting risk for lower-ability users and lower grades. [→ Johansson 2024 (2)](#johansson-2024-2)

## Evidence

### Johansson 2024

Johansson, A. M., Savi, A. O., van der Maas, H. L. J., & Hofman, A. D. (2024). Three Strikes and Who is Out? Individual Differences in Error-Induced Quitting. https://github.com/ann1ejohansson/three-strikes

`q2 · i?` · `associational · r2`

Mixed-effects logistic regression on addition-game data from 3,998 users (≥50 sessions, ≥10 quits) drawn from over 25 million responses by 255,568 unique users. Adding a random slope for sequential errors improved fit; variance estimate for the slope was 0.14 (σ = 0.37).

> "intra-class correlations (ICC) demonstrated that this model accounted for about 68% of between-subject variance in baseline quitting rates, and 56% of between-subject variance in the effect of sequential errors on quitting."

### Johansson 2024 (2)

Johansson, A. M., Savi, A. O., van der Maas, H. L. J., & Hofman, A. D. (2024). Three Strikes and Who is Out? Individual Differences in Error-Induced Quitting. https://github.com/ann1ejohansson/three-strikes

`q2 · i1` · `associational · r2`

Fixed effects from the best-fitting mixed-effects model (random intercept, random slope, covariates ability and grade) on the 3,998-user training sample. User ability (β = −0.10; SE = 0.01; p < .001; OR = 0.90) and grade (β = −0.05; SE = 0.004; p < .001; OR = 0.95) were also significant.

> "There was a significant fixed effect of sequential errors (β = 0.81; SE = 0.001; p < .001) on quitting. This is equivalent to an odds ratio (OR) of about 2.25, meaning that for every sequential error committed, the risk of quitting increases by about 2.25."

## Discussion


## Related Claims
- [Error-induced quitting effects in the addition game can be used to tailor error interventions in the subtraction game](cross-domain-tailoring-of-error-interventions.md) — related
- [Individual differences in error-induced quitting are stable across the addition and subtraction domains](error-induced-quitting-stable-across-domains.md) — related
- [The effect of sequential errors on quitting is moderated by difficulty level, response time, school hours, and grade](moderators-of-error-induced-quitting.md) — related
- [Sequential errors predict transitions into both soft-quit and hard-quit states in an online learning environment](sequential-errors-predict-quitting-ole.md) — related
- [Post-error quitting decreases with playing experience, suggesting an experience-related build-up of tolerance to errors](post-error-quitting-decreases-with-experience.md) — related
- [Case analysis of individual game events reveals anomalies — high-pretest players quitting and low-pretest players succeeding — that may add noise to regression models](game-event-case-anomalies-noise-in-models.md) — related
