---
type: strategy
id: early-prediction-adaptive-pedagogical-strategy
title: Use early student-model predictions to identify at-risk students and adapt pedagogical strategy during tutoring
description: "The article's findings yield a learning environment that can \"foretell students' performance and learning gains early, and can render adaptive pedagogical strategy accordingly\"."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: ye-mao-2018
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    title: "Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318"
    author: Ye Mao, Chen Lin, and Min Chi
---

# Use early student-model predictions to identify at-risk students and adapt pedagogical strategy during tutoring

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article's findings yield a learning environment that can "foretell students' performance and learning gains early, and can render adaptive pedagogical strategy accordingly". Because BKT+SK predicts post-test scores from the earliest 50% of interaction sequences and LSTM predicts learning gains from the earliest 70%, an ITS can identify students at high risk of failing the post-test or of low learning gain well before training ends and offer adaptive recommendation at that point.

## Design Implications

### Context
#### Requirements
- A trained student model (BKT+SK for post-test, LSTM for learning gains) and logged student-ITS interaction trajectories including skills, interventions, performance and response speed
#### Constraints
- Validated on two datasets involving both elicit and tell interventions; the authors state it is not clear whether the same conclusions hold for datasets with only one intervention type or other intervention types such as skip and justify

### Target Learners
- college students in intelligent tutoring systems for physics or probability

### Target Learning Goals
- early identification of students at risk of low post-test scores or low learning gains

## Related Strategies

- [Use predicted hint-taking likelihood and hint effects to adaptively decide whether to withhold or provide hints](adaptive-hint-withholding-from-hint-prediction.md)

## Examples
-

## Key Sources
- Ye Mao, Chen Lin, and Min Chi. (2018). Deep Learning vs. Bayesian Knowledge Tracing: Student Models for Interventions. Journal of Educational Data Mining, Volume 10, No 2. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/318
