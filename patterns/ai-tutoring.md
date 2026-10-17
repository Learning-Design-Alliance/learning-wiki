---
type: pattern
id: ai-tutoring
title: AI Tutoring
description: "A reusable policy for tutoring by software, from step-based intelligent tutoring systems to conversational AI tutors and pedagogical or teachable agents: decide how much the tutor gives away, keep the learner doing the reasoning, judge it on unaided performance rather than assisted practice, and decide when a human tutor or mentor takes over."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-17
grain_size: course
---

# AI Tutoring

> **Pattern** · [All patterns](index.md)

## Description and scope

Tutoring delivered by software rather than a person: step-based intelligent tutoring systems that track a learner's work on each step and give hints and feedback, and conversational tutors built on large language models that answer, question and explain in dialogue. The decisions it covers are how much the tutor gives away (answers, hints, Socratic questions), how it keeps the learner doing the thinking, how it checks understanding rather than accepting a correct-looking answer, how it guards against over-reliance and wrong answers, and when it refers the learner to a human tutor, mentor or instructor.

It draws on three older literatures that conversational AI tutors inherit: **pedagogical agents** (animated or embodied on-screen characters that explain, model, give feedback and motivate), **teachable agents** (learning by teaching a computer agent that learns from the learner, as in Betty's Brain, and the protégé effect), and **computer-supported collaborative learning (CSCL)**, where software scripts, scaffolds or takes part in a learning conversation as a peer or partner.

The study configurations below are evidence; the response-dependent policy is an **untested design proposal**. Use it to gather better evidence about a learner group and a tutor configuration, not to certify that a tutor "works" or that a learner has mastered something because the tutor says so.

**What the evidence does and does not test.** The wiki's strongest evidence is on *step-based intelligent tutoring systems* against conventional instruction: three meta-analyses (Ma et al. 2014, k = 107; Kulik & Fletcher 2016, 50 evaluations; VanLehn 2011) agree on a moderate advantage over classroom instruction, textbooks and other computer-based instruction and no detected difference from one-to-one human tutoring, with much smaller effects on standardized than on locally developed tests. For *LLM tutors* the wiki records a handful of randomized studies, mostly single-session and immediate: an unguarded GPT-4 interface raised practice scores and lowered later unaided exam scores, while a guardrailed tutor removed the harm without a detected gain (Bastani et al. 2025); a research-designed physics tutor beat an in-class active-learning lesson on an immediate post-test (Kestin et al. 2025). No study recorded here follows an LLM tutor across a whole course to a delayed or transfer outcome. Pedagogical-agent evidence rests largely on reviews of older multimedia experiments; teachable-agent evidence on one meta-analysis of learning by teaching and a few small studies; CSCL evidence here is the moderator analyses of one meta-analysis of collaboration scripts (its main effect is not recorded as a claim in the wiki). So the configuration this page defends is narrow: a tutor that works step by step, withholds final answers by default, escalates help contingently, is judged on unaided and delayed performance, and has a named human route.

[Mastery learning](mastery-learning.md) decides when a learner moves on; [self-regulated learning](self-regulated-learning.md) concerns the learner's own planning and monitoring; [practice with simulated people](practice-with-simulated-people.md) covers AI role-play partners and simulated patients or clients; [mentor support in self-paced online learning](mentor-support-in-self-paced-online-learning.md) covers the human side of the handoff. This pattern is about the tutor's moves inside a task.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Task-specific starting knowledge (`novice`, `intermediate`, `advanced`, or `?`); an unaided attempt at a representative task, with reasoning; prior use of AI tools and how the learner says they use them (for answers, hints, checking). Preserve unknowns. |
| Context and activities | Setting and mode (`classroom`, `online-instructor-led`, `online-self-paced`, `workplace-clinical`); whether a human tutor, mentor or instructor is reachable and how fast; time per session and number of sessions; the exact tutor configuration: model or system, system prompt or tutoring rules, answer-withholding rules, hint ladder, problem-specific content given to the tutor, agent persona or voice, logging. |
| Learner-valued goal | Ask what the learner wants from the tutor (finish the assignment, pass the assessment, be able to do this at work) and why. Record disagreement with the designer objective: a learner who wants answers and a designer who wants independent skill want different tutors, and the evidence below says which one each will get. |
| Designer objective | The capability (`procedure`, `concept`, `complex-skill`, `judgement`), whether the domain is well structured (steps can be checked) or ill structured, and which aids are permitted when the capability is assessed. |
| Outcome | Separate measures for assisted performance during practice, unaided performance at the end, a delayed unaided measure and, where it matters, transfer to a changed task. Say whether the test is developed locally (close to the tutored problems) or standardized. Add a reliance or verification measure if over-reliance is a risk. |

A request to "add an AI tutor" does not specify these inputs. Ask for them before choosing a tutor configuration or predicting a gain. Check first that the tutor's answers on the course's own problems are correct: in the wiki, LLM-generated hints were wrong, too general or gave the answer away about a third of the time in one coding study, and expert reviewers discarded a quarter to nearly half of generated hints in another.

## Sequence and conditional policy

1. **Elicit an unaided attempt first.** Before the tutor opens, ask for the learner's own attempt and reasoning on a representative task. Keep it short and record it as a learning exposure. This is the baseline against which tutored practice is later read.
2. **Configure the tutor for the objective, not for helpfulness.** For a structured task, set the tutor to work step by step, to withhold final answers by default, and to give problem-specific hints (teacher- or designer-written content in the prompt, or a validated hint bank). Start contingent: the least help that moves the learner, more only after a failed attempt, less after success. Test the tutor on the course's own problems before learners see it.
3. **Tutored practice, dose by session.** Early sessions (the first one or two in a unit): 20–40 minutes of tutored step-based practice with hints available and an explanation request at each step. Middle sessions: raise the threshold for help (a hint only after an attempt; no worked step without a learner explanation) and add prompts to check the tutor's claims. Late sessions: tutor off for at least one unaided practice set before the assessment. Move a learner on when unaided work on a changed problem meets the agreed criterion, not when tutored practice does. These doses are a proposal; no claim here tests a dose or a fading schedule for an AI tutor.
4. **Read the log, not only the score.** Record what was asked (answer, hint, explanation, check), how many hints, whether the full answer was given, and how often the learner verified the tutor. Use the table below.
5. **Hand off to a human on named triggers.** Repeated impasse at the same step, a learner asking for the answer repeatedly, a tutor error the learner accepted, distress, or a question the tutor cannot answer. Name who takes over and how fast. Two studies recorded here support human involvement alongside software; none tests a specific trigger.
6. **Reobserve unaided and later.** Score an unaided, changed task at the end of the unit and again after a delay, separately from tutored practice. If tutored practice is high and unaided performance is not, treat it as a configuration problem, not as learning.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Tutored practice scores high, unaided scores flat or lower | Compare the log: share of turns asking for the answer or receiving it; give one matched unaided item mid-unit. | If answer-taking dominates, tighten answer-withholding and require an attempt before a hint. This is the pattern Bastani et al. observed with an unguarded interface; the guarded configuration removed the harm but did not show a gain, so expect no more than parity until an unaided measure shows otherwise. |
| Learner asks for the answer repeatedly, or skips | Ask what they are trying to get done and by when; check whether the task is beyond reach with the current hints. | If the task is out of reach, step back (a worked example or a simpler step) rather than release the answer. If the goal is completion under time pressure, negotiate the goal; refer to a human mentor if it persists. Untested branch. |
| Learner accepts a wrong tutor answer | Ask them to check the step against a source or a second method. | Add a short reflection or verification prompt; warning labels alone did not reduce reliance in one study recorded here. Log the error and fix the tutor's content. |
| Learner rarely asks for help but fails unaided | Compare hint use with errors; ask whether they avoided help. | A warning that the tutor can be wrong raised hint requests in one classroom study; a metacognitive help-seeking tutor changed help-seeking but not domain learning in another. Prompt help at impasse rather than waiting to be asked. Untested branch. |
| Correct with hints at the first step, stuck later | Probe the later step alone. | Escalate the hint ladder for that step only; change approach (address the error) rather than repeat the same question, which was followed by lower recovery in one tutor-log study. |
| Fluent explanation in dialogue, weak on a changed problem | A changed problem without the tutor. | Add varied unaided practice; the dialogue may have carried the reasoning. Untested branch. |

## Choosing configurations from evidence

- **Whether to expect a step-based tutor to beat ordinary instruction.** [Intelligent tutoring systems improve achievement over non-individualised instruction](../claims/adaptive-learning-improves-outcomes.md) [+S]: Ma et al. (107 effect sizes, 14,321 participants) and Kulik & Fletcher (50 controlled evaluations, median 0.66 SD; random-effects g = 0.50, 95% CI [0.40, 0.59]) both find a moderate advantage. [The overall weighted effect was g = .41 under random effects](../claims/its-meta-analysis-overall-effect-0-41.md) [+M]. [By comparator](../claims/its-beats-large-group-cbi-textbooks-not-human-tutoring.md) [~M], tutoring systems beat large-group human instruction (g = .44), individual computer-based instruction (g = .57) and textbooks or workbooks (g = .36), but showed no significant difference from small-group (k = 4, g = .05) or individual human tutoring (k = 5, g = −.11); equivalence was not tested.
- **Human tutoring is the ceiling to compare against, and it is lower than often said.** [Human tutoring had a medium effect over no tutoring](../claims/tutoring-effectiveness-comes-from-scaffolding-and-feedback.md) [+S]: VanLehn's review found d = 0.79 for human tutoring and d = 0.76 for step-based tutoring systems against no tutoring (abstract only). In a small study in the same claim (11 tutor–student pairs), students learned as well when tutors only prompted them to construct explanations as when tutors also explained and gave feedback, which is one reason this page defaults to eliciting rather than telling. [AutoTutor's gains were virtually equivalent to experienced human tutors](../claims/autotutor-gains-equivalent-to-human-tutoring.md) [+M] in typed or spoken physics tutoring, with no effect size printed, and [AutoTutor gains of 0.3 to 0.8 sigma over reading text for the same time](../claims/autotutor-learning-gains-0-3-to-0-8-sigma-vs-reading.md) [+M].
- **The test decides the size of the effect.** [Effects were large on locally developed tests and small on standardized ones](../claims/test-type-moderates-its-effects.md) [~M]: average ES 0.73 against 0.13 (g 0.62 against 0.09) across Kulik & Fletcher's evaluations. Plan an outcome that is not written by the tutor's designers, or expect a smaller effect on it. [The largest effects in that set](../claims/darpa-digital-tutor-largest-its-effects.md) [+M] (ES 1.97 and 3.18) came from one system for Navy technicians compared with longer classroom courses on locally developed tests; they are outliers, not a forecast.
- **An unguarded LLM tutor can raise practice and lower learning.** In a randomized trial with nearly a thousand high-school mathematics students (2,848 observations), [a standard GPT-4 interface raised assisted practice scores by 0.137 (out of 1) over a textbook-only control mean of 0.28](../claims/gpt-base-improves-assisted-practice-performance.md) [~M], and [lowered the later unaided exam by 0.054, about 17% of the control mean](../claims/gpt-base-harms-unassisted-exam-performance.md) [-M]. [A guardrailed tutor with teacher-designed, problem-specific hints raised practice more (0.361)](../claims/gpt-tutor-improves-practice-more-than-gpt-base.md) [+M] and [removed the exam harm (−0.004, not significant) without a detected exam gain](../claims/gpt-tutor-exam-effect-null.md) [~M]. In a separate experiment, [costs concentrated among participants who used the AI for direct solutions](../claims/persistence-costs-concentrated-among-direct-solution-users.md) [-M] (61% of the AI group; d = −0.36 against controls on later solving, cross-sectional within the AI arm), while hint users resembled controls.
- **A research-designed LLM tutor against active learning.** In a crossover randomized trial in an undergraduate physics course, [students learned more from an AI tutor than from an in-class active-learning lesson on the same content](../claims/ai-tutor-beats-active-learning-post-test.md) [+M] (median post-test 4.5 against 3.5; N = 142 and 174), [a regression effect of 0.63 after controls, which the authors call an underestimate because of a ceiling](../claims/ai-tutor-regression-large-effect-size.md) [+M], in [a median of 49 minutes against a 60-minute class](../claims/ai-tutor-less-time-on-task.md) [+M], with [the advantage holding above and below 40% on the pre-test concept inventory](../claims/ai-tutor-advantage-holds-subpopulations.md) [+M]. The outcome was an immediate post-test of one lesson; the trial says nothing about retention or a whole course.
- **Answer-giving is not always worse on an immediate test, which is why the horizon matters.** In a 50-person experiment, [an unrestricted chatbot produced larger immediate learning deltas than a Socratic chatbot (d = 0.80) or an adaptive exercise system (d = 0.85)](../claims/unrestricted-chatbot-higher-learning-delta-than-socratic-and-adaptive.md) [~M]; in a proctored experiment with 211 undergraduates, [any generative AI during a 35-minute learning phase raised an immediate unaided test by 7.2 points (0.28 SD)](../claims/genai-access-raises-immediate-test-scores.md) [+M]. In writing, [open AI collaboration gave the best supported writing and bounded support the best independent Week 8 writing](../claims/genai-supported-performance-independent-divergence.md) [~M]; in creativity, [free ChatGPT use raised originality on the assisted task (d = 0.79) and the advantage vanished unaided (d = 0.04)](../claims/chatgpt-free-use-originality-gains-vanish-unassisted.md) [~M]. Read immediate gains as provisional until a delayed unaided measure agrees.
- **Contingent help, and how much to give away.** [Computer-based scaffolding showed g = 0.46 across 144 STEM studies](../claims/scaffolding-improves-learning.md) [+S], and [contingent scaffolding beat fixed or absent support](../claims/contingent-scaffolding-improves-learning.md) [+M] in small tutoring studies. In an LLM tutor comparison, [a tutor that escalated and faded on what the learner did gave away the full answer in one session in sixteen, against one in six for a question-only tutor and three in five for an answer-giving one](../claims/contingent-scaffolding-surrenders-full-answer-least.md) [+M]. [Answer-revealing turns were followed by less independent student work on every tutor model tested](../claims/leakage-reduces-next-turn-independence-all-bases.md) [-M]. In a logic tutor with 113 undergraduates, [adaptive scaffolding policies beat a non-adaptive control on the post-test](../claims/adaptive-icap-scaffolding-improves-posttest-logic-tutor.md) [+M].
- **Feedback content.** [Feedback averages d = 0.48 (435 studies) but more than a third of feedback interventions in an older meta-analysis reduced performance](../claims/feedback-improves-learning.md) [~S]; information-rich feedback is the moderator. [Praise for intelligence after success undermined later persistence](../claims/feedback-praise-reduces-learning.md) [-S], so a tutor's encouragement should name the process, not the person. [ChatGPT-generated hints produced significant gains over no hints](../claims/chatgpt-hints-significant-gains-versus-control.md) [+M] in an online algebra experiment (N = 274, crowd workers), but [GPT-4 feedback was targeted for 66% of errors and too general, wrong or answer-revealing for about 35%](../claims/gpt4-feedback-66-percent-targeted-35-percent-flawed.md) [~M].
- **Over-reliance is not fixed by a warning.** [A brief metacognitive reflection prompt cut acceptance of incorrect AI advice (62.4% to 39.7%; OR = 0.40)](../claims/reflection-reduces-incorrect-ai-advice-acceptance.md) [+M], whereas [warning labels alone did not reduce reliance](../claims/genai-warning-labels-insufficient-reliance.md) [-M] in the medical-education studies a review reports. Learners can spot an error and follow the system anyway: [80.7% detected flawed recommendations yet deferred](../claims/surface-validation-works-substantive-validation-fails.md) [-M]; [7 of 15 students failed a task with plausible falsehoods despite checking](../claims/checking-coexists-with-unresolved-error-zhang.md) [-M]. Where verification was measured, [checking the AI's claims against sources predicted gains](../claims/checking-ai-claims-predicts-gains.md) [+M].
- **Guided prompting of the learner's AI use.** [Theory-guided five-step prompting improved open-ended explanations over unprompted AI access and slides](../claims/structured-prompting-improves-open-ended-ai-learning.md) [+M] (95 undergraduates, construction engineering; 12.41 against 10.45 and 9.68).
- **Human in the loop.** In a preregistered randomized trial with about 900 tutors, [students whose human tutors had real-time AI suggestions were 4 percentage points more likely to master the session's topic](../claims/tutor-copilot-raises-exit-ticket-mastery-4pp.md) [+S] (9 points for students of lower-rated tutors, per a review). In a quasi-experiment with 635 middle-school students, [adding human tutors to AI tutoring raised relative MAP growth by 61% within the analysis bandwidth](../claims/human-ai-tutoring-improves-map-growth-over-ai-only.md) [+M] (the full-sample 26% was not significant) and [time on task by 25%](../claims/human-ai-tutoring-increases-time-on-task.md) [+M].
- **Pedagogical agents: the content and the voice matter more than the face.** A review reports that [a meta-analysis of 43 studies found agents enhance learning against no agent](../claims/pedagogical-agents-enhance-learning.md) [+M] (no effect size printed). [AutoTutor's talking head added little beyond the content of the dialogue](../claims/autotutor-content-matters-not-talking-head.md) [~M]; [effects are attributed mainly to the agent's voice](../claims/agent-effects-due-to-voice-not-visual-presence.md) [~M], with transfer rather than recall improved; [iconic and realistic appearance did not differ](../claims/apa-appearance-null-effect.md) [~M]. In one 2×2 experiment with 72 undergraduates, [a high-competency learning companion improved application (d = 0.46)](../claims/high-competency-pal-improves-application.md) [+M], [a low-competency one raised self-efficacy (d = 0.49)](../claims/low-competency-pal-raises-self-efficacy.md) [~M], and [a proactive companion improved recall over a responsive one (d = 0.78)](../claims/proactive-pal-improves-recall.md) [+M].
- **Teachable agents and learning by teaching.** [Preparing to teach and then teaching gave g = 0.56 across 28 studies, larger when the teaching was interactive](../claims/learning-by-teaching-improves-tutor-learning.md) [+S]. [Adding a teachable agent to a fourth-grade science kit improved gains on curriculum and reasoning tests (d = 1.1 and 0.93)](../claims/ta-improves-basic-and-added-value-gains-fourth-grade.md) [+M] in a two-year quasi-experiment with seven classrooms. With an LLM, [students who taught a ChatGPT agent outscored a video group on knowledge](../claims/chatgpt-teachable-agent-knowledge-gains.md) [+M] (n = 20 and 21; the printed η² = 0.74 overstates an effect the paper's own figures put nearer d ≈ 0.7) but [not on code correctness](../claims/chatgpt-teachable-agent-no-correctness-gain.md) [~M].
- **Collaboration scripts and AI in groups.** In the collaboration-scripts meta-analysis, [prompting transactive activities](../claims/transactivity-moderator-not-significant.md) [~M], [the script level](../claims/script-level-moderator-not-significant.md) [~M] and [extra content support](../claims/content-support-moderator-not-significant.md) [~M] did not significantly moderate effects, but each test had low power (8–16%), so "no detected difference" is not "no difference". In a preregistered online experiment (315 participants), [a tutor plus LLM peers produced the highest unaided accuracy (about 65% against 42% for control)](../claims/tutor-plus-peers-strongest-unassisted-math-accuracy.md) [+M].

Do not rank these results against one another: comparators (no tutoring, textbooks, classroom instruction, active learning, an unguarded chatbot), outcomes (practice, immediate unaided, standardized, transfer) and learners differ. A precise abstention names the missing comparison, outcome or observation and the next way to resolve it.

## Fitting the design to a situation

Ask for four facts when the brief omits them: **is the task structured enough for the tutor to check each step?**, **what is assessed, with what aids, and when (immediately, at the end of the course, later at work)?**, **is a human tutor, mentor or instructor reachable, and how quickly?**, and **what will the tutor actually say, tested on the course's own problems?**

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are novices in the domain | Step-based tutoring with contingent hints and worked steps available; a coach or tutor agent rather than open chat | [Agents as coaches and tutors are most useful with novices](../claims/agents-most-effective-novice-learners.md) [~M]; [Guidance that helps novices becomes redundant with expertise](../claims/expertise-reversal-effect.md) [~S] |
| Learners are already competent and practising for fluency or transfer | Reduce step-level hinting; use the tutor for challenge problems, explanation checking or as a learner to teach | [Guidance that helps novices becomes redundant with expertise](../claims/expertise-reversal-effect.md) [~S]; [Learning by teaching](../claims/learning-by-teaching-improves-tutor-learning.md) [+S] |
| Adult or professional learners (higher education, workforce) | Keep the answer-withholding default; most LLM-tutor trials recorded here were undergraduates or high-school students, and the harm-after-withdrawal result was in high school | [GPT-4 access harmed the unaided exam](../claims/gpt-base-harms-unassisted-exam-performance.md) [-M] (high school); [AI tutor beat active learning](../claims/ai-tutor-beats-active-learning-post-test.md) [+M] (undergraduates) |
| Children or young adolescents | Prefer a structured tutor or teachable agent with teacher oversight to open chat | [Teachable agent improved fourth-graders' science reasoning](../claims/ta-improves-basic-and-added-value-gains-fourth-grade.md) [+M]; [warning about AI mistakes raised seventh-graders' hint requests](../claims/ai-fallibility-warning-increases-help-seeking.md) [+M] |
| The goal is a procedure in a well-structured domain (mathematics, physics problems, programming) | A step-based tutor with problem-specific hints written or checked by a teacher | [Guardrailed tutor with teacher-designed hints](../claims/gpt-tutor-improves-practice-more-than-gpt-base.md) [+M]; [ITS improve achievement](../claims/adaptive-learning-improves-outcomes.md) [+S] |
| The goal is an ill-structured judgement (writing, design, ethics, clinical reasoning) | Use the tutor for questioning and critique of the learner's draft, not for producing it; assess independent work | [Bounded support gave the best independent writing](../claims/genai-supported-performance-independent-divergence.md) [~M]; [originality gains vanished unaided](../claims/chatgpt-free-use-originality-gains-vanish-unassisted.md) [~M] |
| The assessment is unaided, or delayed, or at work | Schedule tutor-off practice before it; measure unaided performance separately from tutored practice | [Practice up, unaided exam down](../claims/gpt-base-harms-unassisted-exam-performance.md) [-M]; [Effects small on standardized tests](../claims/test-type-moderates-its-effects.md) [~M] |
| Online self-paced or asynchronous, no instructor watching | Answer-withholding by default, a hint ladder, logged reliance signals, and a named human handoff with a response time; add reflection prompts before accepting the tutor's answer | [Reflection prompt cut acceptance of wrong advice](../claims/reflection-reduces-incorrect-ai-advice-acceptance.md) [+M]; [Human-AI tutoring raised MAP growth over AI alone](../claims/human-ai-tutoring-improves-map-growth-over-ai-only.md) [+M] |
| Learners will use a general chatbot anyway | Teach a structured way to use it (attempt first, ask for hints, check claims) rather than relying on a warning | [Structured prompting improved explanations; unprompted access did not](../claims/structured-prompting-improves-open-ended-ai-learning.md) [+M]; [warning labels insufficient](../claims/genai-warning-labels-insufficient-reliance.md) [-M] |
| Short time: one session or a single lesson | A research-designed tutor can replace a lesson for an immediate outcome; do not extrapolate to a course | [AI tutor beat active learning in less time](../claims/ai-tutor-less-time-on-task.md) [+M] (one lesson, immediate test) |
| A course of many weeks | Fade tutor help across sessions and add tutor-off checkpoints; no claim here follows an LLM tutor over a course | untested proposal |
| Human tutors or mentors are available but stretched | Give them AI suggestions in real time, and route learners below a threshold to proactive human contact | [Tutor CoPilot raised mastery 4 points](../claims/tutor-copilot-raises-exit-ticket-mastery-4pp.md) [+S]; [Proactive tutoring had larger relative growth](../claims/proactive-tutoring-larger-relative-map-growth.md) [~M] |
| No human is available at all | Narrow the tutor's scope to checkable tasks and accept that it may underperform a human at helping | [Conversational agents were well behind humans at helping the student](../claims/conversational-agents-behind-human-helping-students.md) [~M] |
| High stakes (certification, patient or client safety) | Do not let the tutor's judgement of mastery stand alone; validate its content and its errors, and assess with a human-scored or proctored task | [GPT-4 feedback flawed in about 35% of hints](../claims/gpt4-feedback-66-percent-targeted-35-percent-flawed.md) [~M]; [convincing incorrect explanations](../claims/genai-hallucination-convincing-incorrect-explanations.md) [-M] |
| An animated or avatar agent is planned | Spend effort on what the agent says and its voice before its face; avoid adding visual load on complex content | [Talking head added little](../claims/autotutor-content-matters-not-talking-head.md) [~M]; [voice, not visual presence](../claims/agent-effects-due-to-voice-not-visual-presence.md) [~M]; [visual-channel overload](../claims/apa-visual-channel-overload.md) [-M] |
| Group work with an AI participant | Give the AI a bounded role (tutor or critic) and have the group verify its output together; do not use one AI agent to check another | [Tutor plus peers gave the best unaided accuracy](../claims/tutor-plus-peers-strongest-unassisted-math-accuracy.md) [+M]; [judge agents propagated peer errors](../claims/judge-verification-propagates-peer-errors.md) [-M] |
| Health professions (clinical interviewing, diagnosis) | Use multi-agent simulated patients with scaffolding for interview practice, with faculty review of errors; test long dialogues, where role-play failures cluster | [Multi-agent simulated-patient training raised OSCE-aligned scores (71.8% vs 55.6%)](../claims/ma-scaffolding-improves-osce-exam-score.md) [+M]; [role-play failures rise after turn 6](../claims/rpla-failure-onset-second-half-of-dialogue.md) [-M] |
| Teacher education | Use the tutor to support novice tutors or teachers in the moment (suggested moves), not to replace them | [Tutor CoPilot](../claims/tutor-copilot-raises-exit-ticket-mastery-4pp.md) [+S] (tutors of K-12 students; not tested with teacher candidates) |
| Business or management courses (case analysis, decisions) | Use the tutor to question the learner's analysis and to check claims against case data; keep the decision and justification the learner's | [Checking AI claims against sources predicted decision-making gains](../claims/checking-ai-claims-predicts-gains.md) [+M] (secondary school, socio-scientific issues; carried to business untested) |
| Technology and computing courses | Configure hint-not-solution behaviour and test it; small models frequently give direct code solutions | [Hint-not-solution was the hardest dimension, 6% to 81% across models](../claims/hint-not-solution-most-challenging-dimension.md) [-M]; [learning by teaching an LLM improved assignments, not exams](../claims/learning-by-teaching-llm-improves-assignments-projects.md) [~M] |
| Learners with low self-regulation | Add more external structure (planning prompts, check-ins, hint budgets) rather than open access | [Gen-AI effect on higher-order thinking was larger for high-SRL students (ES 0.86 vs 0.28)](../claims/genai-srl-moderator.md) [~M] |

## The evidence by question

- *Does a step-based tutoring system improve learning over ordinary instruction?* [Intelligent tutoring systems improve achievement over non-individualised instruction](../claims/adaptive-learning-improves-outcomes.md) [+S]
- *How does it compare with a human tutor?* [ITS beat large-group instruction and textbooks but not small-group or individual human tutoring](../claims/its-beats-large-group-cbi-textbooks-not-human-tutoring.md) [~M]; [Human tutoring d = 0.79, step-based tutoring d = 0.76, against no tutoring](../claims/tutoring-effectiveness-comes-from-scaffolding-and-feedback.md) [+S]
- *Does an LLM tutor help or harm learning?* [Unguarded GPT-4 access harmed the unaided exam](../claims/gpt-base-harms-unassisted-exam-performance.md) [-M]; [guardrails removed the harm](../claims/gpt-tutor-exam-effect-null.md) [~M]; [a research-designed tutor beat active learning on an immediate test](../claims/ai-tutor-beats-active-learning-post-test.md) [+M]
- *How much should the tutor give away?* [Answer-revealing turns reduce next-turn independent work](../claims/leakage-reduces-next-turn-independence-all-bases.md) [-M]; [a contingent tutor gave away the answer least](../claims/contingent-scaffolding-surrenders-full-answer-least.md) [+M]
- *Does an on-screen agent help?* [Pedagogical agents enhance learning compared with no agent](../claims/pedagogical-agents-enhance-learning.md) [+M]; [the talking head contributes little](../claims/autotutor-content-matters-not-talking-head.md) [~M]
- *Does teaching an agent help the learner?* [Learning by teaching improves tutor learning](../claims/learning-by-teaching-improves-tutor-learning.md) [+S]
- *When should a human be involved?* [Real-time AI support for human tutors raised mastery](../claims/tutor-copilot-raises-exit-ticket-mastery-4pp.md) [+S]

## Further evidence, not yet read against this model
<!-- Added 2026-10-17 on writing the page: claims two models linked to this pattern, and claims found by search, not used in the model above. Each marker is capped by the claim's recorded evidence (strength_cap). None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims linked to this pattern that the model above does not yet use. Each is evidence about AI tutoring, but none has been re-read against the model; treat them as candidates.

**Intelligent tutoring systems**
- [ITS beat conventional-instruction controls in 92% of 50 evaluations](../claims/its-beat-controls-in-92-percent-of-evaluations.md) [+M]
- [ITS raised test scores by a median of 0.66 SD across 50 evaluations](../claims/its-meta-analysis-median-es-066-sd.md) [+M]
- [Meta-analytic evidence indicates ITS yield positive outcomes](../claims/its-meta-analytic-positive-outcomes.md) [+M]
- [ITS show moderate benefits but are less effective than human tutoring](../claims/its-moderate-effect-less-than-human-tutoring.md) [~M]
- [ITS improve upon typical classroom instruction](../claims/its-improve-upon-typical-classroom-instruction.md) [+M]
- [ITS improve outcomes especially in structured domains](../claims/its-improve-outcomes-structured-domains.md) [+M]
- [ITS in vocational education foster declarative and procedural knowledge](../claims/its-vet-foster-declarative-procedural-knowledge.md) [+M]
- [ITS improve outcomes particularly with immediate actionable feedback](../claims/its-improve-learning-outcomes-with-actionable-feedback.md) [+M]
- [ITS are a mature implementation of personalized learning](../claims/its-mature-implementation-personalized-learning.md) [+M]
- [Personalized learning environments outperform standardized settings](../claims/personalized-learning-outperforms-standardized-settings.md) [+W]
- [AI-enabled personalized STEM education, g = 0.455 over 32 RCTs](../claims/ai-personalized-stem-overall-effect-g0455.md) [+M]
- [Comprehensive courses showed the largest subject effect](../claims/comprehensive-courses-largest-subject-effect.md) [+W]
- [AutoTutor achieved gains comparable to human tutors](../claims/autotutor-learning-gains-comparable-human-tutors.md) [+M]
- [AutoTutor improves learning by nearly one letter grade over reading](../claims/autotutor-improves-learning-one-letter-grade.md) [+M]
- [Student questions extinguish quickly in AutoTutor sessions](../claims/autotutor-student-questions-extinguish.md) [-M]
- [Human tutoring d ≈ 0.79 (VanLehn, as reported)](../claims/human-tutoring-effect-d-079.md) [+M]
- [Cognitive Tutor Algebra students outscored peers on standardized tests](../claims/cognitive-tutor-algebra-standardized-test-advantage.md) [+W]
- [Cognitive Tutor Moore, Oklahoma outcomes, about 0.4 SD](../claims/cognitive-tutor-moore-oklahoma-outcomes.md) [+M]
- [Cognitive Tutor Miami-Dade FCAT pass rates](../claims/cognitive-tutor-miami-dade-fcat-pass-rates.md) [+M]
- [Real-time feedback in an adaptive ITS improved SOLO progression](../claims/real-time-feedback-its-solo-progression-advantage.md) [+M]
- [Individualized BKT reduced questions needed for mastery](../claims/individualized-bkt-reduces-questions-needed-for-mastery.md) [+M]
- [ITS use reduced state math anxiety and improved algebra across conditions](../claims/its-reduces-executive-state-ma-improves-algebra.md) [+M]
- [Personalization to interests improved accuracy on hard knowledge components](../claims/personalization-improves-hard-kc-accuracy-algebra-its.md) [+W]
- [Personalized problems reduced gaming the system (d = 0.35)](../claims/personalization-reduces-gaming-behavior.md) [+M]
- [Adaptive fading of worked examples beat fixed fading or tutored problem solving](../claims/adaptive-fading-worked-examples-benefits.md) [+W]
- [The Help Tutor improved in-tutor help-seeking for a subset of actions](../claims/help-tutor-improved-in-tutor-help-seeking.md) [~M]
- [The Help Tutor produced no domain learning gains](../claims/help-tutor-no-domain-learning-gains.md) [~M]
- [Learning-curve analysis revealed a flaw in a cognitive model](../claims/learning-curve-revealed-coefficient-one-flaw.md) [+M]
- [A DataShop-derived cognitive model improved geometry mastery](../claims/datashop-model-improved-geometry-mastery.md) [+M]
- [Percent correct on single skills rises while overall percent correct stays constant](../claims/constant-error-rate-rising-skill-correct.md) [~M]
- [An intelligent reading tutor offered time efficiencies over human tutoring](../claims/intelligent-reading-tutor-time-efficiency-over-human-tutoring.md) [+M]
- [Speech-recognition tutoring supports word identification, attention and motivation](../claims/asr-tutoring-supports-word-identification-attention-motivation.md) [+M]
- [Classroom-scale data is insufficient for tutor-model misconception acquisition](../claims/tutor-model-sample-efficiency-classroom-insufficient.md) [-M]
- [Tutor models trained on ten misconceptions keep accuracy](../claims/tutor-model-multi-misconception-no-accuracy-tradeoff.md) [+M]
- [Implementation analysis identified engagement as a challenge for technology-driven tutoring](../claims/saga-implementation-engagement-challenges.md) [-M]
- [The field moved toward step-based problem solving and collaboration support](../claims/aied-step-based-domain-focus-collaboration-growth.md) [+M]

**LLM and generative-AI tutors**
- [Reviews citing Bastani et al. report harm after withdrawal of GPT-4 access](../claims/gpt4-access-harms-learning-after-withdrawal.md) [-M]
- [AI tutor students reported higher engagement and motivation](../claims/ai-tutor-engagement-motivation-higher.md) [+M]
- [Pedagogically designed AI tutors outperformed active learning (as reported)](../claims/pedagogically-designed-ai-tutors-outperform-active-learning.md) [+M]
- [An engineered AI tutor doubled learning versus active learning (as reported)](../claims/engineered-ai-tutor-doubled-learning-vs-active-learning.md) [+M]
- [A prompt-engineered chat tutor improved performance in a physics course (as reported)](../claims/genai-chat-tutor-rct-physics-improved-performance.md) [+M]
- [A meta-analysis reports g = 0.7 for generative AI on performance, argued to be task success rather than learning](../claims/genai-meta-analysis-g-0-7-performance-not-learning.md) [~M]
- [GenAI learning effects are heterogeneous and conditional](../claims/genai-learning-effects-heterogeneous-conditional.md) [~M]
- [Instructional method did not significantly moderate Gen-AI effects on higher-order thinking](../claims/genai-instructional-method-moderator.md) [~M]
- [GAI value is contingent on pedagogical integration](../claims/gai-value-contingent-on-pedagogical-integration.md) [~M]
- [Generative-AI performance gains diminished without assistance](../claims/genai-performance-gains-diminish-without-assistance.md) [-M]
- [Students relied on AI in peer feedback and struggled when it was removed](../claims/ai-assistance-peer-feedback-overreliance.md) [-M]
- [AI assistance was followed by 17% lower comprehension (cited study)](../claims/ai-assistance-lower-comprehension-17-percent.md) [-M]
- [Immediate performance is not evidence of independent learning](../claims/immediate-performance-not-evidence-of-independent-learning.md) [-W]
- [AI substitution may impede long-term skill development](../claims/ai-substitution-impedes-long-term-skill-development.md) [-W]
- [AI hints were associated with exam performance only on aligned items](../claims/ai-hints-aligned-exam-performance-only.md) [~M]
- [Generative-AI hints can match human hints but need validation](../claims/genai-hints-effective-but-require-validation.md) [~M]
- [Proactive and critical AI engagement associated with higher exam scores](../claims/proactive-critical-ai-engagement-higher-exam-scores.md) [+M]
- [ChatGPT improved quality and originality of ill-defined problem solutions](../claims/chatgpt-improves-quality-elaboration-originality-pit.md) [+M]
- [LLM teaching effectiveness varies by domain](../claims/llm-teaching-effectiveness-varies-by-domain.md) [~M]
- [Adaptive mode showed a warm-up per-question increase](../claims/adaptive-mode-per-question-delta-increase-warm-up.md) [+M]
- [Poorly grounded GenAI self-study risks fabricated content](../claims/genai-self-study-fabrication-curated-resources.md) [-M]
- [AI hallucination as a pedagogical resource](../claims/hallucination-as-pedagogical-resource.md) [+W]
- [Over-reliance on AI dialogue systems impairs decision-making](../claims/ai-overreliance-impairs-decision-making.md) [-M]
- [Reviewed literature reports over-reliance, errors and uncritical trust in AI for mathematics](../claims/ai-math-risks-overreliance-errors-uncritical-trust.md) [-M]
- [Excessive GenAI reliance risks undermining foundational knowledge](../claims/excessive-genai-reliance-hinders-foundational-knowledge.md) [-M]
- [Overreliance on automated writing evaluation may lower critical thinking](../claims/awe-overreliance-lowers-critical-thinking-creativity.md) [-W]
- [LLM cognitive debt weakens critical thinking](../claims/llm-cognitive-debt-weakens-critical-thinking.md) [-W]
- [Reactive approaches to cognitive debt are insufficient](../claims/cognitive-debt-reactive-ai-approaches-insufficient.md) [-W]
- [Contradictory meta-reviews on AI and critical thinking](../claims/contradictory-meta-reviews-ai-critical-thinking.md) [~M]
- [Brain connectivity scales down with external support in essay writing](../claims/brain-connectivity-scales-down-with-external-support-essay-writing.md) [-M]
- [LLM group performed worse over four sessions](../claims/llm-group-worse-neural-linguistic-scoring-four-sessions.md) [-M]
- [AI substitution: inclusion and time trade-offs](../claims/ai-substitution-inclusion-and-time-tradeoffs.md) [~W]
- [Placebo effect of perceived AI capabilities](../claims/placebo-effect-of-ai-perceived-capabilities.md) [~M]
- [Reflection produced selective, not blanket, rejection of AI advice](../claims/reflection-selective-not-blanket-ai-rejection.md) [+M]
- [Verification visibility interventions reduce overreliance in a model](../claims/verification-visibility-counter-cascade-interventions.md) [+M]
- [Students named awareness of their reliance as the most valued outcome](../claims/reliance-awareness-most-valued-outcome.md) [-M]
- [Student reflections on a copilot comment workflow](../claims/reflection-themes-copilot-comment-workflow.md) [~M]
- [Over-reliance on AI scaffolding risks learned helplessness](../claims/ai-scaffolding-fading-learned-helplessness.md) [-W]
- [Adaptive learning dominance limits student agency](../claims/adaptive-learning-dominance-limits-student-agency.md) [-W]
- [GenAI personalization and bias tensions](../claims/genai-personalization-bias-tensions.md) [~W]
- [AI tools for marginalized students, contingent on safeguards](../claims/ai-tools-potential-marginalized-students-contingent-safeguards.md) [~M]
- [LLM feedback shows praise and withholding bias toward students marked by group](../claims/marked-students-praise-withholding-bias.md) [-M]
- [Scaffolded generative AI augments human judgment in design thinking](../claims/genai-scaffolded-augments-human-judgment-design-thinking.md) [+M]
- [Students exercise ethical agency in GenAI use](../claims/student-ethical-agency-genai-use.md) [+M]
- [Four exploratory student AI-user profiles](../claims/exploratory-four-cluster-student-ai-profiles.md) [~M]
- [Behavioral archetypes of AI tutor use](../claims/itas-behavioral-archetypes.md) [~M]
- [An agentic AI instructor sustained engagement in a field deployment](../claims/agentic-instructor-sustained-engagement-iisc.md) [+W]
- [Embedded AI let a novice troubleshoot in real time](../claims/copilot-embedded-support-real-time-troubleshooting.md) [+W]
- [AI in university physics serves six pedagogical functions](../claims/ai-university-physics-six-pedagogical-functions.md) [+M]
- [Phase VI AI systems face six challenges](../claims/phase-vi-ai-systems-six-challenges.md) [-W]

**Building and evaluating LLM tutors**
- [Guardrail post-training raised accept rate and cut leak-or-overhelp](../claims/tactutor-guardrail-flags-improve-accept-leak.md) [+M]
- [Per-turn leakage predicts higher judged helpfulness and less independent work](../claims/per-turn-leakage-coupling-primary-base.md) [~M]
- [GRPO alignment without a directness reward raised Socratic scaffolding](../claims/grpo-without-directness-raises-socratic-scaffolding-effectiveness.md) [+M]
- [Alignment collapsed teaching-knowledge utterances and raised exploratory questions](../claims/alignment-shifts-mkt-collapse-exploratory-surge.md) [~M]
- [Emotion features help only with theory-grounded strategies](../claims/emotion-plus-theory-prompting-ablation-gain.md) [~M]
- [A task-specific prompt beat PedCoT prompting](../claims/task-specific-prompt-beats-pedcot-prompting.md) [+M]
- [Prompt design can generate cognitively activating feedback](../claims/leap-prompt-design-generates-cognitively-activating-feedback.md) [+M]
- [GPT feedback passed simulated helpfulness checks about 35% of the time](../claims/gpt-feedback-passes-automated-helpfulness-35-percent.md) [-M]
- [GPT-4 feedback was useful for identifying scoring errors](../claims/gpt4-feedback-useful-for-error-identification.md) [+M]
- [Automated verification of AI-drafted content gave mixed results](../claims/verification-layer-one-mixed-results.md) [~M]
- [RL reward misalignment failure modes](../claims/rl-reward-misalignment-failure-modes.md) [-W]
- [Within-session RL improved response quality](../claims/aura-rl-improves-response-quality.md) [+M]
- [Optimal retrieval configuration differs by discipline](../claims/rag-configuration-discipline-dependent-moodle-tutor.md) [+M]
- [Teachers used Purpose for goals and Rules for pedagogical behaviour](../claims/purpose-field-goals-rules-field-pedagogical-behavior.md) [+M]
- [Higher pedagogical scores associated with exercise conversion](../claims/pedagogical-score-predicts-exercise-conversion.md) [+M]
- [Proactive multimodal feedback increased feedback uptake](../claims/propact-feedback-increases-feedback-uptake.md) [+M]
- [Equation handling dominates AI tutor discourse](../claims/equation-handling-dominates-ai-tutor-discourse.md) [+M]
- [Repeating a failed scripted question lowers recovery](../claims/repeating-scripted-question-lowers-recovery.md) [-M]
- [Scripted prompts nearly eliminate persona drift](../claims/scripted-interaction-eliminates-observer-drift.md) [+M]
- [Tutoring over 30 days plateaus within days](../claims/educlaw-bench-plateau-within-days.md) [-M]
- [Systems adapt perceptibly to a learner persona](../claims/persona-adaptation-perceptible-to-raters.md) [+M]
- [Adaptive sessions converge on simulated mastery](../claims/collearn-adaptive-mastery-mae-convergence.md) [+M]
- [Socratic test pilot: conversation forced explanation](../claims/socratic-test-pilot-beyond-recall.md) [+M]
- [Socratic test pilot: students accepted the scaffolding](../claims/socratic-test-pilot-scaffolding-acceptance.md) [+M]
- [Socratic test: faculty saw differentiation](../claims/socratic-test-faculty-differentiation.md) [+W]
- [Knowledge-based design robot perceived as more responsible](../claims/kbd-robot-perceived-more-responsible-tutoring-behavior.md) [+M]
- [Knowledge-based design robot used more Socratic questioning](../claims/kbd-manipulation-check-behavioral-differences-transcripts.md) [+M]
- [Knowledge-based design: no difference in acceptance or motivation](../claims/kbd-no-difference-acceptance-motivation-subjective-learning.md) [~M]
- [Twelve design requirements for tutoring social robots](../claims/twelve-kbd-requirements-gsr-higher-education.md) [+M]
- [Tutoring robots need context knowledge of materials and strategies](../claims/gsr-context-knowledge-materials-strategies-environment.md) [+M]
- [A learning-assistant pilot rated chat and quiz modes positively](../claims/lea-pilot-positive-usability-chat-quiz-trust.md) [+M]
- [MAIC script generation outscored baselines](../claims/maic-funcgen-outperforms-baselines.md) [+M]
- [Computer-generated self-explanation prompts recommended](../claims/computer-generated-self-explanation-prompts-recommendation.md) [+W]
- [Subjective ratings diverged by persona in an adaptive system](../claims/avp-subjective-ratings-persona-divergence.md) [~M]

**Feedback, hints and help-seeking**
- [Subtle cueing feedback tends to have higher impact](../claims/subtle-cueing-feedback-higher-impact.md) [+M]
- [Self-questioning improves comprehension](../claims/self-questioning-improves-comprehension.md) [+S]
- [Students avoid help-seeking despite need](../claims/students-avoid-help-seeking-despite-need.md) [~M]
- [Within a session help-seeking shifts toward answers while self-regulation rises](../claims/within-session-hs-shifts-toward-closure-srl-increases.md) [~M]
- [Learning-oriented intentions did not predict enacted help-seeking](../claims/intent-enactment-gap-genai-help-seeking.md) [~M]
- [Help requests to an AI tutor were mostly instrumental with low verification](../claims/instrumental-help-seeking-procedural-low-verification.md) [~M]
- [Staged disclosure and diagnostic error patterns](../claims/staged-disclosure-diagnostic-error-patterns.md) [~W]

**Pedagogical agents**
- [Animated personas beat static ones and voice contributes](../claims/animated-persona-and-voice-effects.md) [+M]
- [APAs produce more definitive affective than cognitive gains](../claims/apa-affective-gain-stronger-than-cognitive.md) [~M]
- [No evidence for mere visual presence; likeable agents raised motivation and transfer](../claims/no-evidence-mere-visual-presence-social-cue-hypothesis.md) [~M]
- [Nonverbal effects depend on task type](../claims/nonverbal-effects-depend-on-task-type.md) [~M]
- [Redundant speech and gesture improve recall](../claims/speech-gesture-redundancy-better.md) [+M]
- [Minimal social cues trigger social reactions](../claims/minimal-social-cues-trigger-automatic-social-reactions.md) [~M]
- [High-competency companion elicits more positive attitudes (d = 0.91)](../claims/high-competency-pal-more-positive-attitudes.md) [+M]
- [A responsive companion did not improve attitudes](../claims/responsive-pal-no-attitude-benefit-no-interaction.md) [~M]
- [A second writing agent increased cognitive load](../claims/second-agent-increases-cognitive-load-writing.md) [~M]
- [Avatars said to increase tutor engagement (vendor white paper)](../claims/avatar-social-presence-increases-tutor-engagement.md) [+W]

**Collaboration and humans in the loop**
- [CSCL scripts meta-analysis showed no publication bias](../claims/cscl-meta-analysis-no-publication-bias.md) [~M]
- [Subject discipline moderated script effects on collaboration skills](../claims/further-moderators-discipline-duration-measurement-level.md) [~M]
- [Groups verifying chatbot solutions supported problem solving](../claims/collaborative-chatbot-answer-verification-problem-solving.md) [+M]
- [Human-AI tutoring: skill proficiency rose, gap widened](../claims/human-ai-tutoring-skill-proficiency-gap-widens.md) [~M]
- [Proactive and reactive tutoring did not differ at the cutoff](../claims/didc-cutoff-null-proactive-benefit-increases-below-cutoff.md) [~M]
- [Personalized learning as a human–AI collaboration](../claims/human-ai-collaborative-personalized-learning.md) [+M]
- [Adult learners want human-in-the-loop AI design](../claims/human-in-the-loop-ai-design-pf.md) [+M]
- [Practitioners reject AI replacing instructor expertise](../claims/rejection-of-ai-replacing-instructor-expertise.md) [+M]
- [Students prefer hybrid AI and instructor feedback](../claims/students-prefer-hybrid-ai-instructor-feedback.md) [+M]
- [AI-driven PBL enhances educator-student collaboration](../claims/ai-pbl-enhances-educator-student-collaboration.md) [+W]
- [Over-reliance on AI may reduce human interaction](../claims/over-reliance-ai-reduces-human-interaction.md) [-M]

**Role-play and simulated people**
- [RL training reduced missed red flags in a clinical agent](../claims/residencyrl-reduces-missed-red-flags.md) [+M]
- [Role-play agents degrade consistently under attack across models](../claims/cross-model-rpla-degradation-consistent.md) [-M]
- [Authority challenge and emotional manipulation are the most effective attacks](../claims/authority-challenge-emotional-manipulation-most-effective.md) [-M]
- [Automated judging aligns with experts with a conservative bias](../claims/automated-judge-human-alignment-conservative-bias.md) [~M]
- [Persona leakage strongest for communication style and personality](../claims/leakage-strongest-communication-personality.md) [-M]

## Illustrative design instance and observation record

*Illustration only, invented, not a tested course.* An online, self-paced introductory statistics module for working adults, with a mentor who answers within one business day. The designer's objective is that each learner can choose and run the right test on a new data set and explain the result; one learner says she wants to pass the module quickly while working full time. Agree that the module assessment is unaided and proctored, and that a delayed check a month later matters to the programme. The first activity asks each learner to choose a test for a short scenario without help. The tutor is configured to work step by step, never to give the final test choice or computed value, to give problem-specific hints written by the course team, and to ask the learner to check its claims against the course notes. Sessions one and two: about 30 minutes of tutored practice; sessions three and four: hints only after an attempt; session five: an unaided practice set with the tutor off. The log flags a learner who asks for the answer three times on one step, or accepts a tutor statement later marked wrong, and sends a message to the mentor.

Record: **unaided first attempt → tutor configuration and content actually used → per-step requests (answer, hint, explanation, check), hints given, answer released or not → tutor errors and whether the learner accepted them → handoffs to a human and their response time → unaided score on a changed task at the end → delayed unaided score**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record, but must not fabricate missing inputs or assign numerical mastery probabilities without a calibrated model.

## Elements and limits

[Hints](../elements/hints.md), [feedback](../elements/feedback.md), [immediate feedback](../elements/immediate-feedback.md), [scaffolding](../elements/scaffolding.md), [fading scaffolding](../elements/fading-scaffolding.md), [Socratic questioning](../elements/socratic-questioning.md), [self-explanation](../elements/self-explanation.md), [worked examples](../elements/worked-examples.md), [pedagogical agent signaling](../elements/pedagogical-agent-signaling.md), [peer teaching](../elements/peer-teaching.md), [collaborative problem solving](../elements/collaborative-problem-solving.md) and [metacognitive reflection](../elements/metacognitive-reflection.md).

This pattern is scoped to the tutor's moves within tasks and the handoff to people. It does not cover AI grading, AI-generated course content, proctoring or AI role-play as a practice partner (see [practice with simulated people](practice-with-simulated-people.md)). The wiki records no randomized comparison of an LLM tutor across a whole course with a delayed or transfer outcome, no test of a handoff trigger, and no test of fading a conversational tutor's help across sessions; the diagnostic branches above remain to be tested with actual learners.

## Claims

- [Multi-agent AI standardized-patient training improved OSCE-aligned exam scores](../claims/ma-scaffolding-improves-osce-exam-score.md) [+M]
- [Role-play agent failures become more frequent after turn 6](../claims/rpla-failure-onset-second-half-of-dialogue.md) [-M]

## Related Patterns

- [Mastery Learning](mastery-learning.md)
- [Self-Regulated Learning](self-regulated-learning.md)
- [Worked Examples](worked-examples.md)
- [Formative Assessment](formative-assessment.md)
- [Cognitive Apprenticeship](cognitive-apprenticeship.md)
- [Collaborative Learning](collaborative-learning.md)
- [Practice with Simulated People](practice-with-simulated-people.md)
- [Mentor Support in Self-Paced Online Learning](mentor-support-in-self-paced-online-learning.md)
- [Competency-Based Learning](competency-based-learning.md)
- [Online Course Design](online-course-design.md)

## Key Sources

- Ma, W., Adesope, O. O., Nesbit, J. C., & Liu, Q. (2014). Intelligent tutoring systems and learning outcomes: A meta-analysis. *Journal of Educational Psychology, 106*(4), 901–918. [doi:10.1037/a0037123](https://doi.org/10.1037/a0037123)
- Kulik, J. A., & Fletcher, J. D. (2016). Effectiveness of intelligent tutoring systems: A meta-analytic review. *Review of Educational Research, 86*(1), 42–78. [doi:10.3102/0034654315581420](https://doi.org/10.3102/0034654315581420)
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197–221. [doi:10.1080/00461520.2011.611369](https://doi.org/10.1080/00461520.2011.611369)
- Chi, M. T. H., Siler, S. A., Jeong, H., Yamauchi, T., & Hausmann, R. G. (2001). Learning from human tutoring. *Cognitive Science, 25*(4), 471–533. [doi:10.1207/s15516709cog2504_1](https://doi.org/10.1207/s15516709cog2504_1)
- Graesser, A. C. (2016). Conversations with AutoTutor Help Students Learn. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0086-4
- Bastani Hamsa, Bastani Osbert, Sungu Alp, Ge Haosen, Kabakcı Özge, Mariman Rei. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. Proceedings of the National Academy of Sciences of the United States of America. https://doi.org/10.1073/pnas.2422633122
- Kestin, G., Miller, K., Klales, A., Milbourne, T. & Ponti, G. (2025). AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting. Scientific Reports 15:17458. https://doi.org/10.1038/s41598-025-97652-6
- Zara Contractor and Germán Reyes. (2026). Experimental Evidence on the Learning Impact of Generative AI. https://arxiv.org/abs/2607.08849 [doi:10.48550/arxiv.2607.08849](https://doi.org/10.48550/arxiv.2607.08849)
- Grace Liu, Brian Christian, Tsvetomira Dumbalska, Michiel A. Bakker, Rachit Dubey. (2026). AI Assistance Reduces Persistence and Hurts Independent Performance. Published as a conference paper at COLM 2026. https://arxiv.org/abs/2604.04721
- Pardos ZA, Bhandari S (2024) ChatGPT-generated help produces learning gains equivalent to human tutor-authored help on mathematics skills. PLoS ONE 19(5): e0304013. https://doi.org/10.1371/journal.pone.0304013
- Reddig, J. M., Arora, A., & MacLellan, C. J. (2025). Generating In-Context, Personalized Feedback for Intelligent Tutors with Large Language Models. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-025-00505-6
- Hou, X., Weng, Y., Yeh, C. H., Lee, D. L., Zheng, L., Li, F., Wang, W., & Liu, Y. (2026). Adaptive Scaffolding Needs Contingency: An AI Tutor That Escalates and Fades on What the Learner Does. arXiv preprint. https://arxiv.org/abs/2609.22993 [doi:10.48550/arxiv.2609.22993](https://doi.org/10.48550/arxiv.2609.22993)
- Shuyi Fan, Boyuan Deng, Mengyu Xu, Jiale Liu, Hongyang Zhang, Qiaoxin Yang, Chongyang Gao. (2026). Rethinking LLM-Judged Helpfulness as a Pedagogy Signal: A Pre-Registered Audit Across Tutor Models. arXiv. https://arxiv.org/abs/2607.28128 [doi:10.48550/arxiv.2607.28128](https://doi.org/10.48550/arxiv.2607.28128)
- Belland, B. R., Walker, A. E., Kim, N. J., & Lefler, M. (2017). Synthesizing Results From Empirical Research on Computer-Based Scaffolding in STEM Education: A Meta-Analysis. *Review of Educational Research, 87*(2), 309–344. [doi:10.3102/0034654316670999](https://doi.org/10.3102/0034654316670999)
- Wisniewski, B., Zierer, K., & Hattie, J. (2020). The power of feedback revisited: A meta-analysis of educational feedback research. *Frontiers in Psychology, 10*, 3087. [doi:10.3389/fpsyg.2019.03087](https://doi.org/10.3389/fpsyg.2019.03087)
- Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin, 119*(2), 254–284. [doi:10.1037/0033-2909.119.2.254](https://doi.org/10.1037/0033-2909.119.2.254)
- Ren S (2026) College students’ metacognitive awareness of generative-AI reliance: an experimental study of decision confidence and attribution bias. Front. Psychol. 17:1926110. https://doi.org/10.3389/fpsyg.2026.1926110
- Xiaoyu Hou, Bo Xiao, Hexu Liu and Shane Mueller. (2026). The Role of Instructional Guidance in Generative AI-Assisted Learning: Empirical Evidence from Construction Engineering Education. https://arxiv.org/abs/2606.05509 [doi:10.48550/arxiv.2606.05509](https://doi.org/10.48550/arxiv.2606.05509)
- Tomohiro Nagashima, Mirella Hladký, and Vera Rief. (2026). Warning About AI Fallibility Increases Help-Seeking in an Intelligent Tutoring System. https://arxiv.org/abs/2606.03822 [doi:10.48550/arxiv.2606.03822](https://doi.org/10.48550/arxiv.2606.03822)
- Wong, S. S. H., & Qiu, S. X. (2026). Think First, ChatGPT Later: Guiding Human–AI Collaboration for Learning Gains in Independent Human Creativity. Educational Psychology Review. https://doi.org/10.1007/s10648-026-10118-7
- Chen X (2026) Layer-sensitive cognitive offloading in generative AI-assisted writing: supported performance and independent no-AI outcomes. Front. Psychol. 17:1906199. https://doi.org/10.3389/fpsyg.2026.1906199
- Zhao Yan, Yue Yuhe, Sun Zhonghua, Jiang Qiang, Li Gangsheng. (2025). Does Generative Artificial Intelligence Improve Students’ Higher-Order Thinking? A Meta-Analysis Based on 29 Experiments and Quasi-Experiments. Journal of Intelligence. https://doi.org/10.3390/jintelligence13120160
- Rose E. Wang, Ana T. Ribeiro, Carly D. Robinson, Susanna Loeb, and Dora Demszky. (2025). Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise. arXiv:2410.03017v2. https://arxiv.org/abs/2410.03017 [doi:10.48550/arxiv.2410.03017](https://doi.org/10.48550/arxiv.2410.03017)
- Ashish Gurung, Ge Gao, Jordan Gutterman, Danielle R. Thomas, Shivang Gupta, Lee Branstetter, Emma Brunskill, Vincent Aleven, Kenneth R. Koedinger. (2026). Improving Hybrid Human-AI Tutoring by Differentiating Human Tutor Roles Based on Student Needs. arXiv preprint. https://arxiv.org/abs/2605.11155 [doi:10.48550/arxiv.2605.11155](https://doi.org/10.48550/arxiv.2605.11155)
- Koedinger, K., Aleven, V., Roll, I., & Baker, R. (2008). In vivo experiments on whether supporting metacognition in intelligent tutoring systems yields robust learning. https://learnlab.org/
- W. Lewis Johnson & James C. Lester. (2015). Face-to-Face Interaction with Pedagogical Agents, Twenty Years Later. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-015-0065-9
- Nicole C. Krämer & Gary Bente. (2010). Personalizing e-Learning. The Social Effects of Pedagogical Agents. Educ Psychol Rev. https://doi.org/10.1007/s10648-010-9123-x
- Woo, H.L. (2009). Designing multimedia learning environments using animated pedagogical agents: factors and issues. Journal of Computer Assisted Learning, 25, 203-218. https://doi.org/10.1111/j.1365-2729.2008.00299.x
- Kim, Y., Baylor, A. L., & PALS Group. (2006). Pedagogical Agents as Learning Companions: The Role of Agent Competency and Type of Interaction. Educational Technology Research and Development, 54(3), 223-243. https://doi.org/10.1007/s11423-006-8805-z
- Kobayashi, K. (2019). Learning by preparing-to-teach and teaching: A meta-analysis. *Japanese Psychological Research, 61*(3), 192–203. [doi:10.1111/jpr.12221](https://doi.org/10.1111/jpr.12221)
- Doris B. Chin, Ilsa M. Dohmen, and Daniel L. Schwartz. (2013). Young Children Can Learn Scientific Reasoning with Teachable Agents. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2013.24
- Angxuan Chen, Yuang Wei, Huixiao Le, Yan Zhang. (2024). Learning-by-Teaching with ChatGPT: The Effect of Teachable ChatGPT Agent on Programming Education. arXiv. https://arxiv.org/abs/2412.15226 [doi:10.48550/arxiv.2412.15226](https://doi.org/10.48550/arxiv.2412.15226)
- Freydis Vogel & Christof Wecker & Ingo Kollar & Frank Fischer. (2016). Socio-Cognitive Scaffolding with Computer-Supported Collaboration Scripts: a Meta-Analysis. Educ Psychol Rev (2017) 29:477–511. https://doi.org/10.1007/s10648-016-9361-7
- Yang, L., Liu, H., Li, S., Jia, R., Xiao, Y., Chen, G., & Lu, L. (2026). Evaluating Scaffolding-Oriented Multi-Agent Large Language Model System for Clinical Interview Training. https://arxiv.org/abs/2609.10939 [doi:10.48550/arxiv.2609.10939](https://doi.org/10.48550/arxiv.2609.10939)
