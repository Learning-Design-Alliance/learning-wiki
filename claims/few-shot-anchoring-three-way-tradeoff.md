---
type: claim
title: Few-shot anchoring trades surface diversity against construct equivalence and readability parity, with each direction significant at p = 0.004 relative to zero-shot
description: Few-shot anchoring trades surface diversity against construct equivalence and readability parity, with each direction significant at p = 0.004 relative to zero-shot
id: few-shot-anchoring-three-way-tradeoff
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: ernesto-lee-2026
    resource: "https://doi.org/10.35542/osf.io/u6xef_v2"
    title: "Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://doi.org/10.35542/osf.io/u6xef_v2"
    author: Ernesto Lee
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# Few-shot anchoring trades surface diversity against construct equivalence and readability parity, with each direction significant at p = 0.004 relative to zero-shot

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Relative to zero-shot, few-shot anchoring lowers pairwise cosine (delta = -0.035), lowers construct equivalence (delta = -0.130), and raises readability dispersion (delta = +4.0 Flesch points), each at p = 0.004. [→ Ernesto Lee 2026](#ernesto-lee-2026)

## Evidence

### Ernesto Lee 2026

Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://doi.org/10.35542/osf.io/u6xef_v2

`q2 · i?` · `causal · r1`

Exact two-sided sign-flip permutation tests on the nine matched (model, blueprint) cell differences from the single pilot draw, reported in the Results robustness subsection. The three few-shot-versus-zero-shot contrasts remain significant under a Holm correction (adjusted p <= 0.039).

> "The few-shot anchoring trade-off is supported in all three directions relative to zero- shot: anchoring lowers pairwise cosine ( Δ = −0.035 , 𝑝 = 0.004 ), lowers construct equivalence (Δ = −0.130 , 𝑝 = 0.004 ), and raises readability dispersion ( Δ = +4.0 Flesch points, 𝑝 = 0.004 )."

## Discussion


## Related Claims
- [Under illustrative property thresholds, no prompting strategy passes all measured AIAA properties in every model-blueprint cell; few-shot anchoring passes only 2 of 9 cells](threshold-gating-no-strategy-fully-passes.md) — related
- [The two targeted ablations produce small, partially counter-directional effects: removing the construct map does not materially change the composite score (p = 0.34 on equivalence)](varia-ablation-null-effects.md) — related
