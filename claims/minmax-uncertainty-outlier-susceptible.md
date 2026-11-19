---
type: claim
title: The min-max uncertainty measure is highly susceptible to outliers and its deviation grows quickly for larger subsample sizes
description: The min-max uncertainty measure is highly susceptible to outliers and its deviation grows quickly for larger subsample sizes
id: minmax-uncertainty-outlier-susceptible
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

# The min-max uncertainty measure is highly susceptible to outliers and its deviation grows quickly for larger subsample sizes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the simulation, the min-max uncertainty blows up quickly for larger N and shows the highest spread (.52), because it uses the largest distance to the mean over the complete subsample. [→ Kok 2022](#kok-2022)

## Evidence

### Kok 2022

Kok, K., & Priemer, B. (2022). Comparing Different Uncertainty Measures to Quantify Measurement Uncertainties in High School Science Experiments. International Journal of Physics and Chemistry Education, 14(1), 1-9. https://doi.org/10.51724/ijpce.v14i1.214

`q2 · i?` · `theoretical · r3`

Monte Carlo simulation results (Figure 3) plotting mean uncertainty deviations as a function of subsample size N. The article reports the min-max measure "is highly susceptible to outliers, which also explains its high standard deviation", and Table 1 lists its spread as .52 with a biased deviation.

> "As expected, the min-max uncertainty blows up quickly for larger values of 𝑁. Because we take the uncertainty to be the largest distance to the mean using the complete subsample, this measure is highly susceptible to outliers, which also explains its high standard deviation."

## Discussion


## Related Claims
- [The exclude extremes measure crosses zero uncertainty deviation between subsample sizes N = 8 and N = 9, indicating near-perfect average agreement with the reference standard deviation](exclude-extremes-crosses-zero-deviation.md) — related
- [The middle 50% measure shows sharp kinks at subsample sizes that are multiples of four and converges towards the MAD for higher N](middle50-kinks-converges-mad.md) — related
- [In the Monte Carlo simulation, statistical quality of the uncertainty measures increases along with mathematical complexity](uncertainty-quality-increases-with-complexity.md) — a broader claim this one bears on
- [The MAD converges to a mean uncertainty deviation of approximately −.23 and has the smallest spread of all uncertainty measures](mad-converges-negative-point-23.md) — related
