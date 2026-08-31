---
type: strategy
title: Use Spaced Practice
description: Distribute learning sessions and review opportunities over time rather than massing them together, to strengthen retention and transfer.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Use Spaced Practice

> **Strategy** · [All strategies](index.md)

## Description
Spaced practice distributes study, review, or practice of a topic across multiple sessions separated by intervals of time, rather than concentrating it in a single block (massed practice). The intervals can be fixed (e.g., weekly review) or expanding (each successive gap grows longer), and spacing applies equally to revisiting content, re-practicing skills, and re-testing knowledge.

## Design Implications

Spacing produces substantially better long-term retention than massed study of the same total duration — one of the most robust findings in learning science, replicated across verbal learning, motor skills, and classroom studies [Cepeda et al., 2006] [+S]. The benefit arises because a delay before re-engagement introduces mild forgetting, so retrieval during the next session is more effortful and produces stronger memory consolidation than easy, near-perfect recall [Bjork & Bjork, 2011] [+M]. Spacing is frequently combined with [Practice](../elements/practice.md) and self-testing, since spaced retrieval outperforms spaced rereading.

### Context
#### Requirements
- A curriculum or course map that revisits key content at planned intervals rather than treating each unit as "done" once taught
- Cumulative assessment and review activities that include earlier material, not only the most recent unit
- Enough lead time before a high-stakes deadline or exam to allow at least two or three spaced encounters with core content
- Learner awareness of why spacing feels harder and less satisfying than massing — brief instruction on desirable difficulties improves buy-in [Bjork & Bjork, 2011] [+M]

#### Constraints
- Learners systematically prefer massing and judge it more effective, because fluent short-term performance is mistaken for durable learning [Kornell & Bjork, 2008] [-M] — without explicit guidance, students will cram even when a spaced schedule is offered
- Spacing gains shrink or vanish when the material is used only once and never re-encountered; spacing a single exposure does nothing
- Very short intervals (minutes) or very long intervals relative to the retention interval reduce the benefit; the optimal gap scales with how long the knowledge must be retained [Cepeda et al., 2008] [~S]
- In fast-moving curricula where each lesson builds tightly on the last, forcing long gaps before skill consolidation can leave learners practicing on an unstable foundation [~M]

#### Implementation Variability
- **Fixed schedule**: review every lesson N days/weeks apart; simple to administer
- **Expanding schedule**: gaps grow after each successful recall (e.g., 1 day → 3 days → 1 week); slightly more efficient in some studies [~W]
- **Adaptive spacing**: software schedules each item based on individual recall success (e.g., Anki's spaced-repetition algorithm)
- **Interleaved spacing**: alternate topics within and across sessions; see [Interleaving](interleaving.md) if present in your context — combining spacing with interleaving compounds retention benefits for discriminating problem types [+M]

### Target Learners
- All learners benefit, but the effect is largest for retention over weeks and months rather than immediate performance [Cepeda et al., 2006] [+S]
- Younger learners and novices may need the schedule imposed for them, since they are less likely to self-pace study sessions effectively [Kornell & Bjork, 2008] [-M]
- Learners preparing for cumulative or delayed assessments (licensing exams, prerequisite sequencing) gain the most

### Target Learning Goals
- Long-term retention of facts, concepts, and procedures
- Fluency and automaticity in skills that must remain reliable over time
- Cumulative knowledge building where later learning depends on earlier material

### Instructions
1. Identify the core content and skills that must survive beyond the current unit; not everything needs spacing — prioritize durable, foundational knowledge.
2. Schedule the first review within days of initial instruction, before forgetting is complete but after some decay has set in.
3. Design review activities as retrieval, not rereading — low-stakes quizzing, [Practice](../elements/practice.md) problems, or brief recall prompts [Roediger & Karpicke, 2006] [+S].
4. Expand or adapt intervals based on performance; items recalled easily move to longer gaps, items struggled with return sooner.
5. Make assessments cumulative so spaced review has a purpose and learners receive feedback on retention, not just recent learning.
6. Teach learners about the strategy explicitly — explain that spaced practice feels harder and slower but produces more durable learning, to counteract the preference for massing [Kornell & Bjork, 2008] [+M].

## Related Strategies
- [Use Retrieval Practice](use_retrieval_practice.md) — spacing multiplies the benefit of testing; the two are strongest in combination
- [Use Worked Examples](use_worked_examples.md) — faded and revisited worked examples across sessions implement spacing for procedural skills
- [Interleaving](interleaving.md) — the within-session complement to between-session spacing

## Examples
- **Anki** (https://apps.ankiweb.net) — open-source spaced-repetition flashcard software using an adaptive expanding-schedule algorithm; widely used in medical education for high-volume factual retention.
- **Duolingo** (https://www.duolingo.com) — schedules review of previously learned vocabulary and grammar at expanding intervals interleaved with new material.
- **Cumulative math homework** — curricula such as *Everyday Mathematics* build systematic distributed practice into homework and review cycles rather than teaching each topic in a single closed unit.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science, 19*(11), 1095–1102. [doi:10.1111/j.1467-9280.2008.02209.x](https://doi.org/10.1111/j.1467-9280.2008.02209.x)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World* (pp. 56–64). Worth Publishers.
- Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the "enemy of induction"? *Psychological Science, 19*(6), 585–592. [doi:10.1111/j.1467-9280.2008.02127.x](https://doi.org/10.1111/j.1467-9280.2008.02127.x)