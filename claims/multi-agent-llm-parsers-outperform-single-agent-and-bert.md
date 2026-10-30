---
type: claim
title: Multi-agent LLM parsers outperform single-agent structures and BERT baselines in evaluating scaffold reliability
description: Multi-agent LLM parsers outperform single-agent structures and BERT baselines in evaluating scaffold reliability
id: multi-agent-llm-parsers-outperform-single-agent-and-bert
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-29
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: qian-2025
    resource: "https://arxiv.org/abs/2508.05929"
    title: "Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D. (2025). Towards Reliable Generative AI-Driven Scaffolding: Reducing Hallucinations and Enhancing Quality in Self-Regulated Learning Support. https://arxiv.org/abs/2508.05929"
    author: "Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Multi-agent LLM parsers outperform single-agent structures and BERT baselines in evaluating scaffold reliability

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Multi-agent LLM parsers significantly outperformed single-agent parsers and a fine-tuned BERT baseline (κ = -0.100) in evaluating which SRL processes LLM-generated scaffolds support. [→ Qian 2025](#qian-2025)

## Evidence

### Qian 2025

Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D. (2025). Towards Reliable Generative AI-Driven Scaffolding: Reducing Hallucinations and Enhancing Quality in Self-Regulated Learning Support. https://arxiv.org/abs/2508.05929

`q2 · i?` · `design · r2`

Comparison of LLM parsers against a fine-tuned BERT baseline on the same 594-scaffold dataset. The BERT model achieved κ = -0.100 and accuracy = 0.613, while multi-agent LLM parsers reached substantially higher agreement.

> "The performance of LLM parsers also significantly outperformed the machine learning baseline represented by a fine-tuned BERT model (𝜅 = −0.100, 95% CI [-0.193, -0.007], accuracy = 0.613, 95% CI [0.541, 0.685])."

## Discussion


## Related Claims
- [Multi-agent LLM parsers achieve near-perfect agreement with human experts when evaluating the reliability of LLM-generated SRL scaffolds](multi-agent-llm-reliability-evaluation-near-perfect-agreement.md) — possibly the same claim (merge candidate)
