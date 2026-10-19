---
type: principle
id: scaffolding
aliases: [pre-assessment-scaffolding-hypothesized-quality-driver, text-system-controlled-prompts-for-novices]
title: Scaffolding
description: "Temporary support given while a learner attempts a task they cannot yet complete alone may improve later cognitive outcomes compared with unsupported attempts, qualified by the learner's task-specific starting response, the kind of support, the setting and whether the outcome is measured without the support."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
sources:
  - id: wood-1976
    resource: "https://doi.org/10.1111/j.1469-7610.1976.tb00381.x"
    title: "Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89-100"
    author: "Wood, D., Bruner, J. S., & Ross, G"
  - id: bates-2013
    resource: "https://arxiv.org/abs/1308.2202"
    title: "Bates, S. P., Galloway, R. K., Riise, J., and Homer, D. (2013). Assessing the quality of a student-generated question repository. https://arxiv.org/abs/1308.2202"
    author: Bates, S. P., Galloway, R. K., Riise, J., and Homer, D
  - id: reisslein-2004
    resource: "https://eric.ed.gov/?id=ED484994"
    title: "Reisslein, J., Atkinson, R. K., & Reisslein, M. (2004). Exploring the Presentation and Format of Help in a Computer-Based Electrical Engineering Learning Environment. Arizona State University. https://eric.ed.gov/?id=ED484994"
    author: "Reisslein, J., Atkinson, R. K., & Reisslein, M"
---

# Scaffolding

> **Principle** · [All principles](index.md)
> **Evidence** · 58 claims (18 for, 32 mixed, 8 against) · 43 studies (23 causal, 6 review, 4 quant-synthesis, 4 theoretical, 3 design, 2 associational, 1 qualitative), `q1`–`q4` · 12 of 43 report an effect size · 52 claims rest on one study

## Conditional relationship

A learner who cannot yet complete a task alone may learn more from attempting it **with support** than from attempting it unsupported. Support here means hints, prompts, models, partial structures or tutor questions given during the attempt. The expected change is in later cognitive outcomes on the target task (`immediate-performance`, `near-transfer`, `conceptual-understanding`), not in how well the learner does while the support is present. The relationship is bounded by the learner's starting response on *this* task (`novice` for the task, not for the domain), by the kind of support and what it leaves the learner to do, by the setting (most evidence is one-to-one tutoring or computer-based support in STEM problem solving; little is `classroom`, where the wiki holds one whole-class trial with third graders and a few small group-work studies), and by whether the outcome is measured with the support removed.

Two randomised studies in generative-AI settings now test support against its absence directly, and neither settles it. Among novices using an LLM, those given a conceptual roadmap scored higher on a post-intervention exam than unguided novices, at a significance level between .05 and .10, with less spread and with most of the benefit among the weakest at extracting help from the tool [+W]. In a construction-engineering course, learners using AI with instructional prompts, using AI without them, or studying slides did not differ significantly in multiple-choice accuracy [~M]. A non-significant difference does not show the conditions were equivalent. Both studies are under Evidence and qualifications below.

This page owns the general relationship: support versus none. The [Scaffolding and Fading](scaffolding-and-fading.md) principle holds a narrower model inside it, in which support is **contingent** (raised after failure, lowered after success) and then **withdrawn**, and the outcome is unassisted performance. Whether support must be contingent and must fade to help is a question that page treats; the evidence below does not settle it, and one synthesis found no difference by fading. The [cognitive apprenticeship pattern](../patterns/cognitive-apprenticeship.md) is a reusable policy built on that narrower model.

## Fitting the design to a situation

Ask for three facts when the brief omits them: **what the learner does on the task without support**, **whether the outcome that matters will be measured with the support removed**, and **who or what gives the support (a tutor, a teacher with a class, software, an AI assistant)**.

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners cannot yet complete the target task alone | Give support during the attempt (prompts, partial structures, models) rather than leaving them to attempt it unsupported, and judge learning on a later task without the support | [Scaffolding improves learning](../claims/scaffolding-improves-learning.md) [+S] |
| `online-self-paced` or computer-based STEM problem solving | Build conceptual, strategic or metacognitive scaffolds into the tasks; do not rely on motivational messages alone, which showed no effect on their own | [Computer-based scaffolding has a positive effect in STEM](../claims/computer-based-scaffolding-positive-cognitive-outcomes-stem.md) [+M]; [Scaffold design features did not moderate the effect](../claims/scaffolding-design-features-no-moderation.md) [~M] |
| The objective is applying principles, not recalling concepts | Aim the scaffolds at choosing and applying the principle; the effect was larger at the principles level than the concept level | [Scaffolding's effect is greater at the principles level](../claims/principles-level-assessment-highest-scaffolding-effect.md) [+M] |
| The course is project-based, or design-based | Use scaffolds in project-based work; in design-based learning the pooled effect was not distinguishable from zero, so check unsupported performance there | [Scaffolding's effect is highest in project-based contexts](../claims/project-based-context-highest-scaffolding-effect.md) [~M] |
| Learners are underperforming or below grade level | Expect a smaller gain from the same scaffolds; check unsupported performance more often and add explicit teaching of the missing knowledge. Scaffolds that structure the domain task can narrow a gap tied to low prior knowledge (one whole-class trial), but heavy regulative scaffolding (goal trees, cues, templates) can crowd out the domain work: in one inquiry-software study lower-achieving pairs built much worse models with the full regulative tool than with an empty one. Aim support at the task the gap is in, keep regulative scaffolds light, and judge them on the domain outcome | [Education population moderates the scaffolding effect](../claims/education-population-moderates-scaffolding-effect.md) [~M]; [Scaffolding mitigated the limiting effect of low prior knowledge](../claims/scaffolds-mitigate-prior-knowledge-limit.md) [+W]; [Empty-PC dyads built better domain models, concentrated among lower achievers](../claims/empty-pc-better-domain-models.md) [-M] |
| `classroom`, whole-class inquiry with learners who differ in prior knowledge and reasoning | Combine a static structuring scaffold on the task with teacher modelling and adaptive verbal prompts that problematise, and give both procedural and conceptual help where learners stall (for example on graphs); in one trial with third graders this raised posttest reasoning over the same inquiry unit without the scaffolds and almost removed the disadvantage of lower prior knowledge and reasoning. Expect the scaffolded version to lean on different capacities: inhibition predicted learning only under scaffolding, so check who is still left behind | [Scaffolded third-graders outperformed control students on irrelevant-evidence reasoning](../claims/scaffolds-improve-irrelevant-evidence-reasoning-third-graders.md) [+M]; [Scaffolding almost fully diminished the disadvantage of lower logical reasoning](../claims/scaffolds-diminish-logical-reasoning-disadvantage.md) [+W]; [Inhibition predicted posttest scores only under scaffolding](../claims/scaffolds-enable-inhibition-contribution.md) [~W]; [The teacher as adaptive expert in real-time labs](../claims/adaptive-expert-teacher-closes-gaps-real-time-labs.md) [+W] |
| Groups solve an ill-structured problem together (collaborative problem solving, collaboration scripts) | Build hard scaffolds into the task (prompts for each problem-solving phase) and expect more solution evaluation and better group solutions while they are present; then test the group on a later task without them, because neither a collaboration script nor a reflection scaffold improved interaction in a later unsupported collaboration. In a meta-analysis of collaboration scripts, script effects on collaboration skills did not differ significantly between scripts paired with content information and scripts paired with content scaffolds, at 14% post-hoc power | [Scaffolded tasks elicit more solution-evaluation turns](../claims/scaffolds-shift-cps-turn-proportions-p3-p4.md) [+W]; [Scaffolded tasks had process distributions closer to the ideal](../claims/scaffolds-lower-gini-cps-process-distribution.md) [+W]; [Final solution scores were higher on the scaffolded task](../claims/scaffolds-higher-final-solution-scores.md) [+W]; [No script or reflection effect on later interaction quality](../claims/no-script-or-reflection-effect-on-interaction-quality.md) [~W]; [Content support did not moderate script effects](../claims/content-support-moderator-not-significant.md) [~W] |
| Software gives regulative scaffolds (planning, monitoring, report templates) during inquiry | Judge them on the domain outcome, not on the product they template: a full regulative tool gave better-structured, more complete lab reports, while pairs with the empty tool built better domain models | [Full-PC dyads wrote better lab reports](../claims/full-pc-better-lab-reports.md) [~M]; [Empty-PC dyads built better domain models](../claims/empty-pc-better-domain-models.md) [-M] |
| Learners attempt problems before instruction (productive failure) | Either nudge learners toward suboptimal solutions (failure-driven) or give low-specificity heuristics toward the right one (success-driven); conceptual posttests were similar, and failure-driven support gave higher-quality constructive reasoning, so prefer it when reasoning is the goal | [Failure- and success-driven scaffolding produce similar posttest understanding](../claims/failure-and-success-scaffolding-similar-posttest-conceptual-understanding.md) [~M]; [Failure-driven scaffolding gave higher-quality constructive reasoning](../claims/failure-driven-scaffolding-higher-quality-constructive-reasoning.md) [+W] |
| One-to-one tutoring is available | Have tutors prompt the learner to produce the next step before they explain; prompting alone matched ordinary tutoring in one small study | [Tutoring effectiveness comes from scaffolding](../claims/tutoring-effectiveness-comes-from-scaffolding-and-feedback.md) [~M] |
| The support is an AI assistant that can produce the answer | Limit it to hints and questions rather than solutions, and test without it; unrestricted help raised assisted work and lowered unassisted results. Consider teaching learners how to use the tool as a partner rather than an answer source: in one trial structured training of this kind beat problem-solving training on a later problem-solving test. For novices, add a short conceptual roadmap of the topic; its benefit in one study was borderline | [AI assistance impairs unassisted fraction performance](../claims/ai-assistance-impairs-unassisted-fraction-performance-exp1.md) [-M]; [Supported and independent writing performance diverge](../claims/genai-supported-performance-independent-divergence.md) [~M]; [Structured GenAI training improves problem-solving performance](../claims/genai-scaffolding-training-improves-revision-performance.md) [+M]; [Conceptual-map scaffolding and novice LLM performance](../claims/conceptual-map-scaffolding-reduces-novice-variance.md) [+W] |
| Prompts are delivered in a computer module to novices | Write the prompts as text rather than diagrams, and do not judge the format by practice accuracy alone: text prompts gave more correct first attempts, pictorial prompts more correct second attempts, and text prompts gave higher near transfer and stronger reported continuing motivation in the same 51-learner experiment. Far transfer was at the floor in every condition, so the study says nothing about far transfer | [Textual prompts give better near transfer than pictorial](../claims/textual-prompts-better-near-transfer-than-pictorial.md) [+M]; [First- and second-attempt accuracy differ by prompt format](../claims/prompt-format-first-second-attempt-accuracy.md) [~M]; [Textual prompts yield stronger continuing motivation](../claims/textual-prompts-stronger-continuing-motivation.md) [+M]; [Far transfer was at the floor in every condition](../claims/far-transfer-floor-effect-and-equal-time.md) [~M] |
| The module could show prompts automatically or let learners call them up | Either is defensible on performance: posttest totals did not differ significantly between module-controlled and learner-requested prompts. Novices rated module-controlled prompts more favourably, so default to them and record whether a learner-requested version is used | [Prompt presentation had no significant performance effect](../claims/prompt-presentation-no-performance-effect.md) [~M]; [Learners rated externally regulated prompts more positively](../claims/external-prompt-regulation-more-positive-attitudes.md) [+M] |
| Learners are moving from studying worked examples to solving problems alone | Withdraw the support in steps (complete examples, then increasingly incomplete ones, then independent problems), removing the last worked-out steps first; the evidence is for near transfer, not a fading rate or far transfer. See [Scaffolding and Fading](scaffolding-and-fading.md) | [Fading support promotes the transfer of responsibility](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S] |
| A learner already does as well without the support | Make the support optional or remove it; guidance that helps novices can become redundant | [Expertise reversal effect](../claims/expertise-reversal-effect.md) [~S] |
| The strategy can be taught explicitly instead | Consider explicit strategy instruction first; a dynamic-assessment synthesis ranked it above scaffolding | [Contingent scaffolding improves learning](../claims/contingent-scaffolding-improves-learning.md) [~M] |
| Language teachers plan to support learners mainly by repeating or translating | Plan support aimed at the step the learner is stuck on; repetition and translation used as unplanned support were reported to hinder learning | [Repetition and translation as scaffolding can hinder learning](../claims/repetition-translation-scaffolding-hinders-learning.md) [-W] |

## Observation, state and explanation

What can be observed is a response under stated conditions: what the learner attempted, which support was available or given (record its kind and how much of the task it did), whether the learner used it, and what they produced. "Cannot yet do it alone" and "can do it with help" are inferred states, and each depends on the task and on the support offered. A support can make a task easier by doing part of it for the learner; success then shows what the learner and the support did together, not what the learner has learned.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Fails the task unsupported, succeeds with a prompt | The prompt cued knowledge the learner already had; the prompt supplied the missing step; the unsupported attempt failed for a reason unrelated to the step (instructions, access, time) | Give a matched task with a weaker cue (a question, not the step) and record which level is enough; check the unsupported attempt's instructions and response mode. |
| Fails even with support | The task is too far beyond the learner's current knowledge for this support to bridge; the support is the wrong kind (structuring when the gap is a concept); the learner did not read or use it | Ask the learner to say what the support tells them to do; try a different kind of support on a simpler component of the same task. |
| Succeeds with support but cannot explain the result | The support did the reasoning and the learner followed it; the learner has the procedure without its rationale; a language or expression barrier | Ask for an explanation in an accessible mode, and pose a changed case the followed steps would not solve. |
| Does as well without the support as with it, or worse with it | The support is redundant for this learner (expertise reversal); the support adds reading or split attention; the learner ignored it | Offer the task with support optional; record whether it is used and whether accuracy or time changes. |
| A group produces a better solution on a scaffolded task than on an unscaffolded one | The scaffold structured the product and did part of the process; the scaffolded task was easier or different; the group learned a better problem-solving process | Give the group a comparable later task without the scaffold and record whether solution evaluation and solution quality hold; in one study a script and a reflection scaffold left later unsupported interaction unchanged. |
| Takes every support offered | The learner needs it; the learner values finishing over independence; using support carries no cost while trying alone does | Ask privately what the learner is aiming for; vary whether support is on request or automatic on a matched task. |

These rows are proposals for interpreting a response; none has been tested with learners as a diagnostic. A probe is itself practice and can change the state it measures, so record each one. Keep the explanations that remain open rather than choosing the one whose name fits.

## Evidence and qualifications

- [Scaffolding improves learning](../claims/scaffolding-improves-learning.md) [+M]. A random-effects meta-analysis of 144 experimental studies (333 outcomes) of computer-based scaffolding for STEM learners from primary school through adult education, working in ill-structured, problem-centred curricula, reports a positive effect on cognitive outcomes (ĝ = 0.46). The effect did not differ by context-specificity or by whether or how scaffolding was faded, and was greatest at the level of principles and among adult learners. A systematic review of teacher–student scaffolding (1998–2009) found 8 controlled effectiveness studies, mostly small one-to-one tutoring experiments on simple, well-structured tasks, favouring scaffolded or contingent conditions over no or less-contingent support, with no pooled effect and thin classroom evidence. This is the most direct support for the support-versus-none relationship. A pooled program-level effect forecasts no individual learner's response, and the comparison conditions are not described on the claim page. Not yet checked against its sources. The claim's opening sentence says the benefit holds "provided the support is faded", which its own meta-analysis entry does not show.
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]. In one-to-one long-division tutoring (fourth and fifth graders, 8 per condition, coded as a quasi-experiment), fully contingent support beat moderate, high, partly contingent and no support at an immediate and a one-month test. With 11 tutor–student pairs (grade 8, the circulatory system), more interactive tutoring gave similar immediate learning but better transfer. A meta-analysis of dynamic assessment ranked explicit strategy training above scaffolding and scaffolding above coaching. Not settled: the abstracts could not confirm the entries. It supports support over none in tutoring; it does not show a classroom-scale effect, and it does not show that scaffolding beats explicit strategy instruction.
- [Human tutoring has a medium effect over no tutoring, and in one small study students learned as well when tutors only prompted them as when tutors also explained and gave feedback](../claims/tutoring-effectiveness-comes-from-scaffolding-and-feedback.md) [~M]. In one-to-one tutoring of 8th graders on the circulatory system (11 dyads per study), students whose tutors withheld explanations and feedback and only prompted learned as well as students in ordinary tutoring. A review of tutoring experiments reports human tutoring at d = 0.79 against no tutoring, close to intelligent tutoring systems at d = 0.76. The claim page itself says its evidence supports prompting-type scaffolding more than feedback as the active part, so its title overstates. It bears on which kind of support matters, not on support versus none in groups. Not settled: the abstracts could not confirm the entries.
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M]. A synthesis of cognitive-load studies: integrated explanations, worked examples and step-by-step guidance help novices by reducing unnecessary search, and can become redundant for more knowledgeable learners, who may learn more efficiently from leaner tasks. This limits the relationship to learners for whom the task is new; it gives no criterion for when an individual has crossed over. Not settled: the abstract could not confirm the entry.
- [Conceptual-map scaffolding modestly improves novice LLM-condition performance and reduces outcome variance](../claims/conceptual-map-scaffolding-reduces-novice-variance.md) [+W]. Within the LLM arm of a randomised experiment, novices given a conceptual roadmap with recommended sequencing scored M = .45 (SD = .14) on the post-intervention exam against M = .38 (SD = .22) for unguided novices, a difference the authors call weakly significant (p between .05 and .10). The scaffolding × AIC interaction was negative at the same level, so the benefit was largest for participants weakest at extracting help from the AI. This tests support against none, in favour, but not at conventional significance; the claim's title ("improves") reads more firmly than the result. Whether the exam was taken with the LLM is not stated on the claim page. Working paper.
- [Prompted, unprompted, and slide-based learning conditions yield statistically comparable multiple-choice performance](../claims/no-multiple-choice-difference-prompted-ai-learning.md) [~M]. A randomised experiment (n = 95) in construction-engineering education compared AI use with instructional prompts, AI use without them, and slides. Multiple-choice accuracy means were 0.72, 0.59 and 0.63; the ANOVA was not significant (p = 0.099) and equivalence was not tested. It qualifies the relationship: guidance on how to use the tool did not show a significant gain on a recall-type measure in this study; it does not show the guidance had no effect.
- [Structured GenAI scaffolding training improves students' problem-solving performance](../claims/genai-scaffolding-training-improves-revision-performance.md) [+M]. An RCT with 95 sophomore STEM students compared structured training in using generative AI as a collaborative partner with problem-solving training; the trained group scored higher on the posttest (d = 0.814). The comparison is between two trainings, not support against none, and the claim page does not say whether the posttest was taken with the AI; its title speaks of "AI-assisted revision performance" while the quoted result is a posttest score. It bears on how to set up AI support, not on whether support helps.
- [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S]. A systematic review of teacher–student scaffolding names fading as one of its three characteristics, and three experiments (20 ninth graders, 54 and 45 college students) found a gradual move from complete to increasingly incomplete worked examples to independent problems favoured near transfer over static example–problem arrangements, with removing the last steps first better than the first steps first. This compares two ways of giving support, not support against none, and belongs to the narrower model on [Scaffolding and Fading](scaffolding-and-fading.md); one synthesis found no moderation of the scaffolding effect by fading. Not settled: the text available could not confirm the entries.
- [Teacher repetition and translation as unplanned scaffolding can hinder rather than facilitate learning](../claims/repetition-translation-scaffolding-hinders-learning.md) [-W]. A forum piece reports a study of teacher–student exchanges in Cypriot after-school language programmes in which teachers' repetition and translation, used as unplanned support, hindered learning. It is a second-hand report with no design details or outcome measure on the claim page, so it shows only that something called scaffolding can fail; it does not show when. Not yet checked against its sources.
- [Scaffolded third-graders outperformed control students on reasoning based on irrelevant evidence after instruction](../claims/scaffolds-improve-irrelevant-evidence-reasoning-third-graders.md) [+M]. In whole-class inquiry lessons (N = 143 third graders), a condition adding a static structuring scaffold, teacher modelling and adaptive problematising prompts scored higher at posttest on reasoning from irrelevant evidence than the same unit without them (0.71 against 0.54 of items solved, d = 0.49, 95% CI 0.12 to 0.85; gain d = 0.73). It is the wiki's one whole-class test of support against less support, at an immediate posttest. In the same data, prior knowledge predicted posttest reasoning, and combined with teacher-judged logical reasoning to predict it, only without the scaffolds ([prior knowledge](../claims/scaffolds-mitigate-prior-knowledge-limit.md) [+W]; [logical reasoning](../claims/scaffolds-diminish-logical-reasoning-disadvantage.md) [+W]), while inhibition predicted it only with them ([inhibition](../claims/scaffolds-enable-inhibition-contribution.md) [~W]). The p-values printed for the experimental condition (0.054 for prior knowledge) are near the threshold, so "no relation under scaffolding" is not shown. The support was a bundle, so which part did the work is not known.
- [Groups' final solution scores were significantly higher on the scaffolded task than the non-scaffolded task](../claims/scaffolds-higher-final-solution-scores.md) [+W]. Eleven undergraduate engineering groups each did one scaffolded and one non-scaffolded ill-structured task; on the scaffolded one they spent more turns evaluating solutions ([turn proportions](../claims/scaffolds-shift-cps-turn-proportions-p3-p4.md) [+W]), their process distribution was closer to the authors' ideal ([Gini](../claims/scaffolds-lower-gini-cps-process-distribution.md) [+W]) and their solutions scored higher. The scaffold is confounded with the task, the scales differed (rescaled from 6 to 5 points), the rigour is coded r1, and every outcome was measured with the scaffold present, so this is assisted performance, not learning.
- [Neither the external collaboration script nor the reflection scaffold increased the quality of interaction in the subsequent collaboration](../claims/no-script-or-reflection-effect-on-interaction-quality.md) [~W]. A laboratory experiment compared a script, a collaborative reflection scaffold and no support, then had groups collaborate unsupported: no effect on interaction quality was found. Equivalence was not tested. It is a direct test of whether collaboration support carries into unsupported work, and it did not show that it does. [The degree of additional content-related support does not significantly moderate CSCL script effects](../claims/content-support-moderator-not-significant.md) [~W] is a meta-analytic subgroup contrast (d = 1.13 with content information, d = 0.70 with content scaffolds, not significantly different, post-hoc power 14%), so it cannot show the content scaffold adds nothing.
- [Empty-PC dyads built significantly better domain models than full-PC dyads, an effect concentrated among lower-achieving dyads](../claims/empty-pc-better-domain-models.md) [-M]. In inquiry-learning software, pairs given a regulative tool filled with goals, hints and cues (PC+) wrote better-structured, more complete lab reports ([lab reports](../claims/full-pc-better-lab-reports.md) [~M], d = 1.49 and 1.74) than pairs given the empty tool, but built worse system-dynamics models (d = 1.26 for the empty tool), with the gap about 10 points for lower-achieving pairs and 1 point for higher-achieving ones. The reports were scored on the template the full tool supplied, so they are aligned with the support. It contradicts the reading that more support helps weaker learners most, for regulative support; it compares more support with less, not with none.
- [Failure-driven and success-driven scaffolding before instruction produce similar posttest conceptual understanding](../claims/failure-and-success-scaffolding-similar-posttest-conceptual-understanding.md) [~M]. A classroom study (N = 221) of problem solving before instruction compared two kinds of support: nudging learners to generate suboptimal solutions, or giving low-specificity heuristics toward the optimal one. Conceptual posttests were similar (not shown equivalent), and [failure-driven scaffolding gave higher-quality constructive reasoning](../claims/failure-driven-scaffolding-higher-quality-constructive-reasoning.md) [+W]. It is the wiki's one comparison of two kinds of support on a common outcome, and it compares kinds, not support against none; no effect size is printed.

The wiki has one claim comparing two kinds of support on a common outcome (failure-driven against success-driven, before instruction) and one comparing more regulative support with less, but none comparing structuring the task with simplifying it, or procedural with metacognitive prompts. It has one whole-class test of scaffolding against the same lessons without it, at an immediate posttest, and none at a delayed horizon. Before transporting these observations, record the learners, setting (one-to-one, small group, computer-based), the support actually given and what it left to the learner, the comparator, outcome alignment and horizon. These studies do not rank one another; their comparisons differ.

## The evidence by question

Each question below links a general claim that gathers the studies behind it into one table, one row per distinct study, with each study's design and effect as recorded and no averaged verdict (`eval/synthesis/scaffolding.json`, `scripts/synthesize_claim.py`). The count is of distinct studies across the claim and the narrower claims that bear on it.

- Does support during an attempt improve later learning compared with attempting unsupported, and for which learners, contexts and outcomes? [Scaffolding improves learning](../claims/scaffolding-improves-learning.md) [+S]: 7 distinct studies.
- Must support be contingent on the learner's last response, rather than fixed? [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+S]: 20 distinct studies.
- Should support be withdrawn, and in what order? [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S]: 7 distinct studies.
- When the support can do the task for the learner (AI assistants), does it cost independent performance? [How genAI is used, not who uses it, predicts whether independent performance declines or improves](../claims/persistence-costs-concentrated-among-direct-solution-users.md) [~M]: 9 distinct studies.
- In what form, and under whose control, should prompts be given? [Textual instructional prompts yield significantly higher near-transfer posttest performance than pictorial prompts for novice circuit-analysis learners](../claims/textual-prompts-better-near-transfer-than-pictorial.md) [+M]: 1 distinct studies.

## Further evidence, not yet read against this model
<!-- Re-read 2026-10-19: the bullets moved into the model above (Grimm et al. 2023, Parks et al. 2026, Strauß et al. 2025, Vogel et al. 2016, Manlove et al. 2007, Sinha et al. 2021, Ludvigsen et al. 2018) are cited there; what stays below was read and does not change the model. -->
<!-- Restored 2026-10-02 (maintainer's decision): claims this page cited before the 2026-10-02 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Peerwise Student Questions 75 Percent High Quality](../claims/peerwise-student-questions-75-percent-high-quality.md) [~M] — does not test the relationship: it reports that 75% of sampled student-authored physics questions met quality criteria, in a course that gave scaffolding activities before authoring; the authors' link to the scaffolding is an untested hypothesis with no unscaffolded comparison.
- Un andamiaje de autoeficacia en un ambiente computacional incrementa el logro de aprendizaje en matemáticas de estudiantes de quinto de primaria que aprenden de forma individual. [+W] — attached 2026-10-15 from Ramírez Ruiz (2018), which proposed "Incorporar andamiajes motivacionales de autoeficacia en ambientes computacionales para favorecer logro equitativo entre estilos cognitivos"; tests this page's relationship. Not read 2026-10-19: this bullet and the two below link no claim page, and the wiki holds none for Ramírez Ruiz (2018), so there is no evidence entry to read against the model.
- El andamiaje motivacional computacional disminuye las diferencias de logro asociadas al estilo cognitivo en la dimensión DIC, favoreciendo equivalentemente a dependientes e independientes de campo. [+W] — attached 2026-10-15 from Ramírez Ruiz (2018), which proposed "Incorporar andamiajes motivacionales de autoeficacia en ambientes computacionales para favorecer logro equitativo entre estilos cognitivos".
- El andamiaje de autoeficacia aumenta la carga germánica y reduce las cargas cognitivas intrínseca y extrínseca en estudiantes que aprenden con un ambiente computacional. [+W] — attached 2026-10-15 from Ramírez Ruiz (2018), which proposed "Incorporar andamiajes motivacionales de autoeficacia en ambientes computacionales para favorecer logro equitativo entre estilos cognitivos"; tests this page's relationship.
- [Effects of collaboration scripts combined with heuristic worked examples on mathematical argumentation skills depend on prior knowledge and working-memory capacity, consistent with a Matthew Effect](../claims/script-worked-example-fading-matthew-effect.md) [~W] — attached 2026-10-18 from Carolyn P. Rosé et al. (2017), which proposed "Design scaffolding with attention to over-scripting risk and plan for fading scripting support over time". Read 2026-10-19: its only entry is a journal editorial describing the design of a 108-student factorial study (fading or not, order of scaffold types); it quotes no result, so it cannot inform the model until the study itself is recorded.

## Objective and learner-valued goal

The designer's objective is usually a capability the learner shows without the support, on a representative task, at a stated horizon and with stated aids. The learner may value something else: getting this task done, not looking stuck, or the real-world result the task stands for. Ask what they want and why, and record it apart from the objective. A learner who values finishing may use every support; one who values independence may refuse support they still need. In both cases how support is used reflects the goal as well as competence.

For example, an adult returning to study may want to submit a correct statistics assignment this week, while the designer wants them to choose and justify an analysis alone in next term's project. A step-by-step prompt sheet serves the first aim and may hide whether the second has been met. Agree which aim the support is for, and check the second with an unsupported task later, not with the prompted one.

## What would revise this model?

The expectation should weaken if supported attempts fail to beat unsupported ones on aligned outcomes measured without the support, for comparable learners, outside one-to-one tutoring and computer-based STEM problem solving. It should also weaken if explicit strategy instruction matches or exceeds the gain at lower cost, as the dynamic-assessment synthesis suggests. If the benefit appears only while the support is present, the page is describing assisted performance, not learning, and should say so. If one kind of support (for example, support that does part of the task) consistently fails where another succeeds, the relationship belongs to that kind, not to support in general. Do not protect the model by relabelling every failure as "the wrong support" or "outside the zone of proximal development" after the outcome is seen.

Assisted performance, unassisted immediate performance, delayed retention, transfer and use in the learner's own setting are separate claims. The evidence above establishes no best kind or amount of support, no individual readiness criterion and no classroom-scale effect.

## Claims

- [AI scaffolding differs from human scaffolding in availability, feedback timing, and dynamic adjustment, making its developmental impact conditional](../claims/ai-scaffolding-developmental-impact-conditional.md) [~W]
- [Computer-based scaffolding shows a consistently positive effect on cognitive outcomes in STEM education](../claims/computer-based-scaffolding-positive-cognitive-outcomes-stem.md) [+W]
- [How genAI is used, not who uses it, predicts whether independent performance declines or improves](../claims/persistence-costs-concentrated-among-direct-solution-users.md) [~W]
- [Scaffolding's influence was greater when measured at the principles assessment level than at the concept level](../claims/principles-level-assessment-highest-scaffolding-effect.md) [+W]
- [High-school students given GPT-4 access solved more problems in the moment but performed worse than controls once the tool was removed (review attribution)](../claims/gpt4-access-worse-after-removal-math.md) [~W]
- [Scaffolding's effect was greatest among adult learners, though based on a single outcome](../claims/scaffolding-effect-greatest-adult-learners.md) [+W]
- [Immediate unsupported application on a new passage showed no material-condition effect and no Proficiency × Material interaction, indicating no short-term dependence cost](../claims/no-short-term-dependence-cost-unsupported-application.md) [~W]
- [Open AI collaboration yielded the highest supported writing quality, while bounded AI support yielded the highest independent no-AI Week 8 performance](../claims/genai-supported-performance-independent-divergence.md) [+M]
- [LLM scaffolding level varies systematically across student request types and across assignments, but high-assistance responses remain dominant](../claims/scaffolding-varies-by-request-and-assignment.md) [-W]
- [Less successful teachers tended to provide less support because they mistakenly thought prompting was not part of scaffolding](../claims/less-successful-teachers-misconception-prompting-not-scaffolding.md) [~W]
- [Neither global nor local drawing support increased drawing quality, and local support significantly decreased it relative to unsupported drawing](../claims/drawing-support-did-not-increase-quality.md) [-W]
- [In Experiment 1, dyads that more often chose maximum CSCL scaffolding had lower post-test socio-discursive MAS](../claims/more-maximal-script-choices-correlated-lower-socio-discursive-mas.md) [-W]
- [Problematizing scaffolds produced a small significant positive effect on individual metacognitive knowledge compared to structuring scaffolds](../claims/problematizing-scaffolds-metacognitive-knowledge.md) [~W]
- [Problematizing scaffolds produced a small significant positive effect on transfer of individual domain knowledge compared to structuring scaffolds](../claims/problematizing-scaffolds-transfer-effect.md) [~W]
- [The editorial reports that CSCL scripts show positive effects on domain learning and collaboration process skills, and that scaffolding single versus combinations of collaborative activities affects script impact](../claims/cscl-scripts-positive-learning-collaboration-skills.md) [~W]
- [Problematizing scaffolds produced a medium significant positive effect on group performance compared to structuring scaffolds](../claims/problematizing-scaffolds-better-group-performance.md) [~W]
- [Metacognitive avatar scaffolds increase students' proportion of metacognitive activities, with no significant difference between scaffold types](../claims/scaffolds-increase-metacognitive-activities-equally.md) [~W]
- [Metacognitive scaffolding had no significant effect on individual domain knowledge (recall, knowledge tests, or transfer), with effect sizes close to zero](../claims/scaffolding-no-domain-knowledge-effect.md) [-W]
- [Scripted roles scaffold students' cognitive responsibility for building common knowledge in knowledge-building environments](../claims/scripted-roles-scaffold-cognitive-responsibility-knowledge-building.md) [~W]
- [As material scaffolds faded, Mrs. Lewis's students' performance returned to initial levels between High and Low support, while Mr. Green's students declined significantly across the unit](../claims/within-teacher-performance-trajectories-as-scaffolds-faded.md) [~W]
- [Provided support does not influence task regulation between conditions](../claims/support-does-not-influence-task-regulation.md) [~W]
- [On the knowledge assignment, neither the occasion-by-contingency interaction nor the three-way interaction with independent working time was significant](../claims/knowledge-assignment-null-contingency-effects.md) [~W]
- [AI-assisted performance during skill-building does not transfer to subsequent unassisted performance](../claims/ai-assisted-performance-no-unassisted-transfer.md) [-W]

## Related Principles
- [Scaffolding and Fading](scaffolding-and-fading.md)

## Examples
- Hints, worked examples, modeling, and coaching that are reduced as competence grows.
- [Backward-faded worked-example computer module for series and parallel circuit analysis](../elements/backward-faded-circuit-analysis-module.md)

## Key Sources
- Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89-100. [https://doi.org/10.1111/j.1469-7610.1976.tb00381.x](https://doi.org/10.1111/j.1469-7610.1976.tb00381.x)
- Bates, S. P., Galloway, R. K., Riise, J., and Homer, D. (2013). Assessing the quality of a student-generated question repository. https://arxiv.org/abs/1308.2202. [doi:10.48550/arxiv.1308.2202](https://doi.org/10.48550/arxiv.1308.2202)
- Reisslein, J., Atkinson, R. K., & Reisslein, M. (2004). Exploring the Presentation and Format of Help in a Computer-Based Electrical Engineering Learning Environment. Arizona State University. https://eric.ed.gov/?id=ED484994

<!-- deprecated 2026-10-02: superseded by the conditional model above. The former body, kept verbatim:

## Description
Scaffolding is the principle of providing temporary support that helps learners perform beyond what they could do independently. This page serves as the canonical short-form target for links that refer to scaffolding without explicitly naming fading or transfer of responsibility.

## Implications
Scaffolding is useful when learners can succeed with support but not yet on their own. Well-calibrated prompts, hints, models, or partial structures can improve learning when they respond to the learner’s actual bottleneck [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]. The design consequence is that scaffolding should be temporary: support that never fades can reduce independence, while support withdrawn too early can overload the learner [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S].

### Context
#### Requirements
- **A task slightly beyond independent reach**
- **Support calibrated to the learner's current need**
- **A plan to reduce support over time**
#### Constraints
- **Over-scaffolding can create dependence**
- **Premature withdrawal can trigger overload**

### Target Learners
- Learners building new concepts, procedures, or complex performances.

### Target Learning Objectives
- Support successful performance while developing independence.

### Theory
#### Supporting
- Sociocultural and apprenticeship traditions.
- [Cognitive Load Theory](../theories/cognitive-load-theory.md)

### Claims

- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M] — support helps most when it is matched to the learner’s current difficulty
- [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S] — effective scaffolds are designed to hand more of the task back to the learner over time
-->

<!-- merged 2026-10-07 from principles/pre-assessment-scaffolding-hypothesized-quality-driver ("Provide scaffolding and support activities before student question-authoring tasks, because context and support appear to bear on question quality"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Provide scaffolding and support activities before student question-authoring tasks, because context and support appear to bear on question quality

> **Principle** · [All principles](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 design), `q3` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
The article proposes that the quality of student-authored questions depends substantially on the material and support provided before authoring. It states: "It is our hypothesis that the higher quality of student-authored questions found in the present study is connected to the introductory exercises and scaﬀolding activities that we provided to students ahead of the ﬁrst PeerWise assessment task." The scaffolding set a high bar via a worked example and pushed students beyond what they currently know. This remains an untested hypothesis in this study.

## Design Implications

### Context
#### Requirements
- Class time (about 90 minutes) devoted to preparatory scaffolding activities before the first authoring task, including a high-quality example question setting the expected bar.
#### Constraints
- The article states this is a hypothesis not yet tested: the proposed controlled experiment contrasting no PeerWise, PeerWise without scaffolding, and PeerWise with scaffolding has not been run, and prior studies reporting scaffolding examined engagement, not question quality.

### Target Learners
- first-year undergraduate physics students, majors and non-majors

### Target Learning Objectives
- authoring high-cognitive-level assessment questions and explanations

### Claims
- [Peerwise Student Questions 75 Percent High Quality](../claims/peerwise-student-questions-75-percent-high-quality.md) [~M]

## Related Principles
- 

## Examples
-

## Key Sources
- Bates, S. P., Galloway, R. K., Riise, J., and Homer, D. (2013). Assessing the quality of a student-generated question repository. https://arxiv.org/abs/1308.2202. [doi:10.48550/arxiv.1308.2202](https://doi.org/10.48550/arxiv.1308.2202)
-->

<!-- merged 2026-10-07 from principles/text-system-controlled-prompts-for-novices ("For novice learners in highly structured domains, use text-based prompts delivered under the control of the instructional module"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# For novice learners in highly structured domains, use text-based prompts delivered under the control of the instructional module

> **Principle** · [All principles](index.md)
> **Evidence** · 6 claims (3 for, 3 mixed) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The article recommends that for high school students with little domain knowledge, help in computer-based modules should be textual and system-controlled. The authors conclude that "employing text-based prompts and having the prompts under the control of the instructional module are preferred by students" in their circuit-analysis module. This rests on their findings that textual prompts improved near-transfer performance and that externally regulated prompts were rated more favorably despite no performance difference.

## Design Implications

### Context
#### Requirements
- Learners with low prior knowledge in the structured content domain, as in the studied population
#### Constraints
- The authors note the advantage of textual prompts did not extend to far-transfer performance, and recommend testing learners with higher prior knowledge and more elaborate pictorial prompts

### Target Learners
- High school students without prior knowledge of electrical circuit analysis

### Target Learning Objectives
- Initial acquisition of structured, algorithmic problem-solving procedures such as series and parallel circuit resistance calculation

### Claims

- [Textual Prompts Better Near Transfer Than Pictorial](../claims/textual-prompts-better-near-transfer-than-pictorial.md) [+M]
- [External Prompt Regulation More Positive Attitudes](../claims/external-prompt-regulation-more-positive-attitudes.md) [+M]
- [Prompt Presentation No Performance Effect](../claims/prompt-presentation-no-performance-effect.md) [~M]
- [Textual prompts yield significantly stronger continuing motivation than pictorial prompts](../claims/textual-prompts-stronger-continuing-motivation.md) [+M]
- [Textual prompts produce higher first-attempt practice accuracy, while pictorial prompts produce higher second-attempt accuracy](../claims/prompt-format-first-second-attempt-accuracy.md) [~M]
- [In one 51-learner experiment on help formats in computer-based electrical engineering instruction, far-transfer scores were at the floor in every condition, and time spent on instruction did not differ significantly between conditions](../claims/far-transfer-floor-effect-and-equal-time.md) [~M]

## Related Principles
- 

## Examples

- [Backward-faded worked-example computer module for series and parallel circuit analysis](../elements/backward-faded-circuit-analysis-module.md)

## Key Sources
- Reisslein, J., Atkinson, R. K., & Reisslein, M. (2004). Exploring the Presentation and Format of Help in a Computer-Based Electrical Engineering Learning Environment. Arizona State University. https://eric.ed.gov/?id=ED484994
-->
