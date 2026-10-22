---
type: strategy
id: early-warning-system-teacher-support-inquiry
title: Use explainable machine learning early warning systems to help teachers identify struggling inquiry learners early
description: The article recommends building early warning systems that integrate cognitive, affective, and metacognitive data from technology-enhanced learning environments so teachers can notice learners who struggle with self-r...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-22
sources:
  - id: kubsch-2025
    resource: "https://doi.org/10.1007/s10648-025-10011-9"
    title: "Kubsch, M., Strauß, S., Grimm, A., Gombert, S., Drachsler, H., Neumann, K., & Rummel, N. (2025). Self-regulated Learning in the Digitally Enhanced Science Classroom: Toward an Early Warning System. Educational Psychology Review. https://doi.org/10.1007/s10648-025-10011-9"
    author: "Kubsch, M., Strauß, S., Grimm, A., Gombert, S., Drachsler, H., Neumann, K., & Rummel, N"
---

# Use explainable machine learning early warning systems to help teachers identify struggling inquiry learners early

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 3 studies (2 review, 1 associational), `q2` · 0 of 3 report an effect size · 4 claims rest on one study

## Description
The article recommends building early warning systems that integrate cognitive, affective, and metacognitive data from technology-enhanced learning environments so teachers can notice learners who struggle with self-regulation and provide support early in the inquiry process. Interpretability is paramount: "the insights generated must be understandable and accessible to educators, enabling them to make informed decisions." Explainable AI techniques such as feature importance analysis and local approximations support scrutability for teachers and researchers.

## Design Implications

### Context
#### Requirements
- Models must be interpretable and scrutable so educators can act on them; data streams must be collectable under classroom affordances
#### Constraints
- The study investigated preliminary conditions only; no system was actually implemented in practice, and bias must be evaluated before deployment

### Target Learners
- middle school students in inquiry-based science classrooms

### Target Learning Goals
- timely teacher support for students struggling with self-regulated learning during inquiry

### Affordances
- [Camm Self Regulation Framework Classroom](../theories/self-regulated-learning.md)

## Claims

- [Affective and metacognitive data alone predict learning productivity early in the unit, but cognitive data becomes the stronger predictor in later parts](../claims/early-warning-system-cam-predictive-importance-shifts-over-unit.md) [+W]
- [Bias in predicting learning productivity, measured as accuracy differences across gender and parental educational background, was highly dependent on the ML method used](../claims/bias-dependent-on-ml-method.md) [+W]
- [Boosting models (XGBoost) achieved the highest predictive accuracy among the compared ML models, while logistic regression showed the lowest](../claims/boosting-highest-accuracy-logistic-lowest.md) [+W]
- [Combining cognitive, affective, and metacognitive data from digital workbooks predicts middle-school students' learning productivity with accuracy rising from about 60% to 100% as an inquiry unit progresses](../claims/cam-data-predict-learning-productivity-early-warning.md) [+W]
- [Machine-learning analysis of multimodal classroom indicators can predict student productivity, and prior knowledge becomes relevant later in the regulation process](../claims/kubsch-multimodal-prediction-prior-knowledge-timing.md) [+W]

## Related Strategies

- [Implement early-warning systems in real classrooms using easily accessible data and transparent machine learning techniques](early-warning-systems-accessible-data-transparent-ml.md)
- [Deploy ML-based early-warning prediction to shift retention support from reactive to proactive intervention](ml-early-warning-proactive-retention-support.md)
- [Use an early warning system based on linked school and human services data to target resources and lessen risks before they become more serious](early-warning-system-target-resources-near-term-risks.md)
- [Use postsecondary readiness indicators in an early warning system and combine cultural responsiveness with tiered interventions to address disparities](early-warning-system-with-tiered-culturally-responsive-supports.md)
- [Build early-warning indicators and leverage online-learning-system process data to support students before gaps widen in Grade 3](early-indicators-online-system-process-data.md)

## Examples
-

## Key Sources
- Kubsch, M., Strauß, S., Grimm, A., Gombert, S., Drachsler, H., Neumann, K., & Rummel, N. (2025). Self-regulated Learning in the Digitally Enhanced Science Classroom: Toward an Early Warning System. Educational Psychology Review. https://doi.org/10.1007/s10648-025-10011-9
