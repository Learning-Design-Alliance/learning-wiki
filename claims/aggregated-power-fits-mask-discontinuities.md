---
type: claim
title: Simulations show power functions fit aggregated means and standard deviations almost perfectly even when all underlying individual learning curves are discontinuous
description: Simulations show power functions fit aggregated means and standard deviations almost perfectly even when all underlying individual learning curves are discontinuous
id: aggregated-power-fits-mask-discontinuities
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-25
evidence_strength: moderate
newest_evidence: 2002
sources:
  - id: haider-and-frensch-2002
    resource: "https://doi.org/10.1037/0278-7393.28.2.392"
    title: "Hilde Haider & Peter A. Frensch. (2002). Why Aggregated Learning Follows the Power Law of Practice When Individual Learning Does Not: Comment on Rickard (1997, 1999), Delaney et al. (1998), and Palmeri (1999). Journal of Experimental Psychology: Learning, Memory, and Cognition. https://doi.org/10.1037/0278-7393.28.2.392"
    author: "Hilde Haider & Peter A. Frensch"
    q: 1
    i: "?"
    kind: causal
    rigour: 2
  - id: haider-and-frensch-2002-2
    resource: "https://doi.org/10.1037/0278-7393.28.2.392"
    title: "Hilde Haider & Peter A. Frensch. (2002). Why Aggregated Learning Follows the Power Law of Practice When Individual Learning Does Not: Comment on Rickard (1997, 1999), Delaney et al. (1998), and Palmeri (1999). Journal of Experimental Psychology: Learning, Memory, and Cognition. https://doi.org/10.1037/0278-7393.28.2.392"
    author: "Hilde Haider & Peter A. Frensch"
    q: 1
    i: "?"
    kind: causal
    rigour: 1
---

# Simulations show power functions fit aggregated means and standard deviations almost perfectly even when all underlying individual learning curves are discontinuous

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q1`
> **Currency** · newest study 2002 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Haider and Frensch 2002: no comparison group · Haider and Frensch 2002 (2): no comparison group (read from the study by two models, 2026-11-25)

## Subclaims
`q1 i?` Monte Carlo simulations with Weibull-distributed latencies and power-distributed shift points yielded power-function fits to aggregate means with R2 = 99.9%, with fitted exponents almost identical to the shift-point exponents. [→ Haider and Frensch 2002](#haider-and-frensch-2002)
`q1 i?` Aggregate standard deviations also fit power functions well, and the bubble effect appears only under some parameter combinations, so its absence does not rule out strategy shifts. [→ Haider and Frensch 2002 (2)](#haider-and-frensch-2002-2)

## Evidence

### Haider and Frensch 2002

Hilde Haider & Peter A. Frensch. (2002). Why Aggregated Learning Follows the Power Law of Practice When Individual Learning Does Not: Comment on Rickard (1997, 1999), Delaney et al. (1998), and Palmeri (1999). Journal of Experimental Psychology: Learning, Memory, and Cognition. https://doi.org/10.1037/0278-7393.28.2.392

`q1 · i?` · `causal · r2`

Simulations with fixed shift-point exponents and Weibull-distributed first/last-trial latencies (Panel B of Figure 6; Table 4): "the power functions fit the means very well (R2 ⫽ 99.9%)" and fitted exponents matched the shift-point exponents, confirming the mathematical solution.

> "First, the power functions fit the means very well (R2 ⫽ 99.9%). Second, and more important, the exponent for all fitted functions was almost identical to the exponent of the function of the shift points"

### Haider and Frensch 2002 (2)

Hilde Haider & Peter A. Frensch. (2002). Why Aggregated Learning Follows the Power Law of Practice When Individual Learning Does Not: Comment on Rickard (1997, 1999), Delaney et al. (1998), and Palmeri (1999). Journal of Experimental Psychology: Learning, Memory, and Cognition. https://doi.org/10.1037/0278-7393.28.2.392

`q1 · i?` · `causal · r1`

Further simulations varying the shift-point exponent and first-trial RT distributions (Figure 7; Tables 5-6) fit aggregate means and standard deviations well; "the standard deviations show a so-called bubble effect" only when the exponent is small or first/last-trial means differ extremely, so "finding no bubble effect does not allow one to conclude that no strategy shift occurred during training".

> "the standard deviations show a so-called bubble effect (e.g., Rickard, 1999, p. 440) both when the exponent c of the shift-point function is small and when the means of the distributions for the first and last trial are extremely different."

## Discussion


## Related Claims
- [Individual learning curves in the alphabet verification task showed significant deviations from power-function linearity, with latencies changing nonlinearly and probably discontinuously during practice in six single-case studies without a comparison group](avt-individual-curves-deviate-from-linearity.md) — related
- [The power law of practice does not hold in overall (strategy-collapsed) RT and SD data, though instance-theory power fits reached r2 = .94 with systematic deviations](power-law-fails-in-overall-data.md) — related
- [Aggregating Lisp learning data by production rule yields systematic learning curves, while aggregation by more superficial units does not](production-rule-learning-curves-lisp-tutor.md) — related
- [Acquisition of a novel paper-and-pencil matrix task follows a power function of practice at group and individual levels](power-law-learning-in-paper-pencil-matrix-task.md) — related
- [Aggregated over participants, strategy-specific and regular power functions both capture at least 95% of variance in mean solution time, giving no clear preference](aggregated-power-law-fits-mixed.md) — related
- [Reaction time means and standard deviations decreased from pre-test to post-test as power functions of practice with the same exponent in one uncontrolled pre-post study](power-function-speedup-and-sd-reduction.md) — related
- [Autocorrelated residuals show the regular power function deviated systematically from observed aggregated data in two of five cases, while individual-strategy functions showed systematic deviation in only one](residual-autocorrelation-regular-power-function.md) — related
- [Simulated races between algorithm and memory preserve the power law, with memory dominating after about 16 presentations](simulation-race-memory-dominates.md) — related
