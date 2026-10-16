---
type: claim
title: DINA models fit FCI and EMCS posttest data well but fit FMCE data only marginally
description: DINA models fit FCI and EMCS posttest data well but fit FMCE data only marginally
id: dina-fit-fci-emcs-good-fmce-marginal
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
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

# DINA models fit FCI and EMCS posttest data well but fit FMCE data only marginally

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` DINA models fit FCI and EMCS response data well (RMSEA2 at or below 0.05, SRMSR at or below 0.07) but not FMCE data. [→ Vy Le 2026](#vy-le-2026)

## Evidence

### Vy Le 2026

Vy Le, Jayson M. Nissen, Jason W. Morphew, Hua Hua Chang, and Ben Van Dusen. (2026). Mechanics Cognitive Diagnostic: Testing Fine-Grained Learning Objectives in Introductory Physics. https://arxiv.org/abs/2609.09584 [doi:10.48550/arxiv.2609.09584](https://doi.org/10.48550/arxiv.2609.09584)

`q2 · i?` · `design · r2`

Analysis of cleaned LASSO posttest responses (15,371 FCI, 7,033 FMCE, 1,990 EMCS) fit separate DINA models with the refined Q-matrix. "Both assessments met the criteria for good model fit" (RMSEA2 ≤ 0.05, SRMSR ≤ 0.07).

> "The FCI yielded RMSEA2 = 0.033 and SRMSR = 0.055. The EMCS yielded RMSEA2 = 0.022 and SRMSR = 0.037. Both assessments met the criteria for good model fit."

### Vy Le 2026 (2)

Vy Le, Jayson M. Nissen, Jason W. Morphew, Hua Hua Chang, and Ben Van Dusen. (2026). Mechanics Cognitive Diagnostic: Testing Fine-Grained Learning Objectives in Introductory Physics. https://arxiv.org/abs/2609.09584

`q2 · i?` · `design · r2`

The same DINA analyses of LASSO posttest data found FMCE misfit. The authors attribute it to item blocking: "Item chaining creates local item dependence among items within each block," violating the DINA conditional independence assumption.

> "The FMCE yielded RMSEA2 = 0.065 and SRMSR = 0.087, falling outside the criteria (RMSEA2 ≤ 0.05, and SRMSR ≤ 0.07). These results indicate that the DINA model does not reproduce the FMCE response data as well as it does for the FCI and EMCS."

## Discussion


## Related Claims
- [The 14-LO attribute structure improved DINA model fit over MCD-v1's four-skill structure for all three RBAs](14-lo-structure-improved-fit-over-mcd-v1.md) — related
- [Classification accuracy met or exceeded benchmarks for 19 of 22 LO-assessment combinations, with three EMCS energy LOs below the acceptable range](classification-accuracy-22-lo-combinations.md) — related
- [Higher item noise, shared items among conceptually nested energy LOs, and smallest sample size explain the EMCS energy LOs' low classification accuracy](energy-lo-low-accuracy-sources.md) — related
