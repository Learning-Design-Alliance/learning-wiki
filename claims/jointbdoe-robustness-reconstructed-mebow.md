---
type: claim
title: "On the reconstructed, more crowded MEBOW dataset, JointBDOE maintains robustness with an MAE of 16.07° and 88.3% accuracy at 30°"
description: "On the reconstructed, more crowded MEBOW dataset, JointBDOE maintains robustness with an MAE of 16.07° and 88.3% accuracy at 30°"
id: jointbdoe-robustness-reconstructed-mebow
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

# On the reconstructed, more crowded MEBOW dataset, JointBDOE maintains robustness with an MAE of 16.07° and 88.3% accuracy at 30°

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` When evaluated on the reconstructed MEBOW dataset containing severe occlusion and low-resolution samples, JointBDOE's Dec-YOLOv11x variant reached an MAE of 16.074° and 88.3% accuracy at 30°, degrading from original-dataset performance. [→ Chen Yuqing 2025](#chen-yuqing-2025)

## Evidence

### Chen Yuqing 2025

Chen Yuqing, Li Jiawen, Liu Yixin, Jiang Fei. (2025). A Novel Student Engagement Analysis of Real Classroom Teaching Using Unified Body Orientation Estimation. Sensors (Basel, Switzerland). https://doi.org/10.3390/s25206421

`q2 · i?` · `design · r2`

Numerical evaluation on the reconstructed MEBOW dataset (225,912 human instances), which adds restored challenging COCO instances with pseudo-orientation labels. The article states JointBDOE "maintains strong robustness" with MAE 16.07° and 88.3% accuracy at 30°; Table 3 lists Dec-YOLOv11x at 16.074° MAE. No effect size is printed.

> "With the more challenging reconstructed MEBOW dataset, JointBDOE maintains strong robustness with an MAE of 16.07° and an orientation accuracy of 88.3% at 30°."

## Discussion


## Related Claims
- [JointBDOE achieves accuracy comparable to MEBOW at faster processing speed under the same baseline detection framework](jointbdoe-comparable-accuracy-faster-speed.md) — a broader claim this one bears on
- [The Decoupled-YOLOv11x JointBDOE model reduces orientation MAE to 10.631° and reaches 48.7% accuracy within 5° on the original MEBOW dataset](jointbdoe-decoupled-yolov11x-mebow-performance.md) — related
- [A decoupled prediction head improves orientation estimation over a coupled head across YOLOv5 and YOLOv11 backbones](decoupled-head-improves-orientation-estimation.md) — related
