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
> **Evidence** · 6 claims (3 for, 3 unmarked) · 4 studies (4 causal), `q3` · 0 of 4 report an effect size · 6 claims rest on one study

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

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-09-30 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+W] — not settled: the abstract available could not confirm the entries
- [Example–problem sequences reduce cognitive load and improve learning outcomes](../claims/example-problem-sequences-reduce-cognitive-load.md) [+W] — not yet checked against its sources
- [Example-problem sequences reduce cognitive load and improve learning outcomes.](../claims/example-problem-sequences-reduce-cognitive-load.md) [+W] — not yet checked against its sources

## Illustrative design instance and observation record

A learner wants to explain equipment faults; the designer initially requests speed. Elicit the difference, agree whether explanation and/or timing matter, and choose a representative simulated diagnosis. Define an agreed reasoning rubric and permitted aids; assess delayed application separately if it is a target. This is an illustrative proposal, not a tested repair lesson.

Record: **prompt/task → permitted and actual help → response/reasoning → candidate interpretations and confidence basis → distinguishing probe → chosen activity and justification → next observation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record, but must not fabricate missing inputs or assign numerical state probabilities without a calibrated model.

## Elements and limits

[Worked examples](../elements/worked-examples.md), [demonstration](../elements/demonstration.md), [fading](../elements/fading.md), and [practice](../elements/practice.md).

This pattern is scoped to selecting solution support for structured tasks. Open-ended generation, incorrect examples, productive-failure lessons and competency certification need distinct configurations and evidence. The present policy supports observation and design reasoning; predictive accuracy and the learner-significance mechanism remain to be tested with actual learners.
