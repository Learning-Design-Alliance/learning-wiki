---
type: claim
title: "Analytically, the DR estimator's bias is bounded by the product of propensity and imputation errors, and its generalization bound contains a variance term scaling with squared imputation error"
description: "Analytically, the DR estimator's bias is bounded by the product of propensity and imputation errors, and its generalization bound contains a variance term scaling with squared imputation error"
id: dr-bias-product-and-variance-bound
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: peilin-zhan-2026
    resource: "https://doi.org/10.48550/arxiv.2605.05958"
    title: "Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958 [doi:10.48550/arxiv.2605.05958](https://doi.org/10.48550/arxiv.2605.05958)"
    author: Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: peilin-zhan-2026-2
    resource: "https://arxiv.org/abs/2605.05958"
    title: "Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958"
    author: Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Analytically, the DR estimator's bias is bounded by the product of propensity and imputation errors, and its generalization bound contains a variance term scaling with squared imputation error

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Lemma 1 proves the DR estimator is unbiased if either the propensity model or the imputation model is accurate, with bias bounded by the product of the two models' errors. [→ Peilin Zhan 2026](#peilin-zhan-2026)
`q2 i?` Theorem 1 derives a generalization bound whose variance term scales with squared imputation error, motivating temporal smoothness to tighten the bound. [→ Peilin Zhan 2026 (2)](#peilin-zhan-2026-2)

## Evidence

### Peilin Zhan 2026

Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958 [doi:10.48550/arxiv.2605.05958](https://doi.org/10.48550/arxiv.2605.05958)

`q2 · i?` · `design · r2`

Analytical derivation (Lemma 1, Section 4.3) with proof sketch in the article and full proofs in Appendix F. The article states the bias bound confirms the double robustness property and yields second-order error decay when both models are learned with expressive estimators.

> "The bias of the DR estimator is bounded by the product of the errors of the two auxiliary models"

### Peilin Zhan 2026 (2)

Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai. (2026). Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing. https://arxiv.org/abs/2605.05958

`q2 · i?` · `design · r2`

Analytical derivation (Theorem 1, Section 4.4) using the Azuma-Hoeffding inequality over the sequential interaction structure. The article states inaccuracy in the imputation model loosens the bound and leads to unstable training, motivating the temporal smoothness constraint.

> "the total generalization error is dominated not just by the bias product but also by the Variance Term, which scales with the squared imputation errorδ 2
t,c"

## Discussion


## Related Claims
-
