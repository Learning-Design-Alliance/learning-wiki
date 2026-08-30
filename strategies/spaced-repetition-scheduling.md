---
type: strategy
title: Spaced Repetition Scheduling
description: Scheduling review of material at increasing intervals over time rather than massing it into a single session, so each review occurs just as forgetting begins.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Spaced Repetition Scheduling

## Description
Spaced repetition scheduling distributes study or review of an item across multiple sessions separated by expanding intervals (e.g., 1 day, 3 days, 1 week), timed so each review occurs near the point of forgetting. It is typically implemented with [Retrieval Practice](../elements/practice.md) — the learner actively recalls the item rather than rereading it — and an algorithm or rule adjusts the next interval based on recall success.

## Design Implications

Spacing produces substantially better long-term retention than massed study of the same total duration, one of the most robust findings in memory research (the "spacing effect") [+S]. The benefit is largest when reviews are paired with retrieval rather than restudy, and when intervals are long enough to require effortful but successful recall [~S]. Optimal spacing depends on the retention interval: longer delays to the final test call for longer gaps between sessions [+S].

### Context
#### Requirements
- Content decomposable into discrete, testable items (facts, vocabulary, formulas, procedures)
- A scheduling rule or algorithm (e.g., Leitner boxes, SM-2 as used in Anki) that expands intervals after successful recall and contracts them after failure
- Learner persistence across days or weeks — spacing only pays off over time, so the schedule must fit the course timeline

#### Constraints
- Spacing feels harder and slower than massing; learners frequently judge massed study more effective even when spaced study produces superior retention [-S] — a fluency illusion that leads to self-scheduling errors
- Little benefit for material needed only once or for a test occurring within hours; the spacing effect emerges over retention intervals of days and beyond [~S]
- Poorly suited to complex, integrative performances (essays, open-ended design) that resist decomposition into discrete reviewable items [-W]
- Expanding schedules are only marginally better than equally spaced reviews; over-engineering the algorithm adds complexity without proportional gains [~W]

#### Implementation Variability
- **Fixed vs. expanding intervals** — equal spacing (e.g., every 3 days) captures most of the benefit; expanding schedules optimize further for large item sets
- **System-driven (SRS software)** — Anki, SuperMemo, Memrise schedule each item individually; best for large declarative bodies of content
- **Curriculum-driven** — the instructor builds cumulative quizzes and interleaved homework so that older material recurs naturally; better for classroom settings where learners won't self-schedule
- **Successive relearning** — repeated cycles of retrieval practice plus feedback until a criterion is reached, then respaced; combines spacing with mastery

### Target Learners
- Learners building declarative knowledge bases: vocabulary, anatomy, law, programming syntax, music theory [+S]
- Learners preparing for cumulative or high-stakes delayed assessments, where spacing's advantage over cramming is largest [+S]
- Less effective for learners who cannot or will not sustain multi-week engagement, and for advanced learners whose knowledge is already well-consolidated [~W]

### Target Learning Goals
- Long-term retention of facts, definitions, and associations
- Fluency and automaticity in prerequisite skills (e.g., math facts, conjugations) that free working memory for higher-order work
- Maintenance of previously mastered material across a course or program

### Instructions
1. Decompose the target content into discrete items or prompts, each with a defined correct response.
2. Pair each item with an active recall prompt rather than a restudy prompt ([Retrieval Practice](../elements/practice.md)); add feedback for incorrect recalls.
3. Set the initial interval (typically 1–2 days) and an expansion rule (e.g., double the interval on success, reset on failure).
4. Embed the schedule in the course structure — cumulative quizzes, interleaved problem sets, or SRS software — rather than relying on learners to self-schedule, since their metacognitive judgments underweight spacing [-S].
5. Adjust interval length to the retention interval: the longer until the final use of the material, the wider the gaps should be [+S].
6. Monitor item difficulty and retire or rework items that repeatedly fail, to prevent the schedule from filling with poorly encoded material.

## Related Strategies
- [Retrieval Practice](retrieval-practice.md) — the active-recall mechanism that makes each spaced review effective; spacing without retrieval (mere rereading) yields much smaller gains
- [Interleaving](interleaving.md) — often combined with spacing; mixing item types within a session compounds the desirable-difficulty benefit
- [Cumulative Review Quizzes](cumulative-review-quizzes.md) — a classroom implementation that spaces older material without software
- [Cramming](cramming.md) — the massed contrast case; effective for immediate performance but inferior for retention

## Examples
- **[Anki](https://apps.ankiweb.net)** — open-source SRS using the SM-2 expanding-interval algorithm; widely used in medical education, where studies report improved exam retention for spaced flashcard users.
- **[Duolingo](https://www.duolingo.com)** — schedules review of vocabulary items at individualized expanding intervals based on learner error patterns.
- **Cumulative homework in physics courses** — problem sets that deliberately re-include topics from prior weeks, spacing review without any software.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966–968. [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408)
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)