---
type: claim
title: Weight normalization substantially improves robustness to hyperparameters and final learner performance in meta-gradient training of GTNs
description: Weight normalization substantially improves robustness to hyperparameters and final learner performance in meta-gradient training of GTNs
id: weight-normalization-stabilizes-meta-gradient-gtn-training
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
    rigour: 1
---

# Weight normalization substantially improves robustness to hyperparameters and final learner performance in meta-gradient training of GTNs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Such 2019: the intervention came bundled with another change (read from the study by two models, 2026-11-23)

## Subclaims
`q2 i?` Applying weight normalization to the generator and learner weights improves the stability of meta-gradient optimization of GTNs, reducing hyperparameter sensitivity. [→ Such 2019](#such-2019)

## Evidence

### Such 2019

Such, F. P., Rawal, A., Lehman, J., Stanley, K. O., & Clune, J. (2019). Generative Teaching Networks: Accelerating Neural Architecture Search by Learning to Generate Synthetic Training Data. Uber AI Labs. [doi:10.48550/arXiv.1912.07768](https://doi.org/10.48550/arXiv.1912.07768)

`q2 · i?` · `causal · r1`

Hyperparameter optimization comparison of GTNs with and without weight normalization on MNIST; Figure 1b shows the distribution of final loss for 20 runs obtained during hyperparameter optimization with Bayesian Optimization. The authors report that weight normalization "substantially improved robustness to hyperparameters and ﬁnal learner performance". No effect size is printed.

> "Overall, weight normalization substantially improved robustness to hyperparameters and ﬁnal learner performance, supporting the initial hypothesis."

## Discussion


## Related Claims
- [GTN-produced synthetic data generalizes to learner architectures never seen during meta-training](gtn-synthetic-data-generalizes-across-architectures.md) — related
- [Hyperparameter sensitivity in PKT is an inherent characteristic of programming interaction data, varying across models and across assignments within the same model](pkt-hyperparameter-sensitivity-varies-by-model-and-assignment.md) — related
