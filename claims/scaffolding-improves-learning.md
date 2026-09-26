---
type: claim
title: Scaffolding improves learning
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: scaffolding-improves-learning
aliases: [scaffolding-improves-learning-outcomes]
evidence_strength: moderate
sources:
  - id: belland-et-al-2017
    resource: "https://doi.org/10.3102/0034654316670999"
    title: "Belland, B. R., Walker, A. E., Kim, N. J., & Lefler, M. (2017). Synthesizing Results From Empirical Research on Computer-Based Scaffolding in STEM Education: A Meta-Analysis. *Review of Educational Research, 87*(2), 309–344. [doi:10.3102/0034654316670999](https://doi.org/10.3102/0034654316670999)"
    author: "Belland, B. R., Walker, A. E., Kim, N. J., & Lefler, M."
    q: 4
    i: 2
    n: 144 studies (333 outcomes)
  - id: van-de-pol-et-al-2010
    resource: "https://doi.org/10.1007/s10648-010-9127-6"
    title: "van de Pol, J., Volman, M., & Beishuizen, J. (2010). Scaffolding in Teacher–Student Interaction: A Decade of Research. *Educational Psychology Review, 22*(3), 271–296. [doi:10.1007/s10648-010-9127-6](https://doi.org/10.1007/s10648-010-9127-6)"
    author: "van de Pol, J., Volman, M., & Beishuizen, J."
    q: 3
    i: "?"
    n: 8 effectiveness studies (of 66 articles screened)
---

# Scaffolding improves learning

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q3`–`q4` · `i2` medium

Learners who receive temporary, adaptive support — hints, prompts, models, or structured tools — during instruction show better learning outcomes than those left to unsupported discovery, provided the support is faded as competence develops.

## Subclaims

`q4 i2` Computer-based scaffolding in STEM problem-centered curricula produces a consistent, medium-sized positive effect on cognitive learning outcomes across a wide range of contexts, learner ages and scaffold designs. [→ Belland et al. 2017](#belland-et-al-2017)

`q3 i?` Across the small set of controlled effectiveness studies published between 1998–2009 on scaffolding in teacher–student interaction, scaffolding (mainly in one-to-one tutoring, on simple well-structured tasks) is consistently reported to improve students' metacognitive and cognitive performance relative to no-scaffolding or less-contingent-support comparison conditions, though the evidence base for classroom (rather than one-to-one) contexts remains thin. [→ van de Pol et al. 2010](#van-de-pol-et-al-2010)

## Evidence

### Belland et al. 2017

Belland, B. R., Walker, A. E., Kim, N. J., & Lefler, M. (2017). Synthesizing Results From Empirical Research on Computer-Based Scaffolding in STEM Education: A Meta-Analysis. *Review of Educational Research, 87*(2), 309–344. [doi:10.3102/0034654316670999](https://doi.org/10.3102/0034654316670999)

`q4 · random-effects meta-analysis` · `i2 · medium effect, ĝ=0.46` · `n=144 studies (333 outcomes)`

A random-effects meta-analysis of 144 experimental studies (333 outcomes) on computer-based scaffolding designed to assist STEM learners — from primary school through adult education — as they worked through ill-structured, problem-centered curricula. Computer-based scaffolding showed a consistently positive effect on cognitive outcomes (ĝ = 0.46) across contexts of use, scaffold characteristics and levels of assessment; the effect did not differ by context-specificity or by whether/how scaffolding was faded, and was greatest when measured at the level of principles and among adult learners. The authors conclude scaffolding "can largely be designed in many different ways while still being highly effective."

### van de Pol et al. 2010

van de Pol, J., Volman, M., & Beishuizen, J. (2010). Scaffolding in Teacher–Student Interaction: A Decade of Research. *Educational Psychology Review, 22*(3), 271–296. [doi:10.1007/s10648-010-9127-6](https://doi.org/10.1007/s10648-010-9127-6)

`q3 · systematic review` · `i? · no pooled effect size reported` · `n=8 effectiveness studies (of 66 articles screened)`

A systematic review of scaffolding research in primary/secondary teacher–student interaction published 1998–2009 (66 articles found; 8 met criteria as controlled effectiveness studies). Reviewed studies — mostly small one-to-one tutoring experiments on simple, well-structured tasks (e.g., long division, balance-scale problems, hypermedia learning of the circulatory system) — found scaffolded/contingent-support conditions outperformed no-support or less-contingent conditions on cognitive and metacognitive measures (e.g., [Pratt & Savoy-Levine 1998] contingent support solved significantly more problems than moderate/high/partial/no-support groups; [Murphy & Messer 2000] one-to-one scaffolding beat small-group work). The review does not compute a pooled effect size and flags that the evidence base is small and concentrated in one-to-one, simple-task settings, with classroom-scale effectiveness understudied.

## Discussion

**Mechanism.** Scaffolding is grounded in Vygotsky's zone of proximal development: support allows learners to perform tasks they could not yet complete independently, and that assisted performance is gradually internalized [+M]. It also aligns with [Cognitive Load Theory](../theories/cognitive-load-theory.md) — well-designed scaffolds reduce extraneous load during early skill acquisition [+S], connecting to [Cognitive load reduction improves learning](../claims/cognitive-load-reduction-improves-learning.md) and [Chunking reduces working memory load](../claims/chunking-reduces-working-memory-load.md).

**Fading is essential.** The defining feature distinguishing scaffolding from mere help is its gradual removal. Support that persists after learners no longer need it becomes redundant and can depress performance [-M] — the same expertise-reversal dynamic documented for worked examples (see [Expertise reversal effect](../theories/expertise-reversal-effect.md)). Designers should plan fading criteria (accuracy, fluency, or self-regulation indicators) at design time, not improvise them.

**Adaptivity is hard to scale.** Much of the strongest scaffolding evidence comes from one-to-one tutoring, where a human tutor continuously calibrates support [+S]. Fixed, non-adaptive scaffolds embedded in curricula show weaker and more variable effects [~M], and poorly timed hints can short-circuit productive struggle [-M]. Adaptive systems attempt to automate this calibration with mixed results — see [Adaptive learning improves outcomes](../claims/adaptive-learning-improves-outcomes.md).

**Boundary conditions.** Scaffolds are most valuable when the task sits squarely in the learner's zone of proximal development: too easy and the scaffold is redundant [~M], too hard and even supported performance exceeds what the learner can appropriate. Scaffold type also matters — support that structures the task (prompts, cue cards, worked models) tends to be more robust than support that simplifies the task itself, which can leave learners practicing a degraded version of the target skill [-M].

**Open questions.** How much scaffolding is optimal for a given learner and task, and how quickly it should be faded, remain open empirical questions; over-scaffolding and under-scaffolding both carry costs. Most evidence concerns well-structured domains (mathematics, science problem-solving); transfer of scaffolding benefits to ill-structured domains is less well established [~W].

*Merged from “Scaffolding improves learning outcomes” (scaffolding-improves-learning-outcomes):* **Mechanism.** Scaffolding is grounded in Vygotsky's zone of proximal development: support allows learners to operate just beyond their independent capability, then fades as internal competence develops. It also functions as a [cognitive load management](../principles/cognitive-load-management.md) technique — by structuring or partitioning complex tasks, scaffolds reduce extraneous load for novices, consistent with [cognitive load theory](../theories/cognitive-load-theory.md). Worked examples are one of the best-studied scaffold forms; see [Example–problem sequences reduce cognitive load and improve learning outcomes](example-problem-sequences-reduce-cognitive-load.md).

**Fading is essential.** A scaffold that is never withdrawn is not scaffolding but permanent support. The value of scaffolding depends on dynamic assessment of learner progress and timely handover of responsibility; static, one-size-fits-all support risks the expertise reversal problem, where help that benefits novices becomes redundant or burdensome for more advanced learners (see [expertise reversal effect](../theories/expertise-reversal-effect.md) and [Worked examples can become redundant or counterproductive for advanced learners](worked-examples-less-effective-with-expertise.md)).

**Boundary conditions.** Scaffolding is most valuable for complex tasks with high element interactivity; for simple or well-practiced tasks it adds overhead without benefit. Effective scaffolds are contingent — calibrated to the learner's current performance in real time — which is difficult to achieve at scale and is a key design challenge for [adaptive learning](../principles/adaptive-learning.md) systems. Scaffolds also interact with learner self-regulation: support that removes too much of the planning or monitoring burden can leave learners dependent rather than developing the strategies described in [self-regulated learning](../theories/self-regulated-learning.md).

**Open questions.** How to operationalize and automate contingency (diagnosing when to fade) remains an active research problem, and evidence quality varies widely across scaffolding types (conceptual, procedural, metacognitive, motivational). Note also that the classroom-scale evidence recorded above is thin: the systematic review found only eight controlled effectiveness studies, mostly of one-to-one tutoring on simple tasks.

## Related Claims

- [Cognitive load reduction improves learning](../claims/cognitive-load-reduction-improves-learning.md) — scaffolds work partly by managing working-memory load
- [Worked examples reduce unnecessary search for novices](worked-examples-reduce-novice-search.md) — worked examples are a canonical scaffold for novices
- [Adaptive learning improves outcomes](../claims/adaptive-learning-improves-outcomes.md) — adaptive difficulty operationalizes scaffold fading at scale
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — a full instructional pattern built around modeling, coaching, and fading
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — why scaffolds must fade as competence grows
- [Clear structure improves learning](../claims/clear-structure-improves-learning.md) — structural supports are a low-cost, whole-lesson form of scaffolding
- [Activation improves learning](../claims/activation-improves-learning.md) — activating prior knowledge is a common pre-task scaffold
- [Chunking reduces working memory load](../claims/chunking-reduces-working-memory-load.md) — scaffolds often work by partitioning complex content into manageable units
- [Cognitive overload degrades learning](../claims/cognitive-overload-degrades-learning.md) — the load problem scaffolding is designed to prevent
- [Worked examples can become redundant or counterproductive for advanced learners](worked-examples-less-effective-with-expertise.md) — expertise reversal constrains when scaffolds should be faded
- [Example–problem sequences reduce cognitive load and improve learning outcomes](example-problem-sequences-reduce-cognitive-load.md) — worked-example scaffolds are the most empirically studied scaffolding form
- [Fading support promotes the transfer of responsibility from instructor to learner.](fading-support-promotes-transfer-of-responsibility.md) — a narrower finding that bears on this claim
- [Metacognitive prompts improve learning](metacognitive-prompts-improve-learning.md) — related
- [Sequencing worked examples with practice problems improves learning for novices](worked-example-problem-sequences.md) — related
