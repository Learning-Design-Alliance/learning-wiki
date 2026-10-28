---
type: research-method
id: consistencyequality-fairness-metric-for-educational-recommenders
title: Consistency–equality fairness metric for educational recommenders
description: "The paper formalizes consistency as the similarity between the targeted degree p_u(m) each platform sets for each principle m and the degree q(m) achieved in a learner's recommended list, measured as the complement of a weighted Manhattan distance."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
---

# Consistency–equality fairness metric for educational recommenders

> **Research Method** · [All research methods](index.md)
> **Evidence** · no claims cited

## Description
The paper formalizes consistency as the similarity between the targeted degree p_u(m) each platform sets for each principle m and the degree q(m) achieved in a learner's recommended list, measured as the complement of a weighted Manhattan distance. It then defines equality as "the complement of the Gini index over the consistencies across learners", where a value of 1 means the recommender is perfectly equal across learners in terms of consistency. Unlike prior individual-fairness work, learners count as positively treated when they achieve high consistency regardless of their past interactions, and no sensitive demographic attributes are used.

## Accounts
<!-- How each source describes or uses the method -->
- **Fairness metric combining consistency (complement of weighted Manhattan distance) and equality (complement of Gini index) across learners**: The paper formalizes consistency as the similarity between the targeted degree p_u(m) each platform sets for each principle m and the degree q(m) achieved in a learner's recommended list, measured as the complement of a weighted Manhattan distance. It then defines equality as "the complement of the Gini index over the consistencies across learners", where a value of 1 means the recommender is perfectly equal across learners in terms of consistency. Unlike prior individual-fairness work, learners count as positively treated when they achieve high consistency regardless of their past interactions, and no sensitive demographic attributes are used. (Mirko Marras et al. (2022))

### Claims

## Related Research Methods
-

## Key Sources
- Mirko Marras, Ludovico Boratto, Guilherme Ramos, Gianni Fenu. (2022). Equality of Learning Opportunity via Individual Fairness in Personalized Recommendations. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00271-1
