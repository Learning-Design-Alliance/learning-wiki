---
type: claim
title: "The middle 50% measure shows sharp kinks at subsample sizes that are multiples of four and converges towards the MAD for higher N"
description: "The middle 50% measure shows sharp kinks at subsample sizes that are multiples of four and converges towards the MAD for higher N"
id: middle50-kinks-converges-mad
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

# The middle 50% measure shows sharp kinks at subsample sizes that are multiples of four and converges towards the MAD for higher N

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The middle 50% measure is the only non-smooth uncertainty measure, with kinks whenever N is a multiple of four, and it converges towards the MAD for higher values of N. [→ Kok 2022](#kok-2022)

## Evidence

### Kok 2022

Kok, K., & Priemer, B. (2022). Comparing Different Uncertainty Measures to Quantify Measurement Uncertainties in High School Science Experiments. International Journal of Physics and Chemistry Education, 14(1), 1-9. https://doi.org/10.51724/ijpce.v14i1.214

`q2 · i?` · `theoretical · r3`

Monte Carlo simulation results (Figure 3, Table 1). The kinks occur because another pair of minimum-maximum values is excluded at those sizes; Table 1 lists middle 50% with deviation bias −.34, convergent but non-smooth, spread .26.

> "The middle 50% shows sharp kinks whenever 𝑁 is a multiple of four, corresponding to another pair of minimum-maximum-values to be excluded. For higher values of 𝑁, middle 50% converges towards the MAD."

## Discussion


## Related Claims
- [The disregarded measures (68% of measurements, 76% of measurements, and IQR) yield results of similar quality to the middle 50% but at greater complexity, making them less useful](disregarded-measures-no-better-than-middle50.md) — related
- [The exclude extremes measure crosses zero uncertainty deviation between subsample sizes N = 8 and N = 9, indicating near-perfect average agreement with the reference standard deviation](exclude-extremes-crosses-zero-deviation.md) — related
- [The MAD converges to a mean uncertainty deviation of approximately −.23 and has the smallest spread of all uncertainty measures](mad-converges-negative-point-23.md) — related
- [In the Monte Carlo simulation, statistical quality of the uncertainty measures increases along with mathematical complexity](uncertainty-quality-increases-with-complexity.md) — a broader claim this one bears on
- [The min-max uncertainty measure is highly susceptible to outliers and its deviation grows quickly for larger subsample sizes](minmax-uncertainty-outlier-susceptible.md) — related
