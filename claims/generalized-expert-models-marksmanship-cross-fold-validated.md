---
type: claim
title: Cross-fold validation supports generalized expert models of marksmanship behavior across firing conditions and behavioral measures
description: Cross-fold validation supports generalized expert models of marksmanship behavior across firing conditions and behavioral measures
id: generalized-expert-models-marksmanship-cross-fold-validated
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
evidence_strength: moderate
newest_evidence: 2018
recheck_by: 2021
sources:
  - id: goldberg-2018
    resource: "https://doi.org/10.1007/s40593-017-0155-y"
    title: "Goldberg, B., Amburn, C., Ragusa, C., & Chen, D. (2018). Modeling Expert Behavior in Support of an Adaptive Psychomotor Training Environment: a Marksmanship Use Case. Int J Artif Intell Educ 28:194–224. https://doi.org/10.1007/s40593-017-0155-y"
    author: "Goldberg, B., Amburn, C., Ragusa, C., & Chen, D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: goldberg-2018-2
    resource: "https://doi.org/10.1007/s40593-017-0155-y"
    title: "Goldberg, B., Amburn, C., Ragusa, C., & Chen, D. (2018). Modeling Expert Behavior in Support of an Adaptive Psychomotor Training Environment: a Marksmanship Use Case. Int J Artif Intell Educ 28:194–224. https://doi.org/10.1007/s40593-017-0155-y"
    author: "Goldberg, B., Amburn, C., Ragusa, C., & Chen, D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Cross-fold validation supports generalized expert models of marksmanship behavior across firing conditions and behavioral measures

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2018 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2021**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Leave-one-out cross-fold validation of expert models built from seven of eight marksmanship experts supported a generalized expert modeling approach across breathing, barrel movement, and trigger control measures and four firing conditions. [→ Goldberg 2018](#goldberg-2018)
`q2 i?` For each measure and condition, at least one but never more than two experts exhibited significantly different behavioral techniques and were excluded from that condition's model build. [→ Goldberg 2018 (2)](#goldberg-2018-2)

## Evidence

### Goldberg 2018

Goldberg, B., Amburn, C., Ragusa, C., & Chen, D. (2018). Modeling Expert Behavior in Support of an Adaptive Psychomotor Training Environment: a Marksmanship Use Case. Int J Artif Intell Educ 28:194–224. https://doi.org/10.1007/s40593-017-0155-y

`q2 · i?` · `design · r2`

Cross-fold validation study: n-1 leave-one-out models were built from seven experts' AUC measures per condition and behavior, with the excluded expert's shots cross-checked against a 2-SD threshold. The authors report the data "supp orts a generalized expert modeling approach".

> "From our initial results, the data supp orts a generalized expert modeling approach that accounts for multiple behavioral representations on a single mea- sure."

### Goldberg 2018 (2)

Goldberg, B., Amburn, C., Ragusa, C., & Chen, D. (2018). Modeling Expert Behavior in Support of an Adaptive Psychomotor Training Environment: a Marksmanship Use Case. Int J Artif Intell Educ 28:194–224. https://doi.org/10.1007/s40593-017-0155-y

`q2 · i?` · `design · r2`

In the cross-fold validation summary across all condition/metric pairings, the authors report, anecdotally, that "at least one expert (but never more than two)" per measure and condition showed significantly different behavioral techniques and was excluded from model builds.

> "Anecdotally, for each measure and in each condition, at least one expert (but never more than two) exhibited significantly different behavioral techniques when evaluated through cross-check procedures."

## Discussion


## Related Claims
- [Stance, barrel movement, and trigger control significantly predict individual shot performance, accounting for approximately 20% of variance](stance-barrel-trigger-predict-shot-performance.md) — related
- [GIFT serves as a testbed for developing and validating expert models for psychomotor tasks such as rifle marksmanship](gift-testbed-psychomotor-expert-models.md) — a broader claim this one bears on
- [Expert-elicited causal model is compatible with observed data but slightly less predictive than a data-learned Bayesian network](expert-causal-model-vs-data-learned-bn-predictive-accuracy.md) — related
- [Kneeling stance produces worse shot-group performance on average than prone stance among expert marksmen](kneeling-worse-than-prone-expert-groups.md) — related
