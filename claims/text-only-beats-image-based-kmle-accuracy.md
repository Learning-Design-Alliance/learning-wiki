---
type: claim
title: GPT-4o and Claude 3.5 Sonnet are significantly more accurate on text-only than image-based KMLE questions, while Gemini 1.5 Pro performs comparably across formats
description: GPT-4o and Claude 3.5 Sonnet are significantly more accurate on text-only than image-based KMLE questions, while Gemini 1.5 Pro performs comparably across formats
id: text-only-beats-image-based-kmle-accuracy
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
    kind: associational
    rigour: 2
  - id: kim-hyun-jin-2025-2
    resource: "https://doi.org/10.1038/s41598-025-20066-x"
    title: "Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute. (2025). Performance evaluation of large language models on Korean medical licensing examination: a three-year comparative analysis. Scientific Reports. https://doi.org/10.1038/s41598-025-20066-x"
    author: Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# GPT-4o and Claude 3.5 Sonnet are significantly more accurate on text-only than image-based KMLE questions, while Gemini 1.5 Pro performs comparably across formats

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4o and Claude 3.5 Sonnet each achieved significantly higher accuracy on text-only than image-based questions. [→ Kim Hyun Jin 2025](#kim-hyun-jin-2025)
`q2 i?` Gemini 1.5 Pro showed comparable accuracy across the two question types. [→ Kim Hyun Jin 2025 (2)](#kim-hyun-jin-2025-2)

## Evidence

### Kim Hyun Jin 2025

Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute. (2025). Performance evaluation of large language models on Korean medical licensing examination: a three-year comparative analysis. Scientific Reports. https://doi.org/10.1038/s41598-025-20066-x

`q2 · i?` · `associational · r2`

Chi-square comparison of accuracy by question type in the KMLE evaluation. GPT-4o scored 86.1% text-only vs 80.6% image-based; Claude 3.5 Sonnet 83.9% vs 75.6%; both "P < 0.05". No effect size printed.

> "both GPT-4o and Claude 3.5 Sonnet achieved significantly higher accuracy on text-only questions compared to image-based questions (86.1% vs. 80.6%, P < 0.05 and 83.9% vs. 75.6%, P < 0.05, respectively)"

### Kim Hyun Jin 2025 (2)

Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute. (2025). Performance evaluation of large language models on Korean medical licensing examination: a three-year comparative analysis. Scientific Reports. https://doi.org/10.1038/s41598-025-20066-x

`q2 · i?` · `associational · r2`

Within-model comparison for Gemini 1.5 Pro in the same KMLE question-type analysis: 76.7% text-only vs 76.6% image-based, "P > 0.05". The authors attribute this pattern partly to its content filter blocking 21 sensitive-image questions and its PIL-based image handling.

> "while Gemini 1.5 Pro showed comparable performance across both question types (76.7% vs. 76.6%, P > 0.05)"

## Discussion


## Related Claims
- [GPT-4o achieves the highest overall accuracy on KMLE questions (83.2%), significantly outperforming Claude 3.5 Sonnet and Gemini 1.5 Pro across 2022–2024](gpt4o-highest-kmle-accuracy-83-2.md) — related
- [LLM performance on KMLE varies by medical specialty, with relatively weak accuracy in medical law for all three models](kmle-specialty-variation-weak-medical-law.md) — related
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
