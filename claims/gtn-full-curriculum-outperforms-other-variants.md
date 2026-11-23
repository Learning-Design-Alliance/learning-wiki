---
type: claim
title: A fully learned curriculum (deterministic ordering of generator inputs) makes GTN training more effective than other curriculum variants
description: A fully learned curriculum (deterministic ordering of generator inputs) makes GTN training more effective than other curriculum variants
id: gtn-full-curriculum-outperforms-other-variants
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

# A fully learned curriculum (deterministic ordering of generator inputs) makes GTN training more effective than other curriculum variants

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` GTN - Full Curriculum, which learns both the order of presented samples and the specific group of samples, outperforms the No Curriculum, All Shuffled, and Shuffled Batch variants. [→ Such 2019](#such-2019)

## Evidence

### Such 2019

Such, F. P., Rawal, A., Lehman, J., Stanley, K. O., & Clune, J. (2019). Generative Teaching Networks: Accelerating Neural Architecture Search by Learning to Generate Synthetic Training Data. Uber AI Labs. [doi:10.48550/arXiv.1912.07768](https://doi.org/10.48550/arXiv.1912.07768)

`q2 · i?` · `causal · r2`

Experimental comparison of four GTN variants with increasing control over the ordering of z codes input to the generator, plotting learner test accuracy across outer-loop iterations (Figure 1c). The full-curriculum variant "outperforms all other variants", and the authors adopt it for all subsequent GTN experiments. No effect size is printed.

> "Overall, training the GTN with exact ordering of input samples (GTN - Full Curriculum) outperforms all other variants."

## Discussion


## Related Claims
- GTN evaluation rank-correlates with standard search evaluation on CIFAR10, reaching 0.5582 for the top half of architectures at roughly 9x lower cost — related
- [Example-first conditions outperformed problem-first conditions on an immediate circuit test](worked-example-problem-sequences.md) — related
- [GTN-produced synthetic data generalizes to learner architectures never seen during meta-training](gtn-synthetic-data-generalizes-across-architectures.md) — related
- Random shuffling of training data is not essential: systems trained on coherent original-order data perform on par with, or better than, shuffled systems — related
- [Curriculum learning with easy-to-hard data ordering yields better final performance than shuffled vanilla learning on both benchmarks](yoda-curriculum-learning-improves-robustness.md) — related
- [Problem-difficulty-based curricula consistently outperform random shuffling, with gains of up to 3–6% on easier datasets](problem-difficulty-curricula-beat-shuffled-baseline.md) — related
