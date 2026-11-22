---
type: claim
title: SurgGraph outperforms a re-trained state-of-the-art surgical VLM baseline on tool-action-triplet recognition and Critical View of Safety assessment benchmarks
description: SurgGraph outperforms a re-trained state-of-the-art surgical VLM baseline on tool-action-triplet recognition and Critical View of Safety assessment benchmarks
id: surggraph-benchmark-accuracy-vs-surgvlm
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
  - id: jingying-wang-2026-2
    resource: "https://doi.org/10.1109/icmlt69916.2026.11688499"
    title: "Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang. (2026). SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs. [doi:10.1109/icmlt69916.2026.11688499](https://doi.org/10.1109/icmlt69916.2026.11688499)"
    author: Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# SurgGraph outperforms a re-trained state-of-the-art surgical VLM baseline on tool-action-triplet recognition and Critical View of Safety assessment benchmarks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On the CholecT50 test set, SurgGraph achieves 79.2% exact-match tool-action-triplet recognition accuracy vs. 31.3% for the re-trained SurgVLM, with balanced precision and recall (0.915/0.878) while SurgVLM shows high precision but very low recall. [→ Jingying Wang 2026](#jingying-wang-2026)
`q2 i?` On the EndoVis CVS benchmark, SurgGraph achieves 94.59% overall CVS assessment accuracy vs. 79.4% for the re-trained SurgVLM. [→ Jingying Wang 2026 (2)](#jingying-wang-2026-2)

## Evidence

### Jingying Wang 2026

Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang. (2026). SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs. [doi:10.1109/icmlt69916.2026.11688499](https://doi.org/10.1109/icmlt69916.2026.11688499)

`q2 · i?` · `design · r2`

Benchmark evaluation on the CholecT50 test set (1129 frames, 5 videos) using exact-match scoring against a re-trained SurgVLM reimplementation; "SurgGraph achieves 79.2%, vs. 31.3% for the re-trained SurgVLM". The paper reports SurgVLM precision 0.984 but recall 0.273.

> "SurgGraph achieves 79.2%, vs. 31.3% for the re-trained SurgVLM, a 2.5 × advantage."

### Jingying Wang 2026 (2)

Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang. (2026). SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs. [doi:10.1109/icmlt69916.2026.11688499](https://doi.org/10.1109/icmlt69916.2026.11688499)

`q2 · i?` · `design · r2`

Frame-level CVS assessment on the EndoVis CVS benchmark (2,250 frames, 10 videos), mapping each of three CVS criteria to a scene-graph relation. The article reports "94.59% overall, vs. the re-trained SurgVLM's ... 79.4%" and notes overall accuracy can exceed per-criterion accuracy because CVS is conjunctive.

> "SurgGraph achieves 91.8% on C1, 90.5% on C2, 77.0% on C3, and 94.59% overall, vs. the re-trained SurgVLM's 89.4%, 81.3%, 76.5%, and 79.4%.."

## Discussion


## Related Claims
- [Rule-based classifiers over SurgGraph scene-graph values achieve 93.8% phase recognition accuracy with per-phase F1 between 0.914 and 0.975, versus SurgVLM's macro-F1 of 0.529](surggraph-phase-recognition-f1.md) — related
- [SurgGraph's computed relation values are accurate: attachment/occlusion classification reaches a 75.6% lower bound and computed separation matches ground-truth Calot's triangle at average IoU 0.73](surggraph-value-accuracy-lower-bound-iou.md) — related
- [AI-based assessment systems show strong internal performance and early real-time deployment for critical view of safety detection, but lack external validation and clinical impact evidence](ai-lc-assessment-strong-internal-weak-external.md) — related
