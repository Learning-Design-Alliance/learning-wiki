---
type: claim
title: Hurst exponent calculation requires multiple data points (e.g., over 100), which may make real-time computation impractical in some situations such as single-session studies
description: Hurst exponent calculation requires multiple data points (e.g., over 100), which may make real-time computation impractical in some situations such as single-session studies
id: hurst-exponent-data-requirement-limits-real-time-use
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-27
evidence_strength: weak
sources:
  - id: erica-l-snow-2015
    resource: "https://educationaldatamining.org/EDM2015"
    title: "Erica L. Snow. (2015). Dynamic User Modeling within a Game-Based ITS. Proceedings of the 8th International Conference on Educational Data Mining. https://educationaldatamining.org/EDM2015"
    author: Erica L. Snow
    q: 1
    i: "?"
    kind: design
    rigour: 1
---

# Hurst exponent calculation requires multiple data points (e.g., over 100), which may make real-time computation impractical in some situations such as single-session studies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r1` · `q1`

## Subclaims
`q1 i?` Reliably calculating a Hurst exponent requires multiple data points (e.g., over 100), so calculating Hurst in real time may not be practical in all situations, such as a single session study. [→ Erica L. Snow 2015](#erica-l-snow-2015)

## Evidence

### Erica L. Snow 2015

Erica L. Snow. (2015). Dynamic User Modeling within a Game-Based ITS. Proceedings of the 8th International Conference on Educational Data Mining. https://educationaldatamining.org/EDM2015

`q1 · i?` · `design · r1`

The article states this methodological limitation in its advice-sought section, noting that each of the dynamic measures used so far (random walks, Entropy, Hurst analyses) has one or more weaknesses; no empirical test of the limitation is reported.

> "to reliably calculate a Hurst exponent, multiple data points are needed (e.g., over 100), therefore calculating Hurst in real-time may not be practical in all situations (i.e., a single session study)."

## Discussion


## Related Claims
- [Real-time dynamic analyses (Hurst exponents, Entropy) are hypothesized to inform user models about optimal and non-optimal learning behaviors within a game-based ITS](real-time-dynamic-analyses-inform-user-models.md) — related
