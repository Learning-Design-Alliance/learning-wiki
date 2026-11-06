---
type: claim
title: "The RCFLA-YOLO model based on YOLOv11m achieves 77.51% precision, 79.03% recall, 78.28% F1-score and 87.89% mAP50 for assessing root canal filling length acceptability on the RCFL dataset"
description: "The RCFLA-YOLO model based on YOLOv11m achieves 77.51% precision, 79.03% recall, 78.28% F1-score and 87.89% mAP50 for assessing root canal filling length acceptability on the RCFL dataset"
id: rcfla-yolo-yolov11m-performance-rcfl-dataset
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

# The RCFLA-YOLO model based on YOLOv11m achieves 77.51% precision, 79.03% recall, 78.28% F1-score and 87.89% mAP50 for assessing root canal filling length acceptability on the RCFL dataset

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` A YOLOv11m-based object detection model evaluated on a 735-periapical-radiograph dataset of student root canal fillings reached 87.89% mAP50, with precision of 77.51%, recall of 79.03% and F1-score of 78.28%. [→ Ayhan Muhammed 2025](#ayhan-muhammed-2025)

## Evidence

### Ayhan Muhammed 2025

Ayhan Muhammed, Kayadibi İsmail, Aykanat Berkehan. (2025). RCFLA-YOLO: a deep learning-driven framework for the automated assessment of root canal filling quality in periapical radiographs. BMC Medical Education. https://doi.org/10.1186/s12909-025-07483-2

`q2 · i?` · `design · r2`

Performance evaluation of object detection models trained on the RCFL dataset of student-performed root canal fillings, tested on an 80-image test subset with confusion-matrix metrics; the article reports "77.51% precision, 79.03% recall, 78.28% F1-score, and 87.89% mAP50". No standardized effect size is printed.

> "Performance evaluations conducted on the RCFL dataset demonstrated that among the tested models, the YOLOv11m architecture achieved the highest performance, with 77.51% precision, 79.03% recall, 78.28% F1-score, and 87.89% mAP50."

## Discussion


## Related Claims
- [On the test set approximately 7.3% of RCFLA-YOLO predictions were false positives and 15.5% false negatives, leading the authors to recommend use as a decision-support tool rather than an independent evaluator](rcfla-yolo-error-rates-decision-support-role.md) — related
- [Among YOLOv5, YOLOv8 and YOLOv11 variants trained identically, YOLOv11m achieved the highest mAP50, outperforming the other tested models](yolov11m-highest-map50-among-yolo-variants.md) — related
- [In preclinical root canal treatment on extracted premolars, 84% achieved optimum working length, 74% optimum master cone fit, and procedural errors occurred in 23.5% of cases with ledge formation most common at 14%](preclinical-rct-error-and-quality-frequencies.md) — related
