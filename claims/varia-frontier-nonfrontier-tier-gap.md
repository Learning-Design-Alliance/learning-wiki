---
type: claim
title: Frontier LLM prompting strategies cluster at joint integrity scores of 0.81-0.88 while non-frontier references collapse to 0.50-0.55, a 25-31 point capability-tier gap
description: Frontier LLM prompting strategies cluster at joint integrity scores of 0.81-0.88 while non-frontier references collapse to 0.50-0.55, a 25-31 point capability-tier gap
id: varia-frontier-nonfrontier-tier-gap
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

# Frontier LLM prompting strategies cluster at joint integrity scores of 0.81-0.88 while non-frontier references collapse to 0.50-0.55, a 25-31 point capability-tier gap

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` Across 60 condition cells, frontier strategy means span J = 0.806-0.877 while Llama 3.2 3B Instruct reaches 0.552 and GPT-2 small 0.497, and the tier gap is significant under an exact permutation test (p = 0.005). [→ Ernesto Lee 2026](#ernesto-lee-2026)

## Evidence

### Ernesto Lee 2026

Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://doi.org/10.35542/osf.io/u6xef_v2

`q2 · i?` · `design · r2`

Pilot evaluation of the VARIA benchmark: 600 generated variants across 60 condition cells, three frontier families, four prompting strategies plus two ablations, and two non-frontier references on three blueprints. The results section reports the references "drop sharply" with J = 0.552 and 0.497 versus a frontier band of 0.806-0.877.

> "The two non-frontier references then drop sharply: Llama 3.2 3B Instruct reaches 𝒥 = 0.552 and GPT-2 small reaches 𝒥 = 0.497 — a twenty-five to thirty-one percentage-point gap to the weakest frontier strategy, establishing that the benchmark separates capability tiers despite the within-frontier compression."

## Discussion


## Related Claims
- [The two targeted ablations produce small, partially counter-directional effects: removing the construct map does not materially change the composite score (p = 0.34 on equivalence)](varia-ablation-null-effects.md) — related
- [Over a quarter of benchmark tasks (23 of 80) defeat all six frontier models, with over 22% showing capability boundaries where scores swing by up to 90 points](capability-boundaries-and-universal-failures-academiclaw.md) — related
- [BEAGLE generalizes across tasks and LLM backbones: on the out-of-distribution Gradient Descent task it still shrinks DKL by ≥3×, raises error recurrence to ≥79%, and improves all three perceptual scores](beagle-cross-task-cross-backbone-generalization.md) — related
- [Individual model-strategy cells span J = 0.704 to 0.900, a model-by-prompt interaction wider than the tight strategy-level frontier band](varia-model-by-prompt-interaction.md) — related
