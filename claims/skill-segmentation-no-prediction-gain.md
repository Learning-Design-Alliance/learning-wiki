---
type: claim
title: "Segmenting the surgeon's experience into Novice and Expert phases did not improve OPI-based prediction of case complexity"
description: "Segmenting the surgeon's experience into Novice and Expert phases did not improve OPI-based prediction of case complexity"
id: skill-segmentation-no-prediction-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: weak
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

# Segmenting the surgeon's experience into Novice and Expert phases did not improve OPI-based prediction of case complexity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` After eigendecomposition and convex hull analyses identified a Novice-to-Expert transition at 4/30/2017, re-running ensemble models with skill segmentation did not significantly improve OPIs' ability to independently predict case complexity (F1 0.59). [→ Shin TH 2025](#shin-th-2025)

## Evidence

### Shin TH 2025

Shin TH, Fanta A, Gokcal F, Shields M, Benlice C, Kudsi OY. (2025). Decoding surgical proficiency and complexity: a machine learning framework for robotic herniorrhaphy. Surgical Endoscopy. https://doi.org/10.1007/s00464-025-12412-x

`q2 · i?` · `associational · r2`

Sensitivity analysis on attending-surgeon cases: exponential decay fits on eigendecomposition and convex hull of OPI Euclidean distances defined a 4/30/2017 Novice/Expert transition; segmented models were re-run. "skill segmentation did not significantly improve OPI ability to independently predict case complexity". No effect size printed.

> "This sensitivity analysis revealed that skill segmentation did not significantly improve OPI ability to independently predict case complexity (F1 score 0.59; Fig. 5B)."

## Discussion


## Related Claims
- [Objective performance indicators alone poorly predict robotic ventral hernia case complexity compared with clinical factors (F1 0.58 vs 0.87)](opi-alone-poor-predictor-hernia-case-complexity.md) — related
- [OPI-derived learning curves stabilize within the first 10 months of a surgeon's experience despite increasing case complexity](opi-learning-curve-stabilizes-ten-months.md) — related
- [OPIs did not predict case complexity with high fidelity for either attending or non-attending primary surgeons](opi-prediction-attending-versus-trainee.md) — related
