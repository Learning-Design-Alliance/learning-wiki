---
type: claim
title: "Error distributions differed directionally across LLMs: Claude produced more false positives (14.2%), whereas Gemini and ChatGPT produced more false negatives (25.9% and 47.9%, respectively)"
description: "Error distributions differed directionally across LLMs: Claude produced more false positives (14.2%), whereas Gemini and ChatGPT produced more false negatives (25.9% and 47.9%, respectively)"
id: llm-ospe-asymmetric-error-patterns
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

# Error distributions differed directionally across LLMs: Claude produced more false positives (14.2%), whereas Gemini and ChatGPT produced more false negatives (25.9% and 47.9%, respectively)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q3`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q3 i?` ChatGPT's 47.9% false negative rate could classify competent students as failing; false positives could classify underperforming students as passing. [→ Akhund 2026](#akhund-2026)

## Evidence

### Akhund 2026

Akhund, S. A., et al. (2026). Agreement, calibration, and failure of three large language models as high-stakes multimodal OSPE graders: a comparative psychometric analysis. Medical Education Online. https://doi.org/10.1080/10872981.2026.2684837

`q3 · i?` · `associational · r2`

Diagnostic error analysis using a standard framework (false positives: LLM passing a below-threshold student; false negatives: human-passed student receiving a failing LLM score) in the same retrospective study.

> "Claude produced more false positives (14.2%), whereas Gemini and ChatGPT produced more false negatives (25.9% and 47.9%, respectively). These directional differences suggest distinct deployment risk profiles."

## Discussion


## Related Claims
- [No consistent relationship was observed between false-positive and false-negative rates and either the question or the LLM model](no-consistent-fp-fn-pattern.md) — reports the opposite
- [GPT models showed lower accuracy with more rubric-related errors (28% vs. 13% for Gemini 3 Flash) and near parity between false positives and negatives](gpt-models-more-rubric-errors-than-gemini.md) — related
- [Overconfidence rates differ significantly among LLMs, with Gemini highest and Claude showing none](llm-overconfidence-rates-differ-endodontic-questions.md) — related
- [LLM-generated scores on multimodal OSPE items correlate strongly with human scores in rank order yet diverge substantially on categorical pass/fail decisions](llm-ospe-rank-agreement-paradox.md) — related
- [Three LLMs showed inconsistent systematic bias on multimodal OSPE grading: Claude over-scored by +2.5 points (proportional), Gemini under-scored by −5.0 and ChatGPT by −10.0 points (non-proportional)](llm-ospe-systematic-bias-bland-altman.md) — related
- [The pass/fail standard produced false positives and a false negative, possibly because the simulator recognizes a specific fixed pathway](foi-test-false-positives-fixed-pathway-limitation.md) — related
- [Bland-Altman analysis shows a systematic positive bias of about 10 percentage points in favor of GRS over checklists](bland-altman-grs-positive-bias-osce.md) — related
