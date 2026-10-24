---
type: claim
title: Failing to sort student attempt sequences by ServerTimestamp violates temporal causality and can systematically overestimate PKT model performance
description: Failing to sort student attempt sequences by ServerTimestamp violates temporal causality and can systematically overestimate PKT model performance
id: pkt-temporal-causality-violation-inflates-performance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
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
---

# Failing to sort student attempt sequences by ServerTimestamp violates temporal causality and can systematically overestimate PKT model performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The official Code-DKT implementation aggregates interactions in raw appearance order rather than chronological order, introducing look-ahead bias and explicit data leakage. [→ Jaewook Kim 2026](#jaewook-kim-2026)

## Evidence

### Jaewook Kim 2026

Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727 [doi:10.48550/arxiv.2605.04727](https://doi.org/10.48550/arxiv.2605.04727)

`q2 · i?` · `causal · r2`

Audit of the official open-source Code-DKT implementation on CodeWorkout. The authors show with Figure 1 that for SubjectID 106, Attempt 6 (a failure) actually occurred before Attempt 5 (a success), introducing "look-ahead biasand explicit data leakage".

> "the codebase fails to perform chrono- logical sorting byServerTimestamp and instead aggregates interactions based on their raw appearance order"

## Discussion

## Related Claims

- [Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models](learner-models-miscalibrated-outside-data-interval.md) — the general claim this finding bears on, with the studies behind it
- [Code-DKT's attention softmax applied across the temporal dimension (dim=1) is causally invalid and inflates reported performance; rectifying it to the path dimension (dim=2) removes the artificial gain](pkt-attention-softmax-dimension-causal-flaw.md) — related
- [Under causally valid, tuned settings, code-level embeddings do not consistently improve performance: rectified Code-DKT underperforms tuned DKT on several assignments, while ECKT remains competitive](code-embeddings-inconsistent-under-rectified-settings.md) — related
- [Task-specific hyperparameter optimization substantially raises baseline DKT performance, indicating prior DKT-vs-PKT gaps partly reflect insufficient baseline tuning](task-specific-hyperparameter-tuning-raises-dkt-baseline.md) — related
