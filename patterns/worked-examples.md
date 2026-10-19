---
type: pattern
id: worked-examples
title: Worked Examples
description: "A reusable example-first policy for a structured task, qualified by task-specific knowledge, representation and intended outcome."
canonical: true
status: review
generated:
  by: codex/unspecified
  at: 2026-09-30
grain_size: lesson
---

# Worked Examples

> **Pattern** · [All patterns](index.md)
> **Evidence** · 18 claims (6 for, 7 mixed, 2 against, 3 unmarked) · 14 studies (8 causal, 3 review, 2 theoretical, 1 design), `q2`–`q3` · 0 of 14 report an effect size · 16 claims rest on one study

## Description and scope

A reusable policy for selecting and adapting correct solution models on structured tasks. It instantiates the [conditional principle](../principles/worked-examples.md). The study configurations below are evidence; the response-dependent policy is an **untested design proposal**. Use it to gather better evidence, not to certify a latent learner state.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Task-specific experience; an independent response and reasoning; errors, confidence and uncertainty. Preserve unknowns. |
| Context and activities | Representation, language/access conditions, available time, tools, prompts, earlier exposures and exact help. |
| Learner-valued goal | Ask what the learner wants and why. Record disagreement with the designer objective; negotiate rather than assume agreement. |
| Designer objective | Intended capability and representative task; identify what must be independent and which aids are permitted. |
| Outcome | Scoring instrument, locally chosen criterion, immediate/delayed horizon, and any distinct use or safety outcome. |

A request for “better learning” does not specify these inputs. Ask for them before prescribing dose, a fading threshold or a predicted gain. Check the solution and scoring key for correctness and alignment first. Incorrect-example learning is a different configuration with its own evidence; accurate copying of an error is not readiness.

## Sequence and conditional policy

1. **Elicit briefly.** Ask for a first decision and justification without showing the worked answer. Avoid turning a diagnostic attempt into a long unguided treatment. Record its learning exposure.
2. **Select a bounded candidate.** If task-specific reasoning is weak and the task is structured, consider a correct example with visible decision rationale. If varied independent performance is already available, consider independent work or targeted help; the novice contrast does not require a full example for every learner.
3. **Observe the process.** Ask which relation licenses a step or how a relevant condition would change it. A completion problem removes steps inside a solution; an example→problem pair presents a separate complete problem. Record which was actually delivered.
4. **Choose the next activity provisionally.** Use the table below. Repeat matched probes where feasible; task, representation, assistance and practice history can confound their interpretation.
5. **Reobserve.** Use a new representative task under the agreed aids, rubric and horizon. Retain unresolved explanations. If the response disagrees with the expectation, revise the interpretation or configuration.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Cannot start independently | Compare first-step reasoning in matched familiar and changed representations; permit an accessible response mode without supplying the reasoning. | If reasoning remains weak, model the relevant relation and invite another attempt. If only recognition/access fails, compare representations or improve access. Neither branch is a validated diagnosis. |
| Correct with hints or tools only | Vary one named aid while keeping the reasoning demand similar. | Retain necessary access tools; reduce solution hints only provisionally. Do not remove tools that the intended capability permits simply to make the task harder. |
| Correct routine answer and explanation | Change a relevant condition as well as surface details; ask what changes and why. | Offer less solution support after representative independent success, then check again. One success is insufficient to establish an optimal fading threshold. |
| Fluent explanation but weak integrated performance | Compare component and whole-task demands; record time/memory and omitted information. | Offer targeted integration practice or support rather than repeat the whole explanation automatically. |
| Low effort or little participation | Ask about purpose and barriers; compare accuracy/reasoning under accessible, meaningful conditions. | Negotiate purpose or conditions when warranted. Neither effort nor participation alone establishes learning. |

## Choosing configurations from evidence

- For a comparable initial circuit task, [the four-arm contrast](../claims/worked-example-problem-sequences.md) supports an example-first candidate. Calculators/formula sheets were permitted; solution access was restricted. “Independent” must preserve that distinction.
- If examples/problems repeat the identical task, [the qualification](../claims/identical-example-problem-order-advantage-not-detected-at-final-test.md) prevents a universal final-test ordering claim. Lack of a detected difference is not equivalence.
- For a transition to more independent probability reasoning, [backward fading and principle prompts](../claims/fading-and-principle-prompts-improve-probability-transfer.md) provide a candidate configuration. Their study does not validate this table's adaptive branches or a special synergy.

Do not convert reported partial η² into a probability, rank unlike comparators using Cohen/Kraft labels, or predict delayed repair from immediate paper-task scores. A precise abstention names the missing comparison, target or observation and the next way to resolve it.

## Fitting the design to a situation

Ask for three facts when the brief omits them: **what a learner does on a first attempt at this problem type without help**, **how many example–problem pairs the time allows**, and **which outcome is checked, and when** (the practised procedure, a changed problem, a delayed test).

| If the brief says… | Then change… | Basis |
|---|---|---|
| A first lesson on a structured procedure for learners who have not met it | Open with a fully worked example with the reasoning for each step visible, then a comparable problem | [Example-based sequences outperform problem-only practice for novices](../claims/worked-examples-with-practice-improve-transfer.md) [+M]; [Example–problem sequences reduce cognitive load](../claims/worked-example-problem-sequences.md) [+M] |
| One lesson with room for about four pairs | Sequence example → problem in each pair, never problem → example | [Example-first beat problem-first on an immediate test](../claims/worked-example-problem-sequences.md) [+M] |
| The paired problem is identical to the example | Vary the paired problem's surface or numbers, and do not expect an order effect to last to a final test | [Order advantage not detected at the final test](../claims/identical-example-problem-order-advantage-not-detected-at-final-test.md) [~M] |
| A unit of several lessons | Move from full examples to examples with the last step left out, then two steps, then bare problems | [Fading worked steps eases the move to problem solving](../claims/fading-worked-steps-facilitates-example-to-problem-transition.md) [+M] |
| Learners will be tested on the principles, not only the procedure | Fade the steps that apply the principles to be learned, and prompt learners to name the principle at each step | [Learners learned most about the faded principles](../claims/learners-learn-most-about-faded-principles.md) [+M]; [Backward fading and principle prompts supported transfer](../claims/fading-and-principle-prompts-improve-probability-transfer.md) [+M] |
| The first attempt shows learners can already solve and explain the problem | Skip to completion or independent problems for those learners, and check again on a changed problem | [Worked examples become less effective as expertise grows](../claims/worked-examples-less-effective-with-expertise.md) [~M] |
| The first attempt shows little task knowledge | Give full, not completion, examples to these learners | [Lower-prior-knowledge learners did better with full than completion examples](../claims/lower-prior-knowledge-learners-score-higher-with-full-than-completion-worked-examples.md) [+M] |
| Examples come as a diagram plus separate text, or as narrated slides | Integrate the text into the diagram; if narration is used, add cues that direct attention when the visual search is heavy | [Split-attention examples lose their advantage](../claims/split-attention-effect-in-worked-examples.md) [~M]; [Dual-mode presentation helps, except under high visual search without cues](../claims/dual-mode-worked-example-presentation.md) [~W] |
| The practice set uses widely varied problems | Pair varied problems with worked examples rather than with conventional problem solving | [High variability aids learning from examples but harms learning from problems](../claims/variability-effect-format-interaction.md) [~W] |
| An AI tutor or retrieval system is meant to supply worked examples | Check that examples are actually delivered; one system included them in about 42% of responses despite a large problem bank | [Worked examples appeared in only about 42% of responses](../claims/algorag-worked-example-retrieval-42-percent.md) [-W] |

## The evidence by question

- *Do novices learn more from studying worked examples than from solving the same problems unaided?* [Example-based sequences outperform problem-only practice for novices, and fading support is argued to aid transfer](../claims/worked-examples-with-practice-improve-transfer.md) [+M]
- *For whom: how does the benefit change with prior knowledge?* [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
- *How should learners move from studying examples to solving problems alone?* [Successively fading out worked solution steps is effective for facilitating the transition from learning from worked examples to problem solving, compared to example-problem pairs](../claims/fading-worked-steps-facilitates-example-to-problem-transition.md) [+M]

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-09-30 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+W] — not settled: the abstract available could not confirm the entries
- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/worked-example-problem-sequences.md) [+W] — not yet checked against its sources

## Illustrative design instance and observation record

A learner wants to explain equipment faults; the designer initially requests speed. Elicit the difference, agree whether explanation and/or timing matter, and choose a representative simulated diagnosis. Define an agreed reasoning rubric and permitted aids; assess delayed application separately if it is a target. This is an illustrative proposal, not a tested repair lesson.

Record: **prompt/task → permitted and actual help → response/reasoning → candidate interpretations and confidence basis → distinguishing probe → chosen activity and justification → next observation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record, but must not fabricate missing inputs or assign numerical state probabilities without a calibrated model.

## Elements and limits

[Worked examples](../elements/worked-examples.md), [demonstration](../elements/demonstration.md), [fading](../elements/fading.md), and [practice](../elements/practice.md).

This pattern is scoped to selecting solution support for structured tasks. Open-ended generation, incorrect examples, productive-failure lessons and competency certification need distinct configurations and evidence. The present policy supports observation and design reasoning; predictive accuracy and the learner-significance mechanism remain to be tested with actual learners.

## Claims

- [Pedagogical-criterion breakdown shows worked examples in only about 42% of responses, the weakest criterion despite 312 practice problems in the knowledge base](../claims/algorag-worked-example-retrieval-42-percent.md) [-W]
- [Prior knowledge and working memory capacity did not moderate the worked example effect](../claims/no-prior-knowledge-wmc-moderation-worked-examples.md) [~W]
- [Worked examples improved the exchange of relevant information in the CDR process, driven by the initial-situation step](../claims/worked-examples-improve-information-exchange-process.md) [+W]
- [Duration of the initial problem-solving phase reverses the PS-I versus WS-I transfer advantage](../claims/ps-phase-duration-reverses-ps-i-ws-i-transfer.md) [~W]
- [Worked examples did not improve application of CDR strategy knowledge relative to problem-solving](../claims/worked-examples-no-improvement-knowledge-application.md) [-W]
- [Alternating example-practice pairs produce faster and more accurate near-transfer solutions than blocked presentation of examples followed by practice](../claims/alternating-example-problem-pairs.md) [~W]

## Key Sources

- van Gog, T., Kester, L., & Paas, F. (2011). Effects of worked examples, example-problem, and problem-example pairs on novices' learning. *Contemporary Educational Psychology, 36*(3), 212–218. [doi:10.1016/j.cedpsych.2010.10.004](https://doi.org/10.1016/j.cedpsych.2010.10.004)
- van Gog, T. (2011). Effects of identical example–problem and problem–example pairs on learning. *Computers & Education, 57*(2), 1775–1779. [doi:10.1016/j.compedu.2011.03.019](https://doi.org/10.1016/j.compedu.2011.03.019)
- Atkinson, R. K., Renkl, A., & Merrill, M. M. (2003). Transitioning from studying examples to solving problems: Effects of self-explanation prompts and fading worked-out steps. *Journal of Educational Psychology, 95*(4), 774–783. [doi:10.1037/0022-0663.95.4.774](https://doi.org/10.1037/0022-0663.95.4.774)
- Renkl, A., Atkinson, R.K. & Große, C.S. (2004). How Fading Worked Solution Steps Works – A Cognitive Load Perspective. Instructional Science. https://doi.org/10.1023/B:TRUC.0000021815.74806.f6
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59-89. [https://doi.org/10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Gupta, U., & Zheng, R. Z. (2020). Cognitive Load in Solving Mathematics Problems: Validating the Role of Motivation and the Interaction Among Prior Knowledge, Worked Examples, and Task Difficulty. European Journal of STEM Education, 5(1), 05. https://doi.org/10.20897/ejsteme/9252
