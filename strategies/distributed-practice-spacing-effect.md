---
type: strategy
id: distributed-practice-spacing-effect
title: Distributed Practice (Spacing Effect)
description: Distributed practice schedules reviews of information or practice of a task across multiple sessions separated in time, rather than massing them together, producing markedly better long-term retention.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Distributed Practice (Spacing Effect)

> **Strategy** · [All strategies](index.md)

## Description
Distributed practice (spacing) schedules encounters with the same material or skill across multiple sessions separated by time, rather than massing them into one block. Each spaced encounter requires the learner to reconstruct a partially forgotten memory trace, and this effortful retrieval strengthens the trace more than an immediate repetition would. It contrasts with massed practice (cramming), which produces strong short-term performance but rapid forgetting.

## Design Implications

Spacing is one of the most robust findings in learning science: distributed practice reliably outperforms massed practice on delayed tests across ages, materials, and tasks [Distributed practice produces superior long-term retention compared to massed practice.](../claims/distributed-practice-improves-retention.md) [+S]. Its benefit comes partly from the retrieval effort each spaced session demands — which is why spacing pairs naturally with [retrieval practice](../elements/practice.md) rather than rereading [~S]. Optimal gaps scale with retention interval: longer delays to the final test call for longer spacing gaps between sessions [+S].

### Context
#### Requirements
- A curriculum plan that revisits each topic at least twice, with genuine gaps between encounters
- Knowledge of the retention interval (when the material must be recalled) to set gap lengths — roughly 10–20% of the retention interval is a practical heuristic [+M]
- Scheduling infrastructure: course calendars, homework sequencing, or spaced-repetition software that enforces the gaps
- Cumulative assessment so that earlier material remains consequential after its first test

#### Constraints
- Learners judge massed study to be more effective because it feels fluent, while spaced study feels harder — this metacognitive illusion drives cramming even when learners know better [-M]
- Spacing requires advance planning across weeks; it fits poorly with linear, topic-per-week course structures where material is never revisited [-M]
- Benefits are largest for retention of the same material; spacing alone does not build new understanding of poorly comprehended content [-W]
- For very short retention intervals (recall needed within hours), massing may be as effective or more efficient [~M]

#### Implementation Variability
- **Fixed spacing**: predetermined review schedule (e.g., 1 day, 1 week, 1 month after initial learning)
- **Expanding spacing**: gaps lengthen with each successive review (1 day → 3 days → 7 days), often more efficient than fixed schedules [~M]
- **Adaptive spacing**: software schedules each item based on individual recall success (e.g., Anki's algorithm)
- **Interleaving within spacing**: mixing problem types across sessions compounds the benefit for discrimination-based skills [~S]

### Target Learners
- All learners benefit, from early childhood through adulthood [+S]
- Especially valuable for learners preparing for delayed assessments (final exams, certification, licensure)
- Learners prone to cramming benefit most, but must be supported against the fluency illusion — spaced study feels less effective even while producing more learning [-M]

### Target Learning Goals
- Long-term retention of factual and conceptual knowledge
- Durable procedural skill (foreign-language vocabulary, mathematics, music, motor skills)
- Maintenance of prerequisite knowledge that later learning depends on

### Instructions
1. Identify the retention interval — when must this material still be retrievable? Set the first review gap accordingly.
2. Schedule at least two to three review encounters per topic, using [Continuous Review](../elements/continuous-review.md) to revisit earlier material within each new session.
3. Make each spaced encounter a retrieval event, not a rereading: use [Practice](../elements/practice.md) with questions, problems, or recall prompts before feedback.
4. Prefer expanding gaps for efficiency; lengthen gaps as recall becomes easier.
5. Use cumulative quizzes and exams so spaced material continues to carry assessment weight.
6. Where volume is high, use adaptive spaced-repetition software to individualize item scheduling ([Adaptive Learning](../principles/adaptive-learning.md)).

## Related Strategies
- [Retrieval Practice](../strategies/retrieval-practice.md) — the mechanism spacing amplifies; spaced retrieval is the strongest known combination for retention
- [Interleaving](../strategies/interleaving.md) — a scheduling sibling: spacing separates sessions in time, interleaving mixes content within them
- [Cumulative Review](../strategies/cumulative-review.md) — course-level structure that operationalizes spacing across a term

## Examples
- **Duolingo** — schedules practice of previously learned vocabulary on an expanding-spaced algorithm, re-presenting items as recall strength decays.
- **Anki** — open-source flashcard system implementing adaptive spaced repetition (SM-2 family algorithms) for self-directed learners.
- **ASSISTments** — math homework system that interleaves and spaces previously taught skills into new assignments; field studies show improved delayed test performance.
- A typical classroom application: reviewing vocabulary one day, three days, and one week after introduction, with each review as a quiz rather than a rereading.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Kang, S. H. K. (2016). Spaced repetition promotes efficient and effective learning: Policy implications of innovations in teaching and learning. *Policy Insights from the Behavioral and Brain Sciences, 3*(1), 12-19. [doi:10.1177/2372732215624708](https://doi.org/10.1177/2372732215624708)
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)