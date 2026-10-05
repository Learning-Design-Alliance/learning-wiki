---
type: principle
id: adaptive-learning
title: Adaptive Learning
description: "When learners on a cumulative, decomposable task start from different observed responses, choosing each next task, hint or check from the learner's own recent responses (rather than one fixed path) may improve aligned achievement, conditional on how well the responses diagnose the learner, what the adaptation changes, and whether support is withdrawn as performance grows."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-02
---

# Adaptive Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 10 claims (5 for, 3 mixed, 2 against) · 18 studies (7 causal, 5 quant-synthesis, 4 review, 1 associational, 1 qualitative), `q2`–`q4` · 5 of 18 report an effect size · 5 claims rest on one study

## Conditional relationship

Where learners in one course start from different observed responses on a task whose parts can be checked separately (cumulative `procedure`, `principle` or `verbal-association` goals; mathematics, programming and language mechanics are the usual cases), selecting each learner's next task, hint, feedback or check from that learner's recent responses, instead of moving everyone through one fixed sequence, is expected to raise achievement on an aligned measure (`general-achievement`, mostly `immediate` or end-of-course). The relationship is conditional on four things: the responses must diagnose what the learner can and cannot yet do on the target task; the adaptation must change something that matters for learning (the support given or the task chosen, not only its order); support must be reduced as the learner's unassisted performance improves; and the outcome and horizon must be stated, since aligned test scores, standardised achievement, `delayed-retention`, `far-transfer` and `learning-time` move separately.

This page owns the general relationship: individualised selection against a fixed path, whoever or whatever does the selecting. Three converted pages hold narrower models inside it. [Scaffolding](scaffolding.md) treats support versus none during an attempt, and its model of contingent support is the within-task form of adaptation. [Mastery Learning](mastery-learning.md) treats one adaptive rule, a gate with correction and a recheck before advancing. [Formative Assessment](formative-assessment.md) treats the interpretation of evidence and the contingent action that any adaptive decision depends on. This page does not repeat them. The [adaptive learning pattern](../patterns/adaptive-learning.md) is a short, unconverted stub.

**No claim in the wiki tests adaptation itself against the same content in a fixed sequence at scale.** The strongest evidence below compares intelligent tutoring systems, which bundle adaptation with step-level feedback, practice and a model of the task, with conventional instruction; it shows the bundle can help, not which part of it does.

## Default design, while the relationship is untested

The page's earlier guidance, kept as a concrete default a designer can act on and revise. Each step is a design proposal, with its evidence status beside it.

1. **Decide what the adaptation is for and how it will be judged.** Name the capability, the representative instrument, the criterion and the horizon before choosing a system or rule. Untested here; it follows from the outcome dependence in the tutoring meta-analyses below (gains depended on whether tests were locally developed or standardised).
2. **Build a diagnosis the adaptation can rest on.** Frequent, fine-grained checks on the parts of the task, using [assessment](../elements/assessment.md) or [assess performance](../elements/assess-performance.md). Untested as a step; the earlier page's requirement. The learner-model claim below shows that a model's predictions can be biased where it has little data, so treat each adaptive decision as an inference with error.
3. **Provide somewhere to move the learner**: a bank or sequence of tasks at varied difficulty ([adaptive difficulty](../elements/adaptive-difficulty.md)), including worked or partly worked examples for low starting responses. Untested here; from the earlier page.
4. **Adapt the support, not only the difficulty or order.** Give hints and task- and process-level [feedback](../elements/feedback.md) tied to what the response showed, raising support after an error and lowering it after success. Supported in one-to-one tutoring by the contingent-scaffolding claim; the earlier page's statement that difficulty-only adaptation gives weaker gains is not tested by any claim here.
5. **Gate progression on an explicit criterion** with correction and a recheck ([adaptive mastery learning](../elements/adaptive-mastery-learning.md)), as modelled in [Mastery Learning](mastery-learning.md). Evidence is on that page.
6. **Withdraw support as unassisted performance grows**, checking on unsupported items before removing it. Bounded support from the expertise-reversal claim below (a review; abstract not confirmed).
7. **Do not adapt to self-reported learning styles.** Against: the learning-styles claim below.
8. **Watch for narrowing and misrouting.** Check transfer and conceptual items the system does not optimise for, and review learners routed to remediation repeatedly or advanced quickly on sparse evidence. Untested; from the earlier page's constraints.
9. **Check that the adaptation is actually enacted** (usage, teacher use of the data) before judging its effect. Bounded support from the personalised-learning fidelity claim below.

How far the neighbouring claims carry: the tutoring meta-analyses are about whole systems against non-individualised instruction, not about any one step above; the contingent-scaffolding evidence is mostly one-to-one human tutoring; the fidelity claim is a matched-comparison study of school-wide personalised learning, not of an adaptive rule.

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

- [Adaptive learning improves outcomes](../claims/adaptive-learning-improves-outcomes.md) [+S]: two meta-analyses (`synthesis-experimental`, `heterogeneous-synthesis`). Across 107 effect sizes (14,321 participants), intelligent tutoring systems produced higher achievement than teacher-led large-group instruction (g = 0.42), non-tutoring computer-based instruction (g = 0.57) and textbooks or workbooks (g = 0.35), but no advantage over individual human tutoring (g = -0.11) or small-group instruction (g = 0.05). Across 50 controlled evaluations, the median effect over conventional instruction was 0.66 SD, depending strongly on whether tests were locally developed or standardised, and small where controls were nonconventional or implementations flawed. Both entries pass the judge, on abstracts. It supports individualised tutoring over non-individualised instruction on aligned achievement; it does not isolate adaptation from the rest of the system, does not show an advantage over adaptation by people, and reports no common horizon.
- [Contingent versus fixed support](../claims/contingent-scaffolding-improves-learning.md) [+M]: in one-to-one tutoring of long division with fourth and fifth graders (n = 8 per condition), fully contingent support beat fixed, moderate, partly contingent and no support on immediate and one-month follow-up tests; a within-subjects tutoring study reports similar immediate outcomes but better transfer for interactive, contingent tutoring; a synthesis of dynamic assessment ranks explicit strategy training above contingent scaffolding. This is the closest test here of adapting support to responses against fixed support, and it is small and mostly one-to-one; classroom and software contingency are not shown. Not settled: the entries could not be confirmed from abstracts.
- [Guidance and expertise](../claims/expertise-reversal-effect.md) [~M]: a review of cognitive load studies reports that supports such as worked examples and integrated explanations help novices on a task and can become redundant or depress performance as prior knowledge grows. It qualifies the relationship: adaptation that keeps support in place as performance improves can work against it. No effect size; not settled on its abstract.
- [Personalised learning and implementation](../claims/personalized-learning-effects-vary-with-fidelity.md) [~M]: in about 40 schools implementing personalised-learning practices (adaptive software among them), matched against virtual comparison groups (`controlled-nonrandom`), one-year effects were small (+0.09 SD mathematics, significant; +0.07 SD reading, not significant) and larger where implementation was reported as fuller or longer; the authors call that link suggestive, resting on self-report and a small district subsample. It qualifies the relationship: an adopted platform is not an enacted adaptation, and school-level averages are far below the tutoring syntheses' figures. Not yet checked against its source.
- [Learning-styles matching](../claims/learning-styles-matching-does-not-improve-learning.md) [-S]: a systematic review found almost no studies with the crossover design needed to test matching instruction to learning style, and judged the one candidate unconvincing; a randomised study with fifth graders found no style-by-modality interaction. It bears against adapting on self-reported style; it says nothing about adapting on responses or prior knowledge. Not settled on abstracts.
- [Learner-model calibration](../claims/learner-models-miscalibrated-outside-data-interval.md) [~W]: one analysis of two knowledge-tracing models on tutoring datasets reports that both were calibrated only in the range containing most of the data, overestimating learners when the probability of a correct answer was low and underestimating them when it was high. It limits the diagnostic step: a system's estimate for a learner at the extremes is least trustworthy where routing matters most. Associational, one study, no outcome for learners; not yet checked against its source.

Keep the comparator (conventional, non-tutoring software, human tutor), the population band, the outcome instrument and its alignment, and the horizon with each finding. Do not set the meta-analytic g values beside the school-level SD gains as if they measured the same thing.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02: claims this page cited before the 2026-10-02 rewrite. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S] — not settled: the text available could not confirm the entries (abstract)
- [Fading support promotes the transfer of responsibility from instructor to learner.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+S] — not settled: the text available could not confirm the entries (abstract)
- [Example-problem sequences reduce cognitive load and improve learning outcomes.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+M] — not yet checked against its sources
- [Intuitive learners tend to outperform sensing learners in media-based presentations](../claims/intuitive-learners-outperform-sensing-learners.md) [-M] — not yet checked against its sources

## Objective and learner-valued goal

The designer's objective in an adaptive design is usually a criterion on each skill in a map, reached in less time than a fixed path would take. What the learner values may differ: finishing the assigned work quickly, understanding why a method works, preparing for a particular examination, or not being held on one skill while classmates move on. Ask what the learner wants and why, record agreement or divergence as an observation, and do not infer it from time logged in the system.

For example, a secondary-school learner using an adaptive mathematics platform may value being ready for an end-of-year standardised examination, while the platform's objective is mastery of each skill on its own items. The tutoring synthesis above reports that gains depended on whether tests were locally developed or standardised, so the two aims may not move together. A design that serves both states which instrument and horizon count, adds unassisted examination-style items to the platform's checks, and tells the learner how the platform's mastery estimate relates to the examination.

## What would revise this model?

The expectation should weaken if, with comparable learners and content, individualised selection does not outperform the same content in a fixed sequence on independent outcomes, or if tutoring-system gains disappear on standardised measures and at a delay. If difficulty-only adaptation does as well as adaptation of support, the claim that support is the active part should be revised. If routing decisions based on a learner model are no better than a teacher's or the learner's own choices, the diagnostic step needs rethinking. If time saved, persistence or the learner's own goals move against achievement, the model is incomplete without them. Do not protect it by relabelling every failure as low fidelity or poor engagement.

Within-system performance, aligned achievement, standardised achievement, delayed retention, transfer and time to criterion are separate claims. The present evidence does not establish which adaptation target matters most, an optimal difficulty band or mastery threshold, or a forecast for an individual learner.

## Related Principles
- [Cognitive Load Management](cognitive-load-management.md) — adaptation is the primary mechanism for keeping intrinsic load matched to learner expertise over time
- [Assessment for Learning](assessment-for-learning.md) — supplies the continuous diagnostic evidence that any adaptive decision depends on
- [Competency-Based Learning & Assessment](competency-based-learning-assessment.md) — provides the mastery criteria that gate progression in adaptive designs
- [Active Learning](active-learning.md) — adaptive systems still require learners to do generative work; adaptation of difficulty does not replace engagement

## Examples

- [Four-layer system architecture for intelligent oral diagnosis and adaptive training](../elements/four-layer-oral-diagnosis-system-architecture.md)
- [Mask the reinforcement learning policy's action space to a zone-of-proximal-development difficulty band (success probability 0.4–0.8)](../strategies/zpd-masked-rl-content-sequencing.md)

### Validated
- **[ASSISTments](https://www.assistments.org)** — Free web-based math platform (grades 6–12) that adapts problem selection and hint delivery based on item-level responses. Randomized studies across Maine schools showed significant homework-related learning gains over business-as-usual conditions (Roschelle et al., 2016, *AERJ*).
- **[Carnegie Learning MATHia](https://www.carnegielearning.com/solutions/math/mathia/)** — Cognitive-tutor-based adaptive math system using a cognitive model of learner knowledge to select problems and tailor step-level hints. A large RAND study (Pane et al., 2014) found roughly doubled learning-growth effects in second-year algebra relative to conventional instruction.
- **[Khan Academy](https://www.khanacademy.org)** — Mastery-based practice in mathematics that adapts task assignment to demonstrated skill levels, with mastery gates before progression.

### Illustrative
- **[Adaptive Difficulty](../elements/adaptive-difficulty.md)** — The core element: dynamically raising or lowering task difficulty based on performance signals such as accuracy, latency, and error patterns.
- **[Adaptive Mastery Learning](../elements/adaptive-mastery-learning.md)** — Combines mastery criteria with adaptive routing so learners who fail an assessment are routed to remediation rather than the next unit.
- **[Adaptive Learning](../patterns/adaptive-learning.md)** — The full instructional pattern: diagnosis, adaptive task selection, responsive feedback, and mastery gating operating as a cycle.
- **Duolingo** — Language-learning app that adapts item scheduling using a spaced-repetition and learner-error model, reinserting items the learner is predicted to forget.

## Key Sources
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197-221. [doi:10.1080/00461520.2011.611369](https://doi.org/10.1080/00461520.2011.611369)
- Kulik, J. A., & Fletcher, J. D. (2016). Effectiveness of intelligent tutoring systems: A meta-analytic review. *Review of Educational Research, 86*(1), 42–78. [doi:10.3102/0034654315581420](https://doi.org/10.3102/0034654315581420)
- Ma, W., Adesope, O. O., Nesbit, J. C., & Liu, Q. (2014). Intelligent tutoring systems and learning outcomes: A meta-analysis. *Journal of Educational Psychology, 106*(4), 901–918. [doi:10.1037/a0037123](https://doi.org/10.1037/a0037123)
- Corbett, A. T. (2001). Cognitive computer tutors: Solving the two-sigma problem. *User Modeling 2001*, 137–147. [doi:10.1007/3-540-44566-8_14](https://doi.org/10.1007/3-540-44566-8_14)
- Pane, J. F., Steiner, E. D., Baird, M. D., Hamilton, L. S., & Pane, J. D. (2017). Informing progress: Insights on personalized learning implementation and effects. RAND Corporation. [https://www.rand.org/pubs/research_reports/RR2042.html](https://www.rand.org/pubs/research_reports/RR2042.html) [doi:10.7249/rr2042](https://doi.org/10.7249/rr2042)

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
- [Example–problem sequences reduce cognitive load.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+S] — adaptive sequencing can interleave worked examples with problems based on performance

-->
