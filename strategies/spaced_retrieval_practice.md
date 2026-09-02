---
type: strategy
id: spaced_retrieval_practice
title: Spaced Retrieval Practice
description: Distributing retrieval attempts over time and across sessions so learners must reconstruct knowledge from memory rather than re-expose themselves to it.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Spaced Retrieval Practice

> **Strategy** · [All strategies](index.md)

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
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966–968. [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Kang, S. H. K. (2016). Spaced repetition promotes efficient and effective learning: Policy implications of innovations in teaching and learning. *Policy Insights from the Behavioral and Brain Sciences, 3*(1), 12–19. [doi:10.1177/2372732215624708](https://doi.org/10.1177/2372732215624708)