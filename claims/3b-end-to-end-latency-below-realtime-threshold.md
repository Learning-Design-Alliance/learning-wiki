---
type: claim
title: The 3B VR classroom system achieves an average end-to-end latency of approximately 73 ms, below the 150 ms threshold required for real-time interactions
description: The 3B VR classroom system achieves an average end-to-end latency of approximately 73 ms, below the 150 ms threshold required for real-time interactions
id: 3b-end-to-end-latency-below-realtime-threshold
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-17
evidence_strength: moderate
newest_evidence: 2016
recheck_by: 2019
sources:
  - id: lugrin-j-l-2016
    title: Lugrin J-L 2016
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# The 3B VR classroom system achieves an average end-to-end latency of approximately 73 ms, below the 150 ms threshold required for real-time interactions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2019**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Video-based latency measurement of the 3B system found approximately 73 ms average end-to-end latency (SD 45), below the 150 ms real-time threshold, with an average frame rate of 75 fps. [→ Lugrin J-L 2016](#lugrin-j-l-2016)

## Evidence

### Lugrin J-L 2016

Lugrin J-L, Latoschik ME, Habel M, Roth D, Seufert C and Grafe S (2016) Breaking Bad Behaviors: A New Tool for Learning Classroom Management Using Virtual Reality. Front. ICT 3:26. https://doi.org/10.3389/fict.2016.00026

`q2 · i?` · `design · r3`

Pre-user study technical measurement using a video-based frame-counting method with videos recorded at 480 Hz. The measurement found latency "approximately 73 ms (±SD 45)" and the system "delivered an average frame rate of 75 frames per second" for about 400 K triangles per frame.

> "The average end-to-end latency between movements of the participant's head and corresponding updates of the projected images was evaluated to approximately 73 ms (±SD 45), which is below the threshold required for real-time interactions [≤150 ms (Lugrin et al., 2012)]."

## Discussion


## Related Claims
- [The Photon Fusion VR learning system achieves stable real-time communication with minimal device load](photon-fusion-stable-realtime-communication.md) — related
- [An ELEVATE prototype achieves near real-time end-to-end tutoring interaction on consumer-grade school hardware without cloud GPUs](elevate-prototype-near-real-time-consumer-hardware.md) — a broader claim this one bears on
- [The prototype maintains total end-to-end latency of 3-5 seconds between query completion and RAG-generated response delivery](hdr-vr-platform-3-5-second-latency.md) — related
