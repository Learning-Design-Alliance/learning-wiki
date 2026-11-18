---
type: claim
title: The observed mastery proportion m̄ confounds mastery propensity with section difficulty (Spearman r = -0.30), whereas the IRT latent variable ηT does not (r = 0.07)
description: The observed mastery proportion m̄ confounds mastery propensity with section difficulty (Spearman r = -0.30), whereas the IRT latent variable ηT does not (r = 0.07)
id: mbar-confounded-eta-not
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: mixed
newest_evidence: 2017
recheck_by: 2020
sources:
  - id: adam-c-sales-2017
    resource: "https://doi.org/10.48550/arXiv.1707.09308"
    title: "Adam C. Sales, and John F Pane. (2017). The Role of Mastery Learning in an Intelligent Tutoring System: Principal Stratification on a Latent Variable. [doi:10.48550/arXiv.1707.09308](https://doi.org/10.48550/arXiv.1707.09308)"
    author: Adam C. Sales, and John F Pane
    q: 2
    i: 2
    kind: causal
    rigour: 2
  - id: adam-c-sales-2017-2
    resource: "https://doi.org/10.48550/arXiv.1707.09308"
    title: "Adam C. Sales, and John F Pane. (2017). The Role of Mastery Learning in an Intelligent Tutoring System: Principal Stratification on a Latent Variable. [doi:10.48550/arXiv.1707.09308](https://doi.org/10.48550/arXiv.1707.09308)"
    author: Adam C. Sales, and John F Pane
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# The observed mastery proportion m̄ confounds mastery propensity with section difficulty (Spearman r = -0.30), whereas the IRT latent variable ηT does not (r = 0.07)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2` · `i2` medium
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2020**: tool and model accuracy changes quickly
> **Design limits** · Adam C. Sales 2017: no comparison group (read from the study by two models, 2026-11-18)

## Subclaims
`q2 i2` The Spearman correlation between m̄T and average section difficulty is -0.30, so m̄ is only partially a measure of students' ability to master worked sections. [→ Adam C. Sales 2017](#adam-c-sales-2017)
`q2 i0` The posterior mean Spearman correlation between ηT and average section difficulty is positive 0.07, so variance in ηT is not driven by section difficulty. [→ Adam C. Sales 2017 (2)](#adam-c-sales-2017-2)

## Evidence

### Adam C. Sales 2017

Adam C. Sales, and John F Pane. (2017). The Role of Mastery Learning in an Intelligent Tutoring System: Principal Stratification on a Latent Variable. [doi:10.48550/arXiv.1707.09308](https://doi.org/10.48550/arXiv.1707.09308)

`q2 · i2` · `causal · r2`

Figure 3a plots treated students' observed m̄ against average estimated Rasch section difficulty from the CTA1 log data. The printed "Spearman correlation between ¯mT and average section diﬃculty is -0.30" (r = .30, a medium-small correlation), so m̄ also measures which sections students worked.

> "the Spearman correlation between ¯mT and average section diﬃculty is -0.30. Therefore, ¯m is only partially a measure of students’ ability to master worked sections—it also measures which sections they worked."

### Adam C. Sales 2017 (2)

Adam C. Sales, and John F Pane. (2017). The Role of Mastery Learning in an Intelligent Tutoring System: Principal Stratification on a Latent Variable. [doi:10.48550/arXiv.1707.09308](https://doi.org/10.48550/arXiv.1707.09308)

`q2 · i?` · `causal · r2`

Figure 3b plots posterior draws of ηT against average section difficulty. The printed correlation is "positive 0.07", below r = .10, so the difficulty confound present in m̄ is not present in ηT. The article attributes this correlation to more capable students choosing harder sections.

> "In fact, the posterior mean Spearman correlation between ηT and average section diﬃculty is positive 0.07, probably reﬂecting the fact that more capable students are both more likely to master worked sections and more likely to work on hard sections."

## Discussion


## Related Claims
- [In the CTA1 effectiveness trial, the estimated treatment effect decreases with students' latent propensity to master worked sections, though it remains positive across the observed range](cta1-effect-decreases-with-mastery-propensity.md) — related
- [Latent mastery propensity ηT correlates positively with post-test scores in both treatment and control groups, with a slightly lower slope in the treatment group](eta-positive-with-posttest-both-groups.md) — related
- [Students with higher pretest scores, who are white or Asian, male, or gifted are more likely to master worked CTA1 sections; covariates explain about 39% of variance in mastery propensity](covariates-predict-cta1-mastery-propensity.md) — related
