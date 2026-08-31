---
type: strategy
title: Distributed Practice
description: Practicing content in short sessions spaced over time rather than massed into one long session, leveraging desirable difficulties to strengthen long-term retention.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Distributed Practice

> **Strategy** · [All strategies](index.md)

## Description
Distributed practice (spacing) involves practicing content in short sessions separated by intervals of time, in contrast to massed practice (cramming) in a single long session. The gap between sessions allows partial forgetting, so each session requires active reconstruction of the material — a "desirable difficulty" that strengthens the memory trace. It typically begins after initial learning has reached reasonably good accuracy, then repeats at expanding intervals.

## Design Implications

Distributed practice is one of the most robust findings in learning science: spaced retrieval roughly doubles long-term retention relative to massed practice, with effects persisting months to years [+S]. Its power comes from effortful retrieval after partial forgetting — the same mechanism exploited by [Retrieval Practice](../elements/practice.md), with which it is most effective when combined [+S]. Because the effort of reconstruction feels like failure, learners often misjudge its value and prefer easier techniques like re-reading or highlighting that produce weaker learning [+M].

### Context
#### Requirements
- Initial learning to a "pretty good" accuracy baseline before spacing begins (an early massed session is often needed)
- A schedule of short sessions with meaningful gaps — typically days, not minutes — ideally expanding as retention strengthens
- Learner adherence to the schedule; calendar prompts, course structure, or adaptive software can enforce it
- [Feedback](../elements/practice.md) after each retrieval attempt so errors are corrected, not rehearsed

#### Constraints
- Learners perceive spacing as harder and less effective than massing, undermining voluntary adoption [-M] — the subjective fluency of cramming is mistaken for learning
- Spacing requires time to work; it cannot rescue learning the night before an assessment [-S]
- Very short gaps (minutes) or very long gaps (beyond the retention horizon) reduce the benefit [~M] — optimal gap scales with time to test
- For fast-mapping or highly integrated conceptual material, some massing may be appropriate before spacing begins [~W]

#### Implementation Variability
- **Expanding schedules** (intervals grow: 1 day, 3 days, 1 week) vs. **fixed schedules** (equal gaps) — expanding is often slightly better but fixed is easier to administer [~M]
- **Spaced retrieval** (each session tests from memory) vs. **spaced re-study** (each session re-reads) — retrieval versions produce substantially larger effects [+S]
- **Interleaving** related problem types within spaced sessions compounds the benefit for discrimination learning [~M]
- Curriculum-embedded spacing (spiral curricula, cumulative quizzes) vs. learner-managed spacing via flashcard apps

### Target Learners
- Learners of all ages, from early childhood through adulthood [+S]
- Students preparing for exams or certification, and anyone needing retention over months or years
- Learners who rely on re-reading and highlighting — these groups gain most from substitution, though they resist it because it feels less effective [-M]

### Target Learning Goals
- Long-term retention of declarative knowledge (facts, concepts, vocabulary)
- Fluency and durability of procedural skills (e.g., math procedures, music practice)
- Reduced forgetting across a course, enabling cumulative assessment

### Instructions
1. Establish initial accuracy with a focused first session; do not begin spacing before the material is minimally learnable.
2. Schedule the first review 1–3 days later, requiring retrieval from memory rather than re-reading ([Practice](../elements/practice.md)).
3. Provide corrective [Feedback](../elements/practice.md) immediately after each retrieval attempt.
4. Expand intervals as accuracy improves (e.g., 3 days → 1 week → 3 weeks), scaling the final interval to the assessment date.
5. Track decreasing error rates across sessions as evidence that spacing is working; escalate difficulty or interleave related material as fluency grows.

## Related Strategies
- [Retrieval Practice](../elements/practice.md) — the mechanism spacing amplifies; spaced retrieval is the strongest known combination
- [Interleaving](../elements/practice.md) — mixing problem types within spaced sessions adds a second desirable difficulty
- [Cumulative Assessment](../elements/assess-performance.md) — course structures that force spaced review by design

## Examples
- **Anki / spaced-repetition flashcards** ([https://apps.ankiweb.net](https://apps.ankiweb.net)) — implements expanding-interval scheduling for vocabulary, medicine, and law study; used widely in medical education.
- **Spiral curricula in mathematics** (e.g., [Everyday Mathematics](https://www.mheonline.com/em/)) — distributes practice of each concept across the year instead of a single unit, with repeated distributed exposure.
- **Guitar chord practice** — practicing a new chord in short daily sessions over several weeks rather than one long session, matching the CSV example.
- **Cumulative quizzing** — a course in which each weekly quiz includes items from all prior weeks, structurally enforcing spaced retrieval.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)
- Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.
- Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966–968. [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408)