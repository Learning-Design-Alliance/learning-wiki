---
type: claim
title: "SurgGraph's accuracy is stable over wide ranges around its two calibrated depth thresholds and degrades only at physically implausible settings"
description: "SurgGraph's accuracy is stable over wide ranges around its two calibrated depth thresholds and degrades only at physically implausible settings"
id: surggraph-threshold-sensitivity-stability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
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

# SurgGraph's accuracy is stable over wide ranges around its two calibrated depth thresholds and degrades only at physically implausible settings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Accuracy for attachment/occlusion classification stays within four points of the optimum (89.7% at τ=0.034) across τ in [0.02, 0.04] and above 78% across [0.005, 0.05]; the chosen τ=0.01 yields 82.2%. [→ Jingying Wang 2026](#jingying-wang-2026)

## Evidence

### Jingying Wang 2026

Jingying Wang, Rosiana Natalie, Marquise D Singleterry, Filippos Bellos, Brian George, Gurjit Sandhu, Jason J Corso, Anhong Guo, Vitaliy Popov, Xu Wang. (2026). SurgGraph: Quantitative Laparoscopic Video Understanding via Geometry-Grounded Scene Graphs. [doi:10.1109/icmlt69916.2026.11688499](https://doi.org/10.1109/icmlt69916.2026.11688499)

`q2 · i?` · `design · r2`

Threshold-sensitivity sweep against expert annotations (tissue-pair relation labels for τ), holding everything else fixed (Figure 7). "the chosen𝜏= 0.01 yields 82.2%"; accuracy degrades only where the threshold becomes physically implausible relative to the depth model's noise floor.

> "For𝜏, accuracy stays within four points of the optimum (89.7% at𝜏= 0.034) across the range[0.02, 0.04], and remains above 78% across a full order of magnitude[0.005, 0.05]; the chosen𝜏= 0.01 yields 82.2%."

## Discussion


## Related Claims
- [Diagnostic model performance remains relatively stable across moderate hyperparameter ranges, with 8 attention heads and a 512 hidden dimension yielding optimal results](hyperparameter-stability-oral-diagnostic-model.md) — a broader claim this one bears on
- [SurgGraph's computed relation values are accurate: attachment/occlusion classification reaches a 75.6% lower bound and computed separation matches ground-truth Calot's triangle at average IoU 0.73](surggraph-value-accuracy-lower-bound-iou.md) — related
- [Rule-based classifiers over SurgGraph scene-graph values achieve 93.8% phase recognition accuracy with per-phase F1 between 0.914 and 0.975, versus SurgVLM's macro-F1 of 0.529](surggraph-phase-recognition-f1.md) — related
