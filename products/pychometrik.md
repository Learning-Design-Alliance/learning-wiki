---
type: product
id: pychometrik
title: Pychometrik
description: Pychometrik is a Python-based item-analysis and Rasch item-calibration tool developed by NWEA for psychometricians calibrating assessment items.
product_kind: software
status: draft
generated:
  by: "process:sweep-kinds"
  at: 2026-10-10
sources:
  - id: he-2021
    resource: "https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/"
    title: "He, W., Bo, E., Meyer, P., & Grandgeorge, R. (2021). A comparison of item parameter estimates in Pychometrik and the existing item calibration tool. NWEA. https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/"
    author: "He, W., Bo, E., Meyer, P., & Grandgeorge, R"
---

# Pychometrik

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
Pychometrik is a Python-based item-analysis and Rasch item-calibration tool developed by NWEA for psychometricians calibrating assessment items.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->

### Claims
- [When item difficulty and simulee ability ranges align (minimum -10, maximum 8), Pychometrik recovery is accurate, with correlations above 0.99 across all three sample sizes; recovery degrades above the simulee ability maximum of 7.94](../claims/pychometrik-accurate-recovery-when-ranges-align.md) [+W]
- [Item calibration results from Pychometrik and the existing tool are mostly comparable across 1,180 AGC-calibrated MAP Growth items, with average RIT differences ranging from 0.33 (mathematics) to 0.91 (science)](../claims/pychometrik-existing-tool-comparable-calibration-real-data.md) [+W]
- [Log-likelihood comparisons indicate Pychometrik can produce more accurate item parameter estimates than the existing tool for items with RIT differences larger than 2](../claims/pychometrik-higher-loglikelihood-better-estimates.md) [+W]
- [In the Pychometrik item parameter recovery simulation across 27 conditions (Grades K-8, sample sizes 500, 1,000, and 2,000), recovery accuracy increased with sample size and was best for Grade 8 simulees](../claims/pychometrik-recovery-sample-size-and-grade-effects.md) [+W]
- [In a fixed-person calibration simulation with 60 Rasch items and 1,200 simulees, estimates from both tools were comparable to true parameters, with the existing tool underestimating difficulty by 0.03 RIT on average](../claims/simulation-comparability-60-items-1200-simulees.md) [+W]

## Related Products and Programmes
-

## Key Sources
- He, W., Bo, E., Meyer, P., & Grandgeorge, R. (2021). A comparison of item parameter estimates in Pychometrik and the existing item calibration tool. NWEA. https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/

<!-- merged 2026-10-10 from elements/pychometrik-item-calibration-tool ("Pychometrik: a Python-based item calibration tool for Rasch family models"), misfiled as a element and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Pychometrik: a Python-based item calibration tool for Rasch family models

> **Element** · [All elements](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
Pychometrik is a series of Python classes and functions that conducts classical item analysis and Rasch item calibration, using a proportional curve fitting (PCF) algorithm to estimate item difficulty with fixed-person anchoring. It was built to give psychometricians autonomy in calibration for all NWEA shelf products, replacing a restrictive T-SQL-based system; "Both the IGR and Pass 2 procedures from the existing calibration process are not included in Pychometrik." The PCF algorithm is also used in WINSTEPS and jMetrik.

## Design Implications

### Context
#### Requirements
- Fixed-person calibration design: person ability estimates are anchored at values obtained from operational items, then item difficulty is estimated onto the same scale
#### Constraints
- Estimates Rasch family models; additional IRT models such as two-, three-, and four-parameter models are described as designed to be extendable, not yet supported features

### Target Learners
- NWEA psychometricians calibrating MAP Growth field test items

### Target Learning Goals
- Accurate item difficulty (RIT) calibration for K-12 assessment items across mathematics, reading, language, science, and Spanish reading

## Claims

- [When item difficulty and simulee ability ranges align (minimum -10, maximum 8), Pychometrik recovery is accurate, with correlations above 0.99 across all three sample sizes; recovery degrades above the simulee ability maximum of 7.94](../claims/pychometrik-accurate-recovery-when-ranges-align.md) [+W]
- [Item calibration results from Pychometrik and the existing tool are mostly comparable across 1,180 AGC-calibrated MAP Growth items, with average RIT differences ranging from 0.33 (mathematics) to 0.91 (science)](../claims/pychometrik-existing-tool-comparable-calibration-real-data.md) [+W]
- [Log-likelihood comparisons indicate Pychometrik can produce more accurate item parameter estimates than the existing tool for items with RIT differences larger than 2](../claims/pychometrik-higher-loglikelihood-better-estimates.md) [+W]
- [In the Pychometrik item parameter recovery simulation across 27 conditions (Grades K-8, sample sizes 500, 1,000, and 2,000), recovery accuracy increased with sample size and was best for Grade 8 simulees](../claims/pychometrik-recovery-sample-size-and-grade-effects.md) [+W]
- [In a fixed-person calibration simulation with 60 Rasch items and 1,200 simulees, estimates from both tools were comparable to true parameters, with the existing tool underestimating difficulty by 0.03 RIT on average](../claims/simulation-comparability-60-items-1200-simulees.md) [+W]

## Related Elements

- [Five-step SAS-based item fit analysis procedure for MAP Growth K–2 items](../research-methods/five-step-sas-based-item-fit-analysis-procedure-for-map-growth-k2-items.md)

## Examples
-

## Key Sources
- He, W., Bo, E., Meyer, P., & Grandgeorge, R. (2021). A comparison of item parameter estimates in Pychometrik and the existing item calibration tool. NWEA. https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/
-->
