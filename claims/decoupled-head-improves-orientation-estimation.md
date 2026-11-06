---
type: claim
title: A decoupled prediction head improves orientation estimation over a coupled head across YOLOv5 and YOLOv11 backbones
description: A decoupled prediction head improves orientation estimation over a coupled head across YOLOv5 and YOLOv11 backbones
id: decoupled-head-improves-orientation-estimation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
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
---

# A decoupled prediction head improves orientation estimation over a coupled head across YOLOv5 and YOLOv11 backbones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Decoupling the head into classification, localization, and orientation branches improved direction estimation accuracy and 5°-range accuracy across all YOLOv5 backbone versions while detection recall stayed unchanged. [→ Chen Yuqing 2025](#chen-yuqing-2025)

## Evidence

### Chen Yuqing 2025

Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei. (2025). A Novel Student Engagement Analysis of Real Classroom Teaching Using Unified Body Orientation Estimation. Sensors (Basel, Switzerland). https://doi.org/10.3390/s25206421

`q2 · i?` · `design · r2`

Ablation comparison of coupled versus decoupled head structures on YOLOv5 architectures, reported from the authors' prior study and extended to YOLOv11. The decoupled model showed "improved direction estimation accuracy" with unchanged recall; Dec-YOLOv11x reached MAE 10.631°. No effect size is printed.

> "the Decoupled-YOLOv5 model showed improved direction estimation accuracy and higher accuracy within the 5° error range across all backbone network versions while maintaining an unchanged detection recall rate."

## Discussion


## Related Claims
- [In authentic classroom videos, students' attention directions are almost consistent with their body orientations, allowing engagement to be inferred non-intrusively](body-orientation-indicates-classroom-attention.md) — related
- [Hard-sample filtering threshold τ = 0.2 and orientation loss weight λ = 0.05 yield the best detection–orientation balance](tau-lambda-ablation-optimal-settings.md) — related
- [The Decoupled-YOLOv11x JointBDOE model reduces orientation MAE to 10.631° and reaches 48.7% accuracy within 5° on the original MEBOW dataset](jointbdoe-decoupled-yolov11x-mebow-performance.md) — related
- [On the reconstructed, more crowded MEBOW dataset, JointBDOE maintains robustness with an MAE of 16.07° and 88.3% accuracy at 30°](jointbdoe-robustness-reconstructed-mebow.md) — related
