---
type: claim
title: "Code-DKT's attention softmax applied across the temporal dimension (dim=1) is causally invalid and inflates reported performance; rectifying it to the path dimension (dim=2) removes the artificial gain"
description: "Code-DKT's attention softmax applied across the temporal dimension (dim=1) is causally invalid and inflates reported performance; rectifying it to the path dimension (dim=2) removes the artificial gain"
id: pkt-attention-softmax-dimension-causal-flaw
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: jaewook-kim-2026
    resource: "https://doi.org/10.48550/arxiv.2605.04727"
    title: "Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727 [doi:10.48550/arxiv.2605.04727](https://doi.org/10.48550/arxiv.2605.04727)"
    author: Jaewook Kim, Hyeoncheol Kim
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: jaewook-kim-2026-2
    resource: "https://arxiv.org/abs/2605.04727"
    title: "Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727"
    author: Jaewook Kim, Hyeoncheol Kim
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Code-DKT's attention softmax applied across the temporal dimension (dim=1) is causally invalid and inflates reported performance; rectifying it to the path dimension (dim=2) removes the artificial gain

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 causal `r2` · `q2`

## Subclaims
`q2 i?` The official implementation applies Softmax across the time-step dimension, allowing normalization over the entire interaction sequence and introducing temporal data leakage. [→ Jaewook Kim 2026](#jaewook-kim-2026)
`q2 i?` The authors replicated the original reported gain of approximately 0.03–0.04 AUC over DKT before identifying the flaw. [→ Jaewook Kim 2026 (2)](#jaewook-kim-2026-2)

## Evidence

### Jaewook Kim 2026

Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727 [doi:10.48550/arxiv.2605.04727](https://doi.org/10.48550/arxiv.2605.04727)

`q2 · i?` · `causal · r2`

Code audit of the official Code-DKT source. The authors argue this "look-ahead" mechanism lets the importance of code features at time t be influenced by future states, and that normalization must instead occur across the path dimension (dim=2).

> "the Softmax operation in the attention layer is applied across the temporal dimension, specificallydim=1"

### Jaewook Kim 2026 (2)

Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727

`q2 · i?` · `causal · r2`

Replication of Code-DKT results from the official implementation on CodeWorkout, confirming the reported gain over the DKT baseline before the audit. The authors attribute the gain to "this causal violation" rather than architectural superiority.

> "we executed the official source code [16] provided by the authors and successfully replicated the empirical results reported in the original paper, including the performance gain of approximately 0.03–0.04 in AUC"

## Discussion


## Related Claims
- [Failing to sort student attempt sequences by ServerTimestamp violates temporal causality and can systematically overestimate PKT model performance](pkt-temporal-causality-violation-inflates-performance.md) — related
- [Under causally valid, tuned settings, code-level embeddings do not consistently improve performance: rectified Code-DKT underperforms tuned DKT on several assignments, while ECKT remains competitive](code-embeddings-inconsistent-under-rectified-settings.md) — related
- [Extending maximum sequence length from 50 to 100 does not lead to consistent knowledge-tracing performance improvements; negative changes appear more frequently across models and datasets](longer-sequence-length-no-consistent-pkt-gain.md) — related
