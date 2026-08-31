---
type: strategy
title: Distributed Practice
description: Distributed practice involves practicing content in short sessions spaced out over time, contrasting with massed practice (cramming) where content is practiced in one long session.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Distributed Practice

## Description
Distributed practice (spacing) involves practicing content in short sessions separated by intervals of time, rather than in one long massed session. It leverages the principle that some forgetting between sessions is productive: the effort to reconstruct partially forgotten material strengthens retrieval routes and slows subsequent forgetting. Spacing works best after initial learning reaches reasonable accuracy, with intervals scaled to the time until assessment — one common heuristic places gaps at roughly 10–20% of the retention interval.

## Design Implications

Distributed practice is one of the most robust findings in learning science: across hundreds of studies, spaced practice produces substantially better long-term retention than massed practice of equal total duration [Spaced practice produces superior long-term retention compared to massed practice.](../claims/spacing-improves-long-term-retention.md) [+S]. Its counterintuitive cost is that spacing feels less effective in the moment — learners misinterpret the difficulty of retrieval as poor learning, and prefer cramming because it produces fluent short-term performance [Learners often misjudge their learning, favoring less effective strategies like rereading over retrieval and spacing.](../claims/learners-misjudge-effective-learning-strategies.md) [+M]. Effective implementation therefore requires explicit scheduling structures and, ideally, instruction about why desirable difficulty helps.

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
- Learners of all ages, from children to older adults; the effect is remarkably general across materials and populations [Spaced practice produces superior long-term retention compared to massed practice.](../claims/spacing-improves-long-term-retention.md) [+S]
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
- Rohrer, D., & Taylor, K. (2006). The effects of overlearning and distributed practice on the retention and transfer of mathematics skills. *Applied Cognitive Psychology, 20*(9), 1209–1224. [doi:10.1002/acp.1266](https://doi.org/10.1002/acp.1266)
- Bjork, R. A., & Bjork, E. L. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning. In M. A. Gernsbacher et al. (Eds.), *Psychology and the real world* (pp. 56–64). Worth Publishers.