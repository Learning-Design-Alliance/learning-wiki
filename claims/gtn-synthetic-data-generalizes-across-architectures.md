---
type: claim
title: GTN-produced synthetic data generalizes to learner architectures never seen during meta-training
description: GTN-produced synthetic data generalizes to learner architectures never seen during meta-training
id: gtn-synthetic-data-generalizes-across-architectures
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2019
sources:
  - id: such-2019
    resource: "https://doi.org/10.48550/arXiv.1912.07768"
    title: "Such, F. P., Rawal, A., Lehman, J., Stanley, K. O., & Clune, J. (2019). Generative Teaching Networks: Accelerating Neural Architecture Search by Learning to Generate Synthetic Training Data. Uber AI Labs. [doi:10.48550/arXiv.1912.07768](https://doi.org/10.48550/arXiv.1912.07768)"
    author: "Such, F. P., Rawal, A., Lehman, J., Stanley, K. O., & Clune, J."
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# GTN-produced synthetic data generalizes to learner architectures never seen during meta-training

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` A GTN meta-trained only on small proxy learners still produces synthetic data effective for training architectures from the NAS search space it was never trained on. [→ Such 2019](#such-2019)

## Evidence

### Such 2019

Such, F. P., Rawal, A., Lehman, J., Stanley, K. O., & Clune, J. (2019). Generative Teaching Networks: Accelerating Neural Architecture Search by Learning to Generate Synthetic Training Data. Uber AI Labs. [doi:10.48550/arXiv.1912.07768](https://doi.org/10.48550/arXiv.1912.07768)

`q2 · i?` · `causal · r2`

CIFAR10 NAS experiments in which the GTN was meta-trained ahead of time on smaller fully-convolutional proxy learners (8h on one p6000 GPU) rather than on the search-space architectures. The authors report that "synthetic data from GTNs were still effective for training them", supporting learner-agnostic data generation. No effect size is printed.

> "Interestingly, although we never train our GTN on any NAS architectures, because of generalization, synthetic data from GTNs were still effective for training them."

## Discussion


## Related Claims
- GTN evaluation rank-correlates with standard search evaluation on CIFAR10, reaching 0.5582 for the top half of architectures at roughly 9x lower cost — related
- [A fully learned curriculum (deterministic ordering of generator inputs) makes GTN training more effective than other curriculum variants](gtn-full-curriculum-outperforms-other-variants.md) — related
- [Weight normalization substantially improves robustness to hyperparameters and final learner performance in meta-gradient training of GTNs](weight-normalization-stabilizes-meta-gradient-gtn-training.md) — related
