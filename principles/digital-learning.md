---
type: principle
id: digital-learning
aliases: [shared-whiteboard-dual-cohort-workspace]
title: Digital Learning
description: "Putting part of a course on a digital tool is expected to help only through the method it makes affordable (more practice with feedback, adaptive hints, prompts to explain, visible progress) and not through the medium itself; no claim here tests a digital against a non-digital version of the same method."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-05
sources:
  - id: hodges-2020
    resource: "https://er.educause.edu/articles/2020/3/the-difference-between-emergency-remote-teaching-and-online-learning"
    title: "Hodges, C., Moore, S., Lockee, B., Trust, T., & Bond, A. (2020). The difference between emergency remote teaching and online learning. *EDUCAUSE Review*"
    author: "Hodges, C., Moore, S., Lockee, B., Trust, T., & Bond, A"
  - id: qi-2022
    resource: "https://doi.org/10.29140/jaltcall.v18n1.569"
    title: "Qi, G. Y., & Wang, Y. (2022). Challenges and responses: A Complex Dynamic Systems approach to exploring language teacher agency in a blended classroom. The JALT CALL Journal, 18(1). https://doi.org/10.29140/jaltcall.v18n1.569"
    author: "Qi, G. Y., & Wang, Y"
---

# Digital Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 28 claims (13 for, 14 mixed, 1 against) · 39 studies (11 causal, 9 quant-synthesis, 6 review, 6 theoretical, 3 associational, 2 qualitative, 2 design), `q1`–`q4` · 9 of 39 report an effect size · 20 claims rest on one study

## Conditional relationship

Digital learning is a **medium**: devices, platforms and networks. It is not a method. This page covers when to put part of a course onto a digital tool, and how to credit the result. The relationship it proposes is conditional. Suppose a course needs a function that cannot be supplied well enough face to face: more practice items with feedback on each one, adaptive selection of the next task, replay of an explanation, access across time and place, or a record of every attempt. Moving that function onto a digital tool **that carries a named method** (practice with feedback, contingent hints, prompts to explain, visible progress against a criterion) is then expected to raise outcomes on an aligned measure (`general-achievement`, `immediate-performance`). The comparison is the same course without that function. Moving the **same method** from paper or a classroom to a screen is not expected to change learning by itself. Any gain should be credited to the method and to the extra practice, time or feedback the medium made affordable. The medium gets credit for making those affordable, not for the learning.

**No claim in the wiki tests a digital medium against a non-digital one with the method, time and materials held equal and equivalence shown.** The evidence points the other way, at confounds. In a meta-analysis reported second-hand, computer-based instruction's advantage over conventional teaching fell from .51 SD to .13 when the same teacher taught both versions. Intelligent tutoring systems beat *other* computer-based instruction (g = 0.57): same medium, different method. Blended courses beat face-to-face ones (g+ = 0.35), but with extra time and resources in the blended arms. A methodological synthesis argues that whole-medium comparisons confound medium with method, novelty and population, and that their usual "no significant difference" result is uninterpretable, not proof of equivalence. The steps below are therefore a **default design**. They follow the method claims, not the medium.

Several converted pages own narrower relationships that sit inside this one, and this page does not repeat them:

- [Adaptive Learning](adaptive-learning.md): choosing each learner's next task from their responses, which is the strongest reason to go digital at scale.
- [Immediate Feedback](immediate-feedback.md): when corrective feedback should arrive. Software makes immediate feedback cheap, but that does not make it the right timing.
- [Multimedia Learning](multimedia-learning.md): pairing words with pictures.
- [Self-Regulated Learning](self-regulated-learning.md): the pacing and persistence that self-paced online work demands.
- [Cognitive-Load Management](cognitive-load-management.md): interface and presentation load.

The [Blended Learning pattern](../patterns/blended-learning.md) holds how to divide a course between online and in-person work, and flipped learning is one configuration inside it. This page decides **whether a digital tool earns its place and what it is for**. Those pages decide how the method runs.

## Default design, while the relationship is untested

The earlier page's guidance is kept here as a concrete default, and each step states its evidence status. Durations and thresholds are untested proposals to set locally and record.

1. **Name the method before the tool.** Write one line for each digital component: "this tool lets learners do *X* (method) *n* times a week, which we cannot supply in class because *Y*". Drop any component for which no X or Y can be written, for example a lecture posted as a video with nothing asked of the learner, or a worksheet turned into a PDF. Basis: [Media comparison studies produce uninterpretable "no significant difference" findings.](../claims/media-comparison-studies-produce-uninterpretable-results.md) [+M] and [The measured advantage of computer-based instruction over conventional teaching shrinks when the same teacher teaches both versions](../claims/cbi-advantage-shrinks-same-teacher-comparisons.md) [+M], which argue that the medium alone does little. The one-line test itself is an untested proposal.
2. **Use the medium for practice with feedback on each item.** Short sets of 8–15 items, about 10–20 minutes, 2–4 times a week. Show the correct answer and a reason after each item, or after the set where [Immediate Feedback](immediate-feedback.md) argues for a delay. Do not cut practice out of an online lesson to save time. Basis: [In one experiment with 256 undergraduates, computer-based lesson versions that included practice produced significantly higher posttest scores than versions without practice](../claims/practice-presence-raises-cbi-posttest-achievement.md) [+M] (one computer-based lesson; horizon not reported). The set sizes and frequency are untested proposals.
3. **Ask for explanations, not only answers.** Add one "why does this step work?" or "what principle applies here?" prompt for every three to five items. Allow a short typed answer or a choice among explanations, and fade the prompts once a learner's explanations are accurate. Basis: [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] (a meta-analysis across task types and levels, g = .55). It is not specific to digital delivery: the prompt does the work, whatever medium carries it.
4. **Give hints that respond to the attempt.** After an error, give a cue first, then a more specific hint, then the worked step. Give less help after a success. Where a tutoring system is available for the domain, it bundles this with practice and a model of the task. Basis: [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M] (mostly one-to-one human tutoring; carried here to software) and [Adaptive learning improves outcomes](../claims/adaptive-learning-improves-outcomes.md) [+S] (intelligent tutoring beat teacher-led large-group instruction, other computer-based instruction and textbooks, but not human tutoring or small groups). Which part of the bundle does the work is not shown.
5. **Show progress against a stated criterion, and ask the learner to act on it.** A dashboard of completed items is not enough. Show accuracy on each skill against a target, and once a week ask "what will you practise next, and why?". Basis: [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M] (a review and a theoretical synthesis; no test of dashboards).
6. **Keep the interface and the materials lean.** Use one place to find the week's work, the same layout each week, and no decorative media. Segment long videos into parts of a few minutes, each with a question after it. Basis: [Cognitive Overload Degrades Learning](../claims/cognitive-overload-degrades-learning.md) [~M] (reviews of multimedia design: cutting extraneous load helped most on complex material) and [Segmenting Improves Multimedia Learning](../claims/segmenting-improves-multimedia-learning.md) [+M] (the effect held for system-paced segments). Interface load as such is untested here.
7. **Make the first week a contact week.** Most of the extra attrition online in the one study recorded here came before instruction began. In week 1, give a short task that needs a reply from a person (a post the instructor answers within 24–48 hours, or a 15-minute live call), and check that every learner has logged in and completed one item by day 3. Basis: [Online attrition during Orientation Week is twice that of onground classes' first week](../claims/orientation-week-attrition-double-online.md) [~M] (university continuing education, observational). The contact task and its timings are untested proposals.
8. **Check access before launch.** Find out who has which device, what bandwidth, and what accessibility needs. Provide an offline or printable route for each required activity, and do not grade on anything that some learners cannot reach. This step is an untested proposal, kept from the earlier page.
9. **Plan the arc across weeks.**
   - Weeks 1–2: the contact task, items close to a worked example, the full hint ladder, and feedback after every item.
   - Weeks 3–6: hints on request only, a self-check before submitting (compare with a worked answer, or check an inverse), and explanation prompts reduced to one per set.
   - Final weeks: mixed items in the form of the target assessment, no hints, feedback after the set.
   - Open each week with three or four unaided items on the previous week's material. Move a learner to the next unit, or to extension work, once they reach about 80% on two consecutive unaided sets, so that learners who are already accurate are not held back ([Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M]).
   - The arc, the 80% figure and the two-set rule are untested proposals.
10. **Evaluate the method, not the medium.** Do not report "digital versus traditional". Compare two versions of the same digital component that differ in one thing (with or without explanation prompts, immediate or end-of-set feedback). Or compare the component with the same method on paper at the same time on task. Measure unaided performance at least once after a delay. Basis: [Media comparison studies produce uninterpretable "no significant difference" findings.](../claims/media-comparison-studies-produce-uninterpretable-results.md) [+M]. The specific evaluation plan is a proposal.

When a condition is not met: if no function can be named that the classroom cannot supply, keep the activity off-screen. If access is uneven and cannot be fixed, make the digital route optional and equivalent, not required.

## Fitting the design to a situation

The three facts that most change the decision:

- **What the digital tool will do that cannot be done otherwise.** More practice with feedback, adaptive selection, replay, or reach to learners who cannot attend all justify it. "Engagement" or "modernising" do not. If the brief omits it, ask: which activity gets more attempts, more feedback or more access because it is on a screen, and how many more?
- **Whether a person is in the loop, and how quickly.** Fully self-paced work with no human contact loses learners early and puts the whole burden of pacing on them. If the brief omits it, ask: who will see a learner's work or absence in the first week, and how soon will they respond?
- **The learners' access and their starting response on the task.** Devices, bandwidth and accessibility needs decide what can be required. Prior knowledge decides how much guidance the software should give. If the brief omits it, ask: can every learner reach the platform on the device they have, and can they do one item of the target kind unaided now?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are `novice` on the task | Use items close to worked examples, the full cue–hint–worked-step ladder, an explanation prompt every three to five items, and feedback on every item | [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M] (one-to-one tutoring, carried to software) |
| Learners are `advanced` on the task, or succeed unaided on the first set | Remove most hints and prompts; give mixed, whole-task items and feedback only on request | [Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M] (a cognitive-load review; gives no crossover point) |
| Learners are `child` (primary age) | Use short sessions (10 minutes or less), supervised by an adult in the room; give feedback that needs little reading; avoid open typed answers | untested proposal |
| Learners are `adult` or professionals studying around work | Use short sets on a phone that can be done in one sitting, and tasks taken from their own work; keep the first-week contact task | untested proposal; contact task from [Online attrition during Orientation Week is twice that of onground classes' first week](../claims/orientation-week-attrition-double-online.md) [~M] (university continuing education) |
| Goal is a `procedure` or `verbal-association` with checkable answers | Put the bulk of practice online with automatic checking; use an intelligent tutor if one exists for the domain | [Adaptive learning improves outcomes](../claims/adaptive-learning-improves-outcomes.md) [+S] (tutoring-system meta-analyses; gains smaller on standardised than on locally developed tests) |
| Goal is a `concept`, a `principle`, or transfer | Keep answer-checking, but add explanation prompts and changed items; hold discussion of reasons in a live or threaded session | [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] (not specific to digital delivery) |
| Setting is `online-self-paced`, no teacher present | Add the contact task in week 1, a fixed weekly rhythm with a deadline, visible progress against a criterion, and a weekly plan prompt; check logins by day 3 | [Self-regulated learning interventions have a moderate effect (0.65) on learning outcomes in online and blended environments](../claims/srl-interventions-moderate-effect-online-blended.md) [+M] (15 studies); a diary alone did not help in one course ([A daily learning diary alone (Group D) did not produce statistically significant pre-post gains on any measured outcome in an online mathematics preparation course](../claims/learning-diary-alone-no-significant-srl-gains-online-math-prep-course.md) [~M]) |
| `classroom`, one teacher and a large group, devices available | Use the software for individual practice and hints while the teacher watches the class's results live and goes to those who are stuck; use class time for what the software cannot do (discussion of reasons, whole tasks) | untested proposal; contingent-support evidence is one-to-one ([Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M]) |
| Time is short (one or two sessions) | Do not introduce a new platform; use the classroom, or one familiar tool, for practice with feedback | untested proposal; learning a new interface costs time the method needs |
| Note-taking during lectures on laptops or tablets is planned | Ask learners to summarise in their own words, not transcribe; do not ban devices on the strength of the longhand evidence | [Laptop note-takers transcribed more verbatim and did worse on conceptual questions than longhand note-takers in one set of experiments, but a direct replication found no consistent difference in test performance](../claims/laptop-notes-verbatim-shallower.md) [~M] (college students; a replication found no consistent difference) |
| Stakes are high, or the final assessment is unaided and supervised | Judge readiness only on unaided items done without hints; keep a log of hints used; give at least one supervised check in the final assessment's format | untested proposal |
| Access is uneven (shared devices, poor bandwidth, accessibility needs) | Make every required activity available offline or on paper, use low-bandwidth formats (text, short audio, captioned video), and grade nothing that some learners cannot reach | untested proposal, from the earlier page |

Six of the twelve rows rest on a claim. Two more cite one only for part of the move (the adult row's contact task) or for its limit (the classroom row). Two of the six were tested in digital settings: self-regulation interventions online and blended, and laptop note-taking. The tutoring-system row was tested on software, but the software bundles several methods. The others carry a method claim from tutoring, cognitive-load research or self-explanation studies into a digital setting and say so. The remaining rows are untested proposals.

## Observation, state and explanation

What can be observed in a digital setting: logins and their times, items attempted, answers, time per item, hints requested and at what level, which explanation prompts were answered and how, and drops. "Disengaged", "not self-regulating" and "the platform works" are inferred states. Logs record what the software saw. A long time on an item can mean thinking, a distraction or a closed tab.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Learner never logs in after enrolling, or stops in week 1 | Access problem (device, bandwidth, password); unclear what to do first; no human contact yet; competing commitments | Contact the learner directly in week 1. Ask whether they could reach the platform and what they would need, and record the reason. |
| High scores on practice items, low on the unaided check | Hints carried the answers; the items were too close to worked examples; answers were looked up or guessed | Compare accuracy on items done with no hints against those with hints, and give a changed item with no hints available. |
| Many attempts in quick succession on the same item | Guessing through the options; misunderstanding of the feedback; a habit carried over from games | Delay feedback until an explanation has been typed, then check whether accuracy changes. Ask what the feedback meant. |
| Completes everything, but answers explanation prompts with one word or a copy of the question | Prompt seen as busywork; does not know what a good explanation looks like; language or typing barrier | Show one model explanation, offer a choice among explanations, or accept a voice note; compare the quality afterwards. |
| Outcomes better than last year's face-to-face cohort | More practice or time on task; a different cohort; a different test; a novelty effect; a real method effect | Compare time on task and the test used; run the same items on paper with a matched group; re-check after the novelty has worn off. |

These rows are proposals and have not been tested with learners as diagnostics. A probe changes what it measures, so record each one, and keep the explanations that remain open rather than choosing the one whose name fits.

## Evidence and qualifications

No claim compares a digital and a non-digital version of the same method, time and materials and shows equivalence or a difference. The claims below bear on the attribution rule, and on what methods do inside the medium.

- [Media comparison studies produce uninterpretable "no significant difference" findings.](../claims/media-comparison-studies-produce-uninterpretable-results.md) [+M]. Three sources, all argument or review rather than new data: Clark (1983), Levie and Dickie (1973), and Lockee, Moore and Burton (2001). They argue that comparing whole media confounds medium with method, novelty and learner population. They also argue that "no significant difference" is an inconclusive null, not equivalence. The claim page notes Kozma's (1994) counter-argument: some media afford methods that are impractical in others. This page takes that as the reason a medium can still matter, through what it makes affordable. The marker is held below the claim's cap because its sources are arguments.
- [The measured advantage of computer-based instruction over conventional teaching shrinks when the same teacher teaches both versions](../claims/cbi-advantage-shrinks-same-teacher-comparisons.md) [+M]. A 1983 Harvard Project Zero paper reports Kulik et al.'s (1980) meta-analysis of college computer-based teaching. The average advantage was .51 SD with different teachers and .13 SD when the same teacher taught both versions. This is one second-hand report, and its source was published before most current platforms existed.
- [Adaptive learning improves outcomes](../claims/adaptive-learning-improves-outcomes.md) [+S]. Two meta-analyses, read from abstracts. In one, intelligent tutoring systems beat teacher-led large-group instruction (g = 0.42), other computer-based instruction (g = 0.57) and textbooks or workbooks (g = 0.35), but not individual human tutoring (g = -0.11) or small groups (g = 0.05). The other reports a median 0.66 SD over conventional instruction, with smaller gains on standardised tests. The comparison with other computer-based instruction is the clearest case here of method mattering within one medium. The comparison with human tutoring suggests the method, not the computer, carries the effect. [Adaptive Learning](adaptive-learning.md) holds the model.
- [Blended Learning Improves Outcomes](../claims/blended-learning-improves-outcomes.md) [~M]. A meta-analysis (Means et al. 2013) of higher-education and training studies: blended against face-to-face g+ = 0.35 over 23 contrasts, and purely online against face-to-face g+ = 0.14. The authors say the blended arms usually also had extra time and resources, so the format cannot be credited.
- [In one experiment with 256 undergraduates, computer-based lesson versions that included practice produced significantly higher posttest scores than versions without practice](../claims/practice-presence-raises-cbi-posttest-achievement.md) [+M]. Six versions of one computer-based lesson, randomly assigned within pretest blocks. The versions with practice outperformed those without. Within one medium, what the lesson asks learners to do changed the result. No effect size or horizon is reported.
- [The computer-based implementation showed no significant difference from individual paper-based work with brief written answers](../claims/computer-based-no-better-than-individual-paper.md) [~M]. Introductory physics tutorials: a computer-based group (N = 29) against an earlier individual paper-based group (N = 76), with no significant difference in understanding of kinetic energy or momentum (p = 0.64 and p = 0.40), despite richer onscreen feedback. The groups come from different studies, and equivalence was not tested. A sibling claim from the same study, [A computer-based implementation of the tutorial yields the lowest post-test scores, statistically lower on momentum than every other style in the same study and the prior study's ideal implementation](../claims/computer-based-tutorial-implementation-lowest-posttest.md) [~M], shows the computer version scoring lowest of all the implementations studied, below the group-based styles.
- **Limiting:** [Online continuing education courses show lower persistence than comparable onground courses (79% vs 84%) over eight quarters](../claims/online-continuing-education-persistence-lower-than-onground.md) [-M] and [Online attrition during Orientation Week is twice that of onground classes' first week](../claims/orientation-week-attrition-double-online.md) [~M]. Enrolment records from one university extension programme, observational: attrition was 21% online against 15% onground. After instruction began, drop rates were essentially the same ([After instruction has begun, drop rates are essentially the same in online and onground continuing education classes](../claims/no-drop-rate-difference-after-instruction-starts.md) [~M]). The medium carries a cost of its own, concentrated before learners meet the instructor. That is why the default design makes week 1 a contact week.
- **Limiting:** [Laptop note-takers transcribed more verbatim and did worse on conceptual questions than longhand note-takers in one set of experiments, but a direct replication found no consistent difference in test performance](../claims/laptop-notes-verbatim-shallower.md) [~M]. Three experiments with college students found laptop note-takers transcribing more and doing worse on conceptual questions. A direct replication found no consistent difference. A device can invite a less useful behaviour, but the effect is fragile, and the remedy the claim page suggests is a note-taking method, not a device ban.

The learners, outcomes and dates differ widely: college students in the 1970s, physics undergraduates, continuing-education enrolments, tutoring-system studies across levels. So do not rank these by effect size. None measures `delayed-retention` of a digital-versus-non-digital difference.

## Further evidence, not yet read against this model

Claims the earlier page cited, and claims found while rewriting, that bear on parts of the model but have not been read against it in full.

- [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. Cited by the earlier page and used in the default design. A method claim that is independent of medium.
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M]. Cited by the earlier page and used in the default design. Mostly one-to-one human tutoring.
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M]. Cited by the earlier page and used in the default design. A review and a theoretical synthesis, with no test of digital progress displays.
- [Self-regulated learning interventions have a moderate effect (0.65) on learning outcomes in online and blended environments](../claims/srl-interventions-moderate-effect-online-blended.md) [+M]. A meta-analysis of 15 studies in online and blended settings. It bears directly on self-paced digital work; [Self-Regulated Learning](self-regulated-learning.md) holds the model.
- [A daily learning diary alone (Group D) did not produce statistically significant pre-post gains on any measured outcome in an online mathematics preparation course](../claims/learning-diary-alone-no-significant-srl-gains-online-math-prep-course.md) [~M]. One online course: a reflective tool on its own did not help.
- [A tool's effectiveness results from the whole configuration of events, activities, and contexts in which it is used](../claims/tool-effectiveness-depends-on-context-configuration.md) [+W]. Salomon's position, reported second-hand in a conference paper. It states the attribution rule as argument.
- [Salomon distinguishes effects with the computer (system performance) from effects of the computer (cognitive residue on the solo performer)](../claims/effects-with-versus-effects-of-computer.md) [+W]. A conceptual distinction. It is the reason this page judges readiness on unaided items.
- [Technology-supported learning gains depend on the technology being used within student-centered, active-engagement pedagogy](../claims/lab-technology-gains-depend-on-active-engagement-pedagogy.md) [+W]. The authors' interpretation in one physics course, not a tested contrast.
- [Students attributed improved understanding to the discussion process of the implementation model rather than the clicker technology itself](../claims/learning-attributed-to-process-not-technology.md) [+W]. Student self-reports from one course. It bears on attribution only as learners' perception.
- [Students prioritize teacher interaction for face-to-face learning but content interaction for online learning](../claims/interaction-priority-f2f-teacher-online-content.md) [~W]. Student rankings across four universities, associational. It bears on what learners expect from each mode.
- [Online learning communities do not simply emerge; they must be designed for and scaffolded through teaching and assessment activities](../claims/online-communities-must-be-designed-and-scaffolded.md) [+W]. Authors' reflection on fully online units, coded q1.
- [Human embodiment in video: perceived social presence benefits learning ratings, but instructor-face inclusion shows no significant learning-performance difference, and learners prefer human over robot presenters with mixed recall](../claims/human-embodiment-video-presence-effects.md) [~W]. A review of video-lecture studies: preference without a performance difference.
- [In one 30-student study of high-school English learners (Lu 2008, reported in a review), vocabulary learned by mobile phone showed greater gains than vocabulary learned from print](../claims/sms-vocabulary-learning-beats-paper-materials.md) [~W]. One 30-student study reported second-hand in a review. It is a whole-medium comparison of exactly the kind the media-comparison claim calls uninterpretable.
- [Iterative Task Redesign Increased Engagement](../claims/iterative-task-redesign-increased-engagement.md) [+M]

## Objective and learner-valued goal

The designer's objective is usually unaided performance on a representative task at a stated horizon. Ask separately what learners want from the digital part. Some want to fit study around work or care, some want to replay what they missed, some want to avoid being seen getting things wrong, and some want simply to finish the module. Agreement and divergence are both observations. A learner who values flexibility may welcome self-paced sets and drop out without a fixed weekly rhythm. One who values contact may experience a platform with no person in it as being left alone.

For example, a nurse in a continuing-education course may want something to check doses on during a shift, while the designer's objective is unaided calculation accuracy at the end of the module. The software practice serves the objective. A short reference card with worked examples, used and then removed for the unaided check, serves the learner's goal without letting assisted success stand in for the capability. Record both, so that completion rates are not read as the capability either party wanted.

## What would revise this model?

The model should change in four cases:

- If studies that hold method, time and materials equal and are powered to detect a modest difference find a consistent effect of the medium itself (in either direction), the medium should be credited, and "medium, not method" should become a stated exception.
- If the same digital method performs consistently worse than its paper or classroom version (as one physics comparison hints) for reasons the interface explains, interface load becomes part of the model, not a footnote.
- If the first-week contact task does not reduce early attrition when tried, drop it and look for the cause in access or enrolment.
- If tutoring systems' gains vanish on standardised and delayed measures, the case for software-delivered adaptive practice narrows to aligned, immediate outcomes.

Do not protect the model by calling every failure "poor implementation" after the fact. Record the configuration before the results.

Access, use, assisted success, unaided immediate performance, delayed retention and transfer are separate outcomes. The present evidence establishes no dose of digital practice, no threshold for moving on, and no effect of the medium itself.

## Related Principles
- [Flipped Learning](flipped-learning.md) — digital delivery often makes pre-class access and replayable initial exposure possible
- [Learner Choice](autonomy.md) — platforms can support alternative pathways, modalities, and pacing
- [Multimedia Learning](multimedia-learning.md) — digital environments frequently instantiate multimedia principles in practice
- [Adaptive Learning](adaptive-learning.md) — owns choosing each learner's next task from their responses, the main reason to put practice on software
- [Immediate Feedback](immediate-feedback.md) — owns when feedback should arrive; software makes it immediate by default, which is a choice to make, not a given
- [Self-Regulated Learning](self-regulated-learning.md) — owns the pacing and persistence that self-paced digital work demands
- [Cognitive-Load Management](cognitive-load-management.md) — interface and presentation load in digital materials

## Examples

- [PeerWise online tool for student-authored multiple-choice question repositories](../elements/peerwise-online-mcq-authoring-tool.md)
- [Invite students to co-facilitate tasks by typing content into the shared whiteboard or chat](../strategies/student-co-facilitation-via-shared-chat-typing.md)
- [CWPT Learning Management System (CWPT–LMS) software support](../elements/cwpt-learning-management-system.md)

### Illustrative

**[Flipped Learning](../patterns/flipped-classroom.md)** — Learners access short digital explanations before class, then use live time for practice, discussion, and feedback. The gain comes from redesigning class time, not just posting videos.

**[ASSISTments](https://www.assistments.org)** — A digital math platform that combines practice, hints, and immediate feedback. It shows the value of digital learning when the environment supports reasoning and feedback rather than just answer submission.

**[Shared Documents](../elements/shared-documents.md)** — Learners jointly annotate, revise, and synthesize ideas in a shared digital workspace, turning the platform into a medium for collaboration rather than just content storage.

**[Blended Learning](../patterns/blended-learning.md)** — the pattern for dividing a course between online and in-person work, so that each mode does what the other cannot.

## Key Sources
- Means, B., Toyama, Y., Murphy, R., Bakia, M., & Jones, K. (2010). *Evaluation of evidence-based practices in online learning*. U.S. Department of Education.
- Hodges, C., Moore, S., Lockee, B., Trust, T., & Bond, A. (2020). The difference between emergency remote teaching and online learning. *EDUCAUSE Review*. [https://er.educause.edu/articles/2020/3/the-difference-between-emergency-remote-teaching-and-online-learning](https://er.educause.edu/articles/2020/3/the-difference-between-emergency-remote-teaching-and-online-learning)
- Qi, G. Y., & Wang, Y. (2022). Challenges and responses: A Complex Dynamic Systems approach to exploring language teacher agency in a blended classroom. The JALT CALL Journal, 18(1). https://doi.org/10.29140/jaltcall.v18n1.569

<!-- deprecated 2026-10-05: superseded by the conditional model above. The previous body, kept verbatim.

## Description
Digital learning is the principle of using digital environments and tools to support access, interaction, practice, and feedback in instruction.

## Implications

Digital learning matters when technology changes what learners can access, rehearse, replay, produce, or collaborate on. At its best, it is not a separate pedagogy but a delivery and interaction layer that makes strong instructional design more available: replayable explanation, adaptive practice, distributed collaboration, multimodal representation, and flexible pacing. Digital systems are especially useful when they make progress visible and usable for learner adjustment [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M], when they provide adaptive hints or support that responds to performance [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M], and when they prompt annotation, explanation, or reasoning rather than passive consumption [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]. At its worst, digital delivery simply digitizes weak instruction. The quality of the learning design still matters more than the presence of devices or platforms.

### Context
#### Requirements
- **Technology chosen for instructional value, not novelty** — the tool has to solve a real access, practice, feedback, or collaboration problem
- **Reliable access and usability** — digital learning weakens quickly when learners cannot consistently access the platform, content, or support
- **A pedagogical structure that the technology actually serves** — digital delivery is most effective when paired with clear learning goals, activity design, and feedback loops
#### Constraints
- **Technology can amplify poor design** — moving lectures, worksheets, or busywork online does not improve them automatically
- **Access inequities matter** — bandwidth, device quality, accessibility, and home conditions can become instructional barriers
- **Tool complexity can add extraneous load** — learners may spend attention managing systems rather than understanding content

### Target Learners
- Learners who benefit from replayable explanations, flexible pacing, and digital access to materials
- Learners in blended, online, or technology-rich environments where collaboration and feedback are partly mediated by platforms
- Learners with access needs that are better supported through multimodal or digital delivery

### Target Learning Objectives
- Increase access to content, practice, and feedback
- Support interaction, production, and collaboration across time and place
- Enable more flexible pacing and multimodal engagement when the design justifies it

### Theory
#### Supporting
- [Multimedia Learning](multimedia-learning.md) — many digital environments coordinate words, visuals, audio, and interaction in ways that can improve comprehension when designed well
- [Multimodal Instruction](multimodal-instruction.md) — digital platforms often make multiple modes practical at scale
- [Self-Regulated Learning](../theories/self-regulated-learning.md) — replayable content, progress indicators, and flexible pacing can support learner planning and monitoring

#### Contradicting / Qualifying
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — digital environments can either reduce or increase load depending on interface design, modality choices, and tool complexity

### Claims
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M] — digital systems are often most effective when they make progress visible and usable for learner adjustment
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M] — adaptive hints, feedback, and platform supports can help when they respond to learner performance rather than staying generic
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — digital tools that prompt explanation, annotation, or reasoning can outperform passive content delivery

## Related Principles
- [Flipped Learning](flipped-learning.md) — digital delivery often makes pre-class access and replayable initial exposure possible
- [Learner Choice](autonomy.md) — platforms can support alternative pathways, modalities, and pacing
- [Multimedia Learning](multimedia-learning.md) — digital environments frequently instantiate multimedia principles in practice

## Examples

- [PeerWise online tool for student-authored multiple-choice question repositories](../elements/peerwise-online-mcq-authoring-tool.md)

### Illustrative

**[Flipped Learning](../patterns/flipped-classroom.md)** — Learners access short digital explanations before class, then use live time for practice, discussion, and feedback. The gain comes from redesigning class time, not just posting videos.

**[ASSISTments](https://www.assistments.org)** — A digital math platform that combines practice, hints, and immediate feedback. It shows the value of digital learning when the environment supports reasoning and feedback rather than just answer submission.

**[Shared Documents](../elements/shared-documents.md)** — Learners jointly annotate, revise, and synthesize ideas in a shared digital workspace, turning the platform into a medium for collaboration rather than just content storage.

## Key Sources
- Means, B., Toyama, Y., Murphy, R., Bakia, M., & Jones, K. (2010). *Evaluation of evidence-based practices in online learning*. U.S. Department of Education.
- Hodges, C., Moore, S., Lockee, B., Trust, T., & Bond, A. (2020). The difference between emergency remote teaching and online learning. *EDUCAUSE Review*. [https://er.educause.edu/articles/2020/3/the-difference-between-emergency-remote-teaching-and-online-learning](https://er.educause.edu/articles/2020/3/the-difference-between-emergency-remote-teaching-and-online-learning)

-->

<!-- merged 2026-10-07 from principles/shared-whiteboard-dual-cohort-workspace ("Use a shared synchronous whiteboard as the common workspace for both face-to-face and online cohorts"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Use a shared synchronous whiteboard as the common workspace for both face-to-face and online cohorts

> **Principle** · [All principles](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 qualitative), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The article shows a teacher uploading slides to the Collaborate whiteboard rather than projecting them, so that "both cohorts to see, write and highlight the contents on the slides to help with their task completion". The whiteboard served as a shared learning space, reduced multitasking and device-switching, allowed anonymous colour-coded student notetaking, and sat centrally in the interface to draw both cohorts' attention.

## Design Implications

### Context
#### Requirements
- A synchronous platform with a shared, annotatable whiteboard visible to both cohorts
#### Constraints
- Described for a dual-cohort blended classroom using Blackboard Collaborate; anonymity depended on students choosing their own colour codes

### Target Learners
- higher-education language students in blended face-to-face and online cohorts

### Target Learning Objectives
- task participation and interaction
- comprehension support during synchronous tasks
- peer notetaking and feedback

### Claims
- [Iterative Task Redesign Increased Engagement](../claims/iterative-task-redesign-increased-engagement.md) [+M]

## Related Principles
- 

## Examples

- [Invite students to co-facilitate tasks by typing content into the shared whiteboard or chat](../strategies/student-co-facilitation-via-shared-chat-typing.md)

## Key Sources
- Qi, G. Y., & Wang, Y. (2022). Challenges and responses: A Complex Dynamic Systems approach to exploring language teacher agency in a blended classroom. The JALT CALL Journal, 18(1). https://doi.org/10.29140/jaltcall.v18n1.569
-->
