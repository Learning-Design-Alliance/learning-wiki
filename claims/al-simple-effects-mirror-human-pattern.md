---
type: claim
title: In simulated learners with forgetting, study-practice yields higher skill gains while practice-only yields higher fact gains, mirroring the human pattern
description: In simulated learners with forgetting, study-practice yields higher skill gains while practice-only yields higher fact gains, mirroring the human pattern
id: al-simple-effects-mirror-human-pattern
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: rachatasumrit-2023
    resource: "https://doi.org/10.31234/osf.io/eyxfw"
    title: "Rachatasumrit, N., Koedinger, K. R., & Carvalho, P. F. (2023). Evidence and theory for why the best example-problem ratio to optimize learning gain depends on knowledge content. https://osf.io/29wpe [doi:10.31234/osf.io/eyxfw](https://doi.org/10.31234/osf.io/eyxfw)"
    author: "Rachatasumrit, N., Koedinger, K. R., & Carvalho, P. F."
    q: 2
    i: 1
    kind: causal
    rigour: 2
---

# In simulated learners with forgetting, study-practice yields higher skill gains while practice-only yields higher fact gains, mirroring the human pattern

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2` · `i1` small

## Subclaims
`q2 i1` For simulated learners with forgetting, study-practice led to higher skill learning gains than practice-only, while practice-only led to higher fact gains than study-practice. [→ Rachatasumrit 2023](#rachatasumrit-2023)

## Evidence

### Rachatasumrit 2023

Rachatasumrit, N., Koedinger, K. R., & Carvalho, P. F. (2023). Evidence and theory for why the best example-problem ratio to optimize learning gain depends on knowledge content. https://osf.io/29wpe [doi:10.31234/osf.io/eyxfw](https://doi.org/10.31234/osf.io/eyxfw)

`q2 · i1` · `causal · r2`

Simple-effects analysis of the AL simulation with forgetting showed the human-like cross-over: skills favored study-practice (d = 0.286) and facts favored practice-only (d = 0.300). For agents without forgetting, study-practice led to higher gains for both skills and facts.

> "the simulated learners with forgetting in a study-practice condition led to higher learning gains for skills than a practice-only condition (19.9% vs 15.8%), t (228) = -2.404, p = .009, d = 0.286 but the effect was reversed for facts, such that a practice-only condition led to higher learning gains than a study-practice condition (12.7% vs 15.6%), t (243) = 2.072, p = 0.020, d = 0.300"

## Discussion


## Related Claims
- [Adding a memory (forgetting) mechanism slightly decreases simulated learning gains overall yet improves alignment with human results, apparently by letting agents discard incorrect rules](forgetting-mechanism-decreases-gains-improves-alignment.md) — related
- [In a human experiment, verbatim facts are learned better from practice-only training while general skills are learned better from example-integrated training (cross-over content-treatment interaction)](crossover-content-treatment-interaction-facts-practice-skills-examples.md) — related
- [The training-by-content interaction is not specific to test question type, indicating transfer between skill and fact learning](no-three-way-interaction-test-question-type-transfer.md) — related
