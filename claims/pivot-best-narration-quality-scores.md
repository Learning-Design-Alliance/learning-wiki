---
type: claim
title: PIVOT achieves the best automatic narration-quality scores on Accuracy and Logical Flow dimensions
description: PIVOT achieves the best automatic narration-quality scores on Accuracy and Logical Flow dimensions
id: pivot-best-narration-quality-scores
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: xinchen-ma-2026
    resource: "https://arxiv.org/abs/2609.24083"
    title: "Xinchen Ma, Shuimu Wang, Gaole He, Yanbin Zhang, Chunyang Wang, Yunshi Lan, Weining Qian. (2026). From Content Generation to Learning Support: Pedagogy-Guided Generative Video Tutors for STEM Learning. https://arxiv.org/abs/2609.24083"
    author: Xinchen Ma, Shuimu Wang, Gaole He, Yanbin Zhang, Chunyang Wang, Yunshi Lan, Weining Qian
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# PIVOT achieves the best automatic narration-quality scores on Accuracy and Logical Flow dimensions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` GPT-4o-scored narration quality shows PIVOT highest (Overall 0.89) versus TheoremExplainAgent (0.84) and Code2Video (0.75). [→ Xinchen Ma 2026](#xinchen-ma-2026)

## Evidence

### Xinchen Ma 2026

Xinchen Ma, Shuimu Wang, Gaole He, Yanbin Zhang, Chunyang Wang, Yunshi Lan, Weining Qian. (2026). From Content Generation to Learning Support: Pedagogy-Guided Generative Video Tutors for STEM Learning. https://arxiv.org/abs/2609.24083

`q2 · i?` · `design · r2`

Narration fields extracted from generated scripts were independently scored by GPT-4o on Accuracy and Depth and Logical Flow (0-1), with the final transcript score as their arithmetic mean; the table shows "PIVOT0.87 0.91 0.89". No statistical test is reported.

> "Method Accuracy Logical Overall TheoremExplainAgent 0.85 0.82 0.84 Code2video 0.78 0.72 0.75 PIVOT0.87 0.91 0.89"

## Discussion


## Related Claims
- [Expert evaluators rate PIVOT higher than TheoremExplainAgent across nearly all instructional dimensions, with the largest gains in Physics and Computer Science](expert-evaluation-pivot-outperforms-baseline.md) — related
- [PIVOT achieves the best automatic video-quality scores among the compared educational video generation methods on 40 STEM topics](pivot-best-automatic-video-quality-scores.md) — related
- [Each pedagogical verification component contributes to a distinct quality dimension: layout verification most strongly](verification-components-ablation-contributions.md) — related
- [Current AI instructional-video systems score higher on content dimensions (Accuracy, Logic) than on delivery dimensions (Engagement, Adaptability), with Adaptability lowest](ai-video-systems-content-stronger-than-delivery.md) — related
