---
type: strategy
id: probabilistic-opi-adoption-strategy
title: Adopt probabilistic OPI computation for surgical skill evaluation and training feedback without changing annotation practice
description: The article recommends transitioning to the probabilistic framework for computing OPIs used in surgeon skill evaluation, outcome prediction, and directed feedback for surgeon training.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-22
sources:
  - id: li-ye-2026
    resource: "https://doi.org/10.1371/journal.pone.0355276"
    title: "Li Ye, Kamabattula Sreeram, Bhattacharyya Kiran, Berniker Max. (2026). Validation of expected objective performance indicators in surgical data analysis. PLoS One. https://doi.org/10.1371/journal.pone.0355276"
    author: Li Ye, Kamabattula Sreeram, Bhattacharyya Kiran, Berniker Max
---

# Adopt probabilistic OPI computation for surgical skill evaluation and training feedback without changing annotation practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article recommends transitioning to the probabilistic framework for computing OPIs used in surgeon skill evaluation, outcome prediction, and directed feedback for surgeon training. A key practical advantage is that "probabilistic OPIs do not require a change in the established methodology for annotating steps", which matters because human annotations are the most time- and resource-intensive element. The approach also provides a mechanism to explicitly incorporate annotation variability from procedures, steps, and annotators, and the authors suggest downstream applications could compute a probability distribution over skill rather than a single read-out.

## Design Implications

### Context
#### Requirements
- Existing step annotations can be reused as-is; only the probability of a step or the distribution of annotation times must be available
#### Constraints
- There is a nominal increase in computational effort relative to the hard-boundary method
- The authors state the approach "holds promise" rather than presenting it as established practice

### Target Learners
- surgeons in robotic-assisted surgery training programs

### Target Learning Goals
- directed feedback for surgeon training and surgeon skill evaluation

### Affordances

## Claims

- [Expected OPI bias magnitudes are smaller than hard-boundary bias in every procedure-type-by-OPI comparison, significant in all but three scenarios](../claims/expected-opi-bias-magnitudes-smaller.md) [+W]
- [Normalized standard deviations of expected OPIs are significantly smaller than hard-boundary OPIs in all procedure-type-by-OPI conditions](../claims/expected-opi-standard-deviations-significantly-smaller.md) [+W]
- [Expected OPIs are significantly biased less often than hard-boundary OPIs when annotations are noisy (49.37% vs 56.63% of steps)](../claims/expected-opis-biased-less-often-than-hard-boundary.md) [+W]
- [Expected OPIs are less variable under annotator noise: 40.56% of steps showed larger hard-boundary variance versus 8.52% with larger expected variance](../claims/expected-opis-less-variable-annotator-noise.md) [+W]
- [For kinematic OPIs (tool path length and angular path length), expected OPIs show a consistent and substantial accuracy improvement across procedure types](../claims/kinematic-opis-accuracy-improvement-expected-method.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Li Ye, Kamabattula Sreeram, Bhattacharyya Kiran, Berniker Max. (2026). Validation of expected objective performance indicators in surgical data analysis. PLoS One. https://doi.org/10.1371/journal.pone.0355276
