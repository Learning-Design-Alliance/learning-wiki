---
type: claim
title: Human experts and LLMs show qualitatively different error patterns in outcome prediction
description: Human experts and LLMs show qualitatively different error patterns in outcome prediction
id: expert-llm-error-patterns-differ
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: michal-štefánik-2026
    resource: "https://doi.org/10.48550/arxiv.2609.20484"
    title: "Michal Štefánik, Jan Nehyba, Jirina Karasova, Martin Fico, Lucie Škarková, Markéta Košatková, David Kosatka. (2026). Edustories: A Collection of Real-world Case Studies from Classroom Practices. https://arxiv.org/abs/2609.20484 [doi:10.48550/arxiv.2609.20484](https://doi.org/10.48550/arxiv.2609.20484)"
    author: Michal Štefánik, Jan Nehyba, Jirina Karasova, Martin Fico, Lucie Škarková, Markéta Košatková, David Kosatka
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Human experts and LLMs show qualitatively different error patterns in outcome prediction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Experts' errors arise mainly from assigning failure cases to short-term success while remaining highly accurate (84.41%) on long-term success; models primarily struggle to distinguish short- from long-term success. [→ Michal Štefánik 2026](#michal-stefanik-2026)

## Evidence

### Michal Štefánik 2026

Michal Štefánik, Jan Nehyba, Jirina Karasova, Martin Fico, Lucie Škarková, Markéta Košatková, David Kosatka. (2026). Edustories: A Collection of Real-world Case Studies from Classroom Practices. https://arxiv.org/abs/2609.20484 [doi:10.48550/arxiv.2609.20484](https://doi.org/10.48550/arxiv.2609.20484)

`q2 · i?` · `design · r2`

Confusion-matrix comparison (Appendix A.1) of the best expert, best model, and aggregated groups on three-way outcome classification. The best expert identified long-term success at "84.41%"; averaged experts reached 71.97% versus 49.88% for averaged models on that class.

> "This pattern is consistent across experts, who substantially outperform language models in identifying long-term success (71.97% vs. 49.88%), though they are more susceptible to other types of errors."

## Discussion


## Related Claims
- [Current LLMs fall short of human experts in predicting classroom intervention outcomes](llms-below-expert-outcome-prediction.md) — related
- [Zero-shot LLM errors follow four recurring patterns: over-interpretation, failure to detect relevant information, hallucination, and failure to generate a response](llm-competency-error-patterns-four-types.md) — related
- [Qualitative error analysis yields five recurring error types, with over-inference most prevalent (33.5%), followed by evidence misidentification (23.4%) and hallucination (19.8%)](five-error-types-llm-diagnosis-vague-evidence.md) — related
