---
type: claim
title: Scaling model size improves performance within K-5 and at the boundary but does not recover Beyond-K-5 performance
description: Scaling model size improves performance within K-5 and at the boundary but does not recover Beyond-K-5 performance
id: scaling-helps-in-scope-not-beyond-k5
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
sources:
  - id: fanfei-li-2026
    resource: "https://arxiv.org/abs/2608.13545"
    title: "Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545"
    author: Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# Scaling model size improves performance within K-5 and at the boundary but does not recover Beyond-K-5 performance

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`

## Subclaims
`q2 i?` Training LittleLearner at 0.6B, 1.3B, and 5B parameters on MathCAMPS shows scaling delivers substantial gains inside the exposure range and partial gains at Grades 6-7, but essentially no effect on Grade 8 where LittleLearner remains at floor across all three sizes. [→ Fanfei Li 2026](#fanfei-li-2026)

## Evidence

### Fanfei Li 2026

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545

`q2 · i?` · `causal · r2`

Scaling experiment training LittleLearner at 0.6B, 1.3B, and 5B parameters and evaluating each on MathCAMPS (Figure 7, 95% CIs). Inside the exposure range scaling delivers substantial gains, and at the smallest size LittleLearner actually outperforms the UNFILTERED control, an advantage the authors attribute to more focused reasoning traces without high-school algebra or calculus competing for capacity.

> "Scaling has a partial effect at the boundary of the training exposure (Grades 6 and 7), whose problem structure still overlaps withK–5arithmetic, but essentially no effect on Grade 8, whose material lies fully outsideLITTLECURRICULUM ."

## Discussion


## Related Claims
- [GRPO post-training boosts in-scope K-5 capabilities but fails to recover Beyond-K-5 capabilities, even when post-trained on out-of-scope data](grpo-post-training-fails-beyond-k5.md) — related
- [In-context learning with few-shot examples and explanations does not unlock Beyond-K-5 reasoning for the 5B LittleLearner](icl-does-not-unlock-beyond-k5-reasoning.md) — related
- [LittleLearner's capabilities tightly track its controlled exposure: strong on in-scope tasks, degrading beyond the K-5 boundary](littlelearner-capabilities-track-controlled-exposure.md) — related
- [Across scaling, post-training, and in-context learning, the pretraining filter rather than the intervention sets LittleLearner's capability ceiling](pretraining-filter-sets-capability-ceiling.md) — a broader claim this one bears on
