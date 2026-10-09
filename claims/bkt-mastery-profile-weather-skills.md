---
type: claim
title: BKT estimates show most students mastered wind direction and air movement but few mastered wind speed, precipitation type, or amount
description: BKT estimates show most students mastered wind direction and air movement but few mastered wind speed, precipitation type, or amount
id: bkt-mastery-profile-weather-skills
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
evidence_strength: moderate
sources:
  - id: ying-cui-2019
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397"
    title: "Ying Cui, Man-Wai Chu, Fu Chen. (2019). Analyzing Student Process Data in Game-Based Assessments with Bayesian Knowledge Tracing and Dynamic Bayesian Networks. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397"
    author: Ying Cui, Man-Wai Chu, Fu Chen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# BKT estimates show most students mastered wind direction and air movement but few mastered wind speed, precipitation type, or amount

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Final BKT mastery estimates were high for wind direction (mean 0.821) and air movement (0.751) but near zero for wind speed (0.003) and precipitation type (0.012). [→ Ying Cui 2019](#ying-cui-2019)

## Evidence

### Ying Cui 2019

Ying Cui, Man-Wai Chu, Fu Chen. (2019). Analyzing Student Process Data in Game-Based Assessments with Bayesian Knowledge Tracing and Dynamic Bayesian Networks. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397

`q2 · i?` · `design · r2`

BKT parameter estimation on the pilot log data (Table 3) reports mean final mastery probabilities, e.g. wind direction 0.821 and wind speed 0.003. The article states "the majority of students had mastered wind direction and air movement"; no effect size is printed.

> "Results suggested that the majority of students had mastered wind direction and air movement but relatively fewer students for other skills."

## Discussion


## Related Claims
- [Learning curves show error rates decreased for wind direction, air movement, and cloud type but stayed high for wind speed and precipitation skills](bkt-learning-curves-skill-differences.md) — related
- [DBN analysis shows wind direction and air movement reached the highest posterior mastery probabilities while other skills stayed flat or declined](dbn-posterior-mastery-over-time.md) — related
- [Both BKT and DBN show high classification accuracy but low consistency for wind direction, cloud type, and air movement](classification-accuracy-high-consistency-low.md) — related
