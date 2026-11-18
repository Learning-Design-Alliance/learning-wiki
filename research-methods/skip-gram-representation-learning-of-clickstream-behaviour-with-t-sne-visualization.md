---
type: research-method
id: skip-gram-representation-learning-of-clickstream-behaviour-with-t-sne-visualization
title: Skip-gram representation learning of clickstream behaviour with t-SNE visualization
description: This methodology trains a skip-gram model on chronological sequences of student interactions with course screens, learning a continuous vector representation of each course element, then reduces the vectors to two dimensions with t-SNE for visualization.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
---

# Skip-gram representation learning of clickstream behaviour with t-SNE visualization

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
This methodology trains a skip-gram model on chronological sequences of student interactions with course screens, learning a continuous vector representation of each course element, then reduces the vectors to two dimensions with t-SNE for visualization. As the article puts it, "instead of learning the structure of language by training on sequences of words, we are learning the structure of learner behaviour from sequences of page views." The approach replaces hand-engineered features with model-learned representations so that unfamiliar behavioural patterns can surface organically, and interpretation is validated by a subject matter expert whose implicit course knowledge serves as the check on plausible relationships. It is positioned as a middle ground between descriptive statistics and opaque predictive classifiers.

## Accounts
<!-- How each source describes or uses the method -->
- **Skip-gram representation learning of clickstream behaviour with t-SNE visualization and expert-in-the-loop interpretation**: This methodology trains a skip-gram model on chronological sequences of student interactions with course screens, learning a continuous vector representation of each course element, then reduces the vectors to two dimensions with t-SNE for visualization. As the article puts it, "instead of learning the structure of language by training on sequences of words, we are learning the structure of learner behaviour from sequences of page views." The approach replaces hand-engineered features with model-learned representations so that unfamiliar behavioural patterns can surface organically, and interpretation is validated by a subject matter expert whose implicit course knowledge serves as the check on plausible relationships. It is positioned as a middle ground between descriptive statistics and opaque predictive classifiers. (Pardos et al. (2018))

### Claims
- [The highest-rated skip-gram visualization of Habitable Worlds used a window size of five and vector size of twelve, with low vector sizes yielding overly sequential plots](../claims/skip-gram-hyperparameter-tuning-results.md) [+M]
- [Passing students progress linearly through Habitable Worlds content while failing students show a hub-and-spoke pattern of going to quizzes first](../claims/passing-linear-failing-hub-spoke-habitable-worlds.md) [+M]

## Related Research Methods
-

## Key Sources
- Pardos, Z. A., & Horodyskyj, L. (2018). Analysis of Student Behaviour in Habitable Worlds Using Continuous Representation Visualization. https://github.com/CAHLR/d3-scatterplot
