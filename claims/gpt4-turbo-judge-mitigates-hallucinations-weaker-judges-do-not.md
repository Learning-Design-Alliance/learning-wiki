---
type: claim
title: GPT-4-Turbo as an LLM Judge reliably selects better scaffolds and mitigates hallucination errors, while weaker LLM Judges do not
description: GPT-4-Turbo as an LLM Judge reliably selects better scaffolds and mitigates hallucination errors, while weaker LLM Judges do not
id: gpt4-turbo-judge-mitigates-hallucinations-weaker-judges-do-not
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
  - id: qian-2025-2
    resource: "https://arxiv.org/abs/2508.05929"
    title: "Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D. (2025). Towards Reliable Generative AI-Driven Scaffolding: Reducing Hallucinations and Enhancing Quality in Self-Regulated Learning Support. https://arxiv.org/abs/2508.05929"
    author: "Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4-Turbo as an LLM Judge reliably selects better scaffolds and mitigates hallucination errors, while weaker LLM Judges do not

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4-Turbo acting as an LLM Judge achieved accuracy of 0.70 and moderate agreement (κ = 0.40) with human labels, significantly above chance, while GPT-3.5-Turbo and Gemini-Pro performed at chance level. [→ Qian 2025](#qian-2025)

## Evidence

### Qian 2025

Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D. (2025). Towards Reliable Generative AI-Driven Scaffolding: Reducing Hallucinations and Enhancing Quality in Self-Regulated Learning Support. https://arxiv.org/abs/2508.05929

`q2 · i?` · `design · r2`

Evaluation of three LLM Judges on 160 scaffold comparison settings derived from 80 scaffold pairs where one scaffold was hallucinated. GPT-4-Turbo was the only Judge whose lower confidence bound exceeded chance-level accuracy of 0.50.

> "among the three LLM Judges, GPT-4-Turbo demonstrated the highest performance with an accuracy of 0.70 (95% CI [0.63, 0.77]) and a moderate level of agreement with human annotations (𝜅 = 0.40, 95% CI [0.28, 0.52])."

### Qian 2025 (2)

Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D. (2025). Towards Reliable Generative AI-Driven Scaffolding: Reducing Hallucinations and Enhancing Quality in Self-Regulated Learning Support. https://arxiv.org/abs/2508.05929

`q2 · i?` · `design · r2`

GPT-3.5-Turbo and Gemini-Pro as LLM Judges showed chance-level accuracy with confidence intervals including 0.50, and poor agreement with the human benchmark (κ = -0.04 and κ = 0.04 respectively).

> "In contrast, the other two LLM Judges, GPT-3.5-Turbo and Gemini-Pro, exhibited significantly lower performance, with accuracies of 0.48 (95% CI [0.40, 0.56]) and 0.52 (95% CI [0.44, 0.60]), respectively."

## Discussion


## Related Claims
- [Multi-agent LLM parsers achieve near-perfect agreement with human experts when evaluating the reliability of LLM-generated SRL scaffolds](multi-agent-llm-reliability-evaluation-near-perfect-agreement.md) — related
- [Human-LLM agreement remains low across constructs (κ = 0.000 to 0.419), with self-efficacy showing the best alignment and Prior KSAs none](human-llm-agreement-low-construct-varying.md) — related
- [The LLM-judge scoring pipeline for the two metrics aligns with human labels and human raters](llm-judge-pipeline-validated-against-human-raters.md) — related
- [Human-LLM agreement on a complex multi-label codebook falls well below human-human agreement, while LLM-LLM agreement is comparable to human-human agreement](human-llm-agreement-gap-jaccard.md) — related
- [Back-translation evaluation outperforms LLM-as-a-Judge (code+image) in agreement with human raters across four models](backtranslation-outperforms-llm-judge-diagram-agreement.md) — related
