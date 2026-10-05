---
type: pattern
id: gagnes-9-events-of-instruction
aliases: [gagnés-9-events, gagnés-9-events-of-instruction]
title: "Gagné's 9 Events of Instruction"
description: "A reusable lesson policy that moves a learner from an observed starting response through presentation, guided and independent performance with feedback, to a check at a stated horizon, keeping or dropping each event according to what the learner's responses show rather than running all nine by rote."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-02
author: Robert Gagné
grain_size: lesson
---

# Gagné's 9 Events of Instruction

> **Pattern** · [All patterns](index.md)
> **Evidence** · 9 claims (1 for, 8 mixed) · 14 studies (4 causal, 3 quant-synthesis, 3 review, 2 theoretical, 1 associational, 1 qualitative), `q2`–`q4` · 1 of 14 report an effect size · 6 claims rest on one study

## Description and scope

A reusable policy for one bounded lesson on a structured target (a `concept`, `procedure` or rule with a defined correct performance): direct attention, say what the learner will be able to do, surface relevant prior knowledge, present the content, guide the first attempts, elicit performance, give feedback, check performance, and set up retention and transfer. It instantiates the [Direct Instruction principle](../principles/direct-instruction.md): explicit explanation, modelling and guided practice with checks for a learner whose response shows no working method for the target. Two other converted principles govern single events inside it: [Activation](../principles/activation.md) for event 3 (stimulate recall) and [Retrieval Practice](../principles/retrieval-practice.md) for events 6 and 9 when the target includes later recall. The [Direct Instruction pattern](../patterns/direct-instruction.md) is a sibling policy built on the same principle; this page is the general nine-event lesson architecture, and treats each event as a candidate rather than a requirement.

The nine-event sequence itself is a design framework, not a tested intervention. **No claim in this wiki tests the full nine-event lesson against a different lesson design.** The nearest test is one experiment in which events were removed one at a time from a computer-based lesson (below): it found that removing practice lowered the posttest and removing objectives, examples or review individually did not. The study configurations below are evidence; the response-dependent policy on this page is an **untested design proposal**, and the default sequence keeps the earlier page's nine steps, each labelled with what supports it.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | A first attempt at a representative task before instruction, with the reasoning given, the help used and the time taken. Record task-specific `expertise` as observed (`novice`, `intermediate`, `advanced`, or unknown), age band and setting. Preserve unknowns; experience in the wider subject does not settle readiness for this task. |
| Target and outcome | The capability the lesson is for and a representative task that shows it; which aids are permitted; the instrument, the locally chosen criterion and the horizon (`immediate-performance`, `delayed-retention`, `near-transfer`, `far-transfer`). Events 8 and 9 cannot be designed until this is stated. |
| Knowledge type and task structure | Whether the target is a structured `concept` or `procedure`, or a `complex-skill` that has to be practised as a whole; whether the aim is open inquiry, in which case this pattern is likely the wrong frame. |
| Context and time | Lesson length, delivery (`classroom`, `online-self-paced`, `online-instructor-led`), who can give feedback and how fast, and which events earlier or later lessons already carry (a review elsewhere, a later transfer task). |
| Learner-valued goal | Ask what the learner wants from the lesson and why. Record disagreement with the designer objective; negotiate rather than assume agreement. |
| Designer objective | What the lesson is meant to change and how it will be judged; whether the objective will be stated to the learner, and in what words. |

A request for "a lesson using Gagné's events" does not specify these inputs. Ask for the target, the starting response and the horizon before deciding which events to elaborate, merge or omit.

## Sequence and conditional policy

The default sequence keeps the earlier page's nine events; the label after each says what the evidence on this page bears on it.

1. **Gain attention.** Open with a problem, case or question tied to the target. *Untested here; from the earlier page.*
2. **State objectives.** Say what the learner will be able to do and how it will be checked. *Removing objectives alone did not lower the posttest in the one experiment recorded ([single-event removal](../claims/single-event-removal-no-achievement-effect.md) [~M]); keep it short and decide by whether learners need it to direct their own work.*
3. **Stimulate recall of prior knowledge.** Ask for the relevant idea in a form the next instruction will use. *Governed by the [Activation principle](../principles/activation.md), whose evidence is split; activation alone has often shown little effect.*
4. **Present new content.** Explain and model the target, with examples. *Supported for learners who cannot yet start ([Direct Instruction principle](../principles/direct-instruction.md)); removing examples alone did not lower the posttest in the one experiment ([single-event removal](../claims/single-event-removal-no-achievement-effect.md) [~M]).*
5. **Provide learning guidance.** Prompts, cues or a partly worked attempt while the learner works. *Supported for learners without a working method; may become redundant as task expertise grows ([expertise reversal](../claims/expertise-reversal-effect.md) [~M]).*
6. **Elicit performance.** The learner attempts representative tasks. *The one event whose removal lowered the posttest ([practice present](../claims/practice-presence-raises-cbi-posttest-achievement.md) [+M]).*
7. **Provide feedback.** Say what was right, what was not and what to do next. *The practice versions in that experiment are titled "practice with feedback", so practice and feedback were not separated; see [Formative Assessment](../principles/formative-assessment.md).*
8. **Assess performance.** An unaided task matched to the target, under the agreed aids. *A check, not a treatment: the evidence here does not test it as an event.*
9. **Enhance retention and transfer.** Later retrieval, a changed problem, or use in a fuller task. *Untested as an event here. Removing a review alone did not lower the posttest ([single-event removal](../claims/single-event-removal-no-achievement-effect.md) [~M]), but that posttest's horizon is not reported, so it says nothing about delayed retention. For a complex skill, a design argument favours whole-task practice over a part-by-part sequence ([whole-task practice](../claims/whole-task-performance-improves-transfer.md) [~M]).*

Between events, choose the next activity provisionally from what the learner does:

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Cannot begin the representative task before instruction | Ask for a first step on the same relation in a familiar and in a changed representation, with an accessible response mode, recording any hint. | If reasoning is absent, run events 4–5 in full. If only recognition or access fails, change the representation or the response mode first. Neither branch is a validated diagnosis. |
| Already performs the target unaided at the start | A changed problem and a request to say why each step is licensed. | Shorten or skip events 4–5 and move to performance, feedback and transfer; full presentation may be redundant for this learner on this task. One success does not establish the threshold. |
| Succeeds during guided practice, fails the unaided check (event 8) | A matched item with the model removed but the prompt kept, then one with both removed. | Fade guidance in steps and add practice with feedback before the check is repeated; do not repeat the whole presentation by default. |
| Unaided success at the end of the lesson, weaker on a later or changed task | Re-test with a new item at the delay; record what practice and exposure happened in between. | Add spaced retrieval or a transfer task as event 9 in a later session rather than lengthening this lesson. Whether a review event would have prevented the drop is untested. |
| Says the lesson's aims were clear, but cannot state what they were or use them | Ask the learner to state the target in their own words and to judge a worked attempt against it. | Treat attitude ratings as a separate outcome from learning: in the one experiment, the group with no objectives rated goal clarity highest. Revise the objective's wording or drop it, and judge by performance. |

These rows are proposals for local observation, untested with learners. A probe is itself a learning exposure, and one contrast does not identify a cause.

## Choosing configurations from evidence

- **Keep the performance event.** In an experiment with 256 undergraduate computer-literacy students, randomly assigned within pretest blocks to six versions of a computer-based lesson (`randomized`, `adult`, `postsecondary`), the four versions that included practice scored significantly higher on the posttest than the two without ([practice present](../claims/practice-presence-raises-cbi-posttest-achievement.md) [+M]). The claim page prints the omnibus F and group means (above 17 against below 15) but no standardised effect size, and does not report the posttest's horizon, what the feedback consisted of, or the lesson's length. One study, not yet checked against its source. It supports keeping practice; it does not say how much, or test the order of events.
- **Do not read single-event removal as permission to drop everything else.** In the same experiment, versions without objectives, without examples or without review scored 17.16 to 17.36 against the full program's 17.61, a non-significant difference ([single-event removal](../claims/single-event-removal-no-achievement-effect.md) [~M]). The claim page says equivalence was not formally tested, so this is a failure to detect a difference, not evidence that those events do nothing. It concerns one well-designed lesson with the other events present, a horizon the claim page does not report, and one population. Not yet checked against its source.
- **Learners' ratings do not track which events they received.** In the same study, the group with no objectives gave the highest ratings on the goal-clarity items, though not significantly higher than most groups ([no-objectives attitudes](../claims/no-objectives-group-most-positive-attitudes.md) [~M]), while groups without practice or without examples rated those items lower ([missing practice and examples noticed](../claims/students-notice-missing-practice-and-examples.md) [~M]). So learner satisfaction is a separate outcome (`attitude-motivation`), and a positive rating of the lesson is not a check that an event did its job. Both not yet checked against their source.
- **Fade guidance as the learner's task-specific competence grows.** A review of cognitive-load studies argues that integrated explanations, worked examples and step-by-step guidance help novices by reducing search and can become redundant or depress performance for more knowledgeable learners ([expertise reversal](../claims/expertise-reversal-effect.md) [~M]). Read from an abstract, no effect sizes recorded, not settled against its source. It qualifies events 4–5 for advanced learners; it does not say when to fade or how to measure the point.
- **For a complex skill, prefer whole tasks to a part-by-part pass.** A design argument, not an experiment, holds that load-reducing methods suited to practising complex tasks to retention (low variability, complete guidance and feedback) can hinder transfer, and proposes high variability and limited guidance with simpler whole tasks early for novices ([whole-task practice](../claims/whole-task-performance-improves-transfer.md) [~M]). It qualifies a single linear pass through the nine events for a `complex-skill` target with a transfer goal; it is not evidence of an effect.

Unguided discovery against explicit instruction, which bears on events 4–5 for novices, is read on the [Direct Instruction principle](../principles/direct-instruction.md) and not repeated here. None of these entries tests the nine events as a sequence, their order, or event 1 or 9 as such. A precise abstention names the missing comparison, target or observation and the next way to resolve it.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-02 (maintainer's decision): claims this page cited before the 2026-10-02 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [~S] — not settled: the text available could not confirm the entries (abstract)
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M] — not settled: the text available could not confirm the entries (abstract)
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M] — not settled: the text available could not confirm the entries (abstract)

## Illustrative design instance and observation record

*Invented illustration, not a tested lesson.* A 40-minute online module teaches adult warehouse staff to read a stock-rotation label and decide which pallet ships first. Before any instruction, each learner is shown two labels and asked which ships first and why. Most choose by the larger date number; two already apply the rule and are routed to three changed labels and the transfer task. For the rest, the module states the target ("choose the pallet to ship from any two labels"), asks what "best before" means to them, explains and models the rule on three labels, gives four guided items with a hint available, then four unaided items with immediate feedback, then a mixed check. One learner says he wants to stop being corrected by his supervisor; the designer's objective is zero rotation errors on the floor. A week later, a short set of new labels is sent to the same learners. These are local design choices; the evidence above does not establish their optimality.

Record: **target and permitted aids → starting attempt and reasoning → which events were run, merged or skipped, and why → help used during guided items → unaided responses and feedback given → check result → candidate interpretations (rule learned, date heuristic still in use, label format unfamiliar) and their basis → next observation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record but must not fabricate missing inputs or assign numerical probabilities of mastery without a calibrated model.

## Elements and limits

[Attention](../elements/attention.md), [learning objectives](../elements/learning-objectives.md), [prior knowledge activation](../elements/prior-knowledge-activation.md) and [activation](../elements/activation.md), [demonstration](../elements/demonstration.md), [guided practice](../elements/guided-practice.md), [practice](../elements/practice.md), [provide feedback](../elements/provide-feedback.md), [assessment](../elements/assessment.md) and [transfer tasks](../elements/transfer-tasks.md). Principles the policy draws on: [Direct Instruction](../principles/direct-instruction.md), [Activation](../principles/activation.md), [Retrieval Practice](../principles/retrieval-practice.md) and [Formative Assessment](../principles/formative-assessment.md).

This pattern is scoped to a bounded lesson on a structured target. Open inquiry, design work, and complex skills that have to be practised as whole tasks need other configurations (see [Merrill's First Principles of Instruction](merrills-first-principles-of-instruction.md) for a task-centred alternative). The policy supports observation and design reasoning; the effect of the full sequence, of event order, and of any single event other than practice remains to be tested with learners.

## Related Patterns
- [Develop Understanding](develop-understanding.md)
- [Merrill's First Principles of Instruction](merrills-first-principles-of-instruction.md)

## Examples
- A short online lesson that activates prior knowledge, teaches a new concept, and checks application with feedback.
- Instructor-led technical training that sequences demonstration, practice, feedback, and transfer tasks.

## Key Sources
- Gagne, R. M. (1985). *The conditions of learning* (4th ed.). Holt, Rinehart and Winston.
- Gagne, R. M., Wager, W. W., Golas, K. C., & Keller, J. M. (2005). *Principles of instructional design* (5th ed.). Wadsworth.

<!-- deprecated 2026-10-02: superseded by the conditional model above; the body it replaced, kept verbatim.

## Description
Gagné's 9 Events of Instruction is a structured lesson pattern that sequences attention, objectives, recall, presentation, guidance, practice, feedback, assessment, and transfer. It is a classic design for lessons where the instructor wants to move learners through a complete learning cycle with explicit support at each stage. The pattern is especially useful when content needs to be introduced clearly and practiced systematically within a bounded instructional sequence.

Its strength is coherence: each event sets up the next. Its limitation is rigidity. Not every domain or lesson benefits from a fully linear sequence, especially when inquiry, design, or open-ended exploration are the primary aims.

## Implications

### Context
#### Requirements
- **Clear learning objectives**: The pattern assumes the lesson has defined outcomes.
- **Time for the full cycle**: Attention, practice, feedback, and transfer all need deliberate space.
- **Instructional materials for each stage**: Designers need prompts, examples, practice, and assessment aligned to the lesson goal.
- **A teacher or system that can provide feedback**: The pattern loses force if performance and feedback are weak.
#### Constraints
- **Prescriptive feel**: The sequence can become mechanical if applied without judgment.
- **Weak fit for open inquiry**: Highly exploratory learning may need more flexible sequencing.
- **Front-loading risk**: Too much explanation before performance can reduce active processing.
- **Transfer stage often gets dropped**: Many implementations stop at assessment instead of helping learners generalize.
#### Grain Size
- Lesson

### Target Goals
- **Structured concept and skill learning**: Useful for lessons that need clear sequencing.
- **Retention and transfer**: The full pattern aims to move beyond exposure into later use.
- **Aligned practice and feedback**: Keeping performance and correction central to instruction.

### Target Learners
- **Learners in formal instructional settings**: Strong fit for classroom, online module, and corporate lesson design.
- **Novices needing clear structure**: Helpful when learners benefit from explicit sequencing and guidance.
- **Designers building reusable lesson templates**: The pattern provides a stable instructional scaffold.

### Theory
#### Supporting
- Information-processing traditions — different phases of instruction support different learning processes.
- Guided instruction traditions — learners often benefit from explicit sequencing, practice, and feedback.
- Transfer-oriented design — retention is stronger when instruction includes recall and application stages.
#### Contradicting / Qualifying
- The pattern should be adapted, not followed ritualistically.
- More complex or inquiry-heavy learning may need nonlinear returns across the events rather than one pass through them.

### Claims
#### Supporting
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [~S]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M]
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M]
#### Contradicting
- [Whole-task performance improves transfer of complex skills to real-world settings.](../claims/whole-task-performance-improves-transfer.md) [~S]

## Design

### Sequence
1. Gain attention.
2. State objectives.
3. Stimulate recall of prior knowledge.
4. Present new content.
5. Provide learning guidance.
6. Elicit performance.
7. Provide feedback.
8. Assess performance.
9. Enhance retention and transfer.

### Elements Used
- [Activation](../elements/activation.md)
- [Practice](../elements/practice.md)
- [Provide Feedback](../elements/provide-feedback.md)
- [Assessment](../elements/assessment.md)

### Affordances
- [Guided Practice](../principles/guided-practice.md)
- [Immediate Feedback](../principles/immediate-feedback.md)
- [Formative Assessment](../principles/formative-assessment.md)
- [Multiple Methods of Assessment](../principles/multiple-methods-of-assessment.md)

### Personalization
- Individual events can be emphasized differently depending on learner readiness.
- Digital modules can adapt pacing or feedback inside the overall sequence.
- Instructors can shorten or merge events when the lesson does not require full elaboration.

## Impact
- Provides a reliable lesson architecture for explicit, structured instruction.
- Strongest when the final transfer stage is treated as essential rather than optional.
-->
