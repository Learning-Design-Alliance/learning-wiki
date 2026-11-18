---
type: claim
title: Latent mastery propensity ηT correlates positively with post-test scores in both treatment and control groups, with a slightly lower slope in the treatment group
description: Latent mastery propensity ηT correlates positively with post-test scores in both treatment and control groups, with a slightly lower slope in the treatment group
id: eta-positive-with-posttest-both-groups
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2017
sources:
  - id: adam-c-sales-2017
    resource: "https://doi.org/10.48550/arXiv.1707.09308"
    title: "Adam C. Sales, and John F Pane. (2017). The Role of Mastery Learning in an Intelligent Tutoring System: Principal Stratification on a Latent Variable. [doi:10.48550/arXiv.1707.09308](https://doi.org/10.48550/arXiv.1707.09308)"
    author: Adam C. Sales, and John F Pane
    q: 2
    i: "?"
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

# Latent mastery propensity ηT correlates positively with post-test scores in both treatment and control groups, with a slightly lower slope in the treatment group

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Students more likely to master worked sections tend to score higher on the post-test in both treatment groups. [→ Adam C. Sales 2017](#adam-c-sales-2017)
`q2 i?` The slope between post-test scores and ηT is slightly lower in the treatment group than in the control group, so the treatment effect decreases as ηT increases. [→ Adam C. Sales 2017 (2)](#adam-c-sales-2017-2)

## Evidence

### Adam C. Sales 2017

Adam C. Sales, and John F Pane. (2017). The Role of Mastery Learning in an Intelligent Tutoring System: Principal Stratification on a Latent Variable. [doi:10.48550/arXiv.1707.09308](https://doi.org/10.48550/arXiv.1707.09308)

`q2 · i?` · `causal · r2`

Figure 6 plots observed post-test scores against a posterior draw of ηT from model (4.1)–(6.3) for both groups. The article reports "a positive relationship betweenηT andY in both treatment groups"; no standardized effect size is printed.

> "There is a positive relationship betweenηT andY in both treatment groups—students who are more likely to master worked sections tend to score higher on the post-test."

### Adam C. Sales 2017 (2)

Adam C. Sales, and John F Pane. (2017). The Role of Mastery Learning in an Intelligent Tutoring System: Principal Stratification on a Latent Variable. [doi:10.48550/arXiv.1707.09308](https://doi.org/10.48550/arXiv.1707.09308)

`q2 · i?` · `causal · r2`

Same posterior-draw analysis shown in Figure 6. The article reports the treatment-group slope is "slightly lower in the treatment group than in the control group", implying decreasing treatment effects with increasing ηT. The authors state this is unlikely to result from ceiling effects, since only one student answered all posttest items correctly.

> "However, the slope between Y andηT is slightly lower in the treatment group than in the control group. So as ηT increases, the distance between YT andYC—the treatment eﬀect—decreases."

## Discussion


## Related Claims
- [In the CTA1 effectiveness trial, the estimated treatment effect decreases with students' latent propensity to master worked sections, though it remains positive across the observed range](cta1-effect-decreases-with-mastery-propensity.md) — related
- [The observed mastery proportion m̄ confounds mastery propensity with section difficulty (Spearman r = -0.30), whereas the IRT latent variable ηT does not (r = 0.07)](mbar-confounded-eta-not.md) — related
- [Students with higher pretest scores, who are white or Asian, male, or gifted are more likely to master worked CTA1 sections; covariates explain about 39% of variance in mastery propensity](covariates-predict-cta1-mastery-propensity.md) — related
