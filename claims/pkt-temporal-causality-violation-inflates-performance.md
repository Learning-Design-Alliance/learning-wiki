---
type: claim
title: Failing to sort student attempt sequences by ServerTimestamp violates temporal causality and can systematically overestimate PKT model performance
description: Failing to sort student attempt sequences by ServerTimestamp violates temporal causality and can systematically overestimate PKT model performance
id: pkt-temporal-causality-violation-inflates-performance
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jaewook-kim-2026
    resource: "https://arxiv.org/abs/2605.04727"
    title: "Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727"
    author: Jaewook Kim, Hyeoncheol Kim
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Failing to sort student attempt sequences by ServerTimestamp violates temporal causality and can systematically overestimate PKT model performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` The official Code-DKT implementation aggregates interactions in raw appearance order rather than chronological order, introducing look-ahead bias and explicit data leakage. [→ Jaewook Kim 2026](#jaewook-kim-2026)

## Evidence

### Jaewook Kim 2026

Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727

`q2 · i?` · `causal · r2`

Audit of the official open-source Code-DKT implementation on CodeWorkout. The authors show with Figure 1 that for SubjectID 106, Attempt 6 (a failure) actually occurred before Attempt 5 (a success), introducing "look-ahead biasand explicit data leakage".

> "the codebase fails to perform chrono- logical sorting byServerTimestamp and instead aggregates interactions based on their raw appearance order"

## Discussion


## Related Claims
- [Code-DKT's attention softmax applied across the temporal dimension (dim=1) is causally invalid and inflates reported performance; rectifying it to the path dimension (dim=2) removes the artificial gain](pkt-attention-softmax-dimension-causal-flaw.md) — related
