---
type: claim
title: Learning-loss estimates are robust to placebo tests, propensity-score and maximum-entropy reweighting, and school and family fixed effects
description: Learning-loss estimates are robust to placebo tests, propensity-score and maximum-entropy reweighting, and school and family fixed effects
id: learning-loss-robust-to-reweighting-and-fixed-effects
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-15
evidence_strength: moderate
sources:
  - id: engzell-p-2021
    resource: "https://doi.org/10.1073/pnas.2022376118"
    title: "Engzell P., Frey A., Verhagen M. D. (2021). Learning loss due to school closures during the COVID-19 pandemic. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2022376118"
    author: Engzell P., Frey A., Verhagen M. D.
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Learning-loss estimates are robust to placebo tests, propensity-score and maximum-entropy reweighting, and school and family fixed effects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`

## Subclaims
`q3 i?` Placebo analyses assigning treatment to each comparison year yield confidence intervals spanning zero, and estimates remain in line with the baseline when balancing on propensity of treatment, using maximum-entropy weights, restricting to high-response schools, and adding school or family fixed effects. [→ Engzell P. 2021](#engzell-p-2021)

## Evidence

### Engzell P. 2021

Engzell P., Frey A., Verhagen M. D. (2021). Learning loss due to school closures during the COVID-19 pandemic. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2022376118

`q3 · i?` · `causal · r2`

Series of robustness specifications reported in Fig. 4 addressing loss to follow-up: regression adjustment, propensity-score and maximum-entropy reweighting, restricting to schools where at least 75% of students took tests after lockdown, and school and family fixed effects. The article reports that it balances groups "using maximum-entropy weights and the estimated propensity of treatment"; no effect sizes are printed for these checks.

> "we balance treatment and control groups on a wider set of covariates, including at the school level, using maximum-entropy weights and the estimated propensity of treatment"

## Discussion


## Related Claims
- [Most of the lockdown learning loss reflects reduced knowledge learned rather than transitory day-of-test influences](learning-loss-reflects-knowledge-learned-not-transitory.md) — related
- [The learning-loss estimates are robust to restricting the sample to constant schools, adding school fixed effects, and coarsened exact matching](covid-closures-losses-robust-to-robustness-checks.md) — related
- [Propensity score matching produced baseline-equivalent treatment and comparison groups on all measured variables](psm-baseline-equivalence-mtss-study.md) — related
- [Using baseline data strongly predictive of outcome measures considerably reduces bias in nonexperimental estimates of charter school achievement effects](predictive-baseline-data-reduce-nonexperimental-bias.md) — a broader claim this one bears on
- [Nonexperimental methods incorporating pre-treatment outcome measures can replicate experimental ITT impact estimates when control-group crossover occurs](nonexperimental-pre-treatment-methods-replicate-itt-under-crossover.md) — a broader claim this one bears on
- [Propensity score stratification using multilevel models reduces selection bias from confounding variables and improves accuracy of charter school effect estimations](propensity-stratification-multilevel-reduces-selection-bias.md) — a broader claim this one bears on
