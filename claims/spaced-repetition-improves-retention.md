---
type: claim
title: Spaced Repetition Improves Retention
status: draft
generated:
  by: "claude/unspecified"
  at: 2026-08-30
id: spaced-repetition-improves-retention
evidence_strength: strong
---

# Spaced Repetition Improves Retention

> **Claim** · [All claims](index.md)
> **Evidence** · none recorded yet

Distributing study of a given item across multiple sessions separated by time produces stronger long-term retention than massing the same amount of study into a single session. The advantage grows as the retention interval lengthens [+S].

## Subclaims

<!-- TODO -->

## Evidence

<!-- TODO -->

## Discussion

**The spacing effect is one of the most robust findings in memory research**, but this page's Evidence section has not yet been populated with specific studies, so no effect sizes or scope claims are asserted here. The canonical literature — beginning with Ebbinghaus's forgetting-curve experiments and extending through modern meta-analyses of verbal learning and classroom studies — consistently favors spaced over massed practice for delayed retention tests, with the advantage growing as the retention interval lengthens [+S].

**Optimal gap depends on retention interval.** A recurring moderator in the literature is that the best spacing gap scales with how long the learner needs to remember: gaps that are optimal for a test one week later are too short for a test six months later [~M]. Designers of [adaptive-learning](../patterns/adaptive-learning.md) systems and flashcard tools should treat spacing as a parameter to tune, not a fixed rule.

**Mechanism.** Dominant accounts attribute the effect to encoding variability and to desirable-difficulty processes — spaced study requires effortful retrieval and reconstruction of fading traces, which strengthens them more than the fluent, easy processing that massed study affords [+M]. This links spacing to [retrieval practice](retrieval-practice-improves-retention.md), which compounds with spacing when spaced sessions require active recall rather than rereading [+M].

**Boundary conditions.** Spacing benefits are clearest for retention of discrete, relearnable items (vocabulary, facts, skills components). Complex, integrative tasks may benefit more from interleaving and varied practice than from simple temporal spacing of identical material [~W] — see [Interleaving Improves Inductive Learning](interleaving-improves-inductive-learning.md).

**Learner perception.** Learners often judge massed study more effective because it feels fluent, while spaced study feels harder — a metacognitive illusion that can suppress spontaneous spacing [-M]. Explicit instruction about the spacing effect can partially correct this [+W].

**Design implication.** Because the effect is robust but its parameters are context-sensitive, practical implementations (expanding-interval flashcard schedules such as those in [Anki](https://apps.ankiweb.net/) or [SuperMemo](https://www.supermemo.com/), spaced homework in course design) should pair scheduling with [retrieval practice](retrieval-practice-improves-retention.md) rather than rereading, and should calibrate gaps to the intended retention horizon.

## Related Claims

- [Retrieval Practice Improves Retention](retrieval-practice-improves-retention.md) — retrieval practice and spacing compound; spaced retrieval is the strongest known retention combination
- [Interleaving Improves Inductive Learning](interleaving-improves-inductive-learning.md) — a related temporal-distribution effect operating across item categories rather than sessions
- [Chunking Reduces Working Memory Load](chunking-reduces-working-memory-load.md) — within-session organization of material that spacing complements across sessions
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — the theoretical frame for why effortful spaced processing strengthens encoding
- [Adaptive Learning Improves Outcomes](adaptive-learning-improves-outcomes.md) — adaptive platforms operationalize spacing by scheduling reviews at expanding intervals