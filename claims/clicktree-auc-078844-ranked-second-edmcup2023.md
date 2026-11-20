---
type: claim
title: The ClickTree method achieved an AUC of 0.78844 on test data and ranked second in the EDM Cup 2023.
description: The ClickTree method achieved an AUC of 0.78844 on test data and ranked second in the EDM Cup 2023.
id: clicktree-auc-078844-ranked-second-edmcup2023
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
evidence_strength: moderate
newest_evidence: 2024
recheck_by: 2027
sources:
  - id: rohani-2024
    resource: "https://doi.org/10.48550/arXiv.2403.14664"
    title: "Rohani, N., Rohani, B., & Manataki, A. (2024). ClickTree: A Tree-based Method for Predicting Math Students' Performance Based on Clickstream Data. [doi:10.48550/arXiv.2403.14664](https://doi.org/10.48550/arXiv.2403.14664)"
    author: "Rohani, N., Rohani, B., & Manataki, A."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The ClickTree method achieved an AUC of 0.78844 on test data and ranked second in the EDM Cup 2023.

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2024 · not yet checked against its sources · not reviewed by a person · recheck by 2027: tool and model accuracy changes quickly

## Subclaims
`q2 i?` ClickTree predicted end-unit assignment problem scores with an AUC of 0.78844 on test data, ranking second in the EDM Cup 2023. [→ Rohani 2024](#rohani-2024)

## Evidence

### Rohani 2024

Rohani, N., Rohani, B., & Manataki, A. (2024). ClickTree: A Tree-based Method for Predicting Math Students' Performance Based on Clickstream Data. [doi:10.48550/arXiv.2403.14664](https://doi.org/10.48550/arXiv.2403.14664)

`q2 · i?` · `design · r2`

Evaluation of the CatBoost-based ClickTree predictor on the competition test set of ASSISTments clickstream data. The article reports that the method "achieved an AUC of 0.78844" and "ranked second in the EDM Cup 2023"; no effect size is printed, so impact is coded i? (no magnitude reported; not a null effect).

> "The ClickTree method achieved an AUC of 0.78844 on the test data and ranked second in the EDM Cup 2023."

## Discussion


## Related Claims
- [The proposed Transformer-based framework achieved first place in the EDM Cup 2023 with an AUC of 78.969% on the private evaluation dataset](transformer-kt-first-place-edm-cup-2023.md) — reports the opposite
- [Rank-averaged ensembling stabilized predictions but did not outperform the single base model](ensemble-stabilizes-but-not-better-than-model1.md) — related
- [ClickTree with the CatBoost classifier achieved higher validation AUC than Random Forest, Decision Tree and Logistic Regression on the same features.](catboost-outperformed-rf-dt-lr-validation-auc.md) — related
- [The most important feature for the ClickTree model was sequence folder path level 3, representing the subject of the assignment problem.](sequence-folder-path-level-3-most-important-feature.md) — related
