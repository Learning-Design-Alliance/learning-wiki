---
type: claim
title: "Three LLMs showed inconsistent systematic bias on multimodal OSPE grading: Claude over-scored by +2.5 points (proportional), Gemini under-scored by −5.0 and ChatGPT by −10.0 points (non-proportional)"
description: "Three LLMs showed inconsistent systematic bias on multimodal OSPE grading: Claude over-scored by +2.5 points (proportional), Gemini under-scored by −5.0 and ChatGPT by −10.0 points (non-proportional)"
id: llm-ospe-systematic-bias-bland-altman
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
---

# Three LLMs showed inconsistent systematic bias on multimodal OSPE grading: Claude over-scored by +2.5 points (proportional), Gemini under-scored by −5.0 and ChatGPT by −10.0 points (non-proportional)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Claude scored students a mean of 2.5 points above the human grader with proportional bias; Gemini and ChatGPT scored below (−5.0 and −10.0 points) with non-proportional bias. [→ Akhund 2026](#akhund-2026)

## Evidence

### Akhund 2026

Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837

`q3 · i?` · `associational · r2`

Bland–Altman bias visualisation in the same retrospective study (Supplementary Table S2, Figure S1). Claude's proportional over-scoring grew at higher levels; ChatGPT's 95% limits of agreement were widest (approximately ±20 points), indicating highly unreliable individual-level predictions.

> "Claude scored students a mean of 2.5 points above the human grader, and its bias was proportional; the over-scoring became more pronounced at higher performance levels. Gemini and ChatGPT both scored below the human grader (mean differences of −5.0 and −10.0 points respectively), but their biases were non-proportional."

## Discussion


## Related Claims
- [LLM-generated scores on multimodal OSPE items correlate strongly with human scores in rank order yet diverge substantially on categorical pass/fail decisions](llm-ospe-rank-agreement-paradox.md) — related
- [Error distributions differed directionally across LLMs: Claude produced more false positives (14.2%), whereas Gemini and ChatGPT produced more false negatives (25.9% and 47.9%, respectively)](llm-ospe-asymmetric-error-patterns.md) — related
- [LLM grading performance relative to human graders is mixed: comparable in 12 reviewed cases, worse in 11, with the strongest alignment on short, straightforward tasks](llm-grading-mixed-against-human-raters.md) — related
- [LLMs differ systematically in grading strictness, forming liberal, restrictive, and balanced grading styles on programming assignments](llms-differ-liberal-restrictive-balanced-grading-styles.md) — a broader claim this one bears on
- [Bland–Altman analysis shows systematic bias and wide limits of agreement, with AI tending to assign slightly higher scores than the expert across most criteria](bland-altman-ai-higher-scores-poor-interchangeability.md) — related
- [Bland–Altman analysis shows peer and instructor scores agree closely, with limits of agreement from -1.17 to +1.16](bland-altman-agreement-peer-instructor.md) — related
