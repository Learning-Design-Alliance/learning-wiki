---
type: claim
title: Combining the pattern detector with an LLM fallback does not improve joint detection accuracy over the LLM alone
description: Combining the pattern detector with an LLM fallback does not improve joint detection accuracy over the LLM alone
id: pattern-plus-llm-fallback-no-gain
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
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

# Combining the pattern detector with an LLM fallback does not improve joint detection accuracy over the LLM alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` On the real corpus the combined pattern+gemini configuration (pair F1 63.50) was significantly lower than gemini-2.0-flash alone (67.81, p=0.005), though it reduces LLM calls by approximately one third. [→ Laurent Brisson 2026](#laurent-brisson-2026)

## Evidence

### Laurent Brisson 2026

Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598

`q2 · i?` · `design · r2`

Joint orchestration analysis on the real corpus comparing a hybrid configuration (pattern first, LLM fallback on abstention) against gemini-2.0-flash alone. The hybrid reduced LLM calls by roughly one third but degraded pair F1 significantly.

> "the combined pattern+gemini con- ﬁguration (pair F1 63.50) is signiﬁcantly lower than gemini-2.0-ﬂash alone (67.81, p=0.005), indicating that the current pattern introduces errors on queries that the LLM would have handled correctly."

## Discussion


## Related Claims
- [Free-tier LLM detection performance varies widely and differs by corpus: gemini-2.0-flash leads on real data while the pattern detector leads on synthetic data for intent detection](llm-detection-variability-across-corpus.md) — related
- [The deterministic pattern detector achieves high pair precision (73.21%) with explicit abstention but covers only 32% of real queries](pattern-detector-high-precision-low-coverage.md) — reports the opposite
