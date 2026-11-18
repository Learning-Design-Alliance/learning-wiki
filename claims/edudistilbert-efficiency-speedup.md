---
type: claim
title: "The distilled EduDistilBERT delivers the best or near-best results while lowering computational cost, including a 30% inference speedup over the full model"
description: "The distilled EduDistilBERT delivers the best or near-best results while lowering computational cost, including a 30% inference speedup over the full model"
id: edudistilbert-efficiency-speedup
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

# The distilled EduDistilBERT delivers the best or near-best results while lowering computational cost, including a 30% inference speedup over the full model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2019 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2022**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` EduDistilBERT achieves the best results on two of the three tasks while having a lower memory footprint and faster inference, allowing a 30% speedup. [→ Benjamin Clavié 2019](#benjamin-clavie-2019)

## Evidence

### Benjamin Clavié 2019

Benjamin Clavié, Kobi Gal. (2019). EduBERT: Pretrained Deep Language Models for Learning Analytics. Companion Proceedings 10th International Conference on Learning Analytics & Knowledge (LAK20). [doi:10.48550/arXiv.1912.00690](https://doi.org/10.48550/arXiv.1912.00690)

`q2 · i?` · `design · r2`

Authors' reported comparison of the distilled and full models in the Results & Discussions section: EduDistilBERT "has a lower memory footprint and is noticeably faster at inference time", yielding the printed 30% speedup figure.

> "However, EduDistilBERT has a lower memory footprint and is noticeably faster at inference time, allowing for a 30% speedup."

## Discussion


## Related Claims
- [Pretraining on MOOC forum data improves urgency-prediction performance beyond the state of the art, with EduDistilBERT achieving the best overall performance](edubert-urgency-detection-beats-state-of-art.md) — related
