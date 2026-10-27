---
type: strategy
id: early-purchase-prediction-interventions
title: Use early-run purchase predictions to trigger interventions guiding learners towards paying behaviour
description: The article recommends exploiting the fact that its predictive features (time spent per step and registration-time demographics) are logged or collected early in each run, so course providers can apply the prediction...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: alshehri-2021
    resource: "https://doi.org/10.1007/s40593-021-00246-2"
    title: "Alshehri, M., Alamri, A., Cristea, A. I., & Stewart, C. D. (2021). Towards Designing Profitable Courses: Predicting Student Purchasing Behaviour in MOOCs. International Journal of Artificial Intelligence in Education, 31, 215–233. https://doi.org/10.1007/s40593-021-00246-2"
    author: "Alshehri, M., Alamri, A., Cristea, A. I., & Stewart, C. D"
---

# Use early-run purchase predictions to trigger interventions guiding learners towards paying behaviour

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article recommends exploiting the fact that its predictive features (time spent per step and registration-time demographics) are logged or collected early in each run, so course providers can apply the prediction model early and intervene with learners unlikely to purchase. The authors state this aspect is "critical as it means that course providers could use our prediction model to create early interventions and thus guide more of the students towards paying behaviour, potentially increasing their revenue". They also suggest targeting adaptive strategies based on learner characteristics.

## Design Implications

### Context
#### Requirements
- A prediction model trained on features available early in the run (time spent on steps, demographics collected at registration)
#### Constraints
- Time as a prediction variable is potentially influenced by external variables such as transmission rate

### Target Learners
- MOOC learners on FutureLearn

### Target Learning Goals
- Increasing certificate purchasing and MOOC revenue through early intervention

## Claims

- [Machine learning models predict MOOC certificate purchasing with accuracies of 0.82–0.91 using only time spent on each course step](../claims/ml-predicts-mooc-purchase-time-spent.md) [+W]
- [MOOC certificate purchasing is rare: under 1% of enrolled learners purchase, with completion around 10%](../claims/mooc-purchase-rate-under-one-percent.md) [+W]

## Related Strategies

- [Deploy ML-based early-warning prediction to shift retention support from reactive to proactive intervention](ml-early-warning-proactive-retention-support.md)
- [Use early-session timing signals, interpreted relative to proficiency, to identify students needing adaptive support](early-session-timing-signals-target-adaptive-support.md)

## Examples
-

## Key Sources
- Alshehri, M., Alamri, A., Cristea, A. I., & Stewart, C. D. (2021). Towards Designing Profitable Courses: Predicting Student Purchasing Behaviour in MOOCs. International Journal of Artificial Intelligence in Education, 31, 215–233. https://doi.org/10.1007/s40593-021-00246-2
