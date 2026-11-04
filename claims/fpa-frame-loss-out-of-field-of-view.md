---
type: claim
title: "Approximately 29.3% of frames were excluded from object tracking, primarily because target objects were outside the field of view"
description: "Approximately 29.3% of frames were excluded from object tracking, primarily because target objects were outside the field of view"
id: fpa-frame-loss-out-of-field-of-view
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: nozawa-hisataka-2026
    resource: "https://doi.org/10.1097/CCE.0000000000001428"
    title: "Nozawa Hisataka, Kunikata Ayumi, Sakai Yuki, Ouyang Liangyang, Furuta Ryosuke, Sato Yoichi, Matsui Hikoro. (2026). Multiagent First-Person Perspective Analysis for Leadership Assessment in Pediatric Emergency Simulations: A Feasibility Study. Critical Care Explorations. https://doi.org/10.1097/CCE.0000000000001428"
    author: Nozawa Hisataka, Kunikata Ayumi, Sakai Yuki, Ouyang Liangyang, Furuta Ryosuke, Sato Yoichi, Matsui Hikoro
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Approximately 29.3% of frames were excluded from object tracking, primarily because target objects were outside the field of view

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The mean percentage of frames excluded from object tracking was 29.3%, primarily due to target objects being outside the field of view. [→ Nozawa Hisataka 2026](#nozawa-hisataka-2026)

## Evidence

### Nozawa Hisataka 2026

Nozawa Hisataka, Kunikata Ayumi, Sakai Yuki, Ouyang Liangyang, Furuta Ryosuke, Sato Yoichi, Matsui Hikoro. (2026). Multiagent First-Person Perspective Analysis for Leadership Assessment in Pediatric Emergency Simulations: A Feasibility Study. Critical Care Explorations. https://doi.org/10.1097/CCE.0000000000001428

`q2 · i?` · `design · r2`

Results section reports object-of-interest analysis across the two simulations: the "mean frame loss ratio across the two simulations was 29.3%". No frames were excluded due to gaze estimation failures or simultaneous localization and mapping tracking errors.

> "the mean frame loss ratio across the two simulations was 29.3%, accounting for periods where target objects were outside the field of view or undetectable"

## Discussion


## Related Claims
- [Individual computer vision constructs showed notable mean increases and cluster shifts, including sensing the surroundings (26% increase, cluster 4 to 2) and able to detect objects (18% increase, cluster 3 to 1)](individual-cv-construct-shifts-and-mean-increases.md) — related
