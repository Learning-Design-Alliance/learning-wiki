---
type: pattern
id: experiential-learning-cycle
title: Experiential Learning Cycle
description: "A reusable sequence of bounded experience, prompted debrief, a stated and checked principle and a changed attempt with feedback, repeated across sessions with support fading, is expected to improve performance and near transfer where learners can interpret the experience; no claim tests the cycle as a whole, only its steps."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-05
sources:
  - id: kolb-1984
    title: "Kolb, D. A. (1984). *Experiential learning: Experience as the source of learning and development*. Prentice-Hall"
    author: "Kolb, D. A"
  - id: kolb-kolb-2005
    resource: "https://doi.org/10.5465/amle.2005.17268566"
    title: "Kolb, A. Y., & Kolb, D. A. (2005). Learning styles and learning spaces: Enhancing experiential learning in higher education. *Academy of Management Learning & Education, 4*(2), 193–212"
    author: "Kolb, A. Y., & Kolb, D. A"
  - id: bergsteiner-2010
    title: "Bergsteiner, H., Avery, G. C., & Neumann, R. (2010). Kolb's experiential learning model: Critique from a modelling perspective. *Studies in Continuing Education, 32*(1), 29–46"
    author: "Bergsteiner, H., Avery, G. C., & Neumann, R"
  - id: miettinen-2000
    title: "Miettinen, R. (2000). The concept of experiential learning and John Dewey's theory of reflective thought and action. *International Journal of Lifelong Education, 19*(1), 54–72"
    author: "Miettinen, R"
author: "Kolb (1984)"
grain_size: unit, course
---

# Experiential Learning Cycle

> **Pattern** · [All patterns](index.md)
> **Evidence** · 18 claims (8 for, 7 mixed, 3 against) · 36 studies (15 quant-synthesis, 11 causal, 6 review, 2 qualitative, 2 design), `q1`–`q4` · 13 of 36 report an effect size · 8 claims rest on one study

## Description and scope

A reusable sequence, repeated across a unit or course, that turns something learners do into a principle they can use again: **set a noticing focus → a bounded concrete experience in which outcomes can surprise the learner → a debrief straight after, with specific prompts (what did you expect, what happened, why the difference) → the learner states the rule or principle the experience illustrates, and the instructor corrects or completes it → a changed, structurally similar attempt with feedback → the result opens the next loop, with support reduced**. The intended change is in `skill-performance` on a new task, in `conceptual-understanding` (stating and using the principle) and in `near-transfer`. The four stages are Kolb's (concrete experience, reflective observation, abstract conceptualization, active experimentation); the order and the instructor's role in each are design choices, not established requirements.

**No claim in the wiki tests the experiential learning cycle as a whole**: a full loop, or a series of loops, against an alternative of matched time. The one claim that reports a cycle being used, an engineering module built on Kolb's four quadrants, states that the module was not formally assessed ([A four-quadrant experiential module was implemented without formal assessment](../claims/elt-fea-module-implemented-three-topics-unassessed.md) [~W]). What the wiki does test are parts of the sequence, each in its own population: specific reflection prompts beat generic ones; simulation with deliberate practice beats traditional clinical education on procedural skills; guided discovery beats unassisted discovery, and explicit instruction beats unassisted discovery; manipulation beats symbol-only instruction in mathematics and undergraduate physics. Those are read below as evidence for steps, never for the cycle.

**Where this page sits.** The [Experiential Learning principle](../principles/experiential-learning.md) owns the general relationship (an experience becomes learning when it is followed by structured reflection, connection to a concept and a further attempt with feedback; unguided experience for `novice` learners is the failure condition) and its evidence; this page is the reusable sequence built on it and does not restate that model. The [Reflection principle](../principles/reflection.md) owns the debrief step (prompting a learner to examine a completed performance against a criterion and name a change for the next attempt); read it when designing the prompts. [Cognitive Disequilibrium](../principles/cognitive-disequilibrium.md) owns the surprise that opens a loop. Question-driven experiences sit under [Inquiry-based Learning](../principles/inquiry-based-learning.md); designs that lead with expert modeling rather than learner experience are [Cognitive Apprenticeship](cognitive-apprenticeship.md).

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Before the first experience, a short probe of the target task: ask learners what they would do first and what they would watch for, and record what they say. Note whether they have done or seen a task like this before. Preserve unknowns rather than labeling learners `novice` or `advanced`. Do not record a Kolb learning-style score: matching to it is not a design input (below). |
| The capability and kind of goal | What learners should be able to do afterwards and in what situation: a `procedure` or psychomotor skill, a `concept`, a judgement in practice (clinical reasoning, teaching, facilitation), or an `attitude-motivation` goal. Name the principle the experience is meant to illustrate; if no one can name it, the experience is not yet designed. |
| The experience | What learners will do (lab, simulation, placement shift, field activity, lesson taught, case handled), how many things can vary in it, what could go wrong, and whether it can be run again in a changed form. |
| Context and activities | Setting (`classroom`, `workplace-clinical`, field, `online-self-paced`, `online-instructor-led`), `single-session` or `days-weeks`, number of loops available, group size, who can debrief and for how long, whether a second attempt is possible. |
| Learner-valued goal | Ask what the learner wants from the experience (to be trusted on placement, to pass the practical, to feel ready, to find out whether the field suits them). Record disagreement with the designer objective. |
| Designer objective | Which of these the assessment will weigh: performing the task unaided, stating and justifying the principle, applying it to a new case, or changed practice in the learner's own setting. |
| Outcome | A new, unaided task scored apart from the debrief or journal; a statement of the principle scored apart from performance; immediate or `delayed`; and whether it must hold in a different setting (`near-transfer`, `far-transfer`). Satisfaction, time spent doing and journals completed are participation, not outcomes. |

A request to "use Kolb's cycle for this unit" does not specify these. Ask what principle each experience is meant to teach, what learners can already do, who debriefs, and what new task will show the change, before choosing experiences or the number of loops.

## Sequence and conditional policy

The default sequence is the earlier page's, with dose and progression added. No claim tests the sequence or its order; each step's evidence status is stated beside it, and quantities are proposals to observe and revise.

1. **Probe and prepare (about 5–10 minutes).** Run the starting probe (inputs, above), state the noticing focus in one sentence ("watch what happens to the patient's oxygen saturation when you change the position"), and recall the previous loop's rule if there is one. If the probe shows learners cannot name the first move or what to watch, demonstrate it with a worked example before the experience, and narrow the experience so only one or two things can vary. Evidence status: [guided against unassisted discovery](../claims/guided-discovery-outperforms-pure-discovery.md) [~S], carried from discovery tasks with mostly school learners to experiences generally; [activating prior knowledge](../claims/activation-improves-learning.md) [~M] qualifies the recall step: activating prior topic knowledge did not improve primary pupils' comprehension in one experiment, so keep recall brief and tied to the focus. The noticing focus itself is untested.
2. **Concrete experience (proposal: 15–40 minutes in a lesson; one shift, scenario or field session on placement).** Learners do the task with minimal intervention so real outcomes, including mistakes, can occur, but within a scope where a mistake is safe. Evidence status: untested as a stage; a surprising outcome is what the [cognitive-conflict evidence](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M] relies on (science-education conceptual-change strategies), and that claim's own experiment found staged contradictions raised learning only when learners actually became confused.
3. **Debrief straight after (proposal: 10–20 minutes, never deferred to a later week).** Specific prompts, in writing first and then in discussion: what did you expect, what happened, where did they differ, why. "Reflect on the experience" is not a prompt. Evidence status: [structured reflection](../claims/reflective-practice-improves-outcomes-when-structured.md) [+M]: specific prompts beat generic ones in a first-year engineering course with the number of reflections held constant, and metacognitive-reflection prompts were the only content moderator to reach significance in a school writing-to-learn synthesis; neither debriefs an experience. How soon after the experience is untested.
4. **State the principle (proposal: 5–15 minutes).** Each learner writes the rule the experience illustrates in one or two sentences and links it to the course's formal term, or draws it as a concept map; the instructor then confirms, corrects or completes it before anyone acts on it. Evidence status: untested as a stage. [Constructing concept maps](../claims/concept-mapping-improves-learning.md) [~M] beat comparison conditions in a meta-analysis, but with learning time matched, mapping did no better than rereading and less well than retrieval practice; use a map where the principle has relational structure, and a short written rule otherwise.
5. **Changed attempt with feedback (proposal: in the same session where possible, otherwise at the start of the next).** Learners apply the stated rule to a new, structurally similar situation that differs in its surface, and get feedback on whether the rule held. For a `procedure`, repeat to a stated standard with feedback after each attempt and rising difficulty. Evidence status: [simulation with deliberate practice](../claims/simulation-based-education-with-deliberate-practice-improves-clinical-outcomes.md) [+M] beat traditional clinical education on procedural clinical skills in medical education; untested for judgement or interpersonal goals.
6. **Re-enter and fade across loops.** The changed attempt's result and the stated rule open the next loop. Proposal for a unit of four to six loops, one or two a week:
   - *Early loops (1–2):* demonstration before the experience; one or two variables free; instructor-written debrief prompts and a word bank for stating the principle; the instructor checks every learner's stated rule.
   - *Middle loops (3–4):* no demonstration unless the probe shows a gap; more variables free; learners choose two of a set of prompts; debrief in pairs against a written protocol; the instructor checks rules from a sample and every learner whose retry failed.
   - *Late loops (5–6):* ill-structured experiences closer to real practice; learners write their own debrief questions; the instructor reviews only the stated principles.
   - *Move on* to a less supported loop when a learner's stated rule is correct and their changed attempt meets the stated criterion unaided in two consecutive loops; stay at the same level, or add a demonstration, after a failed retry. These thresholds are untested proposals; the [contingent-scaffolding claim](../claims/contingent-scaffolding-improves-learning.md) [+M] is the nearest basis for adjusting support to the learner's last response, and has not been read against this sequence.

If time is short, cut the number of loops, not the stages within a loop: one complete loop (brief experience, prompted debrief, stated rule, one retry) before three that stop after the experience (untested; from the earlier page). If a step cannot be provided, keep the debrief and the second attempt, and shorten the experience.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Debrief narrates what happened and names no rule or next step | Repeat the "expected / happened / why" prompt in writing, privately; then ask directly for the principle in the course's terms. | If a rule appears in writing, the prompt or the public setting was the problem: keep written-first debriefs. If none appears, the learner may lack the concept: teach it, then rerun a shortened experience. Untested. |
| Correct rule stated, the same error on the changed attempt | A component probe of just that step, then a matched retry at the same load. | If the component is done correctly, the retry differed in more than intended or load was too high: narrow it. If not, the rule is held verbally but not yet proceduralized: add repeated practice to a standard. Untested. |
| A learner is busy throughout the experience but draws the wrong lesson | Ask what they watched for; check whether the experience as run could show the target relation. | If the relation was not visible, redesign the experience. If it was, demonstrate it and retry. Consistent with the guided-discovery claim; the branch is untested. |
| Performs well in simulation, poorly on placement | Compare the two tasks feature by feature; observe a second real attempt with a known stressor removed. | Add the missing features to the simulation, or add a supervised real attempt before independent practice. Untested. |
| Reports large personal growth, little change in observed practice | Observe a decision in a new case at a stated later point; compare self-report with a supervisor's or peer's record. | Treat the self-report as a statement of value, not of capability; keep the observed task as the outcome. Untested. |
| A few learners state the rule; others repeat it | Collect written rules before discussion; compare each learner's later changed attempt. | If those who repeated the rule fail the retry, keep private writing first and check rules individually. Untested. |

## Fitting the design to a situation

**The three facts that most change the decision:**

- **What learners already know about the task the experience is meant to teach.** A `novice` cannot tell which parts of an experience matter, so an unguided first loop is mostly noise; an experienced practitioner can interpret more of it unaided. If unstated, ask: have they done or seen a task like this before, and can they say what they would watch for?
- **The kind of goal.** A `procedure` gains from repeated attempts to a standard with feedback; a `concept` from manipulation linked to its formal representation; a judgement or `attitude-motivation` goal has only self-reported evidence here. If unstated, ask: what will the learner do differently afterwards, and how would we see it?
- **Who can debrief and whether there is a second attempt.** The steps that rest on claims (specific prompts, practice with feedback) both need someone or something to structure them; an experience with no debrief and no retry is not this pattern. If unstated, ask: who is with the learner straight afterwards, for how long, and can the task be tried again in a changed form?

| If the brief says… | Then change… | Basis |
|---|---|---|
| Learners are `novice` on the target task | Demonstrate the first loop's task with a worked example before the experience; let one or two variables vary; supply the debrief prompts and the vocabulary for stating the principle; check each learner's rule before the retry; keep this support for at least the first two loops. | [Guided against unassisted discovery](../claims/guided-discovery-outperforms-pure-discovery.md) [~S]; discovery tasks with mostly school learners and mixed domains, not placements or simulations; the meta-analysis does not break results down by prior knowledge |
| Learners are `advanced` or experienced practitioners | Skip the demonstration; make the first experience ill-structured; have learners write their own debrief questions from the first loop; keep the changed attempt with feedback. | Untested; the guided-discovery claim's narrative review argues the advantage of guidance recedes with prior knowledge, which no recorded study tests here |
| Learners are `child`ren (under 12) | Shorter loops (experience 10–15 minutes, debrief 5 minutes); concrete materials linked to the written or symbolic form in the same session; tell them what to try rather than only to explore; the teacher states the rule. | [Hands-on learning](../claims/hands-on-learning-improves-achievement.md) [+M] (mathematics manipulatives, kindergarten to college); [guided against unassisted discovery](../claims/guided-discovery-outperforms-pure-discovery.md) [~S] (third and fourth graders learning a procedure); loop lengths untested |
| `workplace-clinical`, a `procedure` or psychomotor skill | Run the experience as simulated practice repeated to a stated mastery standard, feedback after each attempt, rising difficulty, then a debrief; move to the real setting only when the standard is met. | [Simulation with deliberate practice](../claims/simulation-based-education-with-deliberate-practice-improves-clinical-outcomes.md) [+M]; medical education, procedural skills only |
| The goal is a science or mathematics `concept` | Make the experience a predict-then-manipulate task (physical or virtual), with a stated prediction before acting, and map the result onto the formula or diagram during the principle step; use a virtual lab when a physical one is not available. | [Physical experience](../claims/physical-experience-enhances-science-learning.md) [~M] (undergraduate physics; physical and virtual manipulation equally effective); [cognitive conflict](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M] (science-education conceptual-change strategies) |
| The goal is professional judgement or a disposition | Use cases or placements with structured debriefs; assess a decision on a new case observed later, not a journal; treat any self-reported gain as unconfirmed. | [Experiential learning benefits reported in human services education](../claims/experiential-learning-engagement-skills-ethical-reasoning.md) [+W], second-hand, no design or effect size; otherwise untested |
| `online-self-paced`, no facilitator | Replace the live debrief with three written prompts after each task and a model answer to compare against; offer an automatically scored changed task as the retry. | [Structured reflection](../claims/reflective-practice-improves-outcomes-when-structured.md) [+M] for written specific prompts (a classroom engineering course); untested online |
| `single-session` | One complete loop: a 15-minute experience, a 10-minute written debrief, a stated rule, one changed attempt; no second loop. | Untested; from the earlier page's compressed-timeframe guidance |
| Large cohort, one facilitator | Debrief in pairs or threes against a written protocol; spend facilitator time on checking stated principles, where a wrong rule is hardest for peers to catch. | Untested; [reflection in higher education](../claims/reflective-practice-evidence-mixed-in-professional-education.md) [~M] reports peer interaction as a moderator, direction not stated on the claim page |
| The program bundles the cycle with Kolb's Learning Style Inventory, or asks to start learners at their "preferred stage" | Drop the style diagnosis and the matching; run every learner through every stage. | [Learning-style matching](../claims/learning-styles-matching-does-not-improve-learning.md) [-S]; [Kolb styles unchanged over a year](../claims/kolb-learning-style-stable-over-one-year.md) [-W] and [no link to career choice](../claims/kolb-inventory-limited-validity-career-and-personality.md) [-W], both second-hand reports in one review |
| Credit attaches to reflection, or assessment is high-stakes | Assess the changed attempt and a new unaided task; do not grade journals for completion; score principle and performance separately. | Untested; from the earlier page's constraint that graded reflection becomes a compliance artifact |
| Learners are uncomfortable reflecting in public, or reflect in a second language | Written or recorded reflection, in the language they choose, before any group debrief; sentence starters for the prompts. | Untested; from the earlier page's personalization |

Seven rows rest on a claim (novices, children, clinical procedures, science and mathematics concepts, judgement and dispositions, online self-paced, learning styles), and each is carried beyond the population or design its claim reports, as its Basis cell says; the large-cohort row cites a claim only for a moderator without a direction. The rows for advanced learners, a single session, high stakes and language are untested proposals or the earlier page's guidance.

## Choosing configurations from evidence

- **Structure of the debrief.** [Reflective Practice Improves Outcomes When Structured](../claims/reflective-practice-improves-outcomes-when-structured.md) [+M]: a meta-analysis of 48 school-based writing-to-learn interventions found writing overall produced a small gain (d = 0.22), and prompts for metacognitive reflection were the only content-type moderator that reached significance (b = 0.48); a quasi-experiment in two sections of a first-year engineering course (N = 208) found specific prompts beat generic ones on exams, project score and two problem sets, with 52 reflections apiece in both groups and no effect size reported. Neither reflects on an experiential task. Carry it to "specific prompts after the experience are more likely to help than an open invitation", no further.
- **How much reflection to expect, and what it depends on.** [Reflection interventions in higher education](../claims/reflective-practice-evidence-mixed-in-professional-education.md) [~M]: a random-effects meta-analysis of 23 controlled studies (2,010 participants) found a medium positive pooled effect (g = 0.56) that varied with duration, peer interaction and the reflective activity used. The claim page says its slug's "mixed" is not shown by this synthesis. Marked `~` because the average hides the variation that the design choice is about; it does not say which configuration to pick. Abstract only.
- **The changed attempt, for procedures.** [Simulation Based Education With Deliberate Practice](../claims/simulation-based-education-with-deliberate-practice-improves-clinical-outcomes.md) [+M]: a meta-analysis of 14 studies, mostly randomized trials and pre/post comparisons, found simulation with deliberate practice (repetition with mastery standards and immediate feedback) beat traditional clinical education on clinical skill acquisition (d = 0.71). Procedural and psychomotor skills such as ACLS, laparoscopic and central-line procedures; one synthesis, abstract only. It supports a feedback-rich, repeated experience, not experience as such.
- **Guidance in the experience.** [Unassisted discovery produces less learning than explicit instruction, while discovery enhanced with guidance outperforms other instruction](../claims/guided-discovery-outperforms-pure-discovery.md) [~S]: across 580 comparisons explicit instruction beat unassisted discovery (d = 0.38 favoring explicit instruction), and across 360 comparisons discovery with feedback, worked examples, scaffolding or elicited explanations beat other instruction (d = 0.30); 112 third- and fourth-graders, `novice`s at the control-of-variables procedure, mastered it more often under direct instruction and did as well on a later transfer task; a narrative review names experiential teaching among the minimally guided forms it argues against. This is the boundary of the pattern: a loop with a probe, a focus, a debrief, a checked rule and feedback is a guided form; the same experience left without them is not.
- **The surprise that opens a loop.** [Conflict-based instruction improves science conceptual learning, though staged contradictions helped only learners who reported being confused, and no study isolates disequilibrium as the mechanism](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]: across 218 science-education studies, conceptual-change strategies produced a large improvement (g = 1.10), cognitive-conflict strategies as much as the whole set, with wide variation; in a laboratory experiment with 32 undergraduates, staged contradictions raised self-reported confusion and did not raise posttest scores on their own, and learners gained only in high-confusion cases, with no support given to resolve the conflict. A qualitative study of seven dyads found [peer conflicts produced conceptual change only for students prepared to reflect](../claims/peer-conflicts-conditional-on-reflection.md) [~W]. Carry these to: a surprising outcome gives the debrief something to work on, and the debrief and principle steps are what resolve it.
- **Doing with materials.** [Hands-on learning improves achievement](../claims/hands-on-learning-improves-achievement.md) [+M]: a meta-analysis of 55 studies (N = 7,237, kindergarten to college) found mathematics instruction with concrete manipulatives beat symbol-only instruction, with moderate-to-large effects on retention and small effects on problem solving, transfer and justification. [Physical Experience Enhances Science Learning](../claims/physical-experience-enhances-science-learning.md) [~M]: physical, virtual and combined manipulation were equally effective for undergraduate heat and temperature and all beat traditional instruction without experimentation. Both concern manipulation within instruction, not a full cycle.
- **What the cycle must not carry.** [Learning Styles Matching Does Not Improve Learning](../claims/learning-styles-matching-does-not-improve-learning.md) [-S]: a systematic review found no study meeting the crossover design needed to support matching instruction to style, and a randomized study with fifth-graders found no style-by-modality interaction. Two second-hand reports in one 1985 review add that Kolb's inventory showed [no significant change over a year of varied instruction](../claims/kolb-learning-style-stable-over-one-year.md) [-W] and [no association with medical career choice](../claims/kolb-inventory-limited-validity-career-and-personality.md) [-W]. The stages are a sequence for every learner, not a profile to match.

Do not rank this pattern against direct instruction, case-based learning or simulation alone from these claims: none compares a cycle with them, and none measures the time a loop costs. Do not read a fluent debrief, a completed journal or enthusiasm as the capability changed. A precise abstention names the missing comparison (repeated experience-debrief-principle-retry loops against matched-time instruction with the same practice, on a new unaided task at a stated horizon) and the local observation that would stand in for it: the changed attempt, scored, at the next loop.

## Further evidence, not yet read against this model
<!-- Claims this page cited before the 2026-10-05 rewrite which are not used as core evidence above, plus one found while converting. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap). None has been re-read for the sequence above, so treat them as candidates, not as part of it. -->
Claims this page cited before the 2026-10-05 rewrite and not used as core evidence above. Each says what it is and how far it bears on the pattern.

- [Active Learning Improves Exam Performance](../claims/active-learning-improves-exam-performance.md) [+S]: undergraduate STEM courses with active learning against traditional lecturing (0.47 SD on exams and concept inventories; gaps narrowed only under high-intensity active learning). Bears on the cycle only in the general sense that every stage after the experience asks learners to produce something; it does not test experiential designs.
- [Assessment for learning improves achievement](../claims/assessment-for-learning-improves-achievement.md) [+S]: K-12 formative assessment syntheses (d = .29 and about .20). Bears on the feedback in the changed attempt by analogy; school classroom formative assessment, not experiential loops.
- [Advance organizers aided learning in a 1980 meta-analysis, but activating prior topic knowledge did not improve primary pupils' text comprehension in one experiment](../claims/activation-improves-learning.md) [~M]: cited before as `[+M]` support for re-entering each loop with the previous rule; the claim has since been retitled to what its studies show, and it qualifies the preparation step rather than supporting it, so its marker here is `~`. Used in step 1 above.
- [Concept mapping improves learning over most comparison conditions by a moderate average amount, but not over time-matched retrieval practice](../claims/concept-mapping-improves-learning.md) [~M]: cited before as `[+M]` for the conceptualization artifact; the claim page records that mapping did no better than rereading with time matched. Used in step 4 above, with that qualification.
- [Contingent scaffolding improves learning more than fixed or absent support](../claims/contingent-scaffolding-improves-learning.md) [+M]: added here as the nearest basis for the fading thresholds in step 6; not cited by the earlier page and not read against this sequence.

## Illustrative design instance and observation record

*Invented illustration, not a tested course.* Second-year nursing students, adults with one prior placement, take a six-week unit on recognizing patient deterioration, one loop a week in a simulation suite with one facilitator for 24 students, followed by a ward placement. The table changed the default in three places: the goal is partly a `procedure` (structured observations and escalation), so each simulation runs to a stated standard with feedback after each attempt; the cohort is large, so debriefs run in threes against a written protocol and the facilitator reads every stated rule; and learners have some prior experience, so the demonstration is kept only for loop 1. Loop 1: a 5-minute probe ("what would you check first in a patient who says they feel strange?"), a demonstration, a 20-minute scenario with one deteriorating sign, a 15-minute written-then-group debrief, a written rule checked by the facilitator, and a changed scenario the same afternoon. By loop 5, scenarios have two competing signs, learners write their own debrief questions, and the facilitator reviews only the rules. A student says she wants to stop feeling panicked when a patient worsens; the designer's objective is correct, timely escalation. They agree to record both: her rating of how ready she feels, and her escalation decision on a new scenario at the end of the unit and on a supervised ward shift. The simulation claim covers procedural skills in medical education, not this population or a judgement of when to escalate; these are local choices to observe, not settled ones.

Record: **principle the loop targets → starting probe and response → experience as run (variables free, what happened, help given) → debrief prompts and the learner's written answers → rule stated, and the instructor's correction → changed attempt, its result against the criterion, and the feedback given → candidate interpretations (rule not yet held, held but not proceduralized, retry differed too much, setting-specific stress) and their basis → support level for the next loop → reobservation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record but must not fabricate missing inputs or assign numerical probabilities of competence without a calibrated model.

## Elements and limits

[Simulation](../elements/simulation.md), [debriefing](../elements/debriefing.md), [reflection](../elements/reflection.md), [articulation](../elements/articulation.md), [concept map](../elements/concept-map.md), [demonstration](../elements/demonstration.md), [coaching](../elements/coaching.md), [practice](../elements/practice.md), [feedback](../elements/feedback.md) and [scaffolding](../elements/scaffolding.md). Principles the pattern draws on: [Experiential Learning](../principles/experiential-learning.md), [Reflection](../principles/reflection.md), [Purposeful Reflection](../principles/purposeful-reflection.md), [Cognitive Disequilibrium](../principles/cognitive-disequilibrium.md), [Active Learning](../principles/active-learning.md), [Activation](../principles/activation.md), [Assessment for Learning](../principles/assessment-for-learning.md) and [Authentic Audiences and Purposes](../principles/authentic-audiences-purposes.md).

This pattern is scoped to repeated loops of experience, prompted debrief, stated principle and changed attempt, for a capability that can be shown on a new task. Well-defined procedures that need no discovery are usually faster taught by [direct instruction](direct-instruction.md) with practice; and the four stages are not established as a fixed order (Bergsteiner et al., 2010; Miettinen, 2000), so a design may begin from a principle and test it in experience. Whether repeated loops produce better performance or transfer than matched-time instruction with the same practice, for which learners, at what time cost and at what horizon, remains to be tested.

## Related Patterns
- [Cognitive Apprenticeship](cognitive-apprenticeship.md) — shares the reflection and articulation stages, but leads with expert modeling rather than learner experience
- [Problem-Based Learning](problem-based-learning.md) — an ill-structured problem plays the role of the concrete experience, with the same reliance on structured debrief to convert it into knowledge
- [Inquiry-Based Learning](inquiry-based-learning.md) — organizes the same experience → explanation movement around investigation and evidence
- [Guided Discovery Learning](guided-discovery-learning.md) — addresses the cycle's novice constraint by adding guidance to the experience stage
- [Four-Component Instructional Design](4cid-four-component-instructional-design.md) — supplies formal rules for sequencing whole-task experiences and fading support across loops
- [5E Learning Cycle](5e-learning-cycle.md) — a school-science cycle that builds an elicit, conflict and explain sequence into its engage and explain phases

## Examples

**Clinical placements with structured debrief:** A nursing student manages a patient scenario (experience), reviews a recording against a debrief protocol (reflection), states the clinical rule the case illustrates (conceptualization), and applies it in the next shift or simulation (experimentation).

**Outdoor and adventure education:** The field where the cycle is most explicitly institutionalized — an activity is followed by a facilitated debrief whose stated purpose is to extract a transferable principle rather than to recount the activity.

**Engineering and science labs run as cycles rather than recipes:** Students predict, run the experiment, confront the discrepancy between prediction and result, formalize the underlying principle, then design a follow-up test — as opposed to confirmatory labs, which stop after the experience.

**Teacher preparation practica:** Teach a lesson, review it with a mentor against specific observation prompts, name the pedagogical principle involved, and redesign the next lesson to test it.
- [Close the feedback cycle with guided reflection on what was learned (post-noticing stage)](../strategies/post-noticing-reflection-guides.md)

## Key Sources
- Kolb, D. A. (1984). *Experiential learning: Experience as the source of learning and development*. Prentice-Hall.
- Kolb, A. Y., & Kolb, D. A. (2005). Learning styles and learning spaces: Enhancing experiential learning in higher education. *Academy of Management Learning & Education, 4*(2), 193–212. [doi:10.5465/amle.2005.17268566](https://doi.org/10.5465/amle.2005.17268566)
- Bergsteiner, H., Avery, G. C., & Neumann, R. (2010). Kolb's experiential learning model: Critique from a modelling perspective. *Studies in Continuing Education, 32*(1), 29–46.
- Miettinen, R. (2000). The concept of experiential learning and John Dewey's theory of reflective thought and action. *International Journal of Lifelong Education, 19*(1), 54–72.

<!-- deprecated 2026-10-05: superseded by the conditional model above. The previous body, kept verbatim.

## Description
The experiential learning cycle organizes instruction as a repeating four-stage loop: a **concrete experience**, **reflective observation** on what happened, **abstract conceptualization** that names the principle behind it, and **active experimentation** that puts the principle back to work in a new situation. Kolb's formulation frames learning as "the process whereby knowledge is created through the transformation of experience" — experience alone is the raw material, and the remaining three stages are what convert it into knowledge that transfers. The pattern exists because doing something does not reliably teach anything: without a structured route from event to principle, learners generalize from surface features, keep tacit hunches tacit, or draw the wrong lesson entirely.

## Implications

The cycle's design value is that it makes reflection a scheduled, non-optional stage rather than something learners are trusted to do on their own. A concrete experience that surprises the learner creates the conceptual gap that motivates revision [Cognitive disequilibrium motivates conceptual change](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]; the reflective and conceptualizing stages are what let that gap resolve into an articulated rule instead of a vague impression. Structured reflection of this kind does improve outcomes, but the qualifier matters: the benefit is tied to the structure, not to reflection as a disposition [Reflective Practice Improves Outcomes When Structured](../claims/reflective-practice-improves-outcomes-when-structured.md) [+M]. Because each loop begins by drawing on what the learner already brings to the experience, the cycle also enacts activation of prior knowledge [Advance organizers aided learning in a 1980 meta-analysis, but activating prior topic knowledge did not improve primary pupils' text comprehension in one experiment](../claims/activation-improves-learning.md) [+M], and its experimentation stage keeps learners generating rather than receiving [Active Learning Improves Exam Performance](../claims/active-learning-improves-exam-performance.md) [+S].

### Context
#### Requirements
- An experience with enough friction to be worth reflecting on — a simulation, fieldwork, lab, clinical placement, or authentic task where outcomes can genuinely surprise the learner ([Simulation](../elements/simulation.md))
- Protected time for reflection and debriefing, scheduled as part of the design rather than left to spare capacity ([Debriefing](../elements/debriefing.md))
- A facilitator able to push reflection past "how did that feel" toward the abstraction the experience supports ([Coaching](../elements/coaching.md))
- A second, non-identical situation in which to test the abstraction — a cycle that stops after conceptualization never checks whether the principle holds ([Practice](../elements/practice.md))

#### Constraints
- Where reflection is unstructured, unprompted, or graded as a compliance artifact, the evidence base becomes noticeably weaker and less consistent [Reflection interventions in higher education have a medium positive average effect on learning that varies with duration, peer interaction and the reflective activity used](../claims/reflective-practice-evidence-mixed-in-professional-education.md) [~M]
- The cycle is often taught alongside Kolb's Learning Style Inventory and the practice of assigning learners a preferred stage; matching instruction to a diagnosed style has no learning benefit and should not be treated as part of the pattern [Learning Styles Matching Does Not Improve Learning](../claims/learning-styles-matching-does-not-improve-learning.md) [-S]
- For genuine novices, an unsupported concrete experience imposes heavy extraneous load: with no schema to organize what they are seeing, learners spend the experience coping rather than noticing, and arrive at reflection with nothing to reflect on. Front-load worked examples or demonstration before the first loop ([Demonstration](../elements/demonstration.md))
- The model has been criticized as an oversimplified account of Dewey's reflective thought — the four stages are not empirically established as a fixed sequence, and treating the order as mandatory can force artificial staging onto activities that do not work that way (Bergsteiner et al., 2010; Miettinen, 2000)
- Time cost is high relative to direct instruction for well-defined procedural content, where a full loop buys little

#### Grain Size
Unit or course. A single loop can fit inside one lesson (a lab followed by a structured debrief), but the pattern's value comes from repetition — successive loops across a unit, practicum, or co-op, each entering the cycle with the previous loop's abstraction as prior knowledge.

### Target Goals
- Transfer of principles from a specific experience to structurally similar new situations
- Conceptual change in domains where learners arrive with durable intuitive misconceptions [Cognitive disequilibrium motivates conceptual change](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]
- Professional judgment that cannot be fully specified as rules — clinical reasoning, teaching, facilitation, design
- Metacognitive habits: noticing one's own reasoning during an activity and revising it deliberately

### Target Learners
- Learners with enough domain grounding to interpret the experience — professional-formation contexts (residents, student teachers, trainees, interns) are the canonical fit
- Adult learners bringing substantial prior experience the cycle can draw on [Advance organizers aided learning in a 1980 meta-analysis, but activating prior topic knowledge did not improve primary pupils' text comprehension in one experiment](../claims/activation-improves-learning.md) [+M]
- Weakest fit for complete novices in a domain, who need modeling and scaffolding before a bare experience becomes informative

### Theory
#### Supporting
- [Constructivism](../theories/constructivism.md) — learners build knowledge by acting on the world and reconciling the results with existing schemas, which is precisely the experience → reflection → conceptualization movement
- [Situated Learning](../theories/situated-learning.md) — grounding the cycle in authentic practice keeps the abstraction tied to the conditions under which it applies
- [Self-Regulated Learning](../theories/self-regulated-learning.md) — the reflective observation stage is an externally scaffolded version of the monitoring learners must eventually do unaided

#### Contradicting / Qualifying
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) — an unguided concrete experience is a minimally guided condition; for novices it can consume working memory without producing schema, arguing for demonstration and scaffolding before the first loop

### Claims
#### Supporting
- [Reflective Practice Improves Outcomes When Structured](../claims/reflective-practice-improves-outcomes-when-structured.md) [+M] — the reflective observation stage carries the pattern, and structure is what makes it work
- [Active Learning Improves Exam Performance](../claims/active-learning-improves-exam-performance.md) [+S] — active experimentation keeps learners generating rather than receiving
- [Advance organizers aided learning in a 1980 meta-analysis, but activating prior topic knowledge did not improve primary pupils' text comprehension in one experiment](../claims/activation-improves-learning.md) [+M] — each loop re-enters with the prior loop's abstraction as activated prior knowledge
- [Cognitive disequilibrium motivates conceptual change](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M] — a surprising concrete experience supplies the disequilibrium the cycle then resolves
- [Concept mapping improves learning](../claims/concept-mapping-improves-learning.md) [+M] — concept maps are a practical artifact for the abstract conceptualization stage
- [Assessment for learning improves achievement](../claims/assessment-for-learning-improves-achievement.md) [+S] — feedback during the experimentation stage is what tells learners whether the abstraction held

#### Contradicting
- [Learning Styles Matching Does Not Improve Learning](../claims/learning-styles-matching-does-not-improve-learning.md) [-S] — the Learning Style Inventory commonly bundled with the cycle does not support the instructional adaptations it is used to justify
- [Reflection interventions in higher education have a medium positive average effect on learning that varies with duration, peer interaction and the reflective activity used](../claims/reflective-practice-evidence-mixed-in-professional-education.md) [~M] — unstructured reflection is where the pattern most often fails in practice

## Design

### Sequence
1. **Prepare** — Activate prior experience and set a noticing focus, so learners enter the experience with something to attend to rather than everything at once ([Activation](../principles/activation.md))
2. **Concrete experience** — Learners do the thing: run the lab, see the patient, teach the lesson, operate the [simulation](../elements/simulation.md). Instructor intervention is minimal so that real outcomes, including failures, occur
3. **Reflective observation** — Structured debrief immediately after: what happened, what was expected, where the two diverged ([Debriefing](../elements/debriefing.md), [Reflection](../elements/reflection.md)). Prompts are specific; "reflect on the experience" is not a prompt
4. **Abstract conceptualization** — Learners name the principle the experience illustrates and connect it to the formal content of the course, producing a durable artifact — a rule, a [concept map](../claims/concept-mapping-improves-learning.md), a written account ([Articulation](../elements/articulation.md))
5. **Active experimentation** — Learners apply the stated principle in a new, structurally similar situation and get [feedback](../elements/feedback.md) on whether it held ([Practice](../elements/practice.md))
6. **Re-enter** — The result of experimentation becomes the next loop's concrete experience; scaffolding fades across successive loops ([Scaffolding](../elements/scaffolding.md))

### Affordances
- [Purposeful Reflection](../principles/purposeful-reflection.md) — the pattern's core contribution is making reflection a scheduled stage with its own prompts and artifacts, rather than a hoped-for by-product of doing
- [Experiential Learning](../principles/experiential-learning.md) — supplies the concrete sequence that turns "learn by doing" from a slogan into a design with a defined route from event to transferable principle
- [Active Learning](../principles/active-learning.md) — every stage but the first requires learners to produce something: an observation, an abstraction, a test
- [Activation](../principles/activation.md) — each loop deliberately re-enters with the previous loop's conclusion as prior knowledge
- [Assessment for Learning](../principles/assessment-for-learning.md) — the experimentation stage is a low-stakes test of the learner's own abstraction, with feedback aimed at revision rather than grading
- [Authentic Audiences and Purposes](../principles/authentic-audiences-purposes.md) — the experience stage works best when the task has real consequences, which is what makes surprise possible

### Personalization

**Complete novices in the domain:** Precede the first concrete experience with [demonstration](../elements/demonstration.md) and a narrated example, and narrow the experience so only one variable can vary. Supply the reflection prompts and much of the vocabulary for the conceptualization stage.

**Learners with substantial prior experience:** Shorten the preparation stage and increase the ill-structuredness of the experience. Shift responsibility for generating reflection questions to the learners themselves.

**Large cohorts with limited facilitator time:** Run reflective observation as structured peer debriefs against a shared protocol, reserving facilitator attention for the conceptualization stage, where mis-abstraction is most costly and hardest for peers to catch.

**Learners uncomfortable with public reflection:** Offer written or recorded reflection before any group debrief, so the reflective stage does not become a performance for the confident.

**Compressed timeframes:** Cut the number of loops rather than the stages within a loop — a single complete cycle teaches more than three truncated ones that stop after the experience.

## Related Patterns
- [Cognitive Apprenticeship](cognitive-apprenticeship.md) — shares the reflection and articulation stages, but leads with expert modeling rather than learner experience
- [Problem-Based Learning](problem-based-learning.md) — an ill-structured problem plays the role of the concrete experience, with the same reliance on structured debrief to convert it into knowledge
- [Inquiry-Based Learning](inquiry-based-learning.md) — organizes the same experience → explanation movement around investigation and evidence
- [Guided Discovery Learning](guided-discovery-learning.md) — addresses the cycle's novice constraint by adding guidance to the experience stage
- [Four-Component Instructional Design](4cid-four-component-instructional-design.md) — supplies formal rules for sequencing whole-task experiences and fading support across loops

## Examples

**Clinical placements with structured debrief:** A nursing student manages a patient scenario (experience), reviews a recording against a debrief protocol (reflection), states the clinical rule the case illustrates (conceptualization), and applies it in the next shift or simulation (experimentation).

**Outdoor and adventure education:** The field where the cycle is most explicitly institutionalized — an activity is followed by a facilitated debrief whose stated purpose is to extract a transferable principle rather than to recount the activity.

**Engineering and science labs run as cycles rather than recipes:** Students predict, run the experiment, confront the discrepancy between prediction and result, formalize the underlying principle, then design a follow-up test — as opposed to confirmatory labs, which stop after the experience.

**Teacher preparation practica:** Teach a lesson, review it with a mentor against specific observation prompts, name the pedagogical principle involved, and redesign the next lesson to test it.
- [Close the feedback cycle with guided reflection on what was learned (post-noticing stage)](../strategies/post-noticing-reflection-guides.md)

## Key Sources
- Kolb, D. A. (1984). *Experiential learning: Experience as the source of learning and development*. Prentice-Hall.
- Kolb, A. Y., & Kolb, D. A. (2005). Learning styles and learning spaces: Enhancing experiential learning in higher education. *Academy of Management Learning & Education, 4*(2), 193–212. [doi:10.5465/amle.2005.17268566](https://doi.org/10.5465/amle.2005.17268566)
- Bergsteiner, H., Avery, G. C., & Neumann, R. (2010). Kolb's experiential learning model: Critique from a modelling perspective. *Studies in Continuing Education, 32*(1), 29–46.
- Miettinen, R. (2000). The concept of experiential learning and John Dewey's theory of reflective thought and action. *International Journal of Lifelong Education, 19*(1), 54–72.
-->
