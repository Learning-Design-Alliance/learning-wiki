---
type: claim
title: In-context learning with few-shot examples and explanations does not unlock Beyond-K-5 reasoning for the 5B LittleLearner
description: In-context learning with few-shot examples and explanations does not unlock Beyond-K-5 reasoning for the 5B LittleLearner
id: icl-does-not-unlock-beyond-k5-reasoning
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: fanfei-li-2026
    resource: "https://doi.org/10.48550/arxiv.2608.13545"
    title: "Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545 [doi:10.48550/arxiv.2608.13545](https://doi.org/10.48550/arxiv.2608.13545)"
    author: Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel
    q: 2
    i: "?"
    kind: causal
    rigour: 2
  - id: fanfei-li-2026-2
    resource: "https://arxiv.org/abs/2608.13545"
    title: "Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545"
    author: Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel
    q: 2
    i: "?"
    kind: causal
    rigour: 1
---

# In-context learning with few-shot examples and explanations does not unlock Beyond-K-5 reasoning for the 5B LittleLearner

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r1`–`r2` · `q2`

## Subclaims
`q2 i?` Few-shot prompting with three manually authored chain-of-thought examples per CCSS standard yields modest K-5 gains but no gain at all in Beyond-K-5 on MathCAMPS. [→ Fanfei Li 2026](#fanfei-li-2026)
`q2 i?` Adding explanations instead of few-shot examples changes neither model responses nor performance. [→ Fanfei Li 2026 (2)](#fanfei-li-2026-2)

## Evidence

### Fanfei Li 2026

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545 [doi:10.48550/arxiv.2608.13545](https://doi.org/10.48550/arxiv.2608.13545)

`q2 · i?` · `causal · r2`

ICL experiment on MathCAMPS synthesizing three new problems per CCSS standard with manually authored chain-of-thought solutions as few-shot examples (Figure 9, 95% CIs). Few shots steered output style, e.g. shorter responses, but this steering did not improve reasoning; hand-written examples performed best among presentation ablations.

> "InK–5using a few shots shows modest gains, and inBeyond-K–5there is no gain at all."

### Fanfei Li 2026 (2)

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545

`q2 · i?` · `causal · r1`

Explanation-prompting condition of the same ICL experiment: providing explanations instead of few-shot examples produced no change in model responses and no performance change on MathCAMPS.

> "When we add explanations instead of few shots, we do not observe the same behavior: Model responses do not change depending on the given explanation, and so does not performance."

## Discussion


## Related Claims
- [Across scaling, post-training, and in-context learning, the pretraining filter rather than the intervention sets LittleLearner's capability ceiling](pretraining-filter-sets-capability-ceiling.md) — a broader claim this one bears on
- [Scaling model size improves performance within K-5 and at the boundary but does not recover Beyond-K-5 performance](scaling-helps-in-scope-not-beyond-k5.md) — related
- [Curricular chain-of-thought prompting improves competency-classification accuracy over zero-shot, with gains concentrated in larger models, while definition-based prompting does not improve performance](curricular-cot-improves-accuracy-larger-models.md) — related
- [LittleLearner's capabilities tightly track its controlled exposure: strong on in-scope tasks, degrading beyond the K-5 boundary](littlelearner-capabilities-track-controlled-exposure.md) — related
