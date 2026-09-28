---
type: element
id: spaced-repetition
title: Spaced Repetition
description: Spaced repetition is the element in which key material is revisited at strategically increasing intervals rather than massed into a single session.
status: review
generated:
  by: codex/unspecified
  at: 2026-04-08
sources:
  - id: cepeda-2006
    resource: "https://doi.org/10.1037/0033-2909.132.3.354"
    title: "Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354-380"
    author: "Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D"
---

# Spaced Repetition

> **Element** · [All elements](index.md)
> **Evidence** · 13 claims (12 for, 1 mixed) · 12 studies (5 causal, 4 quant-synthesis, 2 review, 1 theoretical), `q1`–`q4` · 3 of 12 report an effect size · 7 claims rest on one study

## Description
Spaced repetition is the element in which key material is revisited at strategically increasing intervals rather than massed into a single session. It is useful when the aim is durable retention rather than short-term performance.

## Design Implications

### Context
#### Requirements
- **A schedule for revisiting important material**
- **Prompts that require recall, recognition, or use**
#### Constraints
- **Spacing without retrieval is less powerful than spacing with active recall**

### Target Learning Goals
- Strengthen long-term retention and access to important knowledge.

### Affordances
- [Spaced Learning](../principles/spaced-learning.md)
- [Memory Consolidation](../principles/memory-consolidation.md)
- [Retrieval Practice](../principles/retrieval-practice.md)

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [Spaced Repetition Improves Retention](../claims/spaced-repetition-improves-retention.md) [+S]
- [Distributed Practice Improves Retention](../claims/distributed-practice-improves-retention.md) [+M]
- [Learners Misjudge Spacing Benefits](../claims/learners-misjudge-spacing-benefits.md) [+M]
- [Spaced Practice Improves Retention](../claims/spaced-practice-improves-retention.md) [+M]
- [Spaced Retrieval Improves Retention](../claims/spaced-retrieval-improves-retention.md) [+W]
- [Under the mean-recall approximation, the optimal Leitner Queue Network schedule increases the expected delay between reviews as an item moves up through the decks.](../claims/optimal-leitner-schedule-expands-intervals-between-reviews.md) [+W]
- [Spaced retrieval practice produces better final retention than massed retrieval even though spacing lowers initial retrieval success, and more absolute spacing enhances long-term retention](../claims/spaced-retrieval-outperforms-massed-retrieval-despite-lower-initial-recall.md) [+W]
- [Expanding retrieval schedules have not shown consistent advantages over equally spaced or contracting schedules matched on total spacing](../claims/expanding-retrieval-schedules-are-not-superior-to-equal-or-contracting-schedules.md) [+M]
- [Distributed practice benefits L2 learning, and one review argues that spreading it over years can be worse than over months](../claims/distributed-practice-limits-l2.md) [~M]
- [Supplemental computer-based spaced repetition activities nearly triple long-term vocabulary retention in EFL students compared with conventional instruction alone](../claims/spaced-repetition-supplement-triples-vocabulary-retention.md) [+M]
- [Under the Leitner Queue Network optimization, easy items call for roughly uniform time across decks, while more difficult items call for more time on lower decks.](../claims/optimal-leitner-deck-allocation-depends-on-item-difficulty.md) [+W]
- [Retrieval practice effects become more robust as initial retrieval success increases, especially above 75%, while retrieval made too easy yields smaller effects](../claims/retrieval-practice-effects-more-robust-when-initial-retrieval-success-exceeds-75-percent.md) [+M]
- [Under the mean-recall approximation, the optimal Leitner Queue Network review schedule spends more time on lower decks than on higher decks.](../claims/optimal-leitner-schedule-reviews-lower-decks-more-often.md) [+W]

## Design Decisions
<!-- Decision section (2026-09-30 pilot): drafted from the linked claim pages only; every choice
     cites the claims that settle it, with markers capped by each claim's recorded evidence. -->

### Should review be spread across sessions or done in one block?
- **Default:** spread the same study time over several sessions separated by days rather than one block; across 271 comparisons in verbal recall, spacing raised final recall from 36.7% to 47.3% at equal study time — [Distributed Practice Improves Retention](../claims/distributed-practice-improves-retention.md) [+S], [Spaced Practice Improves Retention](../claims/spaced-practice-improves-retention.md) [+S]
- **Changes when:** the task is a complex or motor skill rather than verbal recall → expect a smaller benefit; a meta-analysis across task types put the effect at d = 0.46 and found it smaller for complex tasks — [Spaced Repetition Improves Retention](../claims/spaced-repetition-improves-retention.md) [~S]
- **Changes when:** only an immediate test matters → spacing's advantage is uneven at short delays and shows mainly on delayed tests, so judge the schedule on a delayed test — [Distributed Practice Improves Retention](../claims/distributed-practice-improves-retention.md) [~S]
- **Tested with:** mostly young adults on verbal material (714 of 839 performance differences in Cepeda et al. 2006), an online adult panel learning trivia facts, and L2 learners in 48 experiments.
- **Not settled:** the evidence for children's long-term retention is thin (the Cepeda synthesis says it "cannot say for certain"); no wiki claim sizes the benefit for multi-step procedures.

### How long should the gap between reviews be?
- **Default:** set the gap from how long the material must be remembered: the best gap was about 20% of the test delay for a test a few weeks away, falling to about 5% for a one-year delay; there is an optimum, not "longer is always better" — [Spaced Practice Improves Retention](../claims/spaced-practice-improves-retention.md) [+S], [Distributed Practice Improves Retention](../claims/distributed-practice-improves-retention.md) [+S]
- **Changes when:** second-language learning with a delayed test → longer spacing beat shorter spacing on delayed posttests, but was no better on immediate ones — [Spaced Practice Improves Retention](../claims/spaced-practice-improves-retention.md) [+S]
- **Changes when:** practice would be spread over years → one narrative review reports that spreading over a couple of years may be worse than over a couple of months — [Distributed practice benefits L2 learning, and one review argues that spreading it over years can be worse than over months](../claims/distributed-practice-limits-l2.md) [~M]
- **Tested with:** 1,354 adults learning trivia facts with tests up to a year later (Cepeda et al. 2008); L2 vocabulary experiments.
- **Not settled:** the d = 1.1 for the best gap compares the post hoc best gap with a zero gap, so it is an upper bound for any single schedule; the gaps used in the L2 meta-analysis are not given on the claim pages, and the years-versus-months limit rests on one review of two studies.

### Should intervals expand, or stay equal?
- **Default:** do not rely on an expanding schedule for extra benefit; equal and expanding spacing were statistically equivalent in 48 L2 experiments, and expanding against uniform spacing of retrieval gave g = 0.034 — [Expanding retrieval schedules have not shown consistent advantages over equally spaced or contracting schedules matched on total spacing](../claims/expanding-retrieval-schedules-are-not-superior-to-equal-or-contracting-schedules.md) [+M], [Spaced Retrieval Improves Retention](../claims/spaced-retrieval-improves-retention.md) [+M]
- **Changes when:** a single L2 vocabulary study (128 Japanese college students) found a limited but significant advantage for expanding spacing, with the amount of spacing mattering more than its shape — [Expanding retrieval schedules have not shown consistent advantages over equally spaced or contracting schedules matched on total spacing](../claims/expanding-retrieval-schedules-are-not-superior-to-equal-or-contracting-schedules.md) [~M]
- **Changes when:** an item-level scheduler (Leitner decks) is used → a scheduling model's optimum lengthens the delay as an item moves up the decks, a model result rather than a test with learners — [Under the mean-recall approximation, the optimal Leitner Queue Network schedule increases the expected delay between reviews as an item moves up through the decks.](../claims/optimal-leitner-schedule-expands-intervals-between-reviews.md) [~W]
- **Tested with:** lab word pairs and vocabulary, Japanese college students learning English words, second-language experiments.
- **Not settled:** the L2 meta-analysis's abstract does not say whether its expanding and equal conditions were matched on total spacing.

### What should happen at each review: recall or rereading?
- **Default:** make each review a retrieval attempt, and space those attempts rather than repeating them back to back; spaced beat massed retrieval practice at g = 0.74 across 29 studies — [Spaced Retrieval Improves Retention](../claims/spaced-retrieval-improves-retention.md) [+M]
- **Changes when:** retrievals are repeated within one sitting → massed repeated retrieval gave no benefit over dropping an item after one recall on a one-week test, while more total spacing across trials helped — [Spaced retrieval practice produces better final retention than massed retrieval even though spacing lowers initial retrieval success, and more absolute spacing enhances long-term retention](../claims/spaced-retrieval-outperforms-massed-retrieval-despite-lower-initial-recall.md) [+M]
- **Changes when:** gaps make recall fail often → effects are more robust when initial retrieval succeeds, especially above 75%; expect spacing to cut recall during practice (by about 25% in one experiment) and do not read that drop as failure — [Retrieval practice effects become more robust as initial retrieval success increases, especially above 75%, while retrieval made too easy yields smaller effects](../claims/retrieval-practice-effects-more-robust-when-initial-retrieval-success-exceeds-75-percent.md) [~M], [Spaced retrieval practice produces better final retention than massed retrieval even though spacing lowers initial retrieval success, and more absolute spacing enhances long-term retention](../claims/spaced-retrieval-outperforms-massed-retrieval-despite-lower-initial-recall.md) [~M]
- **Tested with:** the 29 studies of the Latimier et al. meta-analysis; lab vocabulary and word-pair experiments reported in one review chapter.
- **Not settled:** Latimier et al. compare spaced with massed retrieval, not spaced retrieval with spaced rereading, so no claim here sizes that contrast.

### Who sets the schedule: the learner or the system?
- **Default:** build the schedule into the course or tool rather than leaving it to learners; spacing beat massing for 90% of participants in a flashcard study, yet 72% judged massing more effective — [Learners Misjudge Spacing Benefits](../claims/learners-misjudge-spacing-benefits.md) [+S]
- **Changes when:** a computer-based spaced-repetition system can supplement class → items practised in the system were credited on a delayed test at almost three times the rate of items taught only in class (50.1% vs 16.9%), in one study of 22 cadets — [Supplemental computer-based spaced repetition activities nearly triple long-term vocabulary retention in EFL students compared with conventional instruction alone](../claims/spaced-repetition-supplement-triples-vocabulary-retention.md) [+M]
- **Tested with:** undergraduate lab studies of painting-style induction and GRE-type vocabulary; EFL cadets.
- **Not settled:** whether teaching learners about the spacing effect changes their own scheduling; the claim pages say so only in Discussion, with no study recorded.

### Should harder items get more reviews?
- **Default:** give harder items more review time on the lower (less-known) decks; for easy items spread time roughly evenly — [Under the Leitner Queue Network optimization, easy items call for roughly uniform time across decks, while more difficult items call for more time on lower decks.](../claims/optimal-leitner-deck-allocation-depends-on-item-difficulty.md) [+W], [Under the mean-recall approximation, the optimal Leitner Queue Network review schedule spends more time on lower decks than on higher decks.](../claims/optimal-leitner-schedule-reviews-lower-decks-more-often.md) [+W]
- **Tested with:** a scheduling model's optimisation only (Reddy et al. 2016); no learners.
- **Not settled:** no wiki claim tests item-level allocation with learners, and none compares adaptive with fixed schedules.

## Related Elements
- [Continuous Review](continuous-review.md)
- [Retrieval Practice](retrieval-practice.md)

## Patterns That Use This Element
- [Spaced Learning](../patterns/spaced-learning.md)
- [Mastery Learning](../patterns/mastery-learning.md)

## Examples
- Recurrent low-stakes review of vocabulary or formulas at increasing intervals.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354-380. [https://doi.org/10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
