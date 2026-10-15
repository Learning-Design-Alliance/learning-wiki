---
type: principle
id: productive-usage-guaranteed-by-design
title: Design tools so productive usage is guaranteed by affordances and constraints rather than instructions
description: "For learners using a simulation, practice tool or AI assistant, building the productive use into the tool (obvious productive actions, controls that invite comparison, limits on shortcuts such as answer-giving) is expected to yield more of the intended activity and better unaided performance than the same tool governed by written directions; no claim in the wiki compares the two directly, and one randomised trial shows a hints-only limit preventing harm without producing a gain."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-15
sources:
  - id: podolefsky-2013
    resource: "http://phet.colorado.edu/en/simulation/energy-skate-park-basics"
    title: "Podolefsky, N. S., Moore, E. B., & Perkins, K. K. (2013). Implicit scaffolding in interactive simulations: Design strategies to support multiple educational goals. http://phet.colorado.edu/en/simulation/energy-skate-park-basics"
    author: "Podolefsky, N. S., Moore, E. B., & Perkins, K. K"
---

# Design tools so productive usage is guaranteed by affordances and constraints rather than instructions

> **Principle** · [All principles](index.md)
> **Evidence** · 24 claims (13 for, 11 mixed) · 22 studies (6 causal, 6 theoretical, 3 qualitative, 3 design, 2 review, 2 associational), `q1`–`q3` · 5 of 22 report an effect size · 21 claims rest on one study

## Conditional relationship

This page owns one design choice: **how a learning tool steers learners toward the use that teaches**. The tool can be an interactive simulation, a practice app, an adaptive tutor or an AI assistant. The choice is between building the productive use into the tool and relying on written directions. Building it in means making the productive actions the obvious ones on the screen, giving controls ranges that invite useful comparisons, and blocking or bounding the actions that let a learner skip the thinking: an assistant that hands over the answer, a selector that lets a learner keep practising what they have mastered, a path that skips a prerequisite. Such a tool is expected to produce more of the intended activity, and better **unaided** outcomes on the target (`immediate-performance`, `conceptual-understanding`, `near-transfer`), than the same tool left open and governed by instructions. The page's source (Podolefsky, Moore and Perkins, 2013, on PhET simulations, drawing on Norman) argues the general form: "effective designs use affordances and constraints to create tools where correct usage is guaranteed by design", and a text label is often a sign of poor design.

The relationship is conditional on four things: **what the unproductive use is and what it costs** (answer copying costs unaided performance; free exploration of a simulation may cost nothing); **the learner's own strategy** (in a simulation of learners, a constraint changed little for strategies that were already efficient and a great deal for a risk-averse one); **whether the outcome that counts is measured with the tool removed**; and **whether the constraint holds** (a guardrail written into an AI model's prompt is not reliably kept).

**No claim in the wiki compares a tool that builds in productive use with the same tool plus instructions.** Two halves are tested separately. The constraint half has one randomised trial in high school mathematics (Bastani et al.): unrestricted GPT-4 during practice lowered later unaided exam scores against a textbook-only control, and a version limited to teacher-designed hints removed that harm but produced no exam gain. Two smaller studies point the same way for bounded or delayed AI access (writing, creative tasks). The instruction half has one study in which prompt-literacy guidance raised how often students used an LLM in the intended way, so written direction is not always a sign of failure. The simulation evidence behind the page's original argument is one interview study of one student. The architectural-constraint evidence comes from simulated learners and model-judged outputs, not from learners. So the steps below are a **default design**, labelled step by step.

How the converted siblings sit beside this page: [User-Centered Design for Learning](user-centered-design-for-learning.md) owns the user-testing loop that finds where an interface makes learners stall; this page uses that loop to check whether the productive use happens without text. [Digital Learning](digital-learning.md) decides whether a digital tool earns its place and credits gains to the method it carries. [Scaffolding](scaffolding.md) owns support versus no support, including what AI assistance costs independent performance; this page holds the narrower design lever of building the limits into the tool. [Guided Practice](guided-practice.md) holds the practice phase in which an AI tutor's hints are typically used.

## Default design, while the relationship is untested

The earlier page's guidance, kept as a concrete default a designer can act on and revise. Each step is a design proposal; its evidence status is stated beside it. The quantities are untested proposals unless a claim is linked.

1. **Write down the productive use and the shortcuts.** Before designing, list in one line each what learners should do with the tool (drop the skater from different heights and compare, attempt the step before asking for help) and what they could do instead that skips the thinking (ask for the answer, practise only easy items, jump to the last screen). Rank the shortcuts by what they would cost the target outcome. Untested proposal; from the earlier page's "afford productive usage and constrain unproductive usage".
2. **Make the first productive action obvious on the opening screen.** One or two controls that do something visible, no instruction text needed to start. Check it: a learner new to the tool should begin a productive action within about ten seconds. Evidence: [A student began interacting with the sim within 10 seconds and verbalized sense-making without explicit guidance](../claims/implicit-scaffolding-supports-immediate-exploration.md) [+W] (one sixth-grade student, think-aloud with no instructions; the ten-second figure is that observation, used here as a check, not a tested threshold).
3. **Give controls ranges and extremes that invite comparison.** Set sliders and options so the extremes produce a visibly different result (large against small, high against low), so comparing is the natural next move. Evidence: [A student used slider extremes to make qualitative comparisons of skater mass effects](../claims/slider-extremes-support-qualitative-comparisons.md) [+W] (the same student; an illustration, not a test).
4. **Block or bound the shortcuts that cost learning; leave the rest open.** For an AI assistant that can produce the answer, build it to give hints, questions and checks of the learner's own attempt rather than solutions, using teacher-written hints for the specific problems where possible. For a practice selector, steer away from skills already mastered and enforce prerequisites. Leave features open where free movement costs nothing: the earlier page's sources let learners reach any part of the simulation at any time. Evidence: [Guardrails in the GPT Tutor largely eliminate the negative exam effect, though no positive exam effect is observed](../claims/gpt-tutor-exam-effect-null.md) [~M]; [Unfettered GPT-4 access during practice harms subsequent unassisted exam performance in high school mathematics](../claims/gpt-base-harms-unassisted-exam-performance.md) [+M]; [A constrained architecture combining prerequisite enforcement and a minimum cognitive-demand floor substantially reduces reward hacking, lowering RHSI from 0.317 (MO) to 0.102 (ST)](../claims/constrained-architecture-reduces-rhsi.md) [+W] (simulated sessions); [Authors report that flexibility in sim access supports student agency while students tend to explore in a productive sequence](../claims/flexibility-supports-agency-productive-sequence.md) [+W] (the authors' belief, not a result).
5. **Hold the constraint in the tool, not only in a prompt, and test that it holds.** Before learners use an AI tool configured to give hints only, try it with ten to twenty requests that ask outright for the answer, and count how many it answers; fix the configuration if more than one or two get through. Evidence that this varies: [Hint-not-solution is the most challenging rubric dimension, with scores ranging from 6% to 81% across models](../claims/hint-not-solution-most-challenging-dimension.md) [~W] (small language models on block-programming debugging questions, model-judged). The test size and threshold are untested proposals.
6. **Watch learners use it with no written directions, then fix what needed text.** Give five learners the tool with only a think-aloud prompt, for ten to fifteen minutes each. Record the time to the first productive action, whether each reaches the interactions the target needs, and every point where someone asked what to do or the observer had to say something. Each such point is a design problem first: change the screen, then test again. A label is the fallback when a redesign cannot carry it. Untested proposal; from the earlier page (the PUSH sign on a door that affords pulling) and its source's interview method. The test loop itself is modelled in [User-Centered Design for Learning](user-centered-design-for-learning.md).
7. **Add a short instruction where the design cannot carry the use.** Where the productive use depends on the learner's choices the tool cannot see (how to phrase a request to an AI, when to ask for help), give a brief explicit guide alongside the tool rather than counting on the interface alone. Evidence: [Prompt-literacy guidance produced higher transcript-coded rule-following compliance than unrestricted LLM access, driven by process-over-answer and stepwise-hint behaviors](../claims/guided-llm-training-raises-rule-following-compliance.md) [~M] (undergraduate statistics; a measure of use, not of learning). This qualifies the earlier page's rule that textual direction signals poor design.
8. **Judge the tool by what learners can do without it.** Measure the target unaided, on items like the ones practised and on some that differ, and do not read better in-tool performance as learning. Evidence: [A guardrailed GPT-4 tutor with teacher-designed hints improves assisted practice performance more than a standard GPT-4 interface](../claims/gpt-tutor-improves-practice-more-than-gpt-base.md) [~M] beside the exam result in step 4: the tutor's large practice gain left no unaided exam gain. See also [AI-generated homework hints were positively associated with exam performance only when exam questions closely matched the homework content](../claims/ai-hints-aligned-exam-performance-only.md) [~W].
9. **Plan the constraints across sessions, not only in one.** A default arc over three to six sessions:
   - *Session 1* (first 10 to 15 minutes): open exploration of the constrained tool with no written directions; the teacher or the tool's opening screen poses one question; no answer-giving AI.
   - *Sessions 2 to 3*: challenges or puzzles that need the target interactions (the [Four-category design pattern for implicit scaffolding in simulations](productive-usage-guaranteed-by-design.md) lists them); an AI assistant, if used, gives hints only, and only after the learner has entered an attempt; the learner works the first item of each kind alone before help is offered.
   - *Later sessions*: loosen the bounds as unaided success appears, moving the assistant from step-by-step tutor to a coach that checks the learner's own solution, as teachers in one focus-group study chose to configure it ([Teachers sought to preserve student thinking and authorship by bounding chatbot answer-giving and maintaining teacher control over scope](../claims/teachers-preserve-student-thinking-bound-answer-giving.md) [+W]).
   - *Move a learner on* when they complete two consecutive target tasks unaided. The arc, the session counts and the threshold are untested proposals; the order (think first, then use the assistant) follows [The regulated 'think first, ChatGPT later' group outperformed both other groups in independent originality on the unassisted task despite no assisted-task advantage](../claims/regulated-ai-outperforms-independent-originality.md) [+M] (university students, creative product tasks; the claim page does not say whether the order was enforced by the tool or by instruction).

When a condition is not met: if the shortcut cannot be blocked (learners have unrestricted AI on their own phones), the constraint has to come from the task and the assessment instead: an unaided check that the learners know is coming, and work that asks for their own first attempt before any tool use. If the tool is built by someone else and cannot be changed, the design moves to steps 6 to 8: find where learners go wrong, add the shortest instruction that fixes it, and measure unaided.

## Fitting the design to a situation

The three facts that most change the decision:

- **What the shortcut is and what it would cost.** An assistant that can produce the full answer threatens unaided performance; free movement through a simulation may cost nothing. If unstated, ask: what can a learner do with this tool that gets the task done without learning the target, and does the assessment catch it?
- **Whether the outcome is measured with the tool removed.** The constraint evidence is about unaided exams; assisted practice scores rose most where learning did not follow. If unstated, ask: will learners be assessed with or without the tool, and when?
- **Who controls the tool.** A designer who builds the tool can block a shortcut; a teacher handed a commercial assistant can only configure it or set the task around it; a learner with their own device controls it themselves. If unstated, ask: can the tool's behaviour be changed, by whom, and can learners get round it?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are `advanced` on the task, or already use the tool efficiently | Keep constraints light: block only the shortcut that skips the target; leave choice of tasks and features open | [System constraints have minimal effect on already-efficient task-selection strategies while strongly correcting inefficient ones](../claims/constraints-selectively-affect-inefficient-strategies.md) [~W] (simulated learners in mastery learning; carried to real learners untested) |
| Learners tend to avoid risk (keep practising what they can already do) | Steer task selection toward skills close to mastery rather than letting them choose freely; show the next skill as the default choice | [A closer-to-mastery task-selection constraint sharply reduces overpractice for the risk-averse strategy, with large Cohen's d effect sizes](../claims/closer-to-mastery-constraint-reduces-overpractice.md) [+W] (simulated learners; untested with learners) |
| Learners are `child` or `adolescent` | Children: an opening screen they can act on without reading, controls with visible extremes, and an adult nearby for the first session. Adolescents with an AI tutor: hints only, teacher-written per problem | Child: [A student began interacting with the sim within 10 seconds and verbalized sense-making without explicit guidance](../claims/implicit-scaffolding-supports-immediate-exploration.md) [+W] (one sixth-grade student). Adolescent: [Guardrails in the GPT Tutor largely eliminate the negative exam effect, though no positive exam effect is observed](../claims/gpt-tutor-exam-effect-null.md) [~M] (high school mathematics) |
| Learners are `adult` in a work setting (`adult-workplace`), using a tool on the job | Bound the assistant to checking and hinting during training tasks, and judge readiness on an unaided task from their own work; tell them why the tool is bounded | untested proposal; the AI evidence is from students, not workers |
| Goal is open exploration of a `concept` or `principle` (a simulation) | Constrain little: make productive actions obvious and leave free movement between parts; add challenges for continued engagement | [Authors report that flexibility in sim access supports student agency while students tend to explore in a productive sequence](../claims/flexibility-supports-agency-productive-sequence.md) [+W] (authors' belief; not tested) |
| Goal is a `procedure` or problem solving where the assistant could produce the answer | Hints only, after an attempt; an unaided check before moving on | [Unfettered GPT-4 access during practice harms subsequent unassisted exam performance in high school mathematics](../claims/gpt-base-harms-unassisted-exam-performance.md) [+M] |
| Goal is writing or a creative product | Bound the assistant (feedback on the learner's own draft, not generation) or have learners draft before opening it; assess one piece written without it | [Open AI collaboration yielded the highest supported writing quality, while bounded AI support yielded the highest independent no-AI Week 8 performance](../claims/genai-supported-performance-independent-divergence.md) [+M] (one class-clustered quasi-experiment, 168 students) |
| The product goes to a real audience, and the assisted product is what matters | Open assistance can raise the product's quality; if the learner's own later work also matters, keep a think-first step and one unassisted piece | [Free ChatGPT use boosts originality on the assisted creative task but the advantage disappears when assistance is removed](../claims/chatgpt-free-use-originality-gains-vanish-unassisted.md) [~M] (university students; the product gain did not carry over) |
| `online-self-paced`, no teacher present | All steering must be in the tool: a self-explaining opening screen, hints-only assistant, an unaided check item the tool scores; nobody can correct a learner who takes the shortcut | untested proposal; the guardrail trial was in classrooms |
| `classroom` with one teacher and many learners | Let the tool hold the constraint so the teacher is free to circulate; the teacher watches for learners stuck at the same point and gives one spoken pointer to all, then notes it as a screen to redesign | untested proposal |
| Scarce facilitator time (volunteers, one tutor checking in briefly) | Put the constraint in the tool and the check in a short unaided item the tutor reviews in two minutes; skip designs that rely on the tutor policing tool use | untested proposal |
| Some learners remote and some in the room, or phone-only | Test the opening screen on the phones learners use; give remote learners the same bounded tool rather than whatever assistant they have at home, and the same unaided check | untested proposal |
| Single session only | 10 to 15 minutes of exploration with the constrained tool, a 15 to 20 minute challenge, a 5 minute unaided item; claim nothing about retention | untested proposal |
| Fixed short time budget (for example 30 minutes) | Cut exploration to 8 minutes and the challenge to 15; keep the 5 minute unaided item and the minutes adding to the budget; drop the second challenge before the check | untested proposal |
| Learners with low literacy or low confidence | Rely on the screen rather than text: icons and visible results, one action per screen, and spoken help available on request; let learners attempt privately before anyone sees | untested proposal; from the earlier page's argument that text directions are a sign of poor design |
| Learners want direct answers, or will rate a hints-only tool poorly | Offer guidance first and an answer only after the learner's own attempt and one hint; record which learners reach the answer step | [Most introductory physics students preferred a combination chatbot (guidance first, answers when stuck), while few preferred pure guided Q&A](../claims/students-prefer-combination-chatbot-over-guided-qa.md) [~W] (anticipated preference, physics students; not a learning outcome) |
| Stakes are high or the assessment is unaided | Judge readiness only on unaided work; log assistant use and do not count assisted success | [A guardrailed GPT-4 tutor with teacher-designed hints improves assisted practice performance more than a standard GPT-4 interface](../claims/gpt-tutor-improves-practice-more-than-gpt-base.md) [~M] (assisted gain without exam gain) |
| The brief names its own routine, rubric or tool configuration | Keep it; change only what the evidence says matters: one bound on answer-giving, one unaided check, one think-first step. If its rubric rewards tool use, keep that criterion and add an unaided check beside it | untested proposal |
| The brief gives its own categories or criteria for good use | Use them as the list of productive and unproductive uses in the design; do not substitute this page's | untested proposal |
| Material is private or sensitive (learners' own writing, health or work data) | Use a tool whose logs the learner controls; the unaided check is seen only by the learner and whoever the brief names | untested proposal |
| The brief wants a whole-task performance kept whole | Bound the assistant within the whole task (hints on the learner's current step) rather than splitting the task into constrained parts | untested proposal |
| The brief reports a shortcut learners actually took (pasting the question into a chatbot) | Use it as the compared case: show the two routes side by side and block or bound that route in the tool | untested proposal; the answer-copying pattern is shown in [Students use standard GPT-4 access as a crutch—copying answers rather than engaging with the material—which explains the harm to learning](../claims/gpt-base-crutch-mechanism.md) [+M] |

Ten of the twenty-two rows cite a claim, one of them (the reported shortcut) only to illustrate an untested move. Four of those carry evidence from simulated learners, one student, or the authors' own belief, and say so; the others carry a claim from one study to learners or settings it did not test, which the row names. The remaining rows are untested proposals.

## Observation, state and explanation

What can be observed is use under stated conditions: the actions a learner takes and in what order, the time to the first productive action, the requests made to an assistant and what it returned, where the learner stopped or asked what to do, in-tool performance, and performance with the tool removed. "Is exploring productively", "is using the tool as a crutch" and "understands the model" are inferred states.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Learner does not start, or asks what to do | The productive action is not visible; the learner expects instructions in school software; low confidence about doing it wrong | Watch a second learner on the same screen; offer a single spoken cue ("try moving that") and see whether use then continues without help. |
| High in-tool scores, weak unaided result | The tool did the work (answer copying); the unaided items differ more than intended; the constraint was not holding | Read the assistant log for answer requests and what came back; give a matched unaided item. |
| Explores busily but never reaches the target interaction | The target is hidden or not rewarded; the learner is pursuing their own question; the session was too short | Pose one challenge that needs the target interaction and record whether it is reached. |
| Gets round the constraint (rewords requests, uses another device) | The constraint is in a prompt, not in the tool; the learner values finishing quickly; the task is graded on completion | Test the configuration with direct answer requests; ask what the learner was trying to get done. |
| Uses the tool as intended and still learns little | The productive use is not the right activity for this target; the constraint removes work the learner needed to see modelled | Compare with a learner given a worked example first; check what the unaided task asks. |

These rows are proposals, untested as diagnostics. Asking a learner what they are doing changes what they do, so record each probe.

## Evidence and qualifications

The claims below test parts of the relationship. None compares a constrained tool with the same tool plus instructions.

- [Guardrails in the GPT Tutor largely eliminate the negative exam effect, though no positive exam effect is observed](../claims/gpt-tutor-exam-effect-null.md) [~M]: high school mathematics; the GPT Tutor arm's unaided exam performance was statistically indistinguishable from the textbook-only control (point estimate −0.004). It is the only randomised test in the wiki of building a limit into a tool, and it shows the limit preventing harm, not producing a gain.
- [Unfettered GPT-4 access during practice harms subsequent unassisted exam performance in high school mathematics](../claims/gpt-base-harms-unassisted-exam-performance.md) [+M]: the same trial's preregistered primary analysis; the unrestricted arm scored 0.054 lower (out of 1) than control on the unaided exam, a 17% reduction. It shows what the shortcut costs when nothing blocks it.
- [A guardrailed GPT-4 tutor with teacher-designed hints improves assisted practice performance more than a standard GPT-4 interface](../claims/gpt-tutor-improves-practice-more-than-gpt-base.md) [~M]: the same trial; practice scores rose by 0.361 with the tutor and 0.137 with unrestricted access, against a control mean of 0.28. Read with the exam claim, it is the reason to judge a tool by unaided performance.
- [Students use standard GPT-4 access as a crutch—copying answers rather than engaging with the material—which explains the harm to learning](../claims/gpt-base-crutch-mechanism.md) [+M]: the same trial's message analysis; unrestricted users mostly asked for the answer, while tutor users increasingly asked for help and attempted problems themselves. It is the trial's mechanism reading.
- [Unrestricted GPT-4 access improved practice performance but harmed later exam performance, and a guardrailed hint-based version mitigated the harm, as reported by the whitepaper citing Bastani et al.](../claims/gpt4-access-harms-learning-after-withdrawal.md) [+W]: a second-hand report of the same trial (nearly 1,000 students, practice up 48%, exam down 17%). It adds no study.
- [Open AI collaboration yielded the highest supported writing quality, while bounded AI support yielded the highest independent no-AI Week 8 performance](../claims/genai-supported-performance-independent-divergence.md) [+M]: six intact classes, 168 students, class-clustered quasi-experiment; bounded support had the highest observed means on the Week 8 no-AI essay (writing quality 3.88 against 3.59 for open collaboration). Observed means, no effect size printed.
- [The regulated 'think first, ChatGPT later' group outperformed both other groups in independent originality on the unassisted task despite no assisted-task advantage](../claims/regulated-ai-outperforms-independent-originality.md) [+M]: 196 university students randomly assigned; on the later unassisted task the regulated group was more original than the human-only (d = 0.52) and free-use (d = 0.48) groups. Whether the order was built into the tool is not stated on the claim page.
- [AI assistance reduces persistence: persistence costs concentrate among learners who used AI for direct solutions, not hints](../claims/ai-assistance-persistence-costs-direct-solutions.md) [+W]: a second-hand report of randomised experiments (Liu et al.); after losing AI access, participants solved fewer problems and gave up more often, concentrated among those who had used it for direct solutions. It bears on which use to block.
- [Prompt-literacy guidance produced higher transcript-coded rule-following compliance than unrestricted LLM access, driven by process-over-answer and stepwise-hint behaviors](../claims/guided-llm-training-raises-rule-following-compliance.md) [~M]: undergraduate statistics; instruction alone raised intended use (compliance 3.21 against 2.43 of 6 rules, d = 0.81; process-over-answer 100% against 22%). **This limits the page's claim that instructions signal poor design**: a written guide changed use when the tool was left open. It measures use, not learning.
- [A medium feature's affordance does not guarantee its actual cognitive effects: LOGO instruction designed to enhance conditional reasoning may not do so](../claims/affordance-does-not-guarantee-cognitive-effect.md) [~W]: a theoretical argument (Salomon and Gardner, 1983) that what a feature affords and how it is processed do not correspond one to one. **It limits the "guaranteed by design" wording**: a designed affordance makes a use likely, it does not guarantee the cognitive effect.
- Simulation interviews: [A student began interacting with the sim within 10 seconds and verbalized sense-making without explicit guidance](../claims/implicit-scaffolding-supports-immediate-exploration.md) [+W], [A student used slider extremes to make qualitative comparisons of skater mass effects](../claims/slider-extremes-support-qualitative-comparisons.md) [+W] and [Authors report that flexibility in sim access supports student agency while students tend to explore in a productive sequence](../claims/flexibility-supports-agency-productive-sequence.md) [+W]: one study (Podolefsky et al., 2013), a microanalysis of one sixth-grade student's think-aloud interview on Energy Skate Park: Basics, and the authors' stated belief about flexibility. They illustrate the page's argument; they do not test it.
- Architectural constraints in tutors: [A constrained architecture combining prerequisite enforcement and a minimum cognitive-demand floor substantially reduces reward hacking, lowering RHSI from 0.317 (MO) to 0.102 (ST)](../claims/constrained-architecture-reduces-rhsi.md) [+W] (a reinforcement-learning tutor in simulation, 30 sessions; d = −1.45 and −1.50 against unconstrained reward designs) and [Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding](../claims/ablation-structural-components-lower-judge-scores.md) [+W] (74 against 26 interactions with an agentic cybersecurity game, scored by a language model). Both test constraints on what the *tool* does, judged without learners.

The trial claims all come from one study, so the AI evidence rests on about four distinct studies (Bastani et al., Chen, Wong and Qiu, and Liu et al. reported second-hand), across mathematics, writing and creative tasks. Do not rank them by effect label: outcomes, comparators and designs differ.

## The evidence by question

- *When an AI assistant can produce the answer, does building limits into it (hints rather than answers, bounded or delayed access) protect unaided performance better than unrestricted access?* [Unrestricted GPT-4 access improved practice performance but harmed later exam performance, and a guardrailed hint-based version mitigated the harm, as reported by the whitepaper citing Bastani et al.](../claims/gpt4-access-harms-learning-after-withdrawal.md) [+W]
- *Do constraints built into an adaptive or agentic tutor's architecture keep what it does pedagogically productive, compared with the same system unconstrained?* [A constrained architecture combining prerequisite enforcement and a minimum cognitive-demand floor substantially reduces reward hacking, lowering RHSI from 0.317 (MO) to 0.102 (ST)](../claims/constrained-architecture-reduces-rhsi.md) [+W]

## Further evidence, not yet read against this model

Claims read for this page and used only for a limit or a row, or bearing on it from a neighbouring question.

- [How genAI is used, not who uses it, predicts whether independent performance declines or improves](../claims/persistence-costs-concentrated-among-direct-solution-users.md) [~W] — the general question of what AI use costs independent performance, owned by [Scaffolding](scaffolding.md); its studies table counts 14 distinct studies, several of them second-hand reports of the same high school mathematics trial.
- [Over-reliance on AI scaffolding risks learned helplessness, so focus should shift to fostering self-regulated AI interaction](../claims/ai-scaffolding-fading-learned-helplessness.md) [~W] — a review's argued risk, no data; it argues for teaching self-regulated use rather than only constraining the tool.
- [Hint-not-solution is the most challenging rubric dimension, with scores ranging from 6% to 81% across models](../claims/hint-not-solution-most-challenging-dimension.md) [~W] — whether a hints-only configuration holds depends on the model; used in the default design's configuration test.
- [AI-generated homework hints were positively associated with exam performance only when exam questions closely matched the homework content](../claims/ai-hints-aligned-exam-performance-only.md) [~W] — an association reported in a review (382 physics students); bears on what an unaided check should include.

## Objective and learner-valued goal

The designer's objective is usually unaided capability on a target, with the tool as a means. Elicit separately what the learner wants from the tool: to finish tonight's assignment, to understand, to look competent, to explore something they find interesting. A learner who values finishing will look for the shortcut, and a constraint they do not understand reads as an obstacle. In one physics course most students anticipated preferring a chatbot that guides first and gives answers when they are stuck, and few chose guidance only ([Most introductory physics students preferred a combination chatbot (guidance first, answers when stuck), while few preferred pure guided Q&A](../claims/students-prefer-combination-chatbot-over-guided-qa.md) [~W]). Teachers configuring chatbots wanted the opposite emphasis, preserving students' thinking and authorship ([Teachers sought to preserve student thinking and authorship by bounding chatbot answer-giving and maintaining teacher control over scope](../claims/teachers-preserve-student-thinking-bound-answer-giving.md) [+W]). Record both. Where they diverge, say why the tool is bounded, and give the learner a route to an answer after their own attempt rather than none.

For example, a nursing student using a dosage-calculation tutor wants to pass the shift's calculations quickly; the designer's objective is calculating unaided on the licensing exam. A tool that checks the student's own working and hints at the error step serves the objective; a final answer after two failed attempts serves the learner's goal without removing the attempt. Record which route each learner takes.

## What would revise this model?

The expectation should weaken if a comparison of a tool with built-in limits against the same tool with written guidance, on aligned unaided outcomes, finds no difference: then the cheaper instruction route is enough, as the prompt-literacy study hints for use. It should weaken if hints-only assistants keep preventing harm without ever producing a gain over no assistant, which would make the constraint a safety measure rather than a design for learning. If constraints help only learners with inefficient strategies with real learners as they did with simulated ones, the default should target those learners rather than bound everyone. If learners routinely get round in-tool limits with other tools, the constraint belongs in the task and the assessment. Do not protect the model by calling every failure "the affordance was not salient enough" after the fact.

Productive use in the tool, assisted performance, unaided immediate performance, delayed retention and use in the setting the learner values are separate claims. The evidence here establishes no time-to-first-action threshold, no constraint level and no schedule for loosening bounds.

## Related Principles
- [User-Centered Design for Learning](user-centered-design-for-learning.md) — the user-testing loop that finds where an interface needs text it should not.
- [Digital Learning](digital-learning.md) — whether a digital tool earns its place, and crediting gains to its method.
- [Scaffolding](scaffolding.md) — support versus none, including what AI assistance costs independent performance.
- [Guided Practice](guided-practice.md) — the practice phase in which a hints-only tutor is used.

## Examples

- [Five design principles: one artifact, dependency sequencing, progressive sim-hardware integration, scaffolded bounded choice, and paired collaboration with individual evidence](../designs/five-principles-robotics-course-framework.md)

## Key Sources
- Podolefsky, N. S., Moore, E. B., & Perkins, K. K. (2013). Implicit scaffolding in interactive simulations: Design strategies to support multiple educational goals. http://phet.colorado.edu/en/simulation/energy-skate-park-basics

<!-- deprecated 2026-10-15: superseded by the conditional model above. The previous body, kept verbatim.

## Description
Drawing on Norman's tool-design model, the article argues that effective designs make affordances salient and use productive constraints so that correct usage requires no textual direction. The authors state: "Effective designs use affordances and constraints to create tools where correct usage is guaranteed by design (Norman, 2002)." They illustrate with a door needing a push but affording pulling (poor design, requiring a PUSH sign) versus a handle-less plate (good design, no instruction needed), and apply the same logic to sim design, which should afford productive usage and constrain unproductive usage.

## Design Implications

### Context
#### Requirements
- Affordances must be readily perceived within the users' culture and context; constraints must increase the likelihood of intended usage
#### Constraints
- Textual directions such as inscribed labels are described as often a sign of poor design

### Target Learners
- all learners using designed tools or simulations

### Target Learning Objectives
- productive tool use without explicit instruction

### Claims

- [A student began interacting with the sim within 10 seconds and verbalized sense-making without explicit guidance](../claims/implicit-scaffolding-supports-immediate-exploration.md) [+W]
- [A student used slider extremes to make qualitative comparisons of skater mass effects](../claims/slider-extremes-support-qualitative-comparisons.md) [+W]
- [Authors report that flexibility in sim access supports student agency while students tend to explore in a productive sequence](../claims/flexibility-supports-agency-productive-sequence.md) [+W]
- [Ablating expert-informed structural components lowered LLM-judge scores on all dimensions, with largest drops in challenge quality, intent alignment, and domain grounding](../claims/ablation-structural-components-lower-judge-scores.md) [+W] — attached 2026-10-10 from Hornung et al. (2026), which proposed "Bound generative agent flexibility with structured autonomy rather than static scripting in high-stakes agentic learning systems"; tests this page's relationship.
- [A constrained architecture combining prerequisite enforcement and a minimum cognitive-demand floor substantially reduces reward hacking, lowering RHSI from 0.317 (MO) to 0.102 (ST)](../claims/constrained-architecture-reduces-rhsi.md) [+W] — attached 2026-10-11 from Oluseyi Olukolaa (2026), which proposed "Reward design alone may be insufficient to ensure pedagogically aligned behavior in educational RL; pair reward shaping with architectural constraints"; tests this page's relationship.
- [Guardrails in the GPT Tutor largely eliminate the negative exam effect, though no positive exam effect is observed](../claims/gpt-tutor-exam-effect-null.md) [~M] — attached 2026-10-12 from Bastani Hamsa et al. (2025), which proposed "Deploy generative AI tutors with guardrails—hints instead of answers—whenever learning, not just task performance, is the goal"; tests this page's relationship.
- [Unrestricted GPT-4 access improved practice performance but harmed later exam performance, and a guardrailed hint-based version mitigated the harm, as reported by the whitepaper citing Bastani et al.](../claims/gpt4-access-harms-learning-after-withdrawal.md) [+W]

## Related Principles
- 

## Examples

- [Five design principles: one artifact, dependency sequencing, progressive sim-hardware integration, scaffolded bounded choice, and paired collaboration with individual evidence](../designs/five-principles-robotics-course-framework.md)

## Key Sources
- Podolefsky, N. S., Moore, E. B., & Perkins, K. K. (2013). Implicit scaffolding in interactive simulations: Design strategies to support multiple educational goals. http://phet.colorado.edu/en/simulation/energy-skate-park-basics
-->

<!-- merged 2026-10-15 from patterns/four-category-implicit-scaffolding-pattern ("Four-category design pattern for implicit scaffolding in simulations"), a fragment of this page: a non-canonical page folded into its canonical parent, chosen by two models agreeing or a third settling (2026-10-15): its body as it stood. Its bullets this page lacked were added above.

# Four-category design pattern for implicit scaffolding in simulations

> **Pattern** · [All patterns](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 qualitative), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article organizes implicit scaffolding strategies into four categories that work together: scaffolding the general concept (scope, sequence, interactivity), scaffolding students' framing of sim use (opening screen, initial interaction), scaffolding to enable sense making (representations, feedback, layout, range of interactions, illuminating cases), and scaffolding for continued engagement (puzzles and challenges). The authors state: "We divide our description of implicit scaffolding strategies into four categories: Scaffolding 1) the general concept, 2) students’ framing of sim use, 3) to enable sense making, and 4) for continued engagement." Together these enable agency while affording and constraining productive actions.

## Design Implications

### Context
#### Requirements
- Strategies must be designed in coordination so learners are likely to encounter pedagogically useful scenarios through exploration
#### Constraints
- Developed iteratively over 10 years of PhET design work on 125 sims with over 600 student interviews

### Target Learners
- students using interactive science and mathematics simulations

### Target Goals
- conceptual understanding
- productive inquiry
- continued engagement

### Claims

- [Authors report that flexibility in sim access supports student agency while students tend to explore in a productive sequence](../claims/flexibility-supports-agency-productive-sequence.md) [+W]
- [A student began interacting with the sim within 10 seconds and verbalized sense-making without explicit guidance](../claims/implicit-scaffolding-supports-immediate-exploration.md) [+W]
- [A student used slider extremes to make qualitative comparisons of skater mass effects](../claims/slider-extremes-support-qualitative-comparisons.md) [+W]

## Related Patterns

- [Three pedagogical design considerations for physics simulations: consistent world view, multiple representations, and game for concept testing](../designs/three-pedagogical-simulation-design-considerations.md)

## Examples
-

## Key Sources
- Podolefsky, N. S., Moore, E. B., & Perkins, K. K. (2013). Implicit scaffolding in interactive simulations: Design strategies to support multiple educational goals. http://phet.colorado.edu/en/simulation/energy-skate-park-basics
-->
