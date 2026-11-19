---
type: claim
title: In the Monte Carlo simulation, statistical quality of the uncertainty measures increases along with mathematical complexity
description: In the Monte Carlo simulation, statistical quality of the uncertainty measures increases along with mathematical complexity
id: uncertainty-quality-increases-with-complexity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: kok-2022
    resource: "https://doi.org/10.51724/ijpce.v14i1.214"
    title: "Kok, K., & Priemer, B. (2022). Comparing Different Uncertainty Measures to Quantify Measurement Uncertainties in High School Science Experiments. International Journal of Physics and Chemistry Education, 14(1), 1-9. https://doi.org/10.51724/ijpce.v14i1.214"
    author: "Kok, K., & Priemer, B."
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# In the Monte Carlo simulation, statistical quality of the uncertainty measures increases along with mathematical complexity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across the five uncertainty measures, deviation bias, convergence, and spread improve as mathematical complexity increases, with the exception of the standard deviation's spread. [→ Kok 2022](#kok-2022)

## Evidence

### Kok 2022

Kok, K., & Priemer, B. (2022). Comparing Different Uncertainty Measures to Quantify Measurement Uncertainties in High School Science Experiments. International Journal of Physics and Chemistry Education, 14(1), 1-9. https://doi.org/10.51724/ijpce.v14i1.214

`q2 · i?` · `theoretical · r3`

Monte Carlo simulation (Python 2.7.15) comparing five uncertainty measures from subsamples of a 1,000-value normally distributed set across subsample sizes N = [4; 20], with 10,000 repetitions. The classification table shows "the quality in terms of deviation bias, convergence, and spread ... appears to increase along with the complexity", with spreads of .52, .35, .26, .19, and .24 for min-max, exclude extremes, middle 50%, MAD, and standard deviation respectively.

> "Simultaneously the quality in terms of deviation bias, convergence, and spread (with the exception of the standard deviation) appears to increase along with the complexity."

## Discussion


## Related Claims
- [Middle school mathematics curricula in the USA, Germany, and the Netherlands introduce the operations underlying simpler spread measures years before the standard deviation](curricula-sequence-math-operations-before-standard-deviation.md) — related
- [The disregarded measures (68% of measurements, 76% of measurements, and IQR) yield results of similar quality to the middle 50% but at greater complexity, making them less useful](disregarded-measures-no-better-than-middle50.md) — reports the opposite
- [The exclude extremes measure crosses zero uncertainty deviation between subsample sizes N = 8 and N = 9, indicating near-perfect average agreement with the reference standard deviation](exclude-extremes-crosses-zero-deviation.md) — a narrower finding that bears on this claim
- [The MAD converges to a mean uncertainty deviation of approximately −.23 and has the smallest spread of all uncertainty measures](mad-converges-negative-point-23.md) — a narrower finding that bears on this claim
- [The middle 50% measure shows sharp kinks at subsample sizes that are multiples of four and converges towards the MAD for higher N](middle50-kinks-converges-mad.md) — a narrower finding that bears on this claim
- [The min-max uncertainty measure is highly susceptible to outliers and its deviation grows quickly for larger subsample sizes](minmax-uncertainty-outlier-susceptible.md) — a narrower finding that bears on this claim
