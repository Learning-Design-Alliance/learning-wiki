---
type: strategy
title: Distributed Practice (Spaced Learning)
description: Distributed practice involves reviewing information or practicing skills across multiple sessions spread out over time, rather than in one continuous session (massed practice).
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Distributed Practice (Spaced Learning)

## Description
Distributed practice, also known as spaced learning, involves reviewing information or practicing skills across multiple sessions spread out over time, rather than in one continuous session (massed practice). It leverages the spacing effect: spaced reviews produce superior long-term retention compared to cramming, because the gaps between encounters make retrieval more effortful, which strengthens the memory trace. Spacing also encodes material with varied contextual cues, supporting transfer and generalization.

## Design Implications

Distributed practice is one of the most robust findings in learning science, with meta-analyses showing large, durable advantages of spaced over massed study across ages, materials, and retention intervals. Its effectiveness depends on scheduling: gaps that are too short produce little benefit, while optimal gaps scale with the retention interval — longer delays before the test call for longer spacing. Spacing works best when each session requires actual retrieval rather than passive re-reading, pairing naturally with [Practice](../elements/practice.md) and retrieval-based activities.

### Context
#### Requirements
- Structured review materials and a schedule that revisits content at planned intervals
- A mechanism to track spacing (planner, LMS scheduling, or spaced-repetition software)
- Review tasks that require retrieval or application, not mere re-exposure

#### Constraints
- Requires advance planning; cramming is easier to organize and often feels more productive to learners [~S]
- Learners systematically misjudge spacing: massed practice feels effective in the moment, so learners left to their own preferences under-space their study [-M]
- Benefits diminish when review sessions become passive re-reading rather than retrieval [-M]
- Very short spacing intervals (seconds to minutes within a session) yield little advantage over massed practice [~S]

#### Implementation Variability
- **Fixed spacing**: equal intervals between sessions (e.g., weekly review)
- **Expanding spacing**: intervals grow after each successful recall (e.g., 1 day, 3 days, 1 week)
- **Interleaving within sessions**: mixing problem types or topics across sessions, which compounds spacing benefits for discrimination and transfer
- **Curriculum-embedded spacing**: revisiting prior-unit content in homework and warm-ups rather than using dedicated software

### Target Learners
- Effective across all ages, from early childhood through adult learning [~S]
- Particularly valuable for learners building long-term knowledge bases — vocabulary, facts, procedures, and skills requiring durable retention
- Learners need explicit guidance on *why* spacing feels harder but works better, since metacognitive misjudgment otherwise drives them back to cramming [-M]

### Target Learning Goals
- Long-term retention of factual and conceptual knowledge
- Durable procedural skill acquisition (mathematics, music, motor skills)
- Transfer and generalization, supported by varied contexts across sessions

### Instructions
1. Identify content that must be retained long-term and schedule its first review within days of initial instruction.
2. Design each review session as a retrieval activity — [Practice](../elements/practice.md) problems, self-quizzing, or application tasks — rather than re-reading.
3. Space subsequent sessions at expanding intervals, adjusting to learner performance; use [Continuous Review](../elements/continuous-review.md) structures to embed review into ongoing coursework.
4. Provide [Feedback](../elements/provide-feedback.md) promptly in each session so errors are corrected before they consolidate.
5. Teach learners about the spacing effect so they can schedule their own study effectively.

## Related Strategies
- [Retrieval Practice](retrieval-practice.md) — the mechanism that makes each spaced session effortful and effective; spacing without retrieval is far weaker
- [Interleaved Practice](interleaved-practice.md) — mixing problem types within and across sessions compounds spacing benefits
- [Mastery Learning](mastery-learning.md) — spacing schedules can be driven by individual mastery rather than fixed calendars

## Examples
- **Vocabulary learning**: reviewing new words at expanding intervals (1 day, 3 days, 1 week, 1 month) rather than repeating them twenty times in one sitting.
- **Mathematics**: re-solving problems from previous units in weekly warm-ups, so procedures from months earlier remain active.
- **[Anki](https://apps.ankiweb.net)** — open-source spaced-repetition software that schedules flashcards using an expanding-interval algorithm based on learner recall success.
- **[Duolingo](https://www.duolingo.org)** — schedules review of previously learned vocabulary and grammar at spaced intervals interleaved with new material.
- **[Khan Academy](https://www.khanacademy.org)** — mastery-based practice automatically revisits earlier skills, distributing practice across the curriculum.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966–968. [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408)
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the Real World*. Worth Publishers.