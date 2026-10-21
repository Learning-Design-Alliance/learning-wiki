---
type: claim
title: "T-testing raw meta-d′/d′ or meta-da/da yields a false positive rate below 5%; log transformation or the Mann–Whitney U-test restores an adequate rate"
description: "T-testing raw meta-d′/d′ or meta-da/da yields a false positive rate below 5%; log transformation or the Mann–Whitney U-test restores an adequate rate"
id: meta-d-ratio-ttest-low-false-positive-rate
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
---

# T-testing raw meta-d′/d′ or meta-da/da yields a false positive rate below 5%; log transformation or the Mann–Whitney U-test restores an adequate rate

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Direct t-tests on meta-d′/d′ produce a false positive rate below the nominal 5%, while log-transformed t-tests and Mann–Whitney U-tests produce rates consistent with 5%. [→ Manuel Rausch 2023](#manuel-rausch-2023)

## Evidence

### Manuel Rausch 2023

Manuel Rausch, Michael Zehetleitner. (2023). Evaluating false positive rates of standard and hierarchical measures of metacognitive accuracy. Metacognition and Learning. https://doi.org/10.1007/s11409-023-09353-y

`q2 · i?` · `causal · r2`

Group-comparison simulations from the confidence database resampling; ratio measures meta-d′/d′ and meta-da/da were tested raw, log-transformed, and with the non-parametric U-test, with Bayes factors evaluating deviation from the 5% alpha level.

> "Concerning meta-d′/d′, there was moderate evidence that the empirical false positive rate is below 5% when significance testing was performed using t-tests. There was moderate evidence that the false positive rate is 5% when meta-d′/d′ was log-transformed before"

## Discussion


## Related Claims
- [HMeta-d's false positive rate depends on study design and prior specification: independent group priors inflate it, priors on the group difference fix it, and default priors for continuous predictors yield a rate below 5%](hmeta-d-false-positive-rate-prior-dependent.md) — related
- Logistic mixed-model regression of confidence on accuracy shows dramatically inflated false positive rates when random slopes are omitted, but an adequate rate when random slopes are included — related
- Distributions of meta-d′/d′ and meta-da/da deviate substantially from normality, motivating log transformation before parametric testing — related
- [Summary-statistic measures of metacognitive accuracy (gamma, type 2 ROC, meta-d′, meta-da) maintain a false positive rate consistent with the nominal 5% alpha level in group comparisons](summary-statistics-metacognitive-accuracy-adequate-false-positive-rate.md) — related
