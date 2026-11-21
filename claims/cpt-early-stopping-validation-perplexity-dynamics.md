---
type: claim
title: Early stopping on course-material perplexity lets CPT adapt to course materials while minimizing forgetting, per validation-loss dynamics
description: Early stopping on course-material perplexity lets CPT adapt to course materials while minimizing forgetting, per validation-loss dynamics
id: cpt-early-stopping-validation-perplexity-dynamics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
evidence_strength: weak
newest_evidence: 2026
sources:
  - id: tu-anh-dinh-2026
    resource: "https://doi.org/10.63317/5bjdtya4ui69"
    title: "Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues. (2026). From Slides to Chatbots: Enhancing Large Language Models with University Course Materials. Originally published 2025. [doi:10.63317/5bjdtya4ui69](https://doi.org/10.63317/5bjdtya4ui69)"
    author: Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Early stopping on course-material perplexity lets CPT adapt to course materials while minimizing forgetting, per validation-loss dynamics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` During CPT, course-material validation perplexity drops sharply in the first few steps before stabilizing while Wikipedia validation perplexity gradually increases; early stopping once course-material perplexity converges yields a model that adapts while minimizing forgetting. [→ Tu Anh Dinh 2026](#tu-anh-dinh-2026)

## Evidence

### Tu Anh Dinh 2026

Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues. (2026). From Slides to Chatbots: Enhancing Large Language Models with University Course Materials. Originally published 2025. [doi:10.63317/5bjdtya4ui69](https://doi.org/10.63317/5bjdtya4ui69)

`q2 · i?` · `causal · r2`

Analysis of validation losses (perplexity) during CPT of LLaMA 3.1 8B on course material and Wikipedia replay data, shown in Figure 4. The article reports the course-material perplexity "drops sharply in the first few steps" while Wikipedia perplexity gradually increases, and that early stopping yields a model adapting "while minimizing forgetting of its original knowledge".

> "The validation perplexity on the course materials drops sharply in the first few steps beforestabilizing, whereastheWikipediavalidation perplexity gradually increases over time."

## Discussion


## Related Claims
- [CPT on course materials does not bring consistent improvement, performing on average worse than both baseline and RAG](cpt-inconsistent-gains-catastrophic-forgetting.md) — related
- [Language models catastrophically forget L1 when exposure ceases, unlike humans past the critical period](lms-catastrophic-l1-attrition-sequential.md) — a broader claim this one bears on
