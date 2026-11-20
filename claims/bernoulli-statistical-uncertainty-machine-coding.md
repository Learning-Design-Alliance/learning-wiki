---
type: claim
title: Statistical uncertainty of machine-coded code frequencies follows a Bernoulli-based estimate that conservatively over-predicts variability
description: Statistical uncertainty of machine-coded code frequencies follows a Bernoulli-based estimate that conservatively over-predicts variability
id: bernoulli-statistical-uncertainty-machine-coding
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2024
sources:
  - id: rebeckah-k-fussell-2024
    resource: "https://doi.org/10.1103/physrevphyseducres.20.010113"
    title: "Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)"
    author: Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Statistical uncertainty of machine-coded code frequencies follows a Bernoulli-based estimate that conservatively over-predicts variability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Empirical standard deviations of the machine estimate follow the predicted 1/√n relationship with sample size and the predicted parabolic relationship with EC, with Eqn. 3 over-predicting variability. [→ Rebeckah K. Fussell 2024](#rebeckah-k-fussell-2024)

## Evidence

### Rebeckah K. Fussell 2024

Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)

`q2 · i?` · `design · r2`

Numerical test of Eqn. 3 for the CR code: 30 values of n between 10 and 200, each with 1000 sample test sets drawn from a test bank with code proportion 0.5. The article reports Eqn. 3 "over-predicts, rather than under-predicts, the standard deviation", giving a conservative estimate; a parallel test over EC shows the same pattern (Fig. 3b).

> "We find that the empirical values of σEC approximately follow the predicted 1/√n relationship (see Fig. 3a), though the empirical values are consistently less than the values predicted by Eqn. 3."

## Discussion


## Related Claims
- [The model's posterior confidence estimates are conservative: over 95% of predictions the model claims 90–95% confidence in are correct](peer-grading-confidence-estimates-conservative.md) — related
- [Machine coding shows a systematic offset dependent on the measured prevalence EC, which can be calibrated with a best-fit function S(EC)](systematic-offset-function-of-ec-calibration.md) — related
- [Systematic offsets are larger when machine coding data from a population different from the training population](population-shift-increases-machine-coding-systematics.md) — related
- [Machine coding systematically over- or under-estimates code prevalence when the training set is outcome-unbalanced, with no offset at ptrain = 0.5](training-imbalance-causes-systematic-machine-coding-offset.md) — related
