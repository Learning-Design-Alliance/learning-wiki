---
type: claim
title: "In the authors' practical test, vision-capable LLMs recognized handwritten examination letters with high accuracy, with Gemini 3 Flash best at about 98.84% (35 errors in 3009 letters)"
description: "In the authors' practical test, vision-capable LLMs recognized handwritten examination letters with high accuracy, with Gemini 3 Flash best at about 98.84% (35 errors in 3009 letters)"
id: vision-llm-letter-recognition-98-84-percent
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: hartwig-grabowski-2026
    resource: "https://arxiv.org/abs/2606.08855"
    title: "Hartwig Grabowski, Michael Canz. (2026). Hybrid E-Assessment in Higher Education: Semi-Automated Grading of Paper-Based Written Examinations. https://arxiv.org/abs/2606.08855"
    author: Hartwig Grabowski, Michael Canz
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# In the authors' practical test, vision-capable LLMs recognized handwritten examination letters with high accuracy, with Gemini 3 Flash best at about 98.84% (35 errors in 3009 letters)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across 3009 letters recognized in practical use, Gemini 3 Flash produced 35 incorrect recognitions requiring manual post-processing, about 98.84% accuracy, outperforming Qwen3-VL-30B-A3B-Instruct (~98.31%), GPT-5 (~96.54%), and Grok 4.1 Fast (~88.90%). [→ Hartwig Grabowski 2026](#hartwig-grabowski-2026)

## Evidence

### Hartwig Grabowski 2026

Hartwig Grabowski, Michael Canz. (2026). Hybrid E-Assessment in Higher Education: Semi-Automated Grading of Paper-Based Written Examinations. https://arxiv.org/abs/2606.08855

`q2 · i?` · `design · r2`

Practical evaluation of vision-capable LLMs on scanned examination answer tables: "Across 3009 letters to be recognized, 35 incorrect recognitions occurred and required manual post-processing". Table 1 prints error rates for four models; Gemini 3 Flash showed the best performance in the tested setting. No standardized effect size is printed.

> "Google Gemini 3 Flash showed the best evaluation performance in the tested setting. Across 3009 letters to be recognized, 35 incorrect recognitions occurred and required manual post-processing (Table 1)."

## Discussion


## Related Claims

- [An earlier YOLO-5-based handwriting recognition method reached only 88.28% accuracy on examination table fields, which the authors judge insufficient for summative assessment](yolo5-handwriting-recognition-88-percent-insufficient.md) — related
- [Most AI grading errors (87% for the best model) were attributable to transcription failures rather than rubric misapplication](transcription-failures-dominate-grading-errors.md)
