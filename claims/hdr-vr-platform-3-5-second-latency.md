---
type: claim
title: The prototype maintains total end-to-end latency of 3-5 seconds between query completion and RAG-generated response delivery
description: The prototype maintains total end-to-end latency of 3-5 seconds between query completion and RAG-generated response delivery
id: hdr-vr-platform-3-5-second-latency
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: ronghua-xu-2026
    resource: "https://arxiv.org/abs/2608.08163"
    title: "Ronghua Xu, Kepha Barasa, Manoj Kumal, Xinyun Liu, Weihua Zhou, Xin Qian. (2026). Agentic AI-driven Immersive Simulation: A Knowledge-Aware Virtual Training Platform for High Dose Rate (HDR) Brachytherapy. arXiv. https://arxiv.org/abs/2608.08163"
    author: Ronghua Xu, Kepha Barasa, Manoj Kumal, Xinyun Liu, Weihua Zhou, Xin Qian
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The prototype maintains total end-to-end latency of 3-5 seconds between query completion and RAG-generated response delivery

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Empirical testing on a Meta Quest 3 interfaced with a dedicated backend server over a LAN measured total latency of 3-5 seconds, judged suitable for HDR training by domain experts. [→ Ronghua Xu 2026](#ronghua-xu-2026)

## Evidence

### Ronghua Xu 2026

Ronghua Xu, Kepha Barasa, Manoj Kumal, Xinyun Liu, Weihua Zhou, Xin Qian. (2026). Agentic AI-driven Immersive Simulation: A Knowledge-Aware Virtual Training Platform for High Dose Rate (HDR) Brachytherapy. arXiv. https://arxiv.org/abs/2608.08163

`q2 · i?` · `design · r2`

Latency measurement on the prototype testbed: 50 Monte Carlo runs on a Meta Quest 3 linked to a dedicated backend server via LAN, with results shown in Table II. The article reports "a network-related delay of 2-3 seconds" and a total of 3-5 seconds, deemed acceptable with thinking animations.

> "We conduct 50 Monte Carlo runs to evaluate the average latency, as shown in Table II. The total latency can be divided into network latency and inference latency."

## Discussion


## Related Claims
- [The ELEVATE server pipeline runs locally on two heterogeneous consumer machines, keeping LLM and TTS models fully resident in memory for low-latency inference](elevate-local-two-machine-low-latency-deployment.md) — related
- [An ELEVATE prototype achieves near real-time end-to-end tutoring interaction on consumer-grade school hardware without cloud GPUs](elevate-prototype-near-real-time-consumer-hardware.md) — a broader claim this one bears on
- [On the live single-node deployment, short-answer rounds take ≈32 s (≈$0.015/round) while multiple-choice rounds are ≈4× faster (≈7.6 s, ≈$0.005/round) because grading is deterministic](collearn-latency-cost-efficiency.md) — related
