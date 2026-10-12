---
type: claim
title: "In automated evaluation, equivalence with the human baseline depended on the evaluator model: DeepSeek V3 met equivalence for all rubric sources while GPT-4.1 and GPT-4o scored below the baseline"
description: "In automated evaluation, equivalence with the human baseline depended on the evaluator model: DeepSeek V3 met equivalence for all rubric sources while GPT-4.1 and GPT-4o scored below the baseline"
id: llm-evaluator-equivalence-depends-on-model
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
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# In automated evaluation, equivalence with the human baseline depended on the evaluator model: DeepSeek V3 met equivalence for all rubric sources while GPT-4.1 and GPT-4o scored below the baseline

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`–`q3`

## Subclaims
`q3 i?` DeepSeek V3 stayed within the ±5-point margin for all four AI-generated rubric sources, whereas GPT-4.1 and GPT-4o showed systematic negative deviations, largest under structured rubrics. [→ Pedro C. Mendonça 2026](#pedro-c-mendonca-2026)
`q3 i?` A cluster-robust linear model estimated GPT-4.1 4.13 points lower and GPT-4o 2.47 points lower than DeepSeek V3 relative to the human baseline (both p < 0.001). [→ Pedro C. Mendonça 2026 (2)](#pedro-c-mendonca-2026-2)

## Evidence

### Pedro C. Mendonça 2026

Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça. (2026). A hybrid reasoning framework for artificial intelligence assessment rubric generation in human and automated contexts: Evidence from an undergraduate programming course. Computers and Education: Artificial Intelligence 11 (2026) 100663. https://doi.org/10.1016/j.caeai.2026.100663

`q3 · i?` · `causal · r2`

Within-LLM comparison across 308 responses and five rubric sources (Table 5): three LLM evaluators each scored all responses under all rubrics. Mean differences ranged from −6.28 (GPT-4.1 with OpenAI Structured) to 3.07 points (DeepSeek V3 with DeepSeek Free).

> "DeepSeek V3 remained within the ±5-point margin for all four AI-generated rubric sources, while GPT-4.1 and GPT-4o scored below the human baseline, with their largest deviations under structured rubrics."

### Pedro C. Mendonça 2026 (2)

Pedro C. Mendonça, Filipe Quintal, Mário Figueiredo, Karolina Baras, Fábio Mendonça. (2026). A hybrid reasoning framework for artificial intelligence assessment rubric generation in human and automated contexts: Evidence from an undergraduate programming course. Computers and Education: Artificial Intelligence 11 (2026) 100663. https://doi.org/10.1016/j.caeai.2026.100663

`q2 · i?` · `causal · r2`

Linear model of within-LLM differences with cluster-robust standard errors clustered by response, separating evaluator and rubric-family contributions. The rubric-family effect was 1.64 points, with DeepSeek-family rubrics scoring higher than OpenAI-family rubrics (p < 0.001).

> "Relative to DeepSeek V3, the differences from the human-created baseline were 4.13 points lower for GPT-4.1 (95% CI [ 5.47,  2.79], p < 0.001) and 2.47 points lower for GPT-4o (95% CI [ 3.67,  1.26], p < 0.001)."

## Discussion


## Related Claims
- [When applied by human evaluators, all four AI-generated rubrics met pooled scoring equivalence with a human-created baseline within a ±5-point margin](ai-rubrics-pooled-equivalence-human-evaluators.md) — related
- [Equivalence failures under human evaluators were confined to five assignment-by-question-type cells, four of them on code questions](five-cells-exceeded-equivalence-margin.md) — related
- [Open-weight (DeepSeek) and proprietary (OpenAI) rubrics produced equivalent grading outcomes in every assignment-approach comparison except Assignment 1 free-form](open-weight-proprietary-rubric-equivalence.md) — related
- [Under LLM evaluators, structured rubrics produced larger negative deviations from the human baseline than free-form rubrics, the opposite direction of the human-evaluator pattern](structured-free-form-llm-deviation-contrast.md) — possibly the same claim (merge candidate)
