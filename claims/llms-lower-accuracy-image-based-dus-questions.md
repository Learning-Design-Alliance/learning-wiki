---
type: claim
title: All seven LLMs showed markedly lower accuracy on image-based than text-based DUS questions, with significant text-image gaps for five models but not Gemini or Claude
description: All seven LLMs showed markedly lower accuracy on image-based than text-based DUS questions, with significant text-image gaps for five models but not Gemini or Claude
id: llms-lower-accuracy-image-based-dus-questions
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: geduk-gediz-2026
    resource: "https://doi.org/10.1038/s41598-026-37800-8"
    title: "Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem. (2026). A comparative analysis of the performance of large Language models in the dentistry specialty examination. Scientific Reports. https://doi.org/10.1038/s41598-026-37800-8"
    author: Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: geduk-gediz-2026-2
    resource: "https://doi.org/10.1038/s41598-026-37800-8"
    title: "Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem. (2026). A comparative analysis of the performance of large Language models in the dentistry specialty examination. Scientific Reports. https://doi.org/10.1038/s41598-026-37800-8"
    author: Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# All seven LLMs showed markedly lower accuracy on image-based than text-based DUS questions, with significant text-image gaps for five models but not Gemini or Claude

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r1` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All models demonstrated markedly lower accuracy on image-based items; the best image-based performers (ChatGPT 4.0, Gemini, Copilot) reached 63.6% while DeepSeek reached 36.4%. [→ Geduk Gediz 2026](#geduk-gediz-2026)
`q2 i?` The image-versus-text difference was statistically significant for ChatGPT 4.0, ChatGPT 4.5, DeepSeek, Copilot, and Grok (p < 0.05), but not for Gemini and Claude (p > 0.05). [→ Geduk Gediz 2026 (2)](#geduk-gediz-2026-2)

## Evidence

### Geduk Gediz 2026

Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem. (2026). A comparative analysis of the performance of large Language models in the dentistry specialty examination. Scientific Reports. https://doi.org/10.1038/s41598-026-37800-8

`q2 · i?` · `design · r2`

Comparison of model performance on the 11 image-based versus 197 text-based DUS questions (Table 5). ChatGPT 4.0, Gemini, and Copilot each achieved 63.6% on image-based items; DeepSeek achieved 36.4%.

> "The highest accuracy for image-based questions was observed in ChatGPT 4.0, gemini, and Copilot, each achieving 63.6%, whereas deepseek showed the lowest performance with an accuracy rate of 36.4%."

### Geduk Gediz 2026 (2)

Geduk Gediz, Hasırcı Utku Cem, Kusay Didem Dumanlı, Aras Rabia Çayır, Çapar İsmail, Altın Edanur, Şeker Çiğdem. (2026). A comparative analysis of the performance of large Language models in the dentistry specialty examination. Scientific Reports. https://doi.org/10.1038/s41598-026-37800-8

`q2 · i?` · `associational · r1`

Statistical comparison of image-based versus text-based accuracy per model (Table 5). Five models performed significantly better on text-based questions; Gemini and Claude showed no statistically significant difference between the two question types.

> "the difference between image-based and text-based accuracy rates was statistically significant for ChatGPT 4.0, ChatGPT 4.5, deepseek, Copilot, and Grok (p < 0.05), indicating that these models performed significantly better on text-based questions. In contrast, gemini and Claude did not demonstrate a statistically significant difference between the two question types (p > 0.05)."

## Discussion


## Related Claims
- [ChatGPT 4.0 achieved the highest accuracy (91.3%) on DUS oral and maxillofacial radiology questions and significantly outperformed all other evaluated LLMs](chatgpt-4-highest-accuracy-dus-radiology.md) — related
- [All four LLMs show higher accuracy on general than clinical questions, significant only for Grok-4](general-vs-clinical-accuracy-gap.md) — related
- [Accuracy is significantly lower on image-based than non-image-based questions for three of four LLMs](image-based-questions-lower-accuracy.md) — related
- [LLM accuracy varied by subject area, with oral pathology (94%) and salivary gland diseases (91.8%) highest and radiological anatomy (67.3%) lowest; only Copilot showed a statistically significant across-subject difference](subject-area-accuracy-variation-dus-llms.md) — related
