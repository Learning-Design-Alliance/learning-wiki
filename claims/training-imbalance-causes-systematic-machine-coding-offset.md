---
type: claim
title: Machine coding systematically over- or under-estimates code prevalence when the training set is outcome-unbalanced, with no offset at ptrain = 0.5
description: Machine coding systematically over- or under-estimates code prevalence when the training set is outcome-unbalanced, with no offset at ptrain = 0.5
id: training-imbalance-causes-systematic-machine-coding-offset
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
    kind: design
    rigour: 2
---

# Machine coding systematically over- or under-estimates code prevalence when the training set is outcome-unbalanced, with no offset at ptrain = 0.5

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The difference between machine and human estimates of code prevalence deviates from zero as training-set balance deviates from 0.5, with overestimation when ptrain > 0.5 and underestimation when ptrain < 0.5. [→ Rebeckah K. Fussell 2024](#rebeckah-k-fussell-2024)

## Evidence

### Rebeckah K. Fussell 2024

Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)

`q2 · i?` · `design · r2`

Numerical experiment training nine logistic-regression models for the CR code with ptrain from 0.1 to 0.9, each with 600 responses, tested on 100 samples of n = 100 from test banks with code proportion 0.5. The article reports "the machine coding overestimates the prevalence of the code in the test set (i.e., EC > EH) when ptrain > 0.5" and underestimates when ptrain < 0.5, with no offset at ptrain = 0.5.

> "We observe that the magnitude of the difference between EC and EH deviates from zero as ptrain deviates from 0.5"

## Discussion


## Related Claims
- [Systematic offsets are larger when machine coding data from a population different from the training population](population-shift-increases-machine-coding-systematics.md) — related
- [Machine coding shows a systematic offset dependent on the measured prevalence EC, which can be calibrated with a best-fit function S(EC)](systematic-offset-function-of-ec-calibration.md) — related
- [In one study of five LLMs scoring 60 undergraduate essays on IELTS rubric dimensions, systematic underestimation of human scores was the dominant bias trend, with some models also compressing scores into a narrow range](llm-essay-scoring-systematic-underestimation.md) — related
- [Statistical uncertainty of machine-coded code frequencies follows a Bernoulli-based estimate that conservatively over-predicts variability](bernoulli-statistical-uncertainty-machine-coding.md) — related
- [Bounded data (scale limits) naturally lead to overestimation by lower performers and underestimation by higher performers, a statistical constraint on interpreting the Dunning-Kruger effect](bounded-data-scale-limits-over-underestimation.md) — related
