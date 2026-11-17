---
type: claim
title: Engagement, video play proportion and IPI trajectories predict complete course dropout in a MOOC
description: Engagement, video play proportion and IPI trajectories predict complete course dropout in a MOOC
id: trajectories-predict-complete-course-dropout
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: moderate
newest_evidence: 2014
recheck_by: 2017
sources:
  - id: sinha-2014
    resource: "https://doi.org/10.3115/v1/w14-4102"
    title: "Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)"
    author: "Sinha, T., Jermann, P., Li, N., & Dillenbourg, P."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: sinha-2014-2
    resource: "https://doi.org/10.3115/v1/w14-4102"
    title: "Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)"
    author: "Sinha, T., Jermann, P., Li, N., & Dillenbourg, P."
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Engagement, video play proportion and IPI trajectories predict complete course dropout in a MOOC

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Operationalized trajectories of engagement, video play proportion and IPI predict complete course dropout with accuracy 0.80 (kappa 0.57, false negative rate 0.143). [→ Sinha 2014](#sinha-2014)
`q2 i?` Non-dropouts show sustained high trajectories (e.g., IPI=H H H H), while dropouts show declining trajectories (e.g., IPI=H H VL VL VL). [→ Sinha 2014 (2)](#sinha-2014-2)

## Evidence

### Sinha 2014

Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)

`q2 · i?` · `associational · r2`

Course-level dropout experiment spanning "all 48 videos of "Functional Programming in Scala" MOOC (4710 non-dropouts, 9596 dropouts)", using cost-sensitive L2 regularized logistic regression with 5-fold cross validation annotated by student-id on trajectory features.

> "The data for this experiment comes from all 48 videos of "Functional Programming in Scala" MOOC (4710 non-dropouts, 9596 dropouts)."

### Sinha 2014 (2)

Sinha, T., Jermann, P., Li, N., & Dillenbourg, P. (2014). Your click decides your fate: Inferring Information Processing and Attrition Behavior from MOOC Video Clickstream Interactions. [doi:10.3115/v1/w14-4102](https://doi.org/10.3115/v1/w14-4102)

`q2 · i?` · `associational · r2`

Trajectory features (n-grams of engagement, video play proportion and IPI trajectories) achieved accuracy 0.80, kappa 0.57 and false negative rate 0.143; non-dropouts showed trajectories like "trajectory IPI=H H H H, trajectory eng=H H H VL H" while dropout trajectories declined.

> "Operationalized trajectories 0.80 0.57 0.143 Non dropouts (trajectory IPI=H H H H, trajectory eng=H H H VL H, trajectory vpp=H H H L H) Dropouts (trajectory IPI=H H VL VL VL, trajectory eng=H L H L L, trajectory vpp=H H H H VL)"

## Discussion


## Related Claims
- [Clickstream features predict students' next click state while watching MOOC video lectures](clickstream-predicts-next-click-state-mooc.md) — related
- [Across the full course, IPI distinguishes non-dropouts from dropouts and viewers from active students, but does not cleanly separate statement achievers from non-achievers](ipi-full-course-partition-differences.md) — related
- [Greater IPI, increased rewatching and greater video play proportion each associate with lower MOOC dropout hazard](ipi-survival-dropout-hazard.md) — related
- [Average IPI differs significantly across student partitions: high versus low engagers, in-video dropouts versus non-dropouts, course dropouts versus non-dropouts, and Active versus Viewers](ipi-varies-across-student-partitions.md) — related
