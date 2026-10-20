---
type: claim
title: The multi-stage filtering pipeline reduces Beyond-K-5 retention to near zero while preserving a minority of K-5 content
description: The multi-stage filtering pipeline reduces Beyond-K-5 retention to near zero while preserving a minority of K-5 content
id: k5-filter-pipeline-near-zero-beyond-k5-retention
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
    kind: design
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

# The multi-stage filtering pipeline reduces Beyond-K-5 retention to near zero while preserving a minority of K-5 content

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q2`

## Subclaims
`q2 i?` On the held-out CommonCoreText ground-truth set, the pipeline reduces Beyond-K-5 retention to 0% while preserving about 35% of K-5 documents. [→ Fanfei Li 2026](#fanfei-li-2026)
`q2 i?` On the external WeeBit corpus the filter retains 2.48% of 6,000 Beyond-K-5 passages, with genuinely out-of-scope concepts in only three passages (0.05%). [→ Fanfei Li 2026 (2)](#fanfei-li-2026-2)

## Evidence

### Fanfei Li 2026

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545 [doi:10.48550/arxiv.2608.13545](https://doi.org/10.48550/arxiv.2608.13545)

`q2 · i?` · `design · r2`

Validation of the filtering pipeline on CommonCoreText, a held-out ground-truth dataset of recommended reading materials and textbooks with grade-level labels. The pipeline achieves "the retention ofBeyond-K–5content to 0%" while preserving ~35% of K-5, a deliberate precision-over-recall design; removed K-5 passages were systematically longer and lexically more complex.

> "The pipeline successfully reduces the retention ofBeyond-K–5content to 0% while preserving ~35% ofK–5(Figure 2, left)."

### Fanfei Li 2026 (2)

Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, Wieland Brendel. (2026). LittleLearner: Language Models Under Pedagogically Controlled Knowledge Exposure. Preprint. https://arxiv.org/abs/2608.13545

`q2 · i?` · `causal · r2`

Independent leakage check applying the same pipeline to WeeBit, an external grade-labeled corpus. Retention of Beyond-K-5 passages was 2.48% of 6,000, and manual inspection attributed most retained content to web scraping artifacts, with genuinely out-of-scope concepts in only three passages (0.05%). A corpus-wide scan of 126 Beyond-K-5 n-grams found matches in only 0.09% of retained passages.

> "The filter retains 2.48% of 6,000Beyond-K–5passages; manual inspection identifies genuinely out-of-scope concepts in only three passages, corresponding to 0.05% of theBeyond-K–5split"

## Discussion


## Related Claims
- [GRPO post-training boosts in-scope K-5 capabilities but fails to recover Beyond-K-5 capabilities, even when post-trained on out-of-scope data](grpo-post-training-fails-beyond-k5.md) — related
- [LittleLearner's capabilities tightly track its controlled exposure: strong on in-scope tasks, degrading beyond the K-5 boundary](littlelearner-capabilities-track-controlled-exposure.md) — related
- [Across scaling, post-training, and in-context learning, the pretraining filter rather than the intervention sets LittleLearner's capability ceiling](pretraining-filter-sets-capability-ceiling.md) — related
- [Multi-layer defense significantly reduces bypass relative to regex-only filtering (69.65% to 46.34%), confirmed by exact McNemar test](multi-layer-beats-regex-only-bypass.md) — related
