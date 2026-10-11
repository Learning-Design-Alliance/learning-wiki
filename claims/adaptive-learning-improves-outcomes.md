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
    kind: quant-synthesis
    rigour: 2
  - id: kulik-fletcher-2016
    resource: "https://doi.org/10.3102/0034654315581420"
    title: "Kulik, J. A., & Fletcher, J. D. (2016). Effectiveness of intelligent tutoring systems: A meta-analytic review. *Review of Educational Research, 86*(1), 42–78. [doi:10.3102/0034654315581420](https://doi.org/10.3102/0034654315581420)"
    author: "Kulik, J. A., & Fletcher, J. D."
    q: 4
    i: 2
    n: 50 controlled evaluations
    kind: quant-synthesis
    rigour: "?"
---

# Adaptive learning improves outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 2 quant-synthesis `r2` · `q4` · `i2` medium

Learning environments that adjust task difficulty, sequencing, or support to individual learner performance can improve outcomes relative to fixed, one-size-fits-all sequences — but the effect depends heavily on how adaptation is implemented and for whom.

## Subclaims

`q4 i2` Across 107 effect sizes (14,321 participants), intelligent tutoring systems produced higher achievement than teacher-led large-group instruction (g = 0.42), non-ITS computer-based instruction (g = 0.57) and textbooks or workbooks (g = 0.35), but no advantage over individual human tutoring (g = -0.11) or small-group instruction (g = 0.05). [→ Ma et al. 2014](#ma-et-al-2014)

`q4 i2` In 50 controlled evaluations the median effect of intelligent tutoring was 0.66 SD over conventional instruction, but the gain depended heavily on whether tests were locally developed or standardized, and was small where control treatments were nonconventional or implementations flawed. [→ Kulik & Fletcher 2016](#kulik-fletcher-2016)

## Evidence

### Ma et al. 2014

Ma, W., Adesope, O. O., Nesbit, J. C., & Liu, Q. (2014). Intelligent tutoring systems and learning outcomes: A meta-analysis. *Journal of Educational Psychology, 106*(4), 901–918. [doi:10.1037/a0037123](https://doi.org/10.1037/a0037123)

`q4 · meta-analysis` · `i2 · medium effect, g=0.42 vs teacher-led large-group instruction` · `n=107 effect sizes, 14,321 participants` · `quant-synthesis · r2`

A meta-analysis of studies comparing students learning from intelligent tutoring systems (computer programs that model the learner's state to individualise instruction) with students in non-ITS learning environments. ITS were associated with greater achievement than teacher-led large-group instruction, other computer-based instruction and textbooks or workbooks, with positive effects at all education levels and in almost all subject domains. They did not outperform individualised human tutoring or small-group instruction, so the advantage is relative to non-individualised instruction rather than to adaptation delivered by people. Read from the abstract only.

### Kulik & Fletcher 2016

Kulik, J. A., & Fletcher, J. D. (2016). Effectiveness of intelligent tutoring systems: A meta-analytic review. *Review of Educational Research, 86*(1), 42–78. [doi:10.3102/0034654315581420](https://doi.org/10.3102/0034654315581420)

`q4 · meta-analysis` · `i2 · medium effect, median 0.66 SD` · `n=50 controlled evaluations` · `quant-synthesis · r?`

A meta-analysis of 50 controlled evaluations of intelligent computer tutoring systems against conventional instruction. The median effect raised test scores 0.66 standard deviations, from the 50th to the 75th percentile. The size of the gain depended strongly on whether outcomes were measured with locally developed or standardized tests, which the authors suggest makes test-instruction alignment a critical determinant of the effect; ten further evaluations with nonconventional control groups or flawed implementations showed small effects. Read from the abstract only.

## Discussion

**Mechanism.** Adaptive systems plausibly improve outcomes through two routes: keeping learners in their zone of proximal development (tasks neither too easy nor too hard, consistent with [cognitive load management](../principles/cognitive-load-management.md)), and ensuring mastery of prerequisites before advancing (as in [adaptive mastery learning](../elements/adaptive-mastery-learning.md)). Both routes predict the largest gains for learners who would otherwise be mismatched to a fixed sequence — struggling learners overwhelmed by uniform pacing, or advanced learners bored by it.

**Boundary conditions.** Adaptation is only as good as its model of the learner. Systems that adapt on shallow signals (response time, item counts) rather than diagnostic assessment of knowledge components may route learners poorly. There is also a plausible expertise-reversal concern: highly adaptive scaffolding that remains in place for already-proficient learners can become redundant and depress performance, mirroring the pattern documented for worked examples in [expertise reversal effect](../theories/expertise-reversal-effect.md). Adaptation should fade support as competence grows.

**Open questions.** Two meta-analyses of intelligent tutoring systems are recorded (Ma et al. 2014; Kulik & Fletcher 2016), both read from abstracts: tutoring systems outperformed large-group instruction, other computer-based instruction and textbooks, but not individual human tutoring or small-group instruction, and gains were smaller on standardized than on locally developed tests. No recorded study covers other adaptive systems, such as mastery-based platforms or adaptive quizzing. Key moderators still to establish include: which adaptation target (difficulty, pacing, feedback, content sequence) drives effects; whether gains persist beyond the adaptive period; and how outcomes compare across intelligent tutoring systems, mastery-based platforms, and simpler adaptive quizzing.

<!-- deprecated (2026-10-05, stale: entries had been added): **Open questions.** The evidence base for this claim has not yet been populated. Key moderators to establish include: which adaptation target (difficulty, pacing, feedback, content sequence) drives effects; whether gains persist beyond the adaptive period; and how outcomes compare across intelligent tutoring systems, mastery-based platforms, and simpler adaptive quizzing. Studies must be added before any strength rating can be assigned. -->

## Related Claims

- [Mastery learning improves achievement.](../elements/adaptive-mastery-learning.md) — mastery-based adaptation is the classic mechanism by which adaptive sequencing helps
- [Cognitive load theory](../principles/cognitive-load-theory.md) — adaptation aims to keep load within learners' working-memory limits
- [Expertise reversal effect](../theories/expertise-reversal-effect.md) — adaptive support can backfire when it persists for advanced learners
- [Feedback improves learning](../elements/assessment.md) — adaptive feedback delivery is a common implementation of adaptation
- [Adaptive learning](../principles/adaptive-learning.md) — the design principle this claim evaluates empirically
- [Adaptive difficulty](../elements/adaptive-difficulty.md) — difficulty adjustment is the most common adaptation target in practice
- [Contingent scaffolding improves learning more than fixed or absent support.](contingent-scaffolding-improves-learning.md) — related
- [Human tutoring has a medium effect over no tutoring, and in one small study students learned as well when tutors only prompted them as when tutors also explained and gave feedback](tutoring-effectiveness-comes-from-scaffolding-and-feedback.md) — related
- [The survey reports, citing Lee and Brunskill, that individualized BKT in an intelligent tutoring system reduced by about half the questions required for 20% of students to achieve mastery.](individualized-bkt-reduces-questions-needed-for-mastery.md) — related
- [Peer Tutoring Improves Achievement](peer-tutoring-improves-achievement.md) — related
- [Scaffolding improves learning](scaffolding-improves-learning.md) — related
- [Early objective and subjective feedback helps evaluate program effectiveness and prevents small problems from growing](early-objective-subjective-feedback-program-effectiveness.md) — related
- [The survey reports, citing Long and Aleven, that students who used DragonBox enjoyed the experience more, while students who used the Lynnette intelligent tutoring system performed significantly better on the test.](intelligent-tutor-lynnette-outperformed-dragonbox-on-test.md) — related
- [Mastery Learning Improves Outcomes](mastery-learning-improves-outcomes.md) — related
- [Tutoring benefits both tutors and tutees](tutoring-benefits-tutors-and-tutees.md) — related
- [The measured advantage of computer-based instruction over conventional teaching shrinks when the same teacher teaches both versions](cbi-advantage-shrinks-same-teacher-comparisons.md) — related
- [System compensation as implemented is not a satisfactory adaptive variable](system-compensation-unsatisfactory-adaptive-variable.md) — related
- [Strategic speeded practice outperformed strategic non-speeded practice within Galaxy Math, with a +0.57 effect size for the disseminated speeded version](galaxy-math-speeded-practice-advantage.md) — related
- [Platform-enabled experimentation research draws on multiple intellectual lineages, including intelligent tutoring systems, formative feedback, and exemplar platforms like ASSISTments](multiple-intellectual-lineages-shared-foundations.md) — related
- [An intelligent reading tutor used 20 minutes a day offered time efficiencies over conventional human tutoring of 30 or more minutes a day](intelligent-reading-tutor-time-efficiency-over-human-tutoring.md) — related
- [Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS](adaptive-icap-scaffolding-improves-posttest-logic-tutor.md) — a narrower finding that bears on this claim
- [AI-supported adaptive systems are reported to enhance adult learner engagement, motivation, and outcomes when aligned with learner goals and prior knowledge](ai-adaptive-systems-enhance-adult-engagement.md) — a broader claim this one bears on
- [AURA's within-session reinforcement learning improved composite response quality over non-adaptive baselines (p = 0.044, d = 0.66), with fewer specification prompts and more validation behavior](aura-rl-improves-response-quality.md) — a narrower finding that bears on this claim
- [Intelligent tutoring systems are reported to improve learning outcomes, especially in structured knowledge domains](its-improve-outcomes-structured-domains.md) — a broader claim this one bears on
- [Intelligent tutoring systems can improve learning outcomes, particularly with immediate actionable feedback](its-improve-learning-outcomes-with-actionable-feedback.md) — a broader claim this one bears on
- [In university physics education, AI has been applied for tutoring and explanations, formative feedback and scaffolding, collaborative problem solving, simulation and modeling, instructional design, and AI literacy development](ai-university-physics-six-pedagogical-functions.md) — related
- [One-to-one human tutoring lifts an ordinary student well beyond the average classroom with an effect of about d = 0.79 (VanLehn, 2011, as reported)](human-tutoring-effect-d-079.md) — related
- [The system has no empirical evaluation yet: profile accuracy has not been assessed and learning outcomes remain an open question](ecnuclaw-no-empirical-evaluation-yet.md) — related
- [Meta-analytic evidence indicates intelligent tutoring systems yield positive learning outcomes compared with non-ITS conditions](its-meta-analytic-positive-outcomes.md) — a broader claim this one bears on