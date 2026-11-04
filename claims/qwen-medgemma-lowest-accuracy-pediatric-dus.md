---
type: claim
title: Qwen-3 and MedGemma exhibited notably lower accuracy on pediatric dentistry DUS questions than other LLMs
description: Qwen-3 and MedGemma exhibited notably lower accuracy on pediatric dentistry DUS questions than other LLMs
id: qwen-medgemma-lowest-accuracy-pediatric-dus
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: kayaci-sukriye-turkoglu-2026
    resource: "https://doi.org/10.1038/s41598-026-57392-7"
    title: "Kayaci Sukriye Turkoglu, Ilhan Hamza Osman, Tassoker Melek, Cap Taha, Demir Helin. (2026). Benchmarking GPT-5, Gemini 2.5 Pro, Grok 4, and other LLMs on pediatric dentistry questions from a dental specialization exam. Scientific Reports. https://doi.org/10.1038/s41598-026-57392-7"
    author: Kayaci Sukriye Turkoglu, Ilhan Hamza Osman, Tassoker Melek, Cap Taha, Demir Helin
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Qwen-3 and MedGemma exhibited notably lower accuracy on pediatric dentistry DUS questions than other LLMs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Qwen-3 (49.58% reasoning, 54.62% no reasoning) and MedGemma (58.82%) showed the weakest accuracy across most comparisons. [→ Kayaci Sukriye Turkoglu 2026](#kayaci-sukriye-turkoglu-2026)

## Evidence

### Kayaci Sukriye Turkoglu 2026

Kayaci Sukriye Turkoglu, Ilhan Hamza Osman, Tassoker Melek, Cap Taha, Demir Helin. (2026). Benchmarking GPT-5, Gemini 2.5 Pro, Grok 4, and other LLMs on pediatric dentistry questions from a dental specialization exam. Scientific Reports. https://doi.org/10.1038/s41598-026-57392-7

`q2 · i?` · `design · r2`

Same benchmark of 119 DUS pediatric dentistry MCQs. Qwen-3 and MedGemma recorded the lowest accuracy rates, with Qwen-3 reasoning mode at "49.58" percent and MedGemma at "58.82" percent.

> "In contrast, Qwen-3 (49.58 - Reasoning, 54.62 - No Reasoning), and MedGemma (58.82%) exhibited notably lower accuracy rates across most comparisons."

## Discussion


## Related Claims
- [Gemini 2.5 Pro achieved the highest accuracy (92.44%) on pediatric dentistry DUS questions, significantly outperforming most other LLMs](gemini-2-5-pro-highest-accuracy-pediatric-dus.md) — related
- [Pairwise comparisons with Bonferroni-corrected McNemar's tests identified statistically significant differences favouring the highest-performing proprietary systems, most notably GPT-5 Pro over five lower-ranked models.](mcnemar-pairwise-llm-ebhs-significant-differences.md) — related
