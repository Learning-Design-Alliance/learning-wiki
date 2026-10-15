---
type: claim
title: Qwen 7B and Mistral Nemo 12B passed the classroom speed gate in round 2 and were retained as candidates pending faculty review
description: Qwen 7B and Mistral Nemo 12B passed the classroom speed gate in round 2 and were retained as candidates pending faculty review
id: round2-candidates-pass-speed-gate
status: draft
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
  - id: sidney-shapiro-and-joshua-lindemann-2026-2
    resource: "https://arxiv.org/abs/2610.02510"
    title: "Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510"
    author: Sidney Shapiro and Joshua Lindemann
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# Qwen 7B and Mistral Nemo 12B passed the classroom speed gate in round 2 and were retained as candidates pending faculty review

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r3` · `q2`

## Subclaims
`q2 i?` Qwen 7B and Mistral Nemo 12B both passed 12/12 probes with latency ratios of 1.01 and 1.24, and Qwen completeness was 0.93 versus 0.91 for 8B. [→ Sidney Shapiro and Joshua Lindemann 2026](#sidney-shapiro-and-joshua-lindemann-2026)
`q2 i?` Round 2 counters categorical rejection of larger models: Nemo 12B completed at 1.24 times its fresh baseline. [→ Sidney Shapiro and Joshua Lindemann 2026 (2)](#sidney-shapiro-and-joshua-lindemann-2026-2)

## Evidence

### Sidney Shapiro and Joshua Lindemann 2026

Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510 [doi:10.48550/arxiv.2610.02510](https://doi.org/10.48550/arxiv.2610.02510)

`q2 · i?` · `design · r3`

Bake-off round 2 on Node A with non-thinking candidates and a fresh 8B baseline; the decision summary reports "latency ratios were 1.01 and 1.24" and a small completeness-proxy difference, and both were retained as candidates for paired review.

> "Both passed 12/12 probes; latency ratios were 1.01 and 1.24. Qwen completeness was 0.93 versus 0.91 for 8B."

### Sidney Shapiro and Joshua Lindemann 2026 (2)

Sidney Shapiro and Joshua Lindemann. (2026). On-Premises Multi-Course RAG Tutoring for Business Education: Hardware–Software Trade-offs in a Campus AI Tutor. arXiv. https://arxiv.org/abs/2610.02510

`q2 · i?` · `design · r3`

The results section states the round-2 outcome in the authors' words: "Nemo 12B completed at 1.24 times its fresh baseline", showing a larger model can fit the latency allowance.

> "Round 2 provides a counterexample to rejecting larger models categorically: Nemo 12B completed at 1.24 times its fresh baseline."

## Discussion


## Related Claims
- [Larger dense generators passed smoke probes but all exceeded the +30% classroom latency limit in bake-off round 1](larger-generators-fail-classroom-speed-gate.md) — related
- [Head-to-head comparison exposes a security-usability-latency tension: NeMo reaches 0% bypass at 16.22% FPR and ~1.5 s latency while Prompt Guard yields 38.48% bypass at 3.60% FPR](nemo-prompt-guard-tradeoff-holdout.md) — related
