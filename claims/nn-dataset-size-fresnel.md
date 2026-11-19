---
type: claim
title: Model error varies by more than two orders of magnitude with network size, small datasets induce overlearning, and training time depends quasi-linearly on dataset size
description: Model error varies by more than two orders of magnitude with network size, small datasets induce overlearning, and training time depends quasi-linearly on dataset size
id: nn-dataset-size-fresnel
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2022
sources:
  - id: c-finot-and-s-boscolo-2022
    resource: "https://doi.org/10.1088/1361-6404/ac5bec"
    title: "C Finot and S Boscolo (2022). Exploring Fresnel diffraction at a straight edge with a neural network. [doi:10.1088/1361-6404/ac5bec](https://doi.org/10.1088/1361-6404/ac5bec)"
    author: C Finot and S Boscolo
    q: 2
    i: "?"
    kind: design
    rigour: 1
---

# Model error varies by more than two orders of magnitude with network size, small datasets induce overlearning, and training time depends quasi-linearly on dataset size

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Model error varies by more than two orders of magnitude according to network size, and overlearning occurs for small datasets. [→ C Finot and S Boscolo 2022](#c-finot-and-s-boscolo-2022)
`q2 i?` Training time has a quasi-linear dependence on dataset size. [→ C Finot and S Boscolo 2022](#c-finot-and-s-boscolo-2022)

## Evidence

### C Finot and S Boscolo 2022

C Finot and S Boscolo (2022). Exploring Fresnel diffraction at a straight edge with a neural network. [doi:10.1088/1361-6404/ac5bec](https://doi.org/10.1088/1361-6404/ac5bec)

`q2 · i?` · `design · r1`

Numerical results from a three-layered network with 6, 12 or 15 neurons per layer trained for 100 epochs on datasets of varying size (Fig. 5c-d). The article reports the error range, the overlearning instances for small datasets, and the quasi-linear training-time dependence.

> "we see that the model error may vary by more than two orders of magnitude according to the network size (Fig. 5c). We also notice some overlearning instances for small datasets, where the accuracy measured against the training set is good, but the model does not generalise well to the validation set. The training time has a quasi-linear dependence on the dataset size (Fig. 5d)."

## Discussion


## Related Claims
- [Which knowledge-tracing model predicts learner performance best depends on the data, with logistic regression leading on smaller datasets and very long learner histories and deep knowledge tracing on large or sequential ones](knowledge-tracing-model-choice-depends-on-dataset.md) — related
