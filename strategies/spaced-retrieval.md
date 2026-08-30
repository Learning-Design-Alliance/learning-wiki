---
type: strategy
title: Spaced Retrieval
description: Scheduling recall attempts at increasing intervals over time so that effortful retrieval, rather than rereading, drives durable memory.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Spaced Retrieval

## Description
Spaced retrieval combines two of the most robust findings in learning science: *spacing* (distributing study across time rather than massing it) and *retrieval practice* (actively recalling information instead of rereading it). Learners attempt to recall material, receive feedback, and then revisit it after a delay — with intervals expanding as memory strengthens (e.g., one day, three days, one week). The strategy is carried out through low-stakes quizzes, flashcards, cumulative review, or prompts embedded in later lessons.

## Design Implications

Retrieval attempts strengthen memory more than restudying of equivalent duration, and the advantage grows when retrieval is spaced over time rather than immediately repeated [~S]. The two effects are complementary: spacing introduces *desirable difficulty* by partially weakening memory, forcing effortful reconstruction at each recall attempt. Success depends on feedback — retrieval without correction can entrench errors, so every recall attempt should be followed by verification.

### Context
#### Requirements
- Identifiable core content worth retaining long-term (facts, definitions, procedures, formulas)
- A schedule that revisits material at expanding intervals, not a single review
- Feedback or answer-checking after each retrieval attempt
- Low-stakes framing so retrieval functions as learning, not evaluation ([Assessment](../elements/assessment.md) for learning rather than of learning)

#### Constraints
- Learners experience retrieval as harder and less productive than rereading, and often abandon spaced systems prematurely [~S] — perceived fluency from rereading masquerades as learning
- Spacing benefits shrink for highly complex or rapidly changing material where the underlying schema, not the memory trace, is the bottleneck
- Retrieval of partially learned or never-encoded material yields little benefit and can reinforce guessing if feedback is delayed or absent
- Expanding schedules require tracking; without a system (software or instructor-managed review), spacing collapses into cramming

#### Implementation Variability
- **Expanding vs. fixed intervals:** expanding schedules (1 day → 3 days → 1 week) are generally efficient; fixed short intervals work well for very new material
- **Cumulative quizzing:** each assessment includes items from prior units, embedding spacing without a separate review system
- **Flashcard scheduling:** algorithms such as those in Anki or SuperMemo automate interval selection
- **Interleaved retrieval:** mixing item types within a session adds discrimination practice on top of spacing

### Target Learners
- Learners of all ages; spacing benefits appear from early childhood through adulthood and across subject domains [~S]
- Learners preparing for cumulative or delayed assessments (licensing exams, end-of-course tests)
- Struggling learners benefit, but need more frequent initial retrieval and tighter intervals before expansion
- Less useful for learners who already retrieve the material effortlessly — successful, easy recall adds little; difficulty must be calibrated

### Target Learning Goals
- Long-term retention of declarative knowledge: vocabulary, facts, definitions, formulas
- Automaticity of foundational procedures so working memory is freed for higher-order tasks
- Maintenance of previously mastered skills over months and years

### Instructions
1. Identify the small set of high-value items that must be retained (not everything deserves spacing).
2. Ensure material is initially understood and encoded — retrieval does not substitute for first teaching ([Chunking](../principles/chunking.md) reduces initial load).
3. Schedule the first retrieval within 24–48 hours of initial learning.
4. Present a retrieval prompt ([Practice](../elements/practice.md), quiz item, or flashcard) and require an actual recall attempt — written or spoken, not a recognition glance.
5. Provide immediate feedback and re-study for missed items, then shorten that item's next interval.
6. Expand intervals for successfully recalled items (e.g., 1 day → 3 days → 1 week → 1 month).
7. Make the schedule visible and explain the rationale to learners, since the effort of retrieval is otherwise misread as ineffectiveness.

## Related Strategies
- Cumulative quizzing — the classroom-scale implementation of spaced retrieval across a course
- Interleaved practice — combines spacing with discrimination between problem types
- Rereading and highlighting — the common alternatives that spaced retrieval replaces; less effective at equal time

## Examples
- **[Anki](https://apps.ankiweb.net)** — spaced-repetition flashcard software using the SM-2 expanding-interval algorithm; widely used in medical education for high-volume factual retention.
- **[Duolingo](https://www.duolingo.com)** — schedules review of previously learned vocabulary at expanding intervals interleaved with new material.
- **Cumulative midterm/final design** — courses where each quiz includes 20–30% items from prior units, converting assessment into spaced retrieval without extra study time.
- **Retrieval warm-ups** — opening a class with two or three recall questions from the previous week before introducing new content.

## Key Sources
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255. [doi:10.1111/medu.12141](https://doi.org/10.1111/medu.12141)
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966–968. [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Bjork, R. A., & Bjork, E. L. (2020). Desirable difficulties in theory and practice. *Journal of Applied Research in Memory and Cognition, 9*(4), 475–479. [doi:10.1016/j.jarmac.2020.09.003](https://doi.org/10.1016/j.jarmac.2020.09.003)