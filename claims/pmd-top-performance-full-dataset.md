---
type: claim
title: In full-dataset fine-tuning, the proposed difficulty-based sampling strategies, especially PMD, achieve top performance on multiple datasets for both BERT and RoBERTa
description: In full-dataset fine-tuning, the proposed difficulty-based sampling strategies, especially PMD, achieve top performance on multiple datasets for both BERT and RoBERTa
id: pmd-top-performance-full-dataset
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

# In full-dataset fine-tuning, the proposed difficulty-based sampling strategies, especially PMD, achieve top performance on multiple datasets for both BERT and RoBERTa

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` PMD yields top performance on multiple datasets for both backbone models, especially SST-2 and XNLI. [→ Qi Feng 2025](#qi-feng-2025)

## Evidence

### Qi Feng 2025

Qi Feng, Yihong Liu, Hinrich Schütze. (2025). Your Pretrained Model Tells the Difficulty Itself: A Self-Adaptive Curriculum Learning Paradigm for Natural Language Understanding. arXiv preprint. [doi:10.18653/v1/2025.acl-srw.15](https://doi.org/10.18653/v1/2025.acl-srw.15)

`q2 · i?` · `causal · r2`

Comparison of sampling strategies and Random/Length baselines across SST-2, SST-5, HSOL and XNLI (Table 1), averaged over 3 random seeds, reporting accuracy, F1, precision and recall. The authors' interpretation attributes PMD's consistency to its dynamic sampling mechanism.

> "The PMD strategy yields top performance (highlighted in bold) on multiple datasets for both BERT and RoBERTa, especially on SST-2 and XNLI. Its consistent superiority suggests that its dynamic sampling mechanism effectively emphasizes worth-learning examples during training."

## Discussion


## Related Claims
- Dataset difficulty moderates the benefit of difficulty-based sampling: performance differences are more pronounced on challenging datasets like SST-5 and XNLI than on easier ones — related
- Early in fine-tuning, strategies exposing difficult examples (D2E, PME, PMD, SMD) show a clear accuracy advantage at the first checkpoint on SST-2 — related
- In few-shot fine-tuning with 64 instances, most proposed sampling strategies outperform both baselines on SST-2 and SST-5 except E2D, indicating hard examples are particularly important in few-shot learning — related
- [On the imbalanced HSOL dataset, proposed sampling strategies such as PME and SME consistently achieve higher F1 scores than baselines](sampling-strategies-f1-advantage-imbalanced-hsol.md) — related
