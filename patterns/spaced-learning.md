---
type: pattern
id: spaced-learning
title: Spaced Learning
description: A reusable sequence of repeated encounters whose gap and activity are selected for a target retention horizon, with outcomes checked at that horizon.
status: review
generated:
  by: codex/unspecified
  at: 2026-04-08
grain_size: course
---

# Spaced Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 9 claims (7 for, 2 mixed) · 11 studies (6 causal, 4 quant-synthesis, 1 review), `q2`–`q4` · 3 of 11 report an effect size · 5 claims rest on one study

## Description
Spaced learning is a reusable way to distribute repeated encounters with the same material. The designer chooses the gap relative to when learners must perform, and separately chooses whether each encounter is study, retrieval, or application.

## Design

### Elements Used
- [Spaced Repetition](../elements/spaced-repetition.md)
- [Retrieval Practice](../elements/retrieval-practice.md)

### Sequence and Adaptation

1. Define the target material and an observable final performance: factual recall, application, or another outcome. State when it will be measured.
2. Arrange an initial encounter and a later encounter with a recorded gap. The gap may be measured in intervening trials within a session or in calendar days between sessions; these are different interventions.
3. Decide separately what learners do at each encounter: study, recall, apply, or receive feedback. Record successes and failures when retrieval is used.
4. Check performance at the chosen horizon and revise the gap if observed retention is poor. The cited studies do not provide a universal schedule or an individual adaptation threshold.

### Prediction Contract

**State and target.** For the specific material and learner, record current success on a representative recall or application task, the study/retrieval/feedback at each encounter, the gap in its actual units, and the intended final-test delay. State a measurable target (for example, a chosen proportion correct on a named assessment at a named time). Record whether that delayed goal matters to the learner when known; a course's target and the learner's own goal need not coincide. The cited spacing comparisons did not measure the learner's valuation of the goal, starting performance for a new design, an individual optimum, or a universal target criterion. If any input is absent, report it as unknown rather than turning a pooled effect into an individual forecast. A retrieval response is an observation bearing on learning state, not a direct readout of that state.

| Conditional forecast from recorded evidence | Response and next-action hypothesis to test locally | Diagnostic alternatives if the target is missed |
|---|---|---|
| For verbal facts, increasing the review gap can first improve and then reduce final recall at a *fixed* test delay. In Cepeda et al. (2008), the gap associated with best performance grew as the delay grew, but fell as a share of it (about 5–10% at a one-year test in that study) — [distributed practice claim](../claims/distributed-practice-improves-retention.md) [~M]. This is a source-bounded group pattern, not a day-level prescription for a learner. | Observe performance at the later encounter and at the intended final horizon. If retrieval fails at the encounter, test shorter gaps or added support on later items; if practice succeeds but final recall falls short, compare candidate gaps while holding material, feedback, and target horizon as constant as feasible. These are proposed local design tests, not adaptation thresholds validated by the cited study. | A failed later encounter may reflect weak initial encoding, a long gap, or missing feedback. Good practice followed by poor final recall may reflect an ill-matched gap or an assessment with different demands. Record initial performance, intermediate retrieval and final outcome to distinguish these possibilities; a final score alone does not. |
| After one correct recall of foreign-word pairs, three additional tests spread across more intervening trials improved one-week recall in Karpicke and Bauernschmidt (2011), while expanding versus equal versus contracting schedules at matched total spacing were not detectably different — [total/relative retrieval claim](../claims/total-retrieval-spacing-beats-massed-but-relative-schedule-not-distinguished.md) [~M]. No equivalence or calendar-day inference follows. | Record correctness and latency at each retrieval separately from one-week cued recall. A different latency slope under an expanding schedule is an intermediate observation, not evidence to prefer that schedule for final retention. If retrieval fails, support or feedback is a separately configured action to evaluate. | If final recall differs, check whether total intervening trials, initial retrieval success, feedback, or the final-test delay differed before attributing it to relative schedule. Latency can indicate effort without showing that difficulty caused the final outcome. |

### Context

- **Target goals:** durable recall is best supported for verbal materials; a smaller classroom study includes factual and rephrased application questions.
- **Target learners:** the cited tests include undergraduate word-pair and science-lecture learners; the broader verbal-recall synthesis samples other ages and tasks but does not establish every use case.
- **Requirements:** repeated contact with a common target, an explicit gap, and a specified test delay.
- **Constraints:** immediate practice fluency cannot substitute for delayed outcome measurement. A gap that helps one test horizon may not be best for another; the same-gap comparison does not isolate retrieval or feedback.

## Claims
- [Spaced Repetition Improves Retention](../claims/spaced-repetition-improves-retention.md) [+S]
- [Spaced Retrieval Improves Retention](../claims/spaced-retrieval-improves-retention.md) [+M]
- [Learners Misjudge Spacing Benefits](../claims/learners-misjudge-spacing-benefits.md) [+M]
- [Spaced Practice Improves Retention](../claims/spaced-practice-improves-retention.md) [+S]
- [Distributed Practice Improves Retention](../claims/distributed-practice-improves-retention.md) [+M]
- [Spaced Retrieval Outperforms Restudy](../claims/spaced-retrieval-outperforms-restudy.md) [+M]
- [Spaced retrieval practice produces better final retention than massed retrieval even though spacing lowers initial retrieval success, and more absolute spacing enhances long-term retention](../claims/spaced-retrieval-outperforms-massed-retrieval-despite-lower-initial-recall.md) [+W]
- [Total retrieval spacing improved one-week vocabulary recall while relative schedules were not distinguished](../claims/total-retrieval-spacing-beats-massed-but-relative-schedule-not-distinguished.md) [~M]
- [Eight-day review improved a five-week science test versus one-day review in a simulated university classroom](../claims/eight-day-review-improves-five-week-science-test-versus-one-day-review.md) [~M]

## Design Decisions

### Should encounters be distributed when the final test is soon?
- **Default:** for equal-time verbal study, distribute encounters even when a final recall test is very soon; Cepeda et al.'s synthesis found an aggregate spaced advantage in the under-one-minute band — [distributed practice claim](../claims/distributed-practice-improves-retention.md) [+S].
- **Changes when:** the task is not verbal recall or the relevant outcome is immediate execution of a complex skill → measure that outcome rather than transporting the synthesis.
- **Tested with:** pooled verbal-recall experiments at several retention intervals.
- **Not settled:** the pooled result does not guarantee a gain in every individual experiment or make active retrieval a requirement for spacing.

### How much time should separate study encounters?
- **Default:** choose a gap in relation to the intended test delay; across verbal-recall studies the gap giving maximum final retention tended to grow with the retention interval — [distributed practice claim](../claims/distributed-practice-improves-retention.md) [~M].
- **Changes when:** a classroom review is planned with a five-week outcome → in one simulated undergraduate science lecture, review after eight days outperformed review after one day — [classroom-gap claim](../claims/eight-day-review-improves-five-week-science-test-versus-one-day-review.md) [~M].
- **Tested with:** a broad but unevenly sampled verbal-memory literature and one N=169 simulated science classroom.
- **Not settled:** neither the synthesis nor the two-gap experiment validates a fixed days-to-weeks schedule for all learners and subjects. Many long-gap/test-delay combinations were sparse.

### Is a retrieval schedule with expanding intervals better than an equal one?
- **Default:** do not assume expansion is inherently better. A review of study schedules found conflicting results; a foreign-word retrieval experiment found no detectable one-week recall difference among expanding, equal, and contracting schedules when total intervening trials were matched — [total/relative retrieval claim](../claims/total-retrieval-spacing-beats-massed-but-relative-schedule-not-distinguished.md) [~M].
- **Changes when:** more total spacing is feasible after the item has first been recalled → in that experiment, 15, 30, and 90 intervening trials yielded 49%, 64%, and 75% final recall, respectively — [total/relative retrieval claim](../claims/total-retrieval-spacing-beats-massed-but-relative-schedule-not-distinguished.md) [~M].
- **Tested with:** 96 undergraduate learners of Swahili–English pairs, using trial lags within a learning session and a one-week final test.
- **Not settled:** a null relative-schedule result does not establish equivalence, and these trial counts are not calendar-day prescriptions.

### Is difficult retrieval the observed reason a schedule helps?
- **Default:** record practice retrieval success and latency as intermediate observations, then measure final performance separately. Expanding schedules changed response-time slopes at some total gaps but did not improve final recall in the experiment — [total/relative retrieval claim](../claims/total-retrieval-spacing-beats-massed-but-relative-schedule-not-distinguished.md) [~M].
- **Changes when:** a learner cannot retrieve → add support or feedback as a distinct design choice and test its effect; the spacing-only comparison does not identify that contribution.
- **Tested with:** the same word-pair experiment, after an initial correct retrieval.
- **Not settled:** response latency is a proxy for difficulty, not proof that difficulty caused durable learning.

### Does delayed review improve application as well as facts?
- **Default:** in a similar simulated lecture with a five-week test, consider a longer review gap: eight days beat one day for factual questions (.54 vs .47; p=.02) and rephrased application questions (.42 vs .35; p=.03) in the primary analysis — [classroom-gap claim](../claims/eight-day-review-improves-five-week-science-test-versus-one-day-review.md) [~M].
- **Changes when:** the inference must survive a stricter analysis → the factual difference persisted, while application was marginal (p=.06) when counting only initially correct items — [classroom-gap claim](../claims/eight-day-review-improves-five-week-science-test-versus-one-day-review.md) [~M].
- **Tested with:** meteorology material and 169 analyzed undergraduates; the final test was 35 days after each group's review.
- **Not settled:** far transfer, an authentic ongoing course, and an isolated spacing effect without retrieval or feedback.

## Related Patterns
- [Game-Based Mastery Learning](game-based-mastery-learning.md)

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354-380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
