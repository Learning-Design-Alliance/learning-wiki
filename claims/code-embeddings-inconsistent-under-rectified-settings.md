---
type: claim
title: "Under causally valid, tuned settings, code-level embeddings do not consistently improve performance: rectified Code-DKT underperforms tuned DKT on several assignments, while ECKT remains competitive"
description: "Under causally valid, tuned settings, code-level embeddings do not consistently improve performance: rectified Code-DKT underperforms tuned DKT on several assignments, while ECKT remains competitive"
id: code-embeddings-inconsistent-under-rectified-settings
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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
  - id: jaewook-kim-2026-3
    resource: "https://arxiv.org/abs/2605.04727"
    title: "Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727"
    author: Jaewook Kim, Hyeoncheol Kim
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Under causally valid, tuned settings, code-level embeddings do not consistently improve performance: rectified Code-DKT underperforms tuned DKT on several assignments, while ECKT remains competitive

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On assignments 439 and 494, the rectified Code-DKT model underperforms the tuned DKT baseline despite using code-level representations. [→ Jaewook Kim 2026](#jaewook-kim-2026)
`q2 i?` Restoring the W0 component (CRect+) yields only marginal AUC changes across most assignments for both Code-DKT and ECKT. [→ Jaewook Kim 2026 (2)](#jaewook-kim-2026-2)
`q2 i?` ECKT's CRect version consistently matches or outperforms DKT even without the W0 component. [→ Jaewook Kim 2026 (3)](#jaewook-kim-2026-3)

## Evidence

### Jaewook Kim 2026

Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727 [doi:10.48550/arxiv.2605.04727](https://doi.org/10.48550/arxiv.2605.04727)

`q2 · i?` · `causal · r2`

Comparative analysis (Table 3) of DKT, Code-DKT, and ECKT under TAlign/CRect with task-specific tuning on CodeWorkout. The authors conclude inclusion of code2vec embeddings "does not consistently improve performance under causally valid and optimized settings".

> "In several assignments (e.g., 439 and 494), the rectified Code-DKT model underperforms the tuned DKT baseline despite utilizing code-level representations"

### Jaewook Kim 2026 (2)

Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727

`q2 · i?` · `causal · r2`

Numerical comparison in Table 3 of CRect versus CRect+ settings. The authors interpret this as predictive behavior being dominated by sequence modeling and task-specific dynamics rather than the projection weight.

> "our results for both Code-DKT and ECKT show that restoring the W0 component (CRect+) yields only marginal changes in AUC across most assignments"

### Jaewook Kim 2026 (3)

Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727

`q2 · i?` · `causal · r2`

Table 3 results for ECKT under causal rectification. The authors attribute ECKT's more stable profile to "the structured integration of programming context in ECKT" versus simple feature concatenation.

> "Even without the W0 component, theCRect version of ECKT consistently matches or out- performs DKT, effectively narrowing the gap in assignments where Code-DKT struggles."

## Discussion


## Related Claims
- [Code-DKT's attention softmax applied across the temporal dimension (dim=1) is causally invalid and inflates reported performance; rectifying it to the path dimension (dim=2) removes the artificial gain](pkt-attention-softmax-dimension-causal-flaw.md) — related
- [Task-specific hyperparameter optimization substantially raises baseline DKT performance, indicating prior DKT-vs-PKT gaps partly reflect insufficient baseline tuning](task-specific-hyperparameter-tuning-raises-dkt-baseline.md) — related
- [Failing to sort student attempt sequences by ServerTimestamp violates temporal causality and can systematically overestimate PKT model performance](pkt-temporal-causality-violation-inflates-performance.md) — related
