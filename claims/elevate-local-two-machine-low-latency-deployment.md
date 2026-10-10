---
type: claim
title: The ELEVATE server pipeline runs locally on two heterogeneous consumer machines, keeping LLM and TTS models fully resident in memory for low-latency inference
description: The ELEVATE server pipeline runs locally on two heterogeneous consumer machines, keeping LLM and TTS models fully resident in memory for low-latency inference
id: elevate-local-two-machine-low-latency-deployment
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
sources:
  - id: lorenzo-stacchio-2026
    resource: "https://arxiv.org/abs/2606.30662"
    title: "Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni. (2026). ELEVATE: Designing Human-Centered GenAI Virtual Tutors for Scalable and Inclusive Education. arXiv preprint. https://arxiv.org/abs/2606.30662"
    author: Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The ELEVATE server pipeline runs locally on two heterogeneous consumer machines, keeping LLM and TTS models fully resident in memory for low-latency inference

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` In the reported hardware configuration, the system ran on two local consumer machines (one for LLM generation and orchestration, one for TTS) and kept both models fully resident in memory while performing low-latency inference. [→ Lorenzo Stacchio 2026](#lorenzo-stacchio-2026)

## Evidence

### Lorenzo Stacchio 2026

Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni. (2026). ELEVATE: Designing Human-Centered GenAI Virtual Tutors for Scalable and Inclusive Education. arXiv preprint. https://arxiv.org/abs/2606.30662

`q1 · i?` · `design · r2`

Apparatus description of the small-school deployment: the server pipeline was executed on two local machines, one running LLM generation and the Orchestrator and one running TTS, using consumer GPUs of different generations. The authors state this configuration supports "performing low-latency inference"; no latency numbers are printed in the available text.

> "This configuration is capable of keeping both the LLM and TTS models fully resident in memory and performing low-latency inference (while adopting a low-cost and consumer device)."

## Discussion


## Related Claims
- [An ELEVATE prototype achieves near real-time end-to-end tutoring interaction on consumer-grade school hardware without cloud GPUs](elevate-prototype-near-real-time-consumer-hardware.md) — related
