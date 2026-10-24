---
type: claim
title: CFS and GR feature selection shrink decision trees to 3.2-4.7 leaf nodes without degrading predictive performance
description: CFS and GR feature selection shrink decision trees to 3.2-4.7 leaf nodes without degrading predictive performance
id: feature-selection-reduces-tree-size-maintains-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: vincent-zhang-2025
    resource: "https://doi.org/10.1007/s40593-025-00510-9"
    title: "Vincent Zhang, Bryn Jeffries, Irena Koprinska. (2025). A Machine Learning Approach for Predicting Student Progress in Online Programming Education. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00510-9"
    author: Vincent Zhang, Bryn Jeffries, Irena Koprinska
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# CFS and GR feature selection shrink decision trees to 3.2-4.7 leaf nodes without degrading predictive performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Compared with trees without feature selection (6.1-13.9 leaf nodes on average), CFS and GR reduced leaf nodes to 3.4-4.7 and 3.2-4.1 without degrading performance. [→ Vincent Zhang 2025](#vincent-zhang-2025)

## Evidence

### Vincent Zhang 2025

Vincent Zhang, Bryn Jeffries, Irena Koprinska. (2025). A Machine Learning Approach for Predicting Student Progress in Online Programming Education. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00510-9

`q2 · i?` · `associational · r2`

Results across the four courses comparing DT, DT+CFS and DT+GR. The article reports that feature selection produced "a much smaller and more interpretable tree with less paths" and in some cases even improved performance.

> "Compared to the decision trees without feature selection, which had on average 6.1–13.9 leaf nodes, using the CFS and GR feature selection methods reduced the number of leaf nodes to 3.4–4.7 and 3.2–4.1 without degrading performance (Table 6)."

## Discussion


## Related Claims
- [Decision tree classifiers trained on slide interaction features predict end-of-module outcomes with high accuracy across four K-12 programming courses](dt-slide-interaction-features-predict-module-outcomes.md) — related
- [Completion of prior problem slides is the most critical predictor of completing a module's final exercise, consistent with the doer effect](problem-slide-completion-top-predictor-doer-effect.md) — related
- [Decision trees achieve competitive accuracy with black-box models (LR, RF, SVM), which performed slightly better but lack interpretability](dt-competitive-with-black-box-classifiers.md) — related
