---
type: claim
title: "The system's error detection recall rate for complex rhythm errors was 91.2% ± 1.8%"
description: "The system's error detection recall rate for complex rhythm errors was 91.2% ± 1.8%"
id: rhythm-error-detection-recall-91-2
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: zhu-z-2026
    title: Zhu Z 2026
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# The system's error detection recall rate for complex rhythm errors was 91.2% ± 1.8%

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`

## Subclaims
`q2 i?` The system achieved a 91.2% ± 1.8% recall rate in detecting complex rhythm errors. [→ Zhu Z 2026](#zhu-z-2026)

## Evidence

### Zhu Z 2026

Zhu Z, Luo C and Li L (2026) Adaptive teaching assistance model combining generative AI and big data analytics. Front. Psychol. 17:1844703. https://doi.org/10.3389/fpsyg.2026.1844703

`q2 · i?` · `causal · r1`

Technical validation metric for the big data analysis module's rhythm diagnosis, which uses the DTW algorithm with a ±15 ms error threshold. The article reports the "error detection recall rate for complex rhythm errors was 91.2% ± 1.8%"; no effect size is printed for this accuracy metric.

> "the system's error detection recall rate for complex rhythm errors was 91.2% ± 1.8%"

## Discussion


## Related Claims
- [On the PRM800K validation dataset, detection rates dropped by 10.5 percentage points when final answers were correct, consistent with the correct answer trap extending beyond the Eedi data](cat-extends-to-prm800k-validation.md) — related
- [GPT models showed lower accuracy with more rubric-related errors (28% vs. 13% for Gemini 3 Flash) and near parity between false positives and negatives](gpt-models-more-rubric-errors-than-gemini.md) — related
- [Verification bottleneck: as reliance on AI increases, accuracy in detecting AI errors decreases while confidence does not](verification-bottleneck-confidence-dissociation.md) — related
