---
type: claim
title: Taking the third-semester modern physics course is the single most important feature in a random forest model predicting whether a declared physics major earns a physics or an engineering degree
description: Taking the third-semester modern physics course is the single most important feature in a random forest model predicting whether a declared physics major earns a physics or an engineering degree
id: modern-physics-course-most-important-predictor-physics-degree
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
sources:
  - id: john-m-aiken-2019
    resource: "https://doi.org/10.1103/physrevphyseducres.15.010128"
    title: "John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Modeling student pathways in a physics bachelor's degree program. [doi:10.1103/physrevphyseducres.15.010128](https://doi.org/10.1103/physrevphyseducres.15.010128)"
    author: John M. Aiken, Rachel Henderson, and Marcos D. Caballero
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Taking the third-semester modern physics course is the single most important feature in a random forest model predicting whether a declared physics major earns a physics or an engineering degree

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A random forest classifier fit to MSU registrar data identified taking modern physics as the feature of greatest importance for predicting graduation degree, with model AUC = 0.93. [→ John M. Aiken 2019](#john-m-aiken-2019)

## Evidence

### John M. Aiken 2019

John M. Aiken, Rachel Henderson, and Marcos D. Caballero. (2019). Modeling student pathways in a physics bachelor's degree program. [doi:10.1103/physrevphyseducres.15.010128](https://doi.org/10.1103/physrevphyseducres.15.010128)

`q2 · i?` · `associational · r2`

Main Model random forest trained on 70% of 1422 MSU physics-major records and tested on 30% hold-out data, with parameters chosen by grid search. The article reports "taking modern physics was of greatest importance to the model's prediction" and AUC = 0.93; no other feature exceeded importance 0.1.

> "The model demonstrated that taking modern physics was of greatest importance to the model's prediction (Figure 3). This model's predictive ability is high demonsrated by (AUC=0.93) the ROC curve being well above the random guessing discrimina- tion line."

## Discussion


## Related Claims
- [Taking an engineering course while registered as a physics major is the second most important predictor of switching from physics to an engineering degree](engineering-course-while-physics-major-predicts-switch.md) — related
- [Lower-division coursework performance is a strong indicator of whether an electrical engineering student graduates](lower-division-performance-indicates-graduation.md) — related
- [Students who leave the physics major take required introductory courses later than the recommended schedule, while physics degree earners take them earlier](course-timing-differentiates-physics-degree-earners.md) — related
- [Model results are robust to varying training fraction and number of trees, but the highest-physics-degree factor is only marginally meaningful](hyperparameter-robustness-variable-importance.md) — related
- [Recursive feature elimination finds the optimum predictive model uses only two features — taking modern physics and taking an engineering course as a physics major](rfe-two-feature-optimum-model.md) — related
- [High school GPA and MSU math placement scores add no predictive power to models of physics versus engineering graduation](prior-preparation-features-no-predictive-gain.md) — related
- [Modern physics is students' first introduction to quantum concepts, with 70.7% of courses being a graduation requirement for physics majors](modern-physics-first-quantum-introduction-gateway.md) — related
