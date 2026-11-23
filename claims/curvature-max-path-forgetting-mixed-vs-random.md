---
type: claim
title: Curvature-based maximum-sum paths significantly reduce forgetting versus minimum-sum paths across four datasets, but beat a random baseline in only one of four cases
description: Curvature-based maximum-sum paths significantly reduce forgetting versus minimum-sum paths across four datasets, but beat a random baseline in only one of four cases
id: curvature-max-path-forgetting-mixed-vs-random
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: mixed
newest_evidence: 2022
sources:
  - id: samuel-j-bell-and-neil-d-lawrence-2022
    resource: "https://doi.org/10.48550/arXiv.2205.13323"
    title: "Samuel J. Bell and Neil D. Lawrence. (2022). The Effect of Task Ordering in Continual Learning. Preprint. Under review. [doi:10.48550/arXiv.2205.13323](https://doi.org/10.48550/arXiv.2205.13323)"
    author: Samuel J. Bell and Neil D. Lawrence
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Curvature-based maximum-sum paths significantly reduce forgetting versus minimum-sum paths across four datasets, but beat a random baseline in only one of four cases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across synthetic gratings, split MNIST, CIFAR-10 and CIFAR-100, maximum-curvature paths significantly reduce average forgetting versus minimum-curvature paths, but only outperform the random baseline on split MNIST. [→ Samuel J. Bell and Neil D. Lawrence 2022](#samuel-j-bell-and-neil-d-lawrence-2022)

## Evidence

### Samuel J. Bell and Neil D. Lawrence 2022

Samuel J. Bell and Neil D. Lawrence. (2022). The Effect of Task Ordering in Continual Learning. Preprint. Under review. [doi:10.48550/arXiv.2205.13323](https://doi.org/10.48550/arXiv.2205.13323)

`q2 · i?` · `causal · r2`

Numerical experiments summarized in Table 1: mean max-minus-min forgetting changes of -0.065 (gratings), -0.098 (MNIST), -0.105 (CIFAR-10) and -0.035 (CIFAR-100), with MNIST also showing a significant -0.053 versus random. Random-path comparisons were not significant after correction in three of four cases.

> "we find a consistent and significant difference across all experiments between the maximum and minimum sum paths, i.e. taking the path of maximum curvature through task space results in the lowest average forgetting. However, this is only sufficient to outperform the random baseline in one of four cases, with the ReLU net on split MNIST."

## Discussion


## Related Claims
- With true task distances, the maximum-sum path through task space reduces forgetting relative to the minimum-sum path, though neither differs significantly from a random path — related
- The effect of task ordering on forgetting decreases as the number of tasks in the sequence grows — related
