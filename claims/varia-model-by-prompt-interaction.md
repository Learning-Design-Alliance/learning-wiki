---
type: claim
title: Individual model-strategy cells span J = 0.704 to 0.900, a model-by-prompt interaction wider than the tight strategy-level frontier band
description: Individual model-strategy cells span J = 0.704 to 0.900, a model-by-prompt interaction wider than the tight strategy-level frontier band
id: varia-model-by-prompt-interaction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
sources:
  - id: ernesto-lee-2026
    resource: "https://doi.org/10.35542/osf.io/u6xef_v2"
    title: "Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://doi.org/10.35542/osf.io/u6xef_v2"
    author: Ernesto Lee
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Individual model-strategy cells span J = 0.704 to 0.900, a model-by-prompt interaction wider than the tight strategy-level frontier band

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The within-frontier band widens at cell level: Claude Opus 4.7 under dimension-preserving constrained generation reaches J = 0.704 (with Flesch sigma = 20.8, more than triple Gemini's under the same prompt) while Gemini 3.1 Pro under structured chain-of-thought reaches J = 0.900. [→ Ernesto Lee 2026](#ernesto-lee-2026)

## Evidence

### Ernesto Lee 2026

Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://doi.org/10.35542/osf.io/u6xef_v2

`q2 · i?` · `design · r2`

Table 4 disaggregation of the joint integrity score by generator family and prompting strategy, each cell a mean across the three blueprints, described in the Results section. The authors conclude the tight frontier band is a property of the averages, not of every cell.

> "individual model-strategy combinations span 𝒥 = 0.704 (Claude Opus 4.7 under dimension-preserving constrained generation, driven by a readability dis- persion of 𝜎Flesch = 20.8 — more than triple that of Gemini under the same prompt) to 𝒥 = 0.900 (Gemini 3.1 Pro under structured chain-of-thought)."

## Discussion


## Related Claims
- [Under illustrative property thresholds, no prompting strategy passes all measured AIAA properties in every model-blueprint cell; few-shot anchoring passes only 2 of 9 cells](threshold-gating-no-strategy-fully-passes.md) — related
- [Frontier LLM prompting strategies cluster at joint integrity scores of 0.81-0.88 while non-frontier references collapse to 0.50-0.55, a 25-31 point capability-tier gap](varia-frontier-nonfrontier-tier-gap.md) — related
- [The two targeted ablations produce small, partially counter-directional effects: removing the construct map does not materially change the composite score (p = 0.34 on equivalence)](varia-ablation-null-effects.md) — related
