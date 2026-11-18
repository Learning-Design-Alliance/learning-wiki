---
type: claim
title: "AKT's monotonic attention mechanism outperforms positional-encoding attention variants by about 1% to 6% AUC"
description: "AKT's monotonic attention mechanism outperforms positional-encoding attention variants by about 1% to 6% AUC"
id: akt-monotonic-attention-beats-positional-encoding
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

# AKT's monotonic attention mechanism outperforms positional-encoding attention variants by about 1% to 6% AUC

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In ablation experiments, AKT-NR significantly outperforms attention mechanisms using positional embeddings, including SAKT, by about 1% to 6% on all four datasets. [→ Aritra Ghosh 2020](#aritra-ghosh-2020)

## Evidence

### Aritra Ghosh 2020

Aritra Ghosh, Neil Heffernan, and Andrew S. Lan. 2020. Context-Aware Attentive Knowledge Tracing. In Proceedings of the 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '20). https://doi.org/10.1145/3394486.3403282

`q2 · i?` · `design · r2`

Ablation experiment on all four benchmark datasets comparing AKT-NR against variants using learnable or fixed positional encoding and against SAKT; AKT-NR "significantly outperforms other attention mechanisms using positional embeddings, including SAKT."

> "We see that AKT-NR significantly outperforms other attention mechanisms using positional embeddings, including SAKT, by about 1% to 6% on all datasets."

## Discussion


## Related Claims
- [Context-aware question and response representations improve AKT's prediction over raw embeddings](akt-context-aware-representations-improve-prediction.md) — related
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — related
- [AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses](akt-outperforms-kt-baselines-auc-benchmarks.md) — a broader claim this one bears on
- [The survey reports, citing Pu and Becker, that removing students' repeated interactions on the same exercises reduced AKT's performance to close to that of DKVMN.](attentive-knowledge-tracing-benefits-from-repeated-interactions.md) — related
