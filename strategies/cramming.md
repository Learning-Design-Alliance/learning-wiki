---
type: strategy
id: cramming
title: Cramming
description: Massing study into a single session immediately before an assessment, relying on short-term familiarity rather than durable retention.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Cramming

> **Strategy** · [All strategies](index.md)

## Description
Cramming concentrates all study of a topic into one or a few sessions immediately preceding an exam, rather than distributing it over time (spacing) or interleaving topics. It typically involves rereading notes and highlighting — high-fluency, low-retrieval activities — under time pressure and sleep deprivation. It can produce adequate performance on an imminent test while leaving knowledge fragile and rapidly decaying.

## Design Implications

Cramming exploits the *spacing effect*: massed practice feels effective because material remains in working memory and retrieval is easy, but distributed practice produces substantially better long-term retention for the same total study time [~S]. The subjective fluency of a cram session is a poor proxy for learning — learners mistake ease of processing for durable encoding, a metacognitive illusion that makes cramming self-reinforcing. Because cramming relies heavily on rereading rather than retrieval, it skips the retrieval practice that drives durable memory, and sleep loss immediately after study further impairs consolidation.

### Context
#### Requirements
- A deadline or assessment that makes massed study rational in the learner's eyes
- Access to notes, slides, or summaries to reread
- Sufficient unbroken time block immediately before the assessment

#### Constraints
- Retention collapses within days to weeks; massed study produces far worse delayed-test performance than spaced study of equal duration [~S]
- Rereading-based cramming builds recognition familiarity, not recall ability — learners fail when the exam requires generation or transfer rather than recognition
- Sleep deprivation after a late-night session disrupts memory consolidation, offsetting even the short-term gains
- Promotes surface strategies (memorizing isolated facts) over schema building; under time pressure, working memory is overloaded and deep encoding suffers [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-S]
- Models poor self-regulation: learners who habitually cram show weaker planning and monitoring skills [~W]

#### Implementation Variability
- **Instructor-structured spacing** — schedule multiple low-stakes quizzes across the term so learners cannot defer all study to the end; cumulative quizzing forces periodic retrieval
- **"Minimum viable spacing"** — even two sessions separated by a day outperform one session of double length; useful advice for learners who will not adopt full spaced schedules
- **Cramming as review** — a final consolidated session *on top of* prior spaced study is far less harmful than cramming as the only study; the distinction matters for advising
- **Interleaved cramming** — if time is fixed and short, mixing problem types within the session still beats blocking them

### Target Learners
- Most harmful for learners building foundational knowledge intended for later courses, where prior-knowledge decay compounds
- Least harmful for one-off assessments with no cumulative follow-on — though even here retrieval-based study outperforms rereading
- Common among novices who lack the metacognitive awareness to distinguish fluency from learning; explicit instruction on desirable difficulties reduces reliance on cramming [~M]

### Target Learning Goals
- Poorly suited to durable retention, transfer, and cumulative skill building
- Marginally serviceable for short-term recognition of isolated facts
- Counterproductive for goals requiring schema construction, since massed single-session study does not support the repeated, varied encoding that builds flexible knowledge

### Instructions
1. Diagnose the pattern: ask learners when they studied and how (rereading vs. self-testing) — most crammers are also rereaders.
2. Teach the fluency-vs-learning distinction with a demonstration: two groups study the same list, one rereads, one self-tests; test both after five minutes and after a week.
3. Replace the single session with a spaced schedule using [Spaced Practice](../principles/spaced-practice.md) principles — short sessions at expanding intervals.
4. Convert rereading time into retrieval: closed-book recall, flashcards, or practice problems, per the testing effect.
5. Structure the course so cramming is not viable: cumulative low-stakes quizzes, distributed assignments, and final exams weighted toward material from the whole term.

## Related Strategies
- [Spaced Practice](../principles/spaced-practice.md) — the direct alternative; same total time, distributed across sessions
- [Retrieval Practice](retrieval-practice.md) — replaces passive rereading with self-testing that strengthens memory
- [Interleaving](interleaving.md) — mixes problem types within and across sessions, countering blocked massed study
- [Cumulative Quizzing](cumulative-quizzing.md) — course structure that makes deferring study impossible

## Examples
- **Roediger & Karpicke (2006)** — students who repeatedly studied a passage predicted better delayed recall, but students who practiced retrieval remembered far more one week later; the rereaders' confidence was a cramming-style illusion.
- **Dunlosky et al. (2013)** — rated rereading and highlighting (the core cramming behaviors) as *low utility*, while distributed practice and practice testing received the highest utility rating across hundreds of studies.
- **Cumulative quiz design in introductory STEM courses** — weekly quizzes covering all prior material, a common restructuring used to eliminate end-of-term massing.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the "enemy of induction"? *Psychological Science, 19*(6), 585–592. [doi:10.1111/j.1467-9280.2008.02127.x](https://doi.org/10.1111/j.1467-9280.2008.02127.x)