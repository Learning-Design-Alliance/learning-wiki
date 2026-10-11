---
type: claim
title: "Blinded expert annotators misclassified 83.7% of LLM-generated errors as human-written"
description: "Blinded expert annotators misclassified 83.7% of LLM-generated errors as human-written"
id: blinded-annotators-misclassify-83-7-percent-of-llm-errors-as-human
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: ali-keramati-2026
    resource: "https://arxiv.org/abs/2606.14113"
    title: "Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi. (2026). Simulating Students' Java Programming Errors with Large Language Models. arXiv preprint. https://arxiv.org/abs/2606.14113"
    author: Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Blinded expert annotators misclassified 83.7% of LLM-generated errors as human-written

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` In a blinded source-attribution task on 196 synthetic submissions, annotators misclassified 164/196 (83.7%) as human-written, indicating low distinguishability. [→ Ali Keramati 2026](#ali-keramati-2026)

## Evidence

### Ali Keramati 2026

Ali Keramati, Jie Cao, Iman Mohammadi, Mark Warschauer, Yang Shi. (2026). Simulating Students' Java Programming Errors with Large Language Models. arXiv preprint. https://arxiv.org/abs/2606.14113

`q2 · i?` · `design · r2`

Blinded expert annotation study (N=401 single-coded items after a 43-item double-coded pilot) comparing authentic and synthetic errors from the best-performing setting (Claude Sonnet 4 with Self-Refine). The deception rate was "164/196 (83.7%)" on the synthetic items, defined only on those 196 items.

> "Annotators misclassified 164/196 (83.7%) of LLM-generated submissions as human-written, indicating a low level of distinguishability"

## Discussion


## Related Claims
- [LLM-generated errors received significantly higher plausibility ratings than authentic student errors, explained by a narrower, cleaner error-type distribution](llm-errors-score-higher-plausibility-than-authentic-student-errors.md) — related
- [Blind expert verification shows no overall preference for human over LLM qualitative coding when sources are judged symmetrically](blind-verification-no-overall-human-preference.md) — related
- [LLM and human written 7C analyses show no overall difference in behavioral alignment or evidence correspondence, but align less on Communication and Constructive dimensions](llm-7c-analytical-alignment-mixed.md) — related
- [LLM-generated erroneous code aligns with authentic student errors at levels that depend on model and prompting strategy, with Claude Sonnet 4 most consistently aligned](llm-error-alignment-depends-on-model-and-prompting-strategy.md) — related
