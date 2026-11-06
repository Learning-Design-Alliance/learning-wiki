---
type: claim
title: LLM performance on KMLE varies by medical specialty, with relatively weak accuracy in medical law for all three models
description: LLM performance on KMLE varies by medical specialty, with relatively weak accuracy in medical law for all three models
id: kmle-specialty-variation-weak-medical-law
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
  - id: kim-hyun-jin-2025-2
    resource: "https://doi.org/10.1038/s41598-025-20066-x"
    title: "Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute. (2025). Performance evaluation of large language models on Korean medical licensing examination: a three-year comparative analysis. Scientific Reports. https://doi.org/10.1038/s41598-025-20066-x"
    author: Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# LLM performance on KMLE varies by medical specialty, with relatively weak accuracy in medical law for all three models

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` All three models showed relatively lower performance in medical law (GPT-4o 70.0%, Claude 3.5 Sonnet 76.7%, Gemini 1.5 Pro 65.0%) than in other specialties. [→ Kim Hyun Jin 2025](#kim-hyun-jin-2025)
`q2 i?` GPT-4o significantly outperformed the other two models in internal medicine. [→ Kim Hyun Jin 2025 (2)](#kim-hyun-jin-2025-2)

## Evidence

### Kim Hyun Jin 2025

Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute. (2025). Performance evaluation of large language models on Korean medical licensing examination: a three-year comparative analysis. Scientific Reports. https://doi.org/10.1038/s41598-025-20066-x

`q2 · i?` · `design · r2`

Specialty-level accuracy analysis of the KMLE evaluation, with questions classified into seven specialties by two board-certified specialists (Cohen's kappa 0.938). Medical law accuracies are as printed; the authors attribute the weakness to limited Korean medical-law data in training corpora.

> "All models showed relatively lower performance in medical law (GPT-4o: 70.0%, Claude 3.5 Sonnet: 76.7%, Gemini 1.5 Pro: 65.0%) than in other specialties."

### Kim Hyun Jin 2025 (2)

Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute. (2025). Performance evaluation of large language models on Korean medical licensing examination: a three-year comparative analysis. Scientific Reports. https://doi.org/10.1038/s41598-025-20066-x

`q2 · i?` · `design · r2`

Cross-model specialty comparison in the KMLE evaluation. In internal medicine GPT-4o reached 86.1% versus 79.4% and 76.4%, with the printed P values shown; the authors link this to extensive medical literature in the field. No effect size printed.

> "GPT-4o demonstrated particularly strong performance in internal medicine (86.1%), significantly outperforming both Claude 3.5 Sonnet (79.4%, P = 0.001) and Gemini 1.5 Pro (76.4%, P < 0.001)."

## Discussion


## Related Claims
- [Claude, Copilot, and Gemini showed model-specific topic strengths and weaknesses and lower cross-attempt reliability than GPT-4o](claude-copilot-gemini-topic-strengths-reliability.md) — related
- [GPT-4o achieves the highest overall accuracy on KMLE questions (83.2%), significantly outperforming Claude 3.5 Sonnet and Gemini 1.5 Pro across 2022–2024](gpt4o-highest-kmle-accuracy-83-2.md) — related
- [GPT-4o and Claude 3.5 Sonnet are significantly more accurate on text-only than image-based KMLE questions, while Gemini 1.5 Pro performs comparably across formats](text-only-beats-image-based-kmle-accuracy.md) — related
- [Model strengths differ by question type: Gemini 1.5 Pro leads on A1 recall and image-based questions, Claude 3.5 Sonnet on A2 application, and Gemini and GPT-4o on case analysis](llm-strengths-vary-by-srtp-question-type.md) — related
- [All three LLMs exceed the 400/650-point passing threshold on a Chinese anesthesiology SRTP mock exam, with Claude 3.5 Sonnet achieving the highest mean score](llms-pass-chinese-anesthesiology-srtp-exam-claude-highest.md) — related
- [GPT-4o accuracy on EUNACOM varies substantially by medical specialty, highest in psychiatry, neurology, and surgery and lowest in neonatology, otolaryngology, and urology/nephrology](eunacom-accuracy-varies-by-specialty.md) — related
