---
type: claim
title: Providing official reference solutions consistently reduces LLM marking error on structured physics questions
description: Providing official reference solutions consistently reduces LLM marking error on structured physics questions
id: official-solutions-reduce-llm-marking-error
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: will-yeadon-2026
    resource: "https://doi.org/10.48550/arXiv.2603.14732"
    title: "Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)"
    author: Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Providing official reference solutions consistently reduces LLM marking error on structured physics questions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across all five models and the committee, fractional MAE on curriculum questions falls when the official solution is supplied (e.g., Claude 0.120→0.065). [→ Will Yeadon 2026](#will-yeadon-2026)

## Evidence

### Will Yeadon 2026

Will Yeadon, Tom Hardy, Paul Mackay, and Elise Agra. (2026). LLM-as-a-judge validity is strongly task-dependent across physics assessment formats. arXiv. [doi:10.48550/arXiv.2603.14732](https://doi.org/10.48550/arXiv.2603.14732)

`q2 · i?` · `causal · r2`

Comparison of blind versus solution-informed marking on GCSE, A-Level and textbook questions (n=1151). The article reports that "providing the official solution consistently reduces fractional MAE across all models", with all values above the human inter-rater fMAE of 0.051.

> "providing the official solution consistently reduces fractional MAE across all models (GPT-5.2: 0.131→0.083; Claude: 0.120→0.065; Gemini: 0.092→0.070; DeepSeek: 0.185→0.112; Grok: 0.112→0.101; committee: 0.127→0.083)"

## Discussion


## Related Claims
- [False reference solutions degrade LLM absolute marking accuracy but leave rank-order agreement largely intact](false-solutions-degrade-accuracy-not-ranking.md) — related
- [LLM markers show robust rank-order agreement with human markers on blind university exam questions and structured curriculum questions](llm-rank-order-agreement-structured-physics-questions.md) — related
- [LLM-powered error detectors show a consistent performance gap (conformity bias) between conventional and alternative solutions to math word problems](llm-conformity-bias-mwp-error-detection.md) — related
- [State-of-the-art LLMs struggle to locate the first error step in student math solutions even when given the gold reference solution](llms-struggle-first-error-localization-with-gold-solution.md) — related
