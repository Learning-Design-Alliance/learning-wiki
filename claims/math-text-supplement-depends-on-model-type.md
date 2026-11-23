---
type: claim
title: Adding textual rationales to code-based ones helps general-purpose LLMs slightly but negatively impacts code-specialized models
description: Adding textual rationales to code-based ones helps general-purpose LLMs slightly but negatively impacts code-specialized models
id: math-text-supplement-depends-on-model-type
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
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

# Adding textual rationales to code-based ones helps general-purpose LLMs slightly but negatively impacts code-specialized models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For general-purpose Llama-3.1-8B, incorporating Math-Text alongside Math-Code slightly improves math performance. [→ Chengwei Wei 2025](#chengwei-wei-2025)

## Evidence

### Chengwei Wei 2025

Chengwei Wei, Bin Wang, Jung-jae Kim, Guimei Liu, Nancy F. Chen. (2025). CoinMath: Harnessing the Power of Coding Instruction for Math LLMs. arXiv. [doi:10.18653/v1/2025.findings-acl.44](https://doi.org/10.18653/v1/2025.findings-acl.44)

`q2 · i?` · `causal · r2`

Instruction-tuning comparison of Math-Text, Math-Code, and their mix on identical math questions (Table 5); zero-shot Llama-3.1-8B averages 44.0 (M.T.), 66.8 (M.C.), 67.9 (Mix). The paper reports the mix "slightly improves performance".

> "For the general-purpose model, Llama-3.1-8B, incorporating Math-Text alongside Math-Code slightly improves performance by en- hancing the model's ability to comprehend math- ematical problems in a language-based manner."

## Discussion


## Related Claims
- Adding comments to mathematical code-based rationales improves LLM math reasoning, with concise comments slightly outperforming detailed comments — related
- [General-domain coding instruction alone boosts PoT math performance, but mixing it with Math-Code reduces effectiveness relative to Math-Code alone](general-code-limited-benefit-math-reasoning.md) — related
