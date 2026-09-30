---
type: principle
id: spaced-learning
title: Spaced Learning
description: Spaced learning distributes study or practice across multiple sessions separated by intervals of time, rather than concentrating the same total effort into a single block.
status: review
generated:
  by: claude/unspecified
  at: 2026-04-06
sources:
  - id: benjamin-2010
    resource: "https://doi.org/10.1016/j.cogpsych.2010.05.004"
    title: "Benjamin, A. S., & Tullis, J. (2010). What makes distributed practice effective? *Cognitive Psychology, 61*(3), 228–247"
    author: "Benjamin, A. S., & Tullis, J"
  - id: carpenter-2012
    resource: "https://doi.org/10.1177/0963721412452728"
    title: "Carpenter, S. K. (2012). Testing enhances the transfer of learning. *Current Directions in Psychological Science, 21*(5), 369–373"
    author: Carpenter, S. K
  - id: kapler-2015
    resource: "https://doi.org/10.1016/j.learninstruc.2014.11.001"
    title: "Kapler, I. V., Weston, T., & Wiseheart, M. (2015). Spacing in a simulated undergraduate classroom: Long-term benefits for factual and higher-level learning. *Learning and Instruction, 36*, 38–45"
    author: "Kapler, I. V., Weston, T., & Wiseheart, M"
  - id: karpicke-2011
    resource: "https://doi.org/10.1037/a0023436"
    title: "Karpicke, J. D., & Bauernschmidt, A. (2011). Spaced retrieval: Absolute spacing enhances learning regardless of relative spacing. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 37*(5), 1250–1257"
    author: "Karpicke, J. D., & Bauernschmidt, A"
  - id: logan-2012
    resource: "https://doi.org/10.1007/s11409-012-9090-3"
    title: "Logan, J. M., Castel, A. D., Haber, S., & Viehman, E. J. (2012). Metacognition and the spacing effect: The role of repetition, feedback, and instruction on judgments of learning for massed and spaced rehearsal. *Metacognition and Learning, 7*(3), 175–195"
    author: "Logan, J. M., Castel, A. D., Haber, S., & Viehman, E. J"
---

# Spaced Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 6 claims (2 for, 4 mixed) · 11 studies (5 causal, 4 review, 1 quant-synthesis, 1 theoretical), `q2`–`q4` · 0 of 11 report an effect size · 2 claims rest on one study

## Description
Spaced learning distributes repeated encounters with material over time. For verbal recall, equal-time spaced study often improves final recall over massed study; the size and best gap depend on when the final test occurs. Evidence for complex skills and transfer must be assessed separately from this verbal-memory result.

## Implications

Spacing and retrieval are distinct manipulations. Across 271 massed-versus-spaced verbal-recall comparisons with equal study time, mean final accuracy was 36.7% and 47.3%, respectively; the synthesis found an aggregate spacing advantage even with final tests under one minute [Distributed Practice Improves Retention](../claims/distributed-practice-improves-retention.md) [+S]. A separate retrieval experiment found that total intervening trials between successful recalls mattered for a one-week test, while the shape of the schedule did not distinguish the tested groups [Total retrieval spacing and relative schedules](../claims/total-retrieval-spacing-beats-massed-but-relative-schedule-not-distinguished.md) [~M]. These observations do not require that every spaced encounter be a quiz. Retrieval and feedback can be useful additions, but their contribution cannot be read off a spacing-only comparison.

### Conditional Model

**Proposed relationship.** Given repeated encounters with material and a desired final-test horizon, the gap between encounters changes the probability of later successful performance. The best-supported outcome here is verbal recall. Study-phase retrieval and reconstruction of a partially forgotten trace are candidate explanations, not observed states established by a final score alone.

| Condition and observed contrast | Outcome and uncertainty | Design implication |
|---|---|---|
| Equal-time verbal study: massed versus distributed episodes | Spacing increased aggregate final recall in Cepeda et al. (2006), including the very-short test band; the synthesis is not a universal effect for complex skill transfer [Distributed Practice Improves Retention](../claims/distributed-practice-improves-retention.md) [+S]. | Distribute repeated encounters for durable verbal recall. Do not use an untested assertion that massing wins whenever assessment is immediate. |
| Target retention interval changes | In the synthesis, the gap that maximized recall tended to grow as the test delay grew, but long-delay combinations were sparse [Distributed Practice Improves Retention](../claims/distributed-practice-improves-retention.md) [~M]. | Specify the final-test horizon before tuning a gap. A calendar-day rule without that horizon is underidentified. |
| Three additional retrievals after first correct recall of foreign-word pairs | At one week, total spacing of 15, 30, or 90 intervening trials corresponded to 49%, 64%, and 75% recall; expanding, equal, and contracting schedules matched on total spacing did not differ detectably [Total retrieval spacing and relative schedules](../claims/total-retrieval-spacing-beats-massed-but-relative-schedule-not-distinguished.md) [~M]. | Preserve the distinction between **how much spacing** and **the schedule's shape**. No detected difference is not equivalence. |
| Simulated undergraduate science lecture, one versus eight days until review | With final testing 35 days after each review, eight days favored factual and application questions in the primary analysis; the conservative application reanalysis was marginal (p=.06) [Eight-day review in a simulated classroom](../claims/eight-day-review-improves-five-week-science-test-versus-one-day-review.md) [~M]. | Consider a longer gap for a comparable delayed goal; neither eight days nor far transfer is established as a general prescription. |

**Discriminating observations.** Record the first encounter, each later exposure or retrieval and its feedback, the elapsed gap in its actual units, whether retrieval succeeded, the intended test delay, and separate factual, application, and delayed outcomes. A one-week test following within-session lags and a five-week test following calendar-day lags estimate different relationships.

### Context
#### Requirements
- Repeated encounters with the same target material and a recorded interval in seconds, trials, hours, or days appropriate to the intended test delay.
- A separately specified choice of study, retrieval, feedback, or application within each encounter.
- Curriculum-level planning that reserves time for revisiting earlier material, rather than treating each session as a discrete unit.

#### Constraints
- Learners consistently prefer massed practice because spaced practice feels less fluent and more effortful, leading to underuse without external structure [-M].
- The best gap depends on the final-test delay and task; the reviewed literature leaves many combinations sparsely sampled [~M].
- Coordination overhead is high in institutional settings: scheduling spaced review requires deliberate curriculum design that conflicts with standard weekly topic-by-topic pacing [~M].

### Target Learners
- Adult learners in high-retention domains (healthcare, law, language learning) where durable recall under time pressure is essential.
- Learners with limited study time who need efficient encoding — spacing increases yield per hour of study.
- Learners with memory impairments may require different schedules and support; the cited verbal-recall synthesis excluded clinical populations.
- Language learners at any level, where vocabulary and grammar benefit strongly from distributed practice.

### Target Learning Objectives
- Long-term retention of factual, procedural, and conceptual knowledge.
- Delayed application is a distinct outcome that needs its own assessment; one simulated lecture study tested rephrased application questions.
- Development of durable recall that holds under time pressure or interference.
- Metacognitive awareness of the difference between feeling-of-knowing and actual retention.

### Theory
#### Supporting
- [Information Processing Theory](../theories/information-processing-theory.md) — encoding variability and study-phase retrieval are proposed explanations; the spacing contrasts above do not discriminate them.
- Distributed practice / spacing effect — an observed difference across schedules; an individual's point of near-forgetting is not measured or optimized by these cited comparisons.

#### Contradicting / Qualifying
- An immediate feeling of fluency and an immediate **test result** are different outcomes. The verbal-recall synthesis does not support a blanket immediate-test advantage for massed study.

### Claims
- [Distributed Practice Improves Retention](../claims/distributed-practice-improves-retention.md) [+S] — equal-time verbal recall and test-delay moderation
- [Total retrieval spacing and relative schedules](../claims/total-retrieval-spacing-beats-massed-but-relative-schedule-not-distinguished.md) [~M] — total versus relative retrieval spacing in the primary experiment
- [Eight-day review in a simulated classroom](../claims/eight-day-review-improves-five-week-science-test-versus-one-day-review.md) [~M] — one versus eight days, factual and application outcomes
- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [+S] — Organizing review into meaningful units helps learners revisit important material without overloading working memory each time.
- [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [~S] — Spaced review is especially useful when it requires retrieval and then corrects confident mistakes clearly.
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M] — Learners are more likely to sustain spaced study when they can monitor schedules, performance, and forgetting over time.

## Related Principles
- [Formative Assessment](formative-assessment.md) — low-stakes assessments are the natural delivery mechanism for spaced retrieval; quizzes and checks serve both assessment and spacing functions
- [Goal Setting & Monitoring](goal-setting-monitoring.md) — self-monitoring study schedules makes spacing explicit and sustains learner adherence
- [Worked Examples](worked-examples.md) — spacing review of worked examples across sessions improves transfer more than massing the same examples in a single session

## Examples

- **[Anki](https://apps.ankiweb.net)** — A free flashcard application that implements spaced repetition via the SM-2 algorithm, scheduling each card for review at the estimated point of near-forgetting. Widely used in medical education (USMLE preparation) and language learning.
- **[Duolingo](https://www.duolingo.com)** — Spaced repetition drives the vocabulary review schedule; previously learned items resurface at algorithmically timed intervals within the daily lesson flow.
- **Interleaved unit reviews** — A classroom pattern where the first 5–10 minutes of each session revisit material from 1–3 sessions prior via retrieval questions before introducing new content. Low implementation cost; no technology required.

## Key Sources
- Benjamin, A. S., & Tullis, J. (2010). What makes distributed practice effective? *Cognitive Psychology, 61*(3), 228–247. [doi:10.1016/j.cogpsych.2010.05.004](https://doi.org/10.1016/j.cogpsych.2010.05.004)
- Carpenter, S. K. (2012). Testing enhances the transfer of learning. *Current Directions in Psychological Science, 21*(5), 369–373. [doi:10.1177/0963721412452728](https://doi.org/10.1177/0963721412452728)
- Kapler, I. V., Weston, T., & Wiseheart, M. (2015). Spacing in a simulated undergraduate classroom: Long-term benefits for factual and higher-level learning. *Learning and Instruction, 36*, 38–45. [doi:10.1016/j.learninstruc.2014.11.001](https://doi.org/10.1016/j.learninstruc.2014.11.001)
- Karpicke, J. D., & Bauernschmidt, A. (2011). Spaced retrieval: Absolute spacing enhances learning regardless of relative spacing. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 37*(5), 1250–1257. [doi:10.1037/a0023436](https://doi.org/10.1037/a0023436)
- Logan, J. M., Castel, A. D., Haber, S., & Viehman, E. J. (2012). Metacognition and the spacing effect: The role of repetition, feedback, and instruction on judgments of learning for massed and spaced rehearsal. *Metacognition and Learning, 7*(3), 175–195. [doi:10.1007/s11409-012-9090-3](https://doi.org/10.1007/s11409-012-9090-3)
