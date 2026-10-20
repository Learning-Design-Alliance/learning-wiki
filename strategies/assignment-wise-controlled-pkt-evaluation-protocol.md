---
type: strategy
id: assignment-wise-controlled-pkt-evaluation-protocol
title: "Adopt an assignment-wise controlled evaluation protocol for PKT benchmarking: chronological alignment, causal rectification, and grid-search hyperparameter tuning on a single designated fold fixed across all folds"
description: "This strategy is the article's controlled evaluation protocol for reliable and comparable programming knowledge tracing evaluation."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: jaewook-kim-2026
    resource: "https://arxiv.org/abs/2605.04727"
    title: "Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727"
    author: Jaewook Kim, Hyeoncheol Kim
---

# Adopt an assignment-wise controlled evaluation protocol for PKT benchmarking: chronological alignment, causal rectification, and grid-search hyperparameter tuning on a single designated fold fixed across all folds

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
This strategy is the article's controlled evaluation protocol for reliable and comparable programming knowledge tracing evaluation. It enforces strict ascending sort by ServerTimestamp before processing attempt records, changes the attention normalization axis from the time axis to the path axis, and tunes hyperparameters per assignment: "we adopt an assignment-wise tuning strategy where models are trained and evaluated independently for each task." The optimal configuration found on fold 0 is then fixed across all remaining folds, with independent fixed random seeds for data splitting, fold generation, and model initialization to eliminate stochastic variance.

## Design Implications

### Context
#### Requirements
- Chronological sorting by ServerTimestamp as preprocessing before processing all student attempt records
- Grid search on a designated validation fold (fold 0) with the resulting configuration fixed across all remaining folds
- Independent fixed random seeds for train/test separation, cross-validation splits, and model initialization
#### Constraints
- The study is limited to a specific dataset (CodeWorkout) and a subset of PKT models; extending the protocol to broader domains and architectures remains future work

### Target Learners
- students completing programming assignments on CodeWorkout-style online platforms

### Target Learning Goals
- predicting learners' evolving programming knowledge states from interaction histories

## Claims

- [Code-DKT's attention softmax applied across the temporal dimension (dim=1) is causally invalid and inflates reported performance; rectifying it to the path dimension (dim=2) removes the artificial gain](../claims/pkt-attention-softmax-dimension-causal-flaw.md) [+W]
- [Failing to sort student attempt sequences by ServerTimestamp violates temporal causality and can systematically overestimate PKT model performance](../claims/pkt-temporal-causality-violation-inflates-performance.md) [+W]
- [Task-specific hyperparameter optimization substantially raises baseline DKT performance, indicating prior DKT-vs-PKT gaps partly reflect insufficient baseline tuning](../claims/task-specific-hyperparameter-tuning-raises-dkt-baseline.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Jaewook Kim, Hyeoncheol Kim. (2026). Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols. Preprint, International Conference on Intelligent Tutoring Systems (ITS 2026), Springer LNCS. https://arxiv.org/abs/2605.04727
