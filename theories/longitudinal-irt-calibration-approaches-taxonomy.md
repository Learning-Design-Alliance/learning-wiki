---
type: theory
title: Taxonomy of four calibration and scoring approaches for multi-timepoint survey measures
description: "The article organizes scoring options for repeated survey administration into four approaches ordered by complexity: (1) cross-sectional IRT calibration with a unidimensional model using a single timepoint, (2) longit..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: kuhfeld-2020
    resource: "https://www.edworkingpapers.com/ai20-193"
    title: "Kuhfeld, Megan, and James Soland. (2020). Estimating Student Growth on Psychological and Social-emotional Constructs: A Comparison of Multiple Scoring Approaches. EdWorkingPaper No. 20-193. https://www.edworkingpapers.com/ai20-193"
    author: Kuhfeld, Megan, and James Soland
---

# Taxonomy of four calibration and scoring approaches for multi-timepoint survey measures

> **Theory** · [All theories](index.md)
> **Evidence** · 10 claims (7 for, 3 mixed) · 5 studies (3 associational, 1 causal, 1 theoretical), `q2` · 0 of 5 report an effect size · 10 claims rest on one study

## Description
The article organizes scoring options for repeated survey administration into four approaches ordered by complexity: (1) cross-sectional IRT calibration with a unidimensional model using a single timepoint, (2) longitudinal unidimensional calibration pooling all timepoints, (3) longitudinal multidimensional IRT (MIRT) calibration with latent variables for each timepoint, and (4) a two-tier MIRT adding specific factors for serial correlation from repeated items. The article frames the core choice: "whether to use an IRT model that calibrates based on a single timepoint versus a MIRT model that includes latent variables for scores at all timepoints." Unlike Approaches 1 and 2, the MIRT approach explicitly accounts for over-time correlations.

## Design Implications

### Context
#### Requirements
- Item responses from the same Likert-type items administered across multiple timepoints
- Specification of calibration sample, IRT model type, and scoring method (e.g., EAP)
#### Constraints
- The two-tier approach does not model serial correlation due to each item being administered repeatedly across timepoints in Approach 3's formulation; Approach 1 assumes items function similarly across ages

### Target Learners
- elementary and middle school students surveyed on psychological and social-emotional constructs

### Target Learning Objectives
- accurate estimation of student growth trajectories on latent psychological and social-emotional constructs

### Claims

- [Mirt Recovers Growth Slope Better Than Sum Scores](../claims/mirt-recovers-growth-slope-better-than-sum-scores.md) [+M]
- [Mirt Better Quadratic Growth Recovery Four Timepoints](../claims/mirt-better-quadratic-growth-recovery-four-timepoints.md) [+M]
- [In the empirical growth mindset study, MIRT scoring yields substantively higher intercept and slope means and variances, including an intercept-slope covariance of .13 that is indistinguishable from zero under other approaches](../claims/empirical-mindset-mirt-higher-means-variances-covariance.md) [+W]
- [Correlations between estimated and true scores diminish over time mainly with easy items, especially with a true slope of .5 and only four items, likely due to ceiling effects](../claims/score-true-correlations-diminish-easy-items-ceiling.md) [~W]
- [Standardized sum scores greatly compress individual differences in simulated growth trajectories, while only MIRT scores capture the wide variation in true trajectories](../claims/sum-scores-compress-growth-trajectory-variability.md) [+W]
- [Multidimensional IRT scores that account for latent variable covariances over time produce better recovery of growth parameters in longitudinal growth models than sum scores and other IRT approaches](../claims/multidimensional-irt-covariance-scores-better-growth-recovery.md) [+W]
- [Bifactor and second-order structures within measurement occasions keep multidimensional growth IRT models computationally tractable](../claims/bifactor-within-occasion-tractable-cliques.md) [+W]
- [Junction-tree factorization reduces EM algorithm complexity for latent growth IRT models from exponential to linear in the number of measurement occasions](../claims/junction-tree-em-linear-complexity-occasions.md) [+W]
- [In concurrent unidimensional calibration the Speaking subtest dominates the Oral scale score while Listening and Speaking correlate only moderately](../claims/speaking-dominates-concurrent-oral-scale.md) [~W]
- [Response styles can affect estimates of growth parameters, including the slope, on social-emotional survey constructs](../claims/response-styles-affect-growth-parameter-estimates.md) [~W]

## Related Theories
- 

## Examples
-

## Key Sources
- Kuhfeld, Megan, and James Soland. (2020). Estimating Student Growth on Psychological and Social-emotional Constructs: A Comparison of Multiple Scoring Approaches. EdWorkingPaper No. 20-193. https://www.edworkingpapers.com/ai20-193
