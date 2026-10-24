---
type: claim
title: The OCR-based text input uses far fewer tokens than image-based multimodal input for the same slide, making it more cost-effective
description: The OCR-based text input uses far fewer tokens than image-based multimodal input for the same slide, making it more cost-effective
id: ocr-input-lower-token-cost-than-image-input
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: patel-2025
    resource: "https://doi.org/10.48550/arxiv.2509.02998"
    title: "Patel, K., Lin, Y.-Z., Raul, G., Shih, B. P.-J., Redondo, M. W., Latibari, B. S., Pacheco, J., Salehi, S., & Satam, P. (2025). Integrating Generative AI into Cybersecurity Education: A Study of OCR and Multimodal LLM-assisted Instruction. arXiv. https://arxiv.org/abs/2509.02998 [doi:10.48550/arxiv.2509.02998](https://doi.org/10.48550/arxiv.2509.02998)"
    author: "Patel, K., Lin, Y.-Z., Raul, G., Shih, B. P.-J., Redondo, M. W., Latibari, B. S., Pacheco, J., Salehi, S., & Satam, P."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# The OCR-based text input uses far fewer tokens than image-based multimodal input for the same slide, making it more cost-effective

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` For the example slide in Figure 3(a), OCR-based text input consumed 392 tokens for 1124 characters, whereas image-based input of a 1500× 844 px image consumed 1105 tokens. [→ Patel 2025](#patel-2025)

## Evidence

### Patel 2025

Patel, K., Lin, Y.-Z., Raul, G., Shih, B. P.-J., Redondo, M. W., Latibari, B. S., Pacheco, J., Salehi, S., & Satam, P. (2025). Integrating Generative AI into Cybersecurity Education: A Study of OCR and Multimodal LLM-assisted Instruction. arXiv. https://arxiv.org/abs/2509.02998 [doi:10.48550/arxiv.2509.02998](https://doi.org/10.48550/arxiv.2509.02998)

`q2 · i?` · `design · r2`

Token-cost analysis of one example slide (Figure 3(a)) comparing OCR text input (392 tokens for 1124 characters) against image input (1105 tokens for a 1500× 844 px image). The article concludes the OCR method "is more cost-effective"; no aggregate cost statistics are printed.

> "In terms of cost, the OCR-based text input method in this example uses only 392 tokens for 1124 characters, but if image-based input is used to multimodal LLM, an image file is 1500× 844 px, and the number of tokens used is 1105 tokens"

## Discussion


## Related Claims
- [The text-based LLM compensates for noisy OCR input, generating contextually accurate explanations even when OCR produces jumbled text from UI screenshots](llm-compensates-for-noisy-ocr-input.md) — related
- [Multimodal LLMs outperform the OCR-based pipeline on visually dense slides, while the OCR pipeline produces comparable instruction on text-centric slides](multimodal-vs-ocr-pipeline-slide-type-comparison.md) — related
- [Students rate LLM-generated simplified instructions positively, averaging 7.83 on a 1-10 usefulness scale across 42 ratings in a live cybersecurity course](student-feedback-7-83-ocr-llm-instructions.md) — related
- [Multimodal input consistently improves accuracy but not F1, model size correlates moderately with performance, and reasoning models show mixed results](multimodality-size-reasoning-mixed-effects.md) — reports the opposite
- [Purpose-trained single-pass generation completes a slide in a median of 17 seconds and an interactive page in 59 seconds over 220k production requests, and delivers artifacts at 15–22× lower per-artifact API cost than flagship models](cogevol-single-pass-latency-and-cost.md) — related
