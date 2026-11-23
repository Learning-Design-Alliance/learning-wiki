---
type: claim
title: General-domain coding instruction alone boosts PoT math performance, but mixing it with Math-Code reduces effectiveness relative to Math-Code alone
description: General-domain coding instruction alone boosts PoT math performance, but mixing it with Math-Code reduces effectiveness relative to Math-Code alone
id: general-code-limited-benefit-math-reasoning
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
  - id: chengwei-wei-2025-2
    resource: "https://doi.org/10.18653/v1/2025.findings-acl.44"
    title: "Chengwei Wei, Bin Wang, Jung-jae Kim, Guimei Liu, Nancy F. Chen. (2025). CoinMath: Harnessing the Power of Coding Instruction for Math LLMs. arXiv. [doi:10.18653/v1/2025.findings-acl.44](https://doi.org/10.18653/v1/2025.findings-acl.44)"
    author: Chengwei Wei, Bin Wang, Jung-jae Kim, Guimei Liu, Nancy F. Chen
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# General-domain coding instruction alone boosts PoT math performance, but mixing it with Math-Code reduces effectiveness relative to Math-Code alone

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Training solely on General Code mostly enhances zero-shot and few-shot math performance by improving valid code generation, but models trained solely on Math-Code achieve the best performance and adding General Code reduces it. [→ Chengwei Wei 2025](#chengwei-wei-2025)
`q2 i?` Training on General Code improves the models' valid code rate, which the authors identify as the mechanism behind the accuracy gain. [→ Chengwei Wei 2025 (2)](#chengwei-wei-2025-2)

## Evidence

### Chengwei Wei 2025

Chengwei Wei, Bin Wang, Jung-jae Kim, Guimei Liu, Nancy F. Chen. (2025). CoinMath: Harnessing the Power of Coding Instruction for Math LLMs. arXiv. [doi:10.18653/v1/2025.findings-acl.44](https://doi.org/10.18653/v1/2025.findings-acl.44)

`q2 · i?` · `causal · r2`

Zero-shot and few-shot instruction-tuning comparison of General Code, Math-Code, and their mix on Llama-3.1-8B and CodeLlama-Python-7B (Table 4); e.g. zero-shot Llama averages 27.2 (G.C.), 66.8 (M.C.), 58.2 (Mix).

> "However, models solely trained on Math-Code achieve the best performance, and incorporating General Code alongside Math-Code reduces its effectiveness."

### Chengwei Wei 2025 (2)

Chengwei Wei, Bin Wang, Jung-jae Kim, Guimei Liu, Nancy F. Chen. (2025). CoinMath: Harnessing the Power of Coding Instruction for Math LLMs. arXiv. [doi:10.18653/v1/2025.findings-acl.44](https://doi.org/10.18653/v1/2025.findings-acl.44)

`q2 · i?` · `causal · r2`

Analysis of valid code rate, defined as the percentage of executable code generated, shown in Figure 2 under zero-shot settings for Llama-3.1-8B and CodeLlama-Python-7B.

> "The results demonstrate that training on General Code significantly improves the models' ability to generate valid code and adhere to instructions, leading to higher accuracy in solving mathematical questions."

## Discussion


## Related Claims
- Instruction-based fine-tuning on LAZY REVIEW significantly improves LLM lazy-thinking detection over zero-shot and few-shot baselines — related
- [Prompting technique effects are task-dependent: few-shot and self-consistency help, while chain-of-thought helps praise detection but hurts error recognition](prompting-techniques-task-dependent-tutor-moves.md) — related
- [Adding textual rationales to code-based ones helps general-purpose LLMs slightly but negatively impacts code-specialized models](math-text-supplement-depends-on-model-type.md) — related
