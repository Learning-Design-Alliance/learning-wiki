---
type: claim
title: LLM-generated scores on multimodal OSPE items correlate strongly with human scores in rank order yet diverge substantially on categorical pass/fail decisions
description: LLM-generated scores on multimodal OSPE items correlate strongly with human scores in rank order yet diverge substantially on categorical pass/fail decisions
id: llm-ospe-rank-agreement-paradox
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: akhund-2026
    resource: "https://doi.org/10.1080/10872981.2026.2684837"
    title: "Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837"
    author: Akhund, S. A., et al
    q: 3
    i: "?"
    kind: associational
    rigour: 2
  - id: akhund-2026-2
    resource: "https://doi.org/10.1080/10872981.2026.2684837"
    title: "Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837"
    author: Akhund, S. A., et al
    q: 3
    i: "?"
    kind: associational
    rigour: 2
---

# LLM-generated scores on multimodal OSPE items correlate strongly with human scores in rank order yet diverge substantially on categorical pass/fail decisions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Rank-order correlations were strong across all models (rs = 0.784–0.921), but categorical agreement diverged substantially. [→ Akhund 2026](#akhund-2026)
`q3 i?` Pass/fail agreement ranged from 52.1% (ChatGPT; κ = 0.067, slight) to 84.1% (Claude; κ = 0.680, substantial). [→ Akhund 2026 (2)](#akhund-2026-2)

## Evidence

### Akhund 2026

Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837

`q3 · i?` · `associational · r2`

Retrospective inter-rater reliability study of 309 students × 19 OSPE items (5,871 scores per grader). Spearman's rs against human grader: Claude 0.883, ChatGPT 0.784, Gemini 0.921 (all p < 0.001), showing models could broadly order students from weakest to strongest.

> "All three models produced scores that were strongly correlated with human scores in rank order (rs = 0.784–0.921), indicating that the models could broadly order students from weakest to strongest in a pattern similar to that of a human expert."

### Akhund 2026 (2)

Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837

`q3 · i?` · `associational · r2`

Same retrospective study's pass/fail agreement analysis at the institutional 65% threshold. Claude 84.1% agreement (κ = 0.680, substantial), Gemini 73.8% (κ = 0.483, moderate), ChatGPT 52.1% (κ = 0.067, slight, statistically insignificant).

> "Claude achieved the best performance, with 84.1% simple agreement and a Cohen's κ of 0.680 (95% CI: 0.599, 0.760, substantial), although this remains well below the near-perfect agreement expected of human examiners."

## Discussion


## Related Claims
- [Item characteristics associated with LLM-human discrepancy on multimodal OSPE items cluster into three mechanisms: non-standard histological staining, 3D spatial reasoning from 2D images, and semantic inflexibility in short-answer evaluation](llm-ospe-divergence-mechanisms.md) — related
- [Models with similar rank correlations differ substantially in estimating difficulty magnitude (RMSE and MAE)](llm-difficulty-magnitude-error-varies-across-models.md) — a broader claim this one bears on
- [Error distributions differed directionally across LLMs: Claude produced more false positives (14.2%), whereas Gemini and ChatGPT produced more false negatives (25.9% and 47.9%, respectively)](llm-ospe-asymmetric-error-patterns.md) — related
- [LLM-based rubric scores agreed with expert ratings at the total-score level and on cognitive-process dimensions, but agreement was low for more subjective dimensions](ai-expert-agreement-cognitive-versus-subjective-dimensions.md) — related
- [Three LLMs showed inconsistent systematic bias on multimodal OSPE grading: Claude over-scored by +2.5 points (proportional), Gemini under-scored by −5.0 and ChatGPT by −10.0 points (non-proportional)](llm-ospe-systematic-bias-bland-altman.md) — related
