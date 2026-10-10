---
type: claim
title: Multimodal LLMs outperform the OCR-based pipeline on visually dense slides, while the OCR pipeline produces comparable instruction on text-centric slides
description: Multimodal LLMs outperform the OCR-based pipeline on visually dense slides, while the OCR pipeline produces comparable instruction on text-centric slides
id: multimodal-vs-ocr-pipeline-slide-type-comparison
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: mixed
sources:
  - id: patel-2025
    resource: "https://arxiv.org/abs/2509.02998"
    title: "Patel, K., Lin, Y.-Z., Raul, G., Shih, B. P.-J., Redondo, M. W., Latibari, B. S., Pacheco, J., Salehi, S., & Satam, P. (2025). Integrating Generative AI into Cybersecurity Education: A Study of OCR and Multimodal LLM-assisted Instruction. arXiv. https://arxiv.org/abs/2509.02998"
    author: "Patel, K., Lin, Y.-Z., Raul, G., Shih, B. P.-J., Redondo, M. W., Latibari, B. S., Pacheco, J., Salehi, S., & Satam, P."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Multimodal LLMs outperform the OCR-based pipeline on visually dense slides, while the OCR pipeline produces comparable instruction on text-centric slides

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`

## Subclaims
`q2 i?` The OCR-based pipeline consistently produced accurate and helpful instruction across a wide range of slide types, particularly text-dominant or structurally consistent slides. [→ Patel 2025](#patel-2025)

## Evidence

### Patel 2025

Patel, K., Lin, Y.-Z., Raul, G., Shih, B. P.-J., Redondo, M. W., Latibari, B. S., Pacheco, J., Salehi, S., & Satam, P. (2025). Integrating Generative AI into Cybersecurity Education: A Study of OCR and Multimodal LLM-assisted Instruction. arXiv. https://arxiv.org/abs/2509.02998

`q2 · i?` · `design · r2`

Summary of the qualitative slide-type comparison reported in the results section: multimodal LLMs hold advantages on visually rich slides, while the OCR pipeline "is not far behind" across slide types. No quantitative quality metric is printed.

> "Overall, the results indicate that while multimodal LLMs provide advantages for slides rich in visual content, the OCR-based pipeline is not far behind."

## Discussion


## Related Claims
- [The text-based LLM compensates for noisy OCR input, generating contextually accurate explanations even when OCR produces jumbled text from UI screenshots](llm-compensates-for-noisy-ocr-input.md) — related
- [The OCR-based text input uses far fewer tokens than image-based multimodal input for the same slide, making it more cost-effective](ocr-input-lower-token-cost-than-image-input.md) — related
- [Students rate LLM-generated simplified instructions positively, averaging 7.83 on a 1-10 usefulness scale across 42 ratings in a live cybersecurity course](student-feedback-7-83-ocr-llm-instructions.md) — related
