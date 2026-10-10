---
type: claim
title: Evidence is mixed on whether including demographic variables as predictors improves model performance in educational prediction
description: Evidence is mixed on whether including demographic variables as predictors improves model performance in educational prediction
id: mixed-evidence-demographic-predictor-performance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: mixed
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

# Evidence is mixed on whether including demographic variables as predictors improves model performance in educational prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · theoretical `r3` · `q1`

## Subclaims
`q1 i?` Some studies find models including race perform substantially better, while others find worse performance or no significant advantage from including demographic variables. [→ Baker 2023](#baker-2023)
`q1 i?` The authors conclude it is unclear whether including demographic variables generally leads to better model performance. [→ Baker 2023 (3)](#baker-2023-3)

## Evidence

### Baker 2023

Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S. (2023). Using Demographic Data as Predictor Variables: a Questionable Choice. Journal of Educational Data Mining, 15(2). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619

`q1 · i?` · `theoretical · r3`

The article reports, citing Kleinberg et al. (2018), that in models predicting college GPA, "models that take race into account perform substantially better" than models that do not. This is a second-hand reported finding, not a study read here.

> "For example, Kleinberg et al. (2018) investigates this question in the context of models predicting college GPA, comparing models that take race into account to models that do not take race into account. They find that models that take race into account perform substantially better."

### Baker 2023 (2)

Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S. (2023). Using Demographic Data as Predictor Variables: a Questionable Choice. Journal of Educational Data Mining, 15(2). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619

`q1 · i?` · `theoretical · r3`

The article reports, citing Yu et al. (2021), "no significant advantages by including a range of demographic variables" in college dropout prediction across performance, disadvantaged-student performance, and fairness metrics. Second-hand reported null result.

> "Yu and colleagues (2021) find no significant advantages by including a range of demographic variables in a model of college dropout, either in terms of overall model performance, performance for historically disadvantaged students, or fairness metrics."

### Baker 2023 (3)

Baker, R. S., Esbenshade, L., Vitale, J., & Karumbaiah, S. (2023). Using Demographic Data as Predictor Variables: a Questionable Choice. Journal of Educational Data Mining, 15(2). https://jedm.educationaldatamining.org/index.php/JEDM/article/view/619

`q1 · i?` · `theoretical · r3`

The authors' own synthesis of the conflicting findings: "it is unclear whether including demographic variables generally leads to better model performance". They note Yu et al. had a much broader feature set than Kleinberg et al., and call the question empirical, requiring further research and meta-analyses.

> "As such, it appears that it is unclear whether including demographic variables generally leads to better model performance, despite the strong intuitive appeal of such a notion."

## Discussion


## Related Claims
- [The argument that excluding demographic predictors amounts to color-blind racism is contested: inclusion can also produce racist decision-making](colorblind-racism-argument-for-inclusion-contested.md) — related
- [Heterogeneity within demographic categories means group variables as predictors can disadvantage atypical group members and underrepresented groups](demographic-category-heterogeneity-harms-atypical-members.md) — related
- [Using demographic variables as predictors risks reinforcing biases embedded in training labels, including self-fulfilling prophecies](demographic-predictors-reinforce-training-label-bias.md) — a broader claim this one bears on
- [Including demographic variables as predictors can reduce actionability by de-emphasizing correlated actionable risk factors and by discounting intervention effects](demographic-predictors-reduce-actionability.md) — a broader claim this one bears on
- [In descriptive logit models, demographic variables predict dropout at enrollment (e.g., males have a 60% higher chance of dropping out than females), but most lose significance once first-semester performance data is controlled](logit-demographic-predictors-weaken-after-performance-controls.md) — related
- [The working paper examines the sensitivity and precision of teacher value-added estimates under specifications differing in student-level, peer-level, and double-lagged achievement controls](vam-sensitivity-student-peer-controls-examined.md) — related
- [Early-stage performance data is particularly important for predicting attrition, while demographic data has limited predictive value once performance data is available](performance-data-dominates-demographics-in-dropout-prediction.md) — related
- [Using predictive analytics while ignoring teacher knowledge may misidentify students at risk of dropping out and negatively influence teacher views](ignoring-teacher-knowledge-misidentifies-risk-students.md) — related
- [Fairness of AI outputs remains under-evaluated in edtech research](ai-output-fairness-under-evaluated-edtech.md) — related
- [Removing the sensitive race feature caused little impact on predictive performance at Stage 1 and no significant fairness differences, with mixed fairness effects](removing-race-feature-little-performance-impact.md) — a narrower finding that bears on this claim
- [Predictive learning analytics can generate early warnings of dropout risk and trigger targeted interventions in adult education](predictive-analytics-early-warning-dropout-adults.md) — related
