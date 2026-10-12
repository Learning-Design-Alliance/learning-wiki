---
type: claim
title: Under illustrative property thresholds, no prompting strategy passes all measured AIAA properties in every model-blueprint cell; few-shot anchoring passes only 2 of 9 cells
description: Under illustrative property thresholds, no prompting strategy passes all measured AIAA properties in every model-blueprint cell; few-shot anchoring passes only 2 of 9 cells
id: threshold-gating-no-strategy-fully-passes
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
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

# Under illustrative property thresholds, no prompting strategy passes all measured AIAA properties in every model-blueprint cell; few-shot anchoring passes only 2 of 9 cells

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Threshold gating at tau_eq = 0.70, tau_cos = 0.25, tau_ov = 0.15 and tau_Flesch = 10 yields no condition passing all measured properties in all nine cells; no-construct-map CoT passes 8/9 and few-shot collapses to 2/9, mostly through difficulty-parity breaches. [→ Ernesto Lee 2026](#ernesto-lee-2026)

## Evidence

### Ernesto Lee 2026

Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://doi.org/10.35542/osf.io/u6xef_v2

`q2 · i?` · `design · r2`

Per-cell pass/fail analysis under illustrative default thresholds reported in the Results threshold-gating subsection, converting continuous scores into pass rates across the nine (model, blueprint) cells per condition; both non-frontier references pass 0/3 cells.

> "The gate sharpens the trade-off into an operational finding: no condition passes all measured properties in all nine cells. No-construct-map CoT passes 8/9, zero-shot and structured CoT 7/9, and DPCG 6/9, while few-shot collapses to 2/9 — its diversity gain is purchased almost entirely by breaching difficulty parity ( 𝑃4 passes in only 2/9 of its cells)."

## Discussion


## Related Claims
- [Few-shot anchoring trades surface diversity against construct equivalence and readability parity, with each direction significant at p = 0.004 relative to zero-shot](few-shot-anchoring-three-way-tradeoff.md) — related
- [Individual model-strategy cells span J = 0.704 to 0.900, a model-by-prompt interaction wider than the tight strategy-level frontier band](varia-model-by-prompt-interaction.md) — related
