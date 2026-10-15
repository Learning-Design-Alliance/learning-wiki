---
type: claim
title: Self Assessment Accuracy Is Low Without Training
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
id: self-assessment-accuracy-is-low-without-training
evidence_strength: moderate
sources:
  - id: kostons-et-al-2012
    resource: "https://doi.org/10.1016/j.learninstruc.2011.08.004"
    title: "Kostons, D., van Gog, T., & Paas, F. (2012). Training self-assessment and task-selection skills: A cognitive approach to improving self-regulated learning. *Learning and Instruction, 22*(2), 121–132. [doi:10.1016/j.learninstruc.2011.08.004](https://doi.org/10.1016/j.learninstruc.2011.08.004)"
    author: "Kostons, D., van Gog, T., & Paas, F."
    q: 3
    i: 2
    n: 80 (secondary-education students, Experiment 1)
    kind: causal
    rigour: "?"
  - id: falchikov-boud-1989
    resource: "https://doi.org/10.2307/1170205"
    title: "Falchikov, N., & Boud, D. (1989). Student self-assessment in higher education: A meta-analysis. *Review of Educational Research, 59*(4), 395. [doi:10.2307/1170205](https://doi.org/10.2307/1170205)"
    author: "Falchikov, N., & Boud, D."
    q: 4
    i: "?"
    n: 51 studies
    kind: quant-synthesis
    rigour: "?"
---

# Self Assessment Accuracy Is Low Without Training

> **Claim** · [All claims](index.md)
> **Evidence** · 2 studies · 1 causal `r?`, 1 quant-synthesis `r?` · `q3`–`q4` · `i2` medium

Untrained learners systematically misjudge their own performance — typically overestimating it — and self-assessment only becomes reasonably accurate after explicit training, practice with feedback, and access to clear criteria.

## Subclaims

`q3 i2` In a randomized 2×2 experiment, secondary-education students who studied worked modeling examples of self-assessment produced significantly more accurate self-assessments of their own problem-solving performance than students who had not, a medium-sized effect. [→ Kostons et al. 2012](#kostons-et-al-2012)

`q4 i?` Across a meta-analysis of 51 quantitative studies, the correspondence between students' self-assessed marks and teachers' marks in higher education was inconsistent, and was closer in better-designed studies, in more advanced (vs. introductory) courses, and in science compared to other fields — i.e., untrained self-assessment accuracy is not a stable baseline but depends heavily on experience and assessment design. [→ Falchikov & Boud 1989](#falchikov-boud-1989)

## Evidence

### Kostons et al. 2012

Kostons, D., van Gog, T., & Paas, F. (2012). Training self-assessment and task-selection skills: A cognitive approach to improving self-regulated learning. *Learning and Instruction, 22*(2), 121–132. [doi:10.1016/j.learninstruc.2011.08.004](https://doi.org/10.1016/j.learninstruc.2011.08.004)

`q3 · randomized experiment (not pre-registered)` · `i2 · medium effect, ηp²=.10` · `n=80 (secondary-education students, Experiment 1)` · `causal · r?`

80 Dutch fourth-year pre-university students (age M=15.23) were randomly assigned to one of four conditions in a 2×2 design (self-assessment modeling examples: yes/no; task-selection modeling examples: yes/no) and solved genetics problems before and after studying modeling examples. Self-assessment accuracy was scored as the absolute difference between each student's self-rated performance and their actual (objectively scored) performance on the posttest, so a lower score means more accurate self-assessment. Students who had observed a human model demonstrating self-assessment were significantly more accurate (M=.81) than those who had not (M=1.23), F(1,76)=8.04, p=.006, ηp²=.10 — direct experimental evidence that untrained self-assessment is measurably worse than trained self-assessment on the same task.

### Falchikov & Boud 1989

Falchikov, N., & Boud, D. (1989). Student self-assessment in higher education: A meta-analysis. *Review of Educational Research, 59*(4), 395. [doi:10.2307/1170205](https://doi.org/10.2307/1170205)

`q4 · meta-analysis of 51 studies` · `i? · no pooled effect size in the abstract` · `n=51 studies` · `quant-synthesis · r?`

A meta-analysis of 51 quantitative studies comparing students' self-assessed marks with teachers' marks in higher education. Correspondence between the two was not uniformly high: it was closer in better-designed studies than in poorly designed ones, closer for students in advanced courses than in introductory courses, and closer in science than in other fields of study — i.e., raw self-assessment accuracy varies widely and cannot be assumed without attention to design and learner experience. Read at abstract level only (full text is paywalled/JSTOR-gated); no pooled correlation or effect-size statistic appears in the abstract, so no quantitative `i` code beyond `i?` can be supported from what was read.

## Studies bearing on this claim

<!-- synthesis:start -->
*Can learners' own monitoring be trusted, and can it be trained?* This table gathers the studies behind this claim and the 7 narrower claims that bear on it: **12 distinct studies** (7 causal, 3 quant-synthesis, 1 associational, 1 review), `q2`–`q4`, 3 of 12 with an effect size coded. One row per study, codes as each entry records them; no effect is averaged and no verdict is drawn. Built by `scripts/synthesize_claim.py` from `eval/synthesis/`; a row that looks wrong is fixed on the claim it comes from.

| Study | Design | Effect as recorded | Bears on this claim through |
|---|---|---|---|
| [Kostons et al. 2012](https://doi.org/10.1016/j.learninstruc.2011.08.004) | q3 · causal · r? | i2 · medium effect, ηp²=.10 | this claim |
| [Falchikov & Boud 1989](https://doi.org/10.2307/1170205) | q4 · quant-synthesis · r? | i? | this claim |
| [Carpenter et al. 2013](https://doi.org/10.3758/s13423-013-0442-z) | q3 · causal · r? | i? | [Fluent Illusions Mislead Self Assessment](fluent-illusions-mislead-self-assessment.md) (supports) |
| [Rhodes & Castel 2008](https://doi.org/10.1037/a0013684) | q3 · causal · r? | i? | [Fluent Illusions Mislead Self Assessment](fluent-illusions-mislead-self-assessment.md) (supports) |
| [Zell & Krizan 2014](https://doi.org/10.1177/1745691613518075) | q4 · quant-synthesis · r? | i2 · medium, mean r=.29 (SD=.11), individual meta-analytic effects .09–.63 | [Prior Knowledge Needed For Accurate Self Assessment](prior-knowledge-needed-for-accurate-self-assessment.md) (supports) |
| [Hacker et al. 2000](https://doi.org/10.1037/0022-0663.92.1.160) | q2 · associational · r? | i? | [Prior Knowledge Needed For Accurate Self Assessment](prior-knowledge-needed-for-accurate-self-assessment.md) (supports) |
| [Panadero et al. 2017](https://doi.org/10.1016/j.edurev.2017.08.004) | q4 · quant-synthesis · r? | i1 · small effect on Learning SRL, d=0.23; medium/non-significant on the other two SRL measures; large on self-efficacy, d=0.73 | [Self Assessment Improves Self Regulated Learning](self-assessment-improves-self-regulated-learning.md) (qualifies) |
| [Dai 2026](https://doi.org/10.3389/fpsyg.2026.1829268) | q3 · causal · r2 | i? | [In one 2×2 experiment with 120 undergraduates, an Assessment-Performance Calibration Activ](apca-improves-self-assessment-accuracy-overconfidence.md) (supports) |
| Fernandes 2026 | q3 · causal · r2 | i? | [No trace format supported calibrated self-evaluation: perceived-achieved correlations were](no-trace-format-supported-calibrated-self-evaluation.md) (supports) |
| [Fusco 2025](https://doi.org/10.51388/20.500.12265/252) | q3 · review · r1 | i? | [Peer and self-assessment both show significant effects on academic performance with no sig](peer-self-assessment-improve-performance-equally.md) (qualifies) |
| [Andrade et al. 2010](https://doi.org/10.1080/09695941003696172) | q2 · causal · r? | i? | [Self-assessing against a rubric improved the quality of student work in two non-randomised](rubrics-improve-student-work.md) (supports) |
| [Panadero & Romero 2014](https://doi.org/10.1080/0969594x.2013.877872) | q2 · causal · r? | i? | [Self-assessing against a rubric improved the quality of student work in two non-randomised](rubrics-improve-student-work.md) (supports) |
<!-- synthesis:end -->

## Discussion

**Direction of the bias.** The dominant finding in the self-assessment literature is overestimation: low performers lack the domain knowledge to recognize their own errors, a pattern closely related to the Dunning–Kruger effect. Weaker students show the largest miscalibration, while stronger students are sometimes slightly *under*confident. This means raw self-assessment data cannot be treated as a valid proxy for achievement, especially in early stages of learning.

**What training changes.** Accuracy improves when learners are given explicit evaluation criteria (rubrics, exemplars of different quality levels), opportunities to compare their judgments against expert or peer judgments, and iterative feedback on the accuracy of their self-ratings themselves — not just on the work. Self-assessment embedded in [assessment for learning](../principles/assessment-for-learning.md) cycles, where judgments feed directly into revision, tends to be more accurate than one-off self-grading.

**Boundary conditions.** Self-assessment accuracy is domain- and task-dependent: learners calibrate better on well-structured tasks with unambiguous correctness than on open-ended work like essays or design projects. It also develops with expertise — the same [expertise reversal dynamics](../theories/expertise-reversal-effect.md) seen in scaffolding research suggest that supports needed for accurate novice self-assessment (detailed rubrics, guided checklists) should be faded as learners gain experience.

**Relation to self-regulated learning.** Accurate self-monitoring is a core component of [self-regulated learning](../theories/self-regulated-learning.md): learners who misjudge their performance select inappropriate study strategies and terminate practice prematurely. Training calibration is therefore not merely an assessment concern but a prerequisite for effective self-regulated study decisions.

**Design implication.** The claim is a caution, not a prohibition: untrained self-assessment is unreliable as a *measure*, but the act of trained self-assessment can still benefit learning by directing attention to criteria and gaps. Designers should not ask learners to self-assess without first teaching them how, and should treat self-ratings from novices as noisy data requiring triangulation with [assessment](../elements/assessment.md) evidence.

**Open questions.** Two studies are recorded: one randomized experiment in which secondary students trained with modeling examples self-assessed more accurately than untrained students (Kostons et al. 2012, n = 80), and one meta-analysis of 51 higher-education studies, read at abstract level, which found student–teacher agreement inconsistent and closer in advanced courses and better-designed studies but reports no pooled accuracy estimate there (Falchikov & Boud 1989). Still missing: a pooled estimate of how low untrained accuracy is, and replications of the training effect beyond one experiment. <!-- deprecated (2026-10-05, stale: entries had been added): The evidence base for this claim still needs to be populated with primary studies — particularly meta-analytic estimates of self-assessment accuracy and intervention studies comparing trained versus untrained self-assessment. Until then, the claim should be treated as a well-established qualitative pattern rather than a quantified effect. -->

## Related Claims

- [In two secondary-school writing studies, peer reviewers' own performance predicted how helpful their feedback was but not how accurately it identified problems](peer-feedback-accuracy-depends-on-expertise.md) — the general claim this finding bears on, with the studies behind it

- [Self Assessment Improves Self Regulated Learning](self-assessment-improves-self-regulated-learning.md) — the general claim this finding bears on, with the studies behind it

- [Assessment for learning improves achievement.](assessment-for-learning-improves-achievement.md) — feedback-rich assessment cycles are the context in which self-assessment accuracy develops
- [Self-Regulated Learning](../theories/self-regulated-learning.md) — accurate self-monitoring is a core component of self-regulation
- [Expertise Reversal Effect](../theories/expertise-reversal-effect.md) — self-assessment supports needed by novices should be faded as expertise grows
- [Prior Knowledge Needed For Accurate Self Assessment](prior-knowledge-needed-for-accurate-self-assessment.md) — related
- [Metacognitive Strategies Improve Learning](metacognitive-strategies-improve-learning.md) — a broader claim this one bears on
- [Self-regulated learning improves achievement](self-regulated-learning-improves-achievement.md) — a broader claim this one bears on
- [Learners who could decide after a trial whether to receive knowledge of results estimated their own movement outcomes more accurately in retention than Self-Before learners and their yoked counterparts.](self-controlled-kr-decided-after-trial-improves-error-estimation-accuracy.md) — related
- [Sequencing worked examples with practice problems improves learning for novices](worked-example-problem-sequences.md) — related
- [Novice clinical learners show pervasive metacognitive calibration deficits, with overestimated performance and confidence exceeding accuracy](novice-metacognitive-calibration-deficits.md) — a narrower finding that bears on this claim
- [Students' expertise on the task may be an important prerequisite for accurate self-assessment](task-expertise-prerequisite-ssa-accuracy.md) — related