---
type: claim
title: Both BKT and DBN show high classification accuracy but low consistency for wind direction, cloud type, and air movement
description: Both BKT and DBN show high classification accuracy but low consistency for wind direction, cloud type, and air movement
id: classification-accuracy-high-consistency-low
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

# Both BKT and DBN show high classification accuracy but low consistency for wind direction, cloud type, and air movement

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Classification accuracy ranged from .75 to 1.00 for BKT and .74 to 1.00 for DBN, but consistency was comparatively low for wind direction (.58 BKT, .46 DBN), cloud type (.38, .40), and air movement (.50, .43). [→ Ying Cui 2019](#ying-cui-2019)

## Evidence

### Ying Cui 2019

Ying Cui, Man-Wai Chu, Fu Chen. (2019). Analyzing Student Process Data in Game-Based Assessments with Bayesian Knowledge Tracing and Dynamic Bayesian Networks. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397

`q2 · i?` · `design · r2`

Simulation approach of Almond et al. (2015) on the fitted models: 1,000 simulated mastery profiles were classified to compute accuracy and consistency matrices (Table 6). The article reports the printed ranges and the low-consistency skills; no effect size is printed.

> "the classification accuracy indices across different skills were relatively high, ranging from .75 to 1.00 for BKT, and from .74 to 1.00 for DBN"

## Discussion


## Related Claims
- [BKT tended to outperform DBN across skills, possibly because DBN's greater parameter complexity exceeded what the sample size could estimate](bkt-outperforms-dbn.md) — related
- [Learning curves show error rates decreased for wind direction, air movement, and cloud type but stayed high for wind speed and precipitation skills](bkt-learning-curves-skill-differences.md) — related
- [DBN analysis shows wind direction and air movement reached the highest posterior mastery probabilities while other skills stayed flat or declined](dbn-posterior-mastery-over-time.md) — related
- [BKT estimates show most students mastered wind direction and air movement but few mastered wind speed, precipitation type, or amount](bkt-mastery-profile-weather-skills.md) — related
