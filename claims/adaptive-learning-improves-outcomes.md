---
type: claim
title: Adaptive learning improves outcomes
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: adaptive-learning-improves-outcomes
evidence_strength:
sources:
  - id: ma-et-al-2014
    resource: "https://doi.org/10.1037/a0037123"
    title: "Ma, W., Adesope, O. O., Nesbit, J. C., & Liu, Q. (2014). Intelligent tutoring systems and learning outcomes: A meta-analysis. *Journal of Educational Psychology, 106*(4), 901–918. [doi:10.1037/a0037123](https://doi.org/10.1037/a0037123)"
    author: "Ma, W., Adesope, O. O., Nesbit, J. C., & Liu, Q."
    q: 4
    i: 2
    n: 107 effect sizes, 14,321 participants
  - id: kulik-fletcher-2016
    resource: "https://doi.org/10.3102/0034654315581420"
    title: "Kulik, J. A., & Fletcher, J. D. (2016). Effectiveness of intelligent tutoring systems: A meta-analytic review. *Review of Educational Research, 86*(1), 42–78. [doi:10.3102/0034654315581420](https://doi.org/10.3102/0034654315581420)"
    author: "Kulik, J. A., & Fletcher, J. D."
    q: 4
    i: 2
    n: 50 controlled evaluations
---

# Adaptive learning improves outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · `q4` pre-registered or meta-analytic · `i2` medium

Learning environments that adjust task difficulty, sequencing, or support to individual learner performance can improve outcomes relative to fixed, one-size-fits-all sequences — but the effect depends heavily on how adaptation is implemented and for whom.

## Subclaims

`q4 i2` Across 107 effect sizes (14,321 participants), intelligent tutoring systems produced higher achievement than teacher-led large-group instruction (g = 0.42), non-ITS computer-based instruction (g = 0.57) and textbooks or workbooks (g = 0.35), but no advantage over individual human tutoring (g = -0.11) or small-group instruction (g = 0.05). [→ Ma et al. 2014](#ma-et-al-2014)

`q4 i2` In 50 controlled evaluations the median effect of intelligent tutoring was 0.66 SD over conventional instruction, but the gain depended heavily on whether tests were locally developed or standardized, and was small where control treatments were nonconventional or implementations flawed. [→ Kulik & Fletcher 2016](#kulik-fletcher-2016)

## Evidence

### Ma et al. 2014

Ma, W., Adesope, O. O., Nesbit, J. C., & Liu, Q. (2014). Intelligent tutoring systems and learning outcomes: A meta-analysis. *Journal of Educational Psychology, 106*(4), 901–918. [doi:10.1037/a0037123](https://doi.org/10.1037/a0037123)

`q4 · meta-analysis` · `i2 · medium effect, g=0.42 vs teacher-led large-group instruction` · `n=107 effect sizes, 14,321 participants`

A meta-analysis of studies comparing students learning from intelligent tutoring systems (computer programs that model the learner's state to individualise instruction) with students in non-ITS learning environments. ITS were associated with greater achievement than teacher-led large-group instruction, other computer-based instruction and textbooks or workbooks, with positive effects at all education levels and in almost all subject domains. They did not outperform individualised human tutoring or small-group instruction, so the advantage is relative to non-individualised instruction rather than to adaptation delivered by people. Read from the abstract only.

### Kulik & Fletcher 2016

Kulik, J. A., & Fletcher, J. D. (2016). Effectiveness of intelligent tutoring systems: A meta-analytic review. *Review of Educational Research, 86*(1), 42–78. [doi:10.3102/0034654315581420](https://doi.org/10.3102/0034654315581420)

`q4 · meta-analysis` · `i2 · medium effect, median 0.66 SD` · `n=50 controlled evaluations`

A meta-analysis of 50 controlled evaluations of intelligent computer tutoring systems against conventional instruction. The median effect raised test scores 0.66 standard deviations, from the 50th to the 75th percentile. The size of the gain depended strongly on whether outcomes were measured with locally developed or standardized tests, suggesting that test-instruction alignment drives part of the effect; ten further evaluations with nonconventional control groups or flawed implementations showed small effects. Read from the abstract only.

## Discussion

**Mechanism.** Adaptive systems plausibly improve outcomes through two routes: keeping learners in their zone of proximal development (tasks neither too easy nor too hard, consistent with [cognitive load management](../principles/cognitive-load-management.md)), and ensuring mastery of prerequisites before advancing (as in [adaptive mastery learning](../elements/adaptive-mastery-learning.md)). Both routes predict the largest gains for learners who would otherwise be mismatched to a fixed sequence — struggling learners overwhelmed by uniform pacing, or advanced learners bored by it.

**Boundary conditions.** Adaptation is only as good as its model of the learner. Systems that adapt on shallow signals (response time, item counts) rather than diagnostic assessment of knowledge components may route learners poorly. There is also a plausible expertise-reversal concern: highly adaptive scaffolding that remains in place for already-proficient learners can become redundant and depress performance, mirroring the pattern documented for worked examples in [expertise reversal effect](../theories/expertise-reversal-effect.md). Adaptation should fade support as competence grows.

**Open questions.** The evidence base for this claim has not yet been populated. Key moderators to establish include: which adaptation target (difficulty, pacing, feedback, content sequence) drives effects; whether gains persist beyond the adaptive period; and how outcomes compare across intelligent tutoring systems, mastery-based platforms, and simpler adaptive quizzing. Studies must be added before any strength rating can be assigned.

## Related Claims

- [Mastery learning improves achievement.](../elements/adaptive-mastery-learning.md) — mastery-based adaptation is the classic mechanism by which adaptive sequencing helps
- [Cognitive load theory](../principles/cognitive-load-theory.md) — adaptation aims to keep load within learners' working-memory limits
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — adaptive support can backfire when it persists for advanced learners
- [Feedback improves learning](../elements/assessment.md) — adaptive feedback delivery is a common implementation of adaptation
- [Adaptive learning](../principles/adaptive-learning.md) — the design principle this claim evaluates empirically
- [Adaptive difficulty](../elements/adaptive-difficulty.md) — difficulty adjustment is the most common adaptation target in practice
- [Adaptive learning](../patterns/adaptive-learning.md) — the pattern-level implementation of adaptive sequencing