---
type: claim
title: "Model scale does not consistently improve pedagogical safety: within the Qwen2.5 family the 72B model beats the 7B on only 17 of 33 subject-dimension pairs"
description: "Model scale does not consistently improve pedagogical safety: within the Qwen2.5 family the 72B model beats the 7B on only 17 of 33 subject-dimension pairs"
id: llm-scale-does-not-predict-tutor-safety
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
sources:
  - id: rima-hazra-2026
    resource: "https://arxiv.org/abs/2603.17373"
    title: "Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373"
    author: Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Model scale does not consistently improve pedagogical safety: within the Qwen2.5 family the 72B model beats the 7B on only 17 of 33 subject-dimension pairs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Scaling from 7B to 72B within the Qwen2.5 family improves safety on some dimensions but regresses on others, with the 72B model lower than the 7B on only 17 of 33 single-turn subject-dimension pairs. [→ Rima Hazra 2026](#rima-hazra-2026)

## Evidence

### Rima Hazra 2026

Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373

`q2 · i?` · `design · r2`

Comparison of Qwen2.5 family models (7B, 14B, 32B, 72B), which share architecture and training recipe, on single-turn SAFETUTORS harm rates. The article reports the 72B "achieves a lower harm rate than the 7B on only 17 pairs, a higher rate on 14, and ties on 2"; no effect size is printed.

> "Across all 33 subject–dimension pairs in single-turn, the 72B model achieves a lower harm rate than the 7B on only 17 pairs, a higher rate on 14, and ties on 2."

## Discussion


## Related Claims
- [CDPK performance scales with model size, with a sharp Pareto-frontier drop-off below around 8B parameters](cdpk-scales-with-model-size-dropoff-below-8b.md) — related
- [Model family and instruction-tuning approach appear better predictors of tutoring quality than parameter count alone](model-family-beats-parameter-count-for-tutoring-quality.md) — a broader claim this one bears on
- [Single-turn tutors disclose answers pervasively while challenge scores are near zero across every model and subject](single-turn-answer-disclosure-challenge-near-zero.md) — related
