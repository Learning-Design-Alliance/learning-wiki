---
type: claim
title: Adding student-emotion information to LLM tutor prompting produces more desirable pedagogical qualities across most evaluated dimensions, with larger models benefiting most
description: Adding student-emotion information to LLM tutor prompting produces more desirable pedagogical qualities across most evaluated dimensions, with larger models benefiting most
id: emotion-aware-prompting-improves-pedagogical-quality
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
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

# Adding student-emotion information to LLM tutor prompting produces more desirable pedagogical qualities across most evaluated dimensions, with larger models benefiting most

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Feature-enhanced (emotion-aware) versions of tutoring LLMs perform consistently better than their baseline versions on automatic pedagogical evaluation, with the largest model improving on six of eight dimensions. [→ Debanjana Kar 2025](#debanjana-kar-2025)

## Evidence

### Debanjana Kar 2025

Debanjana Kar, Leopold Böss, Dacia Braca, Sebastian Dennerlein, Nina Hubig, Philipp Wintersberger, and Yufang Hou. (2025). MathBuddy: A Multimodal System for Affective Math Tutoring. https://arxiv.org/abs/2508.19993 [doi:10.48550/arxiv.2508.19993](https://doi.org/10.48550/arxiv.2508.19993)

`q2 · i?` · `design · r2`

Automatic evaluation on the MathDial Bridge benchmark (327 human-annotated conversations) using Win Rate and DAMR with an ensemble LLM-as-judge, comparing emotion-enhanced models against baseline tutoring models. The enhanced versions "perform consistently better compared to their respective baseline versions".

> "with much larger models like LearnLM 2.0, we see that the feature enhanced version produces responses with more desirable pedagogical qualities in six out of the eight dimensions and is comparable for the rest of the dimensions"

## Discussion


## Related Claims
- [Emotion features improve tutor performance only when grounded in education-theory-based pedagogical strategies; emotion information alone misguides a smaller model](emotion-plus-theory-prompting-ablation-gain.md) — related
- [MisconceptionTutor achieves higher pedagogical quality (DAMR) than BaselineTutor on nearly all dimensions, with small-to-moderate effect sizes](misconception-tutor-higher-damr-pedagogical-quality.md) — related
