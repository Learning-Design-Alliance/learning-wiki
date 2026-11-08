---
type: claim
title: Dropping standardized test scores from admissions raises or lowers simulated degree completion depending on whether the test is valid
description: Dropping standardized test scores from admissions raises or lowers simulated degree completion depending on whether the test is valid
id: dropping-test-scores-changes-simulated-degree-completion
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: mixed
newest_evidence: 2022
recheck_by: 2025
sources:
  - id: huber-david-e-2022
    resource: "https://doi.org/10.1371/journal.pone.0265459"
    title: "Huber David E., Cohen Andrew L., Staub Adrian. (2022). Compensatory selection with standardized tests. PLoS ONE 17(5): e0265459. https://doi.org/10.1371/journal.pone.0265459"
    author: Huber David E., Cohen Andrew L., Staub Adrian
    q: 2
    i: "?"
    kind: theoretical
    rigour: 2
  - id: huber-david-e-2022-2
    resource: "https://doi.org/10.1371/journal.pone.0265459"
    title: "Huber David E., Cohen Andrew L., Staub Adrian. (2022). Compensatory selection with standardized tests. PLoS ONE 17(5): e0265459. https://doi.org/10.1371/journal.pone.0265459"
    author: Huber David E., Cohen Andrew L., Staub Adrian
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
  - id: huber-david-e-2022-3
    resource: "https://doi.org/10.1371/journal.pone.0265459"
    title: "Huber David E., Cohen Andrew L., Staub Adrian. (2022). Compensatory selection with standardized tests. PLoS ONE 17(5): e0265459. https://doi.org/10.1371/journal.pone.0265459"
    author: Huber David E., Cohen Andrew L., Staub Adrian
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Dropping standardized test scores from admissions raises or lowers simulated degree completion depending on whether the test is valid

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · theoretical `r2`–`r3` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2025**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When the valid test is uncorrelated with other predictors, ignoring it drops average degree completion from 60% to 55.1%. [→ Huber David E. 2022](#huber-david-e-2022)
`q2 i?` When the valid test is correlated with other predictors, dropping it drops completion rates from 62.8% to 60.8%. [→ Huber David E. 2022 (2)](#huber-david-e-2022-2)
`q2 i?` When the test is invalid, dropping it from admissions increases the probability of degree completion to 55.1%. [→ Huber David E. 2022 (3)](#huber-david-e-2022-3)

## Evidence

### Huber David E. 2022

Huber David E., Cohen Andrew L., Staub Adrian. (2022). Compensatory selection with standardized tests. PLoS ONE 17(5): e0265459. https://doi.org/10.1371/journal.pone.0265459

`q2 · i?` · `theoretical · r2`

Simulation ground truth #2 (valid, uncorrelated test): "when Test scores are ignored in the admissions process, the average degree completion rate drops from 60% to 55.1%", because committees lose information about one latent characteristic.

> "when Test scores are ignored in the admissions process, the average degree completion rate drops from 60% to 55.1%."

### Huber David E. 2022 (2)

Huber David E., Cohen Andrew L., Staub Adrian. (2022). Compensatory selection with standardized tests. PLoS ONE 17(5): e0265459. https://doi.org/10.1371/journal.pone.0265459

`q2 · i?` · `theoretical · r3`

Simulation ground truth #4 (valid test correlated with other predictors): "when Test scores were dropped from the admissions process (right graph), the simulation revealed that completion rates dropped from 62.8% to 60.8%".

> "when Test scores were dropped from the admissions process (right graph), the simulation revealed that completion rates dropped from 62.8% to 60.8%"

### Huber David E. 2022 (3)

Huber David E., Cohen Andrew L., Staub Adrian. (2022). Compensatory selection with standardized tests. PLoS ONE 17(5): e0265459. https://doi.org/10.1371/journal.pone.0265459

`q2 · i?` · `theoretical · r3`

Simulation ground truth #1 (invalid test): because the Test is non-diagnostic and merely adds random noise, "the effect of dropping it from the admissions process is to increase probability of degree completion to 55.1%".

> "the effect of dropping it from the admissions process is to increase probability of degree completion to 55.1%."

## Discussion


## Related Claims
- [Compensatory Selection Eliminates Valid Test Correlation](compensatory-selection-eliminates-valid-test-correlation.md)
- [An invalid standardized test used in compensatory selective admissions produces a spurious negative correlation with subsequent success, at any level of selectivity](invalid-test-spurious-negative-correlation-selective-admissions.md) — related
- [High school GPA is the strongest predictor of college admission, persistence, and graduation, more than ACT or SAT scores](hs-gpa-strongest-college-predictor.md) — related
