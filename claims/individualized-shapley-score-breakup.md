---
type: claim
title: "Individualized Shapley values decompose a learner's predicted score into actionable per-feature contributions"
description: "Individualized Shapley values decompose a learner's predicted score into actionable per-feature contributions"
id: individualized-shapley-score-breakup
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: chintan-donda-sayan-dasgupta-soma-s-dhavala-keyur-faldu-aditi-avasthi-2020
    resource: "https://doi.org/10.48550/arXiv.2010.02629"
    title: "Chintan Donda Sayan Dasgupta Soma S Dhavala Keyur Faldu Aditi Avasthi. (2020). A FRAMEWORK FOR PREDICTING, INTERPRETING, AND IMPROVING LEARNING OUTCOMES. arXiv preprint. [doi:10.48550/arXiv.2010.02629](https://doi.org/10.48550/arXiv.2010.02629)"
    author: Chintan Donda Sayan Dasgupta Soma S Dhavala Keyur Faldu Aditi Avasthi
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Individualized Shapley values decompose a learner's predicted score into actionable per-feature contributions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Per-learner Shapley attributions quantify each feature's contribution to that learner's predicted score, e.g. one user's aq_16 contributed +1.57 points while bq_20 (number of test sessions) reduced the predicted score by 0.73 points. [→ Chintan Donda Sayan Dasgupta Soma S Dhavala Keyur Faldu Aditi Avasthi 2020](#chintan-donda-sayan-dasgupta-soma-s-dhavala-keyur-faldu-aditi-avasthi-2020)

## Evidence

### Chintan Donda Sayan Dasgupta Soma S Dhavala Keyur Faldu Aditi Avasthi 2020

Chintan Donda Sayan Dasgupta Soma S Dhavala Keyur Faldu Aditi Avasthi. (2020). A FRAMEWORK FOR PREDICTING, INTERPRETING, AND IMPROVING LEARNING OUTCOMES. arXiv preprint. [doi:10.48550/arXiv.2010.02629](https://doi.org/10.48550/arXiv.2010.02629)

`q2 · i?` · `design · r2`

Illustrative individual-level attribution for one user, shown as a force-plot in Fig. 8. The article states "aq_16 contributed 1.57 points to the predicted score" while bq_20 reduced it by 0.73 points, possibly because the student should have practiced the test more.

> "a force-plot of individualized Shapley values for a user is shown in Fig. 8. For example, we can see that, aq_16 contributed 1.57 points to the predicted score, whereas bq_20(number of test sessions) reduced predicted score by 0.73 points"

## Discussion


## Related Claims
- [Shapley values from cooperative game theory significantly predict individual learning outcomes, and adding content engagement improves model fit](shapley-values-predict-learning-outcomes.md) — related
- [Local explanations from SHAP and LIME show feature contributions but do not indicate whether a feature value should be increased or decreased to improve the prediction.](local-explanations-lack-directional-guidance.md) — reports the opposite
