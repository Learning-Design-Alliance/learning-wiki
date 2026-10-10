---
type: claim
title: "The deterministic pattern detector achieves high pair precision (73.21%) with explicit abstention but covers only 32% of real queries"
description: "The deterministic pattern detector achieves high pair precision (73.21%) with explicit abstention but covers only 32% of real queries"
id: pattern-detector-high-precision-low-coverage
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

# The deterministic pattern detector achieves high pair precision (73.21%) with explicit abstention but covers only 32% of real queries

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` When the pattern detector commits on the real corpus, its (intent, concept) pair is correct 73.21% of the time, versus 60.00 for gemini-2.0-flash, 39.91 for openrouter-free, and 18.04 for mistral-small, while abstaining on 68% of queries. [→ Laurent Brisson 2026](#laurent-brisson-2026)

## Evidence

### Laurent Brisson 2026

Laurent Brisson, Maria Teresa Segarra and Gregory Smits. (2026). A didactical-driven teacher assistant for a dimensional modeling course. https://arxiv.org/abs/2607.22598

`q2 · i?` · `design · r2`

Joint orchestration evaluation on the 195-question real corpus. The lexicon-based pattern detector shows "a radically different precision profile": coverage 32%, pair precision 73.21, and 50 ms median latency, versus gemini-2.0-flash at 95% coverage and 60.00 pair precision.

> "The pattern abstains on 68% of real queries (133 out of 195), but when it commits to a response, it achieves a pair precision of 73.21"

## Discussion


## Related Claims
- [Free-tier LLM detection performance varies widely and differs by corpus: gemini-2.0-flash leads on real data while the pattern detector leads on synthetic data for intent detection](llm-detection-variability-across-corpus.md) — related
- [Combining the pattern detector with an LLM fallback does not improve joint detection accuracy over the LLM alone](pattern-plus-llm-fallback-no-gain.md) — reports the opposite
