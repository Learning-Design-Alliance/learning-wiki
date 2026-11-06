---
type: claim
title: "All three LLMs show near-perfect answer reproducibility under repeated API testing at zero temperature, highest for Claude 3.5 Sonnet (99.9%)"
description: "All three LLMs show near-perfect answer reproducibility under repeated API testing at zero temperature, highest for Claude 3.5 Sonnet (99.9%)"
id: llm-kmle-reproducibility-near-perfect
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

# All three LLMs show near-perfect answer reproducibility under repeated API testing at zero temperature, highest for Claude 3.5 Sonnet (99.9%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Reproducibility across three repeated responses on 910 A-type questions was 99.9% for Claude 3.5 Sonnet, 99.5% for Gemini 1.5 Pro, and 97.7% for GPT-4o, with Fleiss' kappa values indicating almost perfect agreement. [→ Kim Hyun Jin 2025](#kim-hyun-jin-2025)

## Evidence

### Kim Hyun Jin 2025

Kim Hyun Jin, Jung Kiwook, Shin Sunghwan, Lee Wookeun, Lee Jun Hyung, Park Hee Sue, Choi Qute. (2025). Performance evaluation of large language models on Korean medical licensing examination: a three-year comparative analysis. Scientific Reports. https://doi.org/10.1038/s41598-025-20066-x

`q2 · i?` · `design · r2`

Reproducibility analysis in which each model answered 910 A-type KMLE questions three times under a zero-temperature API setting. Fleiss' kappa was 0.9991 (Claude), 0.9954 (Gemini), 0.9803 (GPT-4o); GPT-4o had 20 partial-agreement cases and one complete disagreement.

> "Reproducibility, defined as the proportion of questions with identical answers across all three responses, was highest for Claude 3.5 Sonnet at 99.9%, followed by Gemini 1.5 Pro at 99.5%, while GPT-4o also maintained high reproducibility at 97.7%."

## Discussion


## Related Claims
- [GPT-4o accuracy is comparable via API and web chat interfaces, but response consistency between the two deployments is only 87.5%](gpt4o-api-web-consistency-87-5.md) — related
- [GPT-4o achieves the highest overall accuracy on KMLE questions (83.2%), significantly outperforming Claude 3.5 Sonnet and Gemini 1.5 Pro across 2022–2024](gpt4o-highest-kmle-accuracy-83-2.md) — related
- [Gemini 1.5 Pro shows the highest response consistency across 30 repeated exam attempts, significantly exceeding GPT-4o but statistically comparable to Claude](gemini-highest-response-consistency-repeated-attempts.md) — related
- [Temperature parameter has a statistically significant but negligible effect on GPT-4o exam accuracy (ηG² = 0.0017), with global accuracy peaking at temperature 0.23](temperature-effect-negligible-gpt4o-accuracy.md) — related
- [Chatbot responses show near-perfect repeatability across no-feedback attempts (κ 0.967-1.000)](chatbot-response-consistency-kappa-near-perfect.md) — related
