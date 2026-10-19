---
type: pattern
id: self-regulated-learning
aliases: [explicit-versus-inferred-compliance-prompt-taxonomy]
title: Self-Regulated Learning
description: "A reusable plan–monitor–act policy that makes regulation explicit with task-specific prompts, modelled self-assessment and a usable next action, then reads the response before handing regulation to the learner."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: zimmerman-2002
    resource: "https://doi.org/10.1207/s15430421tip4102_2"
    title: "Zimmerman, B. J. (2002). Becoming a self-regulated learner: An overview. *Theory Into Practice, 41*(2), 64-70"
    author: Zimmerman, B. J
  - id: lallé-2017
    resource: "https://educationaldatamining.org/EDM2017/"
    title: "Lallé, S., Mudrick, N., Conati, C., Taub, M., Azevedo, R. (2017). On the Influence on Learning of Student Compliance with Prompts Fostering Self-Regulated Learning. Proceedings of the 10th International Conference on Educational Data Mining. https://educationaldatamining.org/EDM2017/"
    author: Lallé, S., Mudrick, N., Conati, C., Taub, M., Azevedo, R
author: self-regulated learning tradition
grain_size: unit
---

# Self-Regulated Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 55 claims (19 for, 33 mixed, 3 against) · 49 studies (19 causal, 9 associational, 8 review, 6 quant-synthesis, 5 theoretical, 1 qualitative, 1 design), `q1`–`q4` · 13 of 49 report an effect size · 48 claims rest on one study

## Description and scope

A reusable policy for making planning, monitoring against a criterion and choosing a next action explicit within subject-matter work, then reading each response before reducing support. It instantiates the [conditional principle](../principles/self-regulated-learning.md). The study configurations below (prompts in computer-based environments, school training programmes, web-based training with a diary and peer feedback, modelled self-assessment) are evidence; the response-dependent policy is an **untested design proposal**. Use it to gather better evidence about a learner's regulation, not to certify a trait called "self-regulated".

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Task-specific prior knowledge (a short content probe); a prediction or self-rating set beside a scored result; whether the learner already plans or reviews unprompted; age band and setting. Preserve unknowns. |
| Context and activities | Subject task the regulation is attached to; `classroom`, `online-self-paced` or other setting; time available across the unit; who delivers any training; prompts, diary, rubric, peer groups and feedback actually available; what the learner can choose (chapters, order, pace, help). |
| Learner-valued goal | Ask what the learner wants from this unit and why. Record disagreement with the designer objective; negotiate rather than assume agreement. |
| Designer objective | Which capability matters: subject performance, accurate self-assessment, a planning habit, or independent regulation without prompts. Say which supports are permitted at the target. |
| Outcome | Instrument for each objective (subject test aligned with what was regulated; calibration of self-ratings against scores; behaviour traces such as logged time or revisions; questionnaire, labelled as self-report), the local criterion, and the horizon (`immediate`, end of unit, `delayed`). |

A request to "make learners more independent" does not specify these inputs. Ask for them before prescribing a prompt schedule, a diary or a fading point. Check that the criterion learners monitor against is itself correct and understandable; monitoring against an unclear rubric produces confident error.

## Sequence and conditional policy

1. **Elicit briefly.** Before support, ask for a short plan for the coming task and a prediction of performance; then score the task. Record the gap between prediction and score, and whether a plan was written at all. These probes are also learning events; record them.
2. **Model the regulation on this task.** Show a worked example of someone setting a goal, checking work against the criterion, rating it and choosing a next action, in the subject the learner is studying rather than as a separate study-skills session.
3. **Prompt at natural pauses.** Use short, task-specific planning, monitoring and evaluation prompts before, between and after task segments, paired with feedback on the task where possible. Offer a named set of next actions (review, try a different method, ask for help, move on) so that monitoring has something to act on.
4. **Choose the next activity provisionally.** Use the table below. Repeat matched observations where feasible; prior knowledge, task difficulty and the prompts themselves confound a single reading.
5. **Reobserve, then reduce support.** Score a new representative task with fewer prompts at the agreed horizon, and compare self-ratings with the score again. Reduce prompts only after the learner's choices and calibration hold without them; keep unresolved explanations on the record.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Large overestimate of own score | Ask for a prediction after a retrieval attempt rather than after rereading; have the learner score a worked exemplar with the rubric; run a short content probe. | If calibration improves after retrieval or exemplar scoring, keep that step before every self-rating. If the content probe is weak, treat it as a knowledge gap first and do not rely on self-assessment yet. Neither branch is a validated diagnosis. |
| Accurate rating, next choice does not change | Present a fixed menu of next actions and ask why the learner chose one; ask what they are aiming for. | If no option seems usable, teach one control strategy explicitly. If the goal is not valued, negotiate the task before adding prompts. More monitoring prompts alone are unlikely to help. |
| Prompts and diary completed, subject scores flat | Compare entries with traces (time, revisions, chapters chosen); score the chapters the learner chose to focus on separately from the overall test. | If focus-area scores rise and the overall score does not, the outcome may be misaligned, not the regulation. If traces do not change either, replace generic prompts with task-specific ones or add feedback on the plan. |
| Uses supports only when present | Remove one prompt type on a matched task and observe whether planning or checking still occurs. | Fade one prompt at a time and reobserve. Keep the prompt if removal costs performance at the target and permanent prompting is acceptable to the objective. |
| Little participation or abandons plans | Ask about purpose, time and barriers; supply the plan and see whether execution follows. | If execution follows a supplied plan, provide plans and teach planning later. If not, the barrier may be content, load or motivation rather than planning skill. |

## Choosing configurations from evidence

- For learning in a computer-based environment, [task-specific metacognitive prompts](../claims/metacognitive-prompts-improve-learning.md) [+M] are a candidate configuration: a meta-analysis against no-prompt controls reported g = 0.40 on learning outcomes, varying with feedback pairing, task specificity and adaptivity. It does not set a schedule, and it does not show effects outlast the prompts; one reviewed study found lower-prior-knowledge learners needed training before prompts helped.
- For school learners, [SRL training programmes](../claims/self-regulated-learning-improves-achievement.md) [+M] have a pooled average of 0.69 across 84 studies, but over performance, strategy use and motivation together, and larger when researchers delivered them. Do not forecast a teacher-delivered unit's achievement gain from it; in online settings support helped only when it was used.
- Before relying on self-ratings, [modelling self-assessment](../claims/self-assessment-accuracy-is-low-without-training.md) [~M] is a candidate step: in a randomized experiment with 80 pre-university students on genetics problems, modelling examples improved self-assessment accuracy (ηp² = .10). It shows calibration can be trained; it does not show the trained learners then learned more.
- A [diary alone](../claims/learning-diary-alone-no-significant-srl-gains-online-math-prep-course.md) [~M] showed no detected pre–post gain on any measured outcome in a randomized four-group online mathematics preparation trial; equivalence was not tested, so this is no detected gain, not no effect. Not yet checked against its sources.
- In the same trial, [training plus a diary](../claims/web-based-srl-training-with-diary-raises-srl-knowledge-and-self-efficacy-not-math.md) [~M] raised SRL knowledge, self-reported planning and metacognition, and self-efficacy, but not mathematics scores (checked by the judge: all 2 entries pass, full text); across groups the [overall mathematics score missed significance while a score on self-chosen chapters did not](../claims/srl-interventions-math-overall-score-marginal-focus-score-significant-online-prep-course.md) [~M] (checked by the judge: all 2 entries pass, full text). Choose the outcome instrument before choosing the configuration: a broad test may not register what learners chose to regulate.

Do not rank these configurations by their effect labels: the comparators, learners, outcomes and horizons differ, and the 0.69 and 0.40 figures are not on one outcome.

## Fitting the design to a situation

Ask for three facts when the brief omits them: **the setting** (taught classroom, or `online-self-paced` with no instructor), **the learners' prior knowledge of this content**, and **the outcome and horizon that count**. Each row changes one step of the sequence above.

| If the brief says… | Then change… | Basis |
|---|---|---|
| `online-self-paced`, no instructor to model the steps | Deliver step 2 as a short web-based training on the regulation steps, and pair it with a daily diary; do not run the diary alone | [Training plus a diary raised SRL knowledge and self-efficacy](../claims/web-based-srl-training-with-diary-raises-srl-knowledge-and-self-efficacy-not-math.md) [~M]; [A diary alone gave no significant gains](../claims/learning-diary-alone-no-significant-srl-gains-online-math-prep-course.md) [~M] |
| A cohort that can work in small groups | Add peer-feedback groups to step 3, where learners comment on each other's plans and diaries | [Peer feedback groups added self-motivation, volition and reflection gains](../claims/peer-feedback-groups-add-self-motivation-volition-reflection-gains-to-web-based-srl-training.md) [+M] |
| A computer-based environment that can check what learners do with a prompt | In step 3, prefer prompts that ask for a product (revise your summary, review your notes, set a subgoal) and check the product; prompts that only move learners through pages showed no link to learning | [Review-notes prompt compliance predicts gains](../claims/review-notes-compliance-predicts-learning-gains.md) [+W]; [Four explicit SRL prompts showed no learning effect](../claims/no-learning-effect-for-four-explicit-srl-prompts.md) [~W] |
| Learners have low prior knowledge of the content | In step 1, run the content probe first; in step 2, model self-assessment on a worked example before asking learners to rate themselves | [Self-assessment accuracy is low without training](../claims/self-assessment-accuracy-is-low-without-training.md) [~M]; [Prior knowledge is needed for accurate self-assessment](../claims/prior-knowledge-needed-for-accurate-self-assessment.md) [~M] |
| Learners are acquiring a new procedure | In step 1, have learners plan around process goals (the strategy steps), and move to outcome goals once the steps are secure | [Process goals outperform outcome goals for novices](../claims/process-goals-outperform-outcome-goals-for-novices.md) [+M] |
| Learners rate their work after rereading or after a fluent explanation | Ask for the self-rating after a retrieval attempt or after scoring an exemplar, not straight after study; fluent presentation raises confidence without raising learning | [Fluent illusions mislead self-assessment](../claims/fluent-illusions-mislead-self-assessment.md) [~M] |
| The outcome is a broad end-of-course test over a few weeks | In step 5, score the learner's chosen focus areas and the broad test separately, and keep a behaviour trace beside any questionnaire | [Overall mathematics score marginal, focus score significant](../claims/srl-interventions-math-overall-score-marginal-focus-score-significant-online-prep-course.md) [~M] |
| Learners use a generative AI assistant during the task | Add a step-3 prompt before learners accept AI output (confidence, how would you check it), and feedback on their own AI use | [Reflection reduces acceptance of incorrect AI advice](../claims/reflection-reduces-incorrect-ai-advice-acceptance.md) [+M]; [Metacognitive feedback reduces answer offloading](../claims/metacognitive-feedback-reduces-llm-answer-offloading-improves-unaided-performance.md) [+M] |
| The AI tool shows its reasoning traces to learners | Do not treat reading the traces as self-evaluation; keep a scored check against which learners compare their own rating | [No trace format supported calibrated self-evaluation](../claims/no-trace-format-supported-calibrated-self-evaluation.md) [~W] |
| The unit is long and prompts would run throughout | In step 5, remove one prompt type at a time and reobserve; repeated prompts may become routine rather than build a habit | [Repeated reflective prompts may habituate](../claims/reflective-scaffolding-habituation-deskilling.md) [~W]; untested proposal for the order of removal |
| A single session, not a unit | Keep steps 1 and 3 only (a plan, a prediction, feedback on the gap); skip fading, which needs repeated observation | untested proposal |

## The evidence by question

- *Does teaching and prompting self-regulation improve achievement over ordinary instruction?* [Self-regulated learning improves achievement](../claims/self-regulated-learning-improves-achievement.md) [+M]
- *Do planning, monitoring and evaluation prompts help, and which ones?* [Metacognitive prompts improve learning](../claims/metacognitive-prompts-improve-learning.md) [+M]
- *Can learners' own monitoring be trusted, and can it be trained?* [Self Assessment Accuracy Is Low Without Training](../claims/self-assessment-accuracy-is-low-without-training.md) [~M]

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Self-regulated learning models treat self-monitoring as a core process through which learners notice gaps and adjust strategy](../claims/self-monitoring-improves-self-regulation.md) [+M] — not settled: the text available could not confirm the entries (abstract)
- [Compliance with MetaTutor's summarize, stay-on-subgoal, move-to-next-subgoal, and open-diagram prompts shows no significant effect on learning gains](../claims/no-learning-effect-for-four-explicit-srl-prompts.md) [~W] — attached 2026-10-07 from Lallé et al. (2017), which proposed "Two-category taxonomy of SRL prompts by how compliance can be evaluated: explicit vs inferred compliance prompts"; tests this page's relationship.
- [Higher compliance with MetaTutor's review-notes prompt is associated with larger proportional learning gains](../claims/review-notes-compliance-predicts-learning-gains.md) [+W] — attached 2026-10-07 from Lallé et al. (2017), which proposed "Two-category taxonomy of SRL prompts by how compliance can be evaluated: explicit vs inferred compliance prompts"; tests this page's relationship.
- [Higher compliance with MetaTutor's revise-summary prompt is associated with larger proportional learning gains](../claims/revise-summary-compliance-predicts-learning-gains.md) [+W] — attached 2026-10-07 from Lallé et al. (2017), which proposed "Two-category taxonomy of SRL prompts by how compliance can be evaluated: explicit vs inferred compliance prompts"; tests this page's relationship.
- [Higher compliance with MetaTutor's suggest-subgoal prompt is associated with larger proportional learning gains](../claims/suggest-subgoal-compliance-predicts-learning-gains.md) [+W] — attached 2026-10-07 from Lallé et al. (2017), which proposed "Two-category taxonomy of SRL prompts by how compliance can be evaluated: explicit vs inferred compliance prompts"; tests this page's relationship.
- [Feedback interventions show phase-specific effects: advice feedback reduces reminder bias, but ranking feedback alters beliefs without increasing offloading](../claims/feedback-effects-on-offloading-mixed.md) [+W] — attached 2026-10-10 from Yufei Guo et al. (2026), which proposed "Match feedback type to metacognitive component and task phase: calibrate beliefs before tasks, provide task-specific feedback during tasks".
- [No trace format supported calibrated self-evaluation: perceived-achieved correlations were low and non-significant in all conditions](../claims/no-trace-format-supported-calibrated-self-evaluation.md) [~W] — attached 2026-10-11 from Fernandes et al. (2026), which proposed "Scaffold metacognitive support by eliciting users' own reasoning before exposing the model's reasoning traces or answer".
- [No Learning Effect For Metacognitive Monitoring Prompts](../claims/no-learning-effect-for-metacognitive-monitoring-prompts.md) [~M]
- [More fixations on the learning content after an add-subgoal prompt are associated with higher learning gains, suggesting complying with that prompt may not be effective](../claims/add-subgoal-prompt-compliance-may-not-help-learning.md) [~M]

## Illustrative design instance and observation record

*Illustration, invented, not a tested design.* An adult learner in a four-week self-paced statistics refresher says she wants to stop "freezing" on hypothesis-test questions; the designer's objective is a pass on the end-of-course test and a weekly planning habit. Agree that both count and record them separately. Week 1: a short plan and a prediction before a mixed problem set; she predicts 80% and scores 45%, with errors concentrated in test selection. A content probe shows she cannot yet say which test fits which design, so self-rating is not yet relied on; a modelled self-check of a worked solution against a three-point rubric is added before each later self-rating, with planning prompts at the start of each session and a menu of next actions. Week 3: prediction and score are within ten points on test-selection items; one prompt type is removed on a matched set. The end-of-course test and a score on the chapters she chose are reported separately.

Record: **task and criterion → supports present (prompts, model, rubric, feedback) → plan and prediction → scored result → candidate interpretations and their basis → discriminating probe → chosen next activity and why → next observation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record, but must not fabricate missing inputs or assign numerical state probabilities without a calibrated model.

## Elements and limits

[Goal setting](../elements/goal-setting.md), [self-monitoring](../elements/self-monitoring.md), [prompts](../elements/prompts.md), [metacognitive strategies](../elements/metacognitive-strategies.md), [self-assessment](../elements/self-assessment.md), [rubric](../elements/rubrics.md), [feedback](../elements/feedback.md), [peer feedback](../elements/peer-feedback.md), [reflection](../elements/reflection.md), [daily before-and-after SRL learning diary](../elements/daily-before-and-after-srl-learning-diary.md) and [fading scaffolding](../elements/fading-scaffolding.md).

This pattern is scoped to regulation attached to subject-matter tasks over a unit. Standalone study-skills courses, motivational interventions, behavioural self-monitoring for on-task conduct and adaptive systems that take regulation decisions for the learner are distinct configurations with their own evidence. The present policy supports observation and design reasoning; its branches, fading rule and the role of the learner's valued goal remain to be tested with actual learners.

## Claims

- [A randomized controlled trial with 86 K-12 students found a significant gain in self-regulated-learning strategy use from agentic coaching systems](../claims/agentic-srl-coaching-rct-86-significant-strategy-gain.md) [+W]
- [Repeated reflective prompts may habituate, so scaffolding can replace rather than strengthen the user's own metacognitive habits](../claims/reflective-scaffolding-habituation-deskilling.md) [~W]
- [The pooled effect of self-regulated learning does not differ significantly by school level](../claims/srl-effect-no-school-level-difference.md) [~W]
- [Within-session SRL change shows no detectable association with unaided post-test performance](../claims/srl-change-no-posttest-association.md) [~W]
- [Delegating the terminal evaluation to AI is self-defeating: each hand-off returns one more output someone must accept or not](../claims/delegating-evaluation-self-defeating.md) [+W]
- [Self-regulated learning strategies have a large pooled effect (d = 0.859) on academic achievement across 21 Turkish studies](../claims/srl-strategies-large-effect-academic-achievement.md) [+W]
- [The pooled effect of self-regulated learning does not differ significantly by course type, though mathematics shows the largest descriptive effect](../claims/srl-effect-no-course-type-difference.md) [~W]
- [Verification bottleneck: as reliance on AI increases, accuracy in detecting AI errors decreases while confidence does not](../claims/verification-bottleneck-confidence-dissociation.md) [~W]
- [Reflection increased in the adaptable and non-adaptable script conditions, but only the adaptable script had positive effects on monitoring, supporting overall positive effects on self-regulation](../claims/adaptable-script-monitoring-self-regulation-effects.md) [~W]
- [Groups perceiving a learning situation as challenging switched frequently between planning and performance phases of regulation](../claims/challenging-situations-drive-plan-perform-switching.md) [~W]
- [Explicit instruction of SRL strategies is rare among primary teachers in both an iSELF-trained group and an untrained control group](../claims/explicit-srl-instruction-rare-primary-teachers-both-conditions.md) [~W]
- [In the generalized condition, compliance with several suggested actions was associated with higher essay scores, with one exception: note-taking after the last scaffold was associated with lower essay scores.](../claims/compliance-suggested-actions-essay-scores-mixed.md) [~W]
- [Most direct SRL promotion targeted cognitive capabilities and rarely mentioned the benefit of strategy use](../claims/cognitive-capability-dominance-benefit-rarely-mentioned.md) [~W]
- [A Monitoring and Regulation Strategy delivered online increased university students' exam scores, whereas the Monitoring Exercise alone did not](../claims/mrs-strategy-increased-exam-scores.md) [+W]
- [Absolute monitoring accuracy showed a mixed, inconsistent group-by-time interaction rather than a stable competitiveness difference](../claims/inconsistent-absolute-accuracy-competitiveness.md) [~W]
- [Regulation-of-learning interventions in programming education show an average effect of 0.59 on programming learning](../claims/regulation-interventions-programming-average-effect.md) [+W]
- [No intervention effect on directly observed on-task self-regulation in the musical play study](../claims/musical-play-intervention-no-on-task-self-regulation-effect.md) [-W]
- [No effects of reported planner or reviser scores were found on evaluating own text](../claims/no-effects-evaluating-own-text.md) [-W]
- [Prompts increased learners' self-efficacy during learning within the prompted group but did not produce between-group differences at mid-learning or post-learning](../claims/prompts-increase-self-efficacy-during-learning.md) [~W]
- [In Experiment 2, self-regulation skills significantly positively predicted domain-specific MAS only in the minimal heuristic worked examples condition](../claims/self-regulation-predicts-domain-specific-mas-minimal-worked-examples.md) [~W]
- [Lower-prior-knowledge apprentices gained more self-efficacy with retrospective prompts, while anticipatory prompts were detrimental for them](../claims/prior-knowledge-moderates-prompt-direction-self-efficacy.md) [~W]
- [Students showed significant learning gains on domain knowledge (large effect) and concept maps (medium effect) after a 45-minute SRL-rich learning task](../claims/srl-task-learning-gains-domain-concept-maps.md) [+W]
- [Self-scoring improves regulation accuracy for the whole sample, but not significantly for low- and high-performing students on division tasks](../claims/self-scoring-regulation-accuracy-limited-division.md) [~W]
- [Teachers typically provide only little explicit support for SRL in their classrooms](../claims/teachers-provide-little-explicit-srl-support.md) [+W]
- [The three-way group × time × practice interaction was significant for explicitness but not duration: MCS explicitness rose more in the SRL-AIDE group while KC explicitness rose more in the comparison group](../claims/three-way-interaction-explicitness-not-duration.md) [~W]
- [Teachers perceive SRL as desirable for students but not feasible to implement in their classrooms](../claims/teachers-srl-desirable-but-not-feasible.md) [~W]
- [The hypothesised mediation of prompt effects on self-efficacy via strategy use was not confirmed because prompts did not affect strategy use](../claims/strategy-mediation-of-prompt-self-efficacy-not-confirmed.md) [-W]
- [Sixth-graders' own monitoring accuracy is low and does not differ between no-cue, keyword, and summary cue-prompt conditions (Experiment 1).](../claims/student-monitoring-accuracy-low-no-cue-prompt-effect-exp1.md) [~W]
- [Teachers' SRL&T module scores improved modestly over the year, with Adam improving more (three to six points) than Ben (five to six)](../claims/srlt-module-scores-improvement-adam-ben.md) [~W]
- [Empirical studies support Zimmerman's SRL models, including expert-novice differences and phase-training effects](../claims/empirical-support-zimmerman-srl-models.md) [+W]
- [Explicit group regulation in online PBL was infrequent, emerged in response to challenges, and often involved teacher support](../claims/explicit-regulation-infrequent-challenge-responsive.md) [~W]
- [Low-prior-knowledge students struggle to deploy key self-regulatory processes during learning](../claims/low-prior-knowledge-students-struggle-self-regulation.md) [~W]
- [Teachers allocated on average five percent of intervention sessions to predicting and purpose setting, with fidelity of implementation averaging 45.4%](../claims/low-time-and-fidelity-engaged-reader-processes.md) [~W]
- [Learners often fail to regulate their own learning in computer-based learning environments](../claims/learners-fail-self-regulation-in-cbles.md) [~W]

## Key Sources
- Zimmerman, B. J. (2002). Becoming a self-regulated learner: An overview. *Theory Into Practice, 41*(2), 64-70. [https://doi.org/10.1207/s15430421tip4102_2](https://doi.org/10.1207/s15430421tip4102_2)
- Lallé, S., Mudrick, N., Conati, C., Taub, M., Azevedo, R. (2017). On the Influence on Learning of Student Compliance with Prompts Fostering Self-Regulated Learning. Proceedings of the 10th International Conference on Educational Data Mining. https://educationaldatamining.org/EDM2017/

<!-- deprecated 2026-10-01: superseded by the conditional model above. The original body follows verbatim.

## Description
Self-Regulated Learning is the pattern-level target for designs that explicitly cycle planning, monitoring, feedback, and revision so learners can manage their own learning more effectively.

## Implications

### Context
#### Requirements
- **Clear goals**
- **Feedback or evidence**
- **Routines for monitoring and adjustment**
#### Constraints
- **Learners may need modeling and scaffolds to regulate effectively**
#### Grain Size
- Lesson
- Unit

### Target Goals
- Strengthen planning, monitoring, and adaptive revision.

### Target Learners
- Learners developing independence and strategic control over learning.

### Theory
#### Supporting

- [Self-Regulated Learning](../principles/self-regulated-learning.md)

### Claims

- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [+M]

## Design

### Elements Used
- [Metacognitive Strategies](../elements/metacognitive-strategies.md)
- [Self-Assessment](../elements/self-assessment.md)
- [Reflection](../elements/reflection.md)
-->

<!-- merged 2026-10-15 from patterns/explicit-versus-inferred-compliance-prompt-taxonomy ("Two-category taxonomy of SRL prompts by how compliance can be evaluated: explicit vs inferred compliance prompts"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Two-category taxonomy of SRL prompts by how compliance can be evaluated: explicit vs inferred compliance prompts

> **Pattern** · [All patterns](index.md)
> **Evidence** · 6 claims (3 for, 3 mixed) · 1 study (1 associational), `q3` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The article classifies MetaTutor's SRL prompts into two categories based on how compliance can be evaluated. "Explicit compliance prompts" are those for which compliance "can be explicitly assessed from students subsequent responses", e.g. prompts requiring a yes/no answer or a specific action within a time frame. "Inferred compliance prompts" are those for which "compliance needs to be inferred by mining a variety of behaviors", such as staying on or moving from a page. The article mines window length, number of fixations, and number of SRL strategies to evaluate the latter.

## Design Implications

### Context
#### Requirements
- For inferred prompts, the system must log interaction and eye-tracking behaviors in data windows following each prompt delivery
#### Constraints
- Explicit compliance prompts require additional interactions that "might not always be possible, or might even be intrusive for some students"; for inferred prompts "there is no clear definition of what compliance means"

### Target Learners
- college students learning with an intelligent tutoring system

### Target Goals
- self-regulated learning strategy use

### Claims

- [No Learning Effect For Metacognitive Monitoring Prompts](../claims/no-learning-effect-for-metacognitive-monitoring-prompts.md) [~M]
- [More fixations on the learning content after an add-subgoal prompt are associated with higher learning gains, suggesting complying with that prompt may not be effective](../claims/add-subgoal-prompt-compliance-may-not-help-learning.md) [~M]
- [Compliance with MetaTutor's summarize, stay-on-subgoal, move-to-next-subgoal, and open-diagram prompts shows no significant effect on learning gains](../claims/no-learning-effect-for-four-explicit-srl-prompts.md) [~W]
- [Higher compliance with MetaTutor's review-notes prompt is associated with larger proportional learning gains](../claims/review-notes-compliance-predicts-learning-gains.md) [+W]
- [Higher compliance with MetaTutor's revise-summary prompt is associated with larger proportional learning gains](../claims/revise-summary-compliance-predicts-learning-gains.md) [+W]
- [Higher compliance with MetaTutor's suggest-subgoal prompt is associated with larger proportional learning gains](../claims/suggest-subgoal-compliance-predicts-learning-gains.md) [+W]

## Related Patterns
- 

## Examples
-

## Key Sources
- Lallé, S., Mudrick, N., Conati, C., Taub, M., Azevedo, R. (2017). On the Influence on Learning of Student Compliance with Prompts Fostering Self-Regulated Learning. Proceedings of the 10th International Conference on Educational Data Mining. https://educationaldatamining.org/EDM2017/
-->
