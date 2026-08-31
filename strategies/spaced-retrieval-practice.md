---
type: strategy
title: Spaced Retrieval Practice
description: Scheduling recall attempts across increasing intervals of time so that learners must reconstruct knowledge from memory rather than re-expose themselves to it.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Spaced Retrieval Practice

> **Strategy** · [All strategies](index.md)

## Description
Spaced retrieval practice combines two of the most robust findings in learning science: *retrieval practice* — actively recalling information from memory rather than rereading it — and *spacing* — distributing those recall attempts across time rather than massing them together. In practice, learners answer questions, solve problems, or summarize material from memory at intervals that grow progressively longer (e.g., one day, then three days, then a week), with feedback provided after each attempt.

## Design Implications

Retrieval attempts strengthen memory more than restudying, and spacing those attempts multiplies the benefit by forcing effortful reconstruction each time [Testing effect improves long-term retention.](../claims/testing-improves-retention.md) [+S]. The combination outperforms either technique alone: spaced *rereading* is weaker than spaced *retrieval*, because the difficulty of successful recall is what drives durable learning. Optimal spacing expands as retention intervals lengthen — the gap between sessions should be roughly 10–20% of the desired retention period.

### Context
#### Requirements
- A bank of retrieval prompts (questions, problems, prompts to summarize) mapped to learning objectives
- A schedule that revisits material at expanding intervals ([Spaced Repetition](../elements/spaced-repetition.md))
- Feedback after each attempt, especially for incorrect or incomplete recalls
- Learners must actually attempt recall before seeing answers — the prompt must come first

#### Constraints
- Retrieval attempts that consistently fail (success rate well below ~80%) can encode errors and frustrate learners [Retrieval practice benefits diminish when retrieval repeatedly fails.](../claims/retrieval-failure-reduces-benefit.md) [-M] — calibrate difficulty or provide partial cues
- Learners judge spaced retrieval as harder and less effective than massed rereading, and disengage if the design does not explain why difficulty is desirable [Learners misjudge spaced practice as less effective than massed practice.](../claims/learners-misjudge-spacing.md) [-M]
- Spacing gains shrink for highly complex, integrated skills where "forgetting" between sessions costs more than the spacing buys [~W]
- Requires sustained engagement over days or weeks; single-session implementations cannot realize the spacing effect

#### Implementation Variability
- **Expanding vs. equal intervals:** expanding schedules (1 day → 3 days → 1 week) generally match or beat fixed intervals for retention
- **In-class vs. technology-mediated:** tools like [Anki](https://apps.ankiweb.net) and [Quizlet Learn](https://quizlet.com) automate scheduling with spaced-repetition algorithms; teachers can approximate with cumulative weekly quizzes
- **Cumulative quizzing:** rather than unit-by-unit tests, each quiz samples from all prior material — a low-tech, high-yield variant
- **Retrieval formats:** free recall, cued recall, application problems, and brief summaries all work; varied formats support transfer better than a single repeated format

### Target Learners
- All age groups benefit, including young children and older adults [Spaced practice improves long-term retention across ages.](../claims/spaced-practice-improves-retention.md) [+S]
- Learners preparing for cumulative or delayed assessments (licensing exams, end-of-year tests)
- Learners with weaker metacognition need explicit framing, since they are most likely to abandon the strategy when it feels difficult

### Target Learning Goals
- Long-term retention of declarative knowledge: facts, definitions, vocabulary, formulas
- Fluency and automaticity of foundational skills that later learning depends on
- Cumulative course structures where earlier material must remain accessible

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

## Key Sources
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966–968. [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408)