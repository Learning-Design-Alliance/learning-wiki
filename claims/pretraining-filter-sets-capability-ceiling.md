---
type: claim
title: "Across scaling, post-training, and in-context learning, the pretraining filter rather than the intervention sets LittleLearner's capability ceiling"
description: "Across scaling, post-training, and in-context learning, the pretraining filter rather than the intervention sets LittleLearner's capability ceiling"
id: pretraining-filter-sets-capability-ceiling
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
evidence_strength: moderate
newest_evidence: 2026
source_checked: 2026-10-19
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
---

# Across scaling, post-training, and in-context learning, the pretraining filter rather than the intervention sets LittleLearner's capability ceiling

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q2`
> **Currency** · newest study 2026 · checked against its sources 2026-10-19 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2029: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Across all three tested interventions, each lever amplifies capabilities within K-5 exposure but provides limited gains in Beyond-K-5, so the pretraining filter sets the effective capability ceiling in the tested settings. [→ Fanfei Li 2026](#fanfei-li-2026)

## Evidence

### Fanfei Li 2026

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545 [doi:10.48550/arxiv.2608.13545](https://doi.org/10.48550/arxiv.2608.13545)

`q2 · i?` · `causal · r2`

Cross-intervention synthesis of the scaling (Figure 7), GRPO post-training (Figure 8), and ICL (Figure 9) experiments: each lever amplifies K-5 capability, scaling yields modest boundary gains, ICL does not unlock Beyond-K-5 reasoning, and post-training does not transfer even when trained on unrestricted data.

> "In each case, it is the pretraining filter, rather than the intervention, that sets the effective capability ceiling in our tested settings."

## Discussion


## Related Claims
- [GRPO post-training boosts in-scope K-5 capabilities but fails to recover Beyond-K-5 capabilities, even when post-trained on out-of-scope data](grpo-post-training-fails-beyond-k5.md) — a narrower finding that bears on this claim
- [In-context learning with few-shot examples and explanations does not unlock Beyond-K-5 reasoning for the 5B LittleLearner](icl-does-not-unlock-beyond-k5-reasoning.md) — a narrower finding that bears on this claim
- [LittleLearner's capabilities tightly track its controlled exposure: strong on in-scope tasks, degrading beyond the K-5 boundary](littlelearner-capabilities-track-controlled-exposure.md) — a narrower finding that bears on this claim
- [Scaling model size improves performance within K-5 and at the boundary but does not recover Beyond-K-5 performance](scaling-helps-in-scope-not-beyond-k5.md) — a narrower finding that bears on this claim
- [The multi-stage filtering pipeline reduces Beyond-K-5 retention to near zero while preserving a minority of K-5 content](k5-filter-pipeline-near-zero-beyond-k5-retention.md) — related
