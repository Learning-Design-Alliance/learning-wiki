---
type: claim
title: In a simulation built on vocabulary-app review logs, a cost-minimising review scheduler reached a target number of durable words in fewer days than other schedules under both a hand-built and a neural memory model
description: Simulating learners with two memory models fitted to 220 million vocabulary-app logs, a scheduler that minimises expected review time took 203 and 425 days to bring 2,000 words to a 360-day half-life, against 232 for MEMORIZE and 511 for reviewing at 90% recall, the best alternatives in each; on another group's dataset and memory model it matched a reinforcement-learning scheduler; no learners were tested.
id: cost-minimizing-scheduler-advantage-holds-across-memory-models
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-22
evidence_strength: weak
newest_evidence: 2023
sources:
  - id: su-et-al-2023
    resource: "https://doi.org/10.1109/TKDE.2023.3251721"
    title: "Su, J., Ye, J., Nie, L., Cao, Y., & Chen, Y. (2023). Optimizing spaced repetition schedule by capturing the dynamics of memory. *IEEE Transactions on Knowledge and Data Engineering, 35*(10), 10085–10097. [doi:10.1109/TKDE.2023.3251721](https://doi.org/10.1109/TKDE.2023.3251721)"
    author: "Su, J., Ye, J., Nie, L., Cao, Y., & Chen, Y."
    q: 1
    i: "?"
    n: simulation only; no learners tested
    kind: design
    rigour: 2
---

# In a simulation built on vocabulary-app review logs, a cost-minimising review scheduler reached a target number of durable words in fewer days than other schedules under both a hand-built and a neural memory model

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1` · n=simulation only; no learners tested
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person

This bears on choosing the rule an adaptive [spaced repetition](../elements/spaced-repetition.md) tool uses to set each item's next review. The simulated learners follow memory models fitted to app logs; no learners were given the schedules.

## Subclaims
`q1 i?` With a 360-day target half-life, a 600-second daily limit, 3 s per successful and 9 s per failed review and 1,000 simulated days, the cost-minimising scheduler (SSP-MMC) took 203 days to bring 2,000 words to the target under the hand-built DHP-HLR model, against 232 for MEMORIZE, 239 for reviewing at 90% recall and 244 for an Anki variant, and 425 days under the neural GRU-HLR model, against 511, 611 and 982 for the 90% threshold, Anki variant and MEMORIZE; the authors report savings of about 12.5% and 16.8% over the best alternatives. [→ Su et al. 2023](#su-et-al-2023)

`q1 i?` The scheduler also reached the target for the most words over the run (12,364 under DHP-HLR and 6,742 under GRU-HLR) and led on summed recall probability and on words learned. [→ Su et al. 2023](#su-et-al-2023)

`q1 i?` Under both memory models its optimal interval first lengthened and then shortened as an item's half-life grew, with the recall probability at review rising towards 100% near the target. [→ Su et al. 2023](#su-et-al-2023)

`q1 i?` Ported to another group's dataset and memory model, it matched a reinforcement-learning scheduler (TPPRL) on recall at equal review cost and trained in seconds rather than at least an hour. [→ Su et al. 2023](#su-et-al-2023)

## Evidence

### Su et al. 2023

Su, J., Ye, J., Nie, L., Cao, Y., & Chen, Y. (2023). Optimizing spaced repetition schedule by capturing the dynamics of memory. *IEEE Transactions on Knowledge and Data Engineering, 35*(10), 10085–10097. [doi:10.1109/TKDE.2023.3251721](https://doi.org/10.1109/TKDE.2023.3251721)

`q1 · simulation with fitted memory models` · `i? · days to a target count, no standardised effect size` · `n=simulation only; no learners tested` · `design · r2`

The authors framed scheduling as a stochastic shortest path problem: choose each review interval to minimise the expected review time an item needs to reach a target half-life, with a failed review costing more than a successful one, and solved it by value iteration over the states of a memory model (section 4). They simulated learners with two models fitted to 220 million review logs from the MaiMemo English-vocabulary app, the hand-built DHP-HLR and the neural GRU-HLR, and compared the scheduler with random intervals, an Anki (SM-2) variant, reviewing at the current half-life, reviewing at 90% recall and MEMORIZE (section 5.3, Table 5, Fig. 10). Days to bring 2,000 words to the target were 203, 239, 244, 706, 232 and 399 under DHP-HLR, and 425, 511, 611, not reached, 982 and 902 under GRU-HLR, in the order scheduler, 90% threshold, Anki variant, half-life, MEMORIZE, random. They also ran it on the dataset and half-life-regression student model of a published reinforcement-learning scheduler (section 5.5, Fig. 13). The authors note that the main metric is the quantity the scheduler optimises. Numbers were read from the authors' accepted manuscript; the published version is cited.

## Discussion

Every comparison takes place inside a fitted model of memory, so the scheduler optimised on that model has a built-in advantage, and the size of the gain depends on how well the model describes real learners; neither this article nor its conference version reports schedules tested with learners. What this extension adds is that the lead held under a second, neural memory model and on another group's data. This article extends the authors' conference paper (Ye, Su & Cao, 2022, doi:10.1145/3534678.3539081), which ran the same simulation with one memory model on logs from the same app, so the two are not independent evidence.

## Related Claims
- [In cross-validated vocabulary-app review logs, memory models that use each item's sequence of past recall probabilities and review gaps predicted recall with about a third of half-life regression's error](review-history-features-cut-recall-prediction-error.md) — the memory models the simulation uses
- [Review scheduled by a model of each student's memory improved end-of-semester retention in a middle-school language course more than massed or uniformly spaced review of the same duration](personalized-spaced-review-improves-course-retention.md) — related: model-based scheduling tested with learners
- [In simulations, adaptive model-based scheduling at OETs of 0.8 or higher produced 39–55% better final-test memory than the next best conventional schedule](simulation-oet-above-08-beats-conventional.md) — related: another simulation of model-based scheduling
- [ML-optimized item selection helps learners retain content 67% longer than a difficulty-based selection heuristic after controlling for study length and frequency](select-ml-item-selection-67-percent-longer-retention.md) — related: a model-based scheduler tested with app learners
