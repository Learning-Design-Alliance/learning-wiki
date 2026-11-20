---
type: claim
title: Machine coding shows a systematic offset dependent on the measured prevalence EC, which can be calibrated with a best-fit function S(EC)
description: Machine coding shows a systematic offset dependent on the measured prevalence EC, which can be calibrated with a best-fit function S(EC)
id: systematic-offset-function-of-ec-calibration
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: rebeckah-k-fussell-2024
    resource: "https://doi.org/10.1103/physrevphyseducres.20.010113"
    title: "Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)"
    author: Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: rebeckah-k-fussell-2024-2
    resource: "https://doi.org/10.1103/physrevphyseducres.20.010113"
    title: "Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)"
    author: Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Machine coding shows a systematic offset dependent on the measured prevalence EC, which can be calibrated with a best-fit function S(EC)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the CR code, the model overestimates prevalence when EC < 0.5 and underestimates when EC > 0.5; for the L code the boundary is shifted to about 0.3. [→ Rebeckah K. Fussell 2024](#rebeckah-k-fussell-2024)
`q2 i?` The systematic function S(EC) is unique to the trained model, differing between models trained on different balanced training sets. [→ Rebeckah K. Fussell 2024 (2)](#rebeckah-k-fussell-2024-2)

## Evidence

### Rebeckah K. Fussell 2024

Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)

`q2 · i?` · `causal · r2`

Numerical analysis with eleven test banks (Nbank = 200, code proportion 0 to 1 in steps of 0.1), 100 sample test sets of n = 100 each, for CR and L codes with ptrain = 0.5. The article reports 95% of data fall within two standard deviations of σEC from Eqn. 3.

> "For the CR code (Fig. 4a), the systematic is such that the model overestimates the prevalence of the code when EC < 0.5 and underestimates the prevalence of the code when EC > 0.5."

### Rebeckah K. Fussell 2024 (2)

Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)

`q2 · i?` · `design · r2`

Supplemental analysis constructing new trained models for CR and L with a different balanced training set: best-fit lines S(EC) keep the same downward linear shape but have different parameters, and differences between models can exceed the statistical uncertainty at extremes.

> "The estimates for the systematic, there- fore, depends on the training set used (i.e., is unique to the trained model)."

## Discussion


## Related Claims
- [Statistical uncertainty of machine-coded code frequencies follows a Bernoulli-based estimate that conservatively over-predicts variability](bernoulli-statistical-uncertainty-machine-coding.md) — related
- [Systematic offsets are larger when machine coding data from a population different from the training population](population-shift-increases-machine-coding-systematics.md) — related
- [Prognostic errors are direction-dependent: survival is overestimated for patients surviving under 9 months and underestimated for those surviving longer](overestimation-under-9-months-underestimation-beyond.md) — related
- [Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models](learner-models-miscalibrated-outside-data-interval.md) — related
- [In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range](llm-essay-scoring-systematic-underestimation.md) — related
- [Bounded data (scale limits) naturally lead to overestimation by lower performers and underestimation by higher performers, a statistical constraint on interpreting the Dunning-Kruger effect](bounded-data-scale-limits-over-underestimation.md) — related
- [Machine coding systematically over- or under-estimates code prevalence when the training set is outcome-unbalanced, with no offset at ptrain = 0.5](training-imbalance-causes-systematic-machine-coding-offset.md) — related
