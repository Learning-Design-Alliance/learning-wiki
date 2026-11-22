---
type: claim
title: In a simulation built on vocabulary-app review logs, a scheduler that minimises expected review time brought 6,000 words to a one-year half-life in fewer days than Anki-style, threshold and MEMORIZE schedules
description: In a 1,000-day simulation with a 10-minute daily limit, using a memory model fitted to vocabulary-app logs, a review scheduler solved as a stochastic shortest path problem reached 6,000 words at a 360-day half-life in 466 days, against 533 for reviewing at 90% recall, 569 for an Anki variant and 793 for MEMORIZE; no learners were tested.
id: cost-minimizing-scheduler-fewer-review-days-simulation
status: review
generated:
  by: "process:article-ingest"
  at: 2026-11-22
evidence_strength: weak
newest_evidence: 2022
sources:
  - id: ye-et-al-2022
    resource: "https://doi.org/10.1145/3534678.3539081"
    title: "Ye, J., Su, J., & Cao, Y. (2022). A stochastic shortest path algorithm for optimizing spaced repetition scheduling. In *Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '22)* (pp. 4381–4390). ACM. [doi:10.1145/3534678.3539081](https://doi.org/10.1145/3534678.3539081)"
    author: "Ye, J., Su, J., & Cao, Y."
    q: 1
    i: "?"
    n: simulation only; no learners tested
    kind: design
    rigour: 2
---

# In a simulation built on vocabulary-app review logs, a scheduler that minimises expected review time brought 6,000 words to a one-year half-life in fewer days than Anki-style, threshold and MEMORIZE schedules

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1` · n=simulation only; no learners tested
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

This bears on choosing the rule an adaptive [spaced repetition](../elements/spaced-repetition.md) tool uses to set each item's next review. The result is a simulation in which the simulated learners follow a memory model fitted to app logs; no learners were given the schedules.

## Subclaims
`q1 i?` With a 360-day target half-life, a 600-second daily study limit, 3 s per successful and 9 s per failed review and a 1,000-day horizon, the cost-minimising scheduler (SSP-MMC) took 466 days to bring 6,000 words to the target, against 533 days for reviewing when recall probability falls to 90%, 569 for an Anki (SM-2) variant and 793 for MEMORIZE, which the authors report as 12.6% less review time than the threshold schedule. [→ Ye et al. 2022](#ye-et-al-2022)

`q1 i?` The scheduler also led on the summed recall probability of learned words and, after an early period in which a random schedule learned more new words by neglecting review, on the number of words learned. [→ Ye et al. 2022](#ye-et-al-2022)

`q1 i?` Its optimal policy scheduled reviews at lower recall probability while an item's half-life was short, with the recall probability at review rising towards 100% as the half-life approached the target, so the interval first lengthened and then shortened; at the same half-life it gave easier words shorter intervals than harder ones, to avoid failures that would raise their difficulty. [→ Ye et al. 2022](#ye-et-al-2022)

## Evidence

### Ye et al. 2022

Ye, J., Su, J., & Cao, Y. (2022). A stochastic shortest path algorithm for optimizing spaced repetition scheduling. In *Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '22)* (pp. 4381–4390). ACM. [doi:10.1145/3534678.3539081](https://doi.org/10.1145/3534678.3539081)

`q1 · simulation with a fitted memory model` · `i? · days to a target count, no standardised effect size` · `n=simulation only; no learners tested` · `design · r2`

The authors framed scheduling as a stochastic shortest path problem: choose each review interval to minimise the expected review time an item needs to reach a target half-life, with a successful review costing less time than a failed one, and solved it by dynamic programming over the states of a memory model (DHP) fitted to one month of logs (220 million review events from 828 thousand users) from the MaiMemo English-vocabulary app. In a simulation that used the same fitted model as the learner, they compared the scheduler with random intervals, an Anki (SM-2) variant, reviewing at the current half-life, reviewing when recall probability falls to 90%, and MEMORIZE (Tabibian et al., 2019) (section 5.3, Figure 10, pp. 4388–4389). Days to bring 6,000 words to a 360-day half-life were 466 for the scheduler, 533 for the 90% threshold, 569 for the Anki variant and 793 for MEMORIZE. The authors note that the main metric is the quantity the scheduler optimises, so its lead there is expected, and that the scheduler was deployed in the MaiMemo app (Appendix A), for which the paper reports no learner outcomes.

## Discussion

The comparison is between scheduling rules inside one fitted model of memory, so the scheduler optimised on that model has a built-in advantage, and the size of the gain depends on how well the model describes real learners; the paper does not test the schedules with learners. Two choices in it carry over to design regardless: the goal is set as reaching a durable memory at least total review time, with failed reviews costed higher than successful ones, and the resulting policy lets recall probability at review be low early and high late, rather than reviewing at a fixed recall level. The same authors' journal extension repeats the simulation with a second, neural memory model.

## Related Claims
- [In vocabulary-app review logs, a successful recall lengthened memory half-life more when the review came at a lower recall probability, less as the memory strengthened, and less for harder words](recall-at-lower-probability-lengthens-half-life-more.md) — the memory rules the simulation uses
- [In vocabulary-app review logs, a memory model that tracks each item's review history predicted memory half-life after a review with less error than half-life regression](review-history-model-predicts-half-life-better-than-hlr.md) — the memory model's accuracy
- [Review scheduled by a model of each student's memory improved end-of-semester retention in a middle-school language course more than massed or uniformly spaced review of the same duration](personalized-spaced-review-improves-course-retention.md) — related: model-based scheduling tested with learners
- [In simulations, adaptive model-based scheduling at OETs of 0.8 or higher produced 39–55% better final-test memory than the next best conventional schedule](simulation-oet-above-08-beats-conventional.md) — related: another simulation of model-based scheduling
- [Under the mean-recall approximation, the optimal Leitner Queue Network schedule increases the expected delay between reviews as an item moves up through the decks.](optimal-leitner-schedule-expands-intervals-between-reviews.md) — related: an optimised schedule from a different model
