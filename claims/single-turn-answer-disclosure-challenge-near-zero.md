---
type: claim
title: Single-turn tutors disclose answers pervasively while challenge scores are near zero across every model and subject
description: Single-turn tutors disclose answers pervasively while challenge scores are near zero across every model and subject
id: single-turn-answer-disclosure-challenge-near-zero
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
  - id: rima-hazra-2026-2
    resource: "https://arxiv.org/abs/2603.17373"
    title: "Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373"
    author: Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Single-turn tutors disclose answers pervasively while challenge scores are near zero across every model and subject

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` Answer disclosure is pervasive in single-turn responses, particularly in Chemistry where Qwen2.5-72B gives away answers in 37.9% of responses. [→ Rima Hazra 2026](#rima-hazra-2026)
`q2 i?` Challenge scores are near zero across every model and subject, with the highest observed value being 0.21 for Llama-3.1-70B in Mathematics. [→ Rima Hazra 2026 (2)](#rima-hazra-2026-2)

## Evidence

### Rima Hazra 2026

Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373

`q2 · i?` · `design · r2`

Single-turn process-level pedagogical analysis (Figure 3) across subjects and models, evaluating answer disclosure, challenge, topic maintenance, and clarity. The article reports "answer disclosure is pervasive", with Qwen2.5-72B giving away answers in 37.9% of Chemistry responses; no effect size is printed.

> "However, answer disclosure is pervasive, particu- larly in Chemistry where Qwen2.5-72B gives away answers in 37.9% of responses."

### Rima Hazra 2026 (2)

Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy. (2026). SAFETUTORS: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv preprint. https://arxiv.org/abs/2603.17373

`q2 · i?` · `design · r2`

Single-turn pedagogical quality analysis across all evaluated models and subjects. The article reports "challenge scores are near zero across every model and subject", with the highest value 0.21 for Llama-3.1-70B in Mathematics, indicating models default to passive explanation; no effect size is printed.

> "More critically, challenge scores are near zero across ev- ery model and subject, with the highest observed value being just 0.21 for Llama-3.1-70B in Math- ematics."

## Discussion


## Related Claims
- [Model scale does not consistently improve pedagogical safety: within the Qwen2.5 family the 72B model beats the 7B on only 17 of 33 subject-dimension pairs](llm-scale-does-not-predict-tutor-safety.md) — related
- [No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation](no-llm-tutor-reliably-safe-60-percent-harm.md) — related
