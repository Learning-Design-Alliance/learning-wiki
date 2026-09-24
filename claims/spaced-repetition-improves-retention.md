---
type: claim
title: Spaced Repetition Improves Retention
status: draft
generated:
  by: "claude/unspecified"
  at: 2026-08-30
id: spaced-repetition-improves-retention
evidence_strength: strong
sources:
  - id: cepeda-et-al-2006
    resource: "https://doi.org/10.1037/0033-2909.132.3.354"
    title: "Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)"
    author: "Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D."
    q: 4
    i: 2
  - id: cepeda-et-al-2008
    resource: "https://doi.org/10.1111/j.1467-9280.2008.02209.x"
    title: "Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science, 19*(11), 1095–1102. [doi:10.1111/j.1467-9280.2008.02209.x](https://doi.org/10.1111/j.1467-9280.2008.02209.x)"
    author: "Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H."
    q: 3
    i: 2
  - id: donovan-radosevich-1999
    resource: "https://doi.org/10.1037/0021-9010.84.5.795"
    title: "Donovan, J. J., & Radosevich, D. J. (1999). A meta-analytic review of the distribution of practice effect: Now you see it, now you don't. *Journal of Applied Psychology, 84*(5), 795–805. [doi:10.1037/0021-9010.84.5.795](https://doi.org/10.1037/0021-9010.84.5.795)"
    author: "Donovan, J. J., & Radosevich, D. J."
    q: 4
    i: 2
---

# Spaced Repetition Improves Retention

> **Claim** · [All claims](index.md)
> **Evidence** · 3 studies · `q4` two meta-analyses · `i2` medium · gap scales with retention interval

Distributing study of a given item across multiple sessions separated by time produces stronger long-term retention than massing the same amount of study into a single session. The advantage grows as the retention interval lengthens [+S].

## Subclaims

`q4 i2` A quantitative synthesis of the verbal-recall literature found spaced practice superior to massed practice, with the advantage increasing as the retention interval lengthened. [→ Cepeda et al. 2006](#cepeda-et-al-2006)

`q3 i2` The optimal gap scales with how long the material must be retained: gaps that maximise recall at one week are too short for a test months later. There is no fixed best interval to configure. [→ Cepeda et al. 2008](#cepeda-et-al-2008)

`q4 i2` A meta-analysis outside the verbal-learning laboratory, covering task practice, put the distribution-of-practice effect at d = 0.46 and found it moderated by task complexity. [→ Donovan & Radosevich 1999](#donovan-radosevich-1999)

## Evidence

### Cepeda et al. 2006

Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380. [doi:10.1037/0033-2909.132.3.354](https://doi.org/10.1037/0033-2909.132.3.354)

`q4` · `i2`

A review and quantitative synthesis of distributed-practice studies in verbal recall, covering several hundred experiments. Spacing beat massing broadly, and the interaction with retention interval was the robust moderator: the longer the delay before test, the larger the advantage.

### Cepeda et al. 2008

Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science, 19*(11), 1095–1102. [doi:10.1111/j.1467-9280.2008.02209.x](https://doi.org/10.1111/j.1467-9280.2008.02209.x)

`q3` · `i2`

An experiment varying the gap between two study sessions and the interval before test across a wide grid, producing a ridgeline of optimal gaps rather than a single value. The optimal gap was a rising function of the retention interval. This is the study that makes spacing a parameter to tune against an intended retention horizon rather than a fixed schedule.

### Donovan & Radosevich 1999

Donovan, J. J., & Radosevich, D. J. (1999). A meta-analytic review of the distribution of practice effect: Now you see it, now you don't. *Journal of Applied Psychology, 84*(5), 795–805. [doi:10.1037/0021-9010.84.5.795](https://doi.org/10.1037/0021-9010.84.5.795)

`q4` · `i2`

A meta-analysis of distribution-of-practice effects across task types, reporting d = 0.46 overall and substantial moderation by task complexity — the effect was smaller for complex tasks. Included here because it tests the generalisation outside verbal recall, where most of the other evidence sits.

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