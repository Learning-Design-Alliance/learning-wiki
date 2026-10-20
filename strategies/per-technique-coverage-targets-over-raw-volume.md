---
type: strategy
id: per-technique-coverage-targets-over-raw-volume
title: Set per-technique coverage targets rather than scaling raw volume when constructing domain-specific instruction datasets
description: "A dataset-construction strategy drawn from the paper's per-technique fidelity analysis: technique fidelity scores stabilize only once a technique is represented by a minimum number of high-fidelity examples (roughly 2..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: shwetha-singaravelu-2026
    resource: "https://arxiv.org/abs/2607.23322"
    title: "Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani. (2026). IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems. arXiv. https://arxiv.org/abs/2607.23322"
    author: Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani
---

# Set per-technique coverage targets rather than scaling raw volume when constructing domain-specific instruction datasets

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A dataset-construction strategy drawn from the paper's per-technique fidelity analysis: technique fidelity scores stabilize only once a technique is represented by a minimum number of high-fidelity examples (roughly 200 to 500 pairs per technique). The paper states "The implication for instruction dataset construction is to set per-technique coverage targets rather than to scale raw volume." More complex step-sequence techniques require more examples, while simpler techniques converge with fewer.

## Design Implications

### Context
#### Requirements
- Per-technique Teacher Fidelity tracking to identify when each technique's scores stabilize
#### Constraints
- The authors frame this as a data-composition guideline grounded in per-technique trends, not a model-ranking claim, since version-level model scores did not cleanly separate

### Target Learners
- Builders of domain-specific instruction datasets for specialized educational domains

### Target Learning Goals
- Constructing instruction data that yields stable technique-fidelity performance in fine-tuned models

## Claims

- [Model-level judge quality is non-monotonic in dataset size: the 13,882-pair v1.1 yields the best model (6.39), while both expansion to ~20,000 pairs (6.33) and aggressive curation to 7,130 pairs (6.12) reduce quality](../claims/non-monotonic-quality-volume-iks-instruct.md) [+M] (more pairs did not mean a better model)

## Related Strategies
- 

## Examples

- [IKS-Instruct dataset](../products/iks-instruct-dataset.md): the instruction dataset the guideline was drawn from

## Key Sources
- Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani. (2026). IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems. arXiv. https://arxiv.org/abs/2607.23322
