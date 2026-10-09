---
type: claim
title: Learning curves show error rates decreased for wind direction, air movement, and cloud type but stayed high for wind speed and precipitation skills
description: Learning curves show error rates decreased for wind direction, air movement, and cloud type but stayed high for wind speed and precipitation skills
id: bkt-learning-curves-skill-differences
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

# Learning curves show error rates decreased for wind direction, air movement, and cloud type but stayed high for wind speed and precipitation skills

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Under BKT, error rates for wind direction, air movement, and cloud type decreased with more learning opportunities, while wind speed and precipitation type and amount remained high. [→ Ying Cui 2019](#ying-cui-2019)

## Evidence

### Ying Cui 2019

Ying Cui, Man-Wai Chu, Fu Chen. (2019). Analyzing Student Process Data in Game-Based Assessments with Bayesian Knowledge Tracing and Dynamic Bayesian Networks. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397

`q2 · i?` · `design · r2`

BKT learning curves (Figure 7) plot mean error rate against learning opportunities; model-predicted error rates overlapped observed error rates. The article reports the contrasting skill patterns quoted above; no effect size is printed.

> "The error rates of wind direction, air movement, and cloud type decreased along with more learning opportunities. However, the error rates of wind speed and precipitation type and amount remained high regardless of the number of learning opportunities."

## Discussion


## Related Claims
- [BKT estimates show most students mastered wind direction and air movement but few mastered wind speed, precipitation type, or amount](bkt-mastery-profile-weather-skills.md) — related
- [DBN analysis shows wind direction and air movement reached the highest posterior mastery probabilities while other skills stayed flat or declined](dbn-posterior-mastery-over-time.md) — related
- [Both BKT and DBN show high classification accuracy but low consistency for wind direction, cloud type, and air movement](classification-accuracy-high-consistency-low.md) — related
