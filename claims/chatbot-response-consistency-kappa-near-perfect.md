---
type: claim
title: Chatbot responses show near-perfect repeatability across no-feedback attempts (κ 0.967-1.000)
description: Chatbot responses show near-perfect repeatability across no-feedback attempts (κ 0.967-1.000)
id: chatbot-response-consistency-kappa-near-perfect
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-06
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: sabaner-mehmet-cem-2025
    resource: "https://doi.org/10.4274/tjo.galenos.2025.27895"
    title: "Sabaner Mehmet Cem, Yozgat Zübeyir. (2025). Performance of ChatGPT-4 Omni and Gemini 1.5 Pro on Ophthalmology-Related Questions in the Turkish Medical Specialty Exam. Turkish Journal of Ophthalmology. https://doi.org/10.4274/tjo.galenos.2025.27895"
    author: Sabaner Mehmet Cem, Yozgat Zübeyir
    q: 3
    i: "?"
    kind: causal
    rigour: 1
---

# Chatbot responses show near-perfect repeatability across no-feedback attempts (κ 0.967-1.000)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r1` · `q3`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q3 i?` Cohen's kappa between the first and second no-feedback attempts was 0.974 for ChatGPT-4o and 0.967 for Gemini 1.5 Pro in Turkish, and 1.000 for both models in English. [→ Sabaner Mehmet Cem 2025](#sabaner-mehmet-cem-2025)

## Evidence

### Sabaner Mehmet Cem 2025

Sabaner Mehmet Cem, Yozgat Zübeyir. (2025). Performance of ChatGPT-4 Omni and Gemini 1.5 Pro on Ophthalmology-Related Questions in the Turkish Medical Specialty Exam. Turkish Journal of Ophthalmology. https://doi.org/10.4274/tjo.galenos.2025.27895

`q3 · i?` · `causal · r1`

Consistency analysis of the MCQ evaluation across the first and second attempts, "during which no feedback was provided to the chatbots." The article reports κ with 95% CIs as printed; no standardized effect size accompanies this finding.

> "In Turkish, κ values were 0.974 (95% CI, 0.967-0.980) for ChatGPT-4o and 0.967 (95% CI, 0.957-0.975) for Gemini 1.5 Pro. In English, both models achieved a κ value of 1.000, indicating perfect agreement."

## Discussion


## Related Claims
- [All three LLMs show near-perfect answer reproducibility under repeated API testing at zero temperature, highest for Claude 3.5 Sonnet (99.9%)](llm-kmle-reproducibility-near-perfect.md) — related
- [Gemini 1.5 Pro shows the highest response consistency across 30 repeated exam attempts, significantly exceeding GPT-4o but statistically comparable to Claude](gemini-highest-response-consistency-repeated-attempts.md) — related
- [ChatGPT-4o achieves higher final-attempt accuracy than Gemini 1.5 Pro on ophthalmology MCQs, significantly in English but not in Turkish](chatgpt4o-outperforms-gemini-ophthalmology-mcq-final-attempt.md) — related
- [Chatbot answers were largely stable across 5 successive attempts, with all chatbots answering 104 (52%) of the 200 questions correctly in every attempt](chatbot-answer-stability-across-five-attempts.md) — a narrower finding that bears on this claim
