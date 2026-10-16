---
type: claim
title: "LittleLearner's capabilities tightly track its controlled exposure: strong on in-scope tasks, degrading beyond the K-5 boundary"
description: "LittleLearner's capabilities tightly track its controlled exposure: strong on in-scope tasks, degrading beyond the K-5 boundary"
id: littlelearner-capabilities-track-controlled-exposure
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
    rigour: 2
  - id: fanfei-li-2026-3
    resource: "https://arxiv.org/abs/2608.13545"
    title: "Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545"
    author: Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel
    q: 2
    i: "?"
    kind: causal
    rigour: 2
---

# LittleLearner's capabilities tightly track its controlled exposure: strong on in-scope tasks, degrading beyond the K-5 boundary

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (3 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` On Jeopardy science questions split by NGSS grade scope, LittleLearner shows a sudden drop in factual knowledge beyond its exposure horizon while UNFILTERED performs comparably across both bins. [→ Fanfei Li 2026](#fanfei-li-2026)
`q2 i?` On MathCAMPS, LittleLearner exhibits a disproportionately large decline in performance at higher grade levels compared with UNFILTERED and Gemma 2B, and at Grade 8 even pass@1024 solves fewer than half as many questions as UNFILTERED. [→ Fanfei Li 2026 (2)](#fanfei-li-2026-2)
`q2 i?` LittleLearner's bits-per-byte rises steadily with text hardness on CLEAR while UNFILTERED and Gemma 2B remain comparatively flat, and it shows growing unfamiliarity with Beyond-K-5 math content on CoMTA. [→ Fanfei Li 2026 (3)](#fanfei-li-2026-3)

## Evidence

### Fanfei Li 2026

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545 [doi:10.48550/arxiv.2608.13545](https://doi.org/10.48550/arxiv.2608.13545)

`q2 · i?` · `causal · r2`

Evaluation of factual knowledge on Jeopardy science questions split into NGSS K-5 and Beyond-K-5 bins, with Gemini Flash annotating each question's curriculum strand. LittleLearner shows a sudden drop beyond its exposure horizon while the UNFILTERED control performs comparably across both bins; since both models share the training recipe, the drop is attributed to the limited knowledge in LittleCurriculum.

> "LITTLELEARNER shows a sudden drop in factual knowledge beyond its exposure horizon, while UNFILTERED performs comparably across both bins."

### Fanfei Li 2026 (2)

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545

`q2 · i?` · `causal · r2`

Mathematical reasoning evaluated on MathCAMPS, synthetic questions aligned with individual CCSS standards, estimated from 1024 rollouts with 95% CIs. LittleLearner answers K-5 math on par with the reference models but collapses disproportionately at higher grades; on Grade 8 problems even at pass@1024 it solves fewer than half as many questions as UNFILTERED.

> "Compared with UNFILTERED and Gemma 2B, LITTLELEARNER exhibits a disproportionately large decline in performance at higher grade levels."

### Fanfei Li 2026 (3)

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545

`q2 · i?` · `causal · r2`

Language-familiarity validation on the CLEAR dataset, which provides Bradley-Terry easiness scores from expert teacher judgments, with BPB as the measure. LittleLearner's BPB steadily rises with hardness while the two reference models remain flat; on CoMTA student turns, LittleLearner matches the references on K-5 math but shows growing unfamiliarity on Beyond-K-5 content.

> "LITTLELEARNER ’s bits-per-byte (BPB) [ 46] steadily rises with increased hardness, whileUNFILTERED ’s and Gemma 2B’s BPB remain comparatively flat and closely track each other."

## Discussion


## Related Claims
- [GRPO post-training boosts in-scope K-5 capabilities but fails to recover Beyond-K-5 capabilities, even when post-trained on out-of-scope data](grpo-post-training-fails-beyond-k5.md) — related
- [Scaling model size improves performance within K-5 and at the boundary but does not recover Beyond-K-5 performance](scaling-helps-in-scope-not-beyond-k5.md) — related
- [Across scaling, post-training, and in-context learning, the pretraining filter rather than the intervention sets LittleLearner's capability ceiling](pretraining-filter-sets-capability-ceiling.md) — a broader claim this one bears on
- [The multi-stage filtering pipeline reduces Beyond-K-5 retention to near zero while preserving a minority of K-5 content](k5-filter-pipeline-near-zero-beyond-k5-retention.md) — related
- [In-context learning with few-shot examples and explanations does not unlock Beyond-K-5 reasoning for the 5B LittleLearner](icl-does-not-unlock-beyond-k5-reasoning.md) — related
