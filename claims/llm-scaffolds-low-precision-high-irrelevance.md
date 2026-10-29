---
type: claim
title: LLM-generated scaffolds show low precision and high irrelevance rates in targeting intended SRL processes
description: LLM-generated scaffolds show low precision and high irrelevance rates in targeting intended SRL processes
id: llm-scaffolds-low-precision-high-irrelevance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-29
evidence_strength: moderate
newest_evidence: 2025
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

# LLM-generated scaffolds show low precision and high irrelevance rates in targeting intended SRL processes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` All tested LLMs produced scaffolds with precision below 73%, irrelevance rates above 13%, and error rates exceeding 3% when generating scaffolds targeting specific SRL processes. [→ Qian 2025](#qian-2025)

## Evidence

### Qian 2025

Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D. (2025). Towards Reliable Generative AI-Driven Scaffolding: Reducing Hallucinations and Enhancing Quality in Self-Regulated Learning Support. https://arxiv.org/abs/2508.05929

`q2 · i?` · `design · r2`

Precision, error rate, and irrelevance rate were calculated for each LLM scaffold generator (n = 24 scaffolds per generator) against human annotations. GPT-4-Turbo achieved the highest precision (0.613) while Gemini-Pro showed the lowest (0.355).

> "Despite this, all LLMs produced scaffolds with precision below 73%, irrelevance rates above 13%, and non-negligible error rates exceeding 3%, reflecting ongoing limitations in the alignment between LLM scaffold generation and scaffold-generation requirements."

## Discussion


## Related Claims
- [Multi-agent LLM parsers achieve near-perfect agreement with human experts when evaluating the reliability of LLM-generated SRL scaffolds](multi-agent-llm-reliability-evaluation-near-perfect-agreement.md) — related
