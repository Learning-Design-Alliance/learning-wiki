---
type: claim
title: Accuracy is significantly lower on image-based than non-image-based questions for three of four LLMs
description: Accuracy is significantly lower on image-based than non-image-based questions for three of four LLMs
id: image-based-questions-lower-accuracy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: liu-mingxin-2026
    resource: "https://doi.org/10.1186/s12911-026-03370-y"
    title: "Liu Mingxin, Okuhara Tsuyoshi, Dai Zhehao, Zhao Minghong, Yin Wenqiang, Okada Hiroko, Furukawa Emi, Kiuchi Takahiro. (2026). Textbook-level medical knowledge in large language models: comparative evaluation using Japanese National Medical Examination. BMC Medical Informatics and Decision Making. https://doi.org/10.1186/s12911-026-03370-y"
    author: Liu Mingxin, Okuhara Tsuyoshi, Dai Zhehao, Zhao Minghong, Yin Wenqiang, Okada Hiroko, Furukawa Emi, Kiuchi Takahiro
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Accuracy is significantly lower on image-based than non-image-based questions for three of four LLMs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-5, Grok-4, and Claude Opus 4.1 showed significantly lower accuracy on image-based questions, while Gemini 2.5 Pro did not differ significantly between question types. [→ Liu Mingxin 2026](#liu-mingxin-2026)

## Evidence

### Liu Mingxin 2026

Liu Mingxin, Okuhara Tsuyoshi, Dai Zhehao, Zhao Minghong, Yin Wenqiang, Okada Hiroko, Furukawa Emi, Kiuchi Takahiro. (2026). Textbook-level medical knowledge in large language models: comparative evaluation using Japanese National Medical Examination. BMC Medical Informatics and Decision Making. https://doi.org/10.1186/s12911-026-03370-y

`q2 · i?` · `design · r2`

Fisher's exact tests compared image-based versus text-only accuracy per model; the article reports "GPT-5, p = 0.016; Grok-4, p < 0.001; Claude Opus 4.1, p = 0.03", with accuracy gaps of 3.7%, 6.0%, 4.7%, and 1.5% respectively.

> "Three of the LLMs showed significant differences (GPT-5, p = 0.016; Grok-4, p < 0.001; Claude Opus 4.1, p = 0.03)"

## Discussion


## Related Claims
- [Accuracy on difficult questions is significantly lower than on easy questions for all four LLMs](difficulty-effect-attenuated-llms.md) — related
- [Four reasoning-enhanced LLMs exceed 95% accuracy on the JNME, with Gemini 2.5 Pro highest at 97.2% and no significant pairwise differences](four-llms-exceed-95-jnme-2026.md) — related
- [All four LLMs show higher accuracy on general than clinical questions, significant only for Grok-4](general-vs-clinical-accuracy-gap.md) — related
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [All seven LLMs showed markedly lower accuracy on image-based than text-based DUS questions, with significant text-image gaps for five models but not Gemini or Claude](llms-lower-accuracy-image-based-dus-questions.md) — related
