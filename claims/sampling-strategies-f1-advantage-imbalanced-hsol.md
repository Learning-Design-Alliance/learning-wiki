---
type: claim
title: On the imbalanced HSOL dataset, proposed sampling strategies such as PME and SME consistently achieve higher F1 scores than baselines
description: On the imbalanced HSOL dataset, proposed sampling strategies such as PME and SME consistently achieve higher F1 scores than baselines
id: sampling-strategies-f1-advantage-imbalanced-hsol
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: qi-feng-2025
    resource: "https://doi.org/10.18653/v1/2025.acl-srw.15"
    title: "Qi Feng, Yihong Liu, Hinrich Schütze. (2025). Your Pretrained Model Tells the Difficulty Itself: A Self-Adaptive Curriculum Learning Paradigm for Natural Language Understanding. arXiv preprint. [doi:10.18653/v1/2025.acl-srw.15](https://doi.org/10.18653/v1/2025.acl-srw.15)"
    author: Qi Feng, Yihong Liu, Hinrich Schütze
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# On the imbalanced HSOL dataset, proposed sampling strategies such as PME and SME consistently achieve higher F1 scores than baselines

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` On HSOL, which exhibits label imbalance, PME and SME consistently achieve higher F1 scores compared to baselines. [→ Qi Feng 2025](#qi-feng-2025)

## Evidence

### Qi Feng 2025

Qi Feng, Yihong Liu, Hinrich Schütze. (2025). Your Pretrained Model Tells the Difficulty Itself: A Self-Adaptive Curriculum Learning Paradigm for Natural Language Understanding. arXiv preprint. [doi:10.18653/v1/2025.acl-srw.15](https://doi.org/10.18653/v1/2025.acl-srw.15)

`q2 · i?` · `causal · r2`

Full-dataset fine-tuning results on the imbalanced HSOL dataset (Table 1, §5.1). The authors interpret this as promoting better representation of minority or harder-to-learn classes, improving the balance between precision and recall.

> "In datasets like HSOL, which exhibit label imbalance or fine-grained distinctions, our sampling strategies, such as PME and SME, consistently achieve higher F1 scores compared to baselines."

## Discussion


## Related Claims
- [In full-dataset fine-tuning, the proposed difficulty-based sampling strategies, especially PMD, achieve top performance on multiple datasets for both BERT and RoBERTa](pmd-top-performance-full-dataset.md) — related
- Dataset difficulty moderates the benefit of difficulty-based sampling: performance differences are more pronounced on challenging datasets like SST-5 and XNLI than on easier ones — reports the opposite
- In few-shot fine-tuning with 64 instances, most proposed sampling strategies outperform both baselines on SST-2 and SST-5 except E2D, indicating hard examples are particularly important in few-shot learning — related
