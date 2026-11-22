---
type: claim
title: "SurgGraph's computed relation values are accurate: attachment/occlusion classification reaches a 75.6% lower bound and computed separation matches ground-truth Calot's triangle at average IoU 0.73"
description: "SurgGraph's computed relation values are accurate: attachment/occlusion classification reaches a 75.6% lower bound and computed separation matches ground-truth Calot's triangle at average IoU 0.73"
id: surggraph-value-accuracy-lower-bound-iou
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: jingying-wang-2026
    resource: "https://doi.org/10.1109/icmlt69916.2026.11688499"
    title: "Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang. (2026). SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs. [doi:10.1109/icmlt69916.2026.11688499](https://doi.org/10.1109/icmlt69916.2026.11688499)"
    author: Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: jingying-wang-2026-2
    resource: "https://doi.org/10.1109/icmlt69916.2026.11688499"
    title: "Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang. (2026). SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs. [doi:10.1109/icmlt69916.2026.11688499](https://doi.org/10.1109/icmlt69916.2026.11688499)"
    author: Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SurgGraph's computed relation values are accurate: attachment/occlusion classification reaches a 75.6% lower bound and computed separation matches ground-truth Calot's triangle at average IoU 0.73

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Against expert labels on 266 Preparation-phase images (1,133 detected pairs), relation classification achieves 82.2%, yielding a lower bound of 75.6% for attachment/occlusion value accuracy. [→ Jingying Wang 2026](#jingying-wang-2026)
`q2 i?` On 74 EndoVis CVS frames with ground-truth Calot's triangle labels, SurgGraph's computed separation area matches the annotation with average IoU 0.73. [→ Jingying Wang 2026 (2)](#jingying-wang-2026-2)

## Evidence

### Jingying Wang 2026

Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang. (2026). SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs. [doi:10.1109/icmlt69916.2026.11688499](https://doi.org/10.1109/icmlt69916.2026.11688499)

`q2 · i?` · `design · r2`

Expert-labeled evaluation of attachment-vs-occlusion classification on CholecT50 Preparation-phase frames across five tissue pairs (266 images, 1,133 detected pairs); "a lower bound of acclower = 0.92× 0.822 = 75.6%" because values are exact whenever segmentation and classification are both correct.

> "Relation classification achieves 82.2%, yielding a lower bound of acclower = 0.92× 0.822 = 75.6%."

### Jingying Wang 2026 (2)

Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang. (2026). SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs. [doi:10.1109/icmlt69916.2026.11688499](https://doi.org/10.1109/icmlt69916.2026.11688499)

`q2 · i?` · `design · r2`

IoU evaluation of the computed separation gap against ground-truth Calot's triangle labels on 74 benchmark frames; "Average IoU is 0.73". Residual tissue within the gap is included when skeletonization is incomplete, but overall size and trend are well captured.

> "On 74 frames from the EndoVis CVS benchmark [20] with ground-truth Calot's triangle labels, we compute IoU between SurgGraph's separation area (Section 4.1.2) and the ground-truth annotation. Average IoU is 0.73."

## Discussion


## Related Claims
- [Learners report that labeled relation extent, cross-stage image comparison, diverse patient examples, and criteria checklists support surgical learning](learners-value-relation-extent-labels.md) — related
- [SurgGraph outperforms a re-trained state-of-the-art surgical VLM baseline on tool-action-triplet recognition and Critical View of Safety assessment benchmarks](surggraph-benchmark-accuracy-vs-surgvlm.md) — related
- [Rule-based classifiers over SurgGraph scene-graph values achieve 93.8% phase recognition accuracy with per-phase F1 between 0.914 and 0.975, versus SurgVLM's macro-F1 of 0.529](surggraph-phase-recognition-f1.md) — related
- [SurgGraph's accuracy is stable over wide ranges around its two calibrated depth thresholds and degrades only at physically implausible settings](surggraph-threshold-sensitivity-stability.md) — related
