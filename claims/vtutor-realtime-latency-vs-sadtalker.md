---
type: claim
title: VTutor produced lip-synced animation within one second in a browser, versus 143 seconds for SadTalker to generate a 7-second video
description: VTutor produced lip-synced animation within one second in a browser, versus 143 seconds for SadTalker to generate a 7-second video
id: vtutor-realtime-latency-vs-sadtalker
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: eason-chen-2025
    resource: "https://doi.org/10.1007/978-3-031-99267-4_19"
    title: "Eason Chen, Chenyu Lin, Yu-Kai Huang, Xinyi Tang, Aprille Xi, Jionghao Lin, Kenneth Koedinger. (2025). VTutor: An Animated Pedagogical Agent SDK that Provide Real Time Multi-Model Feedback. arXiv:2505.06676. [doi:10.1007/978-3-031-99267-4_19](https://doi.org/10.1007/978-3-031-99267-4_19)"
    author: Eason Chen, Chenyu Lin, Yu-Kai Huang, Xinyi Tang, Aprille Xi, Jionghao Lin, Kenneth Koedinger
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: eason-chen-2025-2
    resource: "https://doi.org/10.1007/978-3-031-99267-4_19"
    title: "Eason Chen, Chenyu Lin, Yu-Kai Huang, Xinyi Tang, Aprille Xi, Jionghao Lin, Kenneth Koedinger. (2025). VTutor: An Animated Pedagogical Agent SDK that Provide Real Time Multi-Model Feedback. arXiv:2505.06676. [doi:10.1007/978-3-031-99267-4_19](https://doi.org/10.1007/978-3-031-99267-4_19)"
    author: Eason Chen, Chenyu Lin, Yu-Kai Huang, Xinyi Tang, Aprille Xi, Jionghao Lin, Kenneth Koedinger
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# VTutor produced lip-synced animation within one second in a browser, versus 143 seconds for SadTalker to generate a 7-second video

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` SadTalker required 143 seconds to generate a 7-second video on an NVIDIA Titan XP GPU, whereas VTutor produced the animation within one second via a browser environment. [→ Eason Chen 2025](#eason-chen-2025)
`q2 i?` VTutor can be integrated with just an HTML iframe and requires no specialized backend for animation rendering, which the authors present as lightweight, scalable deployment. [→ Eason Chen 2025 (2)](#eason-chen-2025-2)

## Evidence

### Eason Chen 2025

Eason Chen, Chenyu Lin, Yu-Kai Huang, Xinyi Tang, Aprille Xi, Jionghao Lin, Kenneth Koedinger. (2025). VTutor: An Animated Pedagogical Agent SDK that Provide Real Time Multi-Model Feedback. arXiv:2505.06676. [doi:10.1007/978-3-031-99267-4_19](https://doi.org/10.1007/978-3-031-99267-4_19)

`q2 · i?` · `design · r2`

Technical timing measurement in the authors' experiment: SadTalker needed 143 seconds on an NVIDIA Titan XP GPU to generate a 7-second video, while VTutor "produced the animation within one second via a browser environment".

> "In our experiment, SadTalker required 143 seconds to generate a 7-second video on an NVIDIA Titan XP GPU, whereas VTutor produced the animation within one second via a browser environment."

### Eason Chen 2025 (2)

Eason Chen, Chenyu Lin, Yu-Kai Huang, Xinyi Tang, Aprille Xi, Jionghao Lin, Kenneth Koedinger. (2025). VTutor: An Animated Pedagogical Agent SDK that Provide Real Time Multi-Model Feedback. arXiv:2505.06676. [doi:10.1007/978-3-031-99267-4_19](https://doi.org/10.1007/978-3-031-99267-4_19)

`q2 · i?` · `design · r2`

Deployment analysis of the SDK: VTutor "can be integrated with just an HTML iframe and requires no specialized backend" for animation rendering, which the authors present as lightweight, scalable deployment of animated pedagogical agents.

> "Moreover, VTutor can be integrated with just an HTML iframe and requires no specialized backend to compute the animation rendering, underscoring its lightweight and scalability in deploying APA at scale."

## Discussion


## Related Claims
- [In a 50-participant blind comparison, users strongly preferred VTutor over a SadTalker-generated talking head](vtutor-preferred-over-sadtalker.md) — related
- [An ELEVATE prototype achieves near real-time end-to-end tutoring interaction on consumer-grade school hardware without cloud GPUs](elevate-prototype-near-real-time-consumer-hardware.md) — a broader claim this one bears on
- [VTutor received significantly higher ratings than the SadTalker talking head on all five evaluation dimensions](vtutor-higher-ratings-all-dimensions.md) — related
