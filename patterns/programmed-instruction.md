---
type: pattern
id: programmed-instruction
title: Programmed Instruction
description: "A reusable sequence in which content is broken into small frames, each needing an active response that is confirmed or corrected at once, with progress at the learner's pace or by branching on the response, behind a unit check; expected to help with facts, rules and procedures that have checkable answers when steps fit prior knowledge and a dated schedule guards against non-completion. No claim in this wiki tests programmed instruction itself; the nearest evidence is from self-paced mastery programs (PSI), feedback after retrieval and intelligent tutoring."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-15
author: B. F. Skinner (linear); Norman Crowder (branching/intrinsic)
grain_size: lesson
---

# Programmed Instruction

> **Pattern** · [All patterns](index.md)
> **Evidence** · 21 claims (5 for, 14 mixed, 2 against) · 19 studies (8 quant-synthesis, 4 causal, 3 associational, 2 review, 2 theoretical), `q1`–`q4` · 5 of 19 report an effect size · 17 claims rest on one study

## Description and scope

A reusable sequence for teaching well-defined content one small step at a time: **a frame gives a little information → the learner makes an active response (writes or selects an answer) before the answer is shown → the answer is confirmed or corrected at once → the next frame follows, at the learner's own pace (linear programming) or chosen by the response (branching: a remedial frame after an error, a skip ahead after strong performance) → a unit check decides whether the learner moves on**. The intended change is in recalling facts, applying rules and carrying out procedures (`factual`, `procedure`), measured on items the learner has not just seen in a frame.

It sits inside three converted neighbours and does not repeat their models. The [Mastery Learning pattern](mastery-learning.md) owns the unit criterion, the corrective loop and the recheck; this page uses that gate at the end of each run of frames. The [Immediate Feedback principle](../principles/immediate-feedback.md) owns when feedback should come and what form it takes; this page applies it at the grain of one frame. The [Adaptive Learning principle](../principles/adaptive-learning.md) owns when adjusting the path to the learner helps; branching programming is its oldest form. [Game-Based Mastery Learning](game-based-mastery-learning.md) is a modern descendant that adds a game layer to the same small-step core, and [Direct Instruction](direct-instruction.md) is the teacher-led, group-paced relative. Self-pacing as such belongs to the [Self-Directed Learning](self-directed-learning.md) pattern and [principle](../principles/self-directed-learning.md).

**No claim in this wiki tests programmed instruction itself**: no recorded study compares frames with a response and immediate confirmation against another form of the same content, and none compares linear with branching programs or small steps with large ones. The nearest evidence is of four kinds, each carried here by extrapolation: Keller's Personalized System of Instruction (PSI), a descendant that keeps self-paced units and a mastery test, from one large 1990 meta-analysis; feedback after a retrieval attempt; intelligent tutoring systems, which branch on each response; and one experiment and one meta-analysis on learner control of pacing. The old page's account ([Molenda, 2008](https://edtechbooks.org/lidtfoundations/programmed_instruction)) says that most of PI's specific hypotheses (small steps, linear order, confirmation as a universal reinforcer) did not hold up under testing, while PI as a format still did better than conventional group instruction in comparison studies; that history is the old page's, from its Key Sources, not from a claim page. The sequence below is the earlier page's, kept as the default, with each step's evidence status stated.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Before the first frame, a short set of unprompted items from the end of the unit and one or two from its prerequisites. Record each response, whether it was right, and how long it took. Use `expertise` values where known (`novice`, `intermediate`, `advanced`); record unknowns as unknown rather than assuming `novice`. |
| The content | Whether it breaks into steps that each have a checkable right answer (`factual`, `procedure`, a rule), or whether answers are open, contested or judged as a whole (`complex-skill`, design, argument). Which steps depend on which. Which errors learners commonly make. |
| Context and activities | Setting (`classroom`, `online-self-paced`, `online-instructor-led`, `workplace-clinical`), device (paper, computer, phone only), `single-session` or `days-weeks`, whether a teacher, tutor or proctor is present and for how long, whether learners must finish by a date. |
| Learner-valued goal | Ask what the learner wants to be able to do and by when (pass a certification, do a task at work, keep up with a class). Record disagreement with the designer objective, and how much extra time the learner will accept for repeating frames. |
| Designer objective | The capability each unit stands for, its knowledge type, the unit criterion (the share correct on the unit check) and its justification, and which later units depend on it. If the brief names its own check, rubric or criterion, record it as given. |
| Outcome | The unit check and the course examination, scored on items not shown in the frames; whether the examination is written locally or is an independent standardized test; completion (`persistence`) and time to criterion (`learning-time`); and any delayed horizon. |

A request to "turn this module into self-paced bite-sized steps" does not specify these. Ask what the right answer to each step is, what the learner should be able to do at the end, and whether the learner must finish by a date, before choosing step size, branching rules or a criterion.

## Sequence and conditional policy

The default sequence is the earlier page's five steps, with a placement step and a unit gate added from the neighbouring patterns. Steps 3 and 6 have neighbouring claims, carried by extrapolation; the others are untested here.

1. **Place the learner.** Give the starting items (inputs, above). A learner who meets the unit criterion on them skips the unit's frames and takes the unit check; a learner who misses a prerequisite starts with its frames. Evidence status: untested proposal. More proficient learners respond faster at the step level in tutoring data ([higher prior proficiency goes with faster step-level responses](../claims/higher-proficiency-faster-step-responses.md) [~W], associational, eight algebra-tutor deployments), which is a reason to expect placement to save their time, not evidence that it does.
2. **Break the content into frames.** Each frame presents one piece of information or one step, then asks for a response that uses it. For a new rule, state the rule, give one or two examples, then give incomplete examples for the learner to complete. Evidence status: [the rule-example sequence](../claims/rule-example-sequence-efficient-rule-introduction.md) [~W], a 1966 conceptual paper reporting that this order "appeared to be an excellent method" in early programmed-instruction work; an argument, not a comparison. Step size is untested here: start with steps a novice gets right on about four frames in five (a proposal), and enlarge them when errors are rare.
3. **Require a response before showing the answer, then confirm or correct at once.** Constructed responses (typed or written) for recall; selected responses only where the final task is recognition. After an error, show the correct answer and, for a rule, the reason; after a correct answer, a short confirmation is enough. Evidence status: [feedback after retrieval](../claims/feedback-enhances-retrieval-practice.md) [+M]: in a laboratory word-pair study, giving the correct answer after a wrong retrieval greatly raised retention a week later while feedback after correct answers made little difference; in classroom studies, quizzes with corrective feedback gave a larger testing effect than quizzes without, a between-study comparison that [an earlier meta-analysis did not find](../claims/feedback-no-significant-moderation.md) [~M]. These are quizzes and word pairs, not programmed frames.
4. **Branch on the response.** After two errors on frames of the same kind (a proposal), route the learner to remedial frames that teach the step a different way, then return; after a run of correct, fast responses (a proposal: five in a row), offer a skip to the next section's first check. Evidence status: untested for frames. [Intelligent tutoring systems](../claims/adaptive-learning-improves-outcomes.md) [~S], which adjust to each response, outperformed teacher-led large-group instruction, other computer-based instruction and textbooks in two meta-analyses, but not individual human tutoring or small groups, and their gains were smaller on standardized than on locally written tests.
5. **Let the learner go at their own pace inside a dated schedule.** Each learner works through the frames on their own time, but each unit has a target date, and a learner who falls behind is contacted. Evidence status: [self-paced mastery programs (PSI) reduced college course completion](../claims/self-paced-mastery-programs-reduce-college-course-completion.md) [-M] (23 of 32 studies found higher completion in the conventional class), and [group-based mastery programs had larger effects than self-paced ones](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M]. The dated schedule is the claim page's own suggestion (deadlines or pacing support), not a tested remedy.
6. **Gate the unit on a check without prompts.** End each unit with items the learner has not seen in a frame, with no cues; advance at or above the criterion; below it, give corrective frames and a parallel recheck (run as the [Mastery Learning pattern](mastery-learning.md) sets out). If the brief names its own check, use it as the gate and add no other test. Evidence status: [mastery programs, PSI among them, raised examination performance](../claims/mastery-learning-improves-outcomes.md) [+M] over conventional instruction (mean 0.52 SD across 103 studies; PSI 0.48, not significantly different from group-based programs), and [higher unit standards went with larger effects](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M]. Those programs had units, tests and proctors, not necessarily frames.

**Dose and progression across sessions** (labelled proposals; no claim here gives a number):

| Stage | Session length | Frames and support | Moves on when |
|---|---|---|---|
| Early sessions (first unit or two) | 15–20 minutes of frames, one sitting | Small steps; each frame carries a cue (a highlighted word, a partly completed answer); rule given before examples; remedial branch after two errors of one kind | The unit check, without cues, is at or above the criterion |
| Middle sessions | 20–25 minutes | Cues removed from about half the frames; steps combine two earlier steps; two or three review frames from earlier units at the start | Unit check at criterion, and the review frames from earlier units are answered without cues |
| Late sessions | 25–30 minutes, including a mixed review | Frames without cues; larger steps or whole short problems; one in four frames draws on earlier units; the learner explains one answer in their own words | Course check at criterion on items from all units, with no cues |

A session ends early when the learner has made three errors on remedial frames for the same step (a proposal): stop, record the step, and have a person look at it before the next session.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Frames answered correctly, unit check failed | Give two unit-check items with the frame's cue restored and two without. | If the cued items are right and the uncued wrong, the cues were carrying the answer: remove cues sooner and add frames without them. If both are wrong, the step was learned in the frame's wording only: add frames that vary the surface. Untested. |
| Repeated errors on one kind of frame | Ask the learner to say what the frame is asking; give one prerequisite item. | If they misread the frame, rewrite it; if the prerequisite fails, branch back to it; if both are fine, the step is too large: split it. One error pattern does not settle which. |
| Very fast responses | Check accuracy on the fast items and give one constructed-response item where the frames used selected responses. | Fast and accurate on constructed items suggests the learner already knows the step ([faster step responses go with higher proficiency](../claims/higher-proficiency-faster-step-responses.md) [~W], associational): offer the skip. Fast and inaccurate suggests guessing or clicking through: require typed responses. |
| Very slow responses | Ask what the learner is doing on a slow frame; compare with their accuracy. | Slow and accurate may be careful work; slow and inaccurate may mean stuck. In tutoring data, slower response tendencies went with faster learning for higher-proficiency students and slightly slower learning for lower-proficiency ones ([response time and prior proficiency](../claims/rt-propensity-proficiency-interaction-learning.md) [~W], associational). Branch the second case to remedial frames; do not hurry the first. |
| Learner looks at the answer before responding | Compare first-attempt accuracy on frames where the answer was hidden with those where it could be seen. | Hide the answer until a response is entered; on paper, use a mask or a separate answer page. |
| Learner stops working or falls behind the dated schedule | Ask what the learner wants from the course and what got in the way. | Contact at the missed date, agree a new date, offer a short session with a person; see the completion row in the table below. |

## Fitting the design to a situation

**The three facts that most change the decision:**

- **Whether each step has a checkable right answer.** Frames with immediate confirmation suit facts, rules and procedures; where the task is judged as a whole or has no single answer, bare right/wrong confirmation does little and may mislead. If unstated, ask: for each step, can you write the correct answer in advance?
- **Whether learners must finish by a date and who will notice if they stop.** Self-pacing raised non-completion in PSI. If unstated, ask: what happens to a learner who has not finished by the end of the course, and is there a person who checks?
- **What the learner already knows.** Placement and step size depend on it, and a learner who already knows the unit gains nothing from its frames. If unstated, ask: can you give five unprompted items from the end of the unit before the first frame?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are `novice` in the domain | Smallest steps; rule then examples then incomplete examples; a cue on every early frame; remedial branch after two errors of one kind; remove cues over three sessions (dose table above). | [Rule-example sequence](../claims/rule-example-sequence-efficient-rule-introduction.md) [~W] (an argument from early programmed-instruction work, not a test); step sizes untested |
| Learners are `intermediate` or `advanced`, or vary widely in prior knowledge | Place each learner with unprompted unit items; let those at criterion take the unit check directly; give larger steps and fewer cues to the rest. | Untested proposal; [faster step responses with higher proficiency](../claims/higher-proficiency-faster-step-responses.md) [~W] is associational and from algebra tutors |
| Learners are `child` (upper primary) or in secondary school | Sessions of 10–15 minutes, a teacher present to see who is stuck, the class working through a unit by a shared date and taking its check together. | [Mastery programs raised examination performance](../claims/mastery-learning-improves-outcomes.md) [+M] in college, high-school and upper-elementary settings; [group-based programs had larger effects](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M]; not frame-based programs |
| The goal is a fact, rule or procedure with one right answer per step | Use the full sequence; constructed responses for recall; correct answer and reason after each error. | [Feedback after retrieval](../claims/feedback-enhances-retrieval-practice.md) [+M] (word pairs and classroom quizzes, not frames) |
| The goal is a complex judgment, a design, an argument or an open problem | Do not build it from right/wrong frames. Use frames only for the prerequisite facts and rules; teach the whole task through worked examples, cases or practice with feedback on the reasoning ([worked examples](worked-examples.md), [direct instruction](direct-instruction.md)). | [Outcome-only feedback impedes learning of complex tasks](../claims/outcome-feedback-impedes-complex-task-learning-mcpl.md) [-W] (a review's report on a laboratory cue-learning paradigm); [induction and errorful learning suit some task types and not others](../claims/task-type-moderates-induction-error-usefulness.md) [~W] (1966 argument) |
| The brief wants a whole-task performance kept whole (a full procedure at work, a case, a performance) | Keep the whole task as the unit check and the goal; use frames only for the parts learners keep getting wrong, and return them to the whole task at once. | Untested proposal |
| `online-self-paced`, no teacher, learners must finish by a date | Dated targets per unit, an automatic reminder at each missed date and a person who contacts anyone two targets behind; keep the unit gate. | [Self-paced mastery programs reduced completion](../claims/self-paced-mastery-programs-reduce-college-course-completion.md) [-M] (college PSI courses); reminders and contact are untested remedies |
| `classroom`, one teacher for many learners | The software or the printed program confirms each response; the teacher sees who is branched to remedial frames twice and goes to them; the class keeps a shared unit date and takes the unit check together. | [Group-based programs had larger effects than self-paced ones](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M]; the teacher's routine is untested |
| Scarce facilitator time (volunteers, a tutor checking in briefly, a busy shift) | The program does all confirmation; the person's time goes only to learners stopped by the three-error rule, for 5 minutes each, with the stuck step shown to them. | Untested proposal (the old page's Programmed Tutoring descendant used a human tutor for hints) |
| A human tutor or a small group is available for every learner | Keep the person; use frames for practice between sessions, not in place of the tutor. | [Intelligent tutoring systems did not outperform individual human tutoring or small-group instruction](../claims/adaptive-learning-improves-outcomes.md) [~S]; carried from tutoring systems to programmed frames |
| Some learners remote and some in the room, or phone only | One frame per screen, responses by tapping a choice or typing a short answer, no frame that needs a printed sheet; the same dated schedule and unit check for both groups; remote learners get the contact by message. | Untested proposal |
| `single-session` only | One program of 20–30 minutes covering one rule or procedure, ending with five unprompted items; no unit gate across sessions, and a note to the learner of which steps to revisit. | Untested proposal |
| A fixed short time budget (for example 15 minutes) | Placement 2 minutes, frames 10 minutes (about 15–20 frames), check 3 minutes; cut content rather than frames' response steps. | Untested proposal |
| Learners with low confidence or low literacy | Early frames that most learners get right, audio for frame text, responses by selecting or pointing, the learner's record private to them; move to constructed responses once accuracy is steady. | Untested proposal |
| Adults in work settings | Place by unprompted items so known steps are skipped; frames use the learner's own job tasks and forms; the unit check is the job task. | Untested proposal (the old page names military and corporate training as PI's main users) |
| The brief names its own check, rubric, criterion or categories | Use them as given: the brief's check is the unit gate, its categories label the frames, its criterion is the cut score; change only step size, the response before the answer, and the immediate correction. Add no test, quiz or survey the brief did not ask for. | Untested proposal |
| Private or sensitive material (health, finances, personal history) | Responses stay with the learner; a person sees only whether the unit check was passed, unless the learner chooses to share more. | Untested proposal |
| A product or performance for a real audience | Not a programmed-instruction goal; use frames only for prerequisite facts and conventions, and teach the product through drafts and feedback on the whole. | Untested proposal |
| High stakes, or an independent standardized test at the end | Write the unit checks as items the frames did not show; expect a smaller gain on the standardized test than on the course's own tests; check at the stated delay. | [Mastery effects were near zero on standardized tests in four studies with both kinds](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M]; [tutoring-system gains were smaller on standardized tests](../claims/adaptive-learning-improves-outcomes.md) [~S] |
| Complex material presented as animation or video inside the program, or learners want to set the pace | Cut it into short segments the learner advances, with pause and replay; do not expect learner control in general to help. | [Learner pacing helped on difficult questions in one experiment, while learner control in general showed almost no effect across 18 studies](../claims/learner-paced-beats-system-paced-complex-material.md) [~M] (primary-school students, one animation) |

Ten of the twenty rows link a claim (novices, varied prior knowledge, children, a rule or procedure, a complex goal, self-paced online, one teacher, a tutor available, high stakes, complex animated material), each carried beyond the population or design its claim page reports, as its Basis cell says; the other rows are untested proposals.

## Choosing configurations from evidence

- **Self-paced units with a mastery gate (PSI).** [Mastery Learning Improves Outcomes](../claims/mastery-learning-improves-outcomes.md) [+M]: one meta-analysis of 108 controlled evaluations (67 of PSI, almost all self-paced and in college; 36 of group-based Learning for Mastery); across 103 studies of examination performance the mean effect was 0.52 SD, with PSI at 0.48 and LFM at 0.59, not significantly different. Its synthesis table gathers 7 distinct studies. [The moderator analysis](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M] found larger effects for group-based than self-paced programs, for higher unit standards, on locally written than on standardized tests (standardized effects near zero, -0.05 to 0.09, in four studies with both), and where the comparison group got less quiz feedback; its table gathers 6 distinct studies. The cost: [PSI reduced completion](../claims/self-paced-mastery-programs-reduce-college-course-completion.md) [-M], h = -0.14 across 32 studies, not enough to explain the examination advantage (0.46 SD where PSI completion was lower, 0.55 where higher). Carry to frames only this far: a self-paced program with a unit gate can raise course-test scores, and self-pacing without dates costs completion.
- **Confirmation and correction after each response.** [Feedback Enhances Retrieval Practice](../claims/feedback-enhances-retrieval-practice.md) [+M]: in classroom studies, quizzes with corrective feedback gave g = 0.537 against g = 0.374 without, a between-study comparison; in one laboratory experiment (258 participants, Luganda–English word pairs), the correct answer after a wrong retrieval raised retention a week later by 494%, and feedback after correct responses made little difference. Its table gathers 6 distinct studies. Qualified by [Adesope et al.'s meta-analysis](../claims/feedback-no-significant-moderation.md) [~M], where testing effects did not differ with and without feedback (g = 0.63 and 0.60). So the correction after an error is the part to keep; a confirmation after every correct answer may add time and little else.
- **Branching on each response.** [Intelligent tutoring systems improve achievement over non-individualised instruction](../claims/adaptive-learning-improves-outcomes.md) [~S]: tutoring systems against teacher-led large-group instruction g = 0.42, against other computer-based instruction 0.57, textbooks 0.35, human tutoring -0.11, small groups 0.05 (Ma et al. 2014, from the abstract); median 0.66 SD in 50 evaluations, smaller on standardized tests ([Kulik & Fletcher 2016](https://doi.org/10.3102/0034654315581420)). Its table gathers 10 distinct studies, one of which found adaptive task difficulty did not help second-graders. Tutoring systems model the learner far more finely than a branching program; carry it to "routing on the response can beat a fixed group sequence", no further.
- **Who sets the pace.** [Learner pacing on complex material](../claims/learner-paced-beats-system-paced-complex-material.md) [~M]: learner-paced animation beat system-paced animation on difficult questions only, for primary-school students in one experiment; learner control in general had an effect near zero (g = 0.05) across 18 studies. Its table gathers 8 distinct studies. PI's self-pacing is not by itself where its benefit lies.
- **Limits on bare confirmation.** [Outcome feedback impedes complex-task learning](../claims/outcome-feedback-impedes-complex-task-learning-mcpl.md) [-W] (Kluger & DeNisi's report of laboratory cue-learning work, no effect size) and [immediate knowledge of results during computerised testing made essentially no difference to achievement estimates](../claims/knowledge-of-results-no-effect-achievement-test-dimensionality.md) [~W] (Weiss 1980, a testing study, not instruction): right/wrong alone is weak where the task has many cues or no single answer.

Do not rank programmed instruction against teacher-led instruction, worked examples or tutoring from these claims: none tests frames. A precise abstention names the missing comparison (the same content as frames with response and immediate correction, against the same content as text with end-of-section questions, on new items at a stated delay, with completion recorded) and the local observation that would stand in for it: unit-check accuracy on unseen items, time to criterion and completion, for learners placed into the program against those placed out.

## The evidence by question

- *Self-paced or group-paced progression through small units, at what criterion, measured how?* [Mastery learning effects vary with the mastery standard, pacing, test type and the control group's feedback](../claims/mastery-learning-effects-vary-with-standard-pacing-and-test-type.md) [~M]
- *Does confirming or correcting each response add to learning from making the response?* [Feedback Enhances Retrieval Practice](../claims/feedback-enhances-retrieval-practice.md) [+M]

## Further evidence, not yet read against this model

Claims read for this page that bear on it less directly; each says how far.

- [Mastery learning effects are larger for lower-aptitude students](../claims/mastery-learning-effects-larger-for-lower-aptitude-students.md) [+M] — from the same 1990 synthesis (13 studies; 0.61 SD against 0.40, not significant): bears on who gains from a gated program, not on frames.
- [Mastery learning gains persist at follow-up](../claims/mastery-learning-gains-persist-at-follow-up.md) [+M] — the same synthesis (11 studies, about eight weeks): bears on the delayed horizon for gated programs, PSI included.
- [A review reports that pretesting helps paired-associate learning only when correct-answer feedback is immediate, but helps trivia-fact learning even when feedback is delayed](../claims/feedback-timing-moderates-pretesting.md) [~M] — bears on whether the confirmation must come at once; for simple paired items it must, for richer facts it may wait. Owned by the [Immediate Feedback principle](../principles/immediate-feedback.md).
- [Intelligent tutoring systems can improve learning outcomes, particularly with immediate actionable feedback](../claims/its-improve-learning-outcomes-with-actionable-feedback.md) [+W] — a framework paper's second-hand report of tutoring meta-analyses; adds no study.

## Illustrative design instance and observation record

*Invented illustration, not a tested program.* New pharmacy assistants, adults on rotating shifts, must learn to read prescription abbreviations and calculate quantities before working alone in four weeks; they study on their phones, and one pharmacist has about 15 minutes a week for the group. The table changed the default: placement with ten unprompted abbreviation and calculation items skips two learners past the abbreviation unit; frames show one abbreviation or one calculation step per screen, require a typed answer, and show the correct answer and its reason after an error; the pharmacist's 15 minutes go to anyone stopped by the three-error rule; each unit has a target date, with a message at a missed date. The brief names the pharmacy's own dispensing checklist, so the unit check is that checklist applied to five new prescriptions, and no other test is added. A learner says she wants to stop asking colleagues what abbreviations mean; the designer's objective is error-free quantities. They agree to record both. The claims cover college PSI courses, classroom quizzes and tutoring systems, not this population, device or horizon; these are local choices to observe.

Record: **content steps and their right answers → placement items and responses, with time → frames shown, response to each, first-attempt accuracy, cue present or not → branches taken and why → time per session and dates met or missed → unit-check items (unseen), score, criterion → candidate interpretations (cue-dependence, prerequisite gap, step too large, guessing, already known) and their basis → recheck and delayed check at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record but must not fabricate missing inputs or assign numerical probabilities of mastery without a calibrated model.

## Elements and limits

[Self-paced learning](../elements/self-paced-learning.md), [immediate feedback](../elements/immediate-feedback.md), [practice](../elements/practice.md), [feedback](../elements/feedback.md), [hints](../elements/hints.md), [fading](../elements/fading.md), [retrieval practice](../elements/retrieval-practice.md), [adaptive mastery learning](../elements/adaptive-mastery-learning.md) and [assessment](../elements/assessment.md). Principles the pattern draws on: [Mastery Learning](../principles/mastery-learning.md), [Immediate Feedback](../principles/immediate-feedback.md), [Adaptive Learning](../principles/adaptive-learning.md), [Active Learning](../principles/active-learning.md), [Scaffolding and Fading](../principles/scaffolding-and-fading.md) and [Chunking](../principles/chunking.md). Theory: [Behaviorism](../theories/behaviorism.md) and the [six-element programmed-instruction framework](../theories/programmed-instruction-six-element-framework.md), whose source also reports that the generality of its principles came into question.

This pattern is scoped to well-defined content whose steps have checkable answers. Open, ill-structured and whole-task goals need other configurations ([case-based learning](case-based-learning.md), [worked examples](worked-examples.md), [direct instruction](direct-instruction.md) with feedback on reasoning). Whether frames with a response and immediate correction teach more than the same content in other forms, for which learners, at what cost in completion, and at what horizon, remains to be tested.

## Claims

- [Guidance, immediate feedback, and system-directed control showed unadjusted moderator signals that did not survive multiplicity adjustment, making them hypothesis-generating only](../claims/design-moderators-unadjusted-only-hypothesis-generating.md) [~W]
- [Immediate-feedback tutors allow learning from errors but deny learning from their downstream consequences](../claims/immediate-feedback-limits-downstream-error-learning.md) [~W]
- [Final recall does not differ reliably between participant-controlled and computer-controlled feedback skipping](../claims/participant-computer-controller-no-recall-difference.md) [~W]
- [Participants' feedback-skipping decisions diverge from the optimal computer algorithm: they skip after some incorrect responses and fail to skip after many correct responses](../claims/skipping-decisions-diverge-from-computer.md) [~W]

## Related Patterns

- [Mastery Learning](mastery-learning.md) — owns the unit criterion, correction and recheck this pattern uses at the end of each run of frames; PSI, its self-paced variant, is programmed instruction's direct descendant
- [Direct Instruction](direct-instruction.md) — the teacher-led, group-paced descendant with scripted small steps and unison responding
- [Game-Based Mastery Learning](game-based-mastery-learning.md) — a modern descendant that adds game mechanics (streaks, levels, adaptive difficulty) to the same small-step, immediate-feedback, self-paced core PI established
- [Tutor-led strategy set for effective adult language lessons: structure, small steps, early success, continuous practice and constant re-use](../designs/tutor-led-strategies-adult-language-lessons.md)

## Examples
- Skinner's original teaching-machine frames and linear programmed textbooks (e.g., *English 2600*)
- Crowder's AutoTutor and TutorText branching programmed books
- The Personalized System of Instruction ("Keller Plan"): self-paced units with a mastery test and proctor feedback before advancing
- [ETV, programmed workbook and drive-in seminar inservice course](../designs/etv-workbook-seminar-inservice-course.md) — Georgia educators complete a workbook session for each statewide TV programme

## Key Sources
- Molenda, M. (2008). The programmed instruction era: When effectiveness mattered. *TechTrends, 52*(2), 52–58. Republished in R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/programmed_instruction](https://edtechbooks.org/lidtfoundations/programmed_instruction)
- Skinner, B. F. (1954). The science of learning and the art of teaching. *Harvard Educational Review, 24*, 86–97.
- Keller, F. S. (1968). Goodbye, teacher... *Journal of Applied Behavior Analysis, 1*, 78–79.
- Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *Review of Educational Research, 60*(2), 265–299. [doi:10.3102/00346543060002265](https://doi.org/10.3102/00346543060002265)

<!-- deprecated 2026-10-15: superseded by the conditional model above. The previous body, kept verbatim.
## Description
Programmed Instruction (PI) restructures content as a sequence of small "frames," each presenting a small amount of information and then requiring the learner to make an active response — write or select an answer — before immediately revealing whether it was correct. Skinner's original **linear programming** moved every learner through the same fixed sequence of small steps; Norman Crowder's **intrinsic (branching) programming** let learners skip ahead through easy material or branch to remedial frames when they struggled, based on their responses (Molenda, 2008).

PI was devised as a humane alternative to lock-step, group-paced instruction: it lets each learner work at their own pace, guarantees a response at every step (rather than passive listening), and provides confirmation immediately rather than after a delay. It was the first instructional format subjected to the "90/90 criterion" (at least 90% of the target population achieving 90% of objectives) as a mandatory development standard, which drove a discipline of testing and revising materials during development — a direct precursor to systematic instructional design.

While PI itself receded after the 1960s once most of its specific hypotheses (small steps, linear sequencing, immediate reinforcement as universally necessary) failed to hold up under testing, several descendants inherited its core mechanism — a small step, an active response, and confirmation or correction — while adding features PI lacked: **Programmed Tutoring** (Ellson) added a human tutor providing social reinforcement and hints instead of a mechanical device; **Direct Instruction** (Engelmann) added fast-paced, scripted, teacher-led group unison responding; and the **Personalized System of Instruction** ("Keller Plan") added self-paced units with a mastery test and proctor feedback at the end of each unit before the learner advances — the direct forerunner of mastery-based and self-paced distance education.

## Implications

### Context
#### Requirements
- Content that can be broken into small, sequential, well-defined steps, each pairing information with a checkable response
- A mechanism (mechanical device, book layout, tutor, or software) for withholding the correct answer until after the learner responds, and revealing it immediately after
#### Constraints
- Small-step, linear sequencing is not itself necessary for effectiveness — later research found branching and larger chunks worked as well or better for many learners; the pattern's value lies in active responding and immediate confirmation, not the specific step size
- Poorly suited to open-ended, ill-structured content where there is no single correct response to confirm at each step
- Schools found PI materials effective in isolation but could not realize gains without restructuring surrounding classroom routines and pacing — the pattern strains against institutions built around fixed group pacing
#### Grain Size
- Lesson
- Unit

### Target Goals
- Discrete, checkable knowledge and skills: recall of facts, application of rules, execution of procedures
- Self-paced mastery, letting faster learners advance without waiting and slower learners repeat without holding others back

### Target Learners
- Learners who benefit from working independently at their own pace rather than a fixed group pace
- Learners in domains (military and corporate training, in particular) where efficiency and measurable objective attainment matter enough to justify the design and testing investment PI requires

### Theory
#### Supporting
- [Behaviorism](../theories/behaviorism.md) [+S] — PI is behaviorism's most direct instructional expression: small stimulus-response steps strengthened by immediate reinforcement (confirmation of the correct response)
#### Contradicting / Qualifying
- Subsequent research undermined several of PI's specific behaviorist hypotheses (that steps must be small, sequencing must be linear, and "knowledge of correct response" is a universal reinforcer), even though PI as a format continued to outperform "conventional" group instruction in comparison studies

### Claims

- [Higher prior proficiency is associated with faster step-level response-time propensities](../claims/higher-proficiency-faster-step-responses.md) [~W]
- [Letting learners pace instruction helped on complex material in one experiment, while learner control in general showed almost no effect across 18 studies](../claims/learner-paced-beats-system-paced-complex-material.md) [~W]

## Design

### Sequence
1. Break the content into small, sequential frames, each presenting a bit of information.
2. Require the learner to make an active response (write or select an answer) before moving on.
3. Reveal the correct answer or confirm the learner's response immediately.
4. For branching/intrinsic programming: route the learner to a remedial frame on an incorrect response, or let them skip ahead on strong performance.
5. Let the learner progress through the full sequence at their own pace, rather than a fixed group pace.

### Elements Used
- [Self-Paced Learning](../elements/self-paced-learning.md)
- [Immediate Feedback](../elements/immediate-feedback.md)
- [Practice](../elements/practice.md)

### Affordances
- [Mastery Learning](../principles/mastery-learning.md)
- [Immediate Feedback](../principles/immediate-feedback.md)

### Personalization
- Branching (intrinsic) programming personalizes the path itself, sending struggling learners to remedial frames and letting confident learners skip ahead
- Even linear programming personalizes pace, since every learner moves through the same steps but on their own schedule

## Related Patterns

- [Game-Based Mastery Learning](game-based-mastery-learning.md) — a modern descendant that adds game mechanics (streaks, levels, adaptive difficulty) to the same small-step, immediate-feedback, self-paced core PI established
- [Tutor-led strategy set for effective adult language lessons: structure, small steps, early success, continuous practice and constant re-use](../designs/tutor-led-strategies-adult-language-lessons.md)

## Examples
- Skinner's original teaching-machine frames and linear programmed textbooks (e.g., *English 2600*)
- Crowder's AutoTutor and TutorText branching programmed books
- The Personalized System of Instruction ("Keller Plan"): self-paced units with a mastery test and proctor feedback before advancing

## Key Sources
- Molenda, M. (2008). The programmed instruction era: When effectiveness mattered. *TechTrends, 52*(2), 52–58. Republished in R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/programmed_instruction](https://edtechbooks.org/lidtfoundations/programmed_instruction)
- Skinner, B. F. (1954). The science of learning and the art of teaching. *Harvard Educational Review, 24*, 86–97.
- Keller, F. S. (1968). Goodbye, teacher... *Journal of Applied Behavior Analysis, 1*, 78–79.
-->
