---
type: claim
title: Hardcoded solutions consistently outperform generalized solutions in mathematical code-based rationales
description: Hardcoded solutions consistently outperform generalized solutions in mathematical code-based rationales
id: hardcoded-solutions-outperform-generalized-solutions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: chengwei-wei-2025
    resource: "https://doi.org/10.18653/v1/2025.findings-acl.44"
    title: "Chengwei Wei, Bin Wang, Jung-jae Kim, Guimei Liu, Nancy F. Chen. (2025). CoinMath: Harnessing the Power of Coding Instruction for Math LLMs. arXiv. [doi:10.18653/v1/2025.findings-acl.44](https://doi.org/10.18653/v1/2025.findings-acl.44)"
    author: Chengwei Wei, Bin Wang, Jung-jae Kim, Guimei Liu, Nancy F. Chen
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Hardcoded solutions consistently outperform generalized solutions in mathematical code-based rationales

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across all four evaluated models, hardcoded problem-specific solutions yield higher zero-shot math accuracy than generalized reusable-function solutions. [→ Chengwei Wei 2025](#chengwei-wei-2025)

## Evidence

### Chengwei Wei 2025

Chengwei Wei, Bin Wang, Jung-jae Kim, Guimei Liu, Nancy F. Chen. (2025). CoinMath: Harnessing the Power of Coding Instruction for Math LLMs. arXiv. [doi:10.18653/v1/2025.findings-acl.44](https://doi.org/10.18653/v1/2025.findings-acl.44)

`q2 · i?` · `causal · r2`

Instruction-tuning comparison of Solution Generality across four models; Table 3 shows e.g. CodeLlama-Python-7B average 59.4 (Hardcoded) vs 53.9 (Generalized). The paper reports hardcoded solutions "consis- tently outperform generalized solutions".

> "As shown in Table 3, hardcoded solutions consis- tently outperform generalized solutions, suggesting that models benefit more from the explicit speci- ficity of hardcoded logic, which simplifies learn- ing."

## Discussion


## Related Claims
- [Combining concise comments, descriptive naming, and hardcoded solutions yields better math performance than combining all coding styles or their counterparts](beneficial-style-combination-ablation.md) — related
- CoinMath outperforms MAmmoTH by an average improvement of 5.9% in accuracy on math evaluation datasets — related
