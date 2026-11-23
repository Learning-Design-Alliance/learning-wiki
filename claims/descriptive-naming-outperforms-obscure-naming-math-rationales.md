---
type: claim
title: Descriptive variable naming in code-based rationales generally outperforms obscure naming for LLM math reasoning
description: Descriptive variable naming in code-based rationales generally outperforms obscure naming for LLM math reasoning
id: descriptive-naming-outperforms-obscure-naming-math-rationales
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

# Descriptive variable naming in code-based rationales generally outperforms obscure naming for LLM math reasoning

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Training on rationales with Descriptive Naming yields higher zero-shot math accuracy than Obscure Naming across the four evaluated models. [→ Chengwei Wei 2025](#chengwei-wei-2025)

## Evidence

### Chengwei Wei 2025

Chengwei Wei, Bin Wang, Jung-jae Kim, Guimei Liu, Nancy F. Chen. (2025). CoinMath: Harnessing the Power of Coding Instruction for Math LLMs. arXiv. [doi:10.18653/v1/2025.findings-acl.44](https://doi.org/10.18653/v1/2025.findings-acl.44)

`q2 · i?` · `causal · r2`

Instruction-tuning comparison holding comments and logic unchanged while varying naming; Table 2 shows e.g. Llama-3.1-8B average 68.2 (Descriptive) vs 66.5 (Obscure). The paper reports "Descriptive Naming generally outperforms Obscure Naming".

> "As shown in Table 2, the results indicate that De- scriptive Naming generally outperforms Obscure Naming."

## Discussion


## Related Claims
- [Combining concise comments, descriptive naming, and hardcoded solutions yields better math performance than combining all coding styles or their counterparts](beneficial-style-combination-ablation.md) — related
- CoinMath outperforms MAmmoTH by an average improvement of 5.9% in accuracy on math evaluation datasets — related
