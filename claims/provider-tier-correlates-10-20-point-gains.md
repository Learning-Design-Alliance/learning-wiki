---
type: claim
title: "Within each provider's model family, successive performance tiers correlate with roughly 10–20 percentage-point accuracy increases"
description: "Within each provider's model family, successive performance tiers correlate with roughly 10–20 percentage-point accuracy increases"
id: provider-tier-correlates-10-20-point-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: giulia-polverini-and-bor-gregorcic-2025
    resource: "https://doi.org/10.1088/1361-6404/ae03f8"
    title: "Giulia Polverini and Bor Gregorcic. (2025). Multimodal large language models and physics visual tasks: comparative analysis of performance and costs. [doi:10.1088/1361-6404/ae03f8](https://doi.org/10.1088/1361-6404/ae03f8)"
    author: Giulia Polverini and Bor Gregorcic
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Within each provider's model family, successive performance tiers correlate with roughly 10–20 percentage-point accuracy increases

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Within OpenAI, Google, and Anthropic families, higher tiers outperformed lower tiers, with successive tiers correlating with 10–20 percentage-point increases in most cases. [→ Giulia Polverini and Bor Gregorcic 2025](#giulia-polverini-and-bor-gregorcic-2025)

## Evidence

### Giulia Polverini and Bor Gregorcic 2025

Giulia Polverini and Bor Gregorcic. (2025). Multimodal large language models and physics visual tasks: comparative analysis of performance and costs. [doi:10.1088/1361-6404/ae03f8](https://doi.org/10.1088/1361-6404/ae03f8)

`q2 · i?` · `design · r2`

Family-level analysis of Table 3 results shows GPT-5, o3, GPT-5 mini, o4 mini and GPT-5 nano beat GPT-4.1 variants, Gemini 2.5 Pro beat Flash tiers, and Claude Opus 4 beat Sonnet 4 and Haiku 3.5; "in most cases each successive tier within a provider correlates with a performance increase of 10–20 percentage points."

> "While exact differences vary, in most cases each successive tier within a provider correlates with a performance increase of 10–20 percentage points."

## Discussion


## Related Claims
- [Cost and performance are correlated but not proportional: GPT-5 mini scored 75% at $0.26 while Claude Opus 4 underperformed at 57.0% despite high cost](mllm-cost-performance-not-proportional.md) — reports the opposite
- [Direct comparisons confirm ChatGPT-4 significantly outperformed earlier versions and some competitor models on dental examination questions](chatgpt4-outperforms-earlier-versions-dental-questions.md) — related
- [GPT-4o answered image-based USMLE sample items with 89.5% accuracy versus GPT-4's 73.4%, a numerically higher but not statistically significant difference](gpt4o-89-5-percent-image-usmle-accuracy.md) — a narrower finding that bears on this claim
- [Pairwise McNemar comparisons showed OpenAI o1 significantly better than GPT-4o, Gemini, and Copilot in Respiratory Medicine, with mixed significance across other courses](mcnemar-pairwise-openai-o1-vs-other-llms-mixed.md) — related
