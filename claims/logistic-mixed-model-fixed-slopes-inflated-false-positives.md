---
type: claim
title: Logistic mixed-model regression of confidence on accuracy shows dramatically inflated false positive rates when random slopes are omitted, but an adequate rate when random slopes are included
description: Logistic mixed-model regression of confidence on accuracy shows dramatically inflated false positive rates when random slopes are omitted, but an adequate rate when random slopes are included
id: logistic-mixed-model-fixed-slopes-inflated-false-positives
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
    kind: design
    rigour: 2
---

# Logistic mixed-model regression of confidence on accuracy shows dramatically inflated false positive rates when random slopes are omitted, but an adequate rate when random slopes are included

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Omitting random slopes from logistic mixed-model regression of metacognitive accuracy inflates the false positive rate above 5%; including random slopes restores an adequate rate. [→ Manuel Rausch 2023](#manuel-rausch-2023)

## Evidence

### Manuel Rausch 2023

Manuel Rausch, Michael Zehetleitner. (2023). Evaluating false positive rates of standard and hierarchical measures of metacognitive accuracy. Metacognition and Learning. https://doi.org/10.1007/s11409-023-09353-y

`q2 · i?` · `design · r2`

Hierarchical-resampling simulations from 46 confidence-database datasets tested two logistic mixed-model specifications (Sandberg et al., 2010 fixed slopes; Wierzchoń et al., 2019 random slopes) against the 5% nominal alpha level using Bayes factors.

> "There was extremely strong evidence that the false positive rate of logistic mixed model regression with a random effect on intercepts is larger than 5%, but there was also moderate evidence that the false positive rate is 5% when logistic mixed model regression included random slopes."

## Discussion


## Related Claims

- [HMeta-d's false positive rate depends on study design and prior specification: independent group priors inflate it, priors on the group difference fix it, and default priors for continuous predictors yield a rate below 5%](hmeta-d-false-positive-rate-prior-dependent.md) — related
- [Summary-statistic measures of metacognitive accuracy (gamma, type 2 ROC, meta-d′, meta-da) maintain a false positive rate consistent with the nominal 5% alpha level in group comparisons](summary-statistics-metacognitive-accuracy-adequate-false-positive-rate.md) — related
- [T-testing raw meta-d′/d′ or meta-da/da yields a false positive rate below 5%; log transformation or the Mann–Whitney U-test restores an adequate rate](meta-d-ratio-ttest-low-false-positive-rate.md) — related
- [Regularization-based graphical modeling has key drawbacks, including difficulty obtaining valid parameter uncertainty and inflated false positive rates](regularization-drawbacks-uncertainty-false-positives.md)
