---
type: claim
title: "GPT-4V's accuracy was inconsistent across medical subdomains, high in some (e.g. immunology 100%) and low in others (e.g. anatomy 25%)"
description: "GPT-4V's accuracy was inconsistent across medical subdomains, high in some (e.g."
id: gpt4v-subdomain-performance-inconsistent
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-07
evidence_strength: weak
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: yang-z-2025
    resource: "https://doi.org/10.2196/65146"
    title: "Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H. (2025). Unveiling GPT-4V's hidden challenges behind high accuracy on USMLE questions: Observational Study. Journal of Medical Internet Research. https://doi.org/10.2196/65146"
    author: Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# GPT-4V's accuracy was inconsistent across medical subdomains, high in some (e.g. immunology 100%) and low in others (e.g. anatomy 25%)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GPT-4V achieved high accuracy on subdomains such as immunology (5/5, 100%) and otolaryngology (6/6, 100%), and low accuracy on anatomy (1/4, 25%), emergency medicine (1/4, 25%), and pathology (5/10, 50%). [→ Yang Z 2025](#yang-z-2025)

## Evidence

### Yang Z 2025

Yang Z, Yao Z, Tasmin M, Vashisht P, Jang WS, Ouyang F, Wang B, McManus D, Berlowitz D, Yu H. (2025). Unveiling GPT-4V's hidden challenges behind high accuracy on USMLE questions: Observational Study. Journal of Medical Internet Research. https://doi.org/10.2196/65146

`q2 · i?` · `associational · r2`

Discussion-section report of per-subdomain accuracy from Table S1 (Multimedia Appendix 1) covering the 227 image questions across 28 subdomains. The quote names the high- and low-accuracy subdomains with their printed fractions.

> "GPT-4V achieved high accuracy on subdomains such as immunology (5/5, 100%), otolaryngology (6/6, 100%), and pulmonology (6/8, 75%), and low accuracy on others such as anatomy (1/4, 25%), emergency medicine (1/4, 25%), and pathology (5/10, 50%)."

## Discussion


## Related Claims
- [Expert hints raised GPT-4V's accuracy and flattened its performance across question difficulty levels, while medical students' performance declined with difficulty](expert-hints-raise-gpt4v-accuracy-plateau-difficulty.md) — related
- [LLM accuracy varied by subject area, with oral pathology (94%) and salivary gland diseases (91.8%) highest and radiological anatomy (67.3%) lowest; only Copilot showed a statistically significant across-subject difference](subject-area-accuracy-variation-dus-llms.md) — a broader claim this one bears on
- [LLM accuracy is uniformly high in OT basic sciences but lower on OT-specific content, widening further on visuals](basic-sciences-high-ot-specific-lower.md) — related
- [GPT-4V outperformed GPT-3.5 Turbo and GPT-4 on multiple-choice medical exam questions with images](gpt4v-outperforms-earlier-llms-image-questions.md) — related
- [When GPT-4V answered incorrectly, its explanations frequently contained image misunderstandings, reasoning errors, and hallucinations](gpt4v-poor-explanations-incorrect-answers.md) — related
- [In a simulated curbside consultation, GPT-4V required multiple specific physician-guided prompts to interpret complex case data accurately](curbside-consultation-required-multiple-prompts.md) — related
- [GPT-4o accuracy on EUNACOM varies substantially by medical specialty, highest in psychiatry, neurology, and surgery and lowest in neonatology, otolaryngology, and urology/nephrology](eunacom-accuracy-varies-by-specialty.md) — a broader claim this one bears on
- [GPT-4 and GPT-4o show substantial improvement over GPT-3.5 across all clinical clerkships, with GPT-4o achieving 100% in family medicine and internal medicine](gpt-4o-clerkship-accuracy-including-perfect-family-and-internal-medicine.md) — related
