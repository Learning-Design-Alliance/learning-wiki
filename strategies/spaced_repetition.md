---
type: strategy
title: Spaced Repetition
description: Distributing review of material across multiple sessions separated by increasing time intervals, rather than massing it into one session.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Spaced Repetition

> **Strategy** · [All strategies](index.md)

## Description
Spaced repetition schedules repeated encounters with the same material across time, with intervals expanding as items become better learned (e.g., 1 day, 3 days, 1 week, 1 month). It is typically implemented with [retrieval practice](../elements/practice.md): each spaced encounter is a test or active recall attempt rather than a rereading. The schedule can be fixed (e.g., expand at a set ratio) or adaptive, driven by learner performance and predicted forgetting.

## Design Implications

Spacing exploits the fact that some forgetting between encounters makes retrieval harder, and that difficulty strengthens memory more than easy restudy — the "desirable difficulty" account [+S]. Meta-analyses consistently find spaced practice outperforms massed practice for long-term retention, with effects persisting across verbal, motor, and factual domains [+S]. Spacing is cheap to implement and compounds with retrieval: spaced *testing* yields the largest durable gains, while spaced rereading is weaker [+M].

### Context
#### Requirements
- A bank of reviewable items or tasks, ideally broken into small units ([Chunking](../principles/chunking.md))
- A scheduling mechanism — software (Anki, SuperMemo, Duolingo), a course calendar, or teacher-planned review cycles
- Retrieval-based review activities; spacing passive rereading forfeits most of the benefit
- Enough lead time before a criterion test for at least two or three spaced encounters

#### Constraints
- Spacing produces little benefit when the criterion test is immediate; massing can even be superior for next-day tests [~S] — the advantage emerges on delayed measures
- Learners often prefer massing and judge it more effective, so self-scheduled study underuses spacing [-M]; the strategy must be built into the course structure rather than left to learner choice
- Very long intervals before a first review can let forgetting proceed too far, making retrieval fail and requiring costly relearning [~W]
- For complex, integrated skills (e.g., essay writing), item-level scheduling is awkward; spacing must operate at the level of whole tasks rather than discrete facts

#### Implementation Variability
- **Fixed expanding schedules** (e.g., 1–3–7–21 days) — simple, predictable, works without software
- **Adaptive algorithms** (SM-2 in Anki, FSRS) — adjust intervals per item based on recall success; more efficient for large item banks
- **Interleaved spacing** — mixing related problem types across sessions combines spacing with [interleaving](interleaving.md), which adds discrimination benefits for categorizable material [+M]
- **Cumulative review** — each quiz or homework includes items from prior units, embedding spacing without a separate review system

### Target Learners
- All learners benefit from spacing for retention, but it is especially valuable for learners who must retain large bodies of factual knowledge (language learners, pre-clinical medical students) [+S]
- Less self-regulated learners benefit most from instructor- or system-scheduled spacing, since they will not impose it themselves [-M]
- Learners preparing for delayed assessments (final exams, certification, licensing) gain more than those facing only immediate tests [+S]

### Target Learning Goals
- Long-term retention of facts, vocabulary, formulas, and concepts
- Fluency and automaticity of foundational skills that later learning depends on
- Not well suited by itself to deep conceptual understanding or transfer; pair with application and elaboration activities

### Instructions
1. Decompose content into small, testable units ([Chunking](../principles/chunking.md)).
2. Schedule the first review 1–3 days after initial instruction, not immediately.
3. Make each encounter a retrieval attempt — flashcards, low-stakes quizzes, or cumulative problem sets ([Practice](../elements/practice.md)) — not rereading.
4. Expand intervals as items are mastered; shorten them after failures (adaptive systems do this automatically).
5. Interleave related item types within sessions so learners also practice discriminating between concepts.
6. Keep reviews low-stakes and brief; spacing works best as frequent, short encounters rather than long cram sessions.

## Related Strategies
- [Retrieval Practice](retrieval-practice.md) — the activity that makes each spaced encounter effective; spacing without retrieval is far weaker
- [Interleaving](interleaving.md) — mixes item types within and across sessions; combines naturally with spacing schedules
- [Cumulative Quizzing](cumulative-quizzing.md) — a course-level mechanism for delivering spaced retrieval at scale

## Examples
- **[Anki](https://apps.ankiweb.net)** — open-source flashcard system using the SM-2 adaptive scheduling algorithm; widely used in medical education for high-volume factual retention.
- **[Duolingo](https://www.duolingo.com)** — language-learning app that resurfaces previously learned vocabulary on expanding intervals based on learner performance.
- **Cumulative homework in mathematics courses** — problem sets that always include 20–30% items from prior units, implementing spacing without dedicated review sessions.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Karpicke, J. D., & Roediger, H. L. (2007). Expanding retrieval practice promotes short-term retention, but equally spaced retrieval enhances long-term retention. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 33*(4), 704–719. [doi:10.1037/0278-7393.33.4.704](https://doi.org/10.1037/0278-7393.33.4.704)
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World* (pp. 56–64). Worth Publishers.
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)