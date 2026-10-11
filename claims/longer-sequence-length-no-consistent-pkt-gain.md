---
type: claim
title: Extending maximum sequence length from 50 to 100 does not lead to consistent knowledge-tracing performance improvements; negative changes appear more frequently across models and datasets
description: Extending maximum sequence length from 50 to 100 does not lead to consistent knowledge-tracing performance improvements; negative changes appear more frequently across models and datasets
id: longer-sequence-length-no-consistent-pkt-gain
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
  - id: jaewook-kim-2026-2
    resource: "https://arxiv.org/abs/2605.04727"
    title: "Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727"
    author: Jaewook Kim, Hyeoncheol Kim
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Extending maximum sequence length from 50 to 100 does not lead to consistent knowledge-tracing performance improvements; negative changes appear more frequently across models and datasets

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` Across DKT, Code-DKT, and ECKT, most assignments show marginal changes or clear degradation when Lmax is increased to 100. [→ Jaewook Kim 2026](#jaewook-kim-2026)
`q2 i?` The 95th percentile of student attempt sequence lengths exceeds the commonly adopted Lmax = 50, ranging from 81 to 135 across assignments, yet longer contexts do not reliably help. [→ Jaewook Kim 2026 (2)](#jaewook-kim-2026-2)

## Evidence

### Jaewook Kim 2026

Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727

`q2 · i?` · `causal · r2`

Numerical comparison (Table 5) of Lmax = 50 versus Lmax = 100 for DKT, Code-DKT, and ECKT on CodeWorkout under TAlign/CRect. The authors suggest extended sequences may introduce "additional irrelevant or weakly informative interactions".

> "most assignments exhibit either marginal changes or clear performance degradation when Lmax is increased to 100. Performance gains are sporadic and limited in magnitude, whereas negative∆values appear more frequently and consistently across models and datasets."

### Jaewook Kim 2026 (2)

Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727

`q2 · i?` · `causal · r2`

Sequence-length analysis of the CodeWorkout dataset (Table 1, Section 4.4) showing that aggressive truncation at Lmax = 50 removes a substantial portion of student interaction histories, motivating the Lmax = 100 comparison.

> "the 95th percentile of student attempt sequence lengths consistently exceeds the commonly adopted limit ofLmax = 50, ranging from 81 to 135 across assignments."

## Discussion


## Related Claims
- [Code-DKT's attention softmax applied across the temporal dimension (dim=1) is causally invalid and inflates reported performance; rectifying it to the path dimension (dim=2) removes the artificial gain](pkt-attention-softmax-dimension-causal-flaw.md) — related
- [Hyperparameter sensitivity in PKT is an inherent characteristic of programming interaction data, varying across models and across assignments within the same model](pkt-hyperparameter-sensitivity-varies-by-model-and-assignment.md) — related
