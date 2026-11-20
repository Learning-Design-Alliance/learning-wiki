---
type: claim
title: DINA models fit FCI and EMCS posttest data well but fit FMCE data only marginally
description: DINA models fit FCI and EMCS posttest data well but fit FMCE data only marginally
id: dina-fit-fci-emcs-good-fmce-marginal
aliases: [dina-model-fit-fci-emcs-good-fmce-marginal]
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-11-20
recheck_by: 2029
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
  - id: vy-le-2025
    resource: "https://doi.org/10.1103/PhysRevPhysEducRes.21.010103"
    title: "Vy Le, Jayson M. Nissen, Xiuxiu Tang, Yuxiao Zhang, Amirreza Mehrabi, Jason W. Morphew, Hua Hua Chang, and Ben Van Dusen. (2025). Applying cognitive diagnostic models to mechanics concept inventories. Physical Review Physics Education Research 21, 010103. https://doi.org/10.1103/PhysRevPhysEducRes.21.010103"
    author: Vy Le, Jayson M. Nissen, Xiuxiu Tang, Yuxiao Zhang, Amirreza Mehrabi, Jason W. Morphew, Hua Hua Chang, and Ben Van Dusen
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# DINA models fit FCI and EMCS posttest data well but fit FMCE data only marginally

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies (3 entries) · 2 design `r2`–`r3` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-11-20 (automated, 3 of 3 entries) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims

`q2 i?` DINA models fit FCI and EMCS response data well (RMSEA2 at or below 0.05, SRMSR at or below 0.07) but not FMCE data. [→ Vy Le 2026](#vy-le-2026)

`q2 i?` DINA model fit indices indicate satisfactory fit for the FCI (RMSEA2 = 0.048, SRMSR = 0.062) and EMCS (RMSEA2 = 0.028, SRMSR = 0.041) but unsatisfactory fit for the FMCE (RMSEA2 = 0.090, SRMSR = 0.110). [→ Vy Le 2025](#vy-le-2025)

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

### Vy Le 2025

Vy Le, Jayson M. Nissen, Xiuxiu Tang, Yuxiao Zhang, Amirreza Mehrabi, Jason W. Morphew, Hua Hua Chang, and Ben Van Dusen. (2025). Applying cognitive diagnostic models to mechanics concept inventories. Physical Review Physics Education Research 21, 010103. https://doi.org/10.1103/PhysRevPhysEducRes.21.010103

`q2 · i?` · `design · r3`

Psychometric analysis fitting the DINA model with the refined Q-matrix to post-test response data from 19,889 students on the LASSO platform, using RMSEA2 and SRMSR criteria. The article reports "satisfactory fit" for FCI and EMCS and unsatisfactory fit for FMCE with the printed indices.

> "the model demonstrated satisfactory fit (RMSEA 2 < 0.05, SRMSR < 0.07) for the FCI (RMSEA2 ¼ 0.048, SRMSR ¼ 0.062) and EMCS (RMSEA2 ¼ 0.028, SRMSR ¼ 0.041), whereas the fit for the FMCE was unsatisfactory (RMSEA 2 ¼ 0.090, SRMSR ¼ 0.110)."

## Discussion



## Related Claims

- [The 14-LO attribute structure improved DINA model fit over MCD-v1's four-skill structure for all three RBAs](14-lo-structure-improved-fit-over-mcd-v1.md) — related
- [Classification accuracy met or exceeded benchmarks for 19 of 22 LO-assessment combinations, with three EMCS energy LOs below the acceptable range](classification-accuracy-22-lo-combinations.md) — related
- [Higher item noise, shared items among conceptually nested energy LOs, and smallest sample size explain the EMCS energy LOs' low classification accuracy](energy-lo-low-accuracy-sources.md) — related
- [Research favors fine-grained knowledge components, but fine granularity brings practical costs that can outweigh better data fit](fine-granularity-knowledge-components-practical-costs.md) — related
