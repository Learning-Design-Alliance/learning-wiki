---
type: claim
title: LLM equation-discovery accuracy drops sharply as the number of independent variables increases
description: LLM equation-discovery accuracy drops sharply as the number of independent variables increases
id: llm-inquiry-accuracy-declines-with-equation-complexity
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
sources:
  - id: marta-knežević-2026
    resource: "https://doi.org/10.18653/2026.findings-emnlp.1861"
    title: "Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser. (2026). Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration. arXiv. [doi:10.18653/2026.findings-emnlp.1861](https://doi.org/10.18653/2026.findings-emnlp.1861)"
    author: Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LLM equation-discovery accuracy drops sharply as the number of independent variables increases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the IL 3-shot setting, accuracy fell from 34.5% to 12.1% for Qwen-32B, from 34.5% to 10.3% for Llama-70B, and from 31% to 13.8% for GPT-4o as independent variables increased from three to five. [→ Marta Knežević 2026](#marta-knezevic-2026)

## Evidence

### Marta Knežević 2026

Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser. (2026). Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration. arXiv. [doi:10.18653/2026.findings-emnlp.1861](https://doi.org/10.18653/2026.findings-emnlp.1861)

`q2 · i?` · `causal · r2`

Analysis of accuracy across equation complexity (3, 4, or 5 independent variables) shown in Figure 2 and reported in Results §5.1. The article reports the printed accuracy drops for the three named models and states few-shot examples consistently improved performance for four models across difficulty levels.

> "in the IL 3-shot setting, accuracy for Qwen-32B, Llama-70B, and GPT-4o fell from 34.5% to 12.1%, 34.5% to 10.3%, and 31% to 13.8%, respectively, highlighting the challenge of multivariable modeling."

## Discussion


## Related Claims
- [LLM-based agents show limited inherent inquiry capabilities, with low rates of correctly discovered equations that improve with in-context examples](llm-agents-limited-inherent-inquiry-capabilities.md) — related
- [Guided Inquiry Learning scaffolding improves LLM agents' equation-discovery success over unguided IL for most models](gil-scaffolding-improves-llm-equation-discovery.md) — related
- Domain priors from meaningful variable names improve LLM mathematical model discovery compared with abstract variable names — related
