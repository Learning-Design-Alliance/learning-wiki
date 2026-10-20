---
type: pattern
id: problem-based-learning
aliases: [problem-based-learning-pbl, maastricht-seven-step-pbl-tutorial-cycle]
title: Problem-Based Learning
description: "A reusable policy for problem-centred units: establish what learners already know of the target content, guide novices explicitly, use a problem-first phase only where learners can generate partial solutions and instruction follows, and judge the unit on individual outcomes."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
sources:
  - id: hmelo-silver-2004
    resource: "https://doi.org/10.1023/B:EDPR.0000034022.16470.f3"
    title: "Hmelo-Silver, C. E. (2004). Problem-based learning: What and how do students learn? *Educational Psychology Review, 16*(3), 235-266"
    author: Hmelo-Silver, C. E
  - id: savery-2006
    resource: "https://doi.org/10.7771/1541-5015.1002"
    title: "Savery, J. R. (2006). Overview of problem-based learning: Definitions and distinctions. *Interdisciplinary Journal of Problem-Based Learning, 1*(1), 9-20"
    author: Savery, J. R
  - id: murray-harvey-2013
    resource: "https://eric.ed.gov/?id=EJ1108330"
    title: "Murray-Harvey, R., Pourshafie, T., & Santos Reyes, W. (2013). What teacher education students learn about collaboration from problem-based learning. Journal of Problem Based Learning in Higher Education, 1(1), 114-134. https://eric.ed.gov/?id=EJ1108330"
    author: "Murray-Harvey, R., Pourshafie, T., & Santos Reyes, W"
author: PBL tradition
grain_size: unit
---

# Problem-Based Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 58 claims (15 for, 39 mixed, 4 against) · 45 studies (15 causal, 8 review, 7 theoretical, 5 quant-synthesis, 5 qualitative, 3 design, 2 associational), `q1`–`q4` · 7 of 45 report an effect size · 53 claims rest on one study

## Description and scope

A reusable policy for organizing a unit around a problem that learners must investigate, deciding how much guidance to give and when, and reading what learners do with the problem. It instantiates the [conditional principle](../principles/problem-based-learning.md). The study configurations below are evidence; the response-dependent policy is an **untested design proposal**. Use it to gather better evidence about a learner group, not to certify that a learner is "ready for open problems".

The pattern is general across domains. A course for a particular setting (a medical curriculum, a primary science unit) is a design that may use it; the longer description of the tradition, from the former `problem-based-learning-pbl` page, is kept in the merged block at the end of this page.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Age band and task-specific starting knowledge (`novice`, `intermediate`, `advanced`, or `?`); a brief independent attempt at framing the problem or a comparable one; what the learner says they would need to know. Preserve unknowns. |
| Context and activities | Setting (`classroom`, `online-instructor-led`, `workplace-clinical`, ...), duration, group size and roles, available resources, who facilitates, and exactly what guidance, instruction and feedback are planned and when. |
| Learner-valued goal | Ask what the learner wants from working on this problem and why. Record disagreement with the designer objective; negotiate rather than assume agreement. |
| Designer objective | The concept, principle or complex skill the problem is meant to carry (`principle`, `complex-skill`, ...), and whether a correct solution to the problem as posed actually requires it. |
| Outcome | Separate instruments for conceptual understanding, transfer, procedural fluency and product quality; individual as well as group measures; immediate and delayed horizons. |

A request for "more engaging, real-world learning" does not specify these inputs. Ask for them before choosing a problem, a guidance level or a predicted gain. Check first that the problem, the resources and any model solution are correct and that the target concept is needed to solve it.

## Sequence and conditional policy

1. **Elicit briefly.** Present the problem and ask each learner (not only the group) for a first framing: what is the question, what do they already know, what do they need to learn. Keep this short; record it as a learning exposure.
2. **Choose the guidance level provisionally.** Default for task-specific novices on the target content: make the content explicit (a short explanation, a worked or modelled example, a short text read before the group discusses the problem, resources that carry it) before or alongside the problem, and use the problem to apply and connect it. A problem-first phase is a narrower candidate, for learners who can generate several partial solutions from what they already know and make real headway on the problem (pilot it), in mathematics and science rather than other domains where it has not replicated, always followed by consolidating instruction. Do not adopt PBL on its label: the average curriculum-level effect is small and varies widely, so the configuration decides.
3. **Run the problem phase with contingent facilitation.** Increase support when a learner or group is stuck, reduce it when they progress; record each intervention. Ask learners to make their solutions visible, including flawed ones.
4. **Consolidate.** Teach the canonical idea explicitly, building on and contrasting with the solutions learners produced. Do not treat the consolidation as optional: the problem-first evidence concerns problem solving *followed by* instruction.
5. **Reobserve individually.** Use a new problem or a changed condition, scored separately for concept, transfer and procedure, at the agreed horizon. If the response disagrees with the expectation, revise the interpretation or the configuration.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Learners cannot frame the problem or list learning issues | Re-present the problem in a familiar representation or with a model of a finished product; ask for a first decision only. | If a familiar framing releases a start, the barrier may be access or representation: adjust the problem. If not, supply the missing content explicitly before continuing: in one experiment, students without relevant prior knowledge who elaborated in a problem-based discussion recalled less than those who did not, immediately and after a delay. Neither branch is a validated diagnosis. |
| Group is active, but solutions do not use the target concept | Ask what idea the solution depends on; check whether the problem as written requires the concept. | If the concept is not required, revise the problem. If it is required and absent, move consolidation earlier or add a targeted resource. Activity alone does not show learning. In one design experiment, [a student asked twelve times in 53 minutes what the group's work meant in disciplinary terms and nobody answered adequately](../claims/twelve-unanswered-conceptual-questions.md) [+W]: a repeated conceptual question is a cue for the facilitator to explain, not to wait. |
| Discussion is all explanation-building, little checking against the problem's data | Ask which facts in the problem the group's explanation does not yet account for; ask each member privately what they are unsure of. | Prompt data exploration and reflection on the group's reasoning. In one tutorial group, [discussion during problem analysis was mainly theory building, with less data exploration and meta-reasoning](../claims/pbl-discussion-mainly-theory-building.md) [~W], and stimulated recall showed that [the talk revealed only part of members' thinking](../claims/pbl-verbal-interaction-tip-of-iceberg.md) [~W]: a quiet member may be reasoning, and a fluent group may be hiding gaps. Both from one qualitative study; the prompt is an untested proposal. |
| Several varied, partly wrong solutions generated | Ask learners to compare two of their solutions and say what each assumes. | Proceed to consolidating instruction that contrasts these solutions with the canonical one. The claim page places the effect mostly in well-structured domains such as mathematics, and its synthesis reports a reversal for second to fifth graders. |
| Strong group product, weak individual explanation | Individual explanation or changed-condition task, matched in demand; ask each member to describe in writing how the group negotiated and built its solution. | Add individual accountability and individual practice; record who contributed what. Do not read the group score as each member's. In one qualitative study of teacher education students, only about half of their written accounts of PBL group work showed co-regulation and co-construction rather than divided group work. |
| Conceptual probe passed, routine procedure failed | Score procedure separately under the same conditions. | Add targeted procedural practice; the problem-first evidence records no procedural advantage, so this is expected rather than a failure of the policy. |

## Choosing configurations from evidence

- **Whether to expect anything from the PBL label.** [The overall effect in a 353-outcome re-analysis is modest (g = 0.27)](../claims/pbl-overall-effect-modest-large-heterogeneity.md) [~M], [ranges from g = −1.26 to 1.91](../claims/massive-range-pbl-outcome-effect-sizes.md) [~M] and may be inflated by publication bias (g = 0.103 after trim-and-fill) [~M]. Plan and evaluate the specific configuration; do not promise a gain from the format. An essay citing an older review reports [equivocal results on knowledge acquisition and clinical reasoning, attributed to how faithfully programmes implement PBL](../claims/pbl-evidence-base-equivocal.md) [~W] (second-hand; the review itself is not read on the claim page), and a meta-synthesis of meta-analyses reports [PBL ahead of conventional instruction on skill development and on student and teacher satisfaction](../claims/pbl-superior-skill-development-satisfaction.md) [+W] (no effect sizes in the text available). Both point the same way: which outcome, and which implementation, decide the result.
- **Who facilitates.** [Tutor background did not predict learning](../claims/tutor-background-meta-regression-not-predictive.md) [~M] in the same data. In a field experiment across 98 health-sciences PBL courses, [staff-tutored groups scored slightly higher than peer-tutored groups](../claims/staff-tutoring-small-achievement-advantage-pbl.md) [~M] (6.79 against 6.64 on a ten-point scale): a real but small difference, so peer tutors are a workable option where staff are scarce, provided they get the preparation below. Prepare facilitators in the guidance and consolidation moves below rather than relying on content expertise or its absence; whether facilitation training itself changes outcomes is not recorded in the wiki.
- **Amount of guidance.** For novices, [unassisted discovery underperforms explicit instruction, while enhanced discovery outperforms other instruction](../claims/minimal-guidance-less-effective-for-novices.md) [-S]. This rules out a configuration in which essential content is left for novices to find unsupported; it does not rule out guided problem work. The meta-analysis is not broken down by prior knowledge on the claim page.
- **Prior knowledge before a problem-based discussion.** In one randomized 2×2 experiment (66 students), [elaboration during a problem-based discussion interacted with relevant prior knowledge on immediate recall](../claims/elaboration-prior-knowledge-interaction-immediate-recall.md) [~M] (η² = .06, p = .06), and [students without relevant prior knowledge who elaborated recalled less than those who did not](../claims/elaboration-without-prior-knowledge-harms-recall.md) [-M], on the immediate and the delayed test. This is the most direct evidence in the wiki for the default at step 2: give learners some relevant prior knowledge (a short text, a pre-reading) before they discuss the problem. It is one study, measuring text recall rather than transfer. An earlier randomized trial with first-year medical students points the same way for a relevant problem: [discussing it before studying a text raised accurate recall of both explanatory and descriptive content](../claims/pbl-recall-benefit-general-not-explanation-specific.md) [+M], [without changing the number of inaccurate propositions](../claims/pbl-discussion-no-change-in-inaccurate-recall.md) [~W], but [did not increase the inferences learners made in recall](../claims/pbl-discussion-no-increase-in-immediate-inferences.md) [~W]. So the evidence in the wiki supports problem discussion as preparation for reading, measured as memory for the text, not as a source of deeper inference. In an example-and-problem sequencing study, [pre-test knowledge strongly predicted application and transfer scores whatever the order](../claims/pretest-predicts-inquiry-outcomes.md) [~W]: measure prior knowledge at step 1 and read any outcome against it.
- **Who sets the learning issues.** In an experiment reviewed by Loyens et al., [groups who generated their own learning issues studied more materials and spent more time on self-study and reporting](../claims/self-generated-learning-issues-benefit-pbl.md) [+W] than groups handed the issues with the same problem. That supports step 1's "what do they need to learn" coming from learners; the review prints no achievement outcome, so it is evidence about study behaviour, not learning.
- **Whole problems or parts first.** [A training-design argument holds that practising whole complex tasks favours transfer](../claims/whole-task-performance-improves-transfer.md) [+W], which is the rationale for a whole problem; no study comparing whole-task with part-task practice is recorded on that claim. For learners with very little prior knowledge facing a task with many interacting elements, [presenting isolated parts before the integrated task helped](../claims/part-task-practice-reduces-load-for-novices.md) [~M] in one experiment. So for absolute novices on a complex problem, isolate the key parts first and then return to the whole problem.
- **Order of problem and instruction.** For conceptual and transfer outcomes, [a problem-first phase followed by instruction](../claims/productive-failure-improves-conceptual-learning.md) [~S] has meta-analytic support over the same instruction taught first, with no procedural difference and a reversal for second to fifth graders and for domain-general skills. A randomized experiment with ninth-graders learning standard deviation, reported in Kapur (2016), found the same pattern (better conceptual understanding and transfer, no procedural difference) when students generated solutions individually, and [the small-group version with ninth-graders learning variance](../claims/pf-outperformed-di-variance-conceptual-transfer.md) [+W] reported the same. Choose it only with a consolidation phase, for learners old enough, and judge it on conceptual and transfer measures. The claim page reports no delayed-horizon breakdown. Two qualifications: across studies, [PS-I benefits appeared where most learners solved the initial problems (80–90%) and not where few did (14–28%)](../claims/solution-rate-moderates-ps-i-benefits.md) [~W] (a cross-study comparison in a theoretical paper), so learners need enough knowledge to make real headway, not merely to fail; and in social-science research methods, [problem-first did not outperform instruction-first in two quasi-experiments with tenth-graders](../claims/pf-effect-not-replicated-non-stem-research-methods.md) [-M], even though [pilot tests had shown the problem drew several solution ideas containing the targeted errors](../claims/pf-problem-sweet-spot-complexity-pilot-tests.md) [~W]. A problem pitched at the right complexity is necessary and was not sufficient there. A secondary account holds that [groups given harder, ill-structured problems solved fewer but did better on later problems](../claims/productive-failure-deeper-learning-lower-posttests.md) [~W]; it is reported second-hand in an editorial, and it is a reason to judge the phase on a later problem (step 5) rather than on the problem phase itself.
- **Facilitation.** [Contingent scaffolding](../claims/contingent-scaffolding-improves-learning.md) [+M] (support raised after failure, lowered after success) outperformed fixed or absent support in small one-to-one tutoring studies, with better transfer in one. It is a candidate rule for a facilitator, not a tested result in PBL groups.
- **Case-based formats.** [Case-based learning](../claims/case-based-learning-improves-exam-performance.md) [~M] raised exam scores in one non-randomized biology cohort, while a systematic review in health professional education found the evidence on learning inconclusive and noted that gains may come from group work. Do not expect a case or problem format alone to carry the effect.
- **Lectures alongside the problem sessions.** In a qualitative comparison across curricula, [where more content was covered in lectures, students in PBL sessions repeated lecture facts rather than questioning or challenging, though the prior knowledge made them less afraid to speak](../claims/scope-of-pbl-implementation-shapes-discussion.md) [~W]. This is the cost side of step 2's default: content given first eases participation and can close down the discussion. Pose a problem the lectured content informs but does not answer.

Do not rank these results against one another: their comparators (instruction-first, explicit instruction, fixed support, lecture and reading) and outcomes differ. A precise abstention names the missing comparison, outcome or observation and the next way to resolve it.

## Fitting the design to a situation

Ask for four facts when the brief omits them: **can learners generate partial solutions to the problem from what they already know?**, **how much time is there (one session or several)?**, **who facilitates, and how many groups each?**, and **which outcomes will be assessed (knowledge, procedure, transfer)?**

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are novices on the content the problem needs | At step 2, teach the content first or alongside (short explanation, worked example, a short text to read before the group discusses the problem) and use the problem to apply it | [Minimal guidance is less effective for novices](../claims/minimal-guidance-less-effective-for-novices.md) [-M]; [Elaborating without relevant prior knowledge lowered recall](../claims/elaboration-without-prior-knowledge-harms-recall.md) [-M] (one experiment, university students) |
| Learners are absolute novices and the problem has many interacting parts | Before the whole problem, give short practice on its key parts in isolation, then pose the integrated problem | [Part-task practice helped absolute novices on high-interactivity material](../claims/part-task-practice-reduces-load-for-novices.md) [~M] (one experiment, not in PBL) |
| Learners can generate several partial solutions and the goal is conceptual | Run a short problem-first phase, have groups make their solutions visible, then build step 4's instruction on those solutions. Pilot the problem first: check that learners produce several ideas and make headway on it; if few get anywhere, teach first | [Problem-first improves conceptual learning when instruction follows](../claims/productive-failure-improves-conceptual-learning.md) [+M]; [Larger effects when instruction builds on student solutions](../claims/pf-fidelity-predicts-psi-effect-size.md) [+M]; [PS-I benefits appeared with high, not low, initial solution rates](../claims/solution-rate-moderates-ps-i-benefits.md) [~W] (cross-study comparison) |
| The domain is outside mathematics and science (for example, social-science methods) | Treat problem-first as unproven there; prefer instruction first with the problem as application, or run problem-first as a comparison and measure it | [Problem-first did not outperform instruction-first for social-science research methods](../claims/pf-effect-not-replicated-non-stem-research-methods.md) [-M] (two quasi-experiments, tenth-graders), despite [a piloted problem of suitable complexity](../claims/pf-problem-sweet-spot-complexity-pilot-tests.md) [~W] |
| The facilitator wants to hint learners toward the method during the problem phase | Do not steer toward the canonical method before step 4; guidance raised solution quality but not later learning | [Guidance during initial problem solving does not improve learning from instruction](../claims/initial-guidance-does-not-improve-learning-from-instruction.md) [~M] |
| Fluent execution of a procedure is part of the objective | Add targeted procedural practice after the consolidation; problem-first gave no procedural advantage | [PS-I shows no pooled benefit for procedural knowledge](../claims/psi-procedural-knowledge-null-pooled-effect.md) [~M] |
| Learners are roughly 7–11 years old | Reverse the order: teach first, then pose the problem as application | [PS-I effects are negative for 2nd–5th graders](../claims/psi-effect-increases-with-grade-level.md) [-M] |
| Only one short session is available | Keep the problem phase short and the design simple, or teach first; do not cram the full sequence into a few hours | [The fidelity benefit reverses for very short interventions](../claims/psi-fidelity-time-span-interaction.md) [~M] |
| The assessment is a basic-knowledge exam | Add explicit review and practice of the facts the exam covers; do not count on the problem work to carry them | [PBL: null or negative on basic knowledge](../claims/pbl-null-basic-knowledge-positive-transfer.md) [~M] |
| Facilitators are not content experts | Give each facilitator the model solution, the target concept and a consolidation script; content background alone did not predict learning. Where facilitators are peers (senior students), give them the same materials and expect at most a small shortfall | [Tutor background did not predict learning](../claims/tutor-background-meta-regression-not-predictive.md) [~M]; [Staff-tutored groups scored slightly higher than peer-tutored groups](../claims/staff-tutoring-small-achievement-advantage-pbl.md) [~M] (one field experiment, health sciences) |
| Tutorial groups are large | Split into small or medium groups for the problem work, each with a clear role structure; do not run the self-directed phase as one large group | [Small and medium tutorial groups gained self-directed-learning readiness; large groups declined](../claims/tutorial-group-size-moderates-sdl.md) [~W] (one pre–post study reported in a review; a self-report scale, not achievement) |
| Content is taught in lectures running alongside the problem sessions | Write problems the lectured content informs but does not settle; ask learners for questions and challenges, not a summary of the lecture | [More lecture coverage went with less critical discussion in PBL sessions, but more willingness to speak](../claims/scope-of-pbl-implementation-shapes-discussion.md) [~W] (one qualitative cross-curriculum study) |
| Group work runs online over several weeks | Re-launch the group's script part-way through (new roles, a fresh argument task, a facilitator check-in), since a script that holds at the start does not hold by itself | [Online PBL groups followed the scripted sequence at first, then drifted to social bonding with fewer high-cognitive interactions](../claims/pbl-group-sequence-derails-to-social.md) [~W] (one sequence-analysis study); the re-launch is an untested proposal |
| Learners work alone (`online-self-paced`) | Replace the facilitator with support that rises after a failed attempt (a hint, then a worked step) and falls after success, and show typical solutions before the consolidation; let a learner who has tried reach an explicit answer rather than only further hints | [Contingent scaffolding improves learning](../claims/contingent-scaffolding-improves-learning.md) [+M] (one-to-one tutoring); [Learners using a staged-disclosure feedback agent valued their agency, but about two in five found it too indirect when they needed an explicit answer](../claims/staged-feedback-survey-perceptions.md) [~W] (one self-selected survey); the self-paced version is an untested proposal |
| One facilitator for many groups | Collect solutions from a sample of groups and build the consolidation on the three or four most common | untested proposal |
| Group products will be the main evidence of learning | Add the individual reobservation at step 5 and record who contributed what; a group product does not show what each member can do | [About half of students' written accounts showed collaborative learning rather than divided group work](../claims/half-of-texts-showed-collaborative-learning.md) [~W] (one qualitative study, teacher education); the individual reobservation is an untested proposal |
| Collaboration is itself an objective (for example, future teachers who will run group work) | Name and teach the skills learners themselves identify (interpersonal, problem-solving and group skills such as sharing roles and resolving conflict) and the attitudes (valuing others' perspectives, interdependence); before the first problem, prepare learners for group work (reading, discussing past good and bad group experiences, practising forming and running a team), as in the [prepare-and-assess strategy](../strategies/prepare-and-assess-pbl-process-reflection.md); have learners reflect in writing on how their group worked and assess that reflection; do not expect learners to report gains in higher-level thinking unprompted | [Skills named: interpersonal, problem-solving, group](../claims/pbl-skills-interpersonal-problem-solving-group.md) [+W]; [Attitudes named: valuing others' perspectives, interdependence, learning about self](../claims/pbl-attitudes-valuing-interdependence-self.md) [+W]; [Knowledge described as generation, application, dissemination, plus pedagogical knowledge](../claims/pbl-knowledge-generation-application-dissemination.md) [+W]; [Students rarely described higher-level cognitive or metacognitive gains](../claims/minimal-reference-higher-level-processing-benefits.md) [~W] (all one qualitative study of 122 students; what learners said, not measured gains) |
| The written unit is tightly scripted, and a real event tied to the driving question arises during it | Allow the facilitator to pause the script and let learners take up the event, then return to the target concept in the consolidation | [A teacher's departure from the written PBL sequence to respond to a real event deepened student-directed inquiry](../claims/spontaneous-authenticity-in-pbl-deepens-student-directed-inquiry.md) [+W] (one grade-3 classroom case study; sufficient there, not shown to be general) |
| The brief adds AI tools to the problem phase and expects higher scores | Treat the AI support as part of the configuration to be evaluated; the one comparison recorded set AI-supported PBL against lecture, so it cannot separate the AI from the PBL. If an AI agent withholds answers to preserve learner agency, give it a route to an explicit answer after repeated attempts and check it does not repeat itself | [AI-supported PBL scored higher than lecture in robotics programming](../claims/ai-pbl-higher-posttest-academic-achievement.md) [~W] and [showed higher normalised gains than the control group](../claims/ai-pbl-high-ngain-versus-control-low.md) [~W] (the same quasi-experiment); a systematic review of 50 studies lists as themes that [AI supports educator–student collaboration through real-time feedback and scaffolding](../claims/ai-pbl-enhances-educator-student-collaboration.md) [~W] and [adaptive, personalised learning linked to engagement and problem solving](../claims/ai-pbl-adaptive-personalized-engagement.md) [~W], with no comparisons or effect sizes on the claim pages; [Staged-disclosure feedback agent: agency valued, 39% found it too indirect, 43% reported repetition](../claims/staged-feedback-survey-perceptions.md) [~W] |

## The evidence by question

- *Does PBL as a curriculum format raise achievement over conventional instruction, and how reliably?* [The overall effect of PBL in the tutor-background meta-analysis is modest (g = 0.27) with large, statistically significant heterogeneity](../claims/pbl-overall-effect-modest-large-heterogeneity.md) [~M]
- *Should learners attempt a problem before the idea is taught, and what must the teaching afterwards do?* [Productive Failure Improves Conceptual Learning](../claims/productive-failure-improves-conceptual-learning.md) [~S]
- *Do learners need relevant prior knowledge before they discuss the problem?* [Elaboration interacts with relevant prior knowledge on immediate recall](../claims/elaboration-prior-knowledge-interaction-immediate-recall.md) [~M]
- *Does PBL group work produce collaborative learning, or only divided work?* [About half of students' analysed texts showed co-regulation and co-construction](../claims/half-of-texts-showed-collaborative-learning.md) [~W]
- *For which outcomes: basic knowledge, application and transfer, or professional skills?* [Problem-based learning shows null or negative effects on basic knowledge acquisition but positive effects on conceptual understanding and transfer relative to direct instruction](../claims/pbl-null-basic-knowledge-positive-transfer.md) [~M]; a meta-synthesis adds [skill development and student and teacher satisfaction](../claims/pbl-superior-skill-development-satisfaction.md) [+W]
- *Where is the research on PBL thin?* [A review found considerable research on flexible knowledge, problem solving and self-directed learning, little on collaboration and motivation, and minimal outside medical and gifted education](../claims/pbl-evidence-uneven-across-goals.md) [~W]

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [~M] — read 2026-10-19: the one experiment is high-school writing revision, not problem-based work; it suggests framing a novice's goal for the problem phase as the investigative process rather than the finished solution, but nothing recorded tests that in PBL, so it does not change the model.

- [Ways of dealing with anomalous data, and the conditions determining them, can be described during PBL problem analysis](../claims/anomalous-data-handling-conditions-pbl.md) [~W] — read 2026-10-19: the claim page records only that these could be described from stimulated recall, not what they were, so it gives the model nothing to act on.
- [Students perceived CCS tasks as authentic problems whose answers teachers did not already know (52.2%) versus everyday school (8%)](../claims/ccs-tasks-authentic-teacher-no-answer.md) [+W] — read 2026-10-19: perceived authenticity in a community-science design, descriptive only; it measures no learning, so it does not change the model.
- [The PBL assumption that student-generated learning issues guide self-directed learning had never been empirically tested before this study](../claims/pbl-learning-issues-assumption-untested.md) [~W] — read 2026-10-19: a framing statement from Dolmans et al. (1994); the claim page does not record the study's result.
- [Despite extensive research on PBL, there is heated debate about its effectiveness](../claims/heated-debate-pbl-effectiveness.md) [~W] — read 2026-10-19: the authors' motivating sentence, with no evidence of its own; the model already plans for a variable effect.
- [Student engagement is higher during PBL than during traditional instruction](../claims/pbl-engagement-higher-than-traditional.md) [+W] — read 2026-10-19: reported second-hand in a scaffolding framework; engagement is not a learning outcome, so it does not change any configuration.
- [PBL offers potential to help students develop flexible understanding and lifelong learning skills](../claims/pbl-potential-flexible-understanding-lifelong-learning.md) [~W] — read 2026-10-19: a review's statement of potential, not a measured effect.
- [Learning through the experience of solving problems can build both content knowledge and thinking strategies](../claims/problem-experience-builds-content-and-thinking-strategies.md) [+W] — read 2026-10-19: the review's theoretical rationale for PBL, not a test of any configuration.

On 2026-10-19 (wave 2) the other twenty-three links the orphan-claim linker had added in a `## Claims` section were read and moved into the model: the evidence-base and outcome claims, staff against peer tutoring, the de Grave et al. (2001) recall trial, pre-test prediction, self-generated learning issues, the productive-failure qualifications (solution rates, the non-STEM replication failure, the piloted problem, the small-group variance study, the second-hand "deeper learning" account), lectures alongside PBL, the discussion-analysis studies, the unanswered conceptual question, group size, online drift, the AI rows and the preparation strategy.

The twelve claims listed here before that wave were read against the model on 2026-10-19 (wave 1) and now sit in it: prior knowledge before discussion (Van Blankenstein et al. 2013), whole and part tasks, the ninth-grade productive-failure experiment, the collaboration-skills and group-products rows (Murray-Harvey et al. 2013), the scripted-unit row and the AI and self-paced rows.

## Illustrative design instance and observation record

*Illustration only, invented, not a tested lesson.* An adult evening class in community health is given a problem: a neighbourhood's clinic reports rising missed appointments. The designer's objective is that learners can explain and apply a model of barriers to access; one learner says she wants to be able to argue for a change at her own workplace. Agree that both an individual explanation of the model and a defensible proposal matter. Ask each learner for a first framing; note that most list causes from experience but none names a structural barrier. Give a short resource on the model, let groups generate competing explanations, then teach the model explicitly against their explanations. Assess individually with a changed case a week later, separately for explanation and proposal.

Record: **problem and its framing → each learner's first response → resources, guidance and facilitation actually given, with timing → solutions generated → candidate interpretations and confidence basis → distinguishing probe → consolidation delivered → individual next observation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record but must not fabricate missing inputs or assign numerical state probabilities without a calibrated model.

## Elements and limits

[Problem-based learning](../elements/problem-based-learning.md), [problem scenario](../elements/problem-scenario.md), [solution development](../elements/solution-development.md), [invention](../elements/invention.md), [scaffolding](../elements/scaffolding.md), [case-based learning](../elements/case-based-learning.md), [group roles](../elements/group-roles.md), [feedback](../elements/feedback.md) and [reflection](../elements/reflection.md).

This pattern is scoped to problem-centred units in which an explicit consolidation of target content is planned. Fully self-directed inquiry with no consolidation, assessment of whole PBL curricula, and learner groups below the ages in the evidence need distinct configurations and evidence. The wiki records no direct comparison of whole PBL curricula with conventional instruction, and the diagnostic branches above remain to be tested with actual learners.

## Claims

- [Prior knowledge correlates negatively with delayed ICL and ECL and positively with delayed GCL, consistent with meta-analytic findings](../claims/prior-knowledge-correlates-with-load-types.md) [~W]
- [Creating products as part of problem-driven learning does not change its effect on motivation](../claims/product-creation-no-motivation-difference.md) [~W]

## Related Patterns
- [Anchored Instruction](anchored-instruction.md)
- [Case-Based Learning (Harvard Method)](case-based-learning.md)
- [Interdisciplinary Societal Dilemma Units](../designs/interdisciplinary-societal-dilemma-units.md) — a variant specific to civic/societal dilemmas spanning named disciplines
- [Organization Simulation for Interdisciplinary Learning](../designs/organization-simulation-for-interdisciplinary-learning.md) — adds a competitive external evaluator and organizational role structure to the authentic-problem, facilitated-inquiry core
- [Interdisciplinary Course-Based Research Experience](../principles/inquiry-based-learning.md) — organizes inquiry around a recurring shared object rather than a single driving problem
- [Bioart Boundary-Crossing Making](../designs/bioart-boundary-crossing-making.md) — organizes inquiry around progressive institutional access and material engagement
- [Learning by Producing (multimedia production as learning)](learning-by-producing-pattern.md)

## Examples

- A unit organized around diagnosing and responding to a realistic problem case.
- Medical learners diagnosing and responding to a patient scenario.
- Business learners working through a complex organizational case.
- Engineering or civic learners designing responses to a local real-world problem.
- [Teach AI through holistic, active, collaborative pedagogical strategies starting from real problem solving](../strategies/active-real-problem-solving-ai-teaching.md)

## Key Sources
- Hmelo-Silver, C. E. (2004). Problem-based learning: What and how do students learn? *Educational Psychology Review, 16*(3), 235-266. [https://doi.org/10.1023/B:EDPR.0000034022.16470.f3](https://doi.org/10.1023/B:EDPR.0000034022.16470.f3)
- Barrows, H. S., & Tamblyn, R. M. (1980). *Problem-based learning: An approach to medical education*. Springer.
- Savery, J. R. (2006). Overview of problem-based learning: Definitions and distinctions. *Interdisciplinary Journal of Problem-Based Learning, 1*(1), 9-20. [https://doi.org/10.7771/1541-5015.1002](https://doi.org/10.7771/1541-5015.1002)
- Murray-Harvey, R., Pourshafie, T., & Santos Reyes, W. (2013). What teacher education students learn about collaboration from problem-based learning. Journal of Problem Based Learning in Higher Education, 1(1), 114-134. https://eric.ed.gov/?id=EJ1108330
- Van Blankenstein, F. M., Dolmans, D. H. J. M., Van der Vleuten, C. P. M., & Schmidt, H. G. (2013). Relevant prior knowledge moderates the effect of elaboration during small group discussion on academic achievement. *Instructional Science, 41*, 729-744. [https://doi.org/10.1007/s11251-012-9252-3](https://doi.org/10.1007/s11251-012-9252-3)

<!-- deprecated 2026-10-01: superseded by the conditional model above. Old body kept verbatim.

## Description
Problem-Based Learning uses an authentic or ill-structured problem to drive inquiry, knowledge building, and solution development. This page serves as the canonical short-form target for links that refer to PBL without the explicit acronym.

## Implications

### Context
#### Requirements
- **A meaningful problem**
- **Learner investigation and solution development**
- **Facilitation and feedback**
#### Constraints
- **Novices may require more guidance**
- **Problems must be authentic enough to sustain inquiry**
#### Grain Size
- Unit
- Course

### Target Goals
- Drive learning through inquiry, explanation, and application.

### Target Learners
- Learners building applied reasoning and collaborative problem solving.

### Theory
#### Supporting
- [Problem-based Learning](../principles/problem-based-learning.md)
- [Constructivism](../principles/cognitive-activation.md)

### Claims
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+M]

## Design

### Sequence
1. Present an authentic problem.
2. Identify what needs to be known.
3. Investigate and develop possible solutions.
4. Test, justify, and refine a response.

### Elements Used
- [Problem-Based Learning](../elements/problem-based-learning.md)
- [Problem Scenario](../elements/problem-scenario.md)
- [Solution Development](../elements/solution-development.md)

### Affordances
- [Problem-based Learning](../principles/problem-based-learning.md)
- [Active Learning](../principles/active-learning.md)
-->

<!-- deprecated 2026-10-02: superseded after the brief test, which found answers following the previous version into problem-first designs for novices.

2. **Choose the guidance level provisionally.** If learners are task-specific novices and the target content cannot be reached from what they know, plan explicit guidance (resources that carry the content, prompts, worked or modelled steps) rather than leaving the content to be discovered. If learners can generate several partial solutions, a bounded problem-first phase followed by consolidating instruction is a candidate.
-->

<!-- merged 2026-10-02 from patterns/problem-based-learning-pbl ("Problem-Based Learning (PBL)"), a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Problem-Based Learning (PBL)

> **Pattern** · [All patterns](index.md)
> **Evidence** · 5 claims (3 for, 2 mixed) · 10 studies (4 causal, 2 qualitative, 2 theoretical, 1 quant-synthesis, 1 review), `q2`–`q4` · 0 of 10 report an effect size · 3 claims rest on one study

## Description
Problem-Based Learning is a pattern that organizes a course, unit, or module around a complex problem that learners must investigate and respond to. Instead of teaching all required content first, the pattern uses the problem to generate the need for inquiry, evidence gathering, collaboration, and explanation. Learners identify what they need to know, research relevant information, test ideas, and refine proposed responses.

The pattern is strongest when the problem is authentic enough to matter and the facilitation is strong enough to keep the inquiry rigorous. It is not equivalent to minimal guidance. Good PBL is structured, coached, and accountable.

## Implications

### Context
#### Requirements
- **A meaningful ill-structured problem**: The problem should require interpretation, inquiry, and judgment.
- **Access to evidence and resources**: Learners need materials, data, cases, or sources they can investigate.
- **Facilitated inquiry**: Instructors need to scaffold process and evidence use without taking over the problem.
- **A decision, proposal, or product**: Learners should arrive at some defended response to the problem.
#### Constraints
- **Novice overload**: Learners with limited background may need more direct support or preteaching.
- **Busy-work risk**: Inquiry can become shallow if evidence use and synthesis expectations are weak.
- **Time intensity**: PBL usually takes longer than direct explanation-first instruction.
- **Coordination demands**: Group work can mask uneven understanding unless roles and accountability are designed clearly.
#### Grain Size
- Unit
- Course

### Target Goals
- **Problem solving and reasoning**: Applying knowledge to ambiguous situations.
- **Evidence-based inquiry**: Identifying what must be learned and using sources purposefully.
- **Transfer**: Learning in ways that resemble authentic future use.

### Target Learners
- **Higher education, adult, and professional learners**: Strong fit where authenticity and application matter.
- **Learners developing self-directed inquiry habits**: PBL builds planning, monitoring, and revision.
- **Collaborative groups**: The pattern benefits from distributed reasoning and shared investigation.

### Theory
#### Supporting
- Constructivist perspectives — learners build understanding through engagement with a meaningful problem.
- Situated and experiential learning traditions — realistic contexts improve relevance and application.
- Self-regulated learning perspectives — extended problem work requires planning, monitoring, and adaptation.
#### Contradicting / Qualifying
- Some foundational objectives are learned more efficiently through explicit instruction before or during PBL.
- The pattern depends on facilitation; unguided open-ended work is not the same thing.
- Written PBL curricula design authenticity in advance ("contrived" authenticity), but the strongest engagement in one case study came from a teacher's spontaneous departure from the script to respond to a real event — suggesting curriculum flexibility and teacher autonomy matter as much as the designed scenario itself.

### Claims
#### Supporting
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [+M]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+M]
- [Process goals lead to better skill acquisition for novices than outcome goals.](../claims/process-goals-outperform-outcome-goals-for-novices.md) [~M]
- [Spontaneous responsiveness to real-world events in PBL can deepen student-directed inquiry beyond what designed curriculum achieves](../claims/spontaneous-authenticity-in-pbl-deepens-student-directed-inquiry.md) [+W] — a single case study found that a teacher's in-the-moment departure from the written PBL sequence, to respond to an unplanned real-world event tied to the driving question, produced deeper student-initiated inquiry than the pre-designed ("contrived") authentic scenario
#### Contradicting

- [Part-task practice reduces cognitive load for absolute novices during initial skill acquisition.](../claims/part-task-practice-reduces-load-for-novices.md) [~M]

## Design

### Sequence
1. Introduce a complex authentic problem.
2. Have learners identify what they know, what they need to know, and how they will investigate.
3. Support inquiry, evidence gathering, and collaborative reasoning.
4. Ask learners to propose and justify a response, solution, or recommendation.
5. Debrief what was learned about both the problem and the inquiry process.

### Elements Used
- [Problem Presentation](../elements/problem-presentation.md)
- [Inquiry and Research](../elements/inquiry-and-research.md)
- [Problem-Solving Tasks](../elements/problem-solving.md)
- [Reflection](../elements/reflection.md)

### Affordances
- [Problem-based Learning](../principles/problem-based-learning.md)
- [Inquiry-based Learning](../principles/inquiry-based-learning.md)
- [Authentic Audiences & Purposes](../principles/authentic-audiences-purposes.md)
- [Guided Practice](../principles/guided-practice.md)

### Personalization
- Problems can be selected or adapted for learner context and domain.
- Inquiry supports can be heavier for novices and lighter for more experienced learners.
- Products can vary, including presentations, proposals, designs, or cases.

## Related Patterns

- [Anchored Instruction](anchored-instruction.md)
- [Case-Based Learning (Harvard Method)](case-based-learning.md)
- [Interdisciplinary Societal Dilemma Units](../designs/interdisciplinary-societal-dilemma-units.md) — a variant specific to civic/societal dilemmas spanning named disciplines
- [Organization Simulation for Interdisciplinary Learning](../designs/organization-simulation-for-interdisciplinary-learning.md) — adds a competitive external evaluator and organizational role structure to the authentic-problem, facilitated-inquiry core
- [Interdisciplinary Course-Based Research Experience](../principles/inquiry-based-learning.md) — organizes inquiry around a recurring shared object rather than a single driving problem
- [Bioart Boundary-Crossing Making](../designs/bioart-boundary-crossing-making.md) — organizes inquiry around progressive institutional access and material engagement
- [Learning by Producing (multimedia production as learning)](learning-by-producing-pattern.md)

## Examples
- Medical learners diagnosing and responding to a patient scenario.
- Business learners working through a complex organizational case.
- Engineering or civic learners designing responses to a local real-world problem.

## Impact
- Strong pattern for integrating inquiry, collaboration, and authentic transfer.
- Most effective when the problem is real enough to matter and the facilitation is strong enough to prevent drift.

## Key Sources
- Barrows, H. S., & Tamblyn, R. M. (1980). *Problem-based learning: An approach to medical education*. Springer.
- Hmelo-Silver, C. E. (2004). Problem-based learning: What and how do students learn? *Educational Psychology Review, 16*(3), 235-266. [https://doi.org/10.1023/B:EDPR.0000034022.16470.f3](https://doi.org/10.1023/B:EDPR.0000034022.16470.f3)
- Savery, J. R. (2006). Overview of problem-based learning: Definitions and distinctions. *Interdisciplinary Journal of Problem-Based Learning, 1*(1), 9-20. [https://doi.org/10.7771/1541-5015.1002](https://doi.org/10.7771/1541-5015.1002)
-->

<!-- merged 2026-10-15 from patterns/maastricht-seven-step-pbl-tutorial-cycle ("Seven-step Maastricht PBL tutorial cycle with progressive case disclosure and group presentation"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Seven-step Maastricht PBL tutorial cycle with progressive case disclosure and group presentation

> **Pattern** · [All patterns](index.md)
> **Evidence** · 6 claims (4 for, 2 mixed) · 2 studies (1 qualitative, 1 design), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The course used a hybrid form of the 7-step Maastricht PBL model in which a case 'story' unfolds progressively over tutorials through 'pages' of information following a trigger scenario. Table 1 structures the cycle: whole-class work on clarification, definition, analysis and review; small groups establishing learning goals; self-directed study; reconvening to report and synthesise; a non-contact preparation week; a 15-minute group presentation with anonymous peer and tutor feedback; and a post-presentation debrief with self-assessment against a four-dimension tutorial performance survey.

## Design Implications

### Context
#### Requirements
- Cases designed with practicing teachers to cover course objectives, represent teacher problems rather than student deficits, and be authentic classroom issues
#### Constraints
- Delivered as a hybrid: cases were interdisciplinary but confined to one course over one semester, concurrent with lectures

### Target Learners
- undergraduate and postgraduate teacher education students in tutorials of 15-25 students, in teams of around five

### Target Goals
- problem solving, self-directed learning, and collaborative teamwork alongside educational psychology content

### Claims

- [Prepare And Assess Pbl Process Reflection](../strategies/prepare-and-assess-pbl-process-reflection.md) [+M]
- [Approximately half of students' analysed texts showed collaborative learning meeting co-regulation and co-construction descriptors](../claims/half-of-texts-showed-collaborative-learning.md) [+W]
- [Students made minimal reference to higher-level cognitive or metacognitive processing benefits of group work, departing from prior PBL research](../claims/minimal-reference-higher-level-processing-benefits.md) [~W]
- [Teacher education students in PBL identified valuing others' perspectives, interdependence, and learning about self as attitudes necessary for collaborative learning](../claims/pbl-attitudes-valuing-interdependence-self.md) [+W]
- [Students described knowledge gained through PBL group work in terms of generation, application, and dissemination of knowledge, plus pedagogical knowledge for future teaching](../claims/pbl-knowledge-generation-application-dissemination.md) [+W]
- [Students characterised the skills needed for collaborative group work as interpersonal (social), problem solving, and group skills](../claims/pbl-skills-interpersonal-problem-solving-group.md) [+W]
- [In a self-selected survey, students favored delayed disclosure and agency, but 39.3% found the system too indirect and 42.9% reported repetition](../claims/staged-feedback-survey-perceptions.md) [~W]

## Related Patterns
- 

## Examples
-

## Key Sources
- Murray-Harvey, R., Pourshafie, T., & Santos Reyes, W. (2013). What teacher education students learn about collaboration from problem-based learning. Journal of Problem Based Learning in Higher Education, 1(1), 114-134. https://eric.ed.gov/?id=EJ1108330
-->
