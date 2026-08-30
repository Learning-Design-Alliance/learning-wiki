---
type: strategy
title: Spaced Scheduling
description: Distributing learning episodes and reviews over time rather than massing them together, exploiting the spacing effect to improve long-term retention.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Spaced Scheduling

## Description
Spaced scheduling distributes study, practice, or review sessions across time — separated by hours, days, or weeks — instead of concentrating them in a single block. It is typically implemented as a fixed schedule (e.g., review at 1 day, 1 week, 1 month) or an expanding schedule in which intervals lengthen as material becomes more secure (spaced repetition).

## Design Implications

Spacing produces substantially better long-term retention than massed study of the same total duration, one of the most robust findings in learning science [Dunlosky et al. rate spaced practice among the highest-utility techniques.](../claims/spaced-practice-improves-retention.md) [+S]. The mechanism is generally attributed to encoding variability and to desirable difficulty: after a delay, retrieval requires partial effortful reconstruction, which strengthens the memory trace more than easy, immediate recall. Spacing works best when each spaced encounter involves active retrieval rather than passive rereading — pairing it with [Practice](../elements/practice.md) and retrieval formats multiplies the benefit.

### Context
#### Requirements
- Content that can be revisited in multiple short encounters rather than one long session
- A schedule or algorithm that determines when material reappears (fixed intervals, expanding intervals, or learner-performance-triggered)
- Retrieval-based activities at each encounter; spacing rereading alone yields weaker gains
- Enough lead time before a criterion test for at least one or two spaced reviews

#### Constraints
- Spacing feels harder and slower than massing, so learners systematically prefer it and judge it less effective [Learners misjudge their own learning, favoring massed study despite worse retention.](../claims/spaced-practice-improves-retention.md) [-S] — without guidance, learners default to cramming
- Gains are largest for retention after delay; for immediate performance, massed practice can look equal or better [~S]
- Very short intervals (seconds) or very long intervals relative to the retention interval reduce the effect [~S]
- Less applicable to complex, integrative skill performance that requires sustained, connected practice sessions rather than isolated item review

#### Implementation Variability
- **Fixed schedule**: reviews at predetermined intervals (e.g., 1 day, 1 week, 1 month); simple to design, slightly less efficient
- **Expanding schedule (spaced repetition)**: intervals grow as items are mastered; used by flashcard systems such as Anki and SuperMemo
- **Cumulative review**: older material is folded into each new unit's practice, common in mathematics curricula (e.g., *Everyday Mathematics*)
- **Interleaved spacing**: spacing combined with alternating problem types; see [Interleaving](interleaving.md) for the distinct but complementary effect

### Target Learners
- All learners benefit, but the effect is especially valuable for learners building durable foundational knowledge (vocabulary, facts, procedures) [+S]
- Learners prone to cramming under assessment pressure need explicit scheduling support, since their metacognitive judgments favor massing [-S]
- Younger learners may need the schedule managed for them; self-regulated learners can run their own spaced-repetition systems

### Target Learning Goals
- Long-term retention of facts, concepts, vocabulary, and procedures
- Fluency and automaticity maintenance after initial acquisition
- Cumulative mastery in courses where later content depends on earlier content

### Instructions
1. Break target content into small, independently retrievable units ([Chunking](../principles/chunking.md)).
2. Schedule the first review within 1–2 days of initial learning, then at expanding intervals scaled to the retention deadline.
3. At each spaced encounter, require retrieval — a quiz, flashcard, or problem — rather than rereading ([Practice](../elements/practice.md)).
4. Adjust intervals based on retrieval success: failed retrieval shortens the next interval; easy success lengthens it.
5. Make the schedule visible to learners and explain why spacing feels harder but works better, to counteract the preference for cramming.

## Related Strategies
- [Retrieval Practice](retrieval-practice.md) — the active component that makes each spaced encounter effective
- [Interleaving](interleaving.md) — mixes item types within and across sessions; combines with spacing for large retention gains
- [Cumulative Review](cumulative-review.md) — a course-level way of institutionalizing spacing
- [Cramming](cramming.md) — the massed alternative; useful for immediate performance but poor for retention

## Examples
- **Anki** (https://apps.ankiweb.net) — open-source spaced-repetition system using the SM-2 expanding-interval algorithm; widely used in medical education for high-volume factual learning.
- **Duolingo** (https://www.duolingo.com) — schedules review of previously learned vocabulary and grammar based on learner performance and predicted forgetting.
- ***Everyday Mathematics*** (https://everydaymath.uchicago.edu) — elementary mathematics curriculum built on distributed practice and cumulative review across units.
- **Kang (2016)** — classroom study in which eighth-grade students' quiz questions were spaced across lessons, improving final-exam performance on spaced material.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Kang, S. H. K. (2016). Spaced repetition promotes efficient and effective learning: Policy implications of innovations in teaching and learning. *Educational Psychology Review, 28*(4), 809–830. [doi:10.1177/2372732215624708](https://doi.org/10.1177/2372732215624708)
- Rohrer, D., & Taylor, K. (2006). The effects of overlearning and distributed practice on the retention of mathematics knowledge. *Applied Cognitive Psychology, 20*(9), 1209–1224. [doi:10.1002/acp.1248](https://doi.org/10.1002/acp.1248)