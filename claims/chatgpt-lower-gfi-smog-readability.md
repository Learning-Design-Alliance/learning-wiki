---
type: claim
title: ChatGPT-5.1 generates EUS answers with significantly lower linguistic complexity (GFI, SMOG) than DeepSeek-R1 and Gemini 2.5 Flash
description: ChatGPT-5.1 generates EUS answers with significantly lower linguistic complexity (GFI, SMOG) than DeepSeek-R1 and Gemini 2.5 Flash
id: chatgpt-lower-gfi-smog-readability
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: balaban-ugur-2026
    resource: "https://doi.org/10.1038/s41598-026-57001-7"
    title: "Balaban Ugur, Erbay Bahar, Aktan Mustafa, Demirkan Kutay. (2026). Performance of large language models on the Turkish Pharmacy Specialty Examination: a comparative analysis of accuracy, confidence, and readability. Scientific Reports. https://doi.org/10.1038/s41598-026-57001-7"
    author: Balaban Ugur, Erbay Bahar, Aktan Mustafa, Demirkan Kutay
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: balaban-ugur-2026-2
    resource: "https://doi.org/10.1038/s41598-026-57001-7"
    title: "Balaban Ugur, Erbay Bahar, Aktan Mustafa, Demirkan Kutay. (2026). Performance of large language models on the Turkish Pharmacy Specialty Examination: a comparative analysis of accuracy, confidence, and readability. Scientific Reports. https://doi.org/10.1038/s41598-026-57001-7"
    author: Balaban Ugur, Erbay Bahar, Aktan Mustafa, Demirkan Kutay
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# ChatGPT-5.1 generates EUS answers with significantly lower linguistic complexity (GFI, SMOG) than DeepSeek-R1 and Gemini 2.5 Flash

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` GFI (p = 0.001) and SMOG (p < 0.001) differed significantly across models, with ChatGPT-5.1 producing the most readable texts; no significant differences were found for FRE (p = 0.790). [→ Balaban Ugur 2026](#balaban-ugur-2026)
`q2 i?` Post-hoc comparisons show ChatGPT-5.1 with significantly lower GFI than DeepSeek-R1 (p = 0.017) and Gemini 2.5 Flash (p < 0.001), and lower SMOG than both (p < 0.001 for both). [→ Balaban Ugur 2026 (2)](#balaban-ugur-2026-2)

## Evidence

### Balaban Ugur 2026

Balaban Ugur, Erbay Bahar, Aktan Mustafa, Demirkan Kutay. (2026). Performance of large language models on the Turkish Pharmacy Specialty Examination: a comparative analysis of accuracy, confidence, and readability. Scientific Reports. https://doi.org/10.1038/s41598-026-57001-7

`q2 · i?` · `design · r2`

Friedman test on readability of machine-translated responses to all 84 EUS questions (Table 3). Both the GFI (p = 0.001) and SMOG (p < 0.001) differed significantly across LLMs; FRE showed no significant difference (p = 0.790).

> "In contrast, both the GFI (p = 0.001) and SMOG (p < 0.001) differed significantly across LLMs, with ChatGPT-5.1 producing relatively more readable texts, whereas DeepSeek-R1 and Gemini 2.5 Flash generated more complex texts requiring higher educational attainment for comprehension."

### Balaban Ugur 2026 (2)

Balaban Ugur, Erbay Bahar, Aktan Mustafa, Demirkan Kutay. (2026). Performance of large language models on the Turkish Pharmacy Specialty Examination: a comparative analysis of accuracy, confidence, and readability. Scientific Reports. https://doi.org/10.1038/s41598-026-57001-7

`q2 · i?` · `design · r2`

Durbin–Conover post-hoc pairwise comparisons of readability indices (Table 4). ChatGPT-5.1 generated significantly lower GFI scores than DeepSeek-R1 (p = 0.017) and Gemini 2.5 Flash (p < 0.001); no significant DeepSeek–Gemini differences for GFI or SMOG.

> "Post-hoc pairwise comparisons showed that ChatGPT-5.1 generated significantly lower GFI scores than DeepSeek-R1 (p = 0.017) and Gemini 2.5 Flash (p < 0.001)."

## Discussion


## Related Claims
- [Iterative prompting to revise overly complex responses raised readability alignment, with most regenerated responses falling at or below target grade levels](iterative-prompting-improves-readability-alignment.md) — related
- [In the random forest, word count was the most important readability feature while traditional readability formulas ranked near the bottom](word-count-top-traditional-formulas-unimportant.md) — related
- [LLMs frequently assign maximum self-reported confidence to incorrect EUS answers](llm-overconfidence-incorrect-eus-answers.md) — related
- [ChatGPT-5.1, DeepSeek-R1, and Gemini 2.5 Flash show high, statistically comparable accuracy on Turkish Pharmacy Specialty Examination questions](llms-high-comparable-accuracy-eus.md) — related
- [All EUS-generated LLM texts show low Flesch Reading Ease scores, indicating substantial reading difficulty](low-fre-llm-pharmacy-texts.md) — related
