---
type: claim
title: Instructional information (subject and educational stage) improves teacher sentiment classification when embedded as a modality
description: Instructional information (subject and educational stage) improves teacher sentiment classification when embedded as a modality
id: instructional-information-modality-improves-teacher-sentiment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: zhiyi-duan-2026
    resource: "https://doi.org/10.1609/aaai.v40i3.37157"
    title: "Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing. (2026). Advancing Multimodal Teacher Sentiment Analysis: The Large-Scale T-MED Dataset & The Effective AAM-TSA Model. arXiv preprint. Originally published 2025. [doi:10.1609/aaai.v40i3.37157](https://doi.org/10.1609/aaai.v40i3.37157)"
    author: Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Instructional information (subject and educational stage) improves teacher sentiment classification when embedded as a modality

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Removing the instructional information feature embedding module from AAM-TSA reduces weighted accuracy and weighted F1 on T-MED. [→ Zhiyi Duan 2026](#zhiyi-duan-2026)

## Evidence

### Zhiyi Duan 2026

Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing. (2026). Advancing Multimodal Teacher Sentiment Analysis: The Large-Scale T-MED Dataset & The Effective AAM-TSA Model. arXiv preprint. Originally published 2025. [doi:10.1609/aaai.v40i3.37157](https://doi.org/10.1609/aaai.v40i3.37157)

`q2 · i?` · `design · r2`

Ablation experiment (Table 4) constructing Var-CIHF by removing the instructional information feature embedding module; the authors conclude "the introduction of school stage and subject as instructional information is crucial to understanding the situational dependence of teachers' emotional expression".

> "Compared with the AAM-TSA, the W A and W-F1 decrease 0.87% and 1.27%, respectively."

## Discussion


## Related Claims
- [AAM-TSA outperforms state-of-the-art multimodal sentiment baselines on the T-MED teacher sentiment benchmark](aam-tsa-outperforms-multimodal-baselines-t-med.md) — related
- [Joint training of the feature encoders contributes the largest single-module ablation loss in AAM-TSA](joint-training-crucial-aam-tsa-ablation.md) — related
- [Raw video features degrade teacher sentiment classification, while LLM-generated video descriptions improve it](raw-video-noise-video-descriptions-help-t-med.md) — related
