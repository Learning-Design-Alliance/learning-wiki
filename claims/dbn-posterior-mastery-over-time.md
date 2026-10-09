---
type: claim
title: DBN analysis shows wind direction and air movement reached the highest posterior mastery probabilities while other skills stayed flat or declined
description: DBN analysis shows wind direction and air movement reached the highest posterior mastery probabilities while other skills stayed flat or declined
id: dbn-posterior-mastery-over-time
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

# DBN analysis shows wind direction and air movement reached the highest posterior mastery probabilities while other skills stayed flat or declined

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` DBN posterior mastery probabilities were highest for wind direction (0.69) and air movement (0.64), while precipitation type and wind speed showed extremely low mastery probabilities for most time slices. [→ Ying Cui 2019](#ying-cui-2019)

## Evidence

### Ying Cui 2019

Ying Cui, Man-Wai Chu, Fu Chen. (2019). Analyzing Student Process Data in Game-Based Assessments with Bayesian Knowledge Tracing and Dynamic Bayesian Networks. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397

`q2 · i?` · `design · r2`

DBN analysis in GeNIe of students' first game completion, with 11 time slices for the 11 storms. Table 5 prints posterior mastery per skill per slice; the article notes "precipitation type and wind speed showed extremely low mastery probabilities for most time slices". No effect size is printed.

> "According to Table 5, wind direction and air movement showed the highest posterior mastery probabilities, 0.69 and 0.64, respectively."

## Discussion


## Related Claims
- [Learning curves show error rates decreased for wind direction, air movement, and cloud type but stayed high for wind speed and precipitation skills](bkt-learning-curves-skill-differences.md) — related
- [BKT estimates show most students mastered wind direction and air movement but few mastered wind speed, precipitation type, or amount](bkt-mastery-profile-weather-skills.md) — related
- [Both BKT and DBN show high classification accuracy but low consistency for wind direction, cloud type, and air movement](classification-accuracy-high-consistency-low.md) — related
