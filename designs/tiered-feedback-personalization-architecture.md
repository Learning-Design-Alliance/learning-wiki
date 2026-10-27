---
type: design
id: tiered-feedback-personalization-architecture
title: Three-tier personalization architecture for feedback selection in a dialogue-based ITS
description: "The article organizes feedback selection as three increasingly personalized Random Forest models: a BASELINE model using only \"linguistic features\" assessing hint quality in isolation (14 features), a SHALLOW PERSONAL..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
sources:
  - id: kochmar-2022
    resource: "https://doi.org/10.1007/s40593-021-00267-x"
    title: "Kochmar, E., Vu, D. D., Belfer, R., Gupta, V., Serban, I. V., & Pineau, J. (2022). Automated Data-Driven Generation of Personalized Pedagogical Interventions in Intelligent Tutoring Systems. International Journal of Artificial Intelligence in Education, 32, 323–349. https://doi.org/10.1007/s40593-021-00267-x"
    author: "Kochmar, E., Vu, D. D., Belfer, R., Gupta, V., Serban, I. V., & Pineau, J"
---

# Three-tier personalization architecture for feedback selection in a dialogue-based ITS

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article organizes feedback selection as three increasingly personalized Random Forest models: a BASELINE model using only "linguistic features" assessing hint quality in isolation (14 features), a SHALLOW PERSONALIZATION model adding 8 "performance-based features" such as past attempts and correctness proportions (22 total), and a DISCOURSE PERSONALIZATION model that also analyzes up to 4 previous interaction turns with keyword, topic-overlap, and perplexity features (49 total). Models are trained in a binary classification setting to predict whether a student will correctly solve the exercise on the next attempt given a hint. This architecture lets an ITS choose pedagogical interventions without hand-crafted rules.

## Design Implications

### Context
#### Requirements
- A database of expectations (reference solutions) from which hints are generated, and recorded historical student–system interactions for training
#### Constraints
- The number of previous dialogue turns (up to 4) was selected to maximize coverage of interactions available on the platform at the time of the experiments

### Target Learners
- adult online learners of machine learning and data science

### Learning Goals
- problem-solving exercises in data science and machine learning

### Claims
- [Discourse Personalization Hint Selection Best Cv](../claims/discourse-personalization-hint-selection-best-cv.md) [+M]
- [Personalized Hints Improve Success Rate Pilot](../claims/personalized-hints-improve-success-rate-pilot.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Kochmar, E., Vu, D. D., Belfer, R., Gupta, V., Serban, I. V., & Pineau, J. (2022). Automated Data-Driven Generation of Personalized Pedagogical Interventions in Intelligent Tutoring Systems. International Journal of Artificial Intelligence in Education, 32, 323–349. https://doi.org/10.1007/s40593-021-00267-x
