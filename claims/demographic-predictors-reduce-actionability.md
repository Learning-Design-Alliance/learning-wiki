---
type: claim
title: Including demographic variables as predictors can reduce actionability by de-emphasizing correlated actionable risk factors and by discounting intervention effects
description: Including demographic variables as predictors can reduce actionability by de-emphasizing correlated actionable risk factors and by discounting intervention effects
id: demographic-predictors-reduce-actionability
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
sources:
  - id: baker-2023
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619"
    title: "Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S. (2023). Using Demographic Data as Predictor Variables: a Questionable Choice. Journal of Educational Data Mining, 15(2). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619"
    author: "Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S."
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
  - id: baker-2023-2
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619"
    title: "Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S. (2023). Using Demographic Data as Predictor Variables: a Questionable Choice. Journal of Educational Data Mining, 15(2). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619"
    author: "Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S."
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
  - id: baker-2023-3
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619"
    title: "Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S. (2023). Using Demographic Data as Predictor Variables: a Questionable Choice. Journal of Educational Data Mining, 15(2). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619"
    author: "Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S."
    q: 1
    i: "?"
    kind: theoretical
    rigour: 3
---

# Including demographic variables as predictors can reduce actionability by de-emphasizing correlated actionable risk factors and by discounting intervention effects

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · theoretical `r3` · `q1`

## Subclaims
`q1 i?` Including demographic variables can cause models to de-emphasize correlated risk factors more directly aligned with a student's particular needs. [→ Baker 2023](#baker-2023)
`q1 i?` Demographic-variable-based risk predictions risk discounting the impact of interventions because the static demographic factor remains in the model. [→ Baker 2023 (3)](#baker-2023-3)

## Evidence

### Baker 2023

Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S. (2023). Using Demographic Data as Predictor Variables: a Questionable Choice. Journal of Educational Data Mining, 15(2). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619

`q1 · i?` · `theoretical · r3`

Theoretical argument (type e) in section 4.1: because machine learning algorithms de-emphasize variables without added predictive power, "including demographic variables in models can cause the model to de-emphasize correlated risk factors" aligned with student needs, occluding the appropriate intervention.

> "As such, including demographic variables in models can cause the model to de-emphasize correlated risk factors that are more directly aligned with the particular needs of the student – even if the demographic variable achieves only slightly better fit than the correlated variables or achieves worse fit than the correlated variables combined."

### Baker 2023 (2)

Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S. (2023). Using Demographic Data as Predictor Variables: a Questionable Choice. Journal of Educational Data Mining, 15(2). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619

`q1 · i?` · `theoretical · r3`

Supporting real-world observation attributed to Feathers (2022): single demographic variables accounted for "over a quarter of the predictive power of the models" in deployed systems, illustrating the de-emphasis concern.

> "Real-world models that incorporate demographic variables often emphasize those variables over other factors, in cases with single demographic variables accounting for over a quarter of the predictive power of the models (see tables in Feathers, 2022)."

### Baker 2023 (3)

Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S. (2023). Using Demographic Data as Predictor Variables: a Questionable Choice. Journal of Educational Data Mining, 15(2). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619

`q1 · i?` · `theoretical · r3`

The authors argue such a model embeds a form of demographic destiny: it "risks discounting the impact of the intervention" since the static demographic factor stays in the model, actively ignoring progress schools make and obscuring students in the group who still need support.

> "a risk prediction model based on demographic variables risks discounting the impact of the intervention on the student’s graduation risk as it continues to include and make predictions based on the static racial factor."

## Discussion


## Related Claims
- [The argument that excluding demographic predictors amounts to color-blind racism is contested: inclusion can also produce racist decision-making](colorblind-racism-argument-for-inclusion-contested.md) — related
- [Heterogeneity within demographic categories means group variables as predictors can disadvantage atypical group members and underrepresented groups](demographic-category-heterogeneity-harms-atypical-members.md) — related
- [Using demographic variables as predictors risks reinforcing biases embedded in training labels, including self-fulfilling prophecies](demographic-predictors-reinforce-training-label-bias.md) — related
- [In descriptive logit models, demographic variables predict dropout at enrollment (e.g., males have a 60% higher chance of dropping out than females), but most lose significance once first-semester performance data is controlled](logit-demographic-predictors-weaken-after-performance-controls.md) — related
- [Evidence is mixed on whether including demographic variables as predictors improves model performance in educational prediction](mixed-evidence-demographic-predictor-performance.md) — a narrower finding that bears on this claim
- [Using predictive analytics while ignoring teacher knowledge may misidentify students at risk of dropping out and negatively influence teacher views](ignoring-teacher-knowledge-misidentifies-risk-students.md) — related
- [Prior research established correlations between observable student experiences such as frustration and clickstream data in ASSISTments, enabling experience-variable equity research without demographic data](bromp-frustration-clickstream-correlations.md) — related
- [Incorporating more learning activity data reduced the potential bias caused by overreliance on demographic information](learning-activity-data-reduces-demographic-bias.md) — a narrower finding that bears on this claim
