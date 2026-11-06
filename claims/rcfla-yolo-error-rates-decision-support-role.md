---
type: claim
title: "On the test set approximately 7.3% of RCFLA-YOLO predictions were false positives and 15.5% false negatives, leading the authors to recommend use as a decision-support tool rather than an independent evaluator"
description: "On the test set approximately 7.3% of RCFLA-YOLO predictions were false positives and 15.5% false negatives, leading the authors to recommend use as a decision-support tool rather than an independent evaluator"
id: rcfla-yolo-error-rates-decision-support-role
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

# On the test set approximately 7.3% of RCFLA-YOLO predictions were false positives and 15.5% false negatives, leading the authors to recommend use as a decision-support tool rather than an independent evaluator

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Quantitative error analysis of the model's test-set predictions found about 7.3% false positives and 15.5% false negatives; the authors conclude the system is more appropriately a decision-support tool than an independent evaluator. [→ Ayhan Muhammed 2025](#ayhan-muhammed-2025)

## Evidence

### Ayhan Muhammed 2025

Ayhan Muhammed, Kayadibi İsmail, Aykanat Berkehan. (2025). RCFLA-YOLO: a deep learning-driven framework for the automated assessment of root canal filling quality in periapical radiographs. BMC Medical Education. https://doi.org/10.1186/s12909-025-07483-2

`q2 · i?` · `design · r2`

Error analysis of YOLOv11m predictions on the RCFL test subset reported in the Discussion; the article prints "approximately 7.3% of the predictions were false positives, while 15.5% were false negatives" and frames the educational implication of these error rates.

> "Quantitative error analysis on the test set indicated that approximately 7.3% of the predictions were false positives, while 15.5% were false negatives."

## Discussion


## Related Claims
- [The RCFLA-YOLO model based on YOLOv11m achieves 77.51% precision, 79.03% recall, 78.28% F1-score and 87.89% mAP50 for assessing root canal filling length acceptability on the RCFL dataset](rcfla-yolo-yolov11m-performance-rcfl-dataset.md) — related
- [Among YOLOv5, YOLOv8 and YOLOv11 variants trained identically, YOLOv11m achieved the highest mAP50, outperforming the other tested models](yolov11m-highest-map50-among-yolo-variants.md) — related
