---
type: principle
id: scaffolding-and-fading
moved_from: [pattern/fading-based-scaffolding-approaches-serious-games, pattern/four-quadrant-library-learner-progression]
aliases: [scaffolding-fading, cognitive-apprenticeship, adult-help-promotes-active-agents-learning, balance-challenge-and-support-library-instruction]
title: Scaffolding and Fading
description: "Contingent support that is withdrawn as the learner shows unaided success may improve later independent performance on a task the learner cannot yet do alone, qualified by the task-specific starting response, how support ends, the setting and the outcome horizon."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: wood-1976
    resource: "https://doi.org/10.1111/j.1469-7610.1976.tb00381.x"
    title: "Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89–100"
    author: "Wood, D., Bruner, J. S., & Ross, G"
  - id: van-de-pol-2010
    resource: "https://doi.org/10.1007/s10648-010-9127-6"
    title: "van de Pol, J., Volman, M., & Beishuizen, J. (2010). Scaffolding in teacher–student interaction: A decade of research. *Educational Psychology Review, 22*(3), 271–296"
    author: "van de Pol, J., Volman, M., & Beishuizen, J"
  - id: renkl-2002
    title: "Renkl, A., Atkinson, R. K., Maier, U. H., & Staley, R. (2002). From example study to problem solving: Smooth transitions help learning. *Instructional Science, 30*(4), 293–308"
    author: "Renkl, A., Atkinson, R. K., Maier, U. H., & Staley, R"
  - id: van-de-pol-2019
    resource: "https://doi.org/10.1080/10508406.2018.1522258"
    title: "van de Pol, J., Mercer, N., & Volman, M. (2019). Scaffolding student understanding in small-group work: Students' uptake of teacher support in subsequent small-group interaction. Journal of the Learning Sciences, 28(2), 206-239"
    author: "van de Pol, J., Mercer, N., & Volman, M"
  - id: kupers-et-al-2017
    resource: "https://doi.org/10.1080/10508406.2016.1259624"
    title: "Kupers, E., van Dijk, M., & van Geert, P. (2017). Changing Patterns of Scaffolding and Autonomy During Individual Music Lessons: A Mixed Methods Approach. Journal of the Learning Sciences, 26(1), 131-166"
    author: "Kupers, E., van Dijk, M., & van Geert, P"
  - id: costley-2012
    resource: "https://eric.ed.gov/?id=ED529565"
    title: "Costley, K. C. (2012). An Overview of the Life, Central Concepts, Including Classroom Applications of Lev Vygotsky. https://eric.ed.gov/?id=ED529565"
    author: Costley, K. C
  - id: carder-1996
    resource: "https://eric.ed.gov/?id=ED406998"
    title: "Carder, Linda; Pracht, Carl; Willingham, J. Robert. (1996). Using Situational Leadership to Reach the Whole Population. https://eric.ed.gov/?id=ED406998"
    author: Carder, Linda; Pracht, Carl; Willingham, J. Robert
  - id: obikwelu-2013
    resource: "https://www.ejel.org"
    title: "Obikwelu, C, Read, J, and Sim, G. (2013). Children’s Problem-Solving in Serious Games: The “Fine-Tuning System (FTS)” Elaborated. The Electronic Journal of e-Learning Volume 11 Issue 1. https://www.ejel.org"
    author: Obikwelu, C, Read, J, and Sim, G
---

# Scaffolding and Fading

> **Principle** · [All principles](index.md)
> **Evidence** · 48 claims (23 for, 23 mixed, 2 against) · 48 studies (17 causal, 11 review, 8 theoretical, 4 associational, 4 qualitative, 3 quant-synthesis, 1 design), `q1`–`q4` · 7 of 48 report an effect size · 41 claims rest on one study

## Conditional relationship

A learner who cannot yet complete a task alone, but can complete it with help, may develop more independent performance when help is **contingent** and then **withdrawn**. Contingent means the tutor or system raises support after a failed attempt and lowers it after a success. The expected change is in later unassisted performance on the target task (`immediate-performance`, `delayed-retention`, `near-transfer`), not in assisted performance during the lesson. The learner's task-specific starting response bounds the relationship (`novice` for this task, not for the domain), as do the knowledge type (`procedure` and `complex-skill` in the studies below), the setting (most evidence is one-to-one tutoring or `lab`, little is `classroom`), how support ends, and the horizon. Withdrawing support too early or too late is a hypothesis about failure, not an established threshold. The [cognitive apprenticeship pattern](../patterns/cognitive-apprenticeship.md) is a reusable policy built on this relationship; its diagnostic branches are untested proposals.

## Fitting the design to a situation

Ask for three facts when the brief omits them: **who adjusts the support (a tutor, a teacher with a group, software, an AI tutor)**, **whether the target is unassisted performance and at what horizon**, and **whether near or far transfer is wanted**.

| If the brief says… | Then change… | Basis |
|---|---|---|
| One-to-one tutoring or an adaptive system | Make support contingent: start with the least help that might do, raise it after a failed attempt, lower it after a success | [Contingent scaffolding improves learning](../claims/contingent-scaffolding-improves-learning.md) [+M] |
| An AI tutor will give the support | Have it escalate and fade on what the learner does, holding back the full answer; this kept learners doing the thinking | [A contingent AI tutor keeps metacognitive demand](../claims/contingent-tutor-metacognitive-demand-matches-withholding-tutor.md) [+M]; [The contingent tutor surrendered the answer least](../claims/contingent-scaffolding-surrenders-full-answer-least.md) [+M] |
| Learners can use an AI assistant that gives answers | Bound it to hints, and schedule regular checks with no AI; answers given in practice lowered later unassisted performance | [AI assistance impairs unassisted performance](../claims/ai-assistance-impairs-unassisted-fraction-performance-exp1.md) [-M]; [Supported and independent performance diverge](../claims/genai-supported-performance-independent-divergence.md) [~M] |
| Learners move from worked examples to problem solving | Fade worked steps over a series of problems, from complete example to incomplete to independent, instead of fixed example–problem pairs | [Fading support promotes transfer of responsibility](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]; [Fading worked steps eases the example-to-problem transition](../claims/fading-worked-steps-facilitates-example-to-problem-transition.md) [+M] |
| The question is which steps to fade first | Removing the last steps first is one tested option; in another experiment the position did not matter, so either is defensible | [Fading support promotes transfer of responsibility](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]; [Faded step position had no effect](../claims/faded-step-position-no-learning-outcome-effect.md) [~M] |
| Transfer to new problems is the goal | Pair backward fading with prompts asking learners to name the principle each step uses | [Backward fading and principle prompts improve transfer](../claims/fading-and-principle-prompts-improve-probability-transfer.md) [+M] |
| A teacher supports several small groups at once | Before withdrawing support, ask a learner to do or explain the next step; learners who applied support rather than copying it gave more accurate later answers | [Uptake of support predicts answer accuracy](../claims/student-uptake-of-support-predicts-small-group-answer-accuracy.md) [~W] |
| Computer-based STEM scaffolds, and building a fading mechanism is costly | Fixed scaffolds may serve as well; the meta-analytic effect did not differ by whether scaffolds faded. Check unassisted performance before investing | [Scaffolding improves learning](../claims/scaffolding-improves-learning.md) [~M] |
| A learner succeeds only at the support level last given | Hold that level on a changed case and lower it one step at a time; no fading threshold is established | untested proposal |
| A learner keeps using support they no longer need | Make the support optional and record whether accuracy changes; guidance can become redundant as expertise grows | [Worked-example guidance becomes less effective with expertise](../claims/worked-examples-less-effective-with-expertise.md) [~M] |

## Observation, state and explanation

What can be observed is a response under stated conditions: a step attempted, the help requested or given (record its level), whether the learner applied, copied or ignored that help, and what they did next without it. "Within reach with support" and "has internalised the skill" are inferred states. The same response fits several states. Assisted success shows what the learner can do with *this* help; it does not show what they can do once it is gone. Copying a hint and applying it can produce the same answer.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Succeeds with a hint, fails the next comparable step without one | The hint supplied the reasoning; the learner has the reasoning but cannot yet start unaided; the next step demands something the hint did not cover | Give a matched step with no hint and ask for the first move and why; then give a minimal prompt (a cue, not the step) and record which level is enough. |
| Uses less help over successive problems | Growing competence; problems getting easier; reluctance to ask (cost, embarrassment, time) | Hold problem difficulty constant and check unassisted accuracy and reasoning; ask privately why help was not requested. |
| Answer is correct after support, but the learner cannot explain it | Copied the support (uptake as copying, not application); has a procedure without its rationale; language or expression barrier | Ask for an explanation in an accessible mode, and pose a changed case that the copied answer would not solve. |
| Performance drops sharply when support is removed | Support withdrawn before the step could be done unaided; withdrawal was abrupt and unannounced; the unaided task differs from the supported one | Check understanding before withdrawing (ask the learner to do or explain the next step); compare a gradual and an abrupt removal on matched tasks if feasible. |
| Asks for or follows support the learner no longer needs | Support has become redundant (expertise reversal); habit or anxiety; the support is required by the task's own conditions | Offer the task with support optional and record whether it is used and whether accuracy changes. |

These rows are proposals for interpreting a response; none has been tested with learners as a diagnostic. A probe is itself practice and can change the state it measures, so record each one. Keep the explanations that remain open rather than choosing the one whose name fits.

## Evidence and qualifications

- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]. Fourth and fifth graders learning long division one-to-one under fully contingent support solved more problems than those under moderate, high, partly contingent or no support, at an immediate and a one-month test. The design is coded as a quasi-experiment with 8 learners per condition. In a within-subjects study of 11 tutor–student pairs (grade 8, the circulatory system), more interactive tutoring showed similar immediate learning but better transfer. A meta-analysis of dynamic assessment ranked explicit strategy training above scaffolding and scaffolding above coaching. Sources: 0 of 3 entries pass and the rest could not be confirmed from abstracts. This does not predict a classroom-scale effect, and it does not show that contingent support beats explicit strategy instruction.
- [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]. Three experiments (20 ninth graders; 54 and 45 college students) compared a gradual move from complete examples to incomplete examples to independent problems with static example–problem arrangements. Results favoured fading at least for near transfer. Removing the last worked steps first did better than removing the first steps first, and learning-phase errors played a mediating role. Not settled: the abstracts could not confirm the entries. It establishes no fading rate and no far-transfer effect.
- [Backward fading and principle prompts supported transfer in probability learning](../claims/fading-and-principle-prompts-improve-probability-transfer.md) [+W]. University students (78, randomised, 2×2) learned probability principles. Backward fading did better than example–problem pairs on study-defined near- and far-transfer tasks, and so did principle-identification prompts; no interaction was detected. The claim page reports reading the full paper for these contrasts, but the entry carries no codes and the judge has not yet checked it. It gives no learner-specific threshold for when to fade and no delayed outcome.
- [Scaffolding improves learning](../claims/scaffolding-improves-learning.md) [~M]. A meta-analysis of 144 experimental studies of computer-based scaffolding in problem-centred STEM curricula reports ĝ = 0.46 on cognitive outcomes. The effect **did not differ by whether or how scaffolding was faded**. It supports the "support" half of this relationship and qualifies the "withdrawal" half. A pooled program-level effect forecasts no individual learner's response. Not yet checked against its sources.
- [Students' application of teacher support predicts accurate answers in small-group work](../claims/student-uptake-of-support-predicts-small-group-answer-accuracy.md) [~M]. This was observational (7 Dutch grade-7 social studies teachers, 28 students, 35 lessons). Students who *applied* support, rather than ignoring or copying it, gave more accurate later answers (odds ratio 1.29). How contingent the support was did not predict whether it was applied. In the qualitative cases, all 7 instances of applied contingent support followed a teacher checking understanding before withdrawing, and in 5 of 7 ignored instances the teacher withdrew without checking. That account is qualitative and associational; it does not show that checking before fading causes uptake. Not settled: the abstract could not confirm the entry.
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M]. A review of cognitive-load studies: guidance that helps novices can be redundant for learners who already hold the schema, and can depress their performance. It is the reason for withdrawal, but it does not say when an individual has crossed over. Not settled: the abstract could not confirm the entry.

Before transporting these observations, record learners, setting (one-to-one, small group, computer-based), the support actually given and how it ended, the comparator, outcome alignment and horizon. Most contingent-support evidence comes from one-to-one tutoring on well-structured tasks, and these studies do not rank one another; their comparisons differ.

## The evidence by question

- *Must support be contingent on the learner's last response, rather than fixed?* [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- *Should support be withdrawn, and in what order?* [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M]
- *When the support can do the task for the learner (AI assistants), does it cost independent performance?* [How genAI is used, not who uses it, predicts whether independent performance declines or improves](../claims/persistence-costs-concentrated-among-direct-solution-users.md) [~W]

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Teacher-student scaffolding and autonomy support co-evolve into self-reinforcing attractor states over sustained one-on-one instruction](../claims/scaffolding-autonomy-dynamics-form-self-reinforcing-attractor-states.md) [~M] — not yet checked against its sources
- [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — guidance becomes redundant as expertise grows, so fading is essential; not settled: the text available could not confirm the entries (abstract)
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M] — early support can reduce blind search for novices before independence develops; not settled: the text available could not confirm the entries (abstract)
- [Current serious games give all learners the same unregulated scaffolding, which the authors argue contradicts the notion of scaffolding](../claims/blanket-scaffolding-in-serious-games-contradicts-scaffolding-notion.md) [+W] — attached 2026-10-07 from Obikwelu et al. (2013), which proposed "Three fading-based scaffolding approaches: supportive, intrinsic and reflective scaffolding".
- [Imbalanced challenge and support causes novice library learners to give up or remain dependent (authors' asserted relationship)](../claims/challenge-support-imbalance-effects-novice-learners.md) [+W] — attached 2026-10-07 from Carder et al. (1996), which proposed "Four-quadrant progression from unready learner to independent library user with matching instructor behavior"; tests this page's relationship.
- [Over-reliance on AI scaffolding risks learned helplessness, so focus should shift to fostering self-regulated AI interaction](../claims/ai-scaffolding-fading-learned-helplessness.md) [+W] — attached 2026-10-10 from Steve Woollaston et al. (2026), which proposed "Implement dynamic fading: AI scaffolding must retreat as student competence increases".
- [A contingent AI tutor places metacognitive demand equal to a question-only tutor and higher than an answer-on-request assistant](../claims/contingent-tutor-metacognitive-demand-matches-withholding-tutor.md) [+W] — attached 2026-10-10 from Hou et al. (2026), which proposed "Preserved metacognitive demand: hold what the learner must decide constant and let carried load vary with demonstrated need"; tests this page's relationship.
- [Perceived task load and germane load did not differ between the contingent tutor and either baseline](../claims/perceived-load-unchanged-under-contingent-tutor.md) [~W] — attached 2026-10-10 from Hou et al. (2026), which proposed "Preserved metacognitive demand: hold what the learner must decide constant and let carried load vary with demonstrated need"; tests this page's relationship.
- [Successively fading out worked solution steps is effective for facilitating the transition from learning from worked examples to problem solving, compared to example-problem pairs](../claims/fading-worked-steps-facilitates-example-to-problem-transition.md) [+W] — attached 2026-10-13 from Renkl et al. (2004), which proposed "Fade out worked solution steps successively to support the transition from example study to problem solving"; tests this page's relationship.
- [Fading is associated with fewer unproductive learning events, which the authors link to better learning outcomes](../claims/fading-fewer-unproductive-learning-events.md) [+W] — attached 2026-10-13 from Renkl et al. (2004), which proposed "Fade out worked solution steps successively to support the transition from example study to problem solving".
- [Metacognitive development exhibits equifinality: multiple viable trajectories challenge linear developmental models](../claims/equifinality-metacognitive-trajectories.md) [-W]
- [Qualitative findings: ease of use supports engagement and confidence, but challenge must be tailored to ability and content must be culturally relatable](../claims/koku-qualitative-acceptability-themes.md) [+W]
- [More teacher support in AI-based instruction is not always better; a review found support worked well when balanced with students' autonomy and independent thinking](../claims/teacher-support-benefits-conditional-on-autonomy-balance.md) [~W]
- [Adaptive fading adjusted to discourse quality is reported as more effective than fixed fading regimes for developing internal script components, but long-term evidence is lacking](../claims/adaptive-fading-beats-fixed-regimes-short-term.md) [+W] — attached 2026-10-22 from Noroozi et al. (2018), which proposed "Design second-order argument scaffolding through a three-step guideline: diagnose internal scripts, adapt support, fade adaptively"; tests this page's relationship.
- [Fading of instructional support in collaborative argumentation has produced mixed results, with effectiveness depending on the fading criterion used](../claims/fading-collaborative-argumentation-mixed-results.md) [~W] — attached 2026-10-22 from Noroozi et al. (2018), which proposed "Design second-order argument scaffolding through a three-step guideline: diagnose internal scripts, adapt support, fade adaptively"; tests this page's relationship.

## Objective and learner-valued goal

The designer's objective is usually independent performance on a representative task, at a stated horizon and with stated aids. The learner may value something else: finishing tonight's assignment, not looking stuck in front of peers, or doing the real task (a working program, a passed placement) rather than its exercise version. Ask what they want and why, and record it apart from the objective. A learner who values finishing quickly may take every hint offered. A learner who values independence may refuse help they still need. In both cases help-seeking reflects the goal as well as the learner's competence.

For example, a student writing a lab report may want a good grade on this report, while the designer wants the student to plan and justify an analysis unaided next term. A sentence-starter template serves the first aim and may hide whether the second has been met. Agree which aim the support is for, and check the second with an unassisted report later, not with the templated one.

## What would revise this model?

The expectation should weaken if contingent support fails to beat fixed or no support on unassisted, aligned outcomes for comparable learners, beyond one-to-one tutoring. It should also weaken if the gain is matched by explicit strategy instruction at lower cost, as the dynamic-assessment synthesis hints. If faded and unfaded scaffolds keep producing the same outcomes, as in the computer-based scaffolding meta-analysis, the withdrawal half of the relationship is unsupported for that setting and should be stated as a design preference only. If checking understanding before withdrawal does not change uptake when tested experimentally, drop that diagnostic branch. Do not protect the model by calling every failure "faded too early" or "faded too late" after the fact. A threshold for withdrawal must be stated before the outcome is seen.

Assisted performance, unassisted immediate performance, delayed retention, transfer and use in the learner's own setting are separate claims. The evidence above establishes no optimal fading rate, no individual readiness criterion and no classroom-scale effect of contingency.

## Claims

- [Adaptive fading with periodic reinforcement yields higher independence than fixed-high or linear-decay scaffolding in simulation](../claims/adaptive-fading-beats-fixed-and-linear-scaffolding.md) [+W]
- [In a randomized experiment on fraction problems, participants who used an AI assistant solved fewer unassisted test problems and skipped more than control participants](../claims/ai-assistance-impairs-unassisted-fraction-performance-exp1.md) [-W]
- [Learners learned most about those principles that were faded](../claims/learners-learn-most-about-faded-principles.md) [+W]
- [Offloading work to AI costs learning: students given answers did well in practice but scored lower on an unassisted exam](../claims/gpt4-access-harms-learning-after-withdrawal.md) [~W]
- [The position of faded worked solution steps did not influence learning outcomes in Experiment 1](../claims/faded-step-position-no-learning-outcome-effect.md) [~W]
- [Scaffolding must be balanced: too little led to confusion and overload, while too much reduced opportunities for critical thinking](../claims/scaffolding-balance-confusion-versus-critical-thinking.md) [~W]
- [How genAI is used, not who uses it, predicts whether independent performance declines or improves](../claims/persistence-costs-concentrated-among-direct-solution-users.md) [~W]
- [Middle school teachers envisioned AI chatbots as adaptive instructional scaffolds providing differentiated support responsive to students' varying needs](../claims/teachers-envision-chatbots-adaptive-scaffolds-differentiated-support.md) [+W]
- [Teacher and researcher coaches both used a cognitive apprenticeship approach but differed in scaffolding style](../claims/bioworld-coaching-styles-cognitive-apprenticeship.md) [~W]
- [Less successful teachers tended to provide less support because they mistakenly thought prompting was not part of scaffolding](../claims/less-successful-teachers-misconception-prompting-not-scaffolding.md) [~W]
- [The scaffolding intervention unintentionally increased small groups' independent working time, roughly doubling it from premeasurement to postmeasurement](../claims/scaffolding-intervention-increases-independent-working-time.md) [+W]
- [Maternal contingent interventions led to children's successful actions at 12 and 18 months but not at 24 months, while children's success led to contingent withdrawal of support at every time-point](../claims/sequential-contingency-success-bidirectional.md) [+W]
- [Higher levels of contingent support were related to higher appreciation of support, regardless of measurement occasion or independent working time](../claims/contingency-relates-to-appreciation-of-support.md) [+W]
- [Expert scaffolding is associated with ILS adoption, but the fading stage shows a comparatively low rate (8.27%) and was a non-significant predictor](../claims/expert-scaffolding-associated-with-adoption-except-fading.md) [~W]
- [Teachers who worked with the model of contingent teaching increased their teaching quality more than teachers who did not participate, especially on the contingent-teaching steps](../claims/mct-pd-increased-teaching-quality-more-than-control.md) [~W]
- [When AI assistance is withdrawn, student performance tends to decline, revealing a lack of internalized learning strategies](../claims/ai-assistance-withdrawal-performance-decline.md) [~W]
- [Cognitive and metacognitive prompts in learning journals helped early in a term but became detrimental by its end; adaptive fading-out mitigated this](../claims/expertise-reversal-writing-journal-prompts-fading.md) [+W]
- [Learning journal writing improves learning outcomes, but learners often do not apply sufficient strategies without support; prompts, worked examples and fading are the supports studied](../claims/journal-writing-improves-outcomes-with-support.md) [~W]
- [Contingency is not treated as a necessary condition of scaffolding in bilingual education research, unlike broader educational research](../claims/contingency-not-necessary-condition-bilingual-education-scaffolding.md) [~W]
- [Fading-out prompts yield more cognitive strategy use and higher learning outcomes than permanent prompts](../claims/fading-out-prompts-beat-permanent-prompts.md) [+W]
- [Self-selected scaffolding customization yields higher effects than fixed time interval and performance-adapted customization](../claims/self-selected-customization-highest-effect.md) [~W]
- [The replication successfully reproduced the original study's execution of contingent instruction, with tutors applying the contingency rule in 68.9% of interventions versus 70% in 1978](../claims/tutor-adherence-contingency-rule-replicated.md) [~W]
- [Tutor accuracy in applying the contingency rule showed no significant association with children's posttest outcome, efficiency, or autonomy, with near-zero correlations](../claims/tutor-accuracy-no-posttest-association.md) [~W]
- [Body-to-body coupling between instructor and learner is greater during scaffolding than explanation instruction](../claims/btbc-greater-scaffolding-than-explanation.md) [+W]
- [Graduated prompts training also increased the number of transformations children applied correctly, indicating progression in task-solving strategies](../claims/graduated-prompts-training-transformations.md) [+W]

## Related Principles
- [Concreteness Fading](concreteness-fading.md)
- [Worked Examples](worked-examples.md) — often the first stage in a scaffolded sequence.
- [Chunking](chunking.md) — breaking the task into units that can be individually scaffolded.
- [Modeling](modeling.md) — a type of scaffold where expert performance is demonstrated.
- [Scaffolding](scaffolding.md) — the broader principle of temporary support during learning
- [Guided Practice](guided-practice.md) — often provides the instructional context in which fading happens
- [Procedural Learning](procedural-learning.md) — many procedural tasks depend on fading from modeled or prompted performance to independence
- [Observation/Shadowing](observationshadowing.md) — observation often provides the first exposure to expert practice before coached participation
- [Assess children's cognitive development both when performing alone and when assisted](multiple-methods-of-assessment.md)

## Examples

- **[Khan Academy Hints](https://www.khanacademy.org)** — Provides on-demand, progressive hints that scaffold a problem-solving task; the learner is encouraged to use fewer hints as they progress.
- **[Codecademy Completion Problems](https://www.codecademy.com)** — Initially provides full code examples, then transitions to "fill-in-the-blank" code, and finally to independent coding challenges.
- **[Faded Worked Examples](../strategies/faded-worked-examples.md)** — A sequence where the first problem is fully worked, the second is half-worked, and the third is a full problem to solve.
- [Provide worked examples during seatwork and homework to increase exposure to problem solving and reduce learning time](../strategies/worked-examples-seatwork-homework-problem-solving.md)
- [Design AI educational systems that fade support and require learner justification to preserve independent problem solving](../strategies/fade-ai-support-require-justification.md)
- [Use scaffolding techniques to help students complete tasks within their zones of proximal development](../strategies/scaffolding-within-zpd-classroom-strategy.md)
- [Teach Self-Regulation Skills](../strategies/teach-self-regulation-strategies.md)
- [When uncertain about a learner's level, begin with high direction and support and keep reassessing](../strategies/start-high-support-when-in-doubt.md)
- [Regulate fading rate per learner, distinguishing perceived fading rate (teacher-set) from actual fading rate (child-set)](../strategies/perceived-versus-actual-fading-rate-strategy.md)
- [Use hands-on practice and immediate feedback in bibliographic instruction for ESL students](../strategies/hands-on-instruction-esl-students.md)
- [Use learner skill levels to determine when to transition from worked examples to problem solving in tutoring systems](../strategies/skill-based-adaptive-fading-schedule.md)
- [From models and closed cues to open cues](../designs/models-closed-cues-to-open-cues-language-independence.md) — teacher cues fade from restrictive to open to build pupils' independent language use
- [Fade embodied support as schemas develop, starting with the least embodied task-relevant support](../strategies/fade-embodied-support-as-schemas-develop.md)

## Key Sources
- Kupers, E., van Dijk, M., & van Geert, P. (2017). Changing Patterns of Scaffolding and Autonomy During Individual Music Lessons: A Mixed Methods Approach. *Journal of the Learning Sciences, 26*(1), 131-166. [https://doi.org/10.1080/10508406.2016.1259624](https://doi.org/10.1080/10508406.2016.1259624)
- van de Pol, J., Mercer, N., & Volman, M. (2019). Scaffolding student understanding in small-group work: Students' uptake of teacher support in subsequent small-group interaction. *Journal of the Learning Sciences, 28*(2), 206-239. [https://doi.org/10.1080/10508406.2018.1522258](https://doi.org/10.1080/10508406.2018.1522258)
- Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89–100. [https://doi.org/10.1111/j.1469-7610.1976.tb00381.x](https://doi.org/10.1111/j.1469-7610.1976.tb00381.x)
- van de Pol, J., Volman, M., & Beishuizen, J. (2010). Scaffolding in teacher–student interaction: A decade of research. *Educational Psychology Review, 22*(3), 271–296. [https://doi.org/10.1007/s10648-010-9127-6](https://doi.org/10.1007/s10648-010-9127-6)
- Renkl, A., Atkinson, R. K., Maier, U. H., & Staley, R. (2002). From example study to problem solving: Smooth transitions help learning. *The Journal of Experimental Education, 70*(4), 293-315. [https://doi.org/10.1080/00220970209599510](https://doi.org/10.1080/00220970209599510)
- van de Pol, J., Volman, M., & Beishuizen, J. (2010). Scaffolding in teacher-student interaction: A decade of research. *Educational Psychology Review, 22*(3), 271-296. [https://doi.org/10.1007/s10648-010-9127-6](https://doi.org/10.1007/s10648-010-9127-6)
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship. In *Knowing, learning, and instruction*. [doi:10.5840/thinking19888129](https://doi.org/10.5840/thinking19888129)
- Collins, A., Brown, J. S., & Holum, A. (1991). Cognitive apprenticeship: Making thinking visible. *American Educator, 15*(3), 6–11, 38–46.
- Costley, K. C. (2012). An Overview of the Life, Central Concepts, Including Classroom Applications of Lev Vygotsky. https://eric.ed.gov/?id=ED529565
- Carder, Linda; Pracht, Carl; Willingham, J. Robert. (1996). Using Situational Leadership to Reach the Whole Population. https://eric.ed.gov/?id=ED406998
- Obikwelu, C, Read, J, and Sim, G. (2013). Children’s Problem-Solving in Serious Games: The “Fine-Tuning System (FTS)” Elaborated. The Electronic Journal of e-Learning Volume 11 Issue 1. https://www.ejel.org

<!-- deprecated 2026-10-01: superseded by the conditional model above. The former body, kept verbatim:

## Description
Scaffolding provides temporary, contingent support to learners as they develop new skills or knowledge. Fading is the systematic and gradual removal of those supports as the learner gains competence, leading to independent performance and the transfer of responsibility.

## Implications
Scaffolding and fading work because novices often need temporary support to perform productively, but that support only remains helpful when it responds to actual learner need [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+S]. The long-term aim is transfer of responsibility, so support has to be reduced as competence grows [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S]. If scaffolds remain too long they can create redundant load or dependency, and if they disappear too early they can trigger overload or failure. The design problem is calibration, not just support provision.

### Context
#### Requirements
- **Contingency (Diagnosis)**: The instructor or system must constantly assess the learner's current performance to provide support only when and where it is needed [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+S].
- **Transfer of Responsibility**: The goal is always the internalization of the skill, not just the completion of the task [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S].
- **Variety of Scaffolds**: Supports can include [think-aloud modeling](../elements/think-aloud.md), [worked examples](../elements/worked-examples.md), [hints](../elements/hints.md), or [coaching](../elements/coaching.md).

#### Constraints
- **Expertise Reversal**: Scaffolding that remains in place for an expert can cause redundant cognitive load and hinder performance [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md).
- **Over-Scaffolding**: Support that is too high or not faded quickly enough can lead to learner dependence.
- **Premature Fading**: Withdrawing support before the learner has developed the necessary internal schemas can lead to cognitive overload and failure.
- **Untimely Fading Blocks Uptake Even When Support Is Well-Calibrated**: A mediation study found that how contingent (well-calibrated) a teacher's support was did NOT predict whether students later applied it — what mattered was whether the teacher checked students' understanding before withdrawing, i.e., fading in time. [Students' application of teacher support predicts accurate answers in small-group work](../claims/student-uptake-of-support-predicts-small-group-answer-accuracy.md) [-M]
- **Abrupt Large Shifts in Support Style Can Fail**: Over sustained one-on-one instruction, a sudden, large change in how much autonomy/control a teacher grants (in either direction) can fall outside the dyad's established interaction pattern and fail to take hold, reverting to the prior pattern within a few sessions. [Teacher-student scaffolding and autonomy support co-evolve into self-reinforcing attractor states over sustained one-on-one instruction](../claims/scaffolding-autonomy-dynamics-form-self-reinforcing-attractor-states.md) [-M]

### Target Learners
- **Novice Learners**: Benefit from high-fidelity scaffolding during initial skill acquisition to manage intrinsic load [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+S].
- **Learners in the "Zone of Proximal Development"**: Scaffolding is specifically designed to support learners as they tackle tasks just beyond their independent capability.

### Target Learning Objectives
- **Complex Skill Acquisition**: Learning to perform integrated, multi-step tasks.
- **Problem-Solving**: Developing the ability to navigate ill-structured or novel challenges.
- **Self-Regulation**: Learning to monitor and adjust one's own performance as external scaffolds fade.

### Theory
#### Supporting
- **Zone of Proximal Development (Vygotsky)** — the distance between what a learner can do unassisted and what they can do with guidance.
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — scaffolding manages extraneous load for novices; fading prevents redundant load for experts [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].
- **Cognitive Apprenticeship** — utilizes modeling, coaching, and scaffolding/fading as core instructional methods.

### Claims

- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+S] — support is most effective when it adapts to the learner’s current difficulty instead of staying fixed
- [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S] — the purpose of scaffolding is growing independence, so support should be withdrawn deliberately as competence develops
- [Students' application of teacher support predicts accurate answers in small-group work](../claims/student-uptake-of-support-predicts-small-group-answer-accuracy.md) [~M] — contingency alone did not predict whether students applied support; timely fading (checking understanding before withdrawing) did
- [Teacher-student scaffolding and autonomy support co-evolve into self-reinforcing attractor states over sustained one-on-one instruction](../claims/scaffolding-autonomy-dynamics-form-self-reinforcing-attractor-states.md) [~M] — a sudden, large shift in support style can fail if it falls outside the dyad's established interaction pattern
-->

<!-- merged 2026-10-02 from principles/scaffolding-fading ("Scaffolding & Fading"), a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Scaffolding & Fading

> **Principle** · [All principles](index.md)
> **Evidence** · 3 claims (3 unmarked) · 8 studies (3 causal, 2 review, 1 quant-synthesis, 1 qualitative, 1 theoretical), `q3`–`q4` · 0 of 8 report an effect size · 1 claim rests on one study

## Description
Scaffolding & Fading is the short-form canonical target for designs that provide temporary support and then reduce it as learner independence grows.

## Implications

Scaffolding and fading matter when learners are expected to perform work they cannot yet do independently but can accomplish with the right support. The principle is not simply “help, then stop helping.” Support has to be calibrated to need, and [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) supports adapting help to learner performance rather than fixing it in advance. The reduction of support also has to respond to evidence of growing capability. Too much support held too long creates dependency and redundancy, which is consistent with [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md). Too little support or premature fading destabilizes performance before the learner has a workable schema or routine, while [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) supports heavier early guidance for novices.

### Context
#### Requirements
- **Temporary support tied to learner need** — hints, prompts, models, partial solutions, or structure must actually help the learner perform beyond current independent capacity
- **A plan to reduce that support over time** — the design needs a path from guided performance to increasing independence
#### Constraints
- **Too much or too little support at the wrong time undermines learning**
- **Support cannot stay generic forever** — fading depends on evidence about learner progress
- **Not all supports fade the same way** — some are reduced in amount, some in specificity, and some by shifting responsibility to the learner

### Target Learners
- Novices learning new procedures, concepts, or complex performances
- Learners who can succeed with support but are not yet ready for full independence
- Learners in environments where guided practice is a bridge to later autonomous work

### Target Learning Objectives
- Support transition from guided to independent performance
- Reduce unproductive search while preserving learner responsibility
- Build confidence and competence through calibrated release of support

### Theory
#### Supporting
- [Scaffolding and Fading](scaffolding-and-fading.md) — the fuller principle page that this short-form canonical page points to
- [Scaffolding](scaffolding.md) — explains why support is needed during early learning
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — support and fading can reduce overload early and avoid redundancy later

#### Contradicting / Qualifying
- [Self-Determination Theory](../theories/self-determination-theory.md) — support should still preserve autonomy and growing ownership rather than feel controlling

### Claims
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M] — support is stronger when it adapts to learner performance rather than staying fixed
- [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — guidance becomes redundant as expertise grows, so fading is essential
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M] — early support can reduce blind search for novices before independence develops

## Related Principles
- [Scaffolding](scaffolding.md) — the broader principle of temporary support during learning
- [Guided Practice](guided-practice.md) — often provides the instructional context in which fading happens
- [Procedural Learning](procedural-learning.md) — many procedural tasks depend on fading from modeled or prompted performance to independence

## Examples

### Illustrative

**[Fading Scaffolding](../elements/fading-scaffolding.md)** — Hints, prompts, or partial steps become shorter, less specific, or less frequent as competence grows.

**[Merrill's First Principles](../patterns/4cid-four-component-instructional-design.md)** — Learners move from activation and demonstration toward application with progressively less support.

**Worked example to independent problem sequence** — Learners first study or complete a heavily supported version, then solve increasingly less scaffolded problems on their own.

## Key Sources
- Renkl, A., Atkinson, R. K., Maier, U. H., & Staley, R. (2002). From example study to problem solving: Smooth transitions help learning. *The Journal of Experimental Education, 70*(4), 293-315. [https://doi.org/10.1080/00220970209599510](https://doi.org/10.1080/00220970209599510)
- van de Pol, J., Volman, M., & Beishuizen, J. (2010). Scaffolding in teacher-student interaction: A decade of research. *Educational Psychology Review, 22*(3), 271-296. [https://doi.org/10.1007/s10648-010-9127-6](https://doi.org/10.1007/s10648-010-9127-6)
-->

<!-- merged 2026-10-02 from principles/cognitive-apprenticeship ("Cognitive Apprenticeship"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Cognitive Apprenticeship

> **Principle** · [All principles](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 8 studies (3 causal, 2 review, 1 quant-synthesis, 1 qualitative, 1 theoretical), `q3`–`q4` · 0 of 8 report an effect size · 1 claim rests on one study

## Description
Cognitive apprenticeship is the principle of making expert thinking visible through modeling, coaching, scaffolding, and gradual participation in authentic tasks.

## Implications

Cognitive apprenticeship is most valuable where the important knowledge is embedded in judgment, interpretation, and process rather than in declarative rules alone. It treats learning as guided entry into expert practice, and visible models are especially valuable early because they reduce unproductive search for novices [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]. The instructor does not merely explain content; they model thinking, coach performance, calibrate support, and then fade assistance as learners become more capable [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M] [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]. The principle is especially strong for writing, diagnosis, inquiry, design, and other domains where expertise is partly tacit and situated.

### Context
#### Requirements
- **Access to modeled expert performance** — learners need to observe how experts think through authentic or realistic work, not just inspect finished outputs
- **Coaching and scaffolded participation** — the principle depends on guided learner performance after observation
#### Constraints
- **Tacit reasoning stays hidden unless experts externalize it** — experts often omit the very moves novices most need to see
- **The full sequence is resource-intensive** — modeling, coaching, and fading require more sustained interaction than content transmission alone
- **Poorly timed fading can destabilize learning** — supports need to be withdrawn in response to performance, not on an arbitrary timetable

### Target Learners
- Novices entering a disciplinary, professional, or craft-like practice
- Learners developing complex cognitive skills such as diagnosis, writing, design, inquiry, or problem solving
- Learners who need access to expert judgment rather than only explicit rules

### Target Learning Objectives
- Build strategic thinking, situated performance, and increasing independence
- Make tacit expert heuristics visible and learnable
- Support transfer from coached performance to more independent work

### Theory
#### Supporting
- [Situated Learning](../theories/situated-learning.md) — learning is shaped by participation in authentic practices and communities
- [Scaffolding](scaffolding.md) — calibrated support is one of the core mechanisms that lets learners do work they cannot yet do alone
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — modeling and fading can reduce the burden of unguided search during early acquisition

#### Contradicting / Qualifying
- [Constructivism](../theories/constructivism.md) — generally compatible, but qualifies that apprenticeship should still preserve learner sensemaking rather than collapse into imitation alone

### Claims
- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M] — visible models reduce unproductive search for novices during early learning
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M] — support is strongest when it adapts to learner performance rather than staying fixed
- [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M] — expert guidance should be faded as learners develop stronger schemas and greater independence

## Related Principles
- [Observation/Shadowing](observationshadowing.md) — observation often provides the first exposure to expert practice before coached participation
- [Modeling](modeling.md) — cognitive apprenticeship extends modeling into a fuller cycle of coached performance
- [Scaffolding](scaffolding.md) — explains how support is calibrated and gradually removed

## Related Patterns
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md)

## Examples

### Illustrative

**[Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md)** — A full instructional pattern in which expert modeling, coaching, articulation, and fading are sequenced over time.

**Clinical rounds and supervised diagnosis** — Learners observe diagnostic reasoning, attempt their own interpretations, receive targeted coaching, and gradually assume more of the reasoning burden.

**Studio critique and guided design practice** — In design education, instructors model tradeoffs, coach works-in-progress, and reduce direct guidance as learners gain fluency with critique and revision.

## Key Sources
- Collins, A., Brown, J. S., & Newman, S. E. (1989). Cognitive apprenticeship. In *Knowing, learning, and instruction*.
- Collins, A., Brown, J. S., & Holum, A. (1991). Cognitive apprenticeship: Making thinking visible. *American Educator, 15*(3), 6–11, 38–46.
-->

<!-- merged 2026-10-15 from principles/adult-help-promotes-active-agents-learning ("Adult help should promote children as active agents of their own learning, not only subject-matter assimilation"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Adult help should promote children as active agents of their own learning, not only subject-matter assimilation

> **Principle** · [All principles](index.md)
> **Evidence** · no claims cited

## Description
Citing Zaretskii (2009), the article states that adult help given to a child working on learning difficulties, whether from a teacher, psychologist, or parent, serves a dual purpose. It can support assimilation of a particular academic subject and also "promote other processes essential to developing children as active agents of their own learning." This frames adult assistance as building learner agency alongside immediate academic gains.

## Design Implications

### Context
#### Requirements
- Adult assistance from a teacher, psychologist, or parent during work on learning difficulties
#### Constraints
- 

### Target Learners
- children receiving adult help on learning difficulties

### Target Learning Objectives
- assimilating academic subject matter
- becoming active agents of their own learning

### Claims
- 

## Related Principles

- [Assess children's cognitive development both when performing alone and when assisted](multiple-methods-of-assessment.md)

## Examples

- [Use scaffolding techniques to help students complete tasks within their zones of proximal development](../strategies/scaffolding-within-zpd-classroom-strategy.md)
- [Teach Self-Regulation Skills](../strategies/teach-self-regulation-strategies.md)

## Key Sources
- Costley, K. C. (2012). An Overview of the Life, Central Concepts, Including Classroom Applications of Lev Vygotsky. https://eric.ed.gov/?id=ED529565
-->

<!-- merged 2026-10-15 from patterns/four-quadrant-library-learner-progression ("Four-quadrant progression from unready learner to independent library user with matching instructor behavior"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Four-quadrant progression from unready learner to independent library user with matching instructor behavior

> **Pattern** · [All patterns](index.md)
> **Evidence** · 2 claims (1 for, 1 against) · 2 studies (2 theoretical), `q1` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The paper organizes library learners into four developmental quadrants, each calling for a different instructor stance. Quadrant one students are unready and unable and receive high support and high direction, often more telling than teaching; quadrant two students, the "average freshman", receive high direction and support with more teaching and critical-thinking assignments; quadrant three students receive low direction and medium support as the librarian shifts to consultant; quadrant four independent users receive low direction and support, mainly through signage. The charted pattern pairs student characteristics with supportive instructor behavior at each level.

## Design Implications

### Context
#### Requirements
- Ongoing assessment of the student's developmental level so the instructional stance can move along with the learner
#### Constraints
- Framed for academic library instruction contexts

### Target Learners
- academic library users from inexperienced freshmen to faculty and independent researchers

### Target Goals
- progression toward independent library use and transfer of research skills across disciplines

### Claims

- [Imbalanced challenge and support causes novice library learners to give up or remain dependent (authors' asserted relationship)](../claims/challenge-support-imbalance-effects-novice-learners.md) [+W]
- [Metacognitive development exhibits equifinality: multiple viable trajectories challenge linear developmental models](../claims/equifinality-metacognitive-trajectories.md) [-W]

## Related Patterns
- 

## Examples

- [When uncertain about a learner's level, begin with high direction and support and keep reassessing](../strategies/start-high-support-when-in-doubt.md)

## Key Sources
- Carder, Linda; Pracht, Carl; Willingham, J. Robert. (1996). Using Situational Leadership to Reach the Whole Population. https://eric.ed.gov/?id=ED406998
-->

<!-- merged 2026-10-15 from patterns/fading-based-scaffolding-approaches-serious-games ("Three fading-based scaffolding approaches: supportive, intrinsic and reflective scaffolding"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Three fading-based scaffolding approaches: supportive, intrinsic and reflective scaffolding

> **Pattern** · [All patterns](index.md)
> **Evidence** · 3 claims (1 for, 2 mixed) · 5 studies (3 review, 2 causal), `q1`–`q3` · 0 of 5 report an effect size · 1 claim rests on one study

## Description
The paper enumerates three scaffolding approaches based on fading, drawn from Jackson et al. (1998). "As supportive scaffolding fades, the task is the same as it was before, but the goal is for the learner to have internalized the procedures and concepts which had been scaffolded". In intrinsic scaffolding the task changes as the scaffold fades, gradually introducing underlying complexity. Reflective scaffolding makes reflection explicit by eliciting articulation, for example player-character conversation with an NPC, faded by gradually disabling conversations from most to least helpful.

## Design Implications

### Context
#### Requirements
- Fading decisions must respect whether the task, the associations, or the reflection support is what fades
#### Constraints
- The paper notes it may be hard for the child to make fading decisions (citing Jackson et al., 1998)

### Target Learners
- Children playing serious games in classrooms

### Target Goals
- Internalizing scaffolded procedures and concepts
- Progressing from simpler to more complex or abstract task variations
- Explicit reflection on tasks such as planning, predicting and evaluating

### Claims

- [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S]
- [Current serious games give all learners the same unregulated scaffolding, which the authors argue contradicts the notion of scaffolding](../claims/blanket-scaffolding-in-serious-games-contradicts-scaffolding-notion.md) [~W]
- [Instructional support suited to novices can have negative effects for more expert learners (expertise-reversal effect), so instructional design should be tailored to learner experience](../claims/expertise-reversal-effect.md) [~W]

## Related Patterns

- [Four methods of reflection on performance: imitation, replay, abstracted replay, and spatial reification](../patterns/cognitive-apprenticeship.md)

## Examples

- [Regulate fading rate per learner, distinguishing perceived fading rate (teacher-set) from actual fading rate (child-set)](../strategies/perceived-versus-actual-fading-rate-strategy.md)

## Key Sources
- Obikwelu, C, Read, J, and Sim, G. (2013). Children’s Problem-Solving in Serious Games: The “Fine-Tuning System (FTS)” Elaborated. The Electronic Journal of e-Learning Volume 11 Issue 1. https://www.ejel.org
-->

<!-- merged 2026-10-15 from principles/balance-challenge-and-support-library-instruction ("Balance challenge and support when instructing inexperienced library users"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Balance challenge and support when instructing inexperienced library users

> **Principle** · [All principles](index.md)
> **Evidence** · 3 claims (2 for, 1 mixed) · 3 studies (1 causal, 1 review, 1 theoretical), `q1`–`q2` · 0 of 3 report an effect size · 3 claims rest on one study

## Description
The paper recommends that librarians provide support while consistently presenting small challenges, because both extremes harm progress: over-challenged students give up, and over-supported students stay dependent. It states "It requires skill on the instructor's part to provide the correct balance of challenge and support at this level." The balance is achieved through individualized instruction, a safe environment for asking questions, and hands-on experience.

## Design Implications

### Context
#### Requirements
- Instructor skill in assessing the student's current level and adjusting support and challenge accordingly
#### Constraints
- Described specifically for quadrant-one (unready and unable) learners in individual library instruction

### Target Learners
- inexperienced college library users, including adult learners and special-needs students

### Target Learning Objectives
- independent use of library resources and progression toward learner autonomy

### Claims

- [Challenge Support Imbalance Effects Novice Learners](../claims/challenge-support-imbalance-effects-novice-learners.md) [+W]
- [Qualitative findings: ease of use supports engagement and confidence, but challenge must be tailored to ability and content must be culturally relatable](../claims/koku-qualitative-acceptability-themes.md) [+W]
- [More teacher support in AI-based instruction is not always better; a review found support worked well when balanced with students' autonomy and independent thinking](../claims/teacher-support-benefits-conditional-on-autonomy-balance.md) [~W]

## Related Principles
- 

## Examples

- [Four-quadrant progression from unready learner to independent library user with matching instructor behavior](scaffolding-and-fading.md)
- [When uncertain about a learner's level, begin with high direction and support and keep reassessing](../strategies/start-high-support-when-in-doubt.md)
- [Use hands-on practice and immediate feedback in bibliographic instruction for ESL students](../strategies/hands-on-instruction-esl-students.md)

## Key Sources
- Carder, Linda; Pracht, Carl; Willingham, J. Robert. (1996). Using Situational Leadership to Reach the Whole Population. https://eric.ed.gov/?id=ED406998
-->
