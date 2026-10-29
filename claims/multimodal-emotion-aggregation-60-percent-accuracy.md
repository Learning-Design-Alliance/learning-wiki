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
newest_evidence: 2025
recheck_by: 2028
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
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

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
- [Text-based emotional expression in student responses showed no statistically significant differences between Emotion ON and OFF conditions](no-textual-emotion-difference-emotion-on.md) — related
- [Adding student-emotion information to LLM tutor prompting produces more desirable pedagogical qualities across most evaluated dimensions, with larger models benefiting most](emotion-aware-prompting-improves-pedagogical-quality.md) — related
- [Facial expression recognition of six basic emotions via FACS can detect learner emotional states in real time](facs-six-basic-emotions-detection.md) — related
- [An intelligent affective tutoring system recognizing facial expressions reduced anxiety and improved Japanese learning](affective-tutoring-reduces-japanese-learning-anxiety.md) — related
