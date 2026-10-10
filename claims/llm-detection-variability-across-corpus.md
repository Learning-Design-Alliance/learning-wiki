---
type: claim
title: "Free-tier LLM detection performance varies widely and differs by corpus: gemini-2.0-flash leads on real data while the pattern detector leads on synthetic data for intent detection"
description: "Free-tier LLM detection performance varies widely and differs by corpus: gemini-2.0-flash leads on real data while the pattern detector leads on synthetic data for intent detection"
id: llm-detection-variability-across-corpus
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: laurent-brisson-2026
    resource: "https://arxiv.org/abs/2607.22598"
    title: "Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598"
    author: Laurent Brisson, Maria Teresa Segarra and Gregory Smits
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Free-tier LLM detection performance varies widely and differs by corpus: gemini-2.0-flash leads on real data while the pattern detector leads on synthetic data for intent detection

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the synthetic corpus the pattern detector achieved the highest F1 macro (65.59), not significantly different from gemini-2.0-flash (60.19, p=0.1741), but on the real corpus gemini-2.0-flash achieved the highest F1 macro (80.59, p<0.001 vs pattern 62.46). [→ Laurent Brisson 2026](#laurent-brisson-2026)

## Evidence

### Laurent Brisson 2026

Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598

`q2 · i?` · `design · r2`

Intent detection evaluation (RQ2) on the real corpus (n=196 intent occurrences). Gemini-2.0-flash significantly outperformed the pattern; mistral-small (53.78, p=0.137) and openrouter-free (66.91, p=0.473) did not differ significantly from the pattern.

> "Gemini-2.0-flash achieves the highest F1 macro (80.59, p<0.001 vs pattern), while the pattern reaches 62.46."

## Discussion


## Related Claims
- [Combining the pattern detector with an LLM fallback does not improve joint detection accuracy over the LLM alone](pattern-plus-llm-fallback-no-gain.md) — related
- [The deterministic pattern detector achieves high pair precision (73.21%) with explicit abstention but covers only 32% of real queries](pattern-detector-high-precision-low-coverage.md) — related
