---
type: strategy
id: spaced-practice-scheduling
aliases: [spaced_practice, use_spaced_practice]
title: Spaced Practice Scheduling
description: Distributing practice sessions over time rather than massing them together, exploiting the spacing effect to improve long-term retention.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Spaced Practice Scheduling

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Spaced practice scheduling distributes study or practice of a given skill or topic across multiple sessions separated in time, rather than concentrating it in one block. The gap between encounters forces partial forgetting and effortful retrieval, which strengthens the memory trace more than equivalent time spent massed together.

## Design Implications

Spacing is one of the most robust findings in learning science: across hundreds of experiments, spaced practice produces substantially better delayed retention than massed practice of equal duration [~S→+S: the effect on delayed retention is strongly supported, though massed practice can win on immediate tests]. The mechanism is desirable difficulty — a gap introduces just enough forgetting that retrieval at the next session requires effort, and that effort deepens encoding. Spacing pairs naturally with [Practice](../elements/practice.md) and with retrieval-based formats; retrieval practice itself benefits from being spaced across sessions.

### Context
#### Requirements
- Content that can be revisited in multiple sessions — a curriculum with room to return to topics rather than "cover and move on"
- A schedule: fixed intervals (e.g., review at 1 day, 1 week, 1 month) or expanding intervals based on learner performance
- Practice tasks that require retrieval or application, not passive re-reading — spacing re-reading yields far weaker benefits
- Learner awareness that spaced study feels harder and less productive in the moment; without this, learners often prefer massing [~M]
- A curriculum plan that revisits content at expanding intervals rather than treating each unit as closed
- Retrieval-based activities at the start of each session ([Practice](../elements/practice.md), cumulative quizzing), not passive re-reading
- Scheduling infrastructure — a course calendar, spiral curriculum map, or platform that automates item resurfacing and reminders
- A curriculum or course map that revisits key content at planned intervals rather than treating each unit as "done" once taught
- Cumulative assessment and review activities that include earlier material, not only the most recent unit
- Enough lead time before a high-stakes deadline or exam to allow at least two or three spaced encounters with core content
- Learner awareness of why spacing feels harder and less satisfying than massing — brief instruction on desirable difficulties improves buy-in [Bjork & Bjork, 2011] [+M]

#### Constraints
- Massed practice outperforms spacing on *immediate* tests [-S] — if assessment occurs right after study, spacing shows no advantage and may look worse to learners
- Very long gaps with insufficient initial learning produce retrieval failure rather than strengthening [~M] — the first encounter must establish enough of a trace to be retrievable after the interval
- Spacing is less effective for material that must be used only once or within a single session (e.g., cramming for a one-off event)
- Learners' judgments of learning are systematically miscalibrated under spacing; they may abandon spaced schedules in favor of massed ones because massing feels easier [-M]
- Expanding schedules require tracking individual item performance; without an adaptive system, fixed schedules are simpler but can mistime reviews for fast or slow learners [~W]
- Learners systematically misjudge spacing as less effective than cramming because massed study feels easier and produces better short-term performance [Learners' preferences diverge from optimal scheduling.](https://doi.org/10.1037/a0031313) [-M] — expect resistance and teach the evidence explicitly
- Benefits accrue over weeks and months; spacing does little for performance on an assessment occurring the next day [~S]
- Gating mechanisms that lock content until an interval passes can frustrate motivated learners or block just-in-time reference use; intervals that are too long cause retrieval failure rather than productive difficulty [~M]
- Requires sustained adherence across a term; a single spaced session has negligible effect
- Learners systematically prefer massing and judge it more effective, because fluent short-term performance is mistaken for durable learning ([Kornell & Bjork, 2008](https://doi.org/10.1111/j.1467-9280.2008.02127.x)) [-M] — without explicit guidance, students will cram even when a spaced schedule is offered
- Spacing gains shrink or vanish when the material is used only once and never re-encountered; spacing a single exposure does nothing
- Very short intervals (minutes) or very long intervals relative to the retention interval reduce the benefit; the optimal gap scales with how long the knowledge must be retained ([Cepeda et al., 2008](https://doi.org/10.1111/j.1467-9280.2008.02209.x)) [~S]
- In fast-moving curricula where each lesson builds tightly on the last, forcing long gaps before skill consolidation can leave learners practicing on an unstable foundation [~M]

#### Implementation Variability
- **Fixed spacing**: predetermined intervals (daily, weekly) — simple to implement in any curriculum
- **Expanding spacing**: intervals grow as items are mastered (e.g., 1 day → 3 days → 1 week) — the basis of most [adaptive-learning](../principles/adaptive-learning.md) flashcard systems
- **Interleaving within spacing**: mixing problem *types* within a session (Rohrer's shuffled mathematics practice) compounds the benefit, though learners perceive it as more confusing [~M]
- **Micro-spacing within a lesson**: revisiting a concept at two points in one class period — a weaker but practical approximation
- **Expanding schedules** (1 day → 3 days → 1 week) vs. **fixed schedules** (every 3 days); expanding intervals are generally at least as effective and more efficient [~S]
- **Instructor-driven** (spiral curriculum, cumulative exams) vs. **learner-driven** (flashcard apps with spaced-repetition algorithms such as Anki's SM-2)
- **Within-session spacing** (interleaving item types) vs. **between-session spacing** (days between lessons) — related but distinct mechanisms
- **Fixed schedule**: review every lesson N days/weeks apart; simple to administer
- **Expanding schedule**: gaps grow after each successful recall (e.g., 1 day → 3 days → 1 week); slightly more efficient in some studies [~W]
- **Adaptive spacing**: software schedules each item based on individual recall success (e.g., Anki's spaced-repetition algorithm)
- **Interleaved spacing**: alternate topics within and across sessions; see [Interleaving](interleaving.md) if present in your context — combining spacing with interleaving compounds retention benefits for discriminating problem types [+M]

### Target Learners
- All learners benefit from spacing on delayed measures; the effect is unusually general across ages, materials, and ability levels [+S]
- Learners preparing for delayed assessments (final exams, certification, licensing) benefit most, since the advantage appears at retention intervals of weeks or more
- Younger learners and those with weaker metacognition need explicit scaffolding to persist with spaced schedules, because spacing feels less effective than massing [~M]
- All age groups benefit, from early readers to medical residents [Cepeda et al. found spacing effects across lifespan and materials.](https://doi.org/10.1037/0033-2909.132.3.354) [+S]
- Particularly high value for cumulative disciplines (languages, anatomy, mathematics) where later content depends on retained earlier content
- Learners with weaker metacognitive monitoring benefit most from instructor- or algorithm-scheduled spacing, since they are least likely to self-schedule effectively [~M]
- All learners benefit, but the effect is largest for retention over weeks and months rather than immediate performance ([Cepeda et al., 2006](https://doi.org/10.1037/0033-2909.132.3.354)) [+S]
- Younger learners and novices may need the schedule imposed for them, since they are less likely to self-pace study sessions effectively ([Kornell & Bjork, 2008](https://doi.org/10.1111/j.1467-9280.2008.02127.x)) [-M]
- Learners preparing for cumulative or delayed assessments (licensing exams, prerequisite sequencing) gain the most

### Target Learning Goals
- Long-term retention of facts, concepts, and procedures
- Automaticity and fluency in procedural skills (e.g., math facts, vocabulary, grammar)
- Durability of learning that must be accessed far after instruction (professional practice, cumulative courses)
- Long-term retention of declarative knowledge (vocabulary, facts, definitions)
- Fluency and automaticity in procedural skills through distributed rehearsal
- Cumulative course mastery rather than unit-by-unit performance
- Fluency and automaticity in skills that must remain reliable over time
- Cumulative knowledge building where later learning depends on earlier material

### Instructions
1. Identify the core content that must be retained long-term and budget multiple encounters for it across the course, rather than one instructional block.
2. Design each encounter as an active [Practice](../elements/practice.md) or retrieval task — quizzing, problem-solving, or application — not re-presentation of the original material.
3. Set the first gap short enough that the material is still retrievable (typically 1–3 days after initial learning), then lengthen subsequent gaps as performance stabilizes.
4. Where possible, interleave related problem types within each spaced session rather than blocking by topic.
5. Tell learners why the schedule feels harder than cramming and that the difficulty is the point; share delayed-test evidence to sustain buy-in.
6. Manage total load when adding spaced reviews to new content, so cumulative review does not trigger overload [Cognitive Load Management](../principles/cognitive-load-management.md).

## Related Strategies

- [Retrieval practice](retrieval-practice-activities.md) — the active mechanism spacing works through; spacing multiplies the value of each retrieval attempt
- [Interleaved practice](interleaved-practice.md) — mixing item types within sessions; combines with spacing for the strongest durable-learning schedules
- [Cumulative review quizzing](cumulative-review-quizzes.md) — a classroom implementation that builds spacing into assessment
- [Build regular reiteration of previously covered vocabulary topics into the EFL curriculum](curriculum-reiteration-one-step-forward-two-steps-back.md)
- [Sequence simpler desirable difficulties (retrieval, spacing, interleaving) during initial L2 vocabulary encoding, reserving generation for post-encoding consolidation](generation-as-post-encoding-consolidation-strategy.md)
- [Retrieval Practice](../elements/practice.md) — the activity that makes each spaced encounter effortful and effective; spacing without retrieval is weak re-exposure
- [Cumulative Assessment](../elements/assessment.md) — assessment structure that forces spaced review rather than unit-then-forget study
- [Use Worked Examples](worked-examples-first.md) — faded and revisited worked examples across sessions implement spacing for procedural skills
- [Interleaving](interleaving.md) — the within-session complement to between-session spacing

## Examples
- **Anki** (https://apps.ankiweb.net) — open-source flashcard system implementing expanding spaced repetition with per-item scheduling; widely used in medical education.
- **[Duolingo](../products/duolingo.md)** (https://www.duolingo.com) — schedules review of previously learned vocabulary at expanding intervals interleaved with new material.
- **Rohrer's shuffled homework studies** — reordering mathematics homework so problems of the same type are separated across assignments improved delayed test scores substantially over blocked, massed assignments.
- **Cumulative weekly quizzes** in a course design where each quiz includes ~30% items from earlier units, converting assessment itself into a spaced schedule.
- **Duolingo** — algorithmically schedules review of lapsed vocabulary items and prompts returning learners with "practice" sessions targeting weakened items ([duolingo.com](https://www.duolingo.com))
- **Anki** — open-source spaced-repetition flashcard system using the SM-2 expanding-interval algorithm; widely used in medical education ([apps.ankiweb.net](https://apps.ankiweb.net))
- A world-language course replaces end-of-unit tests with weekly cumulative quizzes covering all vocabulary to date, converting the assessment schedule itself into a spacing schedule
- **Khan Academy** — mastery system re-assigns previously "mastered" skills for review after delays, requiring learners to demonstrate retention over time
- **Anki** (https://apps.ankiweb.net) — open-source spaced-repetition flashcard software using an adaptive expanding-schedule algorithm; widely used in medical education for high-volume factual retention.
- **[Duolingo](../products/duolingo.md)** (https://www.duolingo.com) — schedules review of previously learned vocabulary and grammar at expanding intervals interleaved with new material.
- **Cumulative math homework** — curricula such as *Everyday Mathematics* build systematic distributed practice into homework and review cycles rather than teaching each topic in a single closed unit.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)
- Karpicke, J. D., & Bauernschmidt, A. (2011). Spaced retrieval: Absolute spacing enhances learning regardless of relative spacing. *Journal of Experimental Psychology: Learning, Memory, and Cognition, 37*(5), 1250–1257. [doi:10.1037/a0023436](https://doi.org/10.1037/a0023436)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
- Kang, S. H. K. (2016). Spaced repetition promotes efficient and effective learning: Policy implications of innovations in teaching and learning. *Policy Insights from the Behavioral and Brain Sciences, 3*(1), 12–19. [doi:10.1177/2372732215624708](https://doi.org/10.1177/2372732215624708)
- Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science, 19*(11), 1095–1102. [doi:10.1111/j.1467-9280.2008.02209.x](https://doi.org/10.1111/j.1467-9280.2008.02209.x)
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World* (pp. 56–64). Worth Publishers.
- Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the "enemy of induction"? *Psychological Science, 19*(6), 585–592. [doi:10.1111/j.1467-9280.2008.02127.x](https://doi.org/10.1111/j.1467-9280.2008.02127.x)

<!-- merged 2026-10-13 from strategies/spaced_practice ("Spaced Practice"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Spaced Practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

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
5. Give feedback after retrieval attempts ([Provide Feedback](../elements/practice.md)); spaced retrieval with feedback outperforms spaced re-reading Roediger & Karpicke's testing-effect experiments..
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
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
- Kang, S. H. K. (2016). Spaced repetition promotes efficient and effective learning: Policy implications of innovations in teaching and learning. *Policy Insights from the Behavioral and Brain Sciences, 3*(1), 12–19. [doi:10.1177/2372732215624708](https://doi.org/10.1177/2372732215624708)
-->

<!-- merged 2026-10-13 from strategies/use_spaced_practice ("Use Spaced Practice"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Use Spaced Practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

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
- [Use Retrieval Practice](retrieval-practice-activities.md) — spacing multiplies the benefit of testing; the two are strongest in combination
- [Use Worked Examples](worked-examples-first.md) — faded and revisited worked examples across sessions implement spacing for procedural skills
- [Interleaving](interleaving.md) — the within-session complement to between-session spacing

## Examples
- **Anki** (https://apps.ankiweb.net) — open-source spaced-repetition flashcard software using an adaptive expanding-schedule algorithm; widely used in medical education for high-volume factual retention.
- **Duolingo** (https://www.duolingo.com) — schedules review of previously learned vocabulary and grammar at expanding intervals interleaved with new material.
- **Cumulative math homework** — curricula such as *Everyday Mathematics* build systematic distributed practice into homework and review cycles rather than teaching each topic in a single closed unit.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science, 19*(11), 1095–1102. [doi:10.1111/j.1467-9280.2008.02209.x](https://doi.org/10.1111/j.1467-9280.2008.02209.x)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World* (pp. 56–64). Worth Publishers.
- Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the "enemy of induction"? *Psychological Science, 19*(6), 585–592. [doi:10.1111/j.1467-9280.2008.02127.x](https://doi.org/10.1111/j.1467-9280.2008.02127.x)
-->
