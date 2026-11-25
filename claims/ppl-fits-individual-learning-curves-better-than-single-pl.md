---
type: claim
title: A piecewise power law model explains individual learning curves significantly better than a single power law
description: A piecewise power law model explains individual learning curves significantly better than a single power law
id: ppl-fits-individual-learning-curves-better-than-single-pl
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: strong
newest_evidence: 2015
recheck_by: 2018
sources:
  - id: donner-2015
    resource: "https://doi.org/10.3758/s13423-015-0811-x"
    title: "Donner, Y., & Hardy, J. L. (2015). Piecewise power laws in individual learning curves. Psychonomic Bulletin & Review. https://doi.org/10.3758/s13423-015-0811-x"
    author: "Donner, Y., & Hardy, J. L."
    q: 3
    i: "?"
    kind: associational
    rigour: 2
  - id: donner-2015-2
    resource: "https://doi.org/10.3758/s13423-015-0811-x"
    title: "Donner, Y., & Hardy, J. L. (2015). Piecewise power laws in individual learning curves. Psychonomic Bulletin & Review. https://doi.org/10.3758/s13423-015-0811-x"
    author: "Donner, Y., & Hardy, J. L."
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# A piecewise power law model explains individual learning curves significantly better than a single power law

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q3`
> **Currency** · newest study 2015 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2018**: tool and model accuracy changes quickly

## Subclaims
`q3 i?` After accounting for model complexity, PPL fits were superior to single-PL fits for all four tasks, with a highly significant likelihood-ratio test overall. [→ Donner 2015](#donner-2015)
`q3 i?` PPL explained 90.74% of noise-subtracted variance overall, versus 86% for a single power law and 33.9% for an autoregressive model. [→ Donner 2015 (2)](#donner-2015-2)

## Evidence

### Donner 2015

Donner, Y., & Hardy, J. L. (2015). Piecewise power laws in individual learning curves. Psychonomic Bulletin & Review. https://doi.org/10.3758/s13423-015-0811-x

`q3 · i?` · `associational · r2`

Likelihood-ratio tests comparing PPL to single-PL fits across 25,280 individual learning curves from four Lumosity cognitive tasks, after Bonferroni correction. The article reports "χ2(94205) = 534,030 overall" with all ps < 10−7000, supporting PPL superiority for every task.

> "After accounting for the numbers of estimated parameters (see the Method), the PPL fits were superior for all tasks [likelihood-ratio test: χ2(1785) = 13,222, χ2(8520) = 61,616, χ2(9020) = 61,975, and χ2(74880) = 367,681, respectively for the four tasks, and χ2(94205) = 534,030 overall; ps< 10−7000 for all tests after Bonferroni correction"

### Donner 2015 (2)

Donner, Y., & Hardy, J. L. (2015). Piecewise power laws in individual learning curves. Psychonomic Bulletin & Review. https://doi.org/10.3758/s13423-015-0811-x

`q3 · i?` · `associational · r2`

Noise-subtracted variance explained by three models across all tasks: PPL explained "90.74 % of the variance in the data", single PL explained 86%, and an autoregressive model explained 33.9%, showing PPL captures substantially more individual-curve structure.

> "After correcting for different DFs and subtracting the estimated measurement noise (see the Method), PPL explained 90.74 % of the variance in the data, PL1 explained 86 %, and an autoregressive (AR) model in which each score predicted the next only explained 33.9 %."

## Discussion


## Related Claims
- [The rate of transitions between power-law pieces is negatively associated with age after controlling for overall performance](age-negatively-associated-with-transitions.md) — related
- [Transitions between power-law pieces are typically followed by a brief performance drop and then a level surpassing the previous piece](transition-dynamics-drop-then-surpass.md) — related
- [The exponential functional form of the BKT Markov chain calls into question the popular practice of fitting that model form to student data](bkt-hmm-exponential-form-questions-fitting-practice.md) — related
- [Acquisition of a novel paper-and-pencil matrix task follows a power function of practice at group and individual levels](power-law-learning-in-paper-pencil-matrix-task.md) — reports the opposite
