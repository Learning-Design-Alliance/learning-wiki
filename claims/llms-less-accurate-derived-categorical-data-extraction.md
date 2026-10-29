---
type: claim
title: LLMs are substantially less accurate at extracting and categorizing derived data based on predefined categories than at extracting explicitly stated data
description: LLMs are substantially less accurate at extracting and categorizing derived data based on predefined categories than at extracting explicitly stated data
id: llms-less-accurate-derived-categorical-data-extraction
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
sources:
  - id: schroeder-2025
    resource: "https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2"
    title: "Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K. (2025). AI-Assisted Data Extraction for Systematic Reviews in Education. https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2"
    author: "Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: schroeder-2025-2
    resource: "https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2"
    title: "Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K. (2025). AI-Assisted Data Extraction for Systematic Reviews in Education. https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2"
    author: "Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLMs are substantially less accurate at extracting and categorizing derived data based on predefined categories than at extracting explicitly stated data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`

## Subclaims
`q2 i?` For 15 derived variables requiring categorization, exact-match agreement fell to 65.48% (Gemini 1.5 Pro, k = 0.24), 64.88% (Gemini 1.5 Flash, k = 0.23), and 56.79% (Mistral Large 2, k = 0.12). [→ Schroeder 2025](#schroeder-2025)
`q2 i?` Accurate-match agreement for derived variables was also low (best: 70.24%, k = 0.29), with recall of 0.64–0.75 despite high precision (0.91–0.93). [→ Schroeder 2025 (2)](#schroeder-2025-2)

## Evidence

### Schroeder 2025

Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K. (2025). AI-Assisted Data Extraction for Systematic Reviews in Education. https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2

`q2 · i?` · `design · r2`

Main-study analysis of 15 derived variables across 112 studies. "Google Gemini 1.5 Pro was again the most accurate, with 65.48% agreement (k = 0.24)". Precision was strong (0.90–0.92) but recall was lower (0.58–0.70).

> "When evaluating the models’ abilities to extract data that exactly matches the human coder’s data extraction, Google Gemini 1.5 Pro was again the most accurate, with 65.48% agreement (k = 0.24), followed by Google Gemini 1.5 Flash with 64.88% agreement (k = 0.23) and Mistral Large 2 (56.79% agreement, k = 0.12)."

### Schroeder 2025 (2)

Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K. (2025). AI-Assisted Data Extraction for Systematic Reviews in Education. https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2

`q2 · i?` · `design · r2`

Accurate-match analysis of the same derived-variable task. "Google Gemini 1.5 Pro again performed best (70.24% agreement, k = 0.29)". Precision was high (0.91–0.93) while recall was lower (0.64–0.75).

> "For the accurate match analysis, we found that Google Gemini 1.5 Pro again performed best (70.24% agreement, k = 0.29), followed by Google Gemini 1.5 Flash (67.74% agreement, k = 0.26) and Mistral Large 2 (61.90% agreement, k = 0.19)."

## Discussion


## Related Claims
- [LLM data extraction accuracy varies by data type, with high precision but lower recall across tasks](llm-extraction-high-precision-lower-recall.md) — related
- [LLMs show moderate agreement with human coders when extracting explicitly stated data from education studies](llms-moderate-agreement-explicit-data-extraction-education.md) — related
- [In a pilot study, leading LLMs showed promising but imperfect agreement with human coders extracting data from K-12 virtual-character studies](pilot-study-llm-agreement-virtual-character-studies.md) — related
