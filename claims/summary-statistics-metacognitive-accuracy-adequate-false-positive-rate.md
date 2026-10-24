---
type: claim
title: "Summary-statistic measures of metacognitive accuracy (gamma, type 2 ROC, meta-d′, meta-da) maintain a false positive rate consistent with the nominal 5% alpha level in group comparisons"
description: "Summary-statistic measures of metacognitive accuracy (gamma, type 2 ROC, meta-d′, meta-da) maintain a false positive rate consistent with the nominal 5% alpha level in group comparisons"
id: summary-statistics-metacognitive-accuracy-adequate-false-positive-rate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-18
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
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

# Summary-statistic measures of metacognitive accuracy (gamma, type 2 ROC, meta-d′, meta-da) maintain a false positive rate consistent with the nominal 5% alpha level in group comparisons

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In hierarchical-resampling simulations, gamma correlations, type 2 ROC curves, meta-d′, and meta-da showed empirical false positive rates statistically consistent with 5% for two-group comparisons. [→ Manuel Rausch 2023](#manuel-rausch-2023)

## Evidence

### Manuel Rausch 2023

Manuel Rausch, Michael Zehetleitner. (2023). Evaluating false positive rates of standard and hierarchical measures of metacognitive accuracy. Metacognition and Learning. https://doi.org/10.1007/s11409-023-09353-y

`q2 · i?` · `causal · r2`

Simulation study using hierarchical bootstrapping from the confidence database to create 5000 simulated experiments; Bayes factors compared each measure's empirical false positive rate to the nominal 5% level, finding "moderate evidence that the empirical false positive rate is identical to 5%" for these summary-statistic measures.

> "There was moderate evidence that the empirical false positive rate is identical to 5% for gamma correlations, type 2 ROC curves, meta-d′, and meta-d a."

## Discussion


## Related Claims
- Logistic mixed-model regression of confidence on accuracy shows dramatically inflated false positive rates when random slopes are omitted, but an adequate rate when random slopes are included — related
- Distributions of meta-d′/d′ and meta-da/da deviate substantially from normality, motivating log transformation before parametric testing — related
- [T-testing raw meta-d′/d′ or meta-da/da yields a false positive rate below 5%; log transformation or the Mann–Whitney U-test restores an adequate rate](meta-d-ratio-ttest-low-false-positive-rate.md) — related
- [HMeta-d's false positive rate depends on study design and prior specification: independent group priors inflate it, priors on the group difference fix it, and default priors for continuous predictors yield a rate below 5%](hmeta-d-false-positive-rate-prior-dependent.md) — related
- [Children's metacognitive judgments are not explained by baseline risk preferences or response-time cues](metacognition-not-risk-preference-or-response-time.md) — related
