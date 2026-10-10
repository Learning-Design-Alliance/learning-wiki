---
type: research-method
id: map-growth-item-calibration-workflow
title: MAP Growth item calibration workflow
description: "The existing tool, built in T-SQL within the Growth Research Database, runs an automated pipeline: data cleaning, item parameter estimation via a brute-force grid search over RIT values 100-350 that minimizes mean square fit with person abilities fixed, and a Model of Man (MoM) procedure that predic"
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

# MAP Growth item calibration workflow

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The existing tool, built in T-SQL within the Growth Research Database, runs an automated pipeline: data cleaning, item parameter estimation via a brute-force grid search over RIT values 100-350 that minimizes mean square fit with person abilities fixed, and a Model of Man (MoM) procedure that predicts which items need human review. Calibration samples are chosen by all grade calibration (AGC) or iterative grade range (IGR) via a chi-square goodness-of-fit test, and Pass 2 filtering removes test events with less than 10% probability of a correct response given Pass 1 estimates. The article documents this workflow as the baseline against which Pychometrik was compared.

## Accounts
<!-- How each source describes or uses the method -->
- **The existing MAP Growth item calibration workflow: automated AGC/IGR sampling, two-pass filtering, brute-force MSF estimation, and Model of Man review triage**: The existing tool, built in T-SQL within the Growth Research Database, runs an automated pipeline: data cleaning, item parameter estimation via a brute-force grid search over RIT values 100-350 that minimizes mean square fit with person abilities fixed, and a Model of Man (MoM) procedure that predicts which items need human review. Calibration samples are chosen by all grade calibration (AGC) or iterative grade range (IGR) via a chi-square goodness-of-fit test, and Pass 2 filtering removes test events with less than 10% probability of a correct response given Pass 1 estimates. The article documents this workflow as the baseline against which Pychometrik was compared. (He et al. (2021))

### Claims
- [Item calibration results from Pychometrik and the existing tool are mostly comparable across 1,180 AGC-calibrated MAP Growth items, with average RIT differences ranging from 0.33 (mathematics) to 0.91 (science)](../claims/pychometrik-existing-tool-comparable-calibration-real-data.md) [+W]
- [Log-likelihood comparisons indicate Pychometrik can produce more accurate item parameter estimates than the existing tool for items with RIT differences larger than 2](../claims/pychometrik-higher-loglikelihood-better-estimates.md) [-W]
- [In a fixed-person calibration simulation with 60 Rasch items and 1,200 simulees, estimates from both tools were comparable to true parameters, with the existing tool underestimating difficulty by 0.03 RIT on average](../claims/simulation-comparability-60-items-1200-simulees.md) [+W]

## Related Research Methods
-

## Key Sources
- He, W., Bo, E., Meyer, P., & Grandgeorge, R. (2021). A comparison of item parameter estimates in Pychometrik and the existing item calibration tool. NWEA. https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/

<!-- merged 2026-10-10 from theories/existing-map-growth-item-calibration-workflow ("The existing MAP Growth item calibration workflow: automated AGC/IGR sampling, two-pass filtering, brute-force MSF estimation, and Model of Man review triage"), misfiled as a theorie and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# The existing MAP Growth item calibration workflow: automated AGC/IGR sampling, two-pass filtering, brute-force MSF estimation, and Model of Man review triage

> **Theory** · [All theories](index.md)
> **Evidence** · 3 claims (2 for, 1 against) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The existing tool, built in T-SQL within the Growth Research Database, runs an automated pipeline: data cleaning, item parameter estimation via a brute-force grid search over RIT values 100-350 that minimizes mean square fit with person abilities fixed, and a Model of Man (MoM) procedure that predicts which items need human review. Calibration samples are chosen by all grade calibration (AGC) or iterative grade range (IGR) via a chi-square goodness-of-fit test, and Pass 2 filtering removes test events with less than 10% probability of a correct response given Pass 1 estimates. The article documents this workflow as the baseline against which Pychometrik was compared.

## Design Implications

### Context
#### Requirements
- Person ability estimates fixed to values from operational items; a calibration sample selected by AGC or IGR before item difficulty estimation
#### Constraints
- Designed specifically for Rasch-based items only; cannot support 2PL, 3PL, or polytomous models, and does not support free estimation of item and person parameters
- Two-pass filtering causes field testing inefficiency because very large numbers of students are excluded from calibration of very difficult items

### Target Learners
- Students taking MAP Growth field test items in grades K-8 and beyond

### Target Learning Objectives
- Operational item difficulty calibration supporting accurate achievement measurement on the RIT scale

### Claims

- [Item calibration results from Pychometrik and the existing tool are mostly comparable across 1,180 AGC-calibrated MAP Growth items, with average RIT differences ranging from 0.33 (mathematics) to 0.91 (science)](../claims/pychometrik-existing-tool-comparable-calibration-real-data.md) [+W]
- [Log-likelihood comparisons indicate Pychometrik can produce more accurate item parameter estimates than the existing tool for items with RIT differences larger than 2](../claims/pychometrik-higher-loglikelihood-better-estimates.md) [-W]
- [In a fixed-person calibration simulation with 60 Rasch items and 1,200 simulees, estimates from both tools were comparable to true parameters, with the existing tool underestimating difficulty by 0.03 RIT on average](../claims/simulation-comparability-60-items-1200-simulees.md) [+W]

## Related Theories
- [Pychometrik Item Calibration Tool](../products/pychometrik.md)

## Examples
-

## Key Sources
- He, W., Bo, E., Meyer, P., & Grandgeorge, R. (2021). A comparison of item parameter estimates in Pychometrik and the existing item calibration tool. NWEA. https://www.nwea.org/research/publication/a-comparison-of-item-parameter-estimates-in-pychometrik-and-the-existing-item-calibration-tool/
-->
