---
type: principle
id: distributed-cognition
title: Distributed Cognition
description: "For a task too large for one learner to hold or do alone, putting part of the work into shared representations, tools or partners is expected to raise performance with those aids present, and to build what the learner can do alone only when the parts the target requires stay with the learner and the learner's decisions to rely on aids are calibrated; no claim tests distributed against individual work, while single studies test how much to hand to an AI tool and feedback that calibrates offloading."
canonical: true
status: review
generated:
  by: claude/unspecified
  at: 2026-10-15
---

# Distributed Cognition

> **Principle** · [All principles](index.md)
> **Evidence** · 40 claims (21 for, 19 mixed) · 37 studies (10 theoretical, 8 causal, 7 review, 6 qualitative, 3 design, 2 associational, 1 quant-synthesis), `q1`–`q4` · 4 of 37 report an effect size · 35 claims rest on one study

## Conditional relationship

This page owns the **division of a task's cognitive work across the learner, external representations, tools and other people**, and the choice of which outcome that division is judged on. Salomon's distinction, as one claim page records it, separates two outcomes that are often run together: **effects *with*** the tool or group (how well the person-plus-system performs) and **effects *of*** it (the "cognitive residue": what the person can do alone afterwards) ([Salomon distinguishes effects with the computer (system performance) from effects of the computer (cognitive residue on the solo performer)](../claims/effects-with-versus-effects-of-computer.md) [+M]).

The relationship: for a task whose demands exceed what one learner can hold in mind or do alone (many interacting elements, several steps to track, expertise split across people), putting part of the work into a well-organised external representation, a tool or a partner is expected to raise performance **with** the system (`immediate-performance` with aids present). Whether it also builds what the learner can do **alone** (`immediate-performance` with aids removed, `delayed-retention`, `near-transfer`) is expected to depend on two things: whether the part the target says must be done unaided stays with the learner, and whether the learner's own decisions about when to rely on an aid are calibrated to how well they actually perform. Learners tend to rely on aids more than their performance warrants, and feedback on their own predictions is expected to correct that.

The relationship is conditional on the learner's task-specific starting response (`novice` learners lean on external structure that `advanced` learners may not need), on age (children and adolescents are reported to err in opposite directions), on whether the outcome counts the system or the solo performer, on how the external resources are organised and shared, and on the horizon.

**What tests it in the wiki, and what does not.** No claim in the wiki compares a task distributed across people, roles or shared representations with the same task done individually, on either outcome. Two parts of the relationship are tested, each by few studies:

- *How much to hand to a tool.* One classroom quasi-experiment (168 students in six intact classes, AI-assisted writing) found open collaboration with an AI gave the best writing while the AI was present and bounded AI support gave the best independent no-AI writing at week 8. That relationship, a tool that could do the learner's part, is owned by [Technology Augments, Not Supplants, Learning Processes](technology-augments-not-supplants-processes.md); this page uses its result and does not repeat its model.
- *Whether learners decide well when to offload, and whether feedback helps.* A review and a pre-registered experiment (N = 164) report that people set more reminders than is optimal; in that experiment a short prediction-plus-feedback intervention reduced the bias (d = .347). A second pre-registered experiment with an LLM assistant found metacognitive feedback lowered answer offloading and raised the odds of a correct unaided test item, though that interval includes no effect.

How the converted siblings sit beside this page: [Collaborative Learning](collaborative-learning.md) holds joint work against individual work on individually measured understanding; this page holds the representations, roles and tools that carry the shared work, and the decision of what stays with each person. [Chunking](chunking.md) and [Cognitive Load Theory](cognitive-load-theory.md) hold how information is grouped and how load is managed inside one learner. [Self-Monitoring](self-monitoring.md) and [Self-Regulated Learning](self-regulated-learning.md) hold learners checking their own performance against criteria; the offloading decision is one such judgement. [Scaffolding and Fading](scaffolding-and-fading.md) holds how support is withdrawn; external representations are faded the same way.

## Default design, while the relationship is untested

The earlier page's guidance, kept as a default a designer can act on and revise. Each step says whether a claim bears on it; most are untested proposals. Quantities are proposals unless a claim gives them.

1. **Decide which outcome counts before dividing the work.** Write down, for this task, whether success is the team's or system's performance with every aid present (a ward team using a checklist, a lab group with shared data), the individual's performance alone afterwards, or both. If both, name the parts each learner must be able to do unaided. Basis: [Salomon distinguishes effects with the computer (system performance) from effects of the computer (cognitive residue on the solo performer)](../claims/effects-with-versus-effects-of-computer.md) [+M] (a conceptual distinction, not a test).
2. **Map the task's load, then assign each part.** List what has to be remembered, tracked, computed, decided and checked. Assign each to the learner's head, an external representation, a tool or a teammate. Keep with each learner what step 1 says must be done unaided; put the rest outside the head. Basis: external structure lowers the number of units to be held ([Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S], carried from memory experiments to task design); for a tool that could do the learner's part, bounded support gave better unaided writing at week 8 than open collaboration ([Bounded AI support outperformed open collaboration on all four Week 8 independent no-AI outcomes, though exact wild-cluster p values sat at the 0.050–0.063 boundary](../claims/bounded-beats-open-week8-independent-outcomes.md) [+M]).
3. **Give the group one external representation that carries the shared memory.** One [shared document](../elements/shared-documents.md), diagram, checklist or board that everyone can see and edit, in a fixed layout: the goal at the top, who holds which part, the current state of the work, open questions. Keep any one view to a few groups of items (the chunking claim page reports three to five chunks as the limit for novel material). Untested as a design; check it with the learners, because representations that help experts externalise their reasoning are not always the ones novices can follow ([Representation-alignment tension between expert externalization and novice comprehension](../claims/representation-alignment-tension-expert-novice.md) [~M]).
4. **Use groups only where the task is too big for one person.** If one learner could do the task alone in the time, make it individual work or make it bigger. Basis: [Collaborative tasks should be complex enough that joint effort is worthwhile, engaging the collective working memory effect](../claims/collective-working-memory-effect-task-complexity.md) [+W] (a primer's report of theory); joint work often fails to be productive when it is only "work together" ([Collaborative situations often fail to be productive in practice, so orchestrating collaboration is not simple](../claims/collaborative-situations-often-fail-productive.md) [~W]).
5. **Make roles and progress visible enough to monitor.** Name each role on the shared representation ([group roles](../elements/group-roles.md): for example a recorder who keeps the representation current, a checker who compares the work with the criteria), and give a progress line a teacher and the group can read at a glance. Basis: [Self-regulated learning models treat self-monitoring as a core process through which learners notice gaps and adjust strategy](../claims/self-monitoring-improves-self-regulation.md) [~M] (reviews of individual self-regulation, carried to groups); roles as such are an untested proposal.
6. **Train the decision to rely on an aid.** Before learners use a reminder, a calculator, a reference sheet or an AI assistant on a practice item, ask them to predict whether they would get it right unaided; after the item, show them how they actually did unaided and with the aid. Five such practice trials reduced over-reliance in one experiment. Basis: [In Experiment 1, a five-trial metacognitive prediction-plus-feedback intervention significantly reduced reminder bias, producing more optimal reminder-setting behaviour](../claims/metacognitive-feedback-reduces-reminder-bias.md) [+M]; with an LLM assistant, [In one preregistered experiment, metacognitive feedback on learners' own LLM use lowered the odds of answer offloading and raised the odds of a correct unaided answer on one-sided tests, with 95% intervals reaching no effect](../claims/metacognitive-feedback-reduces-llm-answer-offloading-improves-unaided-performance.md) [+M]. A reward for effort did not do the same ([An effort-based reward did not significantly reduce answer offloading or improve unaided performance](../claims/effort-based-reward-no-effect-offloading-or-unaided-performance.md) [~M]).
7. **Check each learner with the aids removed.** End each session with one or two items, or one step of the task, done alone with the shared representation and tools out of reach, if step 1 names an unaided outcome. Record what the learner did with and without the aids side by side. Basis: the week-8 unaided result above; answer offloading during learning was associated with lower unaided test performance in an exploratory analysis ([Greater answer offloading during learning is associated with lower subsequent unaided performance (exploratory)](../claims/answer-offloading-associated-lower-unaided-performance-exploratory.md) [~M]). The review distinction between offloading that replaces internal processing and offloading that duplicates it is a framework, not a finding ([Substitutive offloaders show severe performance decline when external stores become unavailable, while duplicative offloaders maintain accuracy](../claims/substitutive-duplicative-offloading-outcomes.md) [~W]).
8. **Fade the external structure across sessions, and move learners on by the unaided check.** A default arc for a unit of four to six sessions: *early sessions*, the teacher provides the shared representation already laid out, assigns roles, and bounds the tool (hints and checks, no finished answers); *middle sessions*, the group builds its own representation from a blank template, roles rotate each session so every learner holds each part once, and the prediction-and-feedback check of step 6 runs on two or three items per session; *late sessions*, the template is withdrawn, the tool is available only on request, and the unaided check covers the whole of what step 1 names. Move a learner or group to the next stage once they pass the unaided check in two consecutive sessions; return to the earlier stage after a failed one. If step 1 names only system performance (a team procedure where the checklist stays in use at work), do not fade the representation: fade the teacher's prompting and keep the artifact. The arc and thresholds are untested proposals; support that responds to the learner's last attempt is better supported than fixed support ([Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M], one-to-one tutoring in most of its studies), and how to fade is modelled in [Scaffolding and Fading](scaffolding-and-fading.md).

A default 50-minute session (untested proposal): 5 minutes to set or check roles and open the shared representation; 30 minutes of joint work with the representation kept current; 5 minutes of prediction and comparison on the aid decision; 10 minutes for the unaided check and a note of what it showed. In a 25-minute session, halve the joint work and keep the unaided check to one item.

When a condition is not met: if the task fits in one head, drop the group and the shared artifact; if no one can see the shared representation during the work (no screen, no wall), give each learner a paper copy of the same layout and collect them at the end; if the brief wants system performance only, skip step 7 and evaluate the team's product with every aid in place.

## Fitting the design to a situation

The three facts that most change the decision:

- **Which outcome counts: the system or the solo performer.** A team that will always work with its checklist and its colleagues needs a well-designed system; a learner who will sit an unaided exam or work alone later needs the critical parts kept in their own head. If unstated, ask: when this matters later, which of these aids and people will the learner have with them?
- **How the learner currently uses aids on this task.** Under-use (children, or learners who do not trust tools) and over-use (reaching for the tool before trying) need opposite moves. If unstated, ask: on one item now, does the learner try first or reach for the aid, and how accurate are they each way?
- **Whether the task is too large for one person.** Distribution earns its cost only when one learner cannot hold or do the whole task in the time. If unstated, ask: could one capable learner do this alone in the time given, and what would they have to write down to do it?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are `advanced` on this task, or already succeed alone | Give them a blank template rather than a laid-out representation, fewer assigned roles, and judge them on the unaided check from the first session | [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] (its Discussion: imposed chunking helps only until the learner can chunk unaided; carried from memory research) |
| Learners are `child` (primary age) | Prompt them to use the external aid (write it down, look at the board) and show when it would have helped; the prediction-and-feedback check is about under-use, not over-use | [Review reports a developmental shift in cognitive offloading: children under-use external aids while adolescents over-rely on them](../claims/developmental-shift-cognitive-offloading.md) [~W] (one word-pair memory study, reported second-hand) |
| Learners are `adolescent`, or have an AI assistant in reach | Bound the tool to hints and checks, run the prediction-and-feedback check of step 6 on every practice set, and keep the unaided check | Developmental claim above [~W]; [Bounded AI support outperformed open collaboration on all four Week 8 independent no-AI outcomes, though exact wild-cluster p values sat at the 0.050–0.063 boundary](../claims/bounded-beats-open-week8-independent-outcomes.md) [+M] (one quasi-experiment, six classes); the tool decision is modelled in [Technology Augments, Not Supplants](technology-augments-not-supplants-processes.md) |
| Adults in work settings, where the checklist, system or colleague will be there on the job | Treat the job aid as part of the performance: train with the real aid, judge the team's performance with it present, and check unaided only the steps the job requires from memory (an emergency, a step done away from the aid) | Untested proposal; [Salomon distinguishes effects with the computer (system performance) from effects of the computer (cognitive residue on the solo performer)](../claims/effects-with-versus-effects-of-computer.md) [+M] names the choice, it does not test it |
| Goal is the learner's unaided understanding (`concept`, `principle`) for an individual exam | Keep the reasoning steps with each learner; the shared representation records the group's results, not the reasoning; every learner takes a turn explaining the representation unaided | Untested proposal; [Among AI-exposed students, open collaboration predicted higher aggregate offloading, which was associated with lower Week 8 higher-order thinking (indirect estimate −0.34)](../claims/offloading-mediation-lower-independent-hot.md) [~M] (exploratory, one study, AI tool rather than peers) |
| Learners keep reaching for the aid or the answer before trying | Ask for a prediction before each aided item and show the unaided result after; do not substitute a reward for effort | [In Experiment 1, a five-trial metacognitive prediction-plus-feedback intervention significantly reduced reminder bias, producing more optimal reminder-setting behaviour](../claims/metacognitive-feedback-reduces-reminder-bias.md) [+M]; [An effort-based reward did not significantly reduce answer offloading or improve unaided performance](../claims/effort-based-reward-no-effect-offloading-or-unaided-performance.md) [~M] (both online adult samples) |
| Learners have low confidence, or low literacy | Expect over-reliance driven by low confidence: show them their own unaided accuracy early so the decision rests on evidence; make the shared representation visual (icons, a fixed grid) with few words | [In Experiment 1, lower confidence predicted greater offloading beyond objective performance in the no-feedback group, but not in the feedback group](../claims/confidence-predicts-offloading-no-feedback-only.md) [+M] (online adults, memory task); the visual layout is an untested proposal |
| Some learners remote, some in the room; or phone-only | Keep one shared representation online that both sites edit, with one person in the room assigned to keep it current aloud for remote members; on phones, keep it to one screen of short entries and move detail into linked items | Untested proposal |
| One teacher for many groups, or scarce facilitator time (volunteers, a short check-in) | Read each group's shared representation and role line instead of listening in; spend the check-in only on groups whose progress line has not moved or whose unaided check failed | Untested proposal; contingent support is better supported one-to-one than at class scale ([Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M]) |
| A single session only | Use a laid-out representation and assigned roles throughout; spend the last 10 minutes on one unaided item per learner; report the session's result as performance with aids and one unaided check, not as learning that lasts | Untested proposal |
| A fixed short time budget (for example 20 minutes) | 2 minutes roles, 12 minutes joint work, 6 minutes unaided check; drop the prediction step if the brief has no aid decision to train | Untested proposal |
| The brief names its own checklist, template, representation or rubric | Keep it as the shared representation and the criteria; change only the layout so roles and progress are visible, and add the unaided check beside it only if an unaided outcome is wanted | Untested proposal (wave lesson: a brief's own routine is kept) |
| The brief uses its own categories for the work | Lay out the shared representation in those categories, not in this page's goal–roles–state headings | Untested proposal |
| Material is private or sensitive (personal reflections, client records) | Keep the shared representation to what the group needs to coordinate; each learner keeps personal material in their own space and decides what enters the shared one | Untested proposal |
| A whole-task performance the brief wants kept whole (a simulation, a ward round, a performance for a real audience) | Distribute by role inside the whole task rather than splitting it into separate pieces; debrief afterwards with the shared record; the unaided check is a short individual run-through of one role | Untested proposal |
| An error on the job is costly (safety, compliance) | Keep the checklist in use as part of the system; add a check that each learner can say why each item is on it and what to do if the aid is unavailable | Untested proposal |

Eight of the sixteen rows cite a claim: four rest on claims tested with learners (the child row, through one second-hand study; the bounded-tool row, one quasi-experiment; the offloading-decision and confidence rows, online adult experiments), one carries chunking research from memory tasks, and three cite a claim only to name a choice or a limit. The other eight are untested proposals. The offloading claims come from online adult samples on memory or study tasks and are carried to classrooms and groups here.

## Observation, state and explanation

What can be observed: which aids each learner used on which item, whether they predicted their own unaided performance and how accurately, what the shared representation showed at the end, which role each person held, and how each learner did on the unaided check. "Relies on the group", "has internalised the procedure" and "offloads too much" are inferred states. Performance with the aids present shows what the system can do, not what any one member can do.

| Response | Plausible explanations | Observation that could change the interpretation |
|---|---|---|
| Group product is strong; most members fail the unaided check | The representation or one member carried the reasoning; the unaided item differs from the task more than intended; the aids were used as substitutes, not duplicates | Ask each member to explain one entry of the representation unaided; give a matched unaided item with only the template's headings visible. |
| A learner never uses the shared representation or the tool | They do not need it (already `advanced`); they do not know how to read it; under-use, as reported for younger learners | Compare their unaided accuracy with the group's; ask them to say what one entry means. |
| A learner uses the aid on every item, including ones they solve unaided | Low confidence rather than low skill; habit; the aid is cheaper than the effort | Ask for a prediction before an item and compare it with their unaided result; repeat after feedback. |
| The shared representation is out of date or contradicts the work | No one holds the recorder role; the layout does not fit the task; members work in separate copies | Check who last edited it and when; ask the group what they would change in its layout. |
| Strong in-session unaided check, weak a week later | Little consolidation; the check came straight after aided practice | Re-test at the delay with a new item and record what aids were used in between. |

These rows are proposals, untested as diagnostics. A probe is itself practice and changes what it measures, so record each one and keep the explanations still open.

## Evidence and qualifications

No claim in the wiki compares distributing a task across people, roles or shared representations with individual work. The claims below test neighbouring parts of the relationship or limit it.

- [Salomon distinguishes effects with the computer (system performance) from effects of the computer (cognitive residue on the solo performer)](../claims/effects-with-versus-effects-of-computer.md) [+M]: a 1999 conference paper's synthesis of the distributed-cognition literature, with Pea's critique that a low share of user contribution need not be alarming and that user–tool relationships evolve. A conceptual distinction; no data.
- [Bounded AI support outperformed open collaboration on all four Week 8 independent no-AI outcomes, though exact wild-cluster p values sat at the 0.050–0.063 boundary](../claims/bounded-beats-open-week8-independent-outcomes.md) [+M] and [Open AI collaboration yielded the highest supported writing quality, while bounded AI support yielded the highest independent no-AI Week 8 performance](../claims/genai-supported-performance-independent-divergence.md) [+M]: one class-clustered quasi-experiment, 168 students in six intact classes, three conditions (no AI, bounded, open). Supported writing was highest under open collaboration; at the week-8 independent assessment the bounded condition was highest, with student-level g from 0.83 to 1.21, but class-clustered p values of 0.050–0.063 with six classes. The claim page's evidence line counts two studies; both entries are the same article. It is the clearest case in the wiki of effects *with* and effects *of* diverging, and it concerns an AI tool, not peers.
- [In Experiment 1, a five-trial metacognitive prediction-plus-feedback intervention significantly reduced reminder bias, producing more optimal reminder-setting behaviour](../claims/metacognitive-feedback-reduces-reminder-bias.md) [+M]: pre-registered online experiment, 164 adults, an optimal-offloading memory task with financial incentive; feedback reduced reminder bias against no feedback (d = .347, one-tailed). Both groups still set more reminders than optimal ([In Experiment 1, participants in both groups were significantly biased towards excessive reminder use relative to the optimal strategy](../claims/excessive-reminder-bias-both-groups-exp1.md) [+M]).
- [In one preregistered experiment, metacognitive feedback on learners' own LLM use lowered the odds of answer offloading and raised the odds of a correct unaided answer on one-sided tests, with 95% intervals reaching no effect](../claims/metacognitive-feedback-reduces-llm-answer-offloading-improves-unaided-performance.md) [+M]: a pre-registered online experiment; feedback lowered the odds of answer offloading (OR = 0.47, 95% CI 0.22 to 1.00) and raised the odds of a correct unaided test item (OR = 1.51, 95% CI 0.98 to 2.33). The second interval includes no effect, so the title's "improves" is stronger than the interval. In the same study feedback broke the run of offloading on consecutive items without changing whether learners used the assistant at all ([Metacognitive feedback disrupted the tendency to repeat answer offloading across consecutive items without changing whether participants engaged with the assistant](../claims/metacognitive-feedback-disrupts-repeated-answer-offloading.md) [+M]), and an effort-based reward did not significantly change offloading or unaided performance ([An effort-based reward did not significantly reduce answer offloading or improve unaided performance](../claims/effort-based-reward-no-effect-offloading-or-unaided-performance.md) [~M]; equivalence not tested).
- [Individuals systematically overuse reminders relative to the optimal offloading level, and reminder bias correlates with confidence and metacognitive bias](../claims/reminder-bias-overuse-external-aids.md) [+M] and [Feedback interventions show phase-specific effects: advice feedback reduces reminder bias, but ranking feedback alters beliefs without increasing offloading](../claims/feedback-effects-on-offloading-mixed.md) [~M]: one 2026 review reporting earlier studies second-hand. Advice feedback reduced reminder bias; ranking feedback shifted beliefs but did not increase offloading. Not every kind of feedback moves the decision.
- **Limits.** [Cognitive offloading is positively, not negatively, associated with transformative learning experience, contrary to the hypothesized negative effect](../claims/cognitive-offloading-positively-predicts-transformative-learning.md) [+W]: in a 912-student survey, delegating tasks to generative AI positively predicted self-reported transformative learning (β = 0.333, f² = 0.140), against the authors' hypothesis. A self-report association, but it warns against treating all offloading as loss. [Strategic cognitive offloading can support transformative learning only when the offloading decision is intentional](../claims/strategic-offloading-intentional-transformative-learning.md) [~W] reports (second-hand, no effect sizes) that the benefit depends on the decision being intentional, which is what step 6 trains. [Review reports a developmental shift in cognitive offloading: children under-use external aids while adolescents over-rely on them](../claims/developmental-shift-cognitive-offloading.md) [~W] means the direction of the correction depends on age. [A tool's effectiveness results from the whole configuration of events, activities, and contexts in which it is used](../claims/tool-effectiveness-depends-on-context-configuration.md) [~M] (Salomon, cited; Logo results varied by context) warns against expecting a tool or artifact alone to change much.
- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S]: reviews and experiments on immediate memory, gathered in its table from four distinct studies; the basis for external structure lowering load, carried here from memory tasks to shared representations, which no study in it tests.
- [Self-regulated learning models treat self-monitoring as a core process through which learners notice gaps and adjust strategy](../claims/self-monitoring-improves-self-regulation.md) [~M] and [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M]: individual self-regulation reviews and mostly one-to-one tutoring studies (its table gathers 25 distinct studies across it and narrower claims); carried here to visible group progress and to fading the shared representation.

Learners, tasks and settings differ across these (online adults on memory tasks, students writing with AI in six classes, surveys), so do not rank them by effect label. None measures a peer group with a shared representation against individuals.

## The evidence by question

- *Do learners rely on external aids more, or less, than their own performance warrants?* [Individuals systematically overuse reminders relative to the optimal offloading level, and reminder bias correlates with confidence and metacognitive bias](../claims/reminder-bias-overuse-external-aids.md) [+M]
- *Does feedback on their own performance make learners' decisions to offload better calibrated?* [Feedback interventions show phase-specific effects: advice feedback reduces reminder bias, but ranking feedback alters beliefs without increasing offloading](../claims/feedback-effects-on-offloading-mixed.md) [~M]

## Further evidence, not yet read against this model

Claims the earlier page cited that are not used above, each with how far it bears on this page.

- [Open collaboration involved more prompts, greater text incorporation, less self-generated text, and deeper idea and reasoning offloading than bounded support](../claims/open-collaboration-process-intensity-profile.md) [+W] — process measures from the same AI-writing quasi-experiment as the bounded-versus-open result; describes what open collaboration hands to the tool. Marked by its own page as a possible duplicate of the next claim.
- [Open collaboration exceeded bounded support in offloading at all four layers, with the largest differences at the idea and reasoning layers](../claims/open-collaboration-deeper-layer-offloading.md) [+W] — same study; the deeper layers (ideas, reasoning) are where open collaboration offloaded most, which bears on step 2's decision of what to keep with the learner.
- [Higher reliance on AI tools is correlated with lower critical-thinking performance, mediated by cognitive offloading](../claims/ai-reliance-correlated-lower-critical-thinking-offloading.md) [~W] — a second-hand report of a correlational user study; bears on the unaided-outcome side, about AI tools rather than shared representations.
- [Some content-based offloading profiles differed in prompting volume even though volume was not a clustering variable, suggesting what is offloaded constrains how much is offloaded](../claims/offloading-content-constrains-volume.md) [~W] — an exploratory clustering of 97 students' prompts; bears only indirectly (what is offloaded matters, not only how much).

Also bearing on this page, read for it but not used in the model: [Unrestricted GPT-4 access in high-school mathematics raised assisted practice performance but left students worse off after withdrawal](../claims/gpt4-access-harms-learning-after-withdrawal.md) [~M] (one trial, reported second-hand; owned by the tool page), [Individual user goals, such as avoiding cognitive load, can contradict the objectives of the educational community](../claims/user-goals-contradict-educational-objectives.md) [~M] (used below on goals), and [External conceptual resources support teachers' pedagogical judgment by affording richer representations and more productive problem frames](../claims/external-resources-support-pedagogical-judgment-alignment.md) [+M] (two debrief episodes in a teachers' partnership; external representations supporting a group's reasoning, qualitatively).
- [The IW-supported group needed less teacher scaffolding in the late problem-solving stage, where nurse and instructor discourse decreased, while scaffolding increased from early to late stage in the TW condition](../claims/iw-group-less-late-stage-scaffolding.md) [+W] — attached 2026-10-18 from Lu et al. (2010), which proposed "Design CSCL visualization and argumentation tools so externalized group work frees the teacher from task structuring to scaffold by increasing challenge".
- [Groups using the Graphical Debate-tool constructed representations of significantly higher quality than groups using the Textual Debate-tool, for both debate positions.](../claims/gd-tool-higher-quality-representations.md) [+W] — attached 2026-10-18 from Jeroen Janssen et al. (2008), which proposed "Take representational guidance into account during instructional design because it affects group and individual performance"; tests this page's relationship.
- [GD groups wrote essays significantly better in total grounds quality, total conceptual quality, and average conceptual quality, but did not cover more topics and were not better in average grounds quality.](../claims/gd-essays-total-grounds-conceptual-quality.md) [+W] — attached 2026-10-18 from Jeroen Janssen et al. (2008), which proposed "Take representational guidance into account during instructional design because it affects group and individual performance"; tests this page's relationship.

## Objective and learner-valued goal

The designer's objective is either a working system (a team or learner that performs well with its aids) or individual capability that survives removing them, at a stated horizon; say which. Elicit separately what the learner wants from the tools and the group: to finish the task, to look competent in front of peers, to spend less effort, to be able to do the job alone. One claim page reports an observation that many student computer users' goal seems to be avoiding cognitive load, at odds with the educational objective ([Individual user goals, such as avoiding cognitive load, can contradict the objectives of the educational community](../claims/user-goals-contradict-educational-objectives.md) [~M]). Agreement and divergence are both observations: a learner whose goal is to finish will offload whatever the design allows, so the design, not exhortation, decides what stays with them.

For example, a nursing student on placement may want to get through the medication round without mistakes, using the ward's checklist and a senior colleague; the designer's objective may be that the student can explain each check unaided. Both can be served: run the round with the checklist (the system), then ask for the reason behind two checks with the checklist put away (the residue). Record both, so that a clean round is not read as the unaided understanding.

## What would revise this model?

The expectation should weaken if studies comparing distributed and individual work on the same task find no difference in unaided outcomes when the critical parts are kept with each learner, or find that keeping them there costs system performance without any unaided gain. If calibration training (prediction plus feedback) does not carry from memory and LLM tasks to group work and shared representations, step 6 should be dropped for groups. If learners who offload heavily turn out to do as well alone at a delay, as the positive survey association hints, the unaided check matters less than this page says. If fading a shared representation harms performance in settings where the artifact stays in use on the job, the "keep the artifact" branch should become the default. Do not protect the model by calling every failure "the wrong part was offloaded" after the fact.

Performance with aids present, unaided performance at the end of a session, delayed retention, and the learner's use of the aids in their own setting are separate claims. The present evidence sets no rule for how much to distribute, no group size and no fading schedule.

## Claims

Claims the earlier page cited, each now placed above (in the model, the evidence or further evidence):

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S]
- [Self-regulated learning models treat self-monitoring as a core process through which learners notice gaps and adjust strategy](../claims/self-monitoring-improves-self-regulation.md) [~M]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M]
- [Review reports a developmental shift in cognitive offloading: children under-use external aids while adolescents over-rely on them](../claims/developmental-shift-cognitive-offloading.md) [~W]
- [Strategic cognitive offloading can support transformative learning only when the offloading decision is intentional](../claims/strategic-offloading-intentional-transformative-learning.md) [~W]
- [Open collaboration involved more prompts, greater text incorporation, less self-generated text, and deeper idea and reasoning offloading than bounded support](../claims/open-collaboration-process-intensity-profile.md) [+W]
- [Open collaboration exceeded bounded support in offloading at all four layers, with the largest differences at the idea and reasoning layers](../claims/open-collaboration-deeper-layer-offloading.md) [+W]
- [Cognitive offloading is positively, not negatively, associated with transformative learning experience, contrary to the hypothesized negative effect](../claims/cognitive-offloading-positively-predicts-transformative-learning.md) [+W]
- [Higher reliance on AI tools is correlated with lower critical-thinking performance, mediated by cognitive offloading](../claims/ai-reliance-correlated-lower-critical-thinking-offloading.md) [~W]
- [Some content-based offloading profiles differed in prompting volume even though volume was not a clustering variable, suggesting what is offloaded constrains how much is offloaded](../claims/offloading-content-constrains-volume.md) [~W]
- [The editorial reports that successful collaborative making teams resolved coordination challenges through intertwined social-discursive and materially mediated processes](../claims/making-team-success-coordination-entanglement.md) [+W]
- [Merging different technical understandings of Minecraft items into shared nomenclature enabled parallel division of building work (Extract 2)](../claims/merged-technical-understanding-minecraft-nomenclature.md) [+W]
- [Multi-modal representations created during collaboration act as metaphors that shape joint reasoning and meaning making](../claims/multimodal-representations-as-metaphors-joint-reasoning.md) [~W]
- [Collaborative dynamic-geometry problem solving relies on coordinating math-content and social/collaborative resources](../claims/oner-coordinated-math-social-resources.md) [~W]
- [Presentation technologies such as paper posters and PowerPoint mediate the sharing of ways of seeing in design studio critique sessions](../claims/presentation-technologies-mediate-ways-of-seeing.md) [+W]
- [In the learning phase, group experience and information distribution each produce significant multivariate effects on performance, mental effort, and efficiency, without interacting](../claims/zambrano-2019-learning-phase-manova-main-effects.md) [+W]

## Related Principles
- [Social Learning](../theories/sociocultural-theory.md) — distributed cognition often depends on learning through interaction with others
- [Community of Inquiry](community-of-inquiry.md) — one context where cognition is distributed across discourse, facilitation, and shared artifacts
- [Situated Learning](../theories/situated-learning.md) — provides the contextual account of why cognition is often distributed in real practice
- [Collaborative Learning](collaborative-learning.md) — joint against individual work on individually measured understanding; this page holds the artifacts, roles and tools that carry the joint work
- [Technology Augments, Not Supplants, Learning Processes](technology-augments-not-supplants-processes.md) — owns the decision of what a tool that could do the learner's part should do
- [Chunking](chunking.md) and [Cognitive Load Theory](cognitive-load-theory.md) — how information is grouped and load is managed within one learner
- [Self-Monitoring](self-monitoring.md) — the judgement behind a learner's decision to rely on an aid
- [Scaffolding and Fading](scaffolding-and-fading.md) — how external support is withdrawn
- [Distributed cognition: cognition as a function of a system of people and tools](../theories/distributed-cognition-system-unit-of-analysis.md) — the theory page this principle applies

## Examples

### Illustrative

**[Shared Documents](../elements/shared-documents.md)** — Learners co-construct an artifact that carries part of the group’s memory, coordination, and reasoning.

**Checklists, diagrams, and dashboards in team-based work** — External representations reduce memory burden and help groups coordinate complex tasks.

**Studio or lab collaboration** — Different learners, tools, and artifacts each carry part of the cognitive work, and success depends on how well those pieces fit together.

**Ward or workplace job aids** — A [checklist](../strategies/checklists.md) or [performance support](../elements/performance-support.md) tool stays part of the job; training judges the team with it in use and checks unaided only the steps the job requires from memory.

## Key Sources
- Hutchins, E. (1995). *Cognition in the wild*. MIT Press. [doi:10.7551/mitpress/1881.001.0001](https://doi.org/10.7551/mitpress/1881.001.0001)
- Salomon, G. (Ed.). (1993). *Distributed cognitions*. Cambridge University Press.

<!-- deprecated 2026-10-15: superseded by the conditional model above. The previous body, kept verbatim.

## Description
Distributed cognition is the principle that thinking and problem solving are often spread across people, tools, representations, and environments rather than residing entirely inside one learner. It is useful when instruction relies on collaboration, external representations, or shared expertise.

## Implications

Distributed cognition matters when successful performance depends on how learners coordinate with tools, artifacts, and other people rather than only on what they can hold in mind individually. The principle reframes instruction away from the isolated learner and toward the whole cognitive system: people, prompts, diagrams, checklists, platforms, and social routines. In design terms, this means that external supports are not just aids for weak learners. They are often part of the normal architecture of expert reasoning, especially when external representations reduce internal memory burden [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S]. The risk is fragmentation: if the distributed system is poorly coordinated, learners may experience scattered resources instead of support, which is why roles, progress, and use of supports have to be visible enough to monitor [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M] and responsive enough to match actual need rather than adding generic complexity [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M].

### Context
#### Requirements
- **Tasks where tools or peers meaningfully extend reasoning** — the problem should actually benefit from external representation, division of expertise, or coordination
- **Design that makes distributed resources usable and visible** — learners need to know what tools, people, or artifacts to rely on and how
#### Constraints
- **Poor coordination can make distributed work feel fragmented rather than supportive**
- **External supports can become crutches if learners never understand how to use them strategically**
- **Shared cognition still requires accountability** — distribution does not eliminate the need for individual understanding and contribution

### Target Learners
- Learners working in collaborative, tool-rich, or professional-like environments
- Learners solving problems that benefit from diagrams, shared documents, checklists, or specialized roles
- Learners preparing for real work settings where cognition is routinely distributed across systems

### Target Learning Objectives
- Improve shared reasoning and effective use of external cognitive supports
- Help learners coordinate with tools, representations, and collaborators productively
- Build understanding of how reasoning is supported by environments, not just minds in isolation

### Theory
#### Supporting
- Situated and sociocultural perspectives — cognition is shaped by participation, tools, and context
- [Situated Learning](../theories/situated-learning.md) — distributed cognition often appears within authentic social practice
- [Collaborative Learning](collaborative-learning.md) — shared reasoning can depend on how work and representation are distributed

#### Contradicting / Qualifying
- [Information Processing Theory](../theories/information-processing-theory.md) — qualifies that individual attention, memory, and processing limits still matter inside distributed systems

### Claims

- [Chunking reduces working memory load by grouping information into fewer, more meaningful units.](../claims/chunking-reduces-working-memory-load.md) [~S] — external representations can reduce internal memory burden when they are organized and interpretable
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M] — distributed systems become stronger when progress and roles are visible enough to monitor
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M] — tools and collaborators are most helpful when support is responsive rather than generic
- [Review reports a developmental shift in cognitive offloading: children under-use external aids while adolescents over-rely on them](../claims/developmental-shift-cognitive-offloading.md) [~W]
- [Strategic cognitive offloading can support transformative learning only when the offloading decision is intentional](../claims/strategic-offloading-intentional-transformative-learning.md) [~W]
- [Open collaboration involved more prompts, greater text incorporation, less self-generated text, and deeper idea and reasoning offloading than bounded support](../claims/open-collaboration-process-intensity-profile.md) [+W]
- [Open collaboration exceeded bounded support in offloading at all four layers, with the largest differences at the idea and reasoning layers](../claims/open-collaboration-deeper-layer-offloading.md) [+W]
- [Cognitive offloading is positively, not negatively, associated with transformative learning experience, contrary to the hypothesized negative effect](../claims/cognitive-offloading-positively-predicts-transformative-learning.md) [+W]
- [Higher reliance on AI tools is correlated with lower critical-thinking performance, mediated by cognitive offloading](../claims/ai-reliance-correlated-lower-critical-thinking-offloading.md) [~W]
- [Some content-based offloading profiles differed in prompting volume even though volume was not a clustering variable, suggesting what is offloaded constrains how much is offloaded](../claims/offloading-content-constrains-volume.md) [~W]

## Related Principles
- [Social Learning](../theories/sociocultural-theory.md) — distributed cognition often depends on learning through interaction with others
- [Community of Inquiry](community-of-inquiry.md) — one context where cognition is distributed across discourse, facilitation, and shared artifacts
- [Situated Learning](../theories/situated-learning.md) — provides the contextual account of why cognition is often distributed in real practice

## Examples

### Illustrative

**[Shared Documents](../elements/shared-documents.md)** — Learners co-construct an artifact that carries part of the group’s memory, coordination, and reasoning.

**Checklists, diagrams, and dashboards in team-based work** — External representations reduce memory burden and help groups coordinate complex tasks.

**Studio or lab collaboration** — Different learners, tools, and artifacts each carry part of the cognitive work, and success depends on how well those pieces fit together.

## Key Sources
- Hutchins, E. (1995). *Cognition in the wild*. MIT Press. [doi:10.7551/mitpress/1881.001.0001](https://doi.org/10.7551/mitpress/1881.001.0001)
- Salomon, G. (Ed.). (1993). *Distributed cognitions*. Cambridge University Press.

-->
