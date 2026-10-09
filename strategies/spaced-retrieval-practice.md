---
type: strategy
id: spaced-retrieval-practice
aliases: [spaced_retrieval_practice]
title: Spaced Retrieval Practice
description: Scheduling recall attempts across increasing intervals of time so that learners must reconstruct knowledge from memory rather than re-expose themselves to it.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Spaced Retrieval Practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (2 for, 2 against) · 9 studies (5 causal, 4 quant-synthesis), `q3`–`q4` · 4 of 9 report an effect size · 1 claim rests on one study

## Description
Spaced retrieval practice combines two of the most robust findings in learning science: *retrieval practice* — actively recalling information from memory rather than rereading it — and *spacing* — distributing those recall attempts across time rather than massing them together. In practice, learners answer questions, solve problems, or summarize material from memory at intervals that grow progressively longer (e.g., one day, then three days, then a week), with feedback provided after each attempt.

## Design Implications

Retrieval attempts strengthen memory more than restudying, and spacing those attempts multiplies the benefit by forcing effortful reconstruction each time [Testing effect improves long-term retention.](../claims/retrieval-practice-improves-retention.md) [+S]. The combination outperforms either technique alone: spaced *rereading* is weaker than spaced *retrieval*, because the difficulty of successful recall is what drives durable learning. Optimal spacing expands as retention intervals lengthen — the gap between sessions should be roughly 10–20% of the desired retention period.

### Context
#### Requirements
- A bank of retrieval prompts (questions, problems, prompts to summarize) mapped to learning objectives
- A schedule that revisits material at expanding intervals ([Spaced Repetition](../elements/spaced-repetition.md))
- Feedback after each attempt, especially for incorrect or incomplete recalls
- Learners must actually attempt recall before seeing answers — the prompt must come first
- A bank of recall prompts (questions, flashcards, problems) targeting the material
- A schedule that revisits material at expanding intervals (e.g., 1 day → 3 days → 1 week → 3 weeks)
- Feedback or answer-checking so errors are corrected, not rehearsed ([Feedback](../elements/feedback.md))
- Enough curricular time for multiple brief sessions rather than one long one

#### Constraints
- Retrieval attempts that consistently fail (success rate well below ~80%) can encode errors and frustrate learners [Retrieval practice benefits diminish when retrieval repeatedly fails.](../claims/retrieval-failure-reduces-benefit.md) [-M] — calibrate difficulty or provide partial cues
- Learners judge spaced retrieval as harder and less effective than massed rereading, and disengage if the design does not explain why difficulty is desirable [Learners misjudge spaced practice as less effective than massed practice.](../claims/learners-misjudge-spacing-benefits.md) [-M]
- Spacing gains shrink for highly complex, integrated skills where "forgetting" between sessions costs more than the spacing buys [~W]
- Requires sustained engagement over days or weeks; single-session implementations cannot realize the spacing effect
- Learners experience retrieval as harder and less productive than rereading, and often abandon it [Learners misjudge their own learning, preferring massed rereading despite worse retention.](https://doi.org/10.1111/j.1467-9280.2006.01693.x) [-M] — illusions of fluency from massed study drive poor self-regulation of study choices
- Spacing gains shrink or reverse when the material is highly complex or when intervals exceed the retention horizon of the assessment [~M]
- Retrieval of partially learned material without feedback can entrench errors [-M]
- Very short intervals collapse spacing into massing; very long intervals produce failed retrievals with little benefit [~S]

#### Implementation Variability
- **Expanding vs. equal intervals:** expanding schedules (1 day → 3 days → 1 week) generally match or beat fixed intervals for retention
- **In-class vs. technology-mediated:** tools like [Anki](https://apps.ankiweb.net) and [Quizlet Learn](https://quizlet.com) automate scheduling with spaced-repetition algorithms; teachers can approximate with cumulative weekly quizzes
- **Cumulative quizzing:** rather than unit-by-unit tests, each quiz samples from all prior material — a low-tech, high-yield variant
- **Retrieval formats:** free recall, cued recall, application problems, and brief summaries all work; varied formats support transfer better than a single repeated format
- **Expanding vs. equal intervals:** expanding schedules (doubling gaps) are generally as good or better than fixed ones and are easier to schedule [~M]
- **Cumulative quizzing:** rather than unit-by-unit tests, each quiz samples from all prior content — a low-tech way to enforce spacing at course scale
- **Adaptive flashcard systems:** algorithms (e.g., Leitner boxes, SM-2) select items for review based on individual recall success
- **Interleaving:** mixing problem *types* within spaced sessions adds discrimination practice, especially valuable in mathematics [~S]

### Target Learners
- All age groups benefit, including young children and older adults [Spaced practice improves long-term retention across ages.](../claims/spaced-practice-improves-retention.md) [+S]
- Learners preparing for cumulative or delayed assessments (licensing exams, end-of-year tests)
- Learners with weaker metacognition need explicit framing, since they are most likely to abandon the strategy when it feels difficult
- All age groups benefit, from early readers to medical residents; effects are among the most age-general in the literature [+S]
- Learners preparing for cumulative or high-stakes assessments, where retention over weeks matters more than momentary fluency
- Struggling learners need shorter initial intervals and more feedback; the schedule, not the technique, must adapt [~M]
- Less suited to learners who need only momentary performance (e.g., a presentation tomorrow) — cramming wins for immediate but not delayed tests [~S]

### Target Learning Goals
- Long-term retention of declarative knowledge: facts, definitions, vocabulary, formulas
- Fluency and automaticity of foundational skills that later learning depends on
- Cumulative course structures where earlier material must remain accessible
- Long-term retention of factual and conceptual knowledge
- Fluency and automaticity in foundational skills ([Automaticity](../elements/automaticity.md))
- Cumulative course mastery where later content builds on earlier content

### Instructions
1. Identify the core knowledge and skills that must remain retrievable over time, and write retrieval prompts for each ([Learning Objectives](../elements/learning-objectives.md)).
2. Schedule the first retrieval shortly after initial instruction, then at expanding intervals ([Spaced Repetition](../elements/spaced-repetition.md)).
3. Present prompts *before* any review material; require an actual attempt ([Practice](../elements/practice.md)).
4. Provide immediate corrective feedback after each attempt ([Feedback](../elements/feedback.md)).
5. Explain the strategy to learners — why effortful recall and spacing feel harder but work better — to sustain buy-in.
6. Track performance and re-insert items that were recalled incorrectly at shorter intervals ([Adaptive Difficulty](../elements/adaptive-difficulty.md)).

## Related Strategies
- [Interleaved Practice](interleaved-practice.md) — mixes problem types within sessions; combines naturally with spacing
- [Cumulative Quizzing](cumulative-quizzing.md) — a classroom implementation of spaced retrieval
- [Elaborative Interrogation](elaborative-interrogation.md) — "why" questions add depth to what is retrieved

## Examples
- **[Anki](https://apps.ankiweb.net)** — open-source spaced-repetition flashcard software using the SM-2 expanding-interval algorithm; widely used in medical education.
- **[Quizlet Learn](https://quizlet.com)** — adapts question scheduling based on items a learner has missed, spacing review of weak items.
- **Cumulative low-stakes quizzing** — courses that begin each class with a short quiz sampling all prior units show large gains on final exams relative to unit-only testing.
- **[DuoLingo](https://www.duolingo.com)** — schedules review of previously learned vocabulary at expanding intervals interleaved with new material.
- **[Anki](https://apps.ankiweb.net)** — open-source spaced-repetition flashcard system using the SM-2 algorithm to schedule expanding review intervals per item.
- **[Duolingo](https://www.duolingo.com)** — schedules review of previously learned vocabulary and grammar just before predicted forgetting, interleaved with new content.
- **[Khan Academy](https://www.khanacademy.org)** — mastery system re-surfaces earlier skills in later exercises, requiring spaced retrieval across units.
- **Medical education "spaced curricula"** — pharmacology and anatomy content revisited across clerkships rather than taught once, a structure adopted by several medical schools following retention research.

## Key Sources
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966–968. [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408)
- Kang, S. H. K. (2016). Spaced repetition promotes efficient and effective learning: Policy implications of innovations in teaching and learning. *Policy Insights from the Behavioral and Brain Sciences, 3*(1), 12–19. [doi:10.1177/2372732215624708](https://doi.org/10.1177/2372732215624708)

<!-- merged 2026-10-09 from strategies/spaced_retrieval_practice ("Spaced Retrieval Practice"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Spaced Retrieval Practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Spaced retrieval practice combines two of the most robust findings in learning science: *spacing* (distributing study or practice across multiple sessions separated in time) and *retrieval practice* (actively recalling information from memory rather than rereading it). Learners attempt to recall material, receive feedback, and then revisit the material after a delay — with intervals that grow progressively longer as mastery stabilizes.

## Design Implications

Retrieval attempts strengthen memory more than restudying of equivalent duration, and spaced schedules dramatically improve long-term retention relative to massed study [Dunlosky et al. rated practice testing and distributed practice among the highest-utility techniques.](https://doi.org/10.1177/1529100612453266) [+S]. The two mechanisms are complementary: spacing forces effortful reconstruction at each encounter, while retrieval makes each spaced encounter a memory-strengthening event rather than a passive review. Effective implementations schedule review *just* as forgetting begins — the desirable difficulty that maximizes encoding benefit [~S].

### Context
#### Requirements
- A bank of recall prompts (questions, flashcards, problems) targeting the material
- A schedule that revisits material at expanding intervals (e.g., 1 day → 3 days → 1 week → 3 weeks)
- Feedback or answer-checking so errors are corrected, not rehearsed ([Feedback](../elements/feedback.md))
- Enough curricular time for multiple brief sessions rather than one long one

#### Constraints
- Learners experience retrieval as harder and less productive than rereading, and often abandon it [Learners misjudge their own learning, preferring massed rereading despite worse retention.](https://doi.org/10.1111/j.1467-9280.2006.01693.x) [-M] — illusions of fluency from massed study drive poor self-regulation of study choices
- Spacing gains shrink or reverse when the material is highly complex or when intervals exceed the retention horizon of the assessment [~M]
- Retrieval of partially learned material without feedback can entrench errors [-M]
- Very short intervals collapse spacing into massing; very long intervals produce failed retrievals with little benefit [~S]

#### Implementation Variability
- **Expanding vs. equal intervals:** expanding schedules (doubling gaps) are generally as good or better than fixed ones and are easier to schedule [~M]
- **Cumulative quizzing:** rather than unit-by-unit tests, each quiz samples from all prior content — a low-tech way to enforce spacing at course scale
- **Adaptive flashcard systems:** algorithms (e.g., Leitner boxes, SM-2) select items for review based on individual recall success
- **Interleaving:** mixing problem *types* within spaced sessions adds discrimination practice, especially valuable in mathematics [~S]

### Target Learners
- All age groups benefit, from early readers to medical residents; effects are among the most age-general in the literature [+S]
- Learners preparing for cumulative or high-stakes assessments, where retention over weeks matters more than momentary fluency
- Struggling learners need shorter initial intervals and more feedback; the schedule, not the technique, must adapt [~M]
- Less suited to learners who need only momentary performance (e.g., a presentation tomorrow) — cramming wins for immediate but not delayed tests [~S]

### Target Learning Goals
- Long-term retention of factual and conceptual knowledge
- Fluency and automaticity in foundational skills ([Automaticity](../elements/automaticity.md))
- Cumulative course mastery where later content builds on earlier content

### Instructions
1. Break target knowledge into discrete, testable items or problems.
2. Schedule the first retrieval shortly after initial instruction ([Practice](../elements/practice.md)), then at expanding intervals.
3. Require actual recall — writing, answering, or solving — before revealing answers; rereading does not substitute.
4. Provide immediate corrective feedback ([Feedback](../elements/feedback.md)) and re-schedule missed items at shorter intervals.
5. Lengthen intervals as items are consistently recalled; drop or archive mastered items.
6. Use cumulative low-stakes quizzes to institutionalize spacing across the course ([Assessment](../elements/assessment.md)).

## Related Strategies
- [Interleaved Practice](interleaved-practice.md) — mixing problem types within sessions; combines with spacing for stronger discrimination learning
- [Cumulative Quizzing](cumulative-quizzing.md) — course-level mechanism for enforcing spaced retrieval
- [Elaborative Interrogation](elaborative-interrogation.md) — "why" questions that can be embedded in retrieval prompts

## Examples
- **[Anki](https://apps.ankiweb.net)** — open-source spaced-repetition flashcard system using the SM-2 algorithm to schedule expanding review intervals per item.
- **[Duolingo](https://www.duolingo.com)** — schedules review of previously learned vocabulary and grammar just before predicted forgetting, interleaved with new content.
- **[Khan Academy](https://www.khanacademy.org)** — mastery system re-surfaces earlier skills in later exercises, requiring spaced retrieval across units.
- **Medical education "spaced curricula"** — pharmacology and anatomy content revisited across clerkships rather than taught once, a structure adopted by several medical schools following retention research.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/j.1467-9280.2006.01693.x](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
- Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966–968. [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Kang, S. H. K. (2016). Spaced repetition promotes efficient and effective learning: Policy implications of innovations in teaching and learning. *Policy Insights from the Behavioral and Brain Sciences, 3*(1), 12–19. [doi:10.1177/2372732215624708](https://doi.org/10.1177/2372732215624708)
-->
