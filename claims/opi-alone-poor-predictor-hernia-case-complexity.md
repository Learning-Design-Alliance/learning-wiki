---
type: claim
title: Objective performance indicators alone poorly predict robotic ventral hernia case complexity compared with clinical factors (F1 0.58 vs 0.87)
description: Objective performance indicators alone poorly predict robotic ventral hernia case complexity compared with clinical factors (F1 0.58 vs 0.87)
id: opi-alone-poor-predictor-hernia-case-complexity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: shin-th-2025
    resource: "https://doi.org/10.1007/s00464-025-12412-x"
    title: "Shin TH, Fanta A, Gokcal F, Shields M, Benlice C, Kudsi OY. (2025). Decoding surgical proficiency and complexity: a machine learning framework for robotic herniorrhaphy. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12412-x"
    author: Shin TH, Fanta A, Gokcal F, Shields M, Benlice C, Kudsi OY
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Objective performance indicators alone poorly predict robotic ventral hernia case complexity compared with clinical factors (F1 0.58 vs 0.87)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In iterative ensemble machine learning models on 468 robotic ventral hernia repairs, CatBoost using both clinical and OPI covariates achieved the best F1 score of 0.87, clinical factors only 0.85, and OPI metrics only the worst at 0.58. [→ Shin TH 2025](#shin-th-2025)

## Evidence

### Shin TH 2025

Shin TH, Fanta A, Gokcal F, Shields M, Benlice C, Kudsi OY. (2025). Decoding surgical proficiency and complexity: a machine learning framework for robotic herniorrhaphy. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12412-x

`q2 · i?` · `associational · r2`

Results of iterative ensemble machine learning (CatBoost, Random Forest, XGBoost, and others with fivefold cross-validation) on 468 cases. OPI-only models were worst: "CatBoost models with OPI metrics only performed the worst with an F1 score of 0.58". No effect size is printed.

> "CatBoost models using both clinical and OPI covariates performed the best, with F1 score of 0.87, followed by CatBoost using clinical factors only with F1 score of 0.85 (Fig. 1B). CatBoost models with OPI metrics only performed the worst with an F1 score of 0.58"

## Discussion


## Related Claims
- [OPIs did not predict case complexity with high fidelity for either attending or non-attending primary surgeons](opi-prediction-attending-versus-trainee.md) — possibly the same claim (merge candidate)
- [Segmenting the surgeon's experience into Novice and Expert phases did not improve OPI-based prediction of case complexity](skill-segmentation-no-prediction-gain.md) — related
