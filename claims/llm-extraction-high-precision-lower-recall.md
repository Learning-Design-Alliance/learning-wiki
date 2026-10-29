---
type: claim
title: LLM data extraction accuracy varies by data type, with high precision but lower recall across tasks
description: LLM data extraction accuracy varies by data type, with high precision but lower recall across tasks
id: llm-extraction-high-precision-lower-recall
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2025
sources:
  - id: schroeder-2025
    resource: "https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2"
    title: "Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K. (2025). AI-Assisted Data Extraction for Systematic Reviews in Education. https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2"
    author: "Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K."
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# LLM data extraction accuracy varies by data type, with high precision but lower recall across tasks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r3` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Across all main-study analyses, precision was consistently high (0.89–0.95) while recall was substantially lower (0.58–0.88), and confusion matrices showed models were more likely to extract inaccurate data than to claim information was not reported. [→ Schroeder 2025](#schroeder-2025)

## Evidence

### Schroeder 2025

Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K. (2025). AI-Assisted Data Extraction for Systematic Reviews in Education. https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2

`q2 · i?` · `design · r3`

Overall exact-match analysis in the main study across all 24 variables and 112 studies. "Precision was high (ranging from 0.90 - 0.93) while recall was substantially lower (ranging from 0.61 - 0.76)". The pattern of high precision and lower recall held across explicit and derived variables.

> "Precision was high (ranging from 0.90 - 0.93) while recall was substantially lower (ranging from 0.61 - 0.76). The confusion matrices show that, generally speaking, models were more likely to extract inaccurate data rather than claim the information was not reported when it actually was."

## Discussion


## Related Claims
- [LLMs are substantially less accurate at extracting and categorizing derived data based on predefined categories than at extracting explicitly stated data](llms-less-accurate-derived-categorical-data-extraction.md) — related
- [LLMs show moderate agreement with human coders when extracting explicitly stated data from education studies](llms-moderate-agreement-explicit-data-extraction-education.md) — related
- [In zero-shot evaluation, GPT-4's multi-label classification results were similar to what might be expected of fine-tuned classifiers, with SetFit and GPT-3.5 showing contrasting precision/recall patterns](gpt4-zero-shot-comparable-finetuned-classifiers.md) — related
- [LLMs are not ready to be used as primary data extraction tools without explicit human validation in education research synthesis](llms-not-ready-primary-data-extraction-without-human-validation.md) — related
- [Hint-based prompts raise ChatGPT scoring agreement with human experts to 98–100%, while no-hint prompts are unstable (Q2 precision 0.42)](hint-prompts-raise-llm-scoring-agreement.md) — related
