---
type: claim
title: "Higher item noise, shared items among conceptually nested energy LOs, and smallest sample size explain the EMCS energy LOs' low classification accuracy"
description: "Higher item noise, shared items among conceptually nested energy LOs, and smallest sample size explain the EMCS energy LOs' low classification accuracy"
id: energy-lo-low-accuracy-sources
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: weak
sources:
  - id: vy-le-2026
    resource: "https://doi.org/10.48550/arxiv.2609.09584"
    title: "Vy Le, Jayson M. Nissen, Jason W. Morphew, Hua Hua Chang, and Ben Van Dusen. (2026). Mechanics Cognitive Diagnostic: Testing Fine-Grained Learning Objectives in Introductory Physics. https://arxiv.org/abs/2609.09584 [doi:10.48550/arxiv.2609.09584](https://doi.org/10.48550/arxiv.2609.09584)"
    author: Vy Le, Jayson M. Nissen, Jason W. Morphew, Hua Hua Chang, and Ben Van Dusen
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: vy-le-2026-2
    resource: "https://arxiv.org/abs/2609.09584"
    title: "Vy Le, Jayson M. Nissen, Jason W. Morphew, Hua Hua Chang, and Ben Van Dusen. (2026). Mechanics Cognitive Diagnostic: Testing Fine-Grained Learning Objectives in Introductory Physics. https://arxiv.org/abs/2609.09584"
    author: Vy Le, Jayson M. Nissen, Jason W. Morphew, Hua Hua Chang, and Ben Van Dusen
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Higher item noise, shared items among conceptually nested energy LOs, and smallest sample size explain the EMCS energy LOs' low classification accuracy

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 design `r2` · `q2`

## Subclaims
`q2 i?` EMCS items are noisier than FCI and FMCE items, with a mean DINA slipping parameter of 0.349 versus 0.138 and 0.136. [→ Vy Le 2026](#vy-le-2026)
`q2 i?` The three energy LOs share most of their items, preventing DINA from separating their mastery, while momentum LOs draw on largely separate items. [→ Vy Le 2026 (2)](#vy-le-2026-2)

## Evidence

### Vy Le 2026

Vy Le, Jayson M. Nissen, Jason W. Morphew, Hua Hua Chang, and Ben Van Dusen. (2026). Mechanics Cognitive Diagnostic: Testing Fine-Grained Learning Objectives in Introductory Physics. https://arxiv.org/abs/2609.09584 [doi:10.48550/arxiv.2609.09584](https://doi.org/10.48550/arxiv.2609.09584)

`q2 · i?` · `design · r2`

Authors' examination of DINA slipping and guessing parameters (and 3PL parameters) for every item found "The mean DINA slipping parameter is 0.349 on the EMCS versus 0.138 on the FCI and 0.136 on the FMCE," weakening each response's evidential value.

> "The mean DINA slipping parameter is 0.349 on the EMCS versus 0.138 on the FCI and 0.136 on the FMCE."

### Vy Le 2026 (2)

Vy Le, Jayson M. Nissen, Jason W. Morphew, Hua Hua Chang, and Ben Van Dusen. (2026). Mechanics Cognitive Diagnostic: Testing Fine-Grained Learning Objectives in Introductory Physics. https://arxiv.org/abs/2609.09584

`q2 · i?` · `design · r2`

Authors' analysis of item mapping found the energy LOs' item overlap "reflects the conceptual nesting of the energy LOs rather than a coding error," violating the DINA conjunctive independent-attribute assumption; momentum LOs share 18–33% of items.

> "Eight items require all three, and any two energy LOs share about 70% of their items (Jaccard overlap 0.67–0.73). The three momentum LOs draw on largely separate items."

## Discussion


## Related Claims
- [Classification accuracy met or exceeded benchmarks for 19 of 22 LO-assessment combinations, with three EMCS energy LOs below the acceptable range](classification-accuracy-22-lo-combinations.md) — related
- [Misspecification of theoretical diagnostic classification models and inaccurate Q-matrices impact classification accuracy](tdcm-qmatrix-misspecification-hurts-classification.md) — a broader claim this one bears on
- [The combined FCI, FMCE, and EMCS item bank covers all 14 learning objectives with at least six items each, mostly single- or two-LO items](rba-item-bank-covers-14-los.md) — related
- [DINA models fit FCI and EMCS posttest data well but fit FMCE data only marginally](dina-fit-fci-emcs-good-fmce-marginal.md) — related
