---
type: claim
title: "Larger dense generators passed smoke probes but all exceeded the +30% classroom latency limit in bake-off round 1"
description: "Larger dense generators passed smoke probes but all exceeded the +30% classroom latency limit in bake-off round 1"
id: larger-generators-fail-classroom-speed-gate
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: sidney-shapiro-and-joshua-lindemann-2026
    resource: "https://doi.org/10.48550/arxiv.2610.02510"
    title: "Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510 [doi:10.48550/arxiv.2610.02510](https://doi.org/10.48550/arxiv.2610.02510)"
    author: Sidney Shapiro and Joshua Lindemann
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Larger dense generators passed smoke probes but all exceeded the +30% classroom latency limit in bake-off round 1

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`

## Subclaims
`q2 i?` In bake-off round 1, larger dense candidates passed all 12/12 live probes but their median completion times were 1.75–3.36 times the 8B baseline, failing the speed gate. [→ Sidney Shapiro and Joshua Lindemann 2026](#sidney-shapiro-and-joshua-lindemann-2026)

## Evidence

### Sidney Shapiro and Joshua Lindemann 2026

Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510 [doi:10.48550/arxiv.2610.02510](https://doi.org/10.48550/arxiv.2610.02510)

`q2 · i?` · `design · r3`

Server-local bake-off round 1 on Node A with fixed retrieval, context length 8192, and output cap 768 tokens; the decision table reports "All passed 12/12 live probes" yet every candidate exceeded the +30% latency limit, so 8B was retained.

> "All passed 12/12 live probes; median completion times were 1.75–3.36 times the 8B baseline."

## Discussion


## Related Claims
- [Qwen 7B and Mistral Nemo 12B passed the classroom speed gate in round 2 and were retained as candidates pending faculty review](round2-candidates-pass-speed-gate.md) — related
- [Purpose-trained single-pass generation completes a slide in a median of 17 seconds and an interactive page in 59 seconds over 220k production requests, and delivers artifacts at 15–22× lower per-artifact API cost than flagship models](cogevol-single-pass-latency-and-cost.md) — related
- [In Quantitative AI sessions, faster AI replies were associated with more engagement, more correct practice, and larger learning gains; these associations were not significant in Verbal](faster-ai-replies-linked-engagement-practice-gains.md) — related
