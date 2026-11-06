---
type: claim
title: ChatGPT-o1pro shows higher response consistency on Turkish questions (κ = 0.836) than English questions (κ = 0.689), while AtlasGPT and ChatGPT-4 remain balanced across languages
description: ChatGPT-o1pro shows higher response consistency on Turkish questions (κ = 0.836) than English questions (κ = 0.689), while AtlasGPT and ChatGPT-4 remain balanced across languages
id: language-specific-consistency-turkish-english
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: çamlar-mahmut-2025
    resource: "https://doi.org/10.1007/s00701-025-06628-y"
    title: "Çamlar Mahmut, Sevgi Umut Tan, Erol Gökberk, Karakaş Furkan, Doğruel Yücel, Güngör Abuzer. (2025). Comparative performance of neurosurgery-specific, peer-reviewed versus general AI chatbots in bilingual board examinations: evaluating accuracy, consistency, and error minimization strategies. Acta Neurochirurgica 167(1):241. https://doi.org/10.1007/s00701-025-06628-y"
    author: Çamlar Mahmut, Sevgi Umut Tan, Erol Gökberk, Karakaş Furkan, Doğruel Yücel, Güngör Abuzer
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ChatGPT-o1pro shows higher response consistency on Turkish questions (κ = 0.836) than English questions (κ = 0.689), while AtlasGPT and ChatGPT-4 remain balanced across languages

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` In non-image questions, ChatGPT-o1pro showed higher consistency in Turkish (κ = 0.836) than English (κ = 0.689); AtlasGPT was balanced (Turkish κ = 0.722, English κ = 0.733). [→ Çamlar Mahmut 2025](#camlar-mahmut-2025)

## Evidence

### Çamlar Mahmut 2025

Çamlar Mahmut, Sevgi Umut Tan, Erol Gökberk, Karakaş Furkan, Doğruel Yücel, Güngör Abuzer. (2025). Comparative performance of neurosurgery-specific, peer-reviewed versus general AI chatbots in bilingual board examinations: evaluating accuracy, consistency, and error minimization strategies. Acta Neurochirurgica 167(1):241. https://doi.org/10.1007/s00701-025-06628-y

`q2 · i?` · `design · r2`

Language-specific kappa analysis of non-image questions. The article cautions these findings cannot be directly interpreted as language-dependent performance differences because different question sets were used for each language rather than translated identical questions.

> "ChatGPT-o1pro showed higher consistency in Turkish (κ = 0.836) compared with English (κ = 0.689). Atlas maintained more balanced performance across languages (Turkish κ = 0.722, English κ = 0.733)."

## Discussion


## Related Claims
- [Inter-model consistency declines progressively with question complexity, from substantial agreement on SBA-R (κ > 0.72) to only fair agreement on image questions (ChatGPT-o1pro κ = 0.40)](kappa-consistency-declines-question-complexity.md) — related
- [No statistically significant performance gap existed between Turkish and English administration of the same radiology questions to ChatGPT-5 and Gemini 2.5 Pro](no-language-gap-turkish-english-llm-radiology-accuracy.md) — related
- [Successive versions of ChatGPT and Gemini showed no statistically significant difference in overall accuracy on the radiology questions, with only moderate response consistency across versions](no-accuracy-difference-across-llm-versions-radiology.md) — related
- [No statistically significant interlingual variation for either chatbot answering the same questions in Turkish versus English](no-interlingual-variation-chatbot-ophthalmology-mcq.md) — related
