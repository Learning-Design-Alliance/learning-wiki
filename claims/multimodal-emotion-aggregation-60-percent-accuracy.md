---
type: claim
title: "MathBuddy's multimodal emotion aggregation matched participant-reviewed emotions at 60% overall accuracy, with sharply reduced recall for the Neutral class"
description: "MathBuddy's multimodal emotion aggregation matched participant-reviewed emotions at 60% overall accuracy, with sharply reduced recall for the Neutral class"
id: multimodal-emotion-aggregation-60-percent-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: debanjana-kar-2025
    resource: "https://doi.org/10.48550/arxiv.2508.19993"
    title: "Debanjana Kar, Leopold Böss, Dacia Braca, Sebastian Dennerlein, Nina Hubig, Philipp Wintersberger, and Yufang Hou. (2025). MathBuddy: A Multimodal System for Affective Math Tutoring. https://arxiv.org/abs/2508.19993 [doi:10.48550/arxiv.2508.19993](https://doi.org/10.48550/arxiv.2508.19993)"
    author: Debanjana Kar, Leopold Böss, Dacia Braca, Sebastian Dennerlein, Nina Hubig, Philipp Wintersberger, and Yufang Hou
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# MathBuddy's multimodal emotion aggregation matched participant-reviewed emotions at 60% overall accuracy, with sharply reduced recall for the Neutral class

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Compared against participants' gold annotations of their own emotions, the aggregated text-plus-face emotion detection reached 60% overall accuracy, with Neutral recall falling to 0.15. [→ Debanjana Kar 2025](#debanjana-kar-2025)

## Evidence

### Debanjana Kar 2025

Debanjana Kar, Leopold Böss, Dacia Braca, Sebastian Dennerlein, Nina Hubig, Philipp Wintersberger, and Yufang Hou. (2025). MathBuddy: A Multimodal System for Affective Math Tutoring. https://arxiv.org/abs/2508.19993 [doi:10.48550/arxiv.2508.19993](https://doi.org/10.48550/arxiv.2508.19993)

`q2 · i?` · `design · r2`

User-study participants reviewed and corrected the system's predicted emotions in Emotion ON conversations; aggregated multimodal predictions were compared to these gold annotations (Table 5: Negative precision 0.57/recall 0.98; Neutral 0.71/0.15; Positive 0.79/0.41).

> "the system achieves an overall accuracy of 60% in real-time usage. However, we observe a sharp fall in the recall scores for theNeutralclass"

## Discussion


## Related Claims
- [In a within-subject user study, participants showed longer positive facial expressions under the emotion-aware (Emotion ON) tutoring condition](emotion-on-longer-positive-facial-expressions.md) — related
- [Emotion features improve tutor performance only when grounded in education-theory-based pedagogical strategies; emotion information alone misguides a smaller model](emotion-plus-theory-prompting-ablation-gain.md) — related
