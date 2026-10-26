---
type: principle
id: digital-learning
aliases: [shared-whiteboard-dual-cohort-workspace, tablets-expand-science-education-approaches, open-licensing-teachers-as-designers]
title: Digital Learning
description: "Putting part of a course on a digital tool is expected to help only through the method it makes affordable (more practice with feedback, adaptive hints, prompts to explain, visible progress) and not through the medium itself; no claim here tests a digital against a non-digital version of the same method."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-19
sources:
  - id: hodges-2020
    resource: "https://er.educause.edu/articles/2020/3/the-difference-between-emergency-remote-teaching-and-online-learning"
    title: "Hodges, C., Moore, S., Lockee, B., Trust, T., & Bond, A. (2020). The difference between emergency remote teaching and online learning. *EDUCAUSE Review*"
    author: "Hodges, C., Moore, S., Lockee, B., Trust, T., & Bond, A"
  - id: qi-2022
    resource: "https://doi.org/10.29140/jaltcall.v18n1.569"
    title: "Qi, G. Y., & Wang, Y. (2022). Challenges and responses: A Complex Dynamic Systems approach to exploring language teacher agency in a blended classroom. The JALT CALL Journal, 18(1). https://doi.org/10.29140/jaltcall.v18n1.569"
    author: "Qi, G. Y., & Wang, Y"
  - id: vom-lara-2014
    resource: "https://arxiv.org/abs/1405.6581"
    title: "V.O.M. Lara, D. F. Amaral, D. Faria, and L. P. Vieira. (2014). Demonstrations of magnetic phenomena: Measuring the air permeablity using tablets. https://arxiv.org/abs/1405.6581"
    author: V.O.M. Lara, D. F. Amaral, D. Faria, and L. P. Vieira
  - id: wee-loo-kang-2013
    resource: "http://ictconnection.opal.moe.edu.sg/cos/o.x?ptid=711&c=/ictconnection/ictlib&func=view&rid=82"
    title: "Wee Loo Kang. (2013). Open Source Physics. i in Practice 1(1), 58-63. http://ictconnection.opal.moe.edu.sg/cos/o.x?ptid=711&c=/ictconnection/ictlib&func=view&rid=82"
    author: Wee Loo Kang
---

# Digital Learning

> **Principle** · [All principles](index.md)
> **Evidence** · 73 claims (35 for, 34 mixed, 4 against) · 82 studies (20 causal, 20 review, 13 theoretical, 12 quant-synthesis, 6 associational, 6 design, 5 qualitative), `q1`–`q4` · 13 of 82 report an effect size · 62 claims rest on one study

## Conditional relationship

Digital learning is a **medium**: devices, platforms and networks. It is not a method. This page covers when to put part of a course onto a digital tool, and how to credit the result. The relationship it proposes is conditional. Suppose a course needs a function that cannot be supplied well enough face to face: more practice items with feedback on each one, adaptive selection of the next task, replay of an explanation, access across time and place, or a record of every attempt. Moving that function onto a digital tool **that carries a named method** (practice with feedback, contingent hints, prompts to explain, visible progress against a criterion) is then expected to raise outcomes on an aligned measure (`general-achievement`, `immediate-performance`). The comparison is the same course without that function. Moving the **same method** from paper or a classroom to a screen is not expected to change learning by itself. Any gain should be credited to the method and to the extra practice, time or feedback the medium made affordable. The medium gets credit for making those affordable, not for the learning.

**One claim in the wiki tests a digital medium against a non-digital one with the method held equal, and it found no difference; none shows equivalence.** Triona and Klahr (2003) taught 92 fourth- and fifth-graders to design unconfounded experiments with the same instruction on physical ramps or on a computer simulation. Both groups gained by the same amount (no effect of condition, F = .01), and a week later the children trained on the computer designed as many good experiments with the physical ramps as those trained on them. That is one study of one science skill, and a nonsignificant difference is not a test of equivalence. The rest of the evidence points at confounds. In a meta-analysis reported second-hand, computer-based instruction's advantage over conventional teaching fell from .51 SD to .13 when the same teacher taught both versions. In the 2009 US Department of Education meta-analysis, online-versus-face-to-face effects were +0.20 where curriculum and instruction were judged near-identical and +0.42 where they differed. A systematic review of immersive virtual reality comparisons found 40% confounded by instructional method or content, and where learning activities were not controlled the confound favoured the VR arm in 14 of 17 comparisons. Intelligent tutoring systems beat *other* computer-based instruction (g = 0.57): same medium, different method. Blended courses beat face-to-face ones (g+ = 0.35), but with extra time and resources in the blended arms. A methodological synthesis argues that whole-medium comparisons confound medium with method, novelty and population, and that their usual "no significant difference" result is uninterpretable, not proof of equivalence. The steps below are therefore a **default design**. They follow the method claims, not the medium.

Several converted pages own narrower relationships that sit inside this one, and this page does not repeat them:

- [Adaptive Learning](adaptive-learning.md): choosing each learner's next task from their responses, which is the strongest reason to go digital at scale.
- [Immediate Feedback](immediate-feedback.md): when corrective feedback should arrive. Software makes immediate feedback cheap, but that does not make it the right timing.
- [Multimedia Learning](multimedia-learning.md): pairing words with pictures.
- [Self-Regulated Learning](self-regulated-learning.md): the pacing and persistence that self-paced online work demands.
- [Cognitive-Load Management](cognitive-load-management.md): interface and presentation load.

The [Blended Learning pattern](../patterns/blended-learning.md) holds how to divide a course between online and in-person work, and flipped learning is one configuration inside it. This page decides **whether a digital tool earns its place and what it is for**. Those pages decide how the method runs.

## Default design, while the relationship is untested

The earlier page's guidance is kept here as a concrete default, and each step states its evidence status. Durations and thresholds are untested proposals to set locally and record.

1. **Name the method before the tool.** Write one line for each digital component: "this tool lets learners do *X* (method) *n* times a week, which we cannot supply in class because *Y*". Drop any component for which no X or Y can be written, for example a lecture posted as a video with nothing asked of the learner, or a worksheet turned into a PDF. Basis: [Media comparison studies produce uninterpretable "no significant difference" findings.](../claims/media-comparison-studies-produce-uninterpretable-results.md) [+M] and [The measured advantage of computer-based instruction over conventional teaching shrinks when the same teacher teaches both versions](../claims/cbi-advantage-shrinks-same-teacher-comparisons.md) [+M], which argue that the medium alone does little. A randomised evaluation of One Laptop per Child in rural Peru, reported second-hand, raised computers per student from 0.12 to 1.18 and found no effect on mathematics or language scores after fifteen months ([Distributing hardware without capable software produced no measurable effect on mathematics or language scores in a large randomized evaluation, as the article reports citing Cristia et al.](../claims/olpc-randomized-hardware-null-no-score-effect.md) [+W]): devices with no named method attached. The one-line test itself is an untested proposal.
2. **Use the medium for practice with feedback on each item.** Short sets of 8–15 items, about 10–20 minutes, 2–4 times a week. Show the correct answer and a reason after each item, or after the set where [Immediate Feedback](immediate-feedback.md) argues for a delay. Do not cut practice out of an online lesson to save time. Basis: [In one experiment with 256 undergraduates, computer-based lesson versions that included practice produced significantly higher posttest scores than versions without practice](../claims/practice-presence-raises-cbi-posttest-achievement.md) [+M] (one computer-based lesson; horizon not reported). The set sizes and frequency are untested proposals.
3. **Ask for explanations, not only answers.** Add one "why does this step work?" or "what principle applies here?" prompt for every three to five items. Allow a short typed answer or a choice among explanations, and fade the prompts once a learner's explanations are accurate. Basis: [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] (a meta-analysis across task types and levels, g = .55). It is not specific to digital delivery: the prompt does the work, whatever medium carries it. Inside one tutoring system, a classroom experiment found that students asked to explain their steps in the Geometry Cognitive Tutor gained more on reason-giving and "not enough information" items than students who only solved problems ([Static self-explanation prompts in the Geometry Cognitive Tutor produced greater gains on Reason and Not Enough Info test items than problem-solving practice alone](../claims/self-explanation-prompts-geometry-tutor-robust-learning.md) [+M]; no effect size printed).
4. **Give hints that respond to the attempt.** After an error, give a cue first, then a more specific hint, then the worked step. Give less help after a success. Where a tutoring system is available for the domain, it bundles this with practice and a model of the task. Basis: [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M] (mostly one-to-one human tutoring; carried here to software) and [Intelligent tutoring systems improve achievement over non-individualised instruction](../claims/adaptive-learning-improves-outcomes.md) [+S] (intelligent tutoring beat teacher-led large-group instruction, other computer-based instruction and textbooks, but not human tutoring or small groups). A meta-analysis of 144 experiments found students given computer-based scaffolds in STEM did better on cognitive tests than those without them, with wide variation between studies ([Computer-based scaffolding shows a consistently positive effect on cognitive outcomes in STEM education](../claims/computer-based-scaffolding-positive-cognitive-outcomes-stem.md) [+M]). Within one tutoring system, adding real-time feedback to the same adaptive diagnostic tutor raised progression on a SOLO-scored mathematics assessment (d = 0.73, reported in a review; [Automated real-time feedback in an adaptive diagnostic ITS produced greater progression on a SOLO-based mathematics assessment than the same system without real-time feedback](../claims/real-time-feedback-its-solo-progression-advantage.md) [+W]). Which part of the bundle does the work is otherwise not shown. **If a generative-AI tutor carries the hints, set it to withhold final answers and give hints instead.** In a trial reported second-hand by several papers, unrestricted access to a general chatbot raised practice scores by 48% and left students 17% worse on the unaided exam once it was removed, while a tutor rebuilt to withhold answers removed most of that loss ([Review reports a field experiment in which GPT access improved supported practice but was followed by poorer unaided test performance, mitigated by a guarded tutor](../claims/gpt4-access-harms-learning-after-withdrawal.md) [~M]). The model was the same in both arms; what learners were asked to do with it changed the result.
5. **Show progress against a stated criterion, and ask the learner to act on it.** A dashboard of completed items is not enough. Show accuracy on each skill against a target, and once a week ask "what will you practise next, and why?". Basis: [Self-regulated learning models treat self-monitoring as a core process through which learners notice gaps and adjust strategy](../claims/self-monitoring-improves-self-regulation.md) [~M] (a review and a theoretical synthesis; no test of dashboards).
6. **Keep the interface and the materials lean.** Use one place to find the week's work, the same layout each week, and no decorative media. Segment long videos into parts of a few minutes, each with a question after it. Basis: [Cognitive Overload Degrades Learning](../claims/cognitive-overload-degrades-learning.md) [~M] (reviews of multimedia design: cutting extraneous load helped most on complex material) and [Segmenting Improves Multimedia Learning](../claims/segmenting-improves-multimedia-learning.md) [+M] (the effect held for system-paced segments). A review of learner-controlled hypermedia names disorientation, distraction and cognitive overload as the usability problems that make its benefits hard to show ([Usability problems — disorientation, distraction, and cognitive overload — hinder demonstrating effectiveness of self-controlled hypermedia learning](../claims/hypermedia-usability-problems-hinder-effectiveness.md) [~W]; an argument, no effect sizes). On video, a review reports that Guo, Kim and Rubin found short videos more engaging and classroom recordings weak online ([Guo et al. found engagement depends on video production style: short videos, talking heads on slides, Khan-style drawing more engaging than slides or coding, classroom recording weak online](../claims/guo-video-style-engagement-findings.md) [+W]; engagement, not learning, and edX science and engineering courses only), and that including the instructor's face showed no significant learning-performance difference, though some learners prefer it ([Human embodiment in video: perceived social presence benefits learning ratings, but instructor-face inclusion shows no significant learning-performance difference, and learners prefer human over robot presenters with mixed recall](../claims/human-embodiment-video-presence-effects.md) [~W]; second-hand, equivalence not tested). So a talking head is a preference to offer, not a learning requirement. Interface load as such is untested here.
7. **Make the first week a contact week.** Most of the extra attrition online in the one study recorded here came before instruction began. In week 1, give a short task that needs a reply from a person (a post the instructor answers within 24–48 hours, or a 15-minute live call), and check that every learner has logged in and completed one item by day 3. Basis: [Online attrition during Orientation Week is twice that of onground classes' first week](../claims/orientation-week-attrition-double-online.md) [~M] (university continuing education, observational). The contact task and its timings are untested proposals.
8. **Check access before launch.** Find out who has which device, what bandwidth, and what accessibility needs. Provide an offline or printable route for each required activity, and do not grade on anything that some learners cannot reach. This step is an untested proposal, kept from the earlier page. The condition it answers is documented: national survey figures put individual internet use in rural Bangladesh at about half the urban rate ([Individual internet penetration in rural Bangladesh (36.5%) is about half the urban rate (71.4%), which one case-study preprint argues puts cloud-dependent AI tools out of reach for rural learners](../claims/rural-urban-connectivity-exclusion-bangladesh.md) [~W]; one country, and an offline route was not tested).
9. **Plan the arc across weeks.**
   - Weeks 1–2: the contact task, items close to a worked example, the full hint ladder, and feedback after every item.
   - Weeks 3–6: hints on request only, a self-check before submitting (compare with a worked answer, or check an inverse), and explanation prompts reduced to one per set.
   - Final weeks: mixed items in the form of the target assessment, no hints, feedback after the set.
   - Open each week with three or four unaided items on the previous week's material. Move a learner to the next unit, or to extension work, once they reach about 80% on two consecutive unaided sets, so that learners who are already accurate are not held back ([Instructional guidance that helps novices can become redundant or counterproductive as expertise grows.](../claims/expertise-reversal-effect.md) [~M]).
   - The arc, the 80% figure and the two-set rule are untested proposals.
10. **Evaluate the method, not the medium.** Do not report "digital versus traditional". Compare two versions of the same digital component that differ in one thing (with or without explanation prompts, immediate or end-of-set feedback). Or compare the component with the same method on paper at the same time on task. Measure unaided performance at least once after a delay. If a tool is compared with a conventional version, write down the activities each arm does before the results come in, because unequal activities inflate the newer medium's apparent advantage. Basis: [Media comparison studies produce uninterpretable "no significant difference" findings.](../claims/media-comparison-studies-produce-uninterpretable-results.md) [+M]; [Effect sizes were larger in studies where online and face-to-face conditions differed in curriculum materials and instructional approach (+0.42) than where curriculum and instruction were nearly identical (+0.20; Q = 5.40, p < .05).](../claims/curriculum-equivalence-moderates-effect-size.md) [+M]; 40% of IVR-vs-conventional comparisons had at least one confound related to instructional method and content [+M] and [When activities were not controlled, the confound favored the IVR condition in 14 of 17 comparisons](../claims/activity-confounds-favor-ivr-condition.md) [+M] (a systematic review of 50 STEM comparisons). The specific evaluation plan is a proposal.

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
| Learners are `child` (primary age) | Use short sessions (10 minutes or less), supervised by an adult in the room; give feedback that needs little reading; avoid open typed answers. A simulation can stand in for physical materials if the same instruction goes with it | session length and supervision are untested proposals; the substitution rests on [Physical and virtual instructional materials are equally effective for teaching fourth- and fifth-graders to design unconfounded experiments when instructional method is controlled](../claims/physical-virtual-materials-equal-cvs-learning.md) [+M] (one science skill; no difference found, equivalence not tested). Online-versus-classroom comparisons for school-age learners are almost absent: [A systematic search found almost no rigorous studies contrasting online and face-to-face instruction for K–12 students: none with computable effect sizes through 2006, and only five meeting meta-analysis criteria through July 2008.](../claims/few-rigorous-k12-online-studies.md) [~M] |
| Learners are `adult` or professionals studying around work | Use short sets on a phone that can be done in one sitting, and tasks taken from their own work; keep the first-week contact task | untested proposal; contact task from [Online attrition during Orientation Week is twice that of onground classes' first week](../claims/orientation-week-attrition-double-online.md) [~M] (university continuing education) |
| Goal is a `procedure` or `verbal-association` with checkable answers | Put the bulk of practice online with automatic checking; use an intelligent tutor if one exists for the domain | [Intelligent tutoring systems improve achievement over non-individualised instruction](../claims/adaptive-learning-improves-outcomes.md) [+S] (tutoring-system meta-analyses; gains smaller on standardised than on locally developed tests) |
| Goal is a `concept`, a `principle`, or transfer | Keep answer-checking, but add explanation prompts and changed items; hold discussion of reasons in a live or threaded session | [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] (not specific to digital delivery) |
| Setting is `online-self-paced`, no teacher present | Add the contact task in week 1, a fixed weekly rhythm with a deadline, visible progress against a criterion, and a weekly plan prompt; check logins by day 3 | [Self-regulated learning interventions have a moderate effect (0.65) on learning outcomes in online and blended environments](../claims/srl-interventions-moderate-effect-online-blended.md) [+M] (15 studies); a diary alone did not help in one course ([A daily learning diary alone (Group D) did not produce statistically significant pre-post gains on any measured outcome in an online mathematics preparation course](../claims/learning-diary-alone-no-significant-srl-gains-online-math-prep-course.md) [~M]) |
| `classroom`, one teacher and a large group, devices available | Use the software for individual practice and hints while the teacher watches the class's results live and goes to those who are stuck; use class time for what the software cannot do (discussion of reasons, whole tasks) | untested proposal; contingent-support evidence is one-to-one ([Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M]) |
| Time is short (one or two sessions) | Do not introduce a new platform; use the classroom, or one familiar tool, for practice with feedback | untested proposal; learning a new interface costs time the method needs |
| Note-taking during lectures on laptops or tablets is planned | Ask learners to summarise in their own words, not transcribe; do not ban devices on the strength of the longhand evidence | [Laptop note-takers transcribed more verbatim and did worse on conceptual questions than longhand note-takers in one set of experiments, but a direct replication found no consistent difference in test performance](../claims/laptop-notes-verbatim-shallower.md) [~M] (college students; a replication found no consistent difference) |
| Stakes are high, or the final assessment is unaided and supervised | Judge readiness only on unaided items done without hints; keep a log of hints used; give at least one supervised check in the final assessment's format | untested proposal; its reasoning is Salomon's distinction between what a learner does with the tool and what remains when working alone ([Salomon distinguishes effects with the computer (system performance) from effects of the computer (cognitive residue on the solo performer)](../claims/effects-with-versus-effects-of-computer.md) [+W], a conceptual argument reported second-hand) |
| Access is uneven (shared devices, poor bandwidth, accessibility needs) | Make every required activity available offline or on paper, use low-bandwidth formats (text, short audio, captioned video), and grade nothing that some learners cannot reach. Check that the software runs on the phones learners own, since out-of-class work may otherwise depend on finding a computer | untested proposal, from the earlier page; the condition is documented in [Individual internet penetration in rural Bangladesh (36.5%) is about half the urban rate (71.4%), which one case-study preprint argues puts cloud-dependent AI tools out of reach for rural learners](../claims/rural-urban-connectivity-exclusion-bangladesh.md) [~W] (survey figures for one country; no offline design tested) and, for adult education, [Learners used products outside class despite infrastructure limits: 65% of surveyed students reported doing software work outside class while mobile access was largely unavailable](../claims/adult-ed-out-of-class-use-mobile-gap.md) [~W] (a survey at fourteen sites; smartphone ownership figures are second-hand) |
| A generative-AI chatbot or tutor is part of the plan | Use a tutor set to withhold final answers and give graded hints, not a general chatbot; judge readiness only on unaided items with the tool removed, both straight after and a week later; ask learners to check its output, and record errors it makes | [Review reports a field experiment in which GPT access improved supported practice but was followed by poorer unaided test performance, mitigated by a guarded tutor](../claims/gpt4-access-harms-learning-after-withdrawal.md) [~M] (one high-school mathematics trial, reported second-hand); a structured tutor raised post-test scores over a no-tutor arm in one small preregistered field experiment ([Access to a structured conversational AI tutor increased post-test content scores over a no-AI holdout with ambient consumer AI available](../claims/structured-ai-tutor-raises-post-test-scores-field-experiment.md) [+M]; 46 analysed). Unrestricted access in a 35-minute learning phase raised unaided scores straight after (0.28 SD) and by 0.21 SD a week later, not significant ([AI access raises immediate unaided test scores by 7.2 percentage points (0.28 SD) after a timed learning phase](../claims/genai-access-raises-immediate-test-scores.md) [~M], [One week later, the AI-access group's lead on unaided assessments shrinks to 3.9 pp (0.21 SD), short of statistical significance (p = 0.068)](../claims/genai-learning-gain-persists-one-week.md) [~M]), so unrestricted access does not always harm; the configuration and the task decide. Errors and lack of real-time response were the weaknesses learners named in one music study ([Students identified weaknesses in the AI feedback model: lack of real-time feedback, software/economic access barriers, and occasional incorrect or inconsistent outputs](../claims/genai-feedback-weaknesses-realtime-and-errors.md) [~W]) |

Seven of the thirteen rows rest on a claim. Five more cite one only for part of the move (the adult row's contact task, the child row's substitution of a simulation for physical materials), for its limit (the classroom row), for its reasoning (the stakes row) or for the condition it answers (the access row). Three of the seven were tested in digital settings: self-regulation interventions online and blended, laptop note-taking, and generative-AI tutors, whose trials are few, short and mostly reported second-hand. The tutoring-system row was tested on software, but the software bundles several methods. The others carry a method claim from tutoring, cognitive-load research or self-explanation studies into a digital setting and say so. The short-time row is an untested proposal.

## Observation, state and explanation

What can be observed in a digital setting: logins and their times, items attempted, answers, time per item, hints requested and at what level, which explanation prompts were answered and how, and drops. "Disengaged", "not self-regulating" and "the platform works" are inferred states. Logs record what the software saw. A long time on an item can mean thinking, a distraction or a closed tab.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Learner never logs in after enrolling, or stops in week 1 | Access problem (device, bandwidth, password); unclear what to do first; no human contact yet; competing commitments | Contact the learner directly in week 1. Ask whether they could reach the platform and what they would need, and record the reason. |
| High scores on practice items, low on the unaided check | Hints carried the answers; the items were too close to worked examples; answers were looked up or guessed; an AI assistant did the work (the pattern in [the GPT-4 trial](../claims/gpt4-access-harms-learning-after-withdrawal.md) [~M]) | Compare accuracy on items done with no hints against those with hints, and give a changed item with no hints or AI available. Ask the learner to explain one practice answer in their own words. |
| Many attempts in quick succession on the same item | Guessing through the options; misunderstanding of the feedback; a habit carried over from games | Delay feedback until an explanation has been typed, then check whether accuracy changes. Ask what the feedback meant. |
| Completes everything, but answers explanation prompts with one word or a copy of the question | Prompt seen as busywork; does not know what a good explanation looks like; language or typing barrier | Show one model explanation, offer a choice among explanations, or accept a voice note; compare the quality afterwards. |
| Outcomes better than last year's face-to-face cohort | More practice or time on task; a different cohort; a different test; a novelty effect; a real method effect | Compare time on task and the test used; run the same items on paper with a matched group; re-check after the novelty has worn off. |

These rows are proposals and have not been tested with learners as diagnostics. A probe changes what it measures, so record each one, and keep the explanations that remain open rather than choosing the one whose name fits.

## Evidence and qualifications

One claim compares a digital and a non-digital version of the same method and finds no difference; none shows equivalence. The claims below bear on the attribution rule, and on what methods do inside the medium.

- [Physical and virtual instructional materials are equally effective for teaching fourth- and fifth-graders to design unconfounded experiments when instructional method is controlled](../claims/physical-virtual-materials-equal-cvs-learning.md) [+M]. Triona and Klahr (2003), *Cognition and Instruction*: 92 children, the same instruction with physical ramps or a computer simulation. The proportion of unconfounded experiments rose from .20 to .65 in both, with no effect of condition (F(1, 90) = .01) and no interaction, and a week later the simulation-trained children did as well with physical ramps. It is the closest the wiki has to the test this page asks for. It is one study of one skill, and a nonsignificant difference is not equivalence.
- **Uncontrolled comparisons inflate the medium.** In the US Department of Education meta-analysis of online learning ([Means et al. 2009](https://www.ed.gov/about/offices/list/opepd/ppss/reports.html)), curriculum and instructional equivalence was the only methodological moderator that mattered: +0.20 where online and face-to-face arms taught nearly the same thing, +0.42 where they differed ([Effect sizes were larger in studies where online and face-to-face conditions differed in curriculum materials and instructional approach (+0.42) than where curriculum and instruction were nearly identical (+0.20; Q = 5.40, p < .05).](../claims/curriculum-equivalence-moderates-effect-size.md) [+M]). The +0.20 is not zero, and what remains in it (time, feedback, the instructor) is not separated. Of 13 online practice variables, only a blended approach and more time on task changed effectiveness ([Of 13 online learning practice variables examined, only use of a blended approach and expanded time on task significantly influenced effectiveness; the other 11 did not.](../claims/eleven-of-thirteen-practice-variables-nonsignificant.md) [~M]), which fits crediting the time the medium buys. A systematic review of 50 immersive-VR comparisons in STEM coded 40% as confounded by method or content, and where activities were not controlled the VR arm came out ahead in 14 of 17, mostly because only the VR arm had learning activities (40% of IVR-vs-conventional comparisons had at least one confound related to instructional method and content [+M]; [When activities were not controlled, the confound favored the IVR condition in 14 of 17 comparisons](../claims/activity-confounds-favor-ivr-condition.md) [+M]). Courseware in a national grant programme showed positive average impacts against face-to-face versions of a course but not against same-modality versions, and positive impacts at four-year institutions but not two-year colleges ([Courseware impact varied by context: positive on average in 4-year institutions but insignificant in 2-year colleges, more positive in biology, psychology, and math/statistics, and positive when the comparison course was face-to-face rather than the same modality.](../claims/ngcc-impact-moderators-context.md) [~W]; moderator summaries with no effect sizes).
- [Distributing hardware without capable software produced no measurable effect on mathematics or language scores in a large randomized evaluation, as the article reports citing Cristia et al.](../claims/olpc-randomized-hardware-null-no-score-effect.md) [+W]. One Laptop per Child in 318 rural Peruvian schools, reported second-hand: a tenfold rise in computers per student and no effect on test scores after fifteen months. A medium delivered with no method changed nothing measured.

- [Media comparison studies produce uninterpretable "no significant difference" findings.](../claims/media-comparison-studies-produce-uninterpretable-results.md) [+M]. Three sources, all argument or review rather than new data: Clark (1983), Levie and Dickie (1973), and Lockee, Moore and Burton (2001). They argue that comparing whole media confounds medium with method, novelty and learner population. They also argue that "no significant difference" is an inconclusive null, not equivalence. The claim page notes Kozma's (1994) counter-argument: some media afford methods that are impractical in others. This page takes that as the reason a medium can still matter, through what it makes affordable. The marker is held below the claim's cap because its sources are arguments.
- [The measured advantage of computer-based instruction over conventional teaching shrinks when the same teacher teaches both versions](../claims/cbi-advantage-shrinks-same-teacher-comparisons.md) [+M]. A 1983 Harvard Project Zero paper reports Kulik et al.'s (1980) meta-analysis of college computer-based teaching. The average advantage was .51 SD with different teachers and .13 SD when the same teacher taught both versions. This is one second-hand report, and its source was published before most current platforms existed.
- [Intelligent tutoring systems improve achievement over non-individualised instruction](../claims/adaptive-learning-improves-outcomes.md) [+S]. Two meta-analyses, read from abstracts. In one, intelligent tutoring systems beat teacher-led large-group instruction (g = 0.42), other computer-based instruction (g = 0.57) and textbooks or workbooks (g = 0.35), but not individual human tutoring (g = -0.11) or small groups (g = 0.05). The other reports a median 0.66 SD over conventional instruction, with smaller gains on standardised tests. The comparison with other computer-based instruction is the clearest case here of method mattering within one medium. The comparison with human tutoring suggests the method, not the computer, carries the effect. [Adaptive Learning](adaptive-learning.md) holds the model.
- [Blended Learning Improves Outcomes](../claims/blended-learning-improves-outcomes.md) [~M]. A meta-analysis ([Means et al. 2013](https://doi.org/10.1177/016146811311500307)) of higher-education and training studies: blended against face-to-face g+ = 0.35 over 23 contrasts, and purely online against face-to-face g+ = 0.14. The authors say the blended arms usually also had extra time and resources, so the format cannot be credited.
- [In one experiment with 256 undergraduates, computer-based lesson versions that included practice produced significantly higher posttest scores than versions without practice](../claims/practice-presence-raises-cbi-posttest-achievement.md) [+M]. Six versions of one computer-based lesson, randomly assigned within pretest blocks. The versions with practice outperformed those without. Within one medium, what the lesson asks learners to do changed the result. No effect size or horizon is reported.
- [The computer-based implementation showed no significant difference from individual paper-based work with brief written answers](../claims/computer-based-no-better-than-individual-paper.md) [~M]. Introductory physics tutorials: a computer-based group (N = 29) against an earlier individual paper-based group (N = 76), with no significant difference in understanding of kinetic energy or momentum (p = 0.64 and p = 0.40), despite richer onscreen feedback. The groups come from different studies, and equivalence was not tested. A sibling claim from the same study, [A computer-based implementation of the tutorial yields the lowest post-test scores, statistically lower on momentum than every other style in the same study and the prior study's ideal implementation](../claims/computer-based-tutorial-implementation-lowest-posttest.md) [~M], shows the computer version scoring lowest of all the implementations studied, below the group-based styles.
- [In one 30-student study of high-school English learners (Lu 2008, reported in a review), vocabulary learned by mobile phone showed greater gains than vocabulary learned from print](../claims/sms-vocabulary-learning-beats-paper-materials.md) [~W]. The one digital-against-print result in the wiki that favours the digital arm. It is a review's two-sentence report of a 30-student, two-group study, with no effect size, assignment method or description of what the messages contained. It compares whole media, so it does not test the medium with the method held equal, and it leaves the relationship untested.
- **The attribution rule as argument.** [A tool's effectiveness results from the whole configuration of events, activities, and contexts in which it is used](../claims/tool-effectiveness-depends-on-context-configuration.md) [+W] (Salomon's position and the varied Logo results, reported second-hand in a conference paper) and [The authors of one physics-course study attribute its technology-supported gains to the student-centred, active-engagement pedagogy the technology was used within](../claims/lab-technology-gains-depend-on-active-engagement-pedagogy.md) [+W] (the authors' interpretation of one physics course; the lecture-based contrast was not run) state the rule this page applies, without testing it. In one mathematics course for pre-service teachers, 57.1% of one instructor's respondents credited discussing the content, not the clickers, for their better understanding ([Students attributed improved understanding to the discussion process of the implementation model rather than the clicker technology itself](../claims/learning-attributed-to-process-not-technology.md) [+W]). That is learners' perception, not a measured contrast.
- **Same medium, different use.** In one blended language class, a teacher changed a weekly peer-feedback task three times, from feedback typed in chat, to notetaking in chat, to anonymous notetaking on a shared whiteboard, and classes became progressively more engaged ([In a single-teacher case study, redesigning a peer-feedback task produced more specific and varied student notes, which the authors read as a more engaged class](../claims/iterative-task-redesign-increased-engagement.md) [+W]; class recordings and stimulated recall, engagement only). The tools stayed the same; what learners were asked to do with them changed the result. Further cases: adaptive, language-processed feedback helped pre-service teachers justify their diagnoses more than static feedback in the same environment ([Pre-service teachers who received NLP-based adaptive feedback were better able to justify their diagnoses than those who received static feedback (reported from Sailer et al.)](../claims/adaptive-feedback-improves-diagnosis-justification.md) [+W]; second-hand, no sample size printed); the same tutor with and without real-time feedback, and with and without self-explanation prompts (steps 3 and 4 above); and the same language model set to give or withhold answers (step 4).
- **Limiting, for AI tutors:** in one single-session classroom study of 98 adolescents using an AI tutor for mathematical modelling, post-test scores fell below pre-test scores (67.5% to 56.9%) ([Post-test mathematics performance was significantly lower than pre-test after AI-tutor use](../claims/post-test-decline-after-ai-tutor-session.md) [-W]). There was no comparison group, so the tool, the test forms and the session cannot be separated, but it is a reason to check unaided performance rather than assume a gain.
- **Courseware in one course:** adaptive courseware in a corequisite statistics course was followed by better course outcomes as the instructor gained experience with it, more so among Pell-eligible and corequisite students ([Adaptive courseware in a corequisite statistics course was associated with improved course outcomes, particularly for Pell-eligible and corequisite students, but effects are confounded with instructor practices](../claims/wileyplus-adaptive-courseware-statistics-outcomes.md) [~W]). Two terms of one instructor's sections, observational: the courseware and the instructor's growing practice are not separated, and the difference between groups describes who gained more, not a cause located in the groups.
- **Limiting:** [Online continuing education courses show lower persistence than comparable onground courses (79% vs 84%) over eight quarters](../claims/online-continuing-education-persistence-lower-than-onground.md) [-M] and [Online attrition during Orientation Week is twice that of onground classes' first week](../claims/orientation-week-attrition-double-online.md) [~M]. Enrolment records from one university extension programme, observational: attrition was 21% online against 15% onground. After instruction began, drop rates were essentially the same ([After instruction has begun, drop rates are essentially the same in online and onground continuing education classes](../claims/no-drop-rate-difference-after-instruction-starts.md) [~M]). The medium carries a cost of its own, concentrated before learners meet the instructor. That is why the default design makes week 1 a contact week.
- **Limiting:** [Laptop note-takers transcribed more verbatim and did worse on conceptual questions than longhand note-takers in one set of experiments, but a direct replication found no consistent difference in test performance](../claims/laptop-notes-verbatim-shallower.md) [~M]. Three experiments with college students found laptop note-takers transcribing more and doing worse on conceptual questions. A direct replication found no consistent difference. A device can invite a less useful behaviour, but the effect is fragile, and the remedy the claim page suggests is a note-taking method, not a device ban.

The learners, outcomes and dates differ widely: college students in the 1970s, physics undergraduates, continuing-education enrolments, tutoring-system studies across levels. So do not rank these by effect size. None measures `delayed-retention` of a digital-versus-non-digital difference.

## The evidence by question

- *Does putting instruction on a digital medium change learning by itself, or only through the method, time and teaching it carries?* [Media comparison studies produce uninterpretable "no significant difference" findings.](../claims/media-comparison-studies-produce-uninterpretable-results.md) [+M]
- *Do learners do as well, and stay as long, in a fully online course as in the same course face to face?* [For college students who can choose between online and in-person sections, taking a course online lowers grades both in that course and in future courses](../claims/online-course-lower-grades-current-and-future.md) [-M]
- *With the method held equal, does a screen version teach as well as a physical one?* [Physical and virtual instructional materials are equally effective for teaching fourth- and fifth-graders to design unconfounded experiments when instructional method is controlled](../claims/physical-virtual-materials-equal-cvs-learning.md) [+M] (no difference found; equivalence not tested)
- *How much of a reported advantage for a new medium is unequal method or content?* [Effect sizes were larger in studies where online and face-to-face conditions differed in curriculum materials and instructional approach (+0.42) than where curriculum and instruction were nearly identical (+0.20; Q = 5.40, p < .05).](../claims/curriculum-equivalence-moderates-effect-size.md) [+M]; [When activities were not controlled, the confound favored the IVR condition in 14 of 17 comparisons](../claims/activity-confounds-favor-ivr-condition.md) [+M]
- *Does using generative AI while learning leave unaided performance higher or lower?* It depends on how the tool is set up: [Review reports a field experiment in which GPT access improved supported practice but was followed by poorer unaided test performance, mitigated by a guarded tutor](../claims/gpt4-access-harms-learning-after-withdrawal.md) [~M]; [AI access raises immediate unaided test scores by 7.2 percentage points (0.28 SD) after a timed learning phase](../claims/genai-access-raises-immediate-test-scores.md) [~M]; [Access to a structured conversational AI tutor increased post-test content scores over a no-AI holdout with ambient consumer AI available](../claims/structured-ai-tutor-raises-post-test-scores-field-experiment.md) [+M]

## Further evidence, not yet read against this model

Claims read against this model that bear on it only at the edges, or not at all. The other claims once listed here, and those the linker added on 2026-10-15 to 2026-10-19, are now cited in the steps, rows and evidence above.

- [Students prioritize teacher interaction for face-to-face learning but content interaction for online learning](../claims/interaction-priority-f2f-teacher-online-content.md) [~W]. Student rankings across four universities, associational. It bears on what learners expect from each mode (the learner-valued goal), not on whether the medium changes learning.
- [Online learning communities do not simply emerge; they must be designed for and scaffolded through teaching and assessment activities](../claims/online-communities-must-be-designed-and-scaffolded.md) [+W]. Authors' reflection on fully online units, coded q1. It bears on community building, which [Social Presence](social-presence.md) and [Community of Inquiry](community-of-inquiry.md) hold, more than on this page's attribution rule.
- [Students preferred taking tests with technology and showed favorability toward the technology-enhanced performance task, citing interactivity and animations that help visualize and work through problems](../claims/students-prefer-technology-enhanced-task-interactivity-animation.md) [+W]. Interview data from one white paper, coded q1. Preference only; no learning outcome, so it does not bear on the relationship.
- [The authors of one robot-projection study interpret co-located AI guidance as most useful when instructions and task share a spatial frame, as in drawing](../claims/spatial-colocation-benefit-task-dependent.md) [+W]. The authors' interpretation of one desk-robot study. It concerns where guidance appears within a digital setup for spatial tasks such as drawing, a narrow interface choice, and does not compare a digital with a non-digital version of a method.
- [Chatbot-based instruction enhanced secondary students' learning experience by enabling self-paced study with less stress, time savings, and maintained motivation](../claims/chatbot-enhances-learning-experience-self-paced.md) [+W]. Read 2026-10-19: a quasi-experiment with 109 Moroccan secondary students in three classes, digital content plus a chatbot against a traditional class. It reports learners' experience (pace, stress, motivation) with no test statistics, and it changes medium and method together, so it does not test the relationship.
- [In one RCT, a content-rich prompt-engineered generative AI chat tutor improved performance and engagement in a Harvard physics course](../claims/genai-chat-tutor-rct-physics-improved-performance.md) [+W]. Read 2026-10-19: a review's one-sentence report of Kestin et al., with no design details or effect size. It agrees with the generative-AI row (a tutor built around content and a method, not a bare chatbot) but adds nothing that row does not already rest on.
- [Meta-analytic evidence reviewed reports medium-to-large positive effects of AI-enabled adaptive learning on cognitive outcomes (g = 0.50–0.70)](../claims/ai-adaptive-learning-medium-large-effects-reviewed.md) [+W] and [Adaptive learning systems report academic performance gains of 15–25% and engagement increases of up to 40%](../claims/adaptive-learning-gains-15-25-percent.md) [~W]. Read 2026-10-19: two reviews passing on other syntheses' figures, unexamined, and the second in percentages, not effect sizes. They bear on [Adaptive Learning](adaptive-learning.md), which owns that relationship, and do not separate method from medium.
- [A DLS with multiple scaffolds improved achievement and SRL attitudes, with high-achieving students beating traditional teaching but not flipped classroom](../claims/multiple-scaffolds-dls-achievement-srl.md) [~W]. Read 2026-10-19: one three-class experiment reported in a scoping review. The scaffolded digital system bundled self-regulation prompts, online collaboration, presentations and teacher scaffolding, and did not differ from a flipped class among high achievers. It fits the page's rule (a bundle of methods, not the system, beat traditional teaching) without adding a condition.
- [LLMs can deliver scalable, personalized, interactive feedback almost instantly, reducing dependency on teacher availability and supporting self-regulated learning in large courses](../claims/llms-scalable-personalized-feedback-large-courses.md) [+W]. Read 2026-10-19: a literature review's summary, no effect sizes. It names what the medium makes affordable (feedback at any hour, at scale), which is the page's account of where a medium earns credit; it does not show the feedback helps learning.
- [Sharing a projected display with multiple mice produced significant collaborative-learning gains for a whole classroom](../claims/multiple-mice-shared-display-collaborative-gains.md) [~W]. Read 2026-10-19: an editorial's report of a Chilean classroom study, no effect size. A collaboration design on one shared screen; it bears on collaborative learning more than on this page's attribution rule.
- [A 2024 vendor white paper cites research that avatars provide social presence and that realistic avatars in intelligent tutoring systems can increase student-tutor engagement](../claims/avatar-social-presence-increases-tutor-engagement.md) [~W]. Read 2026-10-19: a vendor's citations of older work, engagement and presence only. It bears on [Social Presence](social-presence.md); step 6 already treats a presenter's face as a preference, not a learning requirement.
- [MAIC-UI, generating interactive STEM courseware from instructor documents, reported gains in learning agency in classroom deployment (attributed)](../claims/maic-ui-learning-agency-gains-attributed.md) [~W]. Read 2026-10-19: a one-line background citation with no design or statistics. A tool for authoring courseware; no learning outcome to place in the model.
- [Graduate students can effectively develop interactive educational online software modules as a curriculum component of an advanced science course](../claims/graduate-students-develop-interactive-modules-as-course-project.md) [~W] (not about this page). Read 2026-10-19: fifteen students in one course built software modules as a graded project. It is about learning by producing, not about delivering instruction on a digital medium.
- [Emerging empirical studies report positive associations between generative AI use and international-student adaptation](../claims/ai-use-positive-adaptation-associations.md) [~W] (not about this page). Read 2026-10-19: second-hand cross-sectional associations with sociocultural adaptation abroad, not learning from instruction.
- [Tablet Magnetometer Linear B Current Coil](../claims/tablet-magnetometer-linear-b-current-coil.md) [+M], [Tablet Demo Set Estimates Air Permeability](../claims/tablet-demo-set-estimates-air-permeability.md) [+M], [The magnet data cannot determine air permeability; only the magnet's dipole moment can be estimated](../claims/magnet-case-cannot-determine-air-permeability.md) [+W] and [Magnetic field falls off as the inverse cube of axial distance for both a coil and a magnet](../claims/magnetic-field-inverse-cube-axial-distance-coil-magnet.md) [+W] (not about this page). Read 2026-10-19: from one physics demonstration paper (Lara et al. 2014), carried here when a fragment page was folded in. They report how accurately a tablet's magnetometer measures a field, not anything learners learned; the demonstration set is listed under Examples.
- [A Singapore teacher community has remixed 75 EJS models and lesson packages toward a national digital library](../claims/osp-community-remixed-75-ejs-models.md) [+W]
- [The OSP approach helps users overcome barriers in creating, using and scaling up meaningful ICT use in education](../claims/osp-overcomes-ict-barriers.md) [+W]

## Objective and learner-valued goal

The designer's objective is usually unaided performance on a representative task at a stated horizon. Ask separately what learners want from the digital part. Some want to fit study around work or care, some want to replay what they missed, some want to avoid being seen getting things wrong, and some want simply to finish the module. Agreement and divergence are both observations. A learner who values flexibility may welcome self-paced sets and drop out without a fixed weekly rhythm. One who values contact may experience a platform with no person in it as being left alone.

For example, a nurse in a continuing-education course may want something to check doses on during a shift, while the designer's objective is unaided calculation accuracy at the end of the module. The software practice serves the objective. A short reference card with worked examples, used and then removed for the unaided check, serves the learner's goal without letting assisted success stand in for the capability. Record both, so that completion rates are not read as the capability either party wanted.

## What would revise this model?

The model should change in five cases:

- If studies that hold method, time and materials equal and are powered to detect a modest difference find a consistent effect of the medium itself (in either direction), the medium should be credited, and "medium, not method" should become a stated exception. The one such study in the wiki (Triona and Klahr, physical against virtual materials) found none; an equivalence test with a stated margin would settle more than another nonsignificant difference.
- If generative-AI tutors set to withhold answers fail to protect unaided performance across further trials, or unrestricted access consistently helps delayed unaided performance, the generative-AI row changes.
- If the same digital method performs consistently worse than its paper or classroom version (as one physics comparison hints) for reasons the interface explains, interface load becomes part of the model, not a footnote.
- If the first-week contact task does not reduce early attrition when tried, drop it and look for the cause in access or enrolment.
- If tutoring systems' gains vanish on standardised and delayed measures, the case for software-delivered adaptive practice narrows to aligned, immediate outcomes.

Do not protect the model by calling every failure "poor implementation" after the fact. Record the configuration before the results.

Access, use, assisted success, unaided immediate performance, delayed retention and transfer are separate outcomes. The present evidence establishes no dose of digital practice, no threshold for moving on, and no effect of the medium itself.

## Claims

- [Technology can remove geographical barriers and allow rural and external students to engage in WIL activities](../claims/ewil-removes-geographical-barriers.md) [~W]
- [ITS augmentation: meta-analyses find medium to large learning benefits of ITS over unsupported learning and small to medium gains over less adaptive computer-assisted learning](../claims/its-augmentation-benefits-over-unsupported-learning.md) [~M]
- [Meta-analysis attributes a medium effect of ICT use on learning that dissipates and vanishes in studies assessing intervals longer than a year](../claims/ict-learning-medium-effect-vanishes-beyond-one-year.md) [-W]

## Related Principles
- [Flipped Learning](flipped-learning.md) — digital delivery often makes pre-class access and replayable initial exposure possible
- [Learner Choice](autonomy.md) — platforms can support alternative pathways, modalities, and pacing
- [Multimedia Learning](multimedia-learning.md) — digital environments frequently instantiate multimedia principles in practice
- [Adaptive Learning](adaptive-learning.md) — owns choosing each learner's next task from their responses, the main reason to put practice on software
- [Immediate Feedback](immediate-feedback.md) — owns when feedback should arrive; software makes it immediate by default, which is a choice to make, not a given
- [Self-Regulated Learning](self-regulated-learning.md) — owns the pacing and persistence that self-paced digital work demands
- [Cognitive-Load Management](cognitive-load-management.md) — interface and presentation load in digital materials

## Examples

- [PeerWise online tool for student-authored multiple-choice question repositories](../products/peerwise.md)
- [Invite students to co-facilitate tasks by typing content into the shared whiteboard or chat](../strategies/student-co-facilitation-via-shared-chat-typing.md)
- [CWPT Learning Management System (CWPT–LMS) software support](../products/cwpt-learning-management-system-cwptlms.md)
- [Blended Cognitive Tutor® implementation alternating collaborative textbook periods with adaptive software lab periods](../strategies/cognitive-tutor-blended-textbook-software-schedule.md)
- [Tablet-based magnetic-field demonstration set (coil circuit, ruler, book, MagnetMeter app)](../elements/tablet-magnetometer-demonstration-set.md)
- [Extend tablet magnetometer experiments to other current geometries](../strategies/extend-magnetometer-experiments-other-geometries.md)
- [Quantum Randi Challenge: a modifiable computer game teaching quantum mechanics](../products/quantum-randi-challenge-qrc.md)
- [Use freely available gravitational-wave education tools and resources, including Black Hole Hunter and Einstein's Messengers](../strategies/grav-wave-education-tools-for-educators.md)

### Illustrative

**[Flipped Learning](flipped-learning.md)** — Learners access short digital explanations before class, then use live time for practice, discussion, and feedback. The gain comes from redesigning class time, not just posting videos.

**[ASSISTments](https://www.assistments.org)** — A digital math platform that combines practice, hints, and immediate feedback. It shows the value of digital learning when the environment supports reasoning and feedback rather than just answer submission.

**[Shared Documents](../elements/shared-documents.md)** — Learners jointly annotate, revise, and synthesize ideas in a shared digital workspace, turning the platform into a medium for collaboration rather than just content storage.

**[Blended Learning](../patterns/blended-learning.md)** — the pattern for dividing a course between online and in-person work, so that each mode does what the other cannot.

## Key Sources
- Means, B., Toyama, Y., Murphy, R., Bakia, M., & Jones, K. (2010). *Evaluation of evidence-based practices in online learning*. U.S. Department of Education.
- Hodges, C., Moore, S., Lockee, B., Trust, T., & Bond, A. (2020). The difference between emergency remote teaching and online learning. *EDUCAUSE Review*. [https://er.educause.edu/articles/2020/3/the-difference-between-emergency-remote-teaching-and-online-learning](https://er.educause.edu/articles/2020/3/the-difference-between-emergency-remote-teaching-and-online-learning)
- Qi, G. Y., & Wang, Y. (2022). Challenges and responses: A Complex Dynamic Systems approach to exploring language teacher agency in a blended classroom. The JALT CALL Journal, 18(1). https://doi.org/10.29140/jaltcall.v18n1.569
- V.O.M. Lara, D. F. Amaral, D. Faria, and L. P. Vieira. (2014). Demonstrations of magnetic phenomena: Measuring the air permeablity using tablets. https://arxiv.org/abs/1405.6581
- Triona, L. M., & Klahr, D. (2003). Point and Click or Grab and Heft: Comparing the Influence of Physical and Virtual Instructional Materials on Elementary School Students' Ability to Design Experiments. *Cognition and Instruction, 21*(2), 149–173. https://doi.org/10.1207/s1532690xci2102_02
- Lawson, A. P., Martella, A. M., LaBonte, K., Delgado, C. Y., Zhao, F., Gluck, J. A., Munns, M. E., LeRoy, A. W., & Mayer, R. E. (2024). Confounded or Controlled? A Systematic Review of Media Comparison Studies Involving Immersive Virtual Reality for STEM Education. *Educational Psychology Review*. https://doi.org/10.1007/s10648-024-09908-8
- Belland, B. R., Walker, A. E., Kim, N. J., & Lefler, M. (2017). Synthesizing Results From Empirical Research on Computer-Based Scaffolding in STEM Education: A Meta-Analysis. *Review of Educational Research, 87*(2), 309–344. https://doi.org/10.3102/0034654316670999
- Means, B., Toyama, Y., Murphy, R., Bakia, M., & Jones, K. (2009). *Evaluation of Evidence-Based Practices in Online Learning: A Meta-Analysis and Review of Online Learning Studies*. U.S. Department of Education.
- Wee Loo Kang. (2013). Open Source Physics. i in Practice 1(1), 58-63. http://ictconnection.opal.moe.edu.sg/cos/o.x?ptid=711&c=/ictconnection/ictlib&func=view&rid=82

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

- [PeerWise online tool for student-authored multiple-choice question repositories](../products/peerwise.md)

### Illustrative

**[Flipped Learning](flipped-learning.md)** — Learners access short digital explanations before class, then use live time for practice, discussion, and feedback. The gain comes from redesigning class time, not just posting videos.

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

<!-- merged 2026-10-15 from principles/tablets-expand-science-education-approaches ("Use tablets and smartphones in science education to expand approaches that motivate understanding of physical phenomena"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Use tablets and smartphones in science education to expand approaches that motivate understanding of physical phenomena

> **Principle** · [All principles](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 1 of 1 report an effect size · 4 claims rest on one study

## Description
The article opens with the design rationale that consumer mobile devices can serve as scientific measurement instruments in teaching. It states that "The use of tablets and smartphone in science education expands possibilities for approaches that motivate students to understand better several physical phenomena", and notes tablets were shown as good tools to measure magnetostatic responses. The demonstration set realizes this principle by turning an iPad's magnetometer into a quantitative field probe.

## Design Implications

### Context
#### Requirements
- A tablet or smartphone with a magnetometer and a suitable measurement app.
#### Constraints
- 

### Target Learners
- science students at levels where magnetostatics is taught

### Target Learning Objectives
- conceptual understanding of magnetic phenomena through hands-on measurement

### Claims

- [Tablet Magnetometer Linear B Current Coil](../claims/tablet-magnetometer-linear-b-current-coil.md) [+M]
- [Tablet Demo Set Estimates Air Permeability](../claims/tablet-demo-set-estimates-air-permeability.md) [+M]
- [The magnet data cannot determine air permeability; only the magnet's dipole moment can be estimated](../claims/magnet-case-cannot-determine-air-permeability.md) [+W]
- [Magnetic field falls off as the inverse cube of axial distance for both a coil and a magnet](../claims/magnetic-field-inverse-cube-axial-distance-coil-magnet.md) [+W]

## Related Principles
- 

## Examples

- [Tablet-based magnetic-field demonstration set (coil circuit, ruler, book, MagnetMeter app)](../elements/tablet-magnetometer-demonstration-set.md)
- [Extend tablet magnetometer experiments to other current geometries](../strategies/extend-magnetometer-experiments-other-geometries.md)

## Key Sources
- V.O.M. Lara, D. F. Amaral, D. Faria, and L. P. Vieira. (2014). Demonstrations of magnetic phenomena: Measuring the air permeablity using tablets. https://arxiv.org/abs/1405.6581
-->

<!-- merged 2026-10-19 from principles/open-licensing-teachers-as-designers ("Use open-licensed educational computer models so anyone can freely access and modify resources, building teachers' professionalism as designers"), a narrower page folded into its canonical page (fragment step, two models agreeing or a third settling): its body as it stood. Its bullets this page lacked were added above.

# Use open-licensed educational computer models so anyone can freely access and modify resources, building teachers' professionalism as designers

> **Principle** · [All principles](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article argues that open source licensing of educational computer models/software has opened up tremendous opportunities for learning in the 21st century, since anyone can freely access and modify these resources to suit their teaching and learning needs. Using OSP tools builds and deepens teachers' professionalism as they become designers of learning environments through customisation of existing computer models in the Open Source Physics comPADRE Digital Library Collection.

## Design Implications

### Context
#### Requirements
- access to the Open Source Physics comPADRE Digital Library Collection and the EJS authoring toolkit
#### Constraints
- 

### Target Learners
- physics teachers and students customising and using open-licensed models

### Target Learning Objectives
- customising computer models to suit teaching and learning needs; teacher professional development as designers of learning environments

### Claims

- [A Singapore teacher community has remixed 75 EJS models and lesson packages toward a national digital library](../claims/osp-community-remixed-75-ejs-models.md) [+W]
- [The OSP approach helps users overcome barriers in creating, using and scaling up meaningful ICT use in education](../claims/osp-overcomes-ict-barriers.md) [+W]

## Related Principles
- 

## Examples

- [Quantum Randi Challenge: a modifiable computer game teaching quantum mechanics](../products/quantum-randi-challenge-qrc.md)
- [Use freely available gravitational-wave education tools and resources, including Black Hole Hunter and Einstein's Messengers](../strategies/grav-wave-education-tools-for-educators.md)

## Key Sources
- Wee Loo Kang. (2013). Open Source Physics. i in Practice 1(1), 58-63. http://ictconnection.opal.moe.edu.sg/cos/o.x?ptid=711&c=/ictconnection/ictlib&func=view&rid=82
-->
