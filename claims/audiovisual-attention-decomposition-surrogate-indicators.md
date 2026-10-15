---
type: claim
title: Audiovisual attention decomposition via forward encoding and variance partitioning yields VAC, AAC, and SAC as surrogate indicators, not direct measures of attention
description: Audiovisual attention decomposition via forward encoding and variance partitioning yields VAC, AAC, and SAC as surrogate indicators, not direct measures of attention
id: audiovisual-attention-decomposition-surrogate-indicators
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: shixian-zhou-2026
    resource: "https://doi.org/10.48550/arxiv.2607.29413"
    title: "Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou. (2026). SAVVY: Student Attention Visualization for Video-based Learning Analysis. arXiv. https://arxiv.org/abs/2607.29413 [doi:10.48550/arxiv.2607.29413](https://doi.org/10.48550/arxiv.2607.29413)"
    author: Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: shixian-zhou-2026-2
    resource: "https://arxiv.org/abs/2607.29413"
    title: "Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou. (2026). SAVVY: Student Attention Visualization for Video-based Learning Analysis. arXiv. https://arxiv.org/abs/2607.29413"
    author: Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Audiovisual attention decomposition via forward encoding and variance partitioning yields VAC, AAC, and SAC as surrogate indicators, not direct measures of attention

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` Attentional resource allocation across visual and auditory channels is computed via forward encoding and variance partitioning, separating explained variance into Visual, Auditory, and Shared Audiovisual Attention Contributions. [→ Shixian Zhou 2026](#shixian-zhou-2026)
`q2 i?` The three components are empirical surrogate indicators and do not directly measure attention as an internal state. [→ Shixian Zhou 2026 (2)](#shixian-zhou-2026-2)

## Evidence

### Shixian Zhou 2026

Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou. (2026). SAVVY: Student Attention Visualization for Video-based Learning Analysis. arXiv. https://arxiv.org/abs/2607.29413 [doi:10.48550/arxiv.2607.29413](https://doi.org/10.48550/arxiv.2607.29413)

`q2 · i?` · `design · r2`

Methodological description from the Audiovisual Attention Decomposition subsection. A multi-time-lag linear encoding model estimates variance in neural data explained by each modality, then variance partitioning separates it into VAC, AAC, and SAC.

> "Following Desai et al. [77], we compute attentional resource allocation across visual and auditory channels via forward encoding and variance partitioning."

### Shixian Zhou 2026 (2)

Shixian Zhou, Minghuan Shen, Xiaolin Wen, Zijun Qiu, Yongliang Jiang, Xiangyang Wu, Fei Wu, Yong Wang, and Zhiguang Zhou. (2026). SAVVY: Student Attention Visualization for Video-based Learning Analysis. arXiv. https://arxiv.org/abs/2607.29413

`q2 · i?` · `design · r2`

The authors' own scope limit on the decomposition: the components "do not directly measure attention as an internal state" but provide auxiliary cues for teachers' exploratory analysis.

> "These three components are empirical surrogate indicators of the relative involvement of visual, auditory, and shared audiovisual processing. They do not directly measure attention as an internal state."

## Discussion


## Related Claims
- [Avoiding double load on the visual channel improves visual knowledge (channel-overload effect)](voice-media-outperform-picture-text-overall.md) — related
- [In one 37-student classroom experiment, recall and retention differ across media combinations in the direction Dual Coding Theory predicts](media-combinations-affect-recall-and-retention.md) — related
- [Matching modality by conveying complementary information through auditory and visual channels increases retention, transfer, and engagement](modality-matching-complementary-channels-video.md) — related
