---
type: claim
title: GRPO post-training boosts in-scope K-5 capabilities but fails to recover Beyond-K-5 capabilities, even when post-trained on out-of-scope data
description: GRPO post-training boosts in-scope K-5 capabilities but fails to recover Beyond-K-5 capabilities, even when post-trained on out-of-scope data
id: grpo-post-training-fails-beyond-k5
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-20
recheck_by: 2029
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
---

# GRPO post-training boosts in-scope K-5 capabilities but fails to recover Beyond-K-5 capabilities, even when post-trained on out-of-scope data

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-20 (automated, 2 of 2 entries) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly
> **Design limits** · Fanfei Li 2026 (2): the comparison group also received the intervention (read from the study by two models, 2026-10-25)

## Subclaims
`q2 i?` After SFT followed by GRPO, both LittleLearner and UNFILTERED improve within K-5, but in Beyond-K-5 post-training only modestly improves LittleLearner while producing considerably larger gains for UNFILTERED. [→ Fanfei Li 2026](#fanfei-li-2026)
`q2 i?` Within the tested post-training budgets, LittleLearner post-trained on K-5 data shows no difference from LittleLearner post-trained on Beyond-K-5 data. [→ Fanfei Li 2026 (2)](#fanfei-li-2026-2)

## Evidence

### Fanfei Li 2026

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545 [doi:10.48550/arxiv.2608.13545](https://doi.org/10.48550/arxiv.2608.13545)

`q2 · i?` · `causal · r2`

Post-training experiment using a two-stage SFT followed by GRPO pipeline, evaluated on MathCAMPS (Figure 8, 95% CIs). LittleLearner was SFT'd on K-5 data selected by the filtering pipeline and UNFILTERED on a compute-matched unfiltered version; GRPO data was ablated between K-5 and a compute-matched unfiltered counterpart.

> "WithinK–5, post-training lifts both models above their base performance with slightly larger gains for UNFILTERED . InBeyond-K–5, post-training only modestly improves LITTLELEARNER while producing considerably larger gains for UNFILTERED , widening the observed gap between the two models."

### Fanfei Li 2026 (2)

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545

`q2 · i?` · `causal · r2`

GRPO data ablation within the same post-training experiment: LittleLearner post-trained on K-5-filtered questions versus a compute-matched unfiltered counterpart showed no difference within the tested budgets, indicating GRPO alone does not bridge the out-of-scope gap.

> "Crucially, within the tested post-training budgets, we observe no difference between LITTLELEARNER post-trained onK–5data versusBeyond-K–5data."

## Discussion


## Related Claims
- [Across scaling, post-training, and in-context learning, the pretraining filter rather than the intervention sets LittleLearner's capability ceiling](pretraining-filter-sets-capability-ceiling.md) — a broader claim this one bears on
- [Scaling model size improves performance within K-5 and at the boundary but does not recover Beyond-K-5 performance](scaling-helps-in-scope-not-beyond-k5.md) — related
- [LittleLearner's capabilities tightly track its controlled exposure: strong on in-scope tasks, degrading beyond the K-5 boundary](littlelearner-capabilities-track-controlled-exposure.md) — related
- [The multi-stage filtering pipeline reduces Beyond-K-5 retention to near zero while preserving a minority of K-5 content](k5-filter-pipeline-near-zero-beyond-k5-retention.md) — related
- [In-context learning with few-shot examples and explanations does not unlock Beyond-K-5 reasoning for the 5B LittleLearner](icl-does-not-unlock-beyond-k5-reasoning.md) — related
