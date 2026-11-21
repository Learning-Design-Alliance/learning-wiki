---
type: claim
title: "VLab-HV's Light version maintains 30 fps on low-end systems with 8 GB RAM and integrated GPUs"
description: "VLab-HV's Light version maintains 30 fps on low-end systems with 8 GB RAM and integrated GPUs"
id: vlab-hv-light-version-30fps-low-end
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
sources:
  - id: pliuhin-2025
    resource: "https://doi.org/10.48550/arXiv.2511.20919"
    title: "Pliuhin, V., Tsegelnyk, Y., Sukhonos, M., Biletskyi, I., Plankovskyy, S., and Sakhoshko, T. (2025). Virtual High Voltage Lab: Gamified Learning in a Safe 3D Environment. O.M. Beketov National University of Urban Economy in Kharkiv. Originally published 2024. [doi:10.48550/arXiv.2511.20919](https://doi.org/10.48550/arXiv.2511.20919)"
    author: Pliuhin, V., Tsegelnyk, Y., Sukhonos, M., Biletskyi, I., Plankovskyy, S., and Sakhoshko, T.
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# VLab-HV's Light version maintains 30 fps on low-end systems with 8 GB RAM and integrated GPUs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` The optimized Light version of VLab-HV runs at a minimum of 30 fps on low-end hardware (8 GB RAM, integrated GPUs), using LOD and dynamic resolution scaling. [→ Pliuhin 2025](#pliuhin-2025)

## Evidence

### Pliuhin 2025

Pliuhin, V., Tsegelnyk, Y., Sukhonos, M., Biletskyi, I., Plankovskyy, S., and Sakhoshko, T. (2025). Virtual High Voltage Lab: Gamified Learning in a Safe 3D Environment. O.M. Beketov National University of Urban Economy in Kharkiv. Originally published 2024. [doi:10.48550/arXiv.2511.20919](https://doi.org/10.48550/arXiv.2511.20919)

`q1 · i?` · `design · r2`

Definitional/technical statement (type d) from the platform design section, not a measured benchmark study. The Light version achieves accessibility "by reducing polygon counts, disabling advanced effects like Lumen lighting or high-resolution Niagara particles" while keeping 30 fps, leveraging Unreal Engine's LOD system and dynamic resolution scaling for resource-constrained institutions.

> "the "Light" version of VLab -HV optimizes performance on low-end systems (e.g., 8 GB RAM, integrated GPUs) by reducing polygon counts, disabling advanced effects like Lumen lighting or high-resolution Niagara particles, and maintain ing a minimum frame rate of 30 fps."

## Discussion


## Related Claims
- [An ELEVATE prototype achieves near real-time end-to-end tutoring interaction on consumer-grade school hardware without cloud GPUs](elevate-prototype-near-real-time-consumer-hardware.md) — related
- [The VR simulator ran reliably and was quickly deployable, with under-5-minute setup, minimum 90 fps frame rates, and no malfunctions or breakages](vr-simulator-technical-performance-reliability.md) — related
- [The 3B VR classroom system achieves an average end-to-end latency of approximately 73 ms, below the 150 ms threshold required for real-time interactions](3b-end-to-end-latency-below-realtime-threshold.md) — related
