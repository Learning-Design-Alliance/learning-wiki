---
type: claim
title: Open-weight (DeepSeek) and proprietary (OpenAI) rubrics produced equivalent grading outcomes in every assignment-approach comparison except Assignment 1 free-form
description: Open-weight (DeepSeek) and proprietary (OpenAI) rubrics produced equivalent grading outcomes in every assignment-approach comparison except Assignment 1 free-form
id: open-weight-proprietary-rubric-equivalence
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
evidence_strength: moderate
sources:
  - id: pedro-c-mendonça-2026
    resource: "https://doi.org/10.1016/j.caeai.2026.100663"
    title: "Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça. (2026). A hybrid reasoning framework for artificial intelligence assessment rubric generation in human and automated contexts: Evidence from an undergraduate programming course. Computers and Education: Artificial Intelligence 11 (2026) 100663. https://doi.org/10.1016/j.caeai.2026.100663"
    author: Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça
    q: 3
    i: "?"
    kind: causal
    rigour: 2
  - id: pedro-c-mendonça-2026-2
    resource: "https://doi.org/10.1016/j.caeai.2026.100663"
    title: "Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça. (2026). A hybrid reasoning framework for artificial intelligence assessment rubric generation in human and automated contexts: Evidence from an undergraduate programming course. Computers and Education: Artificial Intelligence 11 (2026) 100663. https://doi.org/10.1016/j.caeai.2026.100663"
    author: Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Open-weight (DeepSeek) and proprietary (OpenAI) rubrics produced equivalent grading outcomes in every assignment-approach comparison except Assignment 1 free-form

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3`

## Subclaims
`q3 i?` TOST equivalence between DeepSeek- and OpenAI-generated rubrics held for all assignment-level and pooled comparisons except Assignment 1 free-form (TOST p = 0.790). [→ Pedro C. Mendonça 2026](#pedro-c-mendonca-2026)
`q3 i?` Structured generation showed closer cross-model agreement than free-form on both question types, with the largest divergence on text questions in Assignment 1. [→ Pedro C. Mendonça 2026 (2)](#pedro-c-mendonca-2026-2)

## Evidence

### Pedro C. Mendonça 2026

Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça. (2026). A hybrid reasoning framework for artificial intelligence assessment rubric generation in human and automated contexts: Evidence from an undergraduate programming course. Computers and Education: Artificial Intelligence 11 (2026) 100663. https://doi.org/10.1016/j.caeai.2026.100663

`q3 · i?` · `causal · r2`

TOST comparison of DeepSeek versus OpenAI rubric scores across assignments and generation approaches (Table 8). Pooled mean differences were −0.08 for structured and 2.85 for free-form rubrics; Cohen's d values ranged from −0.296 to 0.446.

> "The only exception was Assignment 1 free-form, for which the confidence interval extended beyond the predefined equivalence bounds and the TOST result was not significant (p = 0.790)."

### Pedro C. Mendonça 2026 (2)

Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça. (2026). A hybrid reasoning framework for artificial intelligence assessment rubric generation in human and automated contexts: Evidence from an undergraduate programming course. Computers and Education: Artificial Intelligence 11 (2026) 100663. https://doi.org/10.1016/j.caeai.2026.100663

`q3 · i?` · `causal · r2`

Summary of the cross-family comparison (Section 3.4). Grade agreement by quadratic weighted kappa ranged from 0.893 (Assignment 1 free-form) to 0.974 (Assignment 3 structured) on the 0-20 scale.

> "Structured generation gave the closer cross-model agreement on both question types and across the three assignments, and the free-form comparison on text questions showed the largest divergence between the two families."

## Discussion


## Related Claims

- [When applied by human evaluators, all four AI-generated rubrics met pooled scoring equivalence with a human-created baseline within a ±5-point margin](ai-rubrics-pooled-equivalence-human-evaluators.md) — related
- [In automated evaluation, equivalence with the human baseline depended on the evaluator model: DeepSeek V3 met equivalence for all rubric sources while GPT-4.1 and GPT-4o scored below the baseline](llm-evaluator-equivalence-depends-on-model.md) — related
- [Equivalence failures under human evaluators were confined to five assignment-by-question-type cells, four of them on code questions](five-cells-exceeded-equivalence-margin.md) — related
- [Cohort members predominantly used off-the-shelf multimodal LLMs, mostly OpenAI's GPT, and nearly all combined closed and open source models](cohort-model-use-off-the-shelf-gpt.md)
