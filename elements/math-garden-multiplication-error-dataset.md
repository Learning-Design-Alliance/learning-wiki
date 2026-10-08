---
type: element
id: math-garden-multiplication-error-dataset
title: Math Garden single-digit multiplication error dataset and 14-category error classification
description: Math Garden is a computerized adaptive practice environment for arithmetic, widely used in the Netherlands, whose multiplication table domain generated over 25 million responses from over 170 thousand primary school c...
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

# Math Garden single-digit multiplication error dataset and 14-category error classification

> **Element** · [All elements](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
Math Garden is a computerized adaptive practice environment for arithmetic, widely used in the Netherlands, whose multiplication table domain generated over 25 million responses from over 170 thousand primary school children with over 5 million errors. The study selected a three-month window (January to March 2017), Dutch grades 3 to 8, and active, committed students, yielding 346 students and over 25,000 error responses. The error-to-cause mapping adapts Straatemeier's (2014) classification into 14 causes, from operator relevant to reverse and zero errors.

## Design Implications

### Context
#### Requirements
- Error responses that can be elicited by causes in the classification; students must permit scientific research on their responses
#### Constraints
- The final selection is highly pragmatic and may limit generalization to students that practice regularly and for whom the majority of responses are correct

### Target Learners
- Dutch primary school children in grades 3 to 8 (approximately age 6 to 12)

### Target Learning Goals
- adaptive practice of the multiplication tables of one to ten

## Claims

- [In single-digit multiplication, most items are susceptible to nearly all considered error causes, which precludes the use of cognitive diagnostic models for this data](../claims/item-cause-density-precludes-cdms.md) [+W]
- [Larger error windows improve SET ranking performance, with a window of 30 errors yielding the highest MAP regardless of edge-weight transformation](../claims/larger-error-windows-improve-set-ranking.md) [+W]
- [SET calibration shows a window-size by beta interaction, with the lowest Brier score for window size 30, cause weights, and beta = .6](../claims/set-calibration-window-beta-interaction.md) [+W]
- [SET adapts its predicted ranking to individual students' errors for the typo and reverse causes but not for all causes](../claims/set-cause-level-ranking-typo-reverse.md) [+W]

## Related Elements
- 

## Examples

- [Use traced error causes as personalized intervention recommendations in online learning systems](../strategies/error-cause-tracing-for-personalized-recommendations.md)

## Key Sources
- Savi, A. O., Deonovic, B. E., Bolsinova, M., van der Maas, H. L. J., & Maris, G. K. J. (2021). Tracing Systematic Errors to Personalize Recommendations in Single Digit Multiplication and Beyond. Journal of Educational Data Mining, Volume 13, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/382
