---
type: claim
title: Raw video features degrade teacher sentiment classification, while LLM-generated video descriptions improve it
description: Raw video features degrade teacher sentiment classification, while LLM-generated video descriptions improve it
id: raw-video-noise-video-descriptions-help-t-med
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

# Raw video features degrade teacher sentiment classification, while LLM-generated video descriptions improve it

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Adding raw video features to text plus audio lowers weighted accuracy and weighted F1, whereas replacing raw video with video description text raises both metrics. [→ Zhiyi Duan 2026](#zhiyi-duan-2026)

## Evidence

### Zhiyi Duan 2026

Zhiyi Duan, Xiangren Wang, Hongyu Yuan, Qianli Xing. (2026). Advancing Multimodal Teacher Sentiment Analysis: The Large-Scale T-MED Dataset & The Effective AAM-TSA Model. arXiv preprint. Originally published 2025. [doi:10.1609/aaai.v40i3.37157](https://doi.org/10.1609/aaai.v40i3.37157)

`q2 · i?` · `design · r2`

Modality-variant experiments (Table 3 and Appendix E.1): raw-video Var-TARV fell below text+audio Var-TA, and replacing raw video with descriptions in Var-TAVD increased WA by 0.40% and W-F1 by 0.36% over Var-TARV; replacing it in Var-TARVI decreased WA by 1.00% and W-F1 by 1.15%.

> "Compared with the Var-TA model, the Var-TARV model shows a decrease of 0.60% in terms of W A and 0.66% in terms of W-F1."

## Discussion


## Related Claims
- [AAM-TSA outperforms state-of-the-art multimodal sentiment baselines on the T-MED teacher sentiment benchmark](aam-tsa-outperforms-multimodal-baselines-t-med.md) — related
- [Audio is the core carrier of teacher emotional expression: audio-only features outperform text-only and video-description-only variants](audio-core-carrier-teacher-emotion-t-med.md) — related
- [Instructional information (subject and educational stage) improves teacher sentiment classification when embedded as a modality](instructional-information-modality-improves-teacher-sentiment.md) — related
