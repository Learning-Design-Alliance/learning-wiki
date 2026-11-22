---
type: claim
title: "Rule-based classifiers over SurgGraph scene-graph values achieve 93.8% phase recognition accuracy with per-phase F1 between 0.914 and 0.975, versus SurgVLM's macro-F1 of 0.529"
description: "Rule-based classifiers over SurgGraph scene-graph values achieve 93.8% phase recognition accuracy with per-phase F1 between 0.914 and 0.975, versus SurgVLM's macro-F1 of 0.529"
id: surggraph-phase-recognition-f1
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: jingying-wang-2026
    resource: "https://doi.org/10.1109/icmlt69916.2026.11688499"
    title: "Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang. (2026). SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs. [doi:10.1109/icmlt69916.2026.11688499](https://doi.org/10.1109/icmlt69916.2026.11688499)"
    author: Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Rule-based classifiers over SurgGraph scene-graph values achieve 93.8% phase recognition accuracy with per-phase F1 between 0.914 and 0.975, versus SurgVLM's macro-F1 of 0.529

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the CholecT50 phase-recognition task, SurgGraph achieves 93.8% accuracy vs. SurgVLM's 91.0%, and maintains per-phase F1 between 0.914 and 0.975 across all seven phases while SurgVLM's macro-F1 is 0.529. [→ Jingying Wang 2026](#jingying-wang-2026)

## Evidence

### Jingying Wang 2026

Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang. (2026). SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs. [doi:10.1109/icmlt69916.2026.11688499](https://doi.org/10.1109/icmlt69916.2026.11688499)

`q2 · i?` · `design · r2`

Phase recognition on the CholecT50 test set (1129 frames, 7 phases) using rule-based classifiers with simple threshold comparisons and no learned parameters, so "accuracy reflects the quality of the underlying geometric values". Macro-F1 was 0.943 vs. 0.529.

> "SurgGraph achieves 93.8% vs. SurgVLM's 91.0% on the same test set. Accuracy alone understates the difference: macro-F1 is 0.943 vs. 0.529, because SurgVLM's accuracy is carried by frequent phases while SurgGraph maintains per-phase F1 between 0.914 and 0.975 across all seven phases."

## Discussion


## Related Claims
- [SurgGraph outperforms a re-trained state-of-the-art surgical VLM baseline on tool-action-triplet recognition and Critical View of Safety assessment benchmarks](surggraph-benchmark-accuracy-vs-surgvlm.md) — related
- [SurgGraph's computed relation values are accurate: attachment/occlusion classification reaches a 75.6% lower bound and computed separation matches ground-truth Calot's triangle at average IoU 0.73](surggraph-value-accuracy-lower-bound-iou.md) — related
- [SurgGraph's accuracy is stable over wide ranges around its two calibrated depth thresholds and degrades only at physically implausible settings](surggraph-threshold-sensitivity-stability.md) — related
