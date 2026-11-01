---
type: claim
title: Tokenizer vocabulary size exhibits a concave-down (Goldilocks) relationship with LLM scoring agreement, with diminishing returns beyond moderate sizes
description: Tokenizer vocabulary size exhibits a concave-down (Goldilocks) relationship with LLM scoring agreement, with diminishing returns beyond moderate sizes
id: vocab-size-concave-scoring-agreement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-01
evidence_strength: moderate
newest_evidence: 2026
recheck_by: 2029
sources:
  - id: michael-hardy-2026
    resource: "https://arxiv.org/abs/2603.04820"
    title: "Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820"
    author: Michael Hardy
    q: 2
    i: "?"
    kind: quant-synthesis
    rigour: 2
---

# Tokenizer vocabulary size exhibits a concave-down (Goldilocks) relationship with LLM scoring agreement, with diminishing returns beyond moderate sizes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · quant-synthesis `r2` · `q2`
> **Currency** · newest study 2026 · not yet checked against its sources · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` The quadratic vocabulary term is negative in the Bayesian model (≈ -0.06, excluding 0), consistent with a concave-down relationship between vocabulary size and QWK agreement. [→ Michael Hardy 2026](#michael-hardy-2026)

## Evidence

### Michael Hardy 2026

Michael Hardy. (2026). Autoscoring Anticlimax: A Meta-analytic Understanding of AI's Short-answer Shortcomings and Wording Weaknesses. https://arxiv.org/abs/2603.04820

`q2 · i?` · `quant-synthesis · r2`

Bayesian meta-regression of 890 QWK observations. The quadratic vocabulary effect is "negative (Bayes≈−0.06 , excluding 0), consistent with a concave-down relationship". The article attributes both failure modes—over-fragmentation at small sizes and under-trained rare tokens at large sizes—to reduced scoring reliability.

> "The more diagnostic result is the quadratic vocabulary effect: |V| 2 is negative (Bayes≈−0.06 , excluding 0), consistent with a concave-down relationship. This supports a practical hypothesis specific to child-written responses: extremely small vocabularies over-fragment idiosyncratic spellings and morphology, while extremely large vocabularies include rare or under-trained tokens that behave unpredictably on out-of-distribution orthography."

## Discussion


## Related Claims
- [In a visual-spatial integration task, the interaction between visual-spatial working memory capacity and visual design is quadratic, with the inverted-U progression more strongly accentuated for the dynamic design](quadratic-ati-spatial-ability-visual-design-study1.md) — a broader claim this one bears on
- [Non-linear (Goldilocks) effects of expectations and aspirations on outcomes are small and largely non-significant](goldilocks-effect-not-supported-expectations.md) — a broader claim this one bears on
- [Perceived task difficulty relates to metacognitive strategy use only linearly, with no significant quadratic component](task-difficulty-linear-metacognitive-strategies.md) — a broader claim this one bears on
- [Intervention duration of 3–9 weeks yields the greatest AWE gains, with diminishing returns beyond 10 weeks](awe-duration-3-9-weeks-optimal.md) — a broader claim this one bears on
