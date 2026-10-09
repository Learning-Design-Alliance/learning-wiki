---
type: element
id: raging-skies-game-assessment
title: "Raging Skies: an Evidence-Centered game Design assessment for Grade 5 weather outcomes"
description: Raging Skies is a digital game-based assessment built with Evidence-Centered game Design, casting students as storm chasers who measure six storm features with weather instruments and identify storm types.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: ying-cui-2019
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397"
    title: "Ying Cui, Man-Wai Chu, Fu Chen. (2019). Analyzing Student Process Data in Game-Based Assessments with Bayesian Knowledge Tracing and Dynamic Bayesian Networks. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397"
    author: Ying Cui, Man-Wai Chu, Fu Chen
---

# Raging Skies: an Evidence-Centered game Design assessment for Grade 5 weather outcomes

> **Element** · [All elements](index.md)
> **Evidence** · 7 claims (2 for, 5 mixed) · 2 studies (2 design), `q2` · 1 of 2 report an effect size · 7 claims rest on one study

## Description
Raging Skies is a digital game-based assessment built with Evidence-Centered game Design, casting students as storm chasers who measure six storm features with weather instruments and identify storm types. It targets six weather knowledge outcomes from Alberta's Grade 5 Weather Watch unit. Difficulty adapts to performance, and in-game money serves as formative feedback after each storm task plus a summative report. The article notes simple reports suffice for learning purposes, but classroom assessment use "a more rigorous scoring procedure that estimates student proficiency levels" is needed.

## Design Implications

### Context
#### Requirements
- Enough evidence per student: all eleven storm tasks are presented so reliable claims can be made
#### Constraints
- Conventional measurement models assuming unchanged proficiency may not be tenable because students learn during gameplay

### Target Learners
- Grade 5 students studying the Weather Watch science unit

### Target Learning Goals
- Describing air movement, wind speed and direction, precipitation, and cloud types; recording observations and stating inferences

## Claims

- [Standard BKT fits Raging Skies pilot process data with acceptable RMSE and good accuracy under 10-fold cross-validation](../claims/bkt-fits-raging-skies-process-data.md) [+W]
- [Learning curves show error rates decreased for wind direction, air movement, and cloud type but stayed high for wind speed and precipitation skills](../claims/bkt-learning-curves-skill-differences.md) [~W]
- [BKT estimates show most students mastered wind direction and air movement but few mastered wind speed, precipitation type, or amount](../claims/bkt-mastery-profile-weather-skills.md) [~W]
- [BKT tended to outperform DBN across skills, possibly because DBN's greater parameter complexity exceeded what the sample size could estimate](../claims/bkt-outperforms-dbn.md) [~W]
- [Both BKT and DBN show high classification accuracy but low consistency for wind direction, cloud type, and air movement](../claims/classification-accuracy-high-consistency-low.md) [~W]
- [DBN analysis shows wind direction and air movement reached the highest posterior mastery probabilities while other skills stayed flat or declined](../claims/dbn-posterior-mastery-over-time.md) [~W]
- [The EM solver consistently outperformed stochastic gradient descent for fitting the models, though by a small margin](../claims/em-beats-sgd-fitting-spectral-bkt.md) [+W]

## Related Elements

- [Assessment Mechanic](assessment-mechanic.md)

## Examples

- [Evidence-Centered Design](../methods/evidence-centered-design.md)

## Key Sources
- Ying Cui, Man-Wai Chu, Fu Chen. (2019). Analyzing Student Process Data in Game-Based Assessments with Bayesian Knowledge Tracing and Dynamic Bayesian Networks. Journal of Educational Data Mining, Volume 11, No 1. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/397
