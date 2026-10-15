---
type: strategy
id: spaced-repetition-scheduling
aliases: [spaced_repetition]
title: Spaced Repetition Scheduling
description: Scheduling review of material at increasing intervals over time rather than massing it into a single session, so each review occurs just as forgetting begins.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Spaced Repetition Scheduling

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Spaced repetition scheduling distributes study or review of an item across multiple sessions separated by expanding intervals (e.g., 1 day, 3 days, 1 week), timed so each review occurs near the point of forgetting. It is typically implemented with [Retrieval Practice](../elements/practice.md) — the learner actively recalls the item rather than rereading it — and an algorithm or rule adjusts the next interval based on recall success.

## Design Implications

Spacing produces substantially better long-term retention than massed study of the same total duration, one of the most robust findings in memory research (the "spacing effect") [+S]. The benefit is largest when reviews are paired with retrieval rather than restudy, and when intervals are long enough to require effortful but successful recall [~S]. Optimal spacing depends on the retention interval: longer delays to the final test call for longer gaps between sessions [+S].

### Context
#### Requirements
- Content decomposable into discrete, testable items (facts, vocabulary, formulas, procedures)
- A scheduling rule or algorithm (e.g., Leitner boxes, SM-2 as used in Anki) that expands intervals after successful recall and contracts them after failure
- Learner persistence across days or weeks — spacing only pays off over time, so the schedule must fit the course timeline
- A bank of reviewable items or tasks, ideally broken into small units ([Chunking](../principles/chunking.md))
- A scheduling mechanism — software (Anki, SuperMemo, Duolingo), a course calendar, or teacher-planned review cycles
- Retrieval-based review activities; spacing passive rereading forfeits most of the benefit
- Enough lead time before a criterion test for at least two or three spaced encounters

#### Constraints
- Spacing feels harder and slower than massing; learners frequently judge massed study more effective even when spaced study produces superior retention [-S] — a fluency illusion that leads to self-scheduling errors
- Little benefit for material needed only once or for a test occurring within hours; the spacing effect emerges over retention intervals of days and beyond [~S]
- Poorly suited to complex, integrative performances (essays, open-ended design) that resist decomposition into discrete reviewable items [-W]
- Expanding schedules are only marginally better than equally spaced reviews; over-engineering the algorithm adds complexity without proportional gains [~W]
- Spacing produces little benefit when the criterion test is immediate; massing can even be superior for next-day tests [~S] — the advantage emerges on delayed measures
- Learners often prefer massing and judge it more effective, so self-scheduled study underuses spacing [-M]; the strategy must be built into the course structure rather than left to learner choice
- Very long intervals before a first review can let forgetting proceed too far, making retrieval fail and requiring costly relearning [~W]
- For complex, integrated skills (e.g., essay writing), item-level scheduling is awkward; spacing must operate at the level of whole tasks rather than discrete facts

#### Implementation Variability
- **Fixed vs. expanding intervals** — equal spacing (e.g., every 3 days) captures most of the benefit; expanding schedules optimize further for large item sets
- **System-driven (SRS software)** — Anki, SuperMemo, Memrise schedule each item individually; best for large declarative bodies of content
- **Curriculum-driven** — the instructor builds cumulative quizzes and interleaved homework so that older material recurs naturally; better for classroom settings where learners won't self-schedule
- **Successive relearning** — repeated cycles of retrieval practice plus feedback until a criterion is reached, then respaced; combines spacing with mastery
- **Fixed expanding schedules** (e.g., 1–3–7–21 days) — simple, predictable, works without software
- **Adaptive algorithms** (SM-2 in Anki, FSRS) — adjust intervals per item based on recall success; more efficient for large item banks
- **Interleaved spacing** — mixing related problem types across sessions combines spacing with [interleaving](interleaving.md), which adds discrimination benefits for categorizable material [+M]
- **Cumulative review** — each quiz or homework includes items from prior units, embedding spacing without a separate review system

### Target Learners
- Learners building declarative knowledge bases: vocabulary, anatomy, law, programming syntax, music theory [+S]
- Learners preparing for cumulative or high-stakes delayed assessments, where spacing's advantage over cramming is largest [+S]
- Less effective for learners who cannot or will not sustain multi-week engagement, and for advanced learners whose knowledge is already well-consolidated [~W]
- All learners benefit from spacing for retention, but it is especially valuable for learners who must retain large bodies of factual knowledge (language learners, pre-clinical medical students) [+S]
- Less self-regulated learners benefit most from instructor- or system-scheduled spacing, since they will not impose it themselves [-M]
- Learners preparing for delayed assessments (final exams, certification, licensing) gain more than those facing only immediate tests [+S]

### Target Learning Goals
- Long-term retention of facts, definitions, and associations
- Fluency and automaticity in prerequisite skills (e.g., math facts, conjugations) that free working memory for higher-order work
- Maintenance of previously mastered material across a course or program
- Long-term retention of facts, vocabulary, formulas, and concepts
- Fluency and automaticity of foundational skills that later learning depends on
- Not well suited by itself to deep conceptual understanding or transfer; pair with application and elaboration activities

### Instructions
1. Decompose the target content into discrete items or prompts, each with a defined correct response.
2. Pair each item with an active recall prompt rather than a restudy prompt ([Retrieval Practice](../elements/practice.md)); add feedback for incorrect recalls.
3. Set the initial interval (typically 1–2 days) and an expansion rule (e.g., double the interval on success, reset on failure).
4. Embed the schedule in the course structure — cumulative quizzes, interleaved problem sets, or SRS software — rather than relying on learners to self-schedule, since their metacognitive judgments underweight spacing [-S].
5. Adjust interval length to the retention interval: the longer until the final use of the material, the wider the gaps should be [+S].
6. Monitor item difficulty and retire or rework items that repeatedly fail, to prevent the schedule from filling with poorly encoded material.

## Related Strategies
- [Retrieval Practice](retrieval-practice-activities.md) — the active-recall mechanism that makes each spaced review effective; spacing without retrieval (mere rereading) yields much smaller gains
- [Interleaving](interleaving.md) — often combined with spacing; mixing item types within a session compounds the desirable-difficulty benefit
- [Cumulative Review Quizzes](cumulative-review-quizzes.md) — a classroom implementation that spaces older material without software
- [Cramming](cramming.md) — the massed contrast case; effective for immediate performance but inferior for retention
- [Cumulative Quizzing](cumulative-quizzing.md) — a course-level mechanism for delivering spaced retrieval at scale

## Examples
- **[Anki](https://apps.ankiweb.net)** — open-source SRS using the SM-2 expanding-interval algorithm; widely used in medical education, where studies report improved exam retention for spaced flashcard users.
- **[Duolingo](https://www.duolingo.com)** — schedules review of vocabulary items at individualized expanding intervals based on learner error patterns.
- **Cumulative homework in physics courses** — problem sets that deliberately re-include topics from prior weeks, spacing review without any software.
- **[Anki](https://apps.ankiweb.net)** — open-source flashcard system using the SM-2 adaptive scheduling algorithm; widely used in medical education for high-volume factual retention.
- **[Duolingo](https://www.duolingo.com)** — language-learning app that resurfaces previously learned vocabulary on expanding intervals based on learner performance.
- **Cumulative homework in mathematics courses** — problem sets that always include 20–30% items from prior units, implementing spacing without dedicated review sessions.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966–968. [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408)
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)
- Karpicke, J. D., & Roediger, H. L. (2007). Expanding retrieval practice promotes short-term retention, but equally spaced retrieval enhances long-term retention. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 33*(4), 704–719. [doi:10.1037/0278-7393.33.4.704](https://doi.org/10.1037/0278-7393.33.4.704)
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World* (pp. 56–64). Worth Publishers.

<!-- merged 2026-10-15 from strategies/spaced_repetition ("Spaced Repetition"), a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Spaced Repetition

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

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
- [Retrieval Practice](retrieval-practice-activities.md) — the activity that makes each spaced encounter effective; spacing without retrieval is far weaker
- [Interleaving](interleaving.md) — mixes item types within and across sessions; combines naturally with spacing schedules
- [Cumulative Quizzing](cumulative-quizzing.md) — a course-level mechanism for delivering spaced retrieval at scale

## Examples
- **[Anki](https://apps.ankiweb.net)** — open-source flashcard system using the SM-2 adaptive scheduling algorithm; widely used in medical education for high-volume factual retention.
- **[Duolingo](https://www.duolingo.com)** — language-learning app that resurfaces previously learned vocabulary on expanding intervals based on learner performance.
- **Cumulative homework in mathematics courses** — problem sets that always include 20–30% items from prior units, implementing spacing without dedicated review sessions.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
- Karpicke, J. D., & Roediger, H. L. (2007). Expanding retrieval practice promotes short-term retention, but equally spaced retrieval enhances long-term retention. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 33*(4), 704–719. [doi:10.1037/0278-7393.33.4.704](https://doi.org/10.1037/0278-7393.33.4.704)
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World* (pp. 56–64). Worth Publishers.
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)
-->
