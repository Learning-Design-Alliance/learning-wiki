---
type: principle
id: adaptive-learning
moved_from: [pattern/adaptive-learning]
aliases: [adaptive-learning-consistent-with-cognitive-structure, gain-then-time-constant-adaptive-progression, multi-objective-exercise-recommendation-objectives, sequential-noisy-estimation-principle, avoid-student-intercepts-for-transfer, uncertainty-aware-knowledge-states-for-adaptive-decisions]
title: Adaptive Learning
description: "When learners on a cumulative, decomposable task start from different observed responses, choosing each next task, hint or check from the learner's own recent responses (rather than one fixed path) may improve aligned achievement, conditional on how well the responses diagnose the learner, what the adaptation changes, and whether support is withdrawn as performance grows."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-15
sources:
  - id: shuanghong-shen-2021
    resource: "https://arxiv.org/abs/2105.15106"
    title: "Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106"
    author: Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen
  - id: norman-1972
    resource: "https://eric.ed.gov/?id=ED059585"
    title: "Norman, D. A.; And Others. (1972). Adaptive Training of Manual Control: 1. Comparison of Three Adaptive Variables and Two Logic Schemes. Life Sciences, Inc. https://eric.ed.gov/?id=ED059585 [doi:10.1037/e426822004-001](https://doi.org/10.1037/e426822004-001)"
    author: Norman, D. A.; And Others
  - id: wolff-1970
    resource: "https://eric.ed.gov/?id=ED051258"
    title: "Wolff, Hans. (1970). On Stochastic Approximation. https://eric.ed.gov/?id=ED051258"
    author: Wolff, Hans
  - id: philip-i-pavlik-2021
    resource: "https://doi.org/10.1109/TLT.2021.3128569"
    title: "Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569"
    author: Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams
  - id: jia-nan-2026
    resource: "https://doi.org/10.1038/s41598-026-50711-y"
    title: "Jia Nan, Su Weitao, Xian Junrui, Zou Shijia, Xia Yixue. (2026). Adaptive G-UKT: a unified probabilistic framework for knowledge tracing via adaptive graph topology learning and uncertainty-aware Gaussian embeddings. Scientific Reports. https://doi.org/10.1038/s41598-026-50711-y"
    author: Jia Nan, Su Weitao, Xian Junrui, Zou Shijia, Xia Yixue
---

# Adaptive Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 66 claims (35 for, 27 mixed, 4 against) · 65 studies (22 causal, 17 review, 8 design, 7 quant-synthesis, 5 associational, 4 theoretical, 2 qualitative), `q1`–`q4` · 10 of 65 report an effect size · 59 claims rest on one study

## Conditional relationship

Where learners in one course start from different observed responses on a task whose parts can be checked separately (cumulative `procedure`, `principle` or `verbal-association` goals; mathematics, programming and language mechanics are the usual cases), selecting each learner's next task, hint, feedback or check from that learner's recent responses, instead of moving everyone through one fixed sequence, is expected to raise achievement on an aligned measure (`general-achievement`, mostly `immediate` or end-of-course). The relationship is conditional on four things: the responses must diagnose what the learner can and cannot yet do on the target task; the adaptation must change something that matters for learning (the support given or the task chosen, not only its order); support must be reduced as the learner's unassisted performance improves; and the outcome and horizon must be stated, since aligned test scores, standardised achievement, `delayed-retention`, `far-transfer` and `learning-time` move separately.

This page owns the general relationship: individualised selection against a fixed path, whoever or whatever does the selecting. Three converted pages hold narrower models inside it. [Scaffolding](scaffolding.md) treats support versus none during an attempt, and its model of contingent support is the within-task form of adaptation. [Mastery Learning](mastery-learning.md) treats one adaptive rule, a gate with correction and a recheck before advancing. [Formative Assessment](formative-assessment.md) treats the interpretation of evidence and the contingent action that any adaptive decision depends on. This page does not repeat them. The [adaptive learning pattern](adaptive-learning.md) is a short, unconverted stub.

**Only small single studies in the wiki test adaptation itself against the same content without it, and none does so at scale.** In the clearest, a randomised experiment with 120 undergraduates, diagnosed personalised paths saved learning time and raised an aligned post-test over a fixed order ([Personalized paths reduced learning time and improved post-test scores](../claims/personalized-paths-experiment-outcomes.md) [+M]); adaptive task difficulty did not help second-graders against an otherwise identical tutor ([Adaptive task difficulty did not improve second-graders' posttest](../claims/task-difficulty-adaptation-no-learning-benefit-second-grade.md) [-W]). The strongest evidence below compares intelligent tutoring systems, which bundle adaptation with step-level feedback, practice and a model of the task, with conventional instruction; it shows the bundle can help, not which part of it does.

## Default design, while the relationship is untested

The page's earlier guidance, kept as a concrete default a designer can act on and revise. Each step is a design proposal, with its evidence status beside it.

1. **Decide what the adaptation is for and how it will be judged.** Name the capability, the representative instrument, the criterion and the horizon before choosing a system or rule. Untested here; it follows from the outcome dependence in the tutoring meta-analyses below (gains depended on whether tests were locally developed or standardised).
2. **Build a diagnosis the adaptation can rest on.** Frequent, fine-grained checks on the parts of the task, using [assessment](../elements/assessment.md) or [assess performance](../elements/assess-performance.md). Untested as a step; the earlier page's requirement. The learner-model claim below shows that a model's predictions can be biased where it has little data, so treat each adaptive decision as an inference with error.
3. **Provide somewhere to move the learner**: a bank or sequence of tasks at varied difficulty ([adaptive difficulty](../elements/adaptive-difficulty.md)), including worked or partly worked examples for low starting responses. The adaptive routing is untested here; starting low responders on an example is supported for novices by one experiment in which sequences opening with a worked example beat problem-first sequences on an immediate test, with lower reported effort ([Example-problem sequences reduce cognitive load](../claims/worked-example-problem-sequences.md) [+M]; secondary-school electrical troubleshooting, n = 96 analysed; delayed and far-transfer outcomes not tested).
4. **Adapt the support, not only the difficulty or order.** Give hints and task- and process-level [feedback](../elements/feedback.md) tied to what the response showed, raising support after an error and lowering it after success. Supported in one-to-one tutoring by the contingent-scaffolding claim. What the feedback should carry is supported, from feedback research in general rather than adaptive systems, by two meta-analyses in which high-information feedback on the task and process outperformed reinforcement and self-directed feedback ([Feedback is most effective at task and process levels](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]; both support the levels only indirectly). In AI tutoring logs, the association between asking another question and recovering from an impasse weakened with each further failed turn, while addressing the learner's error became more useful ([Questioning benefit decays with impasse depth](../claims/questioning-benefit-decays-with-impasse-depth.md) [+W]; [Repeating a scripted question lowers recovery](../claims/repeating-scripted-question-lowers-recovery.md) [+W]; one associational study). The earlier page's statement that difficulty-only adaptation gives weaker gains is not tested by any claim here.
5. **Gate progression on an explicit criterion** with correction and a recheck ([adaptive mastery learning](../elements/adaptive-mastery-learning.md)), as modelled in [Mastery Learning](mastery-learning.md). Evidence is on that page.
6. **Withdraw support as unassisted performance grows**, checking on unsupported items before removing it. Bounded support from the expertise-reversal claim below (a review; abstract not confirmed), and from fading worked examples into independent problems, which favoured near transfer over static example-problem arrangements in three experiments ([Fading support promotes the transfer of responsibility](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S]; near transfer only, no fading rate established).
7. **Do not adapt to self-reported learning styles.** Against: the learning-styles claim below.
8. **Watch for narrowing and misrouting.** Check transfer and conceptual items the system does not optimise for, and review learners routed to remediation repeatedly or advanced quickly on sparse evidence; if the system optimises a reward of its own, set it on unsupported learning, not engagement or in-system correctness ([RL reward misalignment failure modes](../claims/rl-reward-misalignment-failure-modes.md) [~W], an analytical chapter). Untested; from the earlier page's constraints.
9. **Check that the adaptation is actually enacted** (usage, teacher use of the data) before judging its effect. Bounded support from the personalised-learning fidelity claim below.

How far the neighbouring claims carry: the tutoring meta-analyses are about whole systems against non-individualised instruction, not about any one step above; the contingent-scaffolding evidence is mostly one-to-one human tutoring; the fidelity claim is a matched-comparison study of school-wide personalised learning, not of an adaptive rule.

## Fitting the design to a situation

Ask for four facts when the brief omits them: **what the system will adapt** (the support after a response, or only difficulty and order), **what evidence it adapts on** (responses to items, or self-reported preferences), **which outcome and horizon count** (the system's own items, an aligned test, a standardised test), and **who will look at the learner data**. The strongest evidence compares whole tutoring systems with conventional instruction; only a few studies compare adaptation with the same content in a fixed order.

| If the brief says… | Then change… | Basis |
|---|---|---|
| The alternative is conventional, non-individualised instruction or a textbook | Use a system that selects tasks and step-level feedback from each learner's responses; expect a gain on aligned tests, smaller on standardised ones, and none over a human tutor or a small group | [Intelligent tutoring systems improve achievement over non-individualised instruction](../claims/adaptive-learning-improves-outcomes.md) [+S] |
| The plan adapts only task difficulty, for young learners (early primary) | Add adaptive support (hints, worked steps, feedback tied to the error) rather than relying on difficulty alone; one trial found difficulty-only adaptation no better than a fixed version, and its mastery gate held learners back | [Adaptive task difficulty did not improve second-graders' posttest](../claims/task-difficulty-adaptation-no-learning-benefit-second-grade.md) [-M]; [The non-adaptive condition reached higher mastery](../claims/non-adaptive-condition-higher-mastery-probabilities.md) [-M] |
| University learners, a cumulative topic with checkable parts | Diagnose the parts with frequent short items and order each learner's path from the diagnosis; expect time saved as well as a modest post-test gain | [Personalized paths reduced learning time and improved post-test scores](../claims/personalized-paths-experiment-outcomes.md) [+M]; [Adaptive scaffolding policies improved posttest in a logic tutor](../claims/adaptive-icap-scaffolding-improves-posttest-logic-tutor.md) [+M] |
| A tutor (human or AI) responds to learners who are stuck | Change the support as the impasse persists: after a failed question, address the learner's error rather than repeating the question | [Questioning benefit decays with impasse depth](../claims/questioning-benefit-decays-with-impasse-depth.md) [+W]; [Repeating a scripted question lowers recovery](../claims/repeating-scripted-question-lowers-recovery.md) [+W] |
| An AI tutor is used, and the platform holds mastery and practice history | Pass the learner's mastery estimates for the skill and its prerequisites to the tutor, with an instruction to review weak prerequisites | [Student mastery context improved tutor metrics](../claims/student-context-personalization-improves-tutor-metrics.md) [+M]; [Generative AI tutors struggle to infer student knowledge](../claims/genai-tutors-struggle-infer-student-knowledge.md) [~M] |
| Learners improve quickly on a skill | Withdraw worked steps and hints as unassisted performance improves, checking unsupported items before each removal | [Guidance that helps novices can become redundant as expertise grows](../claims/expertise-reversal-effect.md) [~M]; [Fading support promotes the transfer of responsibility](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S] (near transfer) |
| Learners choose their own next tasks inside a mastery system | Constrain choice where a learner's selections are inefficient (for example, risk-averse overpractice of mastered skills) and leave efficient selectors free, rather than constraining everyone | [Constraints selectively affect inefficient strategies](../claims/constraints-selectively-affect-inefficient-strategies.md) [~W] (simulated learners, not tested with people) |
| The brief proposes adapting to learning styles or stated preferences | Adapt on responses to items and on prior knowledge instead | [Learning-styles matching does not improve learning](../claims/learning-styles-matching-does-not-improve-learning.md) [-S]; in one series of media experiments a voice-plus-diagram format lifted sensing-preference learners above intuitive-preference learners given text, so format, not the match, drove the difference ([Intuitive learners outperform sensing learners](../claims/intuitive-learners-outperform-sensing-learners.md) [-W]) |
| Routing depends on a knowledge-tracing or learner model | Treat estimates at the extremes (very low or very high predicted success) as least reliable: add a teacher check or an unassisted probe before repeated remediation or a fast skip | [Learner models are miscalibrated outside the data interval](../claims/learner-models-miscalibrated-outside-data-interval.md) [~M] |
| A vendor reports the model's predictive accuracy (AUC) | Ask whether attempts were ordered by time in the evaluation, and how the model is calibrated, not only its AUC; leakage inflates reported accuracy | [Violating temporal order inflates knowledge-tracing performance](../claims/pkt-temporal-causality-violation-inflates-performance.md) [~M]; [A transformer model won EDM Cup 2023 with an AUC of 0.79](../claims/transformer-kt-first-place-edm-cup-2023.md) [~M] |
| A school or adult programme adopts a platform | Plan for teachers to read and act on the diagnostic reports, and record use; judge the effect only where the adaptation was used | [Personalized learning effects vary with fidelity](../claims/personalized-learning-effects-vary-with-fidelity.md) [~M]; [Adult education programmes used learner data minimally](../claims/adult-ed-minimal-learner-data-use.md) [~M] |
| The system optimises its own reward (a reinforcement-learning policy) | Set the reward on learning measured without support, not on engagement or in-system correctness, and watch for learners who depend on scaffolding | [RL reward misalignment failure modes](../claims/rl-reward-misalignment-failure-modes.md) [~W] |

## Observation, state and explanation

An adaptive system observes **responses to particular items under stated conditions** (correctness, hint requests, time, attempts, which help was shown) and turns them into an inferred state: "has mastered this skill", "probability correct is 0.8", "ready for harder items". The inferred state is a model output, not an observation, and it inherits the model's errors. "Struggling" and "advanced" are labels for a learner's responses on this task, not traits. Record the items, the help given and the model's estimate side by side, so a routing decision can be checked against what was actually seen.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Correct on the system's items, fails a teacher's or standardised test of the same topic | System items narrower than the target; capability tied to the system's format or hints; forgetting between practice and test | Give an item on the same relation in a different format and without hints, soon after practice and again later; compare which conditions the system's items omitted. |
| Many hint requests, then correct answers | Learning from the hints; using hints to reach the answer without the reasoning; low confidence rather than low knowledge | Present a comparable item with hints withheld and ask for the first step; ask the learner why they asked for help. |
| Routed to remediation repeatedly on one skill | A prerequisite gap the system does not model; a skill estimate biased where the learner's data are sparse or extreme; items misaligned with the instruction; disengagement after repeated failure | Probe the prerequisite separately; have a teacher check two or three of the failed items with the learner; compare with other learners' results on the same items. |
| Advances quickly through items | Prior mastery of the target; guessing or gaming on easy items; criterion set too low | Give a few harder or transfer items unassisted; look at response times and error patterns on the items passed. |
| Gains in a school using the platform | The adaptation; extra practice time; the teacher's use of the data; selection of which classes used it | Compare classes with similar starting scores and similar time on task; record how fully the platform and its reports were used. |

These rows are proposals, untested with learners. A probe can shift confidence among explanations; one contrast does not identify a cause, and the probe is itself an exposure that can change the response. Record what remains unresolved rather than letting the system's estimate settle it.

## Evidence and qualifications

- [Intelligent tutoring systems improve achievement over non-individualised instruction](../claims/adaptive-learning-improves-outcomes.md) [+S]: two meta-analyses (`synthesis-experimental`, `heterogeneous-synthesis`). Across 107 effect sizes (14,321 participants), intelligent tutoring systems produced higher achievement than teacher-led large-group instruction (g = 0.42), non-tutoring computer-based instruction (g = 0.57) and textbooks or workbooks (g = 0.35), but no advantage over individual human tutoring (g = -0.11) or small-group instruction (g = 0.05). Across 50 controlled evaluations, the median effect over conventional instruction was 0.66 SD, depending strongly on whether tests were locally developed or standardised, and small where controls were nonconventional or implementations flawed. Both entries pass the judge, on abstracts. It supports individualised tutoring over non-individualised instruction on aligned achievement; it does not isolate adaptation from the rest of the system, does not show an advantage over adaptation by people, and reports no common horizon.
- [Contingent versus fixed support](../claims/contingent-scaffolding-improves-learning.md) [+M]: in one-to-one tutoring of long division with fourth and fifth graders (n = 8 per condition), fully contingent support beat fixed, moderate, partly contingent and no support on immediate and one-month follow-up tests; a within-subjects tutoring study reports similar immediate outcomes but better transfer for interactive, contingent tutoring; a synthesis of dynamic assessment ranks explicit strategy training above contingent scaffolding. This is the closest test here of adapting support to responses against fixed support, and it is small and mostly one-to-one; classroom and software contingency are not shown. Not settled: the entries could not be confirmed from abstracts.
- [Guidance and expertise](../claims/expertise-reversal-effect.md) [~M]: a review of cognitive load studies reports that supports such as worked examples and integrated explanations help novices on a task and can become redundant or depress performance as prior knowledge grows. It qualifies the relationship: adaptation that keeps support in place as performance improves can work against it. No effect size; not settled on its abstract.
- [Personalised learning and implementation](../claims/personalized-learning-effects-vary-with-fidelity.md) [~M]: in about 40 schools implementing personalised-learning practices (adaptive software among them), matched against virtual comparison groups (`controlled-nonrandom`), one-year effects were small (+0.09 SD mathematics, significant; +0.07 SD reading, not significant) and larger where implementation was reported as fuller or longer; the authors call that link suggestive, resting on self-report and a small district subsample. It qualifies the relationship: an adopted platform is not an enacted adaptation, and school-level averages are far below the tutoring syntheses' figures. Not yet checked against its source.
- [Learning-styles matching](../claims/learning-styles-matching-does-not-improve-learning.md) [-S]: a systematic review found almost no studies with the crossover design needed to test matching instruction to learning style, and judged the one candidate unconvincing; a randomised study with fifth graders found no style-by-modality interaction. It bears against adapting on self-reported style; it says nothing about adapting on responses or prior knowledge. Not settled on abstracts.
- [Learner-model calibration](../claims/learner-models-miscalibrated-outside-data-interval.md) [~W]: one analysis of two knowledge-tracing models on tutoring datasets reports that both were calibrated only in the range containing most of the data, overestimating learners when the probability of a correct answer was low and underestimating them when it was high. It limits the diagnostic step: a system's estimate for a learner at the extremes is least trustworthy where routing matters most. Associational, one study, no outcome for learners; not yet checked against its source.

- [Tutor moves at an impasse](../claims/questioning-benefit-decays-with-impasse-depth.md) [+W]: in logs of guided AI tutoring (6,163 impasse turns), the association of scripted and follow-up questions with recovery declined with each further impasse turn while addressing the learner's incorrect answer rose (AORs 0.78, 0.83 and 1.14 per turn); repeating a failed scripted question was followed by recovery in 28.1% of cases against 39.8% after switching to the error ([Repeating a scripted question lowers recovery](../claims/repeating-scripted-question-lowers-recovery.md) [+W]). It supports adapting support to the persistence of a difficulty within a task; it is associational, one study, measures recovery within the session rather than learning, and does not test adaptive against fixed sequencing.
- [What the adaptation changes](../claims/gain-time-constant-product-superior-forcing-function-amplitude.md) [+W]: one 1972 report on adaptive training of a single-axis manual tracking task (eight groups of eight) found the gain-effective time constant product slightly better than forcing-function amplitude as the adaptive variable, and [system compensation, aiding and quickening unsatisfactory](../claims/system-compensation-unsatisfactory-adaptive-variable.md) [~W]. The same report found [manual adaptation slightly superior to automatic adaptation](../claims/manual-adaptation-slightly-superior-automatic-adaptive-training.md) [~W], which the authors say could reflect different performance-measurement levels. It bears on the second condition (what the adaptation changes matters) in perceptual-motor training, not in academic content; no effect sizes.
- [Speed of acquisition and retention](../claims/learning-rate-retention-tradeoff.md) [~W]: a review of skill-learning research reports that slower adaptation processes were more robust over time and that slower learners in sequence learning retained more. It qualifies reading time saved to criterion as a gain: a design that moves learners on as fast as possible should check `delayed-retention`. Motor and sequence learning, cited second-hand, no effect size.

Keep the comparator (conventional, non-tutoring software, human tutor), the population band, the outcome instrument and its alignment, and the horizon with each finding. Do not set the meta-analytic g values beside the school-level SD gains as if they measured the same thing.

## The evidence by question

Each question below links a general claim that gathers the studies behind it into one table, one row per distinct study, with each study's design and effect as recorded and no averaged verdict (`eval/synthesis/adaptive-learning.json`, `scripts/synthesize_claim.py`). The count is of distinct studies across the claim and the narrower claims that bear on it.

- Does adaptive instruction raise achievement over non-individualised instruction or the same content in a fixed sequence? [Intelligent tutoring systems improve achievement over non-individualised instruction](../claims/adaptive-learning-improves-outcomes.md) [+S]: 10 distinct studies.
- What should adapt: the support given after a response, or only difficulty and order? [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [+S]: 20 distinct studies.
- When should support be withdrawn as the learner improves? [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~S]: 13 distinct studies.
- What should the adaptation be based on: responses, or learner styles and preferences? [Learning Styles Matching Does Not Improve Learning](../claims/learning-styles-matching-does-not-improve-learning.md) [-S]: 4 distinct studies.
- Can the system's diagnosis of the learner be trusted? [Current best learner performance models are severely biased outside the interval containing most of the data, hindering downstream adaptive policies and open learner models](../claims/learner-models-miscalibrated-outside-data-interval.md) [~M]: 7 distinct studies.
- What makes an adaptive design fail in practice? [Personalized Learning Effects Vary With Fidelity](../claims/personalized-learning-effects-vary-with-fidelity.md) [~M]: 4 distinct studies.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02: claims this page cited before the 2026-10-02 rewrite. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Re-read 2026-10-15: the claims below were read against the model above and do not bear on its relationship, steps or situation rows; each label says how far they reach. The others once listed here are now worked into the model.

- [Integrating cognitive scores with non-cognitive learner attributes enables the system to dynamically adapt AI-generated explanations in tone, depth and instructional strategy to individual learner performance](../claims/cognitive-noncognitive-integration-adapts-ai-explanations.md) [+W] — read 2026-10-15, does not bear on the relationship: a two-case demonstration that a system's explanations differ with a performance score, with no learner outcome measured.
- [Diminishing step sizes in stochastic approximation induce implicit averaging that eliminates noise effects in the long run](../claims/robbins-monro-diminishing-step-sizes-implicit-averaging.md) [+W] — read 2026-10-15, bears only on the estimation machinery behind an adaptive rule (a mathematical result about noisy sequential estimation), not on learners.
- [Iterate averaging with step sizes decreasing slower than O(1/n) converges at an optimal rate](../claims/polyak-juditsky-iterate-averaging-optimal-rate.md) [+W] — read 2026-10-15, as above: a convergence result for sequential estimation, no learners.
- [Propdec Colinear With Student Intercept](../claims/propdec-colinear-with-student-intercept.md) [+M] — read 2026-10-15, bears only on how a learner model represents individual differences (model fit across datasets); no routing decision or learner outcome, so it does not test the diagnostic step.
- [Kt Encoders Entity Isolated Deterministic Limits](../claims/kt-encoders-entity-isolated-deterministic-limits.md) [+W]
- [Adaptive G Ukt Competitive Performance Sparse Regimes](../claims/adaptive-g-ukt-competitive-performance-sparse-regimes.md) [+M]
- [Identifying learners' difficulties with visual displays is an important basis for selecting appropriate support procedures](../claims/learner-difficulties-basis-for-support-selection.md) [+M] — attached 2026-10-15 from Renkl et al. (2017), which proposed "Choose support procedures for visual displays based on knowledge of the difficulties learners have with them".
- [Intelligent tutoring systems with dynamic student modeling increase learning gains over regular instruction](../claims/its-dynamic-modeling-effective.md) [+W] — attached 2026-10-22 from Leonard Tetzlaff et al. (2021), which proposed "Measure relevant learner characteristics repeatedly during learning and adapt instruction systematically"; tests this page's relationship.

## Objective and learner-valued goal

The designer's objective in an adaptive design is usually a criterion on each skill in a map, reached in less time than a fixed path would take. What the learner values may differ: finishing the assigned work quickly, understanding why a method works, preparing for a particular examination, or not being held on one skill while classmates move on. Ask what the learner wants and why, record agreement or divergence as an observation, and do not infer it from time logged in the system.

For example, a secondary-school learner using an adaptive mathematics platform may value being ready for an end-of-year standardised examination, while the platform's objective is mastery of each skill on its own items. The tutoring synthesis above reports that gains depended on whether tests were locally developed or standardised, so the two aims may not move together. A design that serves both states which instrument and horizon count, adds unassisted examination-style items to the platform's checks, and tells the learner how the platform's mastery estimate relates to the examination.

## What would revise this model?

The expectation should weaken if, with comparable learners and content, individualised selection does not outperform the same content in a fixed sequence on independent outcomes, or if tutoring-system gains disappear on standardised measures and at a delay. If difficulty-only adaptation does as well as adaptation of support, the claim that support is the active part should be revised. If routing decisions based on a learner model are no better than a teacher's or the learner's own choices, the diagnostic step needs rethinking. If time saved, persistence or the learner's own goals move against achievement, the model is incomplete without them. Do not protect it by relabelling every failure as low fidelity or poor engagement.

Within-system performance, aligned achievement, standardised achievement, delayed retention, transfer and time to criterion are separate claims. The present evidence does not establish which adaptation target matters most, an optimal difficulty band or mastery threshold, or a forecast for an individual learner.

## Claims

- [Adaptive learning systems report academic performance gains of 15–25% and engagement increases of up to 40%](../claims/adaptive-learning-gains-15-25-percent.md) [~W]
- [Adaptive scaffolding policies (BKT and DRL) significantly improve posttest performance over a non-adaptive control in a logic ITS](../claims/adaptive-icap-scaffolding-improves-posttest-logic-tutor.md) [+W]
- [Adaptive fading with periodic reinforcement yields higher independence than fixed-high or linear-decay scaffolding in simulation](../claims/adaptive-fading-beats-fixed-and-linear-scaffolding.md) [~W]
- [The survey reports, citing Desmarais and Baker, that students using the BKT-sequence recommendation algorithm solved more difficult exercises, obtained higher performance and spent more time in the system than students using the traditional approach.](../claims/bkt-sequence-recommendation-students-solved-harder-exercises.md) [+W]
- [Case study shows tutor scaffolding lowers estimated task difficulty after errors while student ability rises steadily](../claims/case-study-scaffolding-lowers-difficulty-ability-rises.md) [~W]
- [GenAI can provide personalised feedback in group work, but the depth of personalisation is contested](../claims/genai-personalised-feedback-contested-depth.md) [~W]
- [The system's generated practice trajectories align with learner skill levels at a peak cosine similarity of 0.962 ± 0.014 at the primary difficulty level](../claims/cmt-alignment-cosine-similarity-0962.md) [~W]
- [LMS process indicators documented adaptive engagement during the eight-week intervention, with most experimental students reaching mastery by unit end](../claims/lms-process-indicators-pilot.md) [+W]
- [Learner engagement was strengthened when the AI tutor adapted to learners' pace and prior knowledge](../claims/ai-tutor-pace-adaptation-strengthened-engagement.md) [+W]
- [One-shot path generation raises Validity but lowers Adaptivity and Efficiency relative to step-by-step interaction](../claims/one-shot-generation-lowers-adaptivity.md) [~W]
- [Students in the non-adaptive condition reached significantly higher average mastery probabilities than students in the adaptive condition](../claims/non-adaptive-condition-higher-mastery-probabilities.md) [-W]
- [Emerging evidence indicates generative AI tutors currently struggle to accurately infer student knowledge at the outset of an interaction or as the activity progresses](../claims/genai-tutors-struggle-infer-student-knowledge.md) [-W]
- [In a randomized experiment, personalized paths reduced learning time by 22.0% and improved post-test scores versus a fixed sequence](../claims/personalized-paths-experiment-outcomes.md) [+M]
- [Personalized paths reduced self-reported cognitive load on all six adapted NASA-TLX dimensions with large effect sizes](../claims/personalized-paths-lower-cognitive-load.md) [+W]
- [Tutors showed significant pre-to-post gains in both conceptual knowledge and procedural skill after teaching with adaptive follow-up questioning](../claims/significant-prepost-gains-ckt-pst.md) [~W]
- [Providing the tutor with student mastery and practice-history context improved engagement and next-item correctness](../claims/student-context-personalization-improves-tutor-metrics.md) [+W]
- [Adaptive task difficulty in an ITS did not improve second-graders' mathematics posttest performance compared with an identical non-adaptive ITS](../claims/task-difficulty-adaptation-no-learning-benefit-second-grade.md) [-W]
- [Reinforcement learning in adaptive educational systems faces sample inefficiency and reward-design instability, motivating hybrid RL-ML approaches](../claims/rl-sample-inefficiency-reward-design-limits.md) [~W]
- [An adaptive AI-based STEM instructional program produced statistically significant differences favoring the experimental group across all deep learning dimensions in sixth-grade science](../claims/adaptive-ai-stem-deep-learning-gains-sixth-grade.md) [+W]
- [Meta-analytic evidence reviewed reports medium-to-large positive effects of AI-enabled adaptive learning on cognitive outcomes (g = 0.50–0.70)](../claims/ai-adaptive-learning-medium-large-effects-reviewed.md) [+M]
- [Adaptive versus non-adaptive ITS condition showed no significant differences in mental effort, subjective difficulty, or enjoyment](../claims/adaptive-its-no-difference-cognitive-load-enjoyment.md) [~W]
- [Reviewed literature identifies personalisation, adaptive support, rapid feedback, and teacher-facing automation as recurring pedagogical opportunities of AI in mathematics education](../claims/ai-math-pedagogical-opportunities-personalisation-feedback.md) [+W]
- [The EEG-adaptive exercise condition produced significantly higher cognitive engagement during training than the unrestricted chatbot condition (p = .018), and was the only condition above the 0.5 baseline](../claims/adaptive-mode-higher-eeg-engagement.md) [+W]
- [Effectiveness of AI-driven personalized learning is context-dependent, with CS and Mathematics students showing contrasting engagement and performance trajectories](../claims/context-sensitive-personalization-disciplinary-backgrounds.md) [~W]
- [A multi-site randomized controlled trial found Woot Math's adaptivity contributed significant effects in learning and retention](../claims/woot-math-rct-adaptivity-significant-effects.md) [+W]
- [A technical review reports that one reinforcement-learning adaptive platform raised average course grades by 12%, task completion by 20% and cut dropout by 10% against static curricula (uncontrolled case report)](../claims/rl-adaptive-system-grade-engagement-gains.md) [+W]
- [A stochastic (exploration) router yields a higher exercise conversion rate than the static baseline, while the greedy router is comparable](../claims/stochastic-router-higher-conversion-rate.md) [+M]
- [Adult education programs used product-generated learner data minimally, mostly tracking usage time rather than diagnosing struggles](../claims/adult-ed-minimal-learner-data-use.md) [-W]
- [The DRL policy produced a significantly different scaffolding distribution than Control and BKT, favoring Guided examples (60%) and avoiding Buggy examples (4%)](../claims/drl-policy-favors-guided-examples-distribution.md) [+W]
- [In a classroom study of the G4L system, the Bayesian knowledge propagation algorithm demonstrated the highest knowledge gains, and log-data analysis revealed significant differences in self-regulated learning patterns between learners](../claims/bn-highest-knowledge-gains-g4l.md) [~W]
- [Individualized Knowledge Tracing parameters fit student data significantly better and change mastery-learning practice decisions for many students](../claims/individualized-kt-parameters-change-practice-decisions.md) [~W]
- [Exploratory ANCOVA controlling for mastery probability favored the adaptive condition, but is not interpretable as a causal treatment effect](../claims/mastery-probability-covariate-ancova-favors-adaptive.md) [~W]
- [A multi-skill prior strategy yielded lower prediction error in 33 of 42 problem sets](../claims/multi-skill-prior-strategy-best-prediction-error.md) [~W]
- [Adaptive scaffolding shows descriptively higher effects than adaptable scaffolding in simulation-based learning, though the difference is not statistically significant](../claims/adaptive-scaffolding-descriptively-higher-than-adaptable.md) [+W]
- [Adaptable task progression is descriptively more beneficial than fixed task progression in simulation-based learning](../claims/adaptable-task-progression-higher-effects.md) [+W]
- [Technology-supported adaptive teaching units showed significant learning gains, larger for low-prior-knowledge students and high implementation fidelity](../claims/adaptive-teaching-units-learning-gains-moderated.md) [+W]
- [System-controlled adaptive instruction does not necessarily yield higher transfer than nonadaptive static approaches](../claims/system-control-not-superior-transfer.md) [~W]
- [ITS augmentation: meta-analyses find medium to large learning benefits of ITS over unsupported learning and small to medium gains over less adaptive computer-assisted learning](../claims/its-augmentation-benefits-over-unsupported-learning.md) [+M]

## Related Principles
- [Cognitive Load Management](cognitive-load-management.md) — adaptation is the primary mechanism for keeping intrinsic load matched to learner expertise over time
- [Assessment for Learning](assessment-for-learning.md) — supplies the continuous diagnostic evidence that any adaptive decision depends on
- [Competency-Based Learning & Assessment](competency-based-assessment.md) — provides the mastery criteria that gate progression in adaptive designs
- [Active Learning](active-learning.md) — adaptive systems still require learners to do generative work; adaptation of difficulty does not replace engagement
- [Mastery Learning](mastery-learning.md)
- [Knowledge Tracing Learner Modeling Task](../theories/knowledge-tracing-learner-modeling-task.md)
- [Knowledge Tracing Driven Exercise Recommendation](../strategies/knowledge-tracing-driven-exercise-recommendation.md)
- [Adaptive Difficulty](../elements/adaptive-difficulty.md)
- [Engagement](engagement.md)

## Examples

- [Four-layer system architecture for intelligent oral diagnosis and adaptive training](../elements/four-layer-oral-diagnosis-system-architecture.md)
- [Mask the reinforcement learning policy's action space to a zone-of-proximal-development difficulty band (success probability 0.4–0.8)](../strategies/zpd-masked-rl-content-sequencing.md)
- [Use shaped-spectrum filtered error for rapid adaptive logic response](../strategies/shaped-spectrum-filtered-error-adaptive-logic.md)
- [Four ecosystem recommendations: experiment with currency forms, protect time for inquiry, include everyone in team learning, and invest in adaptive platforms](../strategies/four-micro-credential-ecosystem-recommendations.md)
- [Use early student-model predictions to identify at-risk students and adapt pedagogical strategy during tutoring](../strategies/early-prediction-adaptive-pedagogical-strategy.md)
- [Use in-game scaffolds with automatic feedback displays in math game tasks, monitoring scaffold use against mastery data](../strategies/in-game-scaffolds-with-usage-tracking.md)
- [Use AI to support autonomy-supportive task adaptation in physical education rather than algorithmic exercise prescription](../strategies/autonomy-supportive-ai-task-adaptation-pe.md)
- [cc-self-train adaptive learning system: a three-layer hook-based engagement observation and scaffolding adjustment mechanism](../designs/cc-self-train-adaptive-learning-system.md)
- [Use traced error causes as personalized intervention recommendations in online learning systems](../strategies/error-cause-tracing-for-personalized-recommendations.md)
- [Select iteration coefficients according to the proved convergence condition when implementing stochastic approximation](../strategies/coefficient-selection-strategy.md)
- [Iteration-coefficient sequences as the controllable design element of stochastic approximation](../elements/iteration-coefficient-sequence.md)
- [Design AI learning systems for inspectable, contestable use: provenance, represented uncertainty, user control and epistemic plurality](../strategies/design-contestable-ai-provenance-plurality.md)
- [Self-improving mechanism: learning strategy-selection criteria from student model states by concept learning from examples](../designs/strategy-selection-criteria-from-student-model-states.md)
- [For young learners, adapt instructional support level rather than only task difficulty, and investigate adaptive features in isolation](../strategies/adapt-support-not-just-difficulty-young-learners.md)
- [Use strategy-based evidence models to trigger adaptive scaffolding toward more productive problem-solving strategies](../strategies/strategy-evidence-models-trigger-adaptive-scaffolding.md)

### Validated
- **[ASSISTments](https://www.assistments.org)** — Free web-based math platform (grades 6–12) that adapts problem selection and hint delivery based on item-level responses. Randomized studies across Maine schools showed significant homework-related learning gains over business-as-usual conditions (Roschelle et al., 2016, *AERJ*).
- **[Carnegie Learning MATHia](https://www.carnegielearning.com/solutions/math/mathia/)** — Cognitive-tutor-based adaptive math system using a cognitive model of learner knowledge to select problems and tailor step-level hints. A large RAND study (Pane et al., 2014) found roughly doubled learning-growth effects in second-year algebra relative to conventional instruction.
- **[Khan Academy](https://www.khanacademy.org)** — Mastery-based practice in mathematics that adapts task assignment to demonstrated skill levels, with mastery gates before progression.

### Illustrative
- **[Adaptive Difficulty](../elements/adaptive-difficulty.md)** — The core element: dynamically raising or lowering task difficulty based on performance signals such as accuracy, latency, and error patterns.
- **[Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md)** — Combines mastery criteria with adaptive routing so learners who fail an assessment are routed to remediation rather than the next unit.
- **[Duolingo](../products/duolingo.md)** — Language-learning app that adapts item scheduling using a spaced-repetition and learner-error model, reinserting items the learner is predicted to forget.

## Key Sources
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197-221. [doi:10.1080/00461520.2011.611369](https://doi.org/10.1080/00461520.2011.611369)
- Kulik, J. A., & Fletcher, J. D. (2016). Effectiveness of intelligent tutoring systems: A meta-analytic review. *Review of Educational Research, 86*(1), 42–78. [doi:10.3102/0034654315581420](https://doi.org/10.3102/0034654315581420)
- Ma, W., Adesope, O. O., Nesbit, J. C., & Liu, Q. (2014). Intelligent tutoring systems and learning outcomes: A meta-analysis. *Journal of Educational Psychology, 106*(4), 901–918. [doi:10.1037/a0037123](https://doi.org/10.1037/a0037123)
- Corbett, A. T. (2001). Cognitive computer tutors: Solving the two-sigma problem. *User Modeling 2001*, 137–147. [doi:10.1007/3-540-44566-8_14](https://doi.org/10.1007/3-540-44566-8_14)
- Pane, J. F., Steiner, E. D., Baird, M. D., Hamilton, L. S., & Pane, J. D. (2017). Informing progress: Insights on personalized learning implementation and effects. RAND Corporation. [https://www.rand.org/pubs/research_reports/RR2042.html](https://www.rand.org/pubs/research_reports/RR2042.html) [doi:10.7249/rr2042](https://doi.org/10.7249/rr2042)
- Pane, J. F., Steiner, E. D., Baird, M. D., & Hamilton, L. S. (2015). *Continued progress: Promising evidence on personalized learning*. RAND Corporation. [doi:10.7249/rr1365](https://doi.org/10.7249/rr1365)
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
- Norman, D. A.; And Others. (1972). Adaptive Training of Manual Control: 1. Comparison of Three Adaptive Variables and Two Logic Schemes. Life Sciences, Inc. https://eric.ed.gov/?id=ED059585 [doi:10.1037/e426822004-001](https://doi.org/10.1037/e426822004-001)
- Wolff, Hans. (1970). On Stochastic Approximation. https://eric.ed.gov/?id=ED051258
- Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569
- Jia Nan, Su Weitao, Xian Junrui, Zou Shijia, Xia Yixue. (2026). Adaptive G-UKT: a unified probabilistic framework for knowledge tracing via adaptive graph topology learning and uncertainty-aware Gaussian embeddings. Scientific Reports. https://doi.org/10.1038/s41598-026-50711-y

<!-- deprecated 2026-10-02: superseded by the conditional model above; the earlier Description and Implications, verbatim.

## Description
Adaptive learning adjusts instruction — task difficulty, pacing, content sequencing, and support level — in response to ongoing evidence of each learner's performance, rather than presenting a fixed path to all learners. Adaptation ranges from simple branching and difficulty tuning to algorithmic mastery decisions in intelligent tutoring systems. The core recommendation: use continuous assessment data to keep every learner working on tasks they cannot yet do reliably but can reach with appropriate support.

## Implications

Adaptive designs operationalize the zone of proximal development: tasks are matched to current competence so learners are neither bored by redundancy nor overwhelmed by overload. Meta-analyses of intelligent tutoring systems show performance gains over conventional instruction, often approaching the effectiveness of human tutoring [Intelligent tutoring systems outperform large-group instruction.](../claims/expertise-reversal-effect.md) [+S]. Adaptation depends on accurate diagnosis, so embedded assessment must be frequent and fine-grained [Formative assessment information improves instructional decisions.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]. Adaptation is not a substitute for guidance: as learner expertise grows, the adaptive system must reduce scaffolding, or the same support that helped novices becomes redundant and harmful [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]. Systems that adapt only difficulty without adapting support quality tend to produce weaker gains than those that also adapt hints, feedback, and task sequencing.

### Context
#### Requirements
- A mechanism for continuous diagnosis ([Assessment](../elements/assessment.md) or [Assess Performance](../elements/assess-performance.md)) — adaptation is only as good as the evidence driving it
- A bank or sequence of tasks at varied difficulty ([Adaptive Difficulty](../elements/adaptive-difficulty.md)) — the system needs somewhere to move the learner
- Mastery or competence criteria that gate progression ([Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md)) — without explicit criteria, "adaptation" drifts
- Responsive feedback tied to the diagnosis ([Practice](../elements/practice.md) with task- and process-level feedback) — adaptation without informative feedback is just reordering

#### Constraints
- Less effective when the domain lacks decomposable, assessable sub-skills — adaptation algorithms struggle with open-ended, ill-structured tasks
- Can narrow learning to what is easily measured, over-drilling measurable skills while neglecting transfer and conceptual understanding
- Algorithmic mastery decisions can misclassify learners when assessments are noisy or sparse, producing premature advancement or unnecessary remediation
- Adaptation to learner "preferences" or self-reported styles is not supported by evidence and can reduce effectiveness [Learning-styles matching does not improve outcomes.](../claims/intuitive-learners-outperform-sensing-learners.md) [X]

### Target Learners
- Heterogeneous groups where a single fixed pace leaves some learners lost and others unchallenged
- Struggling learners who need more practice and lower entry difficulty than a fixed sequence provides
- Advanced learners who benefit from acceleration past content they have already mastered
- Effects diminish when all learners are at similar competence — uniform groups gain little from adaptation [~M]

### Target Learning Objectives
- Procedural fluency and skill automatization with well-defined performance criteria
- Mastery of hierarchical knowledge structures (mathematics, programming, language mechanics)
- Efficient use of practice time — minimizing time on already-mastered content
- Sustained productive difficulty rather than frustration or boredom

### Theory
#### Supporting
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — matching task difficulty to current expertise keeps intrinsic load within working-memory limits
- [Expertise Reversal Effect](../theories/expertise-reversal-effect.md) — the core theoretical justification: optimal instruction differs by expertise level, so a single fixed path is wrong for most learners
- [Self-Regulated Learning](../theories/self-regulated-learning.md) — adaptive systems externalize the monitoring-and-adjustment cycle; well-designed systems can also hand that cycle back to learners
- [Information Processing Theory](../theories/information-processing-theory.md) — diagnosis of current knowledge state allows instruction to target exactly the missing components

#### Contradicting / Qualifying
- [Constructivism](../theories/constructivism.md) — algorithmic adaptation can over-script the learning path, reducing learner agency and the productive struggle that generates understanding; adaptation should leave room for learner choice and exploration

### Claims

- [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M] — adaptive systems must fade support as competence grows, or adaptation backfires
- [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S] — adaptation should progressively withdraw scaffolding, not just adjust difficulty
- [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S] — the diagnostic information driving adaptation should feed task- and process-level feedback
- [Example–problem sequences reduce cognitive load.](../claims/worked-example-problem-sequences.md) [+M] — adaptive sequencing can interleave worked examples with problems based on performance

-->

<!-- merged 2026-10-05 from patterns/adaptive-learning ("Adaptive Learning"), misfiled as a pattern and a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Adaptive Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 review), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Adaptive learning is the short-form canonical pattern for adjusting pacing, difficulty, or support based on learner performance.

## Design

### Elements Used
- [Adaptive Learning](../elements/adaptive-learning.md)
- [Immediate Feedback](../elements/immediate-feedback.md)

## Claims
- [Faster rate of learning may be negatively related to long-term retention (efficiency-effectiveness trade-off)](../claims/learning-rate-retention-tradeoff.md) [~W]

## Related Patterns
- [Mastery Learning](../patterns/mastery-learning.md)

## Key Sources
- Pane, J. F., Steiner, E. D., Baird, M. D., & Hamilton, L. S. (2015). *Continued progress: Promising evidence on personalized learning*. RAND Corporation.
-->

<!-- merged 2026-10-07 from principles/adaptive-learning-consistent-with-cognitive-structure ("Adaptive Learning Consistent with Knowledge Level and Knowledge Structure"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Adaptive Learning Consistent with Knowledge Level and Knowledge Structure

> **Principle** · [All principles](index.md)
> **Evidence** · no claims cited

## Description
The survey argues that because students' cognitive structures include both their knowledge level and the knowledge structure of learning items (e.g., prerequisites), "adaptive learning should maintain consistency with both students’ knowledge level and the latent knowledge structure." It cites CSEAL, which uses DKT to trace knowledge states, a knowledge-structure navigation algorithm for logical learning paths, and an actor-critic algorithm to decide what to learn next.

## Design Implications

### Context
#### Requirements
- A KT model tracing each student's evolving knowledge state
- A representation of prerequisite relations among learning items to constrain learning paths
#### Constraints
- The survey states that existing adaptive learning methods often focus separately on either students' knowledge levels or the knowledge structure of learning items

### Target Learners
- Students in adaptive learning systems, including MOOCs and programming tutors

### Target Learning Objectives
- Following individualized, logically ordered learning paths until each rule or concept is mastered

### Claims
- 

## Related Principles
- [Adaptive Learning](adaptive-learning.md)
- [Mastery Learning](mastery-learning.md)
- [Knowledge Tracing Learner Modeling Task](../theories/knowledge-tracing-learner-modeling-task.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
-->

<!-- merged 2026-10-07 from principles/gain-then-time-constant-adaptive-progression ("Sequence adaptive difficulty by increasing gain first, then lengthening the effective time constant"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Sequence adaptive difficulty by increasing gain first, then lengthening the effective time constant

> **Principle** · [All principles](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article recommends that at the beginning of training a low value for both gain and effective time constant be provided. Based upon student improvement, gain would then be increased to provide a more difficult task, followed by increasing te to make the task progressively more difficult. The rationale is that low gain lets trainees learn the gross pattern of control movement without sorting out random movements, and short time constants permit immediate feedback for adjusting control inputs.

## Design Implications

### Context
#### Requirements
- Gain must be low enough early in training so the trainee can learn the gross pattern of control movement without sorting out random, erratic movements
#### Constraints
- The effect of gain is particularly evident during early training trials with the effect decreasing as learning progresses

### Target Learners
- novice manual-control trainees

### Target Learning Objectives
- learning spatial and temporal patterns of control movement

### Claims

- [Gain-effective time constant product is slightly superior to forcing function amplitude as an adaptive variable](../claims/gain-time-constant-product-superior-forcing-function-amplitude.md) [+W]
- [Manual adaptation is slightly superior to automatic adaptation in adaptive training of manual control](../claims/manual-adaptation-slightly-superior-automatic-adaptive-training.md) [+W]
- [System compensation as implemented is not a satisfactory adaptive variable](../claims/system-compensation-unsatisfactory-adaptive-variable.md) [+W]

## Related Principles
- 

## Examples

- [Use shaped-spectrum filtered error for rapid adaptive logic response](../strategies/shaped-spectrum-filtered-error-adaptive-logic.md)
- [Mask the reinforcement learning policy's action space to a zone-of-proximal-development difficulty band (success probability 0.4–0.8)](../strategies/zpd-masked-rl-content-sequencing.md)

## Key Sources
- Norman, D. A.; And Others. (1972). Adaptive Training of Manual Control: 1. Comparison of Three Adaptive Variables and Two Logic Schemes. Life Sciences, Inc. https://eric.ed.gov/?id=ED059585 [doi:10.1037/e426822004-001](https://doi.org/10.1037/e426822004-001)
-->

<!-- merged 2026-10-07 from principles/multi-objective-exercise-recommendation-objectives ("Multi-Objective Exercise Recommendation: Review and Explore, Smooth Difficulty, Engagement"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Multi-Objective Exercise Recommendation: Review and Explore, Smooth Difficulty, Engagement

> **Principle** · [All principles](index.md)
> **Evidence** · no claims cited

## Description
The survey reports three objectives proposed by Huang et al. to go beyond assigning non-mastered exercises: "review and explore , smoothness of difficulty level and student engagement ." Review and explore reinforces non-mastered concepts with timely reviews while keeping opportunities to explore new knowledge; smooth difficulty keeps consecutive exercises within a small difficulty range; engagement aligns recommended exercises with student preferences. These objectives are optimized in a multi-objective deep reinforcement learning (DRE) framework.

## Design Implications

### Context
#### Requirements
- Traced knowledge states plus reward functions that capture and quantify each of the three objectives, as in the DRE framework
#### Constraints
- The survey reports only that DRE can effectively learn from learning records to optimize multiple objectives; no magnitude of learning benefit is given

### Target Learners
- Students receiving exercise recommendations in online intelligent education systems

### Target Learning Objectives
- Reviewing non-mastered concepts, exploring new knowledge, and sustaining enthusiasm during learning

### Claims
- 

## Related Principles
- [Knowledge Tracing Driven Exercise Recommendation](../strategies/knowledge-tracing-driven-exercise-recommendation.md)
- [Adaptive Difficulty](../elements/adaptive-difficulty.md)
- [Engagement](engagement.md)

## Examples
-

## Key Sources
- Shuanghong Shen, Qi Liu, Zhenya Huang, Yonghe Zheng, Minghao Yin, Minjuan Wang, and Enhong Chen. (2021). A Survey of Knowledge Tracing: Models, Variants, and Applications. https://arxiv.org/abs/2105.15106
-->

<!-- merged 2026-10-14 from principles/sequential-noisy-estimation-principle ("Use stochastic approximation for sequential parameter estimation when observations are noisy and each observation is costly"), folded in as a narrower page that rested on two studies or fewer after an evidence search (upgrade_worklist.py, 2026-10-14): its body as it stood. Its bullets this page lacked were added above.

# Use stochastic approximation for sequential parameter estimation when observations are noisy and each observation is costly

> **Principle** · [All principles](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article supports using the Robbins-Monro procedure in settings where a parameter must be estimated sequentially from noisy observations, as in adaptive measurement of learner ability. Because the procedure updates after each observation, it suits contexts where observations are costly and convergence must be guaranteed. The article's contribution is the condition the iteration coefficients must satisfy for such sequential estimation to converge.

## Design Implications

### Context
#### Requirements
- Iteration coefficients chosen to satisfy the article's necessary and sufficient convergence condition
#### Constraints
- The guarantee is mathematical; the article reports no instructional trial of the procedure

### Target Learners
- learners undergoing sequential or adaptive assessment

### Target Learning Objectives
- accurate estimation of learner ability or learning parameters

### Claims

- Convergence Condition Stochastic Approximation [+M]
- [Diminishing step sizes in stochastic approximation induce implicit averaging that eliminates noise effects in the long run](../claims/robbins-monro-diminishing-step-sizes-implicit-averaging.md) [+W]
- [Iterate averaging with step sizes decreasing slower than O(1/n) converges at an optimal rate](../claims/polyak-juditsky-iterate-averaging-optimal-rate.md) [+W]

## Related Principles
- 

## Examples

- [Select iteration coefficients according to the proved convergence condition when implementing stochastic approximation](../strategies/coefficient-selection-strategy.md)
- [Iteration-coefficient sequences as the controllable design element of stochastic approximation](../elements/iteration-coefficient-sequence.md)

## Key Sources
- Wolff, Hans. (1970). On Stochastic Approximation. https://eric.ed.gov/?id=ED051258
-->

<!-- merged 2026-10-14 from principles/avoid-student-intercepts-for-transfer ("Avoid fixed or random student intercepts in learner models intended to transfer to new student populations"), folded in as a narrower page that rested on two studies or fewer after an evidence search (upgrade_worklist.py, 2026-10-14): its body as it stood. Its bullets this page lacked were added above.

# Avoid fixed or random student intercepts in learner models intended to transfer to new student populations

> **Principle** · [All principles](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article argues that to be maximally applicable, a learner model needs to adapt to student differences without requiring student parameters estimated from prior data. The main-comparison models avoid student parameters as a partial solution to the cold start problem that occurs when models are transferred between different populations of students, instead using dynamic adaptive features like propdec at the student level.

## Design Implications

### Context
#### Requirements
- A dynamic adaptive feature (e.g., propdec or logitdec) that captures student variability from the practice sequence itself
#### Constraints
- A pretest could be used to estimate student-level intercept values, but this possibility is not addressed in the article

### Target Learners
- new students in populations unseen during model fitting

### Target Learning Objectives
- generalizable prediction of student performance in adaptive systems

### Claims
- [Propdec Colinear With Student Intercept](../claims/propdec-colinear-with-student-intercept.md) [+M]

## Related Principles
- 

## Examples
-

## Key Sources
- Philip I. Pavlik, Jr., Luke G. Eglington, and Leigh M. Harrell-Williams. (2021). Logistic Knowledge Tracing: A Constrained Framework for Learner Modeling. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2021.3128569
-->

<!-- merged 2026-10-15 from principles/uncertainty-aware-knowledge-states-for-adaptive-decisions ("Model learner knowledge states as distributions with explicit uncertainty so downstream systems can perform confidence-aware inference and adaptive decision-making"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Model learner knowledge states as distributions with explicit uncertainty so downstream systems can perform confidence-aware inference and adaptive decision-making

> **Principle** · [All principles](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article argues that representing latent learner states probabilistically, rather than as deterministic point vectors, lets adaptive systems act on both the state estimate and its reliability: modeling latent state updates over concept graphs means "downstream systems can perform confidence-aware inference and adaptive decision-making". In Adaptive G-UKT this is realized through Gaussian embeddings whose diagonal covariance encodes epistemic uncertainty and gates augmentation during contrastive training.

## Design Implications

### Context
#### Requirements
- A sequential latent state estimation model that outputs both a posterior mean and an uncertainty estimate for each concept
#### Constraints
- The article presents this as a design rationale for knowledge tracing systems; it does not report a controlled study of downstream adaptive decisions

### Target Learners
- learners interacting with online learning platforms and adaptive inference systems

### Target Learning Objectives
- reliable estimation of evolving learner competency to guide adaptive item selection and inference

### Claims
- [Kt Encoders Entity Isolated Deterministic Limits](../claims/kt-encoders-entity-isolated-deterministic-limits.md) [+W]
- [Adaptive G Ukt Competitive Performance Sparse Regimes](../claims/adaptive-g-ukt-competitive-performance-sparse-regimes.md) [+M]

## Related Principles
- 

## Examples

- [Design AI learning systems for inspectable, contestable use: provenance, represented uncertainty, user control and epistemic plurality](../strategies/design-contestable-ai-provenance-plurality.md)

## Key Sources
- Jia Nan, Su Weitao, Xian Junrui, Zou Shijia, Xia Yixue. (2026). Adaptive G-UKT: a unified probabilistic framework for knowledge tracing via adaptive graph topology learning and uncertainty-aware Gaussian embeddings. Scientific Reports. https://doi.org/10.1038/s41598-026-50711-y
-->
