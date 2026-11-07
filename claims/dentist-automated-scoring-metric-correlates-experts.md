---
type: claim
title: "The Dentist automated scoring metric correlates strongly with expert dentists' ratings of root canal access outcomes"
description: "The Dentist automated scoring metric correlates strongly with expert dentists' ratings of root canal access outcomes"
id: dentist-automated-scoring-metric-correlates-experts
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: kaluschke-maximilian-2023
    resource: "https://doi.org/10.1371/journal.pone.0291389"
    title: "Kaluschke Maximilian, Yin Myat Su, Haddawy Peter, Suebnukarn Siriwan, Zachmann Gabriel. (2023). The effect of 3D stereopsis and hand-tool alignment on learning effectiveness and skill transfer of a VR-based simulator for dental training. PLoS One. https://doi.org/10.1371/journal.pone.0291389"
    author: Kaluschke Maximilian, Yin Myat Su, Haddawy Peter, Suebnukarn Siriwan, Zachmann Gabriel
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# The Dentist automated scoring metric correlates strongly with expert dentists' ratings of root canal access outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q3`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q3 i?` The Dentist metric correlates with expert rating with R = 0.85, p < 0.0001, outperforming the best of 24 common classification metrics which reach only approximately −0.65. [→ Kaluschke Maximilian 2023](#kaluschke-maximilian-2023)

## Evidence

### Kaluschke Maximilian 2023

Kaluschke Maximilian, Yin Myat Su, Haddawy Peter, Suebnukarn Siriwan, Zachmann Gabriel. (2023). The effect of 3D stereopsis and hand-tool alignment on learning effectiveness and skill transfer of a VR-based simulator for dental training. PLoS One. https://doi.org/10.1371/journal.pone.0291389

`q3 · i?` · `causal · r2`

Metric validation against expert scores of 20 selected virtual drilling outcomes (experts had κ = 0.89 and ICC = 0.998 reliability); the Dentist metric built from sensitivity and precision achieves R = 0.85, p < 0.0001, with an IBMD of 0.09 versus 0.04–0.21 for an existing scoring method.

> "The correlation of D with the expert rating is of high degree with R = 0.85, p < 0.0001 (see Fig 5). Of the 24 common classification metrics that we evaluated, the best reach a correlation of approx. −0.65."

## Discussion


## Related Claims
- [Pearson correlations between AI and expert scores are weak (all r < 0.3) and statistically non-significant across all five criteria](ai-expert-pearson-weak-nonsignificant.md) — reports the opposite
- [The RCFLA-YOLO model based on YOLOv11m achieves 77.51% precision, 79.03% recall, 78.28% F1-score and 87.89% mAP50 for assessing root canal filling length acceptability on the RCFL dataset](rcfla-yolo-yolov11m-performance-rcfl-dataset.md) — related
- [Calibrated dentist ratings of appliance quality showed good interrater reliability (ICC = 0.826)](good-interrater-reliability-calibrated-dentist-appliance-ratings.md) — related
- [Among YOLOv5, YOLOv8 and YOLOv11 variants trained identically, YOLOv11m achieved the highest mAP50, outperforming the other tested models](yolov11m-highest-map50-among-yolo-variants.md) — related
