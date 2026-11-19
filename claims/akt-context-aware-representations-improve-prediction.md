---
type: claim
title: "Context-aware question and response representations improve AKT's prediction over raw embeddings"
description: "Context-aware question and response representations improve AKT's prediction over raw embeddings"
id: akt-context-aware-representations-improve-prediction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
sources:
  - id: aritra-ghosh-2020
    title: Aritra Ghosh 2020
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Context-aware question and response representations improve AKT's prediction over raw embeddings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On all datasets, AKT variants with question and knowledge encoders outperform variants that use raw question and response embeddings. [→ Aritra Ghosh 2020](#aritra-ghosh-2020)

## Evidence

### Aritra Ghosh 2020

Aritra Ghosh, Neil Heffernan, and Andrew S. Lan. 2020. Context-Aware Attentive Knowledge Tracing. In Proceedings of the 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '20). https://doi.org/10.1145/3394486.3403282

`q2 · i?` · `design · r2`

First ablation experiment comparing AKT-R and AKT-NR, which pass embeddings through the question and knowledge encoders, against AKTraw-NR and AKTraw-R using raw embeddings; the encoded variants "outperform their counterparts" on all datasets.

> "On all datasets AKT-R and AKT-NR outperform their counterparts, AKTraw-NR and AKTraw-R, which use only a single self-attention mechanism with exponential decay (i.e., the knowledge retriever)."

## Discussion


## Related Claims
- [AKT's monotonic attention mechanism outperforms positional-encoding attention variants by about 1% to 6% AUC](akt-monotonic-attention-beats-positional-encoding.md) — related
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
- [AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses](akt-outperforms-kt-baselines-auc-benchmarks.md) — a broader claim this one bears on
- [Among deep learning KT models, simpler DKT performs comparably to complex architectures under limited dialogue data](dkt-comparable-to-complex-kt-architectures.md) — related
- [DKT-based environments converge faster in training, but DKT struggles to estimate higher knowledge levels, unlike the more comprehensive AKT assessments](dkt-faster-convergence-but-poor-high-level-estimates.md) — related
