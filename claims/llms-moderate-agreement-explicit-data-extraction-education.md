---
type: claim
title: LLMs show moderate agreement with human coders when extracting explicitly stated data from education studies
description: LLMs show moderate agreement with human coders when extracting explicitly stated data from education studies
id: llms-moderate-agreement-explicit-data-extraction-education
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
  - id: schroeder-2025-2
    resource: "https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2"
    title: "Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K. (2025). AI-Assisted Data Extraction for Systematic Reviews in Education. https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2"
    author: "Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K."
    q: 2
    i: "?"
    kind: design
    rigour: 3
---

# LLMs show moderate agreement with human coders when extracting explicitly stated data from education studies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r3` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the main study, Gemini 1.5 Pro achieved 83.23% exact-match agreement (k = 0.40) with a human coder on nine explicitly stated variables, and Gemini 1.5 Flash achieved 81.55% (k = 0.39), while Mistral Large 2 reached 71.43% (k = 0.30). [→ Schroeder 2025](#schroeder-2025)
`q2 i?` Under the more lenient accurate-match criterion, agreement rose slightly (Gemini 1.5 Pro 85.02%, k = 0.41), but kappa still did not reach levels typically acceptable in research synthesis contexts. [→ Schroeder 2025 (2)](#schroeder-2025-2)

## Evidence

### Schroeder 2025

Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K. (2025). AI-Assisted Data Extraction for Systematic Reviews in Education. https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2

`q2 · i?` · `design · r3`

Main study comparing three LLMs against human coding of nine explicit variables across 112 studies from a published scoping review. The article reports "Google Gemini 1.5 Pro was the most accurate LLM (83.23% agreement, k = 0.40)". Precision was high (0.89–0.95) but recall ranged from 0.67 to 0.88.

> "Our analysis of exact matches for explicitly stated data showed the following: Google Gemini 1.5 Pro was the most accurate LLM (83.23% agreement, k = 0.40), followed by Gemini 1.5 Flash (81.55% agreement, k = 0.39) and Mistral Large 2 (71.43% agreement, k = 0.30)."

### Schroeder 2025 (2)

Schroeder, N. L., Jaldi, C. D., Zhang, S., & Yamoah, K. (2025). AI-Assisted Data Extraction for Systematic Reviews in Education. https://osf.io/nraxf/?view_only=879654690be249cc9237525ed7f86ec2

`q2 · i?` · `design · r3`

Accurate-match analysis of the same main-study data, allowing semantically equivalent answers. "Google Gemini 1.5 Pro had the highest accuracy (85.02% agreement, k = 0.41)". The authors note kappa "did not reach a level typically acceptable in research synthesis contexts".

> "The accurate match metrics showed that Google Gemini 1.5 Pro had the highest accuracy (85.02% agreement, k = 0.41), followed by Google Gemini 1.5 Flash (82.64% agreement, k = 0.39) and Mistral Large 2 (74.01% agreement, k = 0.32)."

## Discussion


## Related Claims
- [LLM data extraction accuracy varies by data type, with high precision but lower recall across tasks](llm-extraction-high-precision-lower-recall.md) — related
- [LLMs are substantially less accurate at extracting and categorizing derived data based on predefined categories than at extracting explicitly stated data](llms-less-accurate-derived-categorical-data-extraction.md) — related
- [State-of-the-art LLMs extract effect sizes, study counts, and participant counts from educational meta-analyses with excellent agreement with adjudicated gold and silver standards](llm-data-extraction-icc-gold-standard.md) — related
- [In a pilot study, leading LLMs showed promising but imperfect agreement with human coders extracting data from K-12 virtual-character studies](pilot-study-llm-agreement-virtual-character-studies.md) — related
- [In blind verification, model selection matters more than source type: Bradley-Terry ranking interleaves human coders and LLMs, with per-model win rates spanning significant human advantage to numerical LLM advantage](bradley-terry-model-selection-matters-more-than-source-type.md) — related
- [LLMs are not ready to be used as primary data extraction tools without explicit human validation in education research synthesis](llms-not-ready-primary-data-extraction-without-human-validation.md) — related
