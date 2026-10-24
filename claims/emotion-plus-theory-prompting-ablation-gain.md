---
type: claim
title: Emotion features improve tutor performance only when grounded in education-theory-based pedagogical strategies; emotion information alone misguides a smaller model
description: Emotion features improve tutor performance only when grounded in education-theory-based pedagogical strategies; emotion information alone misguides a smaller model
id: emotion-plus-theory-prompting-ablation-gain
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2025
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

# Emotion features improve tutor performance only when grounded in education-theory-based pedagogical strategies; emotion information alone misguides a smaller model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In an ablation on Qwen2.5-7B-Socratic-LM, prompting with pedagogical strategies derived from detected emotion yields gains of 9 points (simple prompt) and 2 points (complex prompt), while emotion-only prompting hurts performance. [→ Debanjana Kar 2025](#debanjana-kar-2025)

## Evidence

### Debanjana Kar 2025

Debanjana Kar, Leopold Böss, Dacia Braca, Sebastian Dennerlein, Nina Hubig, Philipp Wintersberger, and Yufang Hou. (2025). MathBuddy: A Multimodal System for Affective Math Tutoring. https://arxiv.org/abs/2508.19993 [doi:10.48550/arxiv.2508.19993](https://doi.org/10.48550/arxiv.2508.19993)

`q2 · i?` · `design · r2`

Ablation study (Table 3) on the Qwen2.5-7B-Socratic-LM model across simple and complex prompts, comparing baseline, emotion-only, and emotion-plus-education-theory configurations. The authors note that "providing only the emotional information misguides the model".

> "prompting the model with relevant pedagogical strategies based on the detected emotion of the student results in a steep performance gain (by 9 points and 2 points through simple and complex prompts respectively)"

## Discussion


## Related Claims
- [Adding student-emotion information to LLM tutor prompting produces more desirable pedagogical qualities across most evaluated dimensions, with larger models benefiting most](emotion-aware-prompting-improves-pedagogical-quality.md) — related
- [MathBuddy's multimodal emotion aggregation matched participant-reviewed emotions at 60% overall accuracy, with sharply reduced recall for the Neutral class](multimodal-emotion-aggregation-60-percent-accuracy.md) — related
- [Model scale does not consistently improve pedagogical safety: within the Qwen2.5 family the 72B model beats the 7B on only 17 of 33 subject-dimension pairs](llm-scale-does-not-predict-tutor-safety.md) — related
