---
type: principle
id: feedback-loops
aliases: [design-feedback-on-external-outputs-asynchronous, prefer-feedback-loops-over-feedback-systems, dl2f-continuous-improvement-principle]
title: Feedback Loops
description: "For a learner whose performance can be observed, information about it is expected to improve later performance only when the loop closes (the information says what to change, a next attempt uses it, and that attempt is checked again on a new item); corrective feedback and correct-and-recheck programmes are supported on average, but no claim here tests a closed loop against the same feedback without a next attempt."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-15
sources:
  - id: hattie-2007
    resource: "https://doi.org/10.3102/003465430298487"
    title: "Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81-112"
    author: "Hattie, J., & Timperley, H"
  - id: clark-2012
    resource: "https://doi.org/10.1007/s10648-011-9191-6"
    title: "Clark, I. (2012). Formative assessment: Assessment is for self-regulated learning. *Educational Psychology Review, 24*(2), 205-249"
    author: Clark, I
  - id: pollard-2025
    resource: "https://doi.org/10.24059/olj.v29i3.4555"
    title: "Pollard, V., Armatas, C., & Pepe, A. (2025). Feedback is integral: Using a revised ICAP Framework to achieve active learning in an asynchronous online course. Online Learning, 29(3), 236-253. https://doi.org/10.24059/olj.v29i3.4555"
    author: "Pollard, V., Armatas, C., & Pepe, A."
  - id: baker-a-weisgrau-j
    resource: "https://doi.org/10.51388/20.500.12265/155"
    title: "Baker, A., Weisgrau, J., & Bristal Philyaw, K. (2022, May). Feedback loops: Mapping transformative interactions in education innovation. Digital Promise. https://doi.org/10.51388/20.500.12265/155"
  - id: merueña-2023
    resource: "https://doi.org/10.36713/epra2016"
    title: "Merueña, J. A. A. (2023). Dynamic Language Learning Framework (DL2F) Instructional Model. EPRA International Journal of Research and Development (IJRD). https://doi.org/10.36713/epra2016"
    author: Merueña, J. A. A
---

# Feedback Loops

> **Principle** · [All principles](index.md)
> **Evidence** · 29 claims (17 for, 10 mixed, 2 against) · 43 studies (12 causal, 9 quant-synthesis, 9 review, 5 design, 4 qualitative, 2 associational, 2 theoretical), `q1`–`q4` · 7 of 43 report an effect size · 20 claims rest on one study

## Conditional relationship

This page owns the **loop as a whole**: a learner's performance is observed, information about it reaches someone who can act on it (the learner, an instructor or a system), the next attempt is changed by that information, and the next attempt is observed again. For a learner working on a task where performance can be seen and repeated on comparable items (a `procedure`, a `concept` or `principle` applied to new cases, a draft of a `complex-skill` product such as writing), information about the performance is expected to improve later performance only when the loop **closes**: the information says what to change, a next attempt follows soon enough to use it, and that attempt is checked on a new item rather than the corrected one. Information that ends the episode (a score, a comment returned after the unit has moved on, praise of the person) has no route to an effect in this model. Over sessions the loop is expected to move from instructor- or system-run towards learner-run, as the learner learns to compare their own work with the target.

The relationship is conditional on what the information carries (corrective and high-information feedback are supported on average; feedback that draws attention to the self can make performance worse), on whether the next attempt actually uses it, on who can run the loop at the scale of the group, on the learner's expertise, and on the horizon measured (`immediate-performance` on the corrected item, `near-transfer` to a new item, `delayed-retention`). **No claim in the wiki compares a closed loop with the same feedback given without a next attempt, or varies the number or length of cycles.** The nearest evidence tests packages that contain a closed loop (correct-and-recheck mastery programmes, draft–feedback–revision peer review, contingent tutoring, intelligent tutoring), the content of feedback on its own, and self-monitoring as a mechanism. So the design below is a labelled default, not a tested model.

How the converted siblings sit beside this page, so a designer can go to the one that holds each decision: [Formative Assessment](formative-assessment.md) holds how a single response is interpreted against rival explanations and which next action it warrants; this page holds whether that action happens, is re-observed, and repeats. [Immediate Feedback](immediate-feedback.md) holds **when** the information arrives relative to the attempt; this page only requires that it arrive before the next attempt it is meant to change. [Assessment for Learning](assessment-for-learning.md) holds shared criteria and the stakes that make honest evidence possible. [Mastery Learning](mastery-learning.md) holds one specific loop, a criterion-gated correct-and-recheck before advancing between units. [Self-Regulated Learning](self-regulated-learning.md) holds the learner-run loop of planning and monitoring; this page hands over to it. [Check-ins](check-ins.md) holds loops fed by learners' self-reports of their state. The [formative assessment pattern](../patterns/formative-assessment.md) and the [mastery learning pattern](../patterns/mastery-learning.md) carry reusable loop policies; their branches are untested proposals.

## Default design, while the relationship is untested

The earlier page's guidance (observable performance, actionable information, an opportunity to respond, interpretation support; avoid delay, overload, low-information scores and permanent external correction), kept as a concrete default. Each step states its evidence.

1. **Plan the next attempt before the first one.** For every task that will be observed, write the follow-up attempt in advance: a matched item for a step or problem, a revision of the same draft for a written or made product, a re-run of a performance. If no next attempt exists, the feedback is commentary. Untested proposal; from the earlier page ("opportunity to respond").
2. **Make the performance observable and aligned.** Elicit a short response that shows the capability itself (a worked solution, a paragraph, a recorded attempt), not only a right/wrong answer, so the information can say what to change. How to read the response is modelled in [Formative Assessment](formative-assessment.md). Untested here as a step; in asynchronous online courses, the authors of one course audit argue that without an output that receives feedback there is little to show what a learner did ([feedback makes behaviour seen](../claims/feedback-makes-behaviour-seen-asynchronous.md) [+W], an argument, not a comparison).
3. **Give information about the task and what to do next, one or two targets at a time.** Say what was wrong or missing and the next move; leave out praise of the person. Evidence: feedback improves learning on average, more the more information it carries, and more than a third of feedback interventions in one synthesis made performance worse, the more so as they drew attention to the self ([Feedback improves learning by a medium amount on average, but its effect varies widely with the information it carries, and more than a third of feedback interventions reduce performance](../claims/feedback-improves-learning.md) [+S]); intelligence praise after success was followed by worse performance after a later failure in fifth graders ([Praise for intelligence, rather than for effort, after success undermines children's motivation and performance after a later failure](../claims/feedback-praise-reduces-learning.md) [-M]). The one-or-two-target limit is an untested proposal from the earlier page's warning about signal overload.
4. **Require a visible response to the information.** The learner retries, revises and marks what they changed, or states the next step before attempting it. Evidence is thin: in one case study, required revise-and-resubmit after probing feedback moved one teacher candidate towards citing evidence, but progress was not linear and another candidate did not improve ([probing feedback with revise-and-resubmit](../claims/probing-feedback-revise-resubmit-evidence.md) [+W]); in one study of 28 college students, those who complied more with a revise-summary prompt gained more (associational, [revise-summary compliance](../claims/revise-summary-compliance-predicts-learning-gains.md) [~M]); in log data from one platform, a workflow that had students select and prioritise AI-generated feedback and then discuss the selection was followed by more uptake (26.2%) than a directed workflow (14.1%) or a self-directed one (0.1%) ([enacted feedback uptake](../claims/enacted-feedback-higher-uptake-than-directed-self-directed.md) [+M]; uptake is measured within each workflow, and no learning outcome is reported).
5. **Re-observe on a new item, not the corrected one.** A corrected answer can be copied; the check that the loop worked is a fresh comparable item, unaided. For drafts, the check is the next piece of work, not the revised draft. Evidence for the recheck: correct-and-recheck mastery programmes outperformed conventional instruction on examinations in 108 controlled evaluations ([Mastery Learning Improves Outcomes](../claims/mastery-learning-improves-outcomes.md) [+M]); the recheck itself is not isolated there.
6. **Change the support when the same error survives two cycles.** Do not repeat the same message: switch to a worked example of the step, a contrasting case, or a demonstration, then a further new item. Evidence: support adjusted to each response beat fixed or no support in one-to-one tutoring of children on long division, at immediate and one-month tests ([Contingent scaffolding](../claims/contingent-scaffolding-improves-learning.md) [+M]); the two-cycle threshold is an untested proposal. The mastery claim's own discussion says recycling learners through the same material mostly re-exposes them to failure.
7. **Ask for confidence, and loop back to confident errors.** Before showing the answer, ask how sure the learner is; correct confidently wrong answers explicitly and put the item back into a later session. Evidence: corrected high-confidence errors are better retained than low-confidence ones ([hypercorrection](../claims/high-confidence-errors-improve-retention.md) [~S]); the claim's evidence is mostly recall of facts.
8. **Hand the loop over across sessions.** A default arc for a unit of several weeks (untested proposal):
   - *Early sessions*: instructor- or system-run loops on short items. Three to five cycles (attempt, information, matched retry) per new step in a session, each cycle a few minutes. In one observation study, secondary mathematics teachers trained in group-based mastery learning gave about 20 percent of class time to the corrective loop, having given virtually none before ([trained teachers' loop time](../claims/training-increases-feedback-corrective-loop-time.md) [+M]); use that as a planning figure, not a tested dose.
   - *Middle sessions*: the learner checks their own attempt against criteria or a worked answer **before** receiving feedback, and the feedback then checks the learner's judgement as well as the work. Evidence for self-monitoring as the mechanism is theoretical and review-level ([Self-monitoring](../claims/self-monitoring-improves-self-regulation.md) [+M]); learners' self-judgements need checking (see [Assessment for Learning](assessment-for-learning.md)).
   - *Late sessions*: the learner runs the loop; external information comes only on unaided samples and at a delayed recheck about a week after the step was learned.
9. **Move on, or not.** Move a learner on from a step when two consecutive new items are correct unaided and the delayed recheck holds; send a learner back into instructor-run loops when a delayed recheck fails. Untested thresholds; set locally and record them. How a criterion gates advancement between units is modelled in [Mastery Learning](mastery-learning.md).
10. **Close the instructor's loop too.** After each checkpoint, record the decision it informed (reteach, regroup, extend, move on) and check at the next checkpoint whether that decision helped. Untested proposal; from the earlier page (an exit ticket that changes the next day's grouping). The step is not automatic: a brief citing earlier research reports that teachers who can identify where a learner is do not necessarily know the next instructional step ([noticing is not enough](../claims/noticing-not-enough-next-steps.md) [~W], reported second-hand), so plan the candidate next moves for each likely response before the checkpoint.

## Fitting the design to a situation

The three facts that most change the decision:

- **Who can read each performance and how soon the next attempt follows.** One-to-one tutoring, a teacher with thirty learners, peers, software and the learner alone close the loop at very different rates; most evidence for responsive loops is one-to-one. If unstated, ask: after an attempt, who will look at it, and when will the learner make the next attempt?
- **What the next attempt is.** A matched item minutes later, a revised draft days later, and a performance next term make different loops. If unstated, ask: what will the learner do differently next time, on what task, and how will anyone see whether they did?
- **Whether the learner can judge their own work yet.** A novice needs the information supplied; a learner who can compare their work with the target can run the loop with occasional checks. If unstated, ask: shown their own attempt and a correct one, can the learner say what differs?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are `novice` on the task | Run the loop for them: task-level information on every attempt, a matched retry at once, the step re-modelled after two failed cycles | [Contingent scaffolding](../claims/contingent-scaffolding-improves-learning.md) [+M] (children, one-to-one, long division) |
| Learners are `advanced`, or already accurate unaided | Shorten external loops: ask for self-evaluation first, give information only on what the self-evaluation missed, and loop on harder or transfer items | [Expertise reversal](../claims/expertise-reversal-effect.md) [~M] (review of guidance studies, carried to feedback; no crossover point given) |
| Learners are `child` (primary age) | Shorter cycles with the adult reading each attempt; praise the strategy or the work, never ability; small groups so attempts can be seen | Praise: [Praise for intelligence, rather than for effort, after success undermines children's motivation and performance after a later failure](../claims/feedback-praise-reduces-learning.md) [-M] (fifth graders). Cycle length: untested |
| Goal is a written or made product (`complex-skill`) | Loop over drafts: draft, structured peer or teacher feedback against criteria, revision within a few days, then a new piece checked for the same targets | [Peer Feedback Improves Writing](../claims/peer-feedback-improves-writing.md) [+M] (higher education, 24 studies; against no feedback); revision interval untested |
| Goal is spoken second-language accuracy | Correct errors in the exchange itself, with prompts that ask the learner to reformulate rather than only recasts; keep it up over many sessions | [Corrective feedback on L2 errors](../claims/corrective-feedback-effect-on-l2-development-is-significant-and-durable.md) [+S] (two meta-analyses; gains held on delayed tests; prompts larger than recasts in the classroom synthesis; the two disagree on whether longer treatments do better, and younger learners benefited more, so the pooled effect fits adults least) |
| `classroom`, one teacher and a large group | Collect every learner's attempt at once (mini-whiteboards, a poll, a short written item), give whole-class information on the commonest error, have everyone do one matched item, then go to those who still fail; use peers with a rubric for drafts; budget class time for the loop | [Trained teachers' loop time](../claims/training-increases-feedback-corrective-loop-time.md) [+M] (secondary mathematics, time allocation only, no learning outcome); [rubrics and peer feedback](../claims/rubrics-improve-peer-feedback-quality.md) [~M] (rubrics changed peer comments, one study found less reflective feedback) |
| Little facilitator time or equipment: volunteers, busy shifts, no devices | Run the loop in buddy pairs: one partner watches an attempt against a posted checklist of two or three points, names one thing to change, and the other retries at once; a wall tally records which checklist points were met; the facilitator rechecks a sample (one new unaided attempt from two or three people per shift) and changes the checklist if the same point keeps failing. No paperwork beyond the tally | Untested proposal; peer reading carried from [peer feedback on writing](../claims/peer-feedback-improves-writing.md) [+M], which tested drafts, not practical tasks |
| `online-self-paced`, no teacher present | Build automatically checked items with a retry on a new item after each piece of information; route a learner who fails twice to a worked example; keep a delayed recheck in a later session | [Intelligent tutoring systems improve achievement over non-individualised instruction](../claims/adaptive-learning-improves-outcomes.md) [+S] (intelligent tutoring beat large-group, textbook and other computer instruction, not human tutoring or small groups; gains were smaller on standardized than on locally developed tests) |
| Feedback comes from a generative AI tool | Keep a person in the loop to help learners interpret and apply the AI's comments; have the learner choose and rank which comments to act on before revising, and check the revision against the chosen targets | [Feedback quality predicts revision only with teachers](../claims/feedback-quality-predicts-revision-only-in-teacher-condition.md) [~M] (one essay study: teacher feedback quality predicted revised-draft quality, AI feedback quality did not); [enacted feedback uptake](../claims/enacted-feedback-higher-uptake-than-directed-self-directed.md) [+M] (uptake, not learning) |
| Mixed modes: some learners remote, some in the room, or phone-only | Use one submission channel everyone can reach (a shared form or chat poll), return information in that channel, and give remote learners the same matched retry; for phone-only learners keep items short and one target per message | untested proposal |
| One session only | Run at least two complete cycles inside the session and end with one unaided new item; report what that item shows and claim no retention | untested proposal |
| Stakes are high, or the work is graded | Keep loop items ungraded and separate from the graded task; judge readiness only on unaided new items; let a revision replace an earlier mark if revision is the point | untested; [Assessment for Learning](assessment-for-learning.md) holds the stakes model ([retakes and revisions](../strategies/retakes-and-revisions.md) is a recipe, untested) |
| Learners have low confidence or low literacy | Give information privately, about the task, in short spoken or shown form (a demonstration, a marked example) rather than long written comments; one target per cycle | untested proposal; person-focused praise is the one thing with evidence against it ([Praise for intelligence, rather than for effort, after success undermines children's motivation and performance after a later failure](../claims/feedback-praise-reduces-learning.md) [-M], children) |
| Adults in work settings (`adult-workplace`, `workplace-clinical`) | Loop on real work outputs (a case note, a call, a procedure); a supervisor or peer reads one output per cycle against a stated criterion, and the next output is the re-observation | untested; in one teacher-education case, probing feedback with required resubmission helped one candidate and not another ([probing feedback](../claims/probing-feedback-revise-resubmit-evidence.md) [+W]) |
| A product or performance for a real audience | Run the loops in rehearsal with a critic using the criteria, before the audience; treat the audience's response as information for the next product, not a judgement on this one; do not show the audience the drafts or the critique if it should see only the finished work | untested proposal |
| Learners receive feedback but do not use it | Make the use visible: the learner marks what they changed, or answers "what will you do next?" before the next attempt; no new information until the last was used | [revise-summary compliance](../claims/revise-summary-compliance-predicts-learning-gains.md) [~M] (associational, 28 college students, one tutoring system) |
| Learners answer confidently and wrongly (misconceptions) | Ask for confidence before revealing answers; correct confident errors explicitly and bring the item back later | [hypercorrection](../claims/high-confidence-errors-improve-retention.md) [~S] (mostly recall; carried to misconceptions untested) |
| Information can only come later (marking takes days) | Keep the loop closed by attaching a task: the learner uses the returned comments on a new item before the next unit, rather than reading and filing them; whether earlier would be better is not settled | For one outcome, immediate and delayed feedback were equally effective ([feedback after multiple-choice tests](../claims/feedback-after-multiple-choice-tests-halves-lure-intrusions.md) [+M], reported second-hand); timing is held on [Immediate Feedback](immediate-feedback.md) |

Thirteen of the seventeen rows cite a claim, two of them (low confidence or literacy, work settings) only for a limit or a neighbouring case; four are untested proposals. Most cited claims are carried to the row's setting from another one (the contingent-support evidence is one-to-one with children, the hypercorrection evidence is recall of facts, the loop-time study measured teachers' time, not learning), and each row says so.

## Observation, state and explanation

What can be observed in a loop is a sequence: an attempt under stated conditions, the information given (its content, source and delay), what the learner did with it, and the next attempt on a stated item. "Understood the feedback", "has corrected the error" and "can now monitor their own work" are inferred states. A correct retry on the corrected item shows the information was followed; it does not show the change carried to a new item or will last.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Information given, next attempt unchanged | The information was not read or not understood; it named a problem but not a next move; the learner lacked the skill to act on it; the next attempt came too late to connect | Ask the learner to say what the feedback asks them to do, then give a matched item with that move prompted; compare with an item where the move is shown. |
| Correct on the retry of the corrected item, wrong on a new item | The answer was copied; the correction was item-specific; the new item differs more than intended | Give a second new item that varies only the surface, and ask for the step and why. |
| Same error survives two or three cycles | A misconception the information does not address; the information is accurate but too abstract; the learner is anxious and attending to being wrong, not to the task | Present a contrasting case where the misconception and the correct rule predict different answers; give the information privately and as a demonstration. |
| Learner revises only what was pointed out, and new errors of the same kind appear | Compliance with comments rather than a changed criterion; the criterion is not understood | Ask the learner to mark one further instance of the issue in their own work before the next feedback. |
| Accurate at the end of a run of loops, weaker a week later | Loops supported performance without consolidation; items too close together; interference | Recheck at a delay on a new item and record every practice and feedback episode in between. |
| Learner's self-check agrees with the teacher's on some criteria and not others | Calibration differs by criterion; the criteria are understood unevenly | Keep external information on the criteria where the self-check misses, withdraw it where it agrees. |

These rows are proposals, untested as diagnostics. A probe is itself another cycle and changes the state it measures, so record it, and keep rival explanations open.

## Evidence and qualifications

No claim in the wiki compares feedback followed by a required next attempt with the same feedback given without one, or varies the number, length or ownership of cycles. The claims below test neighbouring parts of the loop.

- [Feedback improves learning by a medium amount on average, but its effect varies widely with the information it carries, and more than a third of feedback interventions reduce performance](../claims/feedback-improves-learning.md) [+S]: two meta-analyses. Wisniewski et al. (2020), 435 studies, report a medium average effect (d = 0.48) with large heterogeneity, larger the more information the feedback carries (reinforcement or punishment d = 0.24, corrective d = 0.46, high-information feedback including self-regulation d = 0.99). Kluger & DeNisi (1996), 607 effect sizes in laboratory and field settings, report d = .41 on average, but **more than a third of feedback interventions reduced performance**, and feedback was less effective the more it moved attention from the task to the self. It supports the content step and is also the main limit on this page: information alone does not reliably improve the next performance.
- [Mastery Learning Improves Outcomes](../claims/mastery-learning-improves-outcomes.md) [+M]: a meta-analysis of 108 controlled evaluations at college, high-school and upper-elementary level found mastery programmes (correct and recheck before advancing) improved examination performance, apparently more for weaker students, while increasing time on task and, in self-paced college programmes, often reducing completion. Abstract only; no pooled effect size recorded. It tests a closed loop as part of a package, not the loop alone. The [Mastery Learning](mastery-learning.md) principle holds this relationship.
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]: support adjusted to each response beat fixed, partly contingent or no support for fourth and fifth graders in one-to-one long-division tutoring (8 per condition), at immediate and one-month tests; interactive tutoring of eighth graders matched explanatory tutoring at once and was better on transfer; explicit strategy training outranked scaffolding in a dynamic-assessment meta-analysis. It supports changing the next action from the observed response; it does not show classroom-scale effects, and the claim notes that contingency is scarce in whole-class teaching.
- [Self-regulated learning models treat self-monitoring as a core process through which learners notice gaps and adjust strategy](../claims/self-monitoring-improves-self-regulation.md) [+M]: a review (Zimmerman 2002) and a theoretical synthesis (Butler & Winne 1995) argue that feedback works through the learner comparing their performance with a goal and updating tactics. It supports handing the loop to the learner; it reports no effect sizes and no comparison.
- [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [~S]: a narrative review and one experiment report that confidently held errors, once corrected, are better remembered. It supports correcting and revisiting confident errors; the evidence is about recall, and the claim's discussion says it depends on clear corrective feedback.
- [Peer Feedback Improves Writing](../claims/peer-feedback-improves-writing.md) [+M]: a meta-analysis of 24 higher-education studies found structured peer feedback improved later writing against no feedback (g = 0.91) and against self-assessment only (g = 0.33); the comparison with teacher feedback (g = 0.46) had an interval crossing zero. It supports draft–feedback–revision loops run by peers; it does not separate giving from receiving feedback or test the revision step.
- [Praise for intelligence, rather than for effort, after success undermines children's motivation and performance after a later failure](../claims/feedback-praise-reduces-learning.md) [-M]: fifth graders praised for intelligence after success preferred performance goals and did worse after a later failure than those praised for effort; a review finds person praise can undermine motivation, moderated by age and gender. It limits what the information in a loop should contain.
- [Higher compliance with MetaTutor's revise-summary prompt is associated with larger proportional learning gains](../claims/revise-summary-compliance-predicts-learning-gains.md) [~M]: in 28 college students using one tutoring system, compliance with a prompt to revise a summary was associated with larger proportional gains (ηp² = .15). `associational`: learners who comply may differ in other ways. It is the closest the wiki comes to evidence that using the information, not receiving it, carries the gain.
- [Enacted Feedback yields higher workflow-specific uptake of AI-generated feedback than Directed and Self-Directed Feedback workflows](../claims/enacted-feedback-higher-uptake-than-directed-self-directed.md) [+M]: log data on 51,296 resources across three workflows for AI-generated feedback; the workflow in which students selected, prioritised and discussed the feedback had higher model-estimated uptake (26.2%) than directed (14.1%) and self-directed (0.1%) workflows (Enacted vs Directed OR = 2.16). It bears on step 4 (making use of the information part of the task); uptake is defined per workflow and no later performance is reported.
- [In one study, feedback quality significantly predicts revised essay quality under teacher feedback but not under either GenAI feedback condition, though the conditions are not compared directly](../claims/feedback-quality-predicts-revision-only-in-teacher-condition.md) [~M]: in one essay-revision study with about two dozen students per condition, teacher feedback quality predicted revised-draft quality (β = .53), while the quality of zero-shot or chain-of-thought AI feedback did not. The comparison is between regressions within conditions, not a test of the difference. It qualifies who should run the loop: a better message from an AI tool did not show up in the revision.
- [Mastery-learning teachers' loop time](../claims/training-increases-feedback-corrective-loop-time.md) [+M]: classroom observation of 21 trained and 19 control secondary mathematics teachers; trained teachers gave about 20 percent of class time to the feedback-corrective loop, from virtually none. Time allocation only, no learner outcome; used as a planning figure in step 8 and the classroom row.
- [Probing feedback with required revise-and-resubmit](../claims/probing-feedback-revise-resubmit-evidence.md) [+W]: one qualitative case analysis of teacher candidates' weekly submissions, no comparison; one candidate moved towards citing evidence, non-linearly, another did not improve. It illustrates step 4 and the work-settings row.
- [Rubrics changed what online peer reviewers commented on](../claims/rubrics-improve-peer-feedback-quality.md) [~M]: two quasi-experiments; a rubric changed the content of peer comments (and in one study restrained reflective comments) and helped MOOC peers rate complex criteria, not simple ones. Neither tests whether the receiver's next draft improved.
- [Corrective feedback on second-language errors has a significant effect on L2 development that is maintained on delayed tests](../claims/corrective-feedback-effect-on-l2-development-is-significant-and-durable.md) [+S]: two meta-analyses; 15 classroom studies (N = 827) gave d = 0.74 against controls, with no significant decline from immediate to delayed posttests; prompts did better than recasts; the syntheses disagree on treatment length and setting. It is the one body of evidence here with a delayed outcome of correction in the exchange itself, though not of a closed loop against an open one.
- [Intelligent tutoring systems improve achievement over non-individualised instruction](../claims/adaptive-learning-improves-outcomes.md) [+S]: two meta-analyses of intelligent tutoring, system-run loops that model the learner's state; tutoring systems beat large-group instruction (g = 0.42) and textbooks, but not one-to-one human tutoring or small groups, and gains depended on whether tests were locally developed. It supports the self-paced row as a package.
- [Providing feedback after initial multiple-choice tests cut lure intrusions roughly in half](../claims/feedback-after-multiple-choice-tests-halves-lure-intrusions.md) [+M]: a review chapter reports feedback cutting lure intrusions from about 20% to about 10%, immediate and delayed feedback equally. Second-hand; it bears on delayed marking, held on [Immediate Feedback](immediate-feedback.md).
- [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M]: a narrative review and experiments on guidance formats (integrated text, worked examples), not on feedback; carried to the advanced-learner row with no crossover point.
- [Feedback makes behaviour seen in asynchronous online learning](../claims/feedback-makes-behaviour-seen-asynchronous.md) [+W]: the authors' argument from one course audit that feedback on outputs is what makes a remote learner's work visible. It supports step 2's observable output, not an effect.
- [A practitioner brief, citing Heritage (2009), reports that teachers who can identify a stage of student learning cannot necessarily identify the next instructional steps](../claims/noticing-not-enough-next-steps.md) [~W]: one practitioner brief reporting earlier research second-hand. It qualifies step 10: the instructor's loop needs planned next moves, not only a reading of where learners are.

Learners, tasks, settings and outcomes differ across these claims, so do not rank them by effect size. None measures `delayed-retention` of a closed loop against an open one.

## The evidence by question

- *What should the feedback after a check say, and who or what should give it?* [Feedback improves learning by a medium amount on average, but its effect varies widely with the information it carries, and more than a third of feedback interventions reduce performance](../claims/feedback-improves-learning.md) [+S]
- *Does adjusting instruction to each response help, and what do teachers do with the evidence?* [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- *Does making progress depend on reaching a unit criterion, with correction and a recheck, raise examination performance over conventional pacing?* [Mastery Learning Improves Outcomes](../claims/mastery-learning-improves-outcomes.md) [+M]

## Further evidence, not yet read against this model

Claims this page has read and does not use in the model above, with how far each bears on it.

- [In the Learner Variability Navigator case, feedback loops across multiple partners generated an output of need](../claims/lvn-generator-feedback-loop-case.md) [+W]: read; a design case about feedback loops between organisations in product development, a different sense of "feedback loop"; it does not bear on learners' loops. The principle [Prefer feedback loops over one-directional feedback systems](feedback-loops.md) holds that sense.
- [In the Maker Learning @ Home cohort, feedback loops with cohort members redefined the initiative's outputs and goals](../claims/maker-cohort-amplifier-case.md) [+W]

## Objective and learner-valued goal

The designer's objective is usually unaided performance on new items of the target kind, at a stated horizon, and, later, the learner's ability to run the loop themselves. Elicit separately what the learner wants from the feedback: a mark, reassurance, to finish, or to get better at something they care about. These diverge often in loops. A learner who values the mark may revise only what was pointed out; one who values not looking wrong may avoid the retry, or the confidence question. Agreement and divergence are both observations, and they change how the information should be framed and who should see it.

For example, a nurse in clinical onboarding may want to stop being corrected in front of patients, while the designer's objective is accurate medication calculations under time pressure. A loop that corrects calculations on paper in private, with a matched retry and a supervisor's check on the next real calculation, serves both; the same corrections given on the ward serve the objective and work against the learner's goal. Record both, so that a learner's avoidance of retries is not read as a lack of competence.

## What would revise this model?

The expectation should weaken if comparisons of the same feedback with and without a required next attempt, in comparable learners on aligned new items, show no advantage, or show that the advantage at the end of the session disappears at a delay. If learners given high-information feedback improve as much without a re-observation step as with one, the recheck is a measurement convenience, not part of the mechanism, and the page should say so. If learner-run loops (self-checking against criteria) never match instructor-run loops for learners at a given stage, the hand-over should be later or dropped for them. If one teacher cannot run closed loops with a whole class however the time is budgeted, the model is a one-to-one or software design and should be stated that way. Do not protect the model by calling every null result "the loop was not really closed" after the fact.

Following the information on the corrected item, unaided performance on a new item, delayed retention, and the learner's own monitoring are separate outcomes. The present evidence establishes no number of cycles, no cycle length and no hand-over criterion.

## Claims

- [A design-based study with 42 undergraduates reported a 15% improvement in rubric alignment and faster correction cycles from proactive agentic feedback loops](../claims/agentic-feedback-42-undergrads-rubric-alignment-gain.md) [+W]
- [In the MM-04 workflow case, similar-looking model activity has different evidential validity: GPT-5.5 closes the evidence-to-action loop while GLM-5.1 leaves the assigned deck unchanged and Gemini-3.1-Pro misses required numeric or visual evidence](../claims/mm04-workflow-boundary-failures.md) [~W]
- [Districts use multiple forms of data—learning walks, state assessment items, dashboards, and diagnostics—to give teachers feedback and refine IM implementation over time](../claims/data-use-supports-ongoing-hqim-implementation.md) [~W]
- [Originality is almost never invoked in builders' spoken acceptance verdicts, and defects as well as defaults exit the loop by acceptance without verification](../claims/shallow-acceptance-originality-rarely-invoked.md) [-W]
- [Attempt-reduction patterns differed across course parts: Diagnostic and General Feedback were associated with fewer attempts for New Content, Single-Issue for Old Content](../claims/attempt-reduction-varies-by-course-part.md) [~W]
- [Valid test case feedback improves correctness without reducing subsequent submission counts](../claims/valid-test-cases-not-fewer-submissions.md) [+W]
- [Students reported recognizing writing improvements after revising in response to AI feedback, with observed rubric-score gains on resubmission](../claims/students-recognize-writing-improvement-ai-feedback.md) [+W]
- [Dl2F Dynamic Language Learning Framework](../theories/dl2f-dynamic-language-learning-framework.md) [+M]
- [In water-jug problems, presenting information about available moves and their consequences did not enhance planning, though looping moves reliably decreased](../claims/move-availability-information-did-not-enhance-water-jug-planning.md) [~W]

## Related Principles
- [Immediate Feedback](immediate-feedback.md)
- [Formative Assessment](formative-assessment.md)
- [Check-ins](check-ins.md)
- [Goal Setting & Monitoring](goal-setting-monitoring.md)
- [Assessment for Learning](assessment-for-learning.md) — shared criteria and the stakes that keep loop evidence honest
- [Mastery Learning](mastery-learning.md) — the criterion-gated correct-and-recheck loop between units
- [Self-Regulated Learning](self-regulated-learning.md) — the learner-run loop this page hands over to
- [Peer Feedback](peer-learning.md) — peers as the source of information in a loop

## Examples

- Learners solve a problem, see an explanation for the mistake, and retry immediately.
- An instructor uses an exit ticket to adjust the next day's grouping or re-teaching.
- A writing conference identifies one revision target that the learner applies in the next draft.
- The [feedback element](../elements/feedback.md) and the [formative assessment pattern](../patterns/formative-assessment.md) and [mastery learning pattern](../patterns/mastery-learning.md) carry loops as reusable components and policies.
- [Self-assessment as a formative assessment practice that supports students to act as self-regulated agents](../strategies/self-assessment-supports-self-regulated-agents.md)
- [Identify feedback loops in your organization by sourcing, evaluating, and validating case studies](../strategies/identify-feedback-loops-process.md)

## Key Sources
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81-112. [https://doi.org/10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Clark, I. (2012). Formative assessment: Assessment is for self-regulated learning. *Educational Psychology Review, 24*(2), 205-249. [https://doi.org/10.1007/s10648-011-9191-6](https://doi.org/10.1007/s10648-011-9191-6)
- Pollard, V., Armatas, C., & Pepe, A. (2025). Feedback is integral: Using a revised ICAP Framework to achieve active learning in an asynchronous online course. Online Learning, 29(3), 236-253. https://doi.org/10.24059/olj.v29i3.4555
- Baker, A., Weisgrau, J., & Bristal Philyaw, K. (2022, May). Feedback loops: Mapping transformative interactions in education innovation. Digital Promise. https://doi.org/10.51388/20.500.12265/155
- Merueña, J. A. A. (2023). Dynamic Language Learning Framework (DL2F) Instructional Model. EPRA International Journal of Research and Development (IJRD). https://doi.org/10.36713/epra2016

<!-- deprecated 2026-10-05: superseded by the conditional model above. The previous body, kept verbatim.
## Description
Feedback loops are the principle of using learner performance to generate information that changes the next action for the learner, the instructor, or the system. A loop is only complete when evidence leads to adjustment. The key design move is not merely telling learners how they did, but ensuring that the feedback, interpretation, and next attempt are connected closely enough to improve performance.

## Implications
Feedback loops matter because information about performance is useful only when it changes what happens next. Timely, interpretable feedback can improve self-monitoring [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [+M], guide strategy adjustment through responsive support [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M], and prevent errors from hardening, especially when confident mistakes are corrected while the task is still live [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [~S]. That means a good loop includes not just a signal, but a path for response: retrying, revising, regrouping, or changing support. Without that response phase, feedback remains commentary rather than instruction.

### Context
#### Requirements
- **Observable performance**: There must be something interpretable to respond to.
- **Actionable information**: Feedback needs to suggest what to correct, continue, or try next.
- **Opportunity to respond**: Learners need a chance to revise, retry, or adapt strategy.
- **Interpretation support**: Learners and instructors need criteria for making sense of the result.
#### Constraints
- **Delayed loops**: Long lag between action and response weakens learning value.
- **Signal overload**: Too many feedback messages can fragment attention.
- **Low-quality signals**: Scores without explanation often do not change performance.
- **Overdependence**: Constant external correction can reduce learner judgment if self-monitoring never develops.

### Target Learners
- **Novice learners**: Benefit from quick correction and guidance while building foundational routines.
- **Learners developing self-regulation**: Strong fit when the goal is to compare current performance against goals and adjust.
- **Learners practicing cumulative skills**: Repeated loops support incremental refinement.

### Target Learning Objectives
- **Strategy adjustment**: Improving what learners do on the next attempt.
- **Error correction**: Preventing misconceptions from stabilizing.
- **Metacognitive monitoring**: Helping learners notice progress and remaining gaps.

### Theory
#### Supporting
- Self-regulated learning emphasizes feedback as input for monitoring and strategy change.
- Cybernetic and formative assessment traditions both treat learning as adjustment based on evidence.
#### Contradicting / Qualifying
- Not every task benefits from step-level interruption; some work requires uninterrupted flow before review.
- Fast loops are helpful only when the feedback is aligned and interpretable.

### Claims

- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [+M] — feedback loops help learners notice the gap between current performance and the target
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M] — loops are instructionally valuable when they trigger adaptive changes in support or strategy
- [High-confidence errors lead to better retention after correction than low-confidence errors.](../claims/high-confidence-errors-improve-retention.md) [~S] — timely correction inside a loop can make important errors more memorable and less likely to recur

## Related Principles
- [Immediate Feedback](immediate-feedback.md)
- [Formative Assessment](formative-assessment.md)
- [Check-ins](check-ins.md)
- [Goal Setting & Monitoring](goal-setting-monitoring.md)

## Examples
- Learners solve a problem, see an explanation for the mistake, and retry immediately.
- An instructor uses an exit ticket to adjust the next day's grouping or re-teaching.
- A writing conference identifies one revision target that the learner applies in the next draft.

## Key Sources
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81-112. [https://doi.org/10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Clark, I. (2012). Formative assessment: Assessment is for self-regulated learning. *Educational Psychology Review, 24*(2), 205-249. [https://doi.org/10.1007/s10648-011-9191-6](https://doi.org/10.1007/s10648-011-9191-6)
-->

<!-- merged 2026-10-07 from principles/design-feedback-on-external-outputs-asynchronous ("Design asynchronous online activities so that external outputs receive formative feedback, enabling higher ICAP modes"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Design asynchronous online activities so that external outputs receive formative feedback, enabling higher ICAP modes

> **Principle** · [All principles](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article recommends explicitly designing task-based formative feedback into asynchronous online learning activities so that student-produced external outputs are used to move thinking to higher engagement modes. The audit found "Limited opportunities for feedback on external outputs was also identified as an area requiring attention to produce higher modes of activity and feedback." Simulations and multimedia assets producing reviewable external outputs used in assessments exemplify this design.

## Design Implications

### Context
#### Requirements
- Activities must produce an external output on which peers, the teacher, or another party can provide feedback
- Feedback must be incorporated into a further output for the Interactive mode (double-loop learning)
#### Constraints
- The article notes a place remains for simpler activities such as click and reveals, provided there is a coherent whole-of-course approach to variety and higher modes

### Target Learners
- post-graduate online students

### Target Learning Objectives
- active learning
- higher-order engagement
- use of feedback

### Claims
- [Feedback Makes Behaviour Seen Asynchronous](../claims/feedback-makes-behaviour-seen-asynchronous.md) [+W]
- Audit Most Activities Passive Active Icap [+M]

## Related Principles
- 

## Examples
-

## Key Sources
- Pollard, V., Armatas, C., & Pepe, A. (2025). Feedback is integral: Using a revised ICAP Framework to achieve active learning in an asynchronous online course. Online Learning, 29(3), 236-253. https://doi.org/10.24059/olj.v29i3.4555
-->

<!-- merged 2026-10-15 from principles/prefer-feedback-loops-over-feedback-systems ("Prefer feedback loops over one-directional feedback systems when direct benefits for all participants matter"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Prefer feedback loops over one-directional feedback systems when direct benefits for all participants matter

> **Principle** · [All principles](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 design), `q1` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
The report argues that while simple feedback systems such as surveys are valuable and can lead to significant increases in the impact of a product, feedback loops as conceived here result in not only improvement in outputs, but create direct benefits for all participants. Organizations should therefore assess whether a scenario calls for mere sentiment-gathering or for a bidirectional, iterative, transformative interaction, and reserve feedback loops for cases where mutual transformation and partnership-building are the goal.

## Design Implications

### Context
#### Requirements
- Willingness to invest in iterative, multi-round engagement rather than a single collection point
#### Constraints
- Not every scenario or goal requires a feedback loop; simple feedback systems remain valuable approaches for establishing sentiment about a product or process

### Target Learners
- School districts, education nonprofits, and research-practice partnerships

### Target Learning Objectives
- Designing stakeholder engagement that builds partnership and belonging while improving outputs

### Claims

- [Lvn Generator Feedback Loop Case](../claims/lvn-generator-feedback-loop-case.md) [+W]
- [In the Maker Learning @ Home cohort, feedback loops with cohort members redefined the initiative's outputs and goals](../claims/maker-cohort-amplifier-case.md) [+W]

## Related Principles
- 

## Examples

- [Identify feedback loops in your organization by sourcing, evaluating, and validating case studies](../strategies/identify-feedback-loops-process.md)

## Key Sources
- Baker, A., Weisgrau, J., & Bristal Philyaw, K. (2022, May). Feedback loops: Mapping transformative interactions in education innovation. Digital Promise. https://doi.org/10.51388/20.500.12265/155
-->

<!-- merged 2026-10-15 from principles/dl2f-continuous-improvement-principle ("Build continuous improvement into language instruction through regular feedback, self-assessment, and revision opportunities"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Build continuous improvement into language instruction through regular feedback, self-assessment, and revision opportunities

> **Principle** · [All principles](index.md)
> **Evidence** · 1 claim (1 for) · 2 studies (1 review, 1 theoretical), `q3` · 0 of 2 report an effect size

## Description
DL2F treats language proficiency as an ongoing journey rather than a fixed destination by embedding continuous learning mechanisms into instruction. The article states the framework 'incorporat[es] regular feedback, self-assessment, and opportunities for revision to foster a growth mindset among learners', supported by reflection and discussion sessions and continuous monitoring with adjustments based on student feedback.

## Design Implications

### Context
#### Requirements
- Regular feedback mechanisms
- reflection and discussion sessions
- ongoing monitoring and adaptation based on student feedback
#### Constraints
- 

### Target Learners
- language learners in student-centered programs

### Target Learning Objectives
- growth mindset
- ongoing language proficiency development
- self-assessment skills

### Claims

- [Dl2F Dynamic Language Learning Framework](../theories/dl2f-dynamic-language-learning-framework.md) [+M]
- [Self-regulated learning models treat self-monitoring as a core process through which learners notice gaps and adjust strategy](../claims/self-monitoring-improves-self-regulation.md) [+M]

## Related Principles
- 

## Examples
-

## Key Sources
- Merueña, J. A. A. (2023). Dynamic Language Learning Framework (DL2F) Instructional Model. EPRA International Journal of Research and Development (IJRD). https://doi.org/10.36713/epra2016
-->
