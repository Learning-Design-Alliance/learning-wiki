---
type: claim
title: Pretraining on MOOC forum data improves urgency-prediction performance beyond the state of the art, with EduDistilBERT achieving the best overall performance
description: Pretraining on MOOC forum data improves urgency-prediction performance beyond the state of the art, with EduDistilBERT achieving the best overall performance
id: edubert-urgency-detection-beats-state-of-art
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2019
recheck_by: 2022
sources:
  - id: benjamin-clavié-2019
    resource: "https://doi.org/10.48550/arXiv.1912.00690"
    title: "Benjamin Clavié, Kobi Gal. (2019). EduBERT: Pretrained Deep Language Models for Learning Analytics. Companion Proceedings 10th International Conference on Learning Analytics & Knowledge (LAK20). [doi:10.48550/arXiv.1912.00690](https://doi.org/10.48550/arXiv.1912.00690)"
    author: Benjamin Clavié, Kobi Gal
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Pretraining on MOOC forum data improves urgency-prediction performance beyond the state of the art, with EduDistilBERT achieving the best overall performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On urgency prediction of MOOC forum posts, EduBERT and EduDistilBERT outperform the state-of-the-art model of Guo et al. (2019) on F1 and weighted F1, with EduDistilBERT best overall (weighted F1 0.925). [→ Benjamin Clavié 2019](#benjamin-clavie-2019)

## Evidence

### Benjamin Clavié 2019

Benjamin Clavié, Kobi Gal. (2019). EduBERT: Pretrained Deep Language Models for Learning Analytics. Companion Proceedings 10th International Conference on Learning Analytics & Knowledge (LAK20). [doi:10.48550/arXiv.1912.00690](https://doi.org/10.48550/arXiv.1912.00690)

`q2 · i?` · `design · r2`

Evaluation on the Stanford MOOCPosts urgency-prediction task, comparing EduBERT, EduDistilBERT, BERT-base and DistilBERT against Guo et al. (2019). All pretraining approaches "outperformed the SoA for F1 and weighted F1 measures"; EduDistilBERT reached weighted F1 0.925 versus 0.918 for the prior state of the art.

> "The table shows that all pretraining approaches outperformed the SoA for F1 and weighted F1 measures, with our distilled model EduDistilBERT achieving the best overall performance."

## Discussion


## Related Claims
- [The distilled EduDistilBERT delivers the best or near-best results while lowering computational cost, including a 30% inference speedup over the full model](edudistilbert-efficiency-speedup.md) — related
- [Multi-label BERT classifiers slightly outperformed single-label Random Forest baselines on example-based F1 scores but under-performed with lower exact match ratios on MOOC cognitive presence classification](multi-label-bert-f1-beats-rf-exact-match-lower.md) — related
