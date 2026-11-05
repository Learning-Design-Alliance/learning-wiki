---
type: claim
title: "McNemar's exact test confirms o1-Pro's advantage is statistically significant (P=0.0015, OR 5.00)"
description: "McNemar's exact test confirms o1-Pro's advantage is statistically significant (P=0.0015, OR 5.00)"
id: mcnemar-significant-o1-pro-advantage-ukmla
aliases: [o1-pro-outperforms-gpt4o-ukmla-items]
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
evidence_strength: moderate
newest_evidence: 2025
recheck_by: 2028
sources:
  - id: vakili-b-2025
    resource: "https://doi.org/10.3352/jeehp.2025.22.30"
    title: "Vakili B, Ahmad A, Zolfaghari M. (2025). Performance of GPT-4o and o1-Pro on United Kingdom Medical Licensing Assessment-style items: a comparative study. Journal of Educational Evaluation for Health Professions. https://doi.org/10.3352/jeehp.2025.22.30"
    author: Vakili B, Ahmad A, Zolfaghari M.
    q: 3
    i: "?"
---

# McNemar's exact test confirms o1-Pro's advantage is statistically significant (P=0.0015, OR 5.00)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · `q3` peer-reviewed experiment
> **Currency** · newest study 2025 · not yet checked against its sources · not reviewed by a person · recheck by 2028: tool and model accuracy changes quickly

## Subclaims

`q3 i?` The paired difference between the two models on discordant items reached statistical significance in favor of o1-Pro. [→ Vakili B 2025](#vakili-b-2025)

`q3 i2` On 374 paired UKMLA-style items, o1-Pro (93.0%) significantly outperformed GPT-4o (88.8%) by McNemar's exact test. [→ Vakili B 2025](#vakili-b-2025)

## Evidence

### Vakili B 2025

Vakili B, Ahmad A, Zolfaghari M. (2025). Performance of GPT-4o and o1-Pro on United Kingdom Medical Licensing Assessment-style items: a comparative study. Journal of Educational Evaluation for Health Professions. https://doi.org/10.3352/jeehp.2025.22.30

`q3 · i?`

McNemar's test for paired binary outcomes on the same 374-item set, computed on discordant pairs (20 vs 4 items). The article prints "McNemar’s exact test confirmed that o1-Pro’s advantage was statistically significant (P=0.0015)" with OR 5.00 (95% CI, 1.71–14.63).

> "McNemar’s exact test confirmed that o1-Pro’s advantage was statistically significant (P=0.0015). As a measure of effect size, the odds ratio (OR) for discordant pairs was 5.00 (95% confidence interval [CI], 1.71–14.63)"

<!-- merged 2026-11-05 from o1-pro-outperforms-gpt4o-ukmla-items: that page's entry for this study, which differed from the one above, kept verbatim.
### Vakili B 2025

Vakili B, Ahmad A, Zolfaghari M. (2025). Performance of GPT-4o and o1-Pro on United Kingdom Medical Licensing Assessment-style items: a comparative study. Journal of Educational Evaluation for Health Professions. https://doi.org/10.3352/jeehp.2025.22.30

`q3 · i?`

Descriptive comparative analysis of two OpenAI models answering an identical curated item set; GPT-4o achieved "88.8% accuracy, while o1-Pro answered 348 correctly (93.0%)". Odds ratio OR=5.00 (95% CI, 1.71–14.63) and P=0.0015 are reported in the Results text.

> "Out of 374 UKMLA-style items, GPT-4o answered 332 correctly (88.8% accuracy), while o1-Pro answered 348 correctly (93.0%)."
-->

## Discussion



## Related Claims

- [o1-Pro consistently outperformed GPT-4o in dermatology and respiratory medicine (+18.2 points each) among specialty differences](o1-pro-dermatology-respiratory-specialty-gaps.md) — related
- [Pairwise McNemar comparisons showed OpenAI o1 significantly better than GPT-4o, Gemini, and Copilot in Respiratory Medicine, with mixed significance across other courses](mcnemar-pairwise-openai-o1-vs-other-llms-mixed.md) — related
- [Both ChatGPT models exceed the UKMLA pass threshold (57.5%) on UKMLA-style items](chatgpt-models-exceed-ukmla-pass-threshold.md) — a broader claim this one bears on
- [On 20 image-based items o1-Pro scored 90% versus GPT-4o's 75%, a non-significant difference presented as exploratory](image-based-items-ukmla-exploratory-null.md) — related
- [Newer OpenAI LLM versions achieve significantly higher pooled accuracy on biomedical MCQs than earlier versions (GPT‐4o–o1: 90%; GPT‐4: 82%; GPT‐3/3.5: 59%)](openai-llm-accuracy-improves-across-versions-biomedical-mcq.md) — a broader claim this one bears on
