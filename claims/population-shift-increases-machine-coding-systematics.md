---
type: claim
title: Systematic offsets are larger when machine coding data from a population different from the training population
description: Systematic offsets are larger when machine coding data from a population different from the training population
id: population-shift-increases-machine-coding-systematics
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

# Systematic offsets are larger when machine coding data from a population different from the training population

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Systematics tend to be farther from zero for pre-survey responses (a different population than the training set) than for same-population mixed pre/post responses. [→ Rebeckah K. Fussell 2024](#rebeckah-k-fussell-2024)

## Evidence

### Rebeckah K. Fussell 2024

Rebeckah K. Fussell, Emily M. Stump, and N. G. Holmes. (2024). A method to assess the trustworthiness of machine coding at scale. Originally published 2023. [doi:10.1103/physrevphyseducres.20.010113](https://doi.org/10.1103/physrevphyseducres.20.010113)

`q2 · i?` · `design · r2`

Numerical comparison for the CR code using a training set of 500 responses (80% post-survey, 20% pre-survey, balanced). Fits: S(EC) = −0.329*EC + 0.175 for Set Pre/Post and S(EC) = −0.494*EC + 0.273 for Set Pre; statistical variability was the same for both sets.

> "the systematic tends to be farther from zero when machine coding samples from the Set Pre, a different population than the training set, compared to when machine coding samples from the Set Post/Pre, the same population as the training set."

## Discussion


## Related Claims
- [Statistical uncertainty of machine-coded code frequencies follows a Bernoulli-based estimate that conservatively over-predicts variability](bernoulli-statistical-uncertainty-machine-coding.md) — related
- [AI-based analyses of student learning may perform unevenly across student populations, limiting comparability of findings across settings](ai-uneven-performance-across-student-populations.md) — a broader claim this one bears on
- [Machine coding systematically over- or under-estimates code prevalence when the training set is outcome-unbalanced, with no offset at ptrain = 0.5](training-imbalance-causes-systematic-machine-coding-offset.md) — related
- [Machine coding shows a systematic offset dependent on the measured prevalence EC, which can be calibrated with a best-fit function S(EC)](systematic-offset-function-of-ec-calibration.md) — related
