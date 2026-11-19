---
type: claim
title: "Random forest models of the rubric-based admissions decisions were only weakly predictive, with the full-rubric model's AUC (0.67) below the old-system model's (0.76)"
description: "Random forest models of the rubric-based admissions decisions were only weakly predictive, with the full-rubric model's AUC (0.67) below the old-system model's (0.76)"
id: rubric-model-auc-below-old-system-model
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: weissman-2023
    resource: "https://doi.org/10.1103/physrevphyseducres.19.028001"
    title: "Weissman, M. B. (2023). Comment on \"Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics\". Department of Physics, University of Illinois at Urbana-Champaign. [doi:10.1103/physrevphyseducres.19.028001](https://doi.org/10.1103/physrevphyseducres.19.028001)"
    author: Weissman, M. B.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
  - id: weissman-2023-2
    resource: "https://doi.org/10.1103/physrevphyseducres.19.028001"
    title: "Weissman, M. B. (2023). Comment on \"Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics\". Department of Physics, University of Illinois at Urbana-Champaign. [doi:10.1103/physrevphyseducres.19.028001](https://doi.org/10.1103/physrevphyseducres.19.028001)"
    author: Weissman, M. B.
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# Random forest models of the rubric-based admissions decisions were only weakly predictive, with the full-rubric model's AUC (0.67) below the old-system model's (0.76)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A random forest model using the complete set of rubric ratings achieved a testing AUC of 0.67, lower than the 0.76 achieved by a model of the old system using limited unprocessed inputs. [→ Weissman 2023](#weissman-2023)
`q2 i?` Even after removal of borderline cases, the testing AUC only rose to 0.70, which the comment takes to indicate important factors outside the official rubrics influenced decisions. [→ Weissman 2023 (2)](#weissman-2023-2)

## Evidence

### Weissman 2023

Weissman, M. B. (2023). Comment on "Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics". Department of Physics, University of Illinois at Urbana-Champaign. [doi:10.1103/physrevphyseducres.19.028001](https://doi.org/10.1103/physrevphyseducres.19.028001)

`q2 · i?` · `associational · r2`

Modeling analysis of the original study's admissions data, comparing a random forest trained on the committee's rubric ratings against one trained on the old system's raw metrics. The comment reports AUC 0.67 versus 0.76 on test samples.

> "the random-forest model based on these detailed metrics as evaluated and used by the admissions committee only increased the testing AUC of the rubric model to 0.67, even lower than the 0.76 for a model that used only limited unprocessed input data for the old system."

### Weissman 2023 (2)

Weissman, M. B. (2023). Comment on "Rubric-based holistic review represents a change from traditional graduate admissions approaches in physics". Department of Physics, University of Illinois at Urbana-Champaign. [doi:10.1103/physrevphyseducres.19.028001](https://doi.org/10.1103/physrevphyseducres.19.028001)

`q2 · i?` · `theoretical · r3`

The comment's interpretation of the original study's edited-data model. It infers that factors beyond the rubrics, such as demographic considerations not recorded due to Michigan law, shaped decisions.

> "Since even after removal of borderline cases the testing AUC only rose to 0.70 (1), the outside-the-rubric factors must have been quite important, changing decisions from those predicted by rubric-informed models even in non-borderline cases."

## Discussion


## Related Claims
- [A conditional inference forest acceptably models pre-rubric physics graduate admissions decisions, with physics GRE score, quantitative GRE score, and undergraduate GPA the only meaningful features](pre-rubric-admissions-model-quantitative-metrics-meaningful.md) — related
- [After rubric implementation, admissions decisions from application data could not be acceptably modeled, even with hyperparameter tuning](post-rubric-application-data-unmodelable.md) — related
- [Models built from faculty rubric ratings also failed to reach acceptable predictive performance, with physics GRE score and quality of work the meaningful features](rubric-rating-data-unmodelable.md) — related
