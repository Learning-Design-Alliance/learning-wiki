---
type: claim
title: ACT scores weakly predict college graduation, and the school-level variance in the ACT slope (0.192) exceeds the average slope (0.129), so school effects introduce more noise than the ACT signal
description: ACT scores weakly predict college graduation, and the school-level variance in the ACT slope (0.192) exceeds the average slope (0.129), so school effects introduce more noise than the ACT signal
id: act-weak-predictor-noise-exceeds-signal
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: allensworth-2019
    resource: "https://consortium.uchicago.edu/publications/are-gpas-inconsistent-measure-achievement-across-high-schools-examining-assumptions"
    title: "Allensworth, Elaine M., & Clark, Kallie. (2019). Are GPAs an Inconsistent Measure of College Readiness across High Schools? Examining Assumptions about Grades versus Standardized Test Scores. University of Chicago Consortium on School Research. https://consortium.uchicago.edu/publications/are-gpas-inconsistent-measure-achievement-across-high-schools-examining-assumptions"
    author: "Allensworth, Elaine M., & Clark, Kallie"
    q: 2
    i: "?"
    kind: associational
    rigour: 3
  - id: allensworth-2019-2
    resource: "https://consortium.uchicago.edu/publications/are-gpas-inconsistent-measure-achievement-across-high-schools-examining-assumptions"
    title: "Allensworth, Elaine M., & Clark, Kallie. (2019). Are GPAs an Inconsistent Measure of College Readiness across High Schools? Examining Assumptions about Grades versus Standardized Test Scores. University of Chicago Consortium on School Research. https://consortium.uchicago.edu/publications/are-gpas-inconsistent-measure-achievement-across-high-schools-examining-assumptions"
    author: "Allensworth, Elaine M., & Clark, Kallie"
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# ACT scores weakly predict college graduation, and the school-level variance in the ACT slope (0.192) exceeds the average slope (0.129), so school effects introduce more noise than the ACT signal

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2`–`r3` · `q2`

## Subclaims
`q2 i?` Each standard deviation increase in ACT raises the odds of graduating by only 14 percent (odds coefficient 1.14), and the relationship becomes negative among the highest achievers. [→ Allensworth 2019](#allensworth-2019)
`q2 i?` The variance in ACT slopes across schools (0.192) is larger than the average slope (0.129), so where a student attended high school says more about graduation than their individual ACT score among average or high scorers. [→ Allensworth 2019 (2)](#allensworth-2019-2)

## Evidence

### Allensworth 2019

Allensworth, Elaine M., & Clark, Kallie. (2019). Are GPAs an Inconsistent Measure of College Readiness across High Schools? Examining Assumptions about Grades versus Standardized Test Scores. University of Chicago Consortium on School Research. https://consortium.uchicago.edu/publications/are-gpas-inconsistent-measure-achievement-across-high-schools-examining-assumptions

`q2 · i?` · `associational · r3`

Hierarchical models parallel to the HSGPA models, substituting ACT scores (n=17,753). The article reports an unstandardized "odds coefficient of 1.14" and a "negative quadratic term", so the relationship is larger among low achievers and negative among the highest achievers.

> "The standardized linear term is much smaller than that of standardized HSGPA scores (0.129 vs. 0.703), with the odds of graduating increasing by 14 percent (odds coefficient of 1.14) for every standard deviation increase in ACT scores when the quadratic term equals zero."

### Allensworth 2019 (2)

Allensworth, Elaine M., & Clark, Kallie. (2019). Are GPAs an Inconsistent Measure of College Readiness across High Schools? Examining Assumptions about Grades versus Standardized Test Scores. University of Chicago Consortium on School Research. https://consortium.uchicago.edu/publications/are-gpas-inconsistent-measure-achievement-across-high-schools-examining-assumptions

`q2 · i?` · `associational · r2`

Random-slope ACT model variance components. The article concludes that "noise introduced by school effects is larger than the signal from ACT scores" for students with average or high ACT scores.

> "The variance components show that the linear component of the slope varies significantly, and the variance in the slopes (0.192) is larger than the average slope (0.129)."

## Discussion


## Related Claims
- [Adding ACT scores to models with HSGPA does not improve prediction of college graduation or reduce between-school variability](act-adds-little-beyond-hsgpa.md) — related
- [Adding ACT scores to models with HSGPA does not improve prediction of college graduation or reduce high-school variance](act-adds-little-beyond-hsgpa-graduation.md) — related
- [ACT scores show a weak relationship with college graduation, with slope variation across high schools larger than the average signal](act-weak-inconsistent-predictor-college-graduation.md) — possibly the same claim (merge candidate)
- [For four-year (rather than six-year) graduation, ACT scores are slightly predictive but their coefficient is one-sixth the HSGPA coefficient](act-weakly-predicts-four-year-graduation.md) — related
- [Both HSGPA and ACT strongly predict four-year college enrollment and enrollment in colleges with strong graduation rates](gpa-and-act-predict-enrollment-college-quality.md) — related
- [High school GPA is a better predictor of college graduation than standardized test scores, yet districts continue to rely on test-based readiness benchmarks](gpa-better-predictor-than-test-scores.md) — related
- [HSGPAs have a strong, consistent relationship with college graduation that is larger than school effects, while ACT scores have a weak relationship smaller than high school effects with slopes varying by school](hsgpa-strong-act-weak-college-graduation-predictors.md) — related
- [School average ACT scores predict college graduation for students with the same individual HSGPA and ACT score, reducing between-school variance by 42 percent, while school poverty is not significant once average ACT is included](school-average-act-explains-school-variance.md) — related
