---
type: claim
title: PIVOT achieves the best automatic video-quality scores among the compared educational video generation methods on 40 STEM topics
description: PIVOT achieves the best automatic video-quality scores among the compared educational video generation methods on 40 STEM topics
id: pivot-best-automatic-video-quality-scores
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: xinchen-ma-2026
    resource: "https://doi.org/10.48550/arxiv.2609.24083"
    title: "Xinchen Ma, Shuimu Wang, Gaole He, Yanbin Zhang, Chunyang Wang, Yunshi Lan, Weining Qian. (2026). From Content Generation to Learning Support: Pedagogy-Guided Generative Video Tutors for STEM Learning. https://arxiv.org/abs/2609.24083 [doi:10.48550/arxiv.2609.24083](https://doi.org/10.48550/arxiv.2609.24083)"
    author: Xinchen Ma, Shuimu Wang, Gaole He, Yanbin Zhang, Chunyang Wang, Yunshi Lan, Weining Qian
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# PIVOT achieves the best automatic video-quality scores among the compared educational video generation methods on 40 STEM topics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` On VLM-scored Layout and Richness dimensions across 40 STEM topics, PIVOT scores higher (Overall 7.58) than TheoremExplainAgent (6.62) and Code2Video (6.20). [→ Xinchen Ma 2026](#xinchen-ma-2026)

## Evidence

### Xinchen Ma 2026

Xinchen Ma, Shuimu Wang, Gaole He, Yanbin Zhang, Chunyang Wang, Yunshi Lan, Weining Qian. (2026). From Content Generation to Learning Support: Pedagogy-Guided Generative Video Tutors for STEM Learning. https://arxiv.org/abs/2609.24083 [doi:10.48550/arxiv.2609.24083](https://doi.org/10.48550/arxiv.2609.24083)

`q2 · i?` · `design · r2`

Automatic evaluation using Gemini-2.5-Flash under deterministic decoding scored sampled video frames on Layout and Richness (1-10) for all methods on the same 40 STEM topics; the table shows "PIVOT9.10 6.06 7.58" versus 6.62 and 6.20 overall for the baselines. No statistical test is reported.

> "Method Layout Richness Overall TheoremExplainAgent 9.00 4.23 6.62 Code2video 8.18 4.22 6.20 PIVOT9.10 6.06 7.58"

## Discussion


## Related Claims
- [Expert evaluators rate PIVOT higher than TheoremExplainAgent across nearly all instructional dimensions, with the largest gains in Physics and Computer Science](expert-evaluation-pivot-outperforms-baseline.md) — related
- [Students and teachers responded positively to automatically generated textbook videos, finding explanations easier to follow than plain text](generated-textbook-videos-easier-to-follow-than-plain-text.md) — related
- [PIVOT achieves the best automatic narration-quality scores on Accuracy and Logical Flow dimensions](pivot-best-narration-quality-scores.md) — related
- [Each pedagogical verification component contributes to a distinct quality dimension: layout verification most strongly](verification-components-ablation-contributions.md) — related
- [Current AI instructional-video systems score higher on content dimensions (Accuracy, Logic) than on delivery dimensions (Engagement, Adaptability), with Adaptability lowest](ai-video-systems-content-stronger-than-delivery.md) — related
- [MAIC's script generation function outscores baseline and human script generation on five Likert-rated dimensions](maic-funcgen-outperforms-baselines.md) — related
