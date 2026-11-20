---
type: strategy
id: sensor-free-future-research-agenda
title: Prioritize underrepresented emotion samples, shared log databases, open source code, and real-time CBLE integration in future sensor-free affect research
description: "The review's forward-looking recommendations call for improving sensor-free detection models, collecting more samples of underrepresented emotions, and identifying additional emotions."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: de-morais-2023
    resource: "https://arxiv.org/abs/2310.13711"
    title: "de Morais, F., Goldoni, D. D'Á., Kautzmann, T., Silva, R. R. da, Jaques, P. A. (2023). Automatic Sensor-free Affect Detection: A Systematic Literature Review. https://arxiv.org/abs/2310.13711"
    author: "de Morais, F., Goldoni, D. D'Á., Kautzmann, T., Silva, R. R. da, Jaques, P. A"
---

# Prioritize underrepresented emotion samples, shared log databases, open source code, and real-time CBLE integration in future sensor-free affect research

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 review), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The review's forward-looking recommendations call for improving sensor-free detection models, collecting more samples of underrepresented emotions, and identifying additional emotions. It further recommends refining development practices by "comparing the accuracy of various data collection techniques, determining the optimal granularity of duration, establishing a shared database of action logs and emotion labels, and making the source code of these models publicly accessible." Future work should prioritize integrating models into CBLEs for real-time detection, providing meaningful interventions based on detected emotions, and deepening understanding of emotions' impact on learning.

## Design Implications

### Context
#### Requirements
- Deployment in real-time within CBLEs requires detectors trained on logs synchronized with reliable emotion ground-truth labels
#### Constraints
- 

### Target Learners
- students using computer-based learning environments at scale, including large online populations

### Target Learning Goals
- timely detection of learner affective states to enable intervention and support personalized learning

## Claims

- [Prior reviews conclude emotion and affect detection was not yet mature enough for full automated integration, with most studies using unimodal facial methods](../claims/prior-reviews-affect-detection-immaturity.md) [+W]
- [The grain level for emotion labels in sensor-free affect detection ranges from seconds to weeks depending on the collection approach](../claims/sensor-free-emotion-grain-varies.md) [+W]
- [Boredom, confusion, frustration, and engagement are the most detected emotions in sensor-free affect detection, appearing in more than 84% of reviewed works](../claims/sensor-free-most-detected-emotions-four.md) [+W]

## Related Strategies

- [Future research should study affect and emotion as structural, systemic, racialized, gendered, and embodied phenomena](future-research-affect-structural-systemic.md)

## Examples
-

## Key Sources
- de Morais, F., Goldoni, D. D'Á., Kautzmann, T., Silva, R. R. da, Jaques, P. A. (2023). Automatic Sensor-free Affect Detection: A Systematic Literature Review. https://arxiv.org/abs/2310.13711
