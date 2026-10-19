---
type: claim
title: "HMeta-d's false positive rate depends on study design and prior specification: independent group priors inflate it, priors on the group difference fix it, and default priors for continuous predictors yield a rate below 5%"
description: "HMeta-d's false positive rate depends on study design and prior specification: independent group priors inflate it, priors on the group difference fix it, and default priors for continuous predictors yield a rate belo..."
id: hmeta-d-false-positive-rate-prior-dependent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-18
evidence_strength: moderate
sources:
  - id: manuel-rausch-2023
    resource: "https://doi.org/10.1007/s11409-023-09353-y"
    title: "Manuel Rausch, Michael Zehetleitner. (2023). Evaluating false positive rates of standard and hierarchical measures of metacognitive accuracy. Metacognition and Learning. https://doi.org/10.1007/s11409-023-09353-y"
    author: Manuel Rausch, Michael Zehetleitner
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: manuel-rausch-2023-2
    resource: "https://doi.org/10.1007/s11409-023-09353-y"
    title: "Manuel Rausch, Michael Zehetleitner. (2023). Evaluating false positive rates of standard and hierarchical measures of metacognitive accuracy. Metacognition and Learning. https://doi.org/10.1007/s11409-023-09353-y"
    author: Manuel Rausch, Michael Zehetleitner
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# HMeta-d's false positive rate depends on study design and prior specification: independent group priors inflate it, priors on the group difference fix it, and default priors for continuous predictors yield a rate below 5%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` For group designs, HMeta-d's false positive rate exceeds 5% with independent priors on both groups but is adequate when a prior is placed on the between-group difference. [→ Manuel Rausch 2023](#manuel-rausch-2023)
`q2 i?` For continuous predictor variables, HMeta-d with default priors yields a false positive rate below 5%, while close-to-flat priors give a rate not distinguishable from 5%. [→ Manuel Rausch 2023 (2)](#manuel-rausch-2023-2)

## Evidence

### Manuel Rausch 2023

Manuel Rausch, Michael Zehetleitner. (2023). Evaluating false positive rates of standard and hierarchical measures of metacognitive accuracy. Metacognition and Learning. https://doi.org/10.1007/s11409-023-09353-y

`q2 · i?` · `causal · r2`

Simulation of two-group comparisons via hierarchical resampling from the confidence database; HMeta-d was run with independent group priors versus priors on the group difference, with false positives defined as 95% credible intervals excluding zero.

> "There was extremely strong evidence that the false positive rate is larger than 5% for HMeta-d when independent priors were placed on both groups. However, when a prior was placed on the difference between groups in terms of meta-d′/d′, there was a moderate amount of evidence that the false positive rate is 5%."

### Manuel Rausch 2023 (2)

Manuel Rausch, Michael Zehetleitner. (2023). Evaluating false positive rates of standard and hierarchical measures of metacognitive accuracy. Metacognition and Learning. https://doi.org/10.1007/s11409-023-09353-y

`q2 · i?` · `design · r2`

Simulations with a randomly sampled continuous between-subject predictor tested HMeta-d under three hyperprior sets (standard, close-to-flat, narrow); default priors produced a below-5% rate, and stronger priors produced an even smaller rate.

> "We also found strong evidence that HMeta-d using default priors is associated with a false positive rate below 5%."

## Discussion


## Related Claims
- [Logistic mixed-model regression of confidence on accuracy shows dramatically inflated false positive rates when random slopes are omitted, but an adequate rate when random slopes are included](logistic-mixed-model-fixed-slopes-inflated-false-positives.md) — related
- [T-testing raw meta-d′/d′ or meta-da/da yields a false positive rate below 5%; log transformation or the Mann–Whitney U-test restores an adequate rate](meta-d-ratio-ttest-low-false-positive-rate.md) — related
- [Summary-statistic measures of metacognitive accuracy (gamma, type 2 ROC, meta-d′, meta-da) maintain a false positive rate consistent with the nominal 5% alpha level in group comparisons](summary-statistics-metacognitive-accuracy-adequate-false-positive-rate.md) — related
