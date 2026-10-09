---
type: strategy
id: distributed-practice
aliases: [distributed_practice]
title: Distributed Practice
description: Practicing content in short sessions spaced over time rather than massed into one long session, leveraging desirable difficulties to strengthen long-term retention.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Distributed Practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Distributed practice (spacing) involves practicing content in short sessions separated by intervals of time, in contrast to massed practice (cramming) in a single long session. The gap between sessions allows partial forgetting, so each session requires active reconstruction of the material — a "desirable difficulty" that strengthens the memory trace. It typically begins after initial learning has reached reasonably good accuracy, then repeats at expanding intervals.

## Design Implications

Distributed practice is one of the most robust findings in learning science: spaced retrieval roughly doubles long-term retention relative to massed practice, with effects persisting months to years [+S]. Its power comes from effortful retrieval after partial forgetting — the same mechanism exploited by [Retrieval Practice](../elements/practice.md), with which it is most effective when combined [+S]. Because the effort of reconstruction feels like failure, learners often misjudge its value and prefer easier techniques like re-reading or highlighting that produce weaker learning [+M].

### Context
#### Requirements
- Initial learning to a "pretty good" accuracy baseline before spacing begins (an early massed session is often needed)
- A schedule of short sessions with meaningful gaps — typically days, not minutes — ideally expanding as retention strengthens
- Learner adherence to the schedule; calendar prompts, course structure, or adaptive software can enforce it
- [Feedback](../elements/practice.md) after each retrieval attempt so errors are corrected, not rehearsed
- Initial learning to "pretty good" accuracy before spacing begins — spacing cannot compensate for material never learned
- A schedule that revisits material at increasing intervals, ideally using [Retrieval Practice](../elements/retrieval-practice.md) rather than rereading
- Learner adherence over days or weeks; calendar structures, course design, or software (e.g., flashcard scheduling) must carry the scheduling load, since learners left to their own devices tend to cram

#### Constraints
- Learners perceive spacing as harder and less effective than massing, undermining voluntary adoption [-M] — the subjective fluency of cramming is mistaken for learning
- Spacing requires time to work; it cannot rescue learning the night before an assessment [-S]
- Very short gaps (minutes) or very long gaps (beyond the retention horizon) reduce the benefit [~M] — optimal gap scales with time to test
- For fast-mapping or highly integrated conceptual material, some massing may be appropriate before spacing begins [~W]
- Learners perceive spaced practice as harder and less effective than rereading or cramming, and often abandon it without support [Learners often misjudge their learning, favoring less effective strategies like rereading over retrieval and spacing.](../claims/learners-misjudge-effective-learning-strategies.md) [-M]
- Spacing yields little benefit when material is used only once and never reassessed; the effect depends on at least two encounters separated in time
- Very short intervals (minutes) or intervals approaching the retention interval itself reduce the benefit; the optimal gap shrinks as the test delay shrinks [~S]
- For fast-mapping of brand-new vocabulary or motor skills in early acquisition, some initial massing within a session can be more efficient before spacing kicks in [~M]

#### Implementation Variability
- **Expanding schedules** (intervals grow: 1 day, 3 days, 1 week) vs. **fixed schedules** (equal gaps) — expanding is often slightly better but fixed is easier to administer [~M]
- **Spaced retrieval** (each session tests from memory) vs. **spaced re-study** (each session re-reads) — retrieval versions produce substantially larger effects [+S]
- **Interleaving** related problem types within spaced sessions compounds the benefit for discrimination learning [~M]
- Curriculum-embedded spacing (spiral curricula, cumulative quizzes) vs. learner-managed spacing via flashcard apps
- **Fixed vs. expanding schedules:** expanding intervals (1 day, 3 days, 1 week) generally match or slightly outperform fixed intervals [~M]
- **Interleaving:** alternating problem types within spaced sessions ([Interleaved Practice](interleaved-practice.md)) compounds the benefit, particularly in mathematics [~S]
- **Curriculum-embedded vs. learner-managed:** teachers can build cumulative review into homework and warm-ups, or learners can use spaced-repetition software such as [Anki](https://apps.ankiweb.net) or [Duolingo](https://www.duolingo.com), which schedules review algorithmically

### Target Learners
- Learners of all ages, from early childhood through adulthood [+S]
- Students preparing for exams or certification, and anyone needing retention over months or years
- Learners who rely on re-reading and highlighting — these groups gain most from substitution, though they resist it because it feels less effective [-M]
- Learners of all ages, from children to older adults; the effect is remarkably general across materials and populations [Spaced practice produces superior long-term retention compared to massed practice.](../claims/spaced-practice-improves-retention.md) [+S]
- Especially valuable for learners preparing for delayed assessments (exams, certification, licensure) or building durable professional skills
- Less useful for learners who need performance only in the immediate short term — cramming genuinely wins there, which is precisely why it persists

### Target Learning Goals
- Long-term retention of declarative knowledge (facts, concepts, vocabulary)
- Fluency and durability of procedural skills (e.g., math procedures, music practice)
- Reduced forgetting across a course, enabling cumulative assessment
- Long-term retention of factual and conceptual knowledge
- Durable procedural and motor skill retention (e.g., surgical training, music, athletics)
- Cumulative course mastery where later content builds on earlier content

### Instructions
1. Establish initial accuracy with a focused first session; do not begin spacing before the material is minimally learnable.
2. Schedule the first review 1–3 days later, requiring retrieval from memory rather than re-reading ([Practice](../elements/practice.md)).
3. Provide corrective [Feedback](../elements/practice.md) immediately after each retrieval attempt.
4. Expand intervals as accuracy improves (e.g., 3 days → 1 week → 3 weeks), scaling the final interval to the assessment date.
5. Track decreasing error rates across sessions as evidence that spacing is working; escalate difficulty or interleave related material as fluency grows.

## Related Strategies
- [Retrieval Practice](../elements/practice.md) — the mechanism spacing amplifies; spaced retrieval is the strongest known combination
- [Interleaving](../elements/practice.md) — mixing problem types within spaced sessions adds a second desirable difficulty
- [Cumulative Assessment](../elements/assess-performance.md) — course structures that force spaced review by design
- [Retrieval Practice](retrieval-practice.md) — the activity that fills the spaced sessions; spacing and retrieval combine multiplicatively
- [Interleaved Practice](interleaved-practice.md) — a within-session complement that mixes problem types across spaced reviews
- [Cumulative Review](cumulative-review.md) — curriculum-level mechanism for guaranteeing spacing without learner self-management
- [Sequence simpler desirable difficulties (retrieval, spacing, interleaving) during initial L2 vocabulary encoding, reserving generation for post-encoding consolidation](generation-as-post-encoding-consolidation-strategy.md)

## Examples
- **Anki / spaced-repetition flashcards** ([https://apps.ankiweb.net](https://apps.ankiweb.net)) — implements expanding-interval scheduling for vocabulary, medicine, and law study; used widely in medical education.
- **Spiral curricula in mathematics** (e.g., [Everyday Mathematics](https://www.mheonline.com/em/)) — distributes practice of each concept across the year instead of a single unit, with repeated distributed exposure.
- **Guitar chord practice** — practicing a new chord in short daily sessions over several weeks rather than one long session, matching the CSV example.
- **Cumulative quizzing** — a course in which each weekly quiz includes items from all prior weeks, structurally enforcing spaced retrieval.
- **[Anki](https://apps.ankiweb.net)** — spaced-repetition flashcard software implementing expanding intervals via the SM-2 algorithm; widely used in medical education for high-volume factual retention.
- **[Duolingo](https://www.duolingo.com)** — schedules review of previously learned vocabulary at algorithmically determined intervals, embedding spacing invisibly in the learner's daily session.
- **Cumulative math homework** — Rohrer's research program shows that distributing and interleaving practice problems across a semester's assignments produces large gains on delayed tests compared to blocked, massed problem sets.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Rohrer, D., & Taylor, K. (2007). The shuffling of mathematics problems improves learning. *Instructional Science, 35*(6), 481–498. [doi:10.1007/s11251-007-9015-8](https://doi.org/10.1007/s11251-007-9015-8)
- Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In J. Metcalfe & A. Shimamura (Eds.), *Metacognition: Knowing about knowing* (pp. 185–205). MIT Press.
- Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science, 319*(5865), 966–968. [doi:10.1126/science.1152408](https://doi.org/10.1126/science.1152408)
- Rohrer, D., & Taylor, K. (2006). The effects of overlearning and distributed practice on the retention of mathematics knowledge. *Applied Cognitive Psychology, 20*(9), 1209–1224. [doi:10.1002/acp.1266](https://doi.org/10.1002/acp.1266)
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the real world* (pp. 56–64). Worth Publishers.

<!-- merged 2026-10-09 from strategies/distributed_practice ("Distributed Practice"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Distributed Practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 7 studies (3 quant-synthesis, 2 causal, 1 review, 1 associational), `q2`–`q4` · 2 of 7 report an effect size

## Description
Distributed practice (spacing) involves practicing content in short sessions separated by intervals of time, rather than in one long massed session. It leverages the principle that some forgetting between sessions is productive: the effort to reconstruct partially forgotten material strengthens retrieval routes and slows subsequent forgetting. Spacing works best after initial learning reaches reasonable accuracy, with intervals scaled to the time until assessment — one common heuristic places gaps at roughly 10–20% of the retention interval.

## Design Implications

Distributed practice is one of the most robust findings in learning science: across hundreds of studies, spaced practice produces substantially better long-term retention than massed practice of equal total duration [Spaced practice produces superior long-term retention compared to massed practice.](../claims/spaced-practice-improves-retention.md) [+S]. Its counterintuitive cost is that spacing feels less effective in the moment — learners misinterpret the difficulty of retrieval as poor learning, and prefer cramming because it produces fluent short-term performance [Learners often misjudge their learning, favoring less effective strategies like rereading over retrieval and spacing.](../claims/learners-misjudge-effective-learning-strategies.md) [+M]. Effective implementation therefore requires explicit scheduling structures and, ideally, instruction about why desirable difficulty helps.

### Context
#### Requirements
- Initial learning to "pretty good" accuracy before spacing begins — spacing cannot compensate for material never learned
- A schedule that revisits material at increasing intervals, ideally using [Retrieval Practice](../elements/retrieval-practice.md) rather than rereading
- Learner adherence over days or weeks; calendar structures, course design, or software (e.g., flashcard scheduling) must carry the scheduling load, since learners left to their own devices tend to cram

#### Constraints
- Learners perceive spaced practice as harder and less effective than rereading or cramming, and often abandon it without support [Learners often misjudge their learning, favoring less effective strategies like rereading over retrieval and spacing.](../claims/learners-misjudge-effective-learning-strategies.md) [-M]
- Spacing yields little benefit when material is used only once and never reassessed; the effect depends on at least two encounters separated in time
- Very short intervals (minutes) or intervals approaching the retention interval itself reduce the benefit; the optimal gap shrinks as the test delay shrinks [~S]
- For fast-mapping of brand-new vocabulary or motor skills in early acquisition, some initial massing within a session can be more efficient before spacing kicks in [~M]

#### Implementation Variability
- **Fixed vs. expanding schedules:** expanding intervals (1 day, 3 days, 1 week) generally match or slightly outperform fixed intervals [~M]
- **Interleaving:** alternating problem types within spaced sessions ([Interleaved Practice](interleaved-practice.md)) compounds the benefit, particularly in mathematics [~S]
- **Curriculum-embedded vs. learner-managed:** teachers can build cumulative review into homework and warm-ups, or learners can use spaced-repetition software such as [Anki](https://apps.ankiweb.net) or [Duolingo](https://www.duolingo.com), which schedules review algorithmically

### Target Learners
- Learners of all ages, from children to older adults; the effect is remarkably general across materials and populations [Spaced practice produces superior long-term retention compared to massed practice.](../claims/spaced-practice-improves-retention.md) [+S]
- Especially valuable for learners preparing for delayed assessments (exams, certification, licensure) or building durable professional skills
- Less useful for learners who need performance only in the immediate short term — cramming genuinely wins there, which is precisely why it persists

### Target Learning Goals
- Long-term retention of factual and conceptual knowledge
- Durable procedural and motor skill retention (e.g., surgical training, music, athletics)
- Cumulative course mastery where later content builds on earlier content

### Instructions
1. Establish initial accuracy with a focused first session, using [Practice](../elements/practice.md) until performance is reasonably reliable.
2. Schedule the first review 1–3 days later, using [Retrieval Practice](../elements/retrieval-practice.md) (recall from memory, not rereading).
3. Expand subsequent intervals as recall strengthens — roughly 10–20% of the time remaining until the assessment.
4. Provide [Feedback](../elements/feedback.md) after each retrieval attempt so errors are corrected before the next interval begins.
5. Interleave related topics within sessions where discrimination between categories matters (see [Interleaved Practice](interleaved-practice.md)).
6. Tell learners explicitly that spaced retrieval feels harder but works better, to counteract the fluency illusion.

## Related Strategies

- [Retrieval Practice](retrieval-practice.md) — the activity that fills the spaced sessions; spacing and retrieval combine multiplicatively
- [Interleaved Practice](interleaved-practice.md) — a within-session complement that mixes problem types across spaced reviews
- [Cumulative Review](cumulative-review.md) — curriculum-level mechanism for guaranteeing spacing without learner self-management
- [Sequence simpler desirable difficulties (retrieval, spacing, interleaving) during initial L2 vocabulary encoding, reserving generation for post-encoding consolidation](generation-as-post-encoding-consolidation-strategy.md)

## Related Elements
- [Practice](../elements/practice.md) — the core activity being distributed
- [Feedback](../elements/feedback.md) — corrects errors surfaced by spaced retrieval before forgetting sets in

## Examples
- **[Anki](https://apps.ankiweb.net)** — spaced-repetition flashcard software implementing expanding intervals via the SM-2 algorithm; widely used in medical education for high-volume factual retention.
- **[Duolingo](https://www.duolingo.com)** — schedules review of previously learned vocabulary at algorithmically determined intervals, embedding spacing invisibly in the learner's daily session.
- **Cumulative math homework** — Rohrer's research program shows that distributing and interleaving practice problems across a semester's assignments produces large gains on delayed tests compared to blocked, massed problem sets.

## Key Sources
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Rohrer, D., & Taylor, K. (2006). The effects of overlearning and distributed practice on the retention of mathematics knowledge. *Applied Cognitive Psychology, 20*(9), 1209–1224. [doi:10.1002/acp.1266](https://doi.org/10.1002/acp.1266)
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the real world* (pp. 56–64). Worth Publishers.
-->
