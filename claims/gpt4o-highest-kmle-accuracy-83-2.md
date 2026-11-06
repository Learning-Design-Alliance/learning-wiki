---
type: claim
title: "GPT-4o achieves the highest overall accuracy on KMLE questions (83.2%), significantly outperforming Claude 3.5 Sonnet and Gemini 1.5 Pro across 2022–2024"
description: "GPT-4o achieves the highest overall accuracy on KMLE questions (83.2%), significantly outperforming Claude 3.5 Sonnet and Gemini 1.5 Pro across 2022–2024"
id: gpt4o-highest-kmle-accuracy-83-2
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: kim-hyun-jin-2025
    resource: "https://doi.org/10.1038/s41598-025-20066-x"
    title: "Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute. (2025). Performance evaluation of large language models on Korean medical licensing examination: a three-year comparative analysis. Scientific Reports. https://doi.org/10.1038/s41598-025-20066-x"
    author: Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# GPT-4o achieves the highest overall accuracy on KMLE questions (83.2%), significantly outperforming Claude 3.5 Sonnet and Gemini 1.5 Pro across 2022–2024

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across all three years combined, GPT-4o outperformed Claude 3.5 Sonnet and Gemini 1.5 Pro on KMLE accuracy with statistically significant differences, and all models exceeded the 60% passing threshold. [→ Kim Hyun Jin 2025](#kim-hyun-jin-2025)

## Evidence

### Kim Hyun Jin 2025

Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute. (2025). Performance evaluation of large language models on Korean medical licensing examination: a three-year comparative analysis. Scientific Reports. https://doi.org/10.1038/s41598-025-20066-x

`q2 · i?` · `design · r2`

Automated API-based evaluation of three LLMs on 942 KMLE questions (2022–2024). Overall accuracies were GPT-4o 83.2% (784/942), Claude 3.5 Sonnet 79.5%, Gemini 1.5 Pro 76.6%; the article reports "statistically significant accuracy rates (P = 0.003 and P < 0.001, respectively)". No effect size printed.

> "In the overall analysis combining all three years, GPT-4o outperformed both Claude 3.5 Sonnet and Gemini 1.5 Pro, achieving statistically significant accuracy rates (P = 0.003 and P < 0.001, respectively) (Fig. 1)."

## Discussion


## Related Claims
- [GPT-4o and Claude 3.5 Sonnet are significantly more accurate on text-only than image-based KMLE questions, while Gemini 1.5 Pro performs comparably across formats](text-only-beats-image-based-kmle-accuracy.md) — related
- [Inter-model agreement on KMLE questions is highest between GPT-4o and Claude 3.5 Sonnet, and incorrect consensus declines from 2022 to 2024](inter-model-agreement-gpt4o-claude-highest.md) — related
- [ChatGPT-5, Gemini 3.0 Pro, and Claude Sonnet 4.5 achieved significantly higher overall scores than mean ophthalmology trainee performance, while ChatGPT-4o did not](three-llms-outperform-mean-trainee-overall.md) — related
- [ChatGPT-5 achieved the highest overall accuracy on ophthalmology board-style questions (92.59%), with no statistically significant differences among the four LLMs](chatgpt-5-highest-overall-accuracy-ophthalmology-board-questions.md) — related
- [All three LLMs show near-perfect answer reproducibility under repeated API testing at zero temperature, highest for Claude 3.5 Sonnet (99.9%)](llm-kmle-reproducibility-near-perfect.md) — related
- [LLM performance on KMLE varies by medical specialty, with relatively weak accuracy in medical law for all three models](kmle-specialty-variation-weak-medical-law.md) — related
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [On interpretation-type questions, ChatGPT-5, Gemini 3.0 Pro, and Claude Sonnet 4.5 achieved perfect scores (100%), significantly exceeding trainee performance, while ChatGPT-4o performed comparably to fellows](llms-interpretation-type-questions-perfect-scores.md) — related
