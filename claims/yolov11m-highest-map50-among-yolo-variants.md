---
type: claim
title: Among YOLOv5, YOLOv8 and YOLOv11 variants trained identically, YOLOv11m achieved the highest mAP50, outperforming the other tested models
description: Among YOLOv5, YOLOv8 and YOLOv11 variants trained identically, YOLOv11m achieved the highest mAP50, outperforming the other tested models
id: yolov11m-highest-map50-among-yolo-variants
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: ayhan-muhammed-2025
    resource: "https://doi.org/10.1186/s12909-025-07483-2"
    title: "Ayhan Muhammed, Kayadibi İsmail, Aykanat Berkehan. (2025). RCFLA-YOLO: a deep learning-driven framework for the automated assessment of root canal filling quality in periapical radiographs. BMC Medical Education. https://doi.org/10.1186/s12909-025-07483-2"
    author: Ayhan Muhammed, Kayadibi İsmail, Aykanat Berkehan
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Among YOLOv5, YOLOv8 and YOLOv11 variants trained identically, YOLOv11m achieved the highest mAP50, outperforming the other tested models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` YOLOv11m achieved the highest mAP50 (0.8789) among the tested YOLOv5, YOLOv8 and YOLOv11 nano/small/medium/large variants, and yielded the best Precision and mAP50 while ranking slightly lower in Recall and F1-score. [→ Ayhan Muhammed 2025](#ayhan-muhammed-2025)

## Evidence

### Ayhan Muhammed 2025

Ayhan Muhammed, Kayadibi İsmail, Aykanat Berkehan. (2025). RCFLA-YOLO: a deep learning-driven framework for the automated assessment of root canal filling quality in periapical radiographs. BMC Medical Education. https://doi.org/10.1186/s12909-025-07483-2

`q2 · i?` · `design · r2`

Comparative evaluation in the Experiments and results section: YOLOv5, YOLOv8 and YOLOv11 variants were trained with identical hyperparameters (SGD, 300 epochs, batch size 4) and compared on the test subset; the comparison shows YOLOv11m "outperforming the other models" on mAP@50.

> "According to the performance comparison results presented in Table 3 and Fig. 3, the YOLOv11m architecture achieved the highest performance in the mAP@50 metric, with a success rate approaching 88%, outperforming the other models."

## Discussion


## Related Claims
- [On the test set approximately 7.3% of RCFLA-YOLO predictions were false positives and 15.5% false negatives, leading the authors to recommend use as a decision-support tool rather than an independent evaluator](rcfla-yolo-error-rates-decision-support-role.md) — related
- [The RCFLA-YOLO model based on YOLOv11m achieves 77.51% precision, 79.03% recall, 78.28% F1-score and 87.89% mAP50 for assessing root canal filling length acceptability on the RCFL dataset](rcfla-yolo-yolov11m-performance-rcfl-dataset.md) — related
