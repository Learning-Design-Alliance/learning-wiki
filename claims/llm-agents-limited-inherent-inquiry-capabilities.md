---
type: claim
title: LLM-based agents show limited inherent inquiry capabilities, with low rates of correctly discovered equations that improve with in-context examples
description: LLM-based agents show limited inherent inquiry capabilities, with low rates of correctly discovered equations that improve with in-context examples
id: llm-agents-limited-inherent-inquiry-capabilities
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
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

# LLM-based agents show limited inherent inquiry capabilities, with low rates of correctly discovered equations that improve with in-context examples

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Open-source LLMs performed poorly in zero-shot inquiry-based model discovery, achieving scores of up to 12.6%, and few-shot examples improved performance for most models, with Llama-70B reaching 24.1%. [→ Marta Knežević 2026](#marta-knezevic-2026)

## Evidence

### Marta Knežević 2026

Marta Knežević, Seyed Parsa Neshaei, Jibril Frej, Vinitra Swamy, Tanja Käser. (2026). Evaluating Inquiry Learning in LLM-Based Agents: Hypothesizing, Reasoning, and Exploration. arXiv. [doi:10.18653/2026.findings-emnlp.1861](https://doi.org/10.18653/2026.findings-emnlp.1861)

`q2 · i?` · `causal · r2`

Benchmark evaluation of seven LLMs (six open-source plus GPT-4o) on 174 multivariable equations in the IL-based exploration setting, reported in Results §5.1 and Table 2. The article reports zero-shot scores "of up to 12.6%" and that Llama-70B reached 24.1% with in-context examples.

> "All open-source models per- formed poorly in the zero-shot setting, achieving scores of up to 12.6%. Providing in-context exam- ples improved performance in all models except Llama-8B, with Llama-70B reaching24.1%."

## Discussion


## Related Claims
- Domain priors from meaningful variable names improve LLM mathematical model discovery compared with abstract variable names — related
- [LLM agents rarely explore strategically without guidance; GIL scaffolding raises the proportion of strategic exploration steps](gil-raises-strategic-exploration-proportion.md) — related
- [Guided Inquiry Learning scaffolding improves LLM agents' equation-discovery success over unguided IL for most models](gil-scaffolding-improves-llm-equation-discovery.md) — related
- [LLM equation-discovery accuracy drops sharply as the number of independent variables increases](llm-inquiry-accuracy-declines-with-equation-complexity.md) — related
