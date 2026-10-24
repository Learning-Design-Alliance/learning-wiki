---
type: claim
title: Adding a memory (forgetting) mechanism slightly decreases simulated learning gains overall yet improves alignment with human results, apparently by letting agents discard incorrect rules
description: Adding a memory (forgetting) mechanism slightly decreases simulated learning gains overall yet improves alignment with human results, apparently by letting agents discard incorrect rules
id: forgetting-mechanism-decreases-gains-improves-alignment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: weak
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: rachatasumrit-2023
    resource: "https://doi.org/10.31234/osf.io/eyxfw"
    title: "Rachatasumrit, N., Koedinger, K. R., & Carvalho, P. F. (2023). Evidence and theory for why the best example-problem ratio to optimize learning gain depends on knowledge content. https://osf.io/29wpe [doi:10.31234/osf.io/eyxfw](https://doi.org/10.31234/osf.io/eyxfw)"
    author: "Rachatasumrit, N., Koedinger, K. R., & Carvalho, P. F."
    q: 2
    i: 2
    kind: theoretical
    rigour: 3
---

# Adding a memory (forgetting) mechanism slightly decreases simulated learning gains overall yet improves alignment with human results, apparently by letting agents discard incorrect rules

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2` · `i2` medium
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i2` Introducing the memory mechanism decreased overall learning gains (13.7% vs 22.2%) but did not negate the worked-example benefit for skills, and forgetting agents more effectively utilized correct production rules. [→ Rachatasumrit 2023](#rachatasumrit-2023)

## Evidence

### Rachatasumrit 2023

Rachatasumrit, N., Koedinger, K. R., & Carvalho, P. F. (2023). Evidence and theory for why the best example-problem ratio to optimize learning gain depends on knowledge content. https://osf.io/29wpe [doi:10.31234/osf.io/eyxfw](https://doi.org/10.31234/osf.io/eyxfw)

`q2 · i2` · `theoretical · r3`

Simulation comparison of AL agents with versus without forgetting (d = 0.7). The authors' interpretation, from a closer examination, is that forgetting agents better discard incorrect production rules and more often select correct ones due to stronger memory activation of later-learned correct rules.

> "the introduction of a memory mechanism in simulated learners with forgetting slightly decreases learning gains (22.2% for simulated learners without forgetting vs 13.7% for simulated learners with forgetting), t (948) = 9.409, p < 0.0001, d = 0.7, but does not negate the benefits of worked examples over retrieval practice for skills"

## Discussion


## Related Claims
- [In simulated learners with forgetting, study-practice yields higher skill gains while practice-only yields higher fact gains, mirroring the human pattern](al-simple-effects-mirror-human-pattern.md) — related
- [Ablations show each CogEvolution module contributes: removing ICAP perception, structured retrieval, or evolutionary update degrades mistake precision, learning-curve fit, and alignment](cogevolution-ablation-module-contributions.md) — related
- [In a human experiment, verbatim facts are learned better from practice-only training while general skills are learned better from example-integrated training (cross-over content-treatment interaction)](crossover-content-treatment-interaction-facts-practice-skills-examples.md) — related
