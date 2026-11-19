---
type: claim
title: The MAD converges to a mean uncertainty deviation of approximately −.23 and has the smallest spread of all uncertainty measures
description: The MAD converges to a mean uncertainty deviation of approximately −.23 and has the smallest spread of all uncertainty measures
id: mad-converges-negative-point-23
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
  - id: kok-2022-2
    resource: "https://doi.org/10.51724/ijpce.v14i1.214"
    title: "Kok, K., & Priemer, B. (2022). Comparing Different Uncertainty Measures to Quantify Measurement Uncertainties in High School Science Experiments. International Journal of Physics and Chemistry Education, 14(1), 1-9. https://doi.org/10.51724/ijpce.v14i1.214"
    author: "Kok, K., & Priemer, B."
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# The MAD converges to a mean uncertainty deviation of approximately −.23 and has the smallest spread of all uncertainty measures

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · theoretical `r3` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the simulation, the MAD is systematically lower than the standard deviation, converges quickly to a mean deviation of approximately −.23, and its spread (.19) is even lower than the standard deviation's (.24). [→ Kok 2022](#kok-2022)
`q2 i?` The MAD's low spread is attributed to the linearity of its terms compared with the squared terms in the standard deviation. [→ Kok 2022 (2)](#kok-2022-2)

## Evidence

### Kok 2022

Kok, K., & Priemer, B. (2022). Comparing Different Uncertainty Measures to Quantify Measurement Uncertainties in High School Science Experiments. International Journal of Physics and Chemistry Education, 14(1), 1-9. https://doi.org/10.51724/ijpce.v14i1.214

`q2 · i?` · `theoretical · r3`

Monte Carlo simulation results (Figure 3, Table 1). The MAD is "systematically lower than the standard deviation" because it takes absolute deviations rather than the root of the sum of squares; Table 1 lists its spread as .19 versus .24 for the standard deviation.

> "The mean uncertainty deviation also quickly converges to a mean deviation of approximately −.23, and the uncertainty decreases with increasing values of 𝑁."

### Kok 2022 (2)

Kok, K., & Priemer, B. (2022). Comparing Different Uncertainty Measures to Quantify Measurement Uncertainties in High School Science Experiments. International Journal of Physics and Chemistry Education, 14(1), 1-9. https://doi.org/10.51724/ijpce.v14i1.214

`q2 · i?` · `theoretical · r3`

Same simulation, Table 1 discussion. The article attributes the MAD's spread of .19 being lower than the standard deviation's .24 to "the linearity of the terms in the calculation".

> "With a remarkable behavior for the MAD, which has a spread even lower than the standard deviation. This is due to the linearity of the terms in the calculation as compared to the standard deviation which uses squared terms."

## Discussion


## Related Claims
- [Middle school mathematics curricula in the USA, Germany, and the Netherlands introduce the operations underlying simpler spread measures years before the standard deviation](curricula-sequence-math-operations-before-standard-deviation.md) — related
- [In the Monte Carlo simulation, statistical quality of the uncertainty measures increases along with mathematical complexity](uncertainty-quality-increases-with-complexity.md) — a broader claim this one bears on
- [The middle 50% measure shows sharp kinks at subsample sizes that are multiples of four and converges towards the MAD for higher N](middle50-kinks-converges-mad.md) — related
- [The min-max uncertainty measure is highly susceptible to outliers and its deviation grows quickly for larger subsample sizes](minmax-uncertainty-outlier-susceptible.md) — related
