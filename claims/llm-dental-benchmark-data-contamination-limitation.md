---
type: claim
title: Data contamination and single-dataset limitations restrict generalizability of LLM benchmarking results on dental specialization exams
description: Data contamination and single-dataset limitations restrict generalizability of LLM benchmarking results on dental specialization exams
id: llm-dental-benchmark-data-contamination-limitation
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-04
evidence_strength: weak
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: kayaci-sukriye-turkoglu-2026
    resource: "https://doi.org/10.1038/s41598-026-57392-7"
    title: "Kayaci Sukriye Turkoglu, Ilhan Hamza Osman, Tassoker Melek, Cap Taha, Demir Helin. (2026). Benchmarking GPT-5, Gemini 2.5 Pro, Grok 4, and other LLMs on pediatric dentistry questions from a dental specialization exam. Scientific Reports. https://doi.org/10.1038/s41598-026-57392-7"
    author: Kayaci Sukriye Turkoglu, Ilhan Hamza Osman, Tassoker Melek, Cap Taha, Demir Helin
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Data contamination and single-dataset limitations restrict generalizability of LLM benchmarking results on dental specialization exams

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The authors identify data contamination risk, single-dataset reliance, and non-uniform temperature settings as key limitations. [→ Kayaci Sukriye Turkoglu 2026](#kayaci-sukriye-turkoglu-2026)

## Evidence

### Kayaci Sukriye Turkoglu 2026

Kayaci Sukriye Turkoglu, Ilhan Hamza Osman, Tassoker Melek, Cap Taha, Demir Helin. (2026). Benchmarking GPT-5, Gemini 2.5 Pro, Grok 4, and other LLMs on pediatric dentistry questions from a dental specialization exam. Scientific Reports. https://doi.org/10.1038/s41598-026-57392-7

`q1 · i?` · `design · r2`

Authors' stated limitations section. They flag "data contamination" risk from exam content in training data, alongside single-dataset reliance and GPT-5's non-uniform temperature setting as constraints on generalizability.

> "Another potential limitation is data contamination, as some exam-related content may have been included in the training data of the models, potentially influencing their performance."

## Discussion


## Related Claims
- [Same-model LLM configuration pairs agree more than cross-model pairs, and agreement decreases monotonically as temperature difference increases](llm-pairwise-agreement-model-type-temperature.md) — related
- [Temperature-construct interactions: constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings](temperature-construct-type-interaction-coding.md) — related
