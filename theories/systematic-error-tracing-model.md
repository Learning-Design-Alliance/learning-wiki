---
type: theory
title: Systematic Error Tracing (SET) model
description: "The SET model is a knowledge-based recommendation system that traces the latent causes of a student's systematic errors using a bipartite graph linking causes to errors, derived from the Ising model."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: savi-2021
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382"
    title: "Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382"
    author: "Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J"
---

# Systematic Error Tracing (SET) model

> **Theory** · [All theories](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The SET model is a knowledge-based recommendation system that traces the latent causes of a student's systematic errors using a bipartite graph linking causes to errors, derived from the Ising model. It computes cause probabilities from the relative number of links between a cause and the observed errors, which the authors note is "in accordance with Luce's choice axiom," and can be generalized to a given number of co-occurring causes. It is deliberately not tied to a specific theoretical framework of error origins and is designed for easy implementation in online learning systems, updating after each newly observed error response.

## Design Implications

### Context
#### Requirements
- A known error-to-cause mapping captured in a bigraph, with clearly identifiable errors and mappable possible causes
#### Constraints
- The SET model cannot predict a cause that is not part of the bigraph
- It is confined to items that elicit an erroneous response
- It exhibits a bias to appeal to majority, which can misidentify slips as dominant causes

### Target Learners
- primary school children practicing arithmetic

### Target Learning Objectives
- diagnosis of systematic error causes in single-digit multiplication to guide intervention recommendations

### Claims

- Set Outperforms Majority Vote Beyond Top Recommendation [+M]
- [Set Cause Level Ranking Typo Reverse](../claims/set-cause-level-ranking-typo-reverse.md) [~M]
- [In single-digit multiplication, most items are susceptible to nearly all considered error causes, which precludes the use of cognitive diagnostic models for this data](../claims/item-cause-density-precludes-cdms.md) [+W]
- [Larger error windows improve SET ranking performance, with a window of 30 errors yielding the highest MAP regardless of edge-weight transformation](../claims/larger-error-windows-improve-set-ranking.md) [+W]
- [SET calibration shows a window-size by beta interaction, with the lowest Brier score for window size 30, cause weights, and beta = .6](../claims/set-calibration-window-beta-interaction.md) [+W]

## Related Theories
- 

## Examples

- [Use traced error causes as personalized intervention recommendations in online learning systems](../strategies/error-cause-tracing-for-personalized-recommendations.md)

## Key Sources
- Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382
