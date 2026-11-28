---
type: claim
title: In vocabulary-app review logs, a successful recall lengthened memory half-life more when the review came at a lower recall probability, less as the memory strengthened, and less for harder words
description: Rules fitted to 220 million review logs from a vocabulary app show the spacing effect at item level (a recall at lower predicted recall probability multiplied half-life more), diminishing gains as half-life grows, smaller gains for harder words, and, after a failed recall, a new half-life that is longer for stronger memories and shorter the later the review.
id: recall-at-lower-probability-lengthens-half-life-more
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
    q: 2
    i: "?"
    n: 220 million review logs from 828 thousand app users
    kind: associational
    rigour: 2
---

# In vocabulary-app review logs, a successful recall lengthened memory half-life more when the review came at a lower recall probability, less as the memory strengthened, and less for harder words

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2` · n=220 million review logs from 828 thousand app users
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

These are the rules a scheduler uses to decide when to review an item again. Recall probability at the review falls as the gap since the last review grows, so a review at lower recall probability is a review after a longer gap relative to the memory's current strength (its half-life, the delay at which recall falls to one half).

## Subclaims
`q2 i?` In the rule fitted for a successful recall (eq. 12), the new half-life is the old one multiplied by a factor that grows as recall probability at the review falls (exponent 0.970 on one minus recall probability), which the authors read as the spacing effect. [→ Ye et al. 2022](#ye-et-al-2022)

`q2 i?` The same factor shrinks as the old half-life grows (exponent −0.127), so each successful review added proportionally less to an already strong memory, which the authors describe as a marginal effect. [→ Ye et al. 2022](#ye-et-al-2022)

`q2 i?` The factor also shrinks as word difficulty rises (exponent −0.534), and a failed recall raises the word's difficulty in the model, because forgotten words went on to have shorter half-lives after later successes. [→ Ye et al. 2022](#ye-et-al-2022)

`q2 i?` In the rule fitted for a failed recall (eq. 13), the new half-life is longer when the old half-life was longer (exponent 0.377) and shorter when the review came at lower recall probability (exponent −0.227 on one minus recall probability). [→ Ye et al. 2022](#ye-et-al-2022)

## Evidence

### Ye et al. 2022

Ye, J., Su, J., & Cao, Y. (2022). A stochastic shortest path algorithm for optimizing spaced repetition scheduling. In *Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '22)* (pp. 4381–4390). ACM. [doi:10.1145/3534678.3539081](https://doi.org/10.1145/3534678.3539081)

`q2 · observational log data, fitted model` · `i? · fitted exponents, no standardised effect size` · `n=220 million review logs from 828 thousand app users` · `associational · r2`

One month of review logs (220 million review events from 828 thousand users) from MaiMemo, an app for memorising English vocabulary, were grouped by word difficulty (ten levels, set by next-day recall after first learning) and review history, and a half-life was fitted to each group's forgetting curve. The authors observed that half-life rose after every successful recall, rose more the longer the gap before the review, and that words once forgotten later gained less from a successful recall; they built these into a state-transition model (DHP, eq. 8, p. 4384). The fitted rules (eqs. 12 and 13, p. 4387) are: after a recall, new half-life = old half-life × (e^3.81 · d^−0.534 · h^−0.127 · (1 − p)^0.970 + 1); after a failure, new half-life = e^−0.041 · d^−0.041 · h^0.377 · (1 − p)^−0.227, where d is difficulty, h the old half-life and p the recall probability at the review. The data are observational: the gaps were those learners took in the app, the paper does not report the learners' ages or other characteristics, and no held-out test of these rules is reported.

## Discussion

The rules restate, at the level of single items in a large app population, three things a [spaced repetition](../elements/spaced-repetition.md) schedule has to handle: a longer gap before a successful review strengthens memory more (the [spacing effect](../principles/spaced-learning.md), and the authors link it to "desirable difficulties"); the gain per review falls as an item is better known, so intervals can stretch; and harder items gain less and need more reviews. They are fitted associations from one app and one kind of material, not the result of assigned gaps, and they do not say at what point a gap becomes so long that the failures it causes outweigh the larger gain from success; the authors' scheduler handles that trade-off by weighing the cost of a failed review. The authors name learner characteristics and material beyond language learning as the next things to test.

## Related Claims
- [In vocabulary-app review logs, a memory model that tracks each item's review history predicted memory half-life after a review with less error than half-life regression](review-history-model-predicts-half-life-better-than-hlr.md) — the same model's prediction accuracy
- [In a simulation built on vocabulary-app review logs, a scheduler that minimises expected review time brought 6,000 words to a one-year half-life in fewer days than Anki-style, threshold and MEMORIZE schedules](cost-minimizing-scheduler-fewer-review-days-simulation.md) — the scheduler that uses these rules
- [Spaced retrieval practice produces better final retention than massed retrieval even though spacing lowers initial retrieval success, and more absolute spacing enhances long-term retention](spaced-retrieval-outperforms-massed-retrieval-despite-lower-initial-recall.md) — related: experimental evidence on longer spacing
- [Repeated retrieval practice alters the rate at which learned items are forgotten, according to learn-to-criterion studies and forgetting-curve analyses the chapter reviews](repeated-retrieval-alters-the-rate-of-forgetting.md) — related
- [Regression analysis shows the spacing effect holds in aggregate and the select group's advantage over other groups increases with number of reviews](spacing-effect-and-advantage-grows-with-reviews.md) — related: spacing in another app's logs
- [Retrieval difficulty, not criterion level per se, accounts for the memorial benefit of correct retrievals](retrieval-difficulty-not-criterion-level-drives-benefit.md) — related
