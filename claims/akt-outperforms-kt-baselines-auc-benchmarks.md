---
type: claim
title: AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses
description: AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses
id: akt-outperforms-kt-baselines-auc-benchmarks
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
  - id: aritra-ghosh-2020-2
    title: Aritra Ghosh 2020 (2)
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# AKT outperforms existing knowledge tracing methods on benchmark datasets in predicting future learner responses

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On the ASSISTments2015 and ASSISTments2017 datasets, AKT-NR improves AUC by 6% and 1% over the closest baseline, and performs on-par with the best-performing baseline on Statics2011 and ASSISTments2009. [→ Aritra Ghosh 2020](#aritra-ghosh-2020)
`q2 i?` Under an alternative experimental setting for questions tagged with multiple concepts on ASSISTments2009, AKT-R still outperforms all baselines. [→ Aritra Ghosh 2020 (2)](#aritra-ghosh-2020-2)

## Evidence

### Aritra Ghosh 2020

Aritra Ghosh, Neil Heffernan, and Andrew S. Lan. 2020. Context-Aware Attentive Knowledge Tracing. In Proceedings of the 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '20). https://doi.org/10.1145/3394486.3403282

`q2 · i?` · `design · r2`

Quantitative evaluation on four benchmark datasets (Statics2011, ASSISTments2009, ASSISTments2015, ASSISTments2017) using 5-fold cross-validation with AUC as the metric. AKT-NR "improves the AUC by 6% and 1% over the closest baseline" on ASSISTments2015 and 2017 and "performs on-par with the best-performing baseline" on the other two datasets.

> "On the ASSISTments2015 and ASSISTments2017 datasets, AKT-NR improves the AUC by 6% and 1% over the closest baseline. It performs on-par with the best-performing baseline on the Statics2011 and ASSISTments2009 datasets."

### Aritra Ghosh 2020 (2)

Aritra Ghosh, Neil Heffernan, and Andrew S. Lan. 2020. Context-Aware Attentive Knowledge Tracing. In Proceedings of the 26th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '20). https://doi.org/10.1145/3394486.3403282

`q2 · i?` · `design · r2`

Robustness check on ASSISTments2009 under an alternative setting that averages concept embeddings for questions tagged with multiple concepts; all methods show similar performance drops, yet "AKT-R still comfortably outperforms all baselines."

> "We observe similar performance drops compared to our standard experimental setting for all KT methods, while AKT-R still comfortably outperforms all baselines."

## Discussion


## Related Claims
- [Under one standardised evaluation, most deep knowledge-tracing models published after the original DKT do not beat it, and a common KC-level evaluation shortcut inflates reported accuracy](newer-deep-kt-models-rarely-beat-dkt-standard-protocol.md) — possibly the same claim (merge candidate)
- [AKT's monotonic attention mechanism outperforms positional-encoding attention variants by about 1% to 6% AUC](akt-monotonic-attention-beats-positional-encoding.md) — a narrower finding that bears on this claim
- [Context-aware question and response representations improve AKT's prediction over raw embeddings](akt-context-aware-representations-improve-prediction.md) — a narrower finding that bears on this claim
- [DKT-based environments converge faster in training, but DKT struggles to estimate higher knowledge levels, unlike the more comprehensive AKT assessments](dkt-faster-convergence-but-poor-high-level-estimates.md) — related
