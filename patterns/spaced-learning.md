---
type: pattern
id: spaced-learning
title: Spaced Learning
description: "A reusable policy for distributing learning opportunities, preserving total practice, gap and assessment horizon when comparing schedules."
status: review
generated:
  by: codex/unspecified
  at: 2026-04-08
grain_size: course
---

# Spaced Learning

> **Pattern** · [All patterns](index.md)
> **Evidence** · 8 claims (7 for, 1 unmarked) · 10 studies (5 causal, 4 quant-synthesis, 1 review), `q2`–`q4` · 3 of 10 report an effect size · 4 claims rest on one study

## Description

A reusable policy for distributing learning opportunities, preserving total practice, gap and assessment horizon when comparing schedules.

## Principle

This reusable policy instantiates the [spaced learning principle](../principles/spaced-learning.md).

## Learner state, objective and valued goal

This is a reusable design model. A study result supplies a bounded observation; it does not reveal the state or future outcome of a new learner.

Before selecting a configuration, record the target task and representation, task-specific prior experience, access and language constraints, time available, observed responses and the exact help provided. Preserve an unknown rather than replacing it with a generic label such as novice. Ask the learner what they want to accomplish and why it matters. Record that **valued goal** separately from the designer's **learning objective**; agreement is an observation to elicit, not an assumption. If they diverge, negotiate the task or purpose and retain the unresolved difference.

Define the intended capability, a representative assessment task and scoring instrument, the criterion chosen for this design, and the assessment horizon. Agree what response would warrant changing support and how to check later independent performance. Criteria are local decisions, not universal mastery thresholds. If the brief only asks for better learning, elicit these fields before selecting an exact dose or forecasting a gain.

Keep the record in this form: **response under stated conditions → uncertain state hypotheses → discriminating observation → next activity → response at the stated horizon**. Difficulty, accuracy, speed, confidence and engagement are different observations. None alone proves learning. Record a learner's changed purpose or constraints as well as a changed performance.

## Observation and adaptation

This diagnostic policy is a **design proposal, not a validated scheduling algorithm**. Start with an unassisted sample of the target items, record item-level errors and the time since last exposure, then separate cued recognition, recall and meaningful use. Record restudy, corrective feedback, retrieval opportunities and actual gaps; changing them together changes the intervention.

| Observation | Rival interpretations and discriminating observation | Proposed next action |
|---|---|---|
| An item is not recalled | Weak initial encoding and loss of access across the gap are different possibilities. Check comprehension/recognition with a cue and whether the learner can explain the association; retest unassisted after relearning and an interval. | If the association is not understood, clarify and re-encode it. If understood but inaccessible, use corrective feedback and another separated retrieval. Do not optimize the gap from a single failure. |
| Immediate recall is fluent | Recent repetition and durable retrieval both predict this. Use an unassisted check after the target delay. | Maintain the delayed check rather than count fluency as retained learning; revise the schedule only after collecting later evidence. |
| Words are recalled but not used appropriately | Item retrieval and contextual language use are different capabilities; ask for meaning and use in a new conversational context. | Add contextual practice if recall succeeds but use fails. Do not claim that a word-pair recall study validates conversation transfer. |

If six of ten words are recalled today, that is a sample response, not a calibrated probability of recall next week. For a learner valuing conversation, record the designer's recall criterion (for example eight of ten is a local choice), the sampled prompts and the one-week horizon; also agree how appropriate use will be judged in a representative conversation. Do not silently substitute recall for that valued goal. If these fields are missing, elicit them before choosing a calendar schedule.

## Evidence-bounded expectation

A word-pair experiment separated total retrieval spacing from its relative arrangement: after first correct recall, repeated retrievals with intervening trials improved one-week recall relative to massed retrieval. At matched total nominal spacing, expanding, equal and contracting arrangements did not differ detectably: [absolute versus relative spacing observation](../claims/total-retrieval-spacing-beats-massed-but-relative-schedule-not-distinguished.md). The full source was checked. This does not establish equivalence or an advantage for expanding gaps, a universal calendar gap, or conversational use. Retain total practice, corrective feedback, initial learning criterion, actual gaps and final-test horizon when comparing schedules.

An equal schedule may be selected for practical reasons while this exact comparison remains unresolved; do not predict a gain from changing only equal to expanding gaps on this evidence. Calendar timing and the dose needed for a particular learner remain local questions. Lower practice fluency can coexist with better delayed performance, but difficulty alone does not identify the cause or predict the outcome.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-09-30 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Spaced Repetition Improves Retention](../claims/spaced-repetition-improves-retention.md) [+S] — not settled: the abstract available could not confirm the entries
- [Spaced Retrieval Improves Retention](../claims/spaced-retrieval-improves-retention.md) [+M] — not yet checked against its sources
- [Learners Misjudge Spacing Benefits](../claims/learners-misjudge-spacing-benefits.md) [+M] — checked by the judge: all 2 entries pass (abstract)
- [Spaced Practice Improves Retention](../claims/spaced-practice-improves-retention.md) [+S] — partly checked: 2 of 5 entries pass; the rest could not be settled from the text available
- [Distributed Practice Improves Retention](../claims/distributed-practice-improves-retention.md) [+M] — partly checked: 1 of 2 entries pass; the rest could not be settled from the text available
- [Spaced Retrieval Outperforms Restudy](../claims/spaced-retrieval-outperforms-restudy.md) [+M] — not yet checked against its sources
- [Spaced retrieval practice produces better final retention than massed retrieval even though spacing lowers initial retrieval success, and more absolute spacing enhances long-term retention](../claims/spaced-retrieval-outperforms-massed-retrieval-despite-lower-initial-recall.md) [+W] — checked by the judge: all 3 entries pass (full text)

## Elements

- [spaced repetition](../elements/spaced-repetition.md)
- [retrieval practice](../elements/retrieval-practice.md)

## Source verification and open tests

Karpicke & Bauernschmidt (2011), [author-hosted full text](https://learninglab.psych.purdue.edu/downloads/2011/2011_Karpicke_Bauernschmidt_JEPLMC.pdf). Method and results checked for the bounded contrast above.

The examples are local design instances, not additional observations from those studies. Test the proposed interpretation and activity branches with new learner responses; compare competing designs under matched conditions before claiming a causal or predictive advantage. Reassess the model when the observations disagree with it.
