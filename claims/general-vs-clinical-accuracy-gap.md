---
type: claim
title: All four LLMs show higher accuracy on general than clinical questions, significant only for Grok-4
description: All four LLMs show higher accuracy on general than clinical questions, significant only for Grok-4
id: general-vs-clinical-accuracy-gap
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

# All four LLMs show higher accuracy on general than clinical questions, significant only for Grok-4

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All four LLMs achieved higher accuracy on general questions than clinical questions, but the difference reached statistical significance only for Grok-4 (p < 0.001). [→ Liu Mingxin 2026](#liu-mingxin-2026)

## Evidence

### Liu Mingxin 2026

Liu Mingxin, Okuhara Tsuyoshi, Dai Zhehao, Zhao Minghong, Yin Wenqiang, Okada Hiroko, Furukawa Emi, Kiuchi Takahiro. (2026). Textbook-level medical knowledge in large language models: comparative evaluation using Japanese National Medical Examination. BMC Medical Informatics and Decision Making. https://doi.org/10.1186/s12911-026-03370-y

`q2 · i?` · `design · r2`

Comparison of general (n = 293) versus clinical (n = 497) question accuracy across the 793-question dataset; the article reports "a statistically significant difference was observed only for Grok-4 (p < 0.001)", with general-question accuracies of 97.6–99.0%.

> "All four LLMs demonstrated higher accuracy for general questions than for clinical questions; however, a statistically significant difference was observed only for Grok-4 (p < 0.001)."

## Discussion


## Related Claims
- [Gemini 2.5 Pro achieved the highest accuracy (92.44%) on pediatric dentistry DUS questions, significantly outperforming most other LLMs](gemini-2-5-pro-highest-accuracy-pediatric-dus.md) — related
- [Temporal reliability over a 1-week interval varied across LLMs: Claude 4.5 Sonnet showed very good consistency (kappa = 0.872) while Grok-4 and ChatGPT-5 showed moderate agreement](claude-sonnet-superior-temporal-reliability-radiology-questions.md) — related
- [Accuracy is significantly lower on image-based than non-image-based questions for three of four LLMs](image-based-questions-lower-accuracy.md) — related
- [All seven LLMs showed markedly lower accuracy on image-based than text-based DUS questions, with significant text-image gaps for five models but not Gemini or Claude](llms-lower-accuracy-image-based-dus-questions.md) — related
- [Proprietary LLM architectures showed consistently higher mean accuracy than open-source architectures on the EBHS examination, with GPT-5 Pro the leading model at 85% accuracy.](proprietary-llms-outperform-open-source-ebhs.md) — related
- [LLM accuracy on multilingual medical multiple-choice questions varies substantially by model, with Claude-Sonnet-3.7 highest (87%) and open models lowest (64%-73%)](llm-accuracy-varies-by-model-medical-mcq.md) — related
- [Successive versions of ChatGPT and Gemini showed no statistically significant difference in overall accuracy on the radiology questions, with only moderate response consistency across versions](no-accuracy-difference-across-llm-versions-radiology.md) — related
- [Claude Sonnet 4.5 significantly outperformed Grok 4 on OLA questions, the only significant pairwise difference on that examination](claude-outperformed-grok4-ola-pairwise.md) — related
- [Accuracy on difficult questions is significantly lower than on easy questions for all four LLMs](difficulty-effect-attenuated-llms.md) — related
