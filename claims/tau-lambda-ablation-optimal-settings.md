---
type: claim
title: Hard-sample filtering threshold τ = 0.2 and orientation loss weight λ = 0.05 yield the best detection–orientation balance
description: Hard-sample filtering threshold τ = 0.2 and orientation loss weight λ = 0.05 yield the best detection–orientation balance
id: tau-lambda-ablation-optimal-settings
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: chen-yuqing-2025
    resource: "https://doi.org/10.3390/s25206421"
    title: "Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei. (2025). A Novel Student Engagement Analysis of Real Classroom Teaching Using Unified Body Orientation Estimation. Sensors (Basel, Switzerland). https://doi.org/10.3390/s25206421"
    author: Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: chen-yuqing-2025-2
    resource: "https://doi.org/10.3390/s25206421"
    title: "Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei. (2025). A Novel Student Engagement Analysis of Real Classroom Teaching Using Unified Body Orientation Estimation. Sensors (Basel, Switzerland). https://doi.org/10.3390/s25206421"
    author: Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Hard-sample filtering threshold τ = 0.2 and orientation loss weight λ = 0.05 yield the best detection–orientation balance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In hyperparameter ablations, the lowest MAE occurred at τ = 0.2, and λ = 0.05 was determined to achieve the optimal balance between human detection and orientation estimation tasks. [→ Chen Yuqing 2025](#chen-yuqing-2025)
`q2 i?` Under identical settings (τ = 0.2, λ = 0.05), the YOLOv11 backbone outperformed YOLOv5, which the authors read as generalization across backbones. [→ Chen Yuqing 2025 (2)](#chen-yuqing-2025-2)

## Evidence

### Chen Yuqing 2025

Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei. (2025). A Novel Student Engagement Analysis of Real Classroom Teaching Using Unified Body Orientation Estimation. Sensors (Basel, Switzerland). https://doi.org/10.3390/s25206421

`q2 · i?` · `design · r2`

Ablation study sweeping τ in [0.1, 0.4] at 0.1 intervals with λ fixed at 0.1, on YOLOv5s and YOLOv11s backbones (Table 1). The lowest MAE was "achieved when τ was set to 0.2". No effect size is printed.

> "The experimental results indicate that the lowest MAE value was achieved when τ was set to 0.2, demonstrating the importance of reasonable hard-sample filtering."

### Chen Yuqing 2025 (2)

Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei. (2025). A Novel Student Engagement Analysis of Real Classroom Teaching Using Unified Body Orientation Estimation. Sensors (Basel, Switzerland). https://doi.org/10.3390/s25206421

`q2 · i?` · `design · r2`

Backbone comparison at the selected hyperparameters in the same ablation (Table 1). The article reports the YOLOv11 backbone "exhibits superior performance" under identical conditions, indicating the method is not limited to a specific backbone. No effect size is printed.

> "The results (Table 1) show that under identical conditions (τ= 0.2, λ= 0.05), the YOLOv11 backbone network exhibits superior performance."

## Discussion


## Related Claims
- [In authentic classroom videos, students' attention directions are almost consistent with their body orientations, allowing engagement to be inferred non-intrusively](body-orientation-indicates-classroom-attention.md) — related
- [A decoupled prediction head improves orientation estimation over a coupled head across YOLOv5 and YOLOv11 backbones](decoupled-head-improves-orientation-estimation.md) — related
- [KL-divergence and binary cross-entropy losses for course prediction yield grade prediction within 1-2% of each other](kl-versus-bce-loss-ablation.md) — related
