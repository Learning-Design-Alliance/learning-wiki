---
type: strategy
title: Spaced Practice
description: Spaced practice distributes learning sessions and reviews over time, contrasting with massed practice (cramming), to improve long-term retention.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Spaced Practice

> **Strategy** · [All strategies](index.md)

## Description
Spaced practice distributes study sessions and reviews across time rather than concentrating them in a single block. Its benefit comes partly from the retrieval effort each spaced encounter requires: after a delay, memory is partially faded, and successful recall under those conditions strengthens the trace more than an easy, immediate repetition would. Instructors implement spacing by breaking content into shorter sessions across days or weeks, opening sessions with low-stakes recall of prior material, and scheduling cumulative review. Digital platforms can automate the schedule — sending reminders, resurfacing lapsed items, and gating re-engagement until the intended interval has elapsed.

## Design Implications

Spaced practice is one of the most robust findings in learning science: distributing repetitions reliably improves long-term retention relative to massing them, across ages, materials, and tasks [Cepeda et al.'s meta-analysis of 254 studies.](https://doi.org/10.1037/0033-2909.132.3.354) [+S]. Spacing combines multiplicatively with [retrieval practice](../elements/practice.md) — testing itself, spaced over time, produces the largest durable gains [Dunlosky et al. rate practice testing and distributed practice the two highest-utility techniques.](https://doi.org/10.1037/a0031313) [+S].

### Context
#### Requirements
- A curriculum plan that revisits content at expanding intervals rather than treating each unit as closed
- Retrieval-based activities at the start of each session ([Practice](../elements/practice.md), cumulative quizzing), not passive re-reading
- Scheduling infrastructure — a course calendar, spiral curriculum map, or platform that automates item resurfacing and reminders

#### Constraints
- Learners systematically misjudge spacing as less effective than cramming because massed study feels easier and produces better short-term performance [Learners' preferences diverge from optimal scheduling.](https://doi.org/10.1037/a0031313) [-M] — expect resistance and teach the evidence explicitly
- Benefits accrue over weeks and months; spacing does little for performance on an assessment occurring the next day [~S]
- Gating mechanisms that lock content until an interval passes can frustrate motivated learners or block just-in-time reference use; intervals that are too long cause retrieval failure rather than productive difficulty [~M]
- Requires sustained adherence across a term; a single spaced session has negligible effect

#### Implementation Variability
- **Expanding schedules** (1 day → 3 days → 1 week) vs. **fixed schedules** (every 3 days); expanding intervals are generally at least as effective and more efficient [~S]
- **Instructor-driven** (spiral curriculum, cumulative exams) vs. **learner-driven** (flashcard apps with spaced-repetition algorithms such as Anki's SM-2)
- **Within-session spacing** (interleaving item types) vs. **between-session spacing** (days between lessons) — related but distinct mechanisms

### Target Learners
- All age groups benefit, from early readers to medical residents [Cepeda et al. found spacing effects across lifespan and materials.](https://doi.org/10.1037/0033-2909.132.3.354) [+S]
- Particularly high value for cumulative disciplines (languages, anatomy, mathematics) where later content depends on retained earlier content
- Learners with weaker metacognitive monitoring benefit most from instructor- or algorithm-scheduled spacing, since they are least likely to self-schedule effectively [~M]

### Target Learning Goals
- Long-term retention of declarative knowledge (vocabulary, facts, definitions)
- Fluency and automaticity in procedural skills through distributed rehearsal
- Cumulative course mastery rather than unit-by-unit performance

### Instructions
1. Map the content to be retained and identify items that must remain active across the whole course.
2. Schedule first review within 1–7 days of initial instruction, then at expanding intervals.
3. Open each session with retrieval, not re-exposure — have learners [recall prior material](../elements/practice.md) before any restudy [+S].
4. Interleave spaced review of older items with new instruction rather than isolating review blocks.
5. Give feedback after retrieval attempts ([Provide Feedback](../elements/practice.md)); spaced retrieval with feedback outperforms spaced re-reading [Roediger & Karpicke's testing-effect experiments.](https://doi.org/10.1207/s15326985ps3806_1) [+S].
6. If using a platform, configure intervals and reminders; consider soft gating (nudges) rather than hard lockouts.

## Related Strategies
- [Retrieval Practice](../elements/practice.md) — the activity that makes each spaced encounter effortful and effective; spacing without retrieval is weak re-exposure
- [Interleaving](../elements/practice.md) — within-session counterpart; mixing item types during spaced sessions compounds the benefit
- [Cumulative Assessment](../elements/assessment.md) — assessment structure that forces spaced review rather than unit-then-forget study

## Examples
- **Duolingo** — algorithmically schedules review of lapsed vocabulary items and prompts returning learners with "practice" sessions targeting weakened items ([duolingo.com](https://www.duolingo.com))
- **Anki** — open-source spaced-repetition flashcard system using the SM-2 expanding-interval algorithm; widely used in medical education ([apps.ankiweb.net](https://apps.ankiweb.net))
- A world-language course replaces end-of-unit tests with weekly cumulative quizzes covering all vocabulary to date, converting the assessment schedule itself into a spacing schedule
- **Khan Academy** — mastery system re-assigns previously "mastered" skills for review after delays, requiring learners to demonstrate retention over time

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Kang, S. H. K. (2016). Spaced repetition promotes efficient and effective learning: Policy implications of innovations in teaching and learning. *Policy Insights from the Behavioral and Brain Sciences, 3*(1), 12–19. [doi:10.1177/2372732215624708](https://doi.org/10.1177/2372732215624708)