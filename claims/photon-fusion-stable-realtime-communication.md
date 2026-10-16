---
type: claim
title: The Photon Fusion VR learning system achieves stable real-time communication with minimal device load
description: The Photon Fusion VR learning system achieves stable real-time communication with minimal device load
id: photon-fusion-stable-realtime-communication
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: iwai-wataru-2026
    resource: "https://doi.org/10.48550/arxiv.2606.10325"
    title: "Iwai Wataru, Duc V . Nguyen. (2026). Design and Implementation of a Real-Time Multi-Site Immersive Learning System Using Photon Fusion. https://arxiv.org/abs/2606.10325 [doi:10.48550/arxiv.2606.10325](https://doi.org/10.48550/arxiv.2606.10325)"
    author: Iwai Wataru, Duc V . Nguyen
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: iwai-wataru-2026-2
    resource: "https://arxiv.org/abs/2606.10325"
    title: "Iwai Wataru, Duc V . Nguyen. (2026). Design and Implementation of a Real-Time Multi-Site Immersive Learning System Using Photon Fusion. https://arxiv.org/abs/2606.10325"
    author: Iwai Wataru, Duc V . Nguyen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The Photon Fusion VR learning system achieves stable real-time communication with minimal device load

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` During the lab test the teacher's device averaged 72.47 fps (SD = 0.95), indicating minimal load. [→ Iwai Wataru 2026](#iwai-wataru-2026)
`q2 i?` Average end-to-end audio response time between clients was 1.968 seconds (SD = 0.063), indicating high stability with minimal jitter. [→ Iwai Wataru 2026 (2)](#iwai-wataru-2026-2)

## Evidence

### Iwai Wataru 2026

Iwai Wataru, Duc V . Nguyen. (2026). Design and Implementation of a Real-Time Multi-Site Immersive Learning System Using Photon Fusion. https://arxiv.org/abs/2606.10325 [doi:10.48550/arxiv.2606.10325](https://doi.org/10.48550/arxiv.2606.10325)

`q2 · i?` · `design · r2`

Device-load measurement recorded during the lab evaluation of the proposed system. The average frame rate was "72.47(SD = 0.95 fps)", which the authors interpret as minimal load. No effect size is printed.

> "To evaluate the device load, we recorded the frame rate of the device used by the teacher during the test. The results showed that the average frame rate was 72.47(SD = 0.95 fps), indicating that the load was minimal."

### Iwai Wataru 2026 (2)

Iwai Wataru, Duc V . Nguyen. (2026). Design and Implementation of a Real-Time Multi-Site Immersive Learning System Using Photon Fusion. https://arxiv.org/abs/2606.10325

`q2 · i?` · `design · r2`

End-to-end audio delay measurement in the lab evaluation, defined as the round trip from Client A's speech through Client B's immediate spoken response back to Client A. Average was "1.968 seconds (SD = 0.063 seconds)". No effect size is printed.

> "The measurement results showed that the average audio response time between clients was 1.968 seconds (SD = 0.063 seconds). Given that the standard deviation was extremely small at 0.063 seconds, indicating high stability, this suggests that fluctuations in communication path delay (jitter) and variations in client processing load were minimal."

## Discussion


## Related Claims
- [VR sickness in the system is minimal overall (SSQ total 12.88), with nausea lowest and oculomotor symptoms most significant](photon-fusion-minimal-vr-sickness-ssq.md) — related
