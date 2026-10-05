---
type: pattern
id: peer-instruction
title: Peer Instruction
description: "A reusable question, individual vote, peer discussion, revote and explanation policy for conceptual questions, with an isomorphic individual check to separate revised reasoning from copying."
status: review
generated:
  by: claude/unspecified
  at: 2026-10-01
sources:
  - id: crouch-2001
    resource: "https://doi.org/10.1119/1.1374249"
    title: "Crouch, C. H., & Mazur, E. (2001). Peer instruction: Ten years of experience and results. *American Journal of Physics, 69*(9), 970-977"
    author: "Crouch, C. H., & Mazur, E"
author: Eric Mazur
grain_size: lesson
---

# Peer Instruction

> **Pattern** · [All patterns](index.md)
> **Evidence** · 9 claims (4 for, 5 mixed) · 19 studies (5 causal, 5 quant-synthesis, 5 review, 2 associational, 1 qualitative, 1 theoretical), `q2`–`q4` · 4 of 19 report an effect size · 4 claims rest on one study

## Description and scope

A reusable policy for using a conceptual question to elicit an individual committed answer, have learners discuss their reasoning with peers, collect a second answer and close with explanation: **question → individual vote → peer discussion → revote → explanation**. It instantiates the [Peer Discussion principle](../principles/peer-discussion.md). The study configurations below are evidence; the response-dependent policy (when to discuss, when to explain, when to move on) is an **untested design proposal**. Use it to collect better observations of reasoning, not to certify that a class has understood because a revote converged.

## Inputs: establish the design brief

| Field | Record or elicit |
|---|---|
| Learner and starting observation | Each learner's individual answer and, where possible, confidence and a one-line reason; the class distribution; task-specific prior instruction. Preserve unknowns rather than labelling the class "novice". |
| Context and activities | Setting (`classroom`, `online-instructor-led`), class and group size, response mode (clickers, cards, digital poll, written), time per cycle, whether the distribution is shown before discussion, how groups are formed, language and access conditions, and what the instructor explains afterwards. |
| Learner-valued goal | Ask what learners want from the discussion and why. Record disagreement with the designer's objective; do not assume that participation means agreement. |
| Designer objective | The concept or principle targeted, the misconception or alternative the question is built to separate, and whether the aim is answering this kind of question, explaining it, or applying it to an unfamiliar case. |
| Outcome | An individual answer on a new isomorphic question, a justification rubric, and the horizon (`immediate` in-class, or `delayed`); any course exam or concept inventory used, and how closely it matches the questions practised. |

A request to "make lectures more interactive" does not specify these inputs. Ask for them before prescribing a cycle length, a correct-answer threshold for discussion, or an expected gain. Check that the question has one defensible answer and that its distractors represent reasoning learners actually hold.

## Sequence and conditional policy

1. **Pose the question and collect individual answers.** No discussion before the first vote. Record the distribution and, if feasible, confidence and reasons. Withhold the correct answer.
2. **Decide whether to discuss.** Use the distribution as one observation, not a rule: a split class suggests reasoning worth exchanging; near-unanimity in either direction may call for explanation or a harder question. Any threshold is a local choice; the evidence here does not set one.
3. **Peer discussion of reasoning.** Ask learners to convince a neighbour of their answer by giving a reason, not to agree on a letter. Circulate and sample what groups say.
4. **Revote, then an isomorphic check.** Collect a second individual answer. Where the aim is understanding, follow with a new isomorphic question answered alone, since the revote cannot separate revision from copying.
5. **Explain and reobserve.** Explain why the stronger reasoning is stronger, address the distractors chosen, and recheck at the stated horizon. If observations disagree with the expectation, revise the question, grouping or explanation rather than the interpretation.

| Observation | Discriminating probe | Proposed action, with its uncertainty |
|---|---|---|
| Individual answers split across options | Ask a sample of learners for their reasons before discussion. | Run peer discussion, then revote and an isomorphic question. If reasons show the question is ambiguous rather than diagnostic, fix the question; the split itself does not say which. |
| Most answer correctly on the first vote | Ask for a justification or pose an isomorphic question with changed surface features. | If justifications hold, explain briefly and move on; if they do not, the correct answers may be guesses or recognition, and a harder or changed question may be needed. |
| Few answer correctly on the first vote | Ask what learners took the question to be asking; check whether the needed concept was ever taught. | Consider explanation or a simpler bridging question before discussion. Discussion among learners who share one misconception may reinforce it; this is a proposal, not a tested branch. |
| Revote converges, isomorphic question does not improve | Compare who changed answers with who spoke first or most confidently in each group. | Treat the revote gain as possible copying; add instructor explanation and another isomorphic check rather than declaring understanding. |
| Some groups talk little or one member dominates | Ask privately or in writing for each learner's reasoning; vary group composition on the next question. | Adjust grouping, roles or response mode. Neither silence nor talk volume alone establishes understanding. |

## Choosing configurations from evidence

- For a check that separates revision from copying, [the isomorphic-question design](../claims/peer-discussion-improves-conceptual-understanding.md) [+M] supports following the revote with a new isomorphic question answered alone. In the recorded comparison, peer discussion followed by instructor explanation exceeded either alone in undergraduate genetics courses; that is one quasi-experimental classroom study with no standardized effect size, and its "similar gains" detail could not be confirmed from the abstract. It supports keeping the explanation step, not dropping it.
- For the expectation over a course, [active learning in undergraduate STEM](../claims/active-learning-improves-exam-performance.md) [+M] reports 0.47 SD higher exam and concept-inventory scores than traditional lecturing across 158 studies, largest on concept inventories and in small classes, and gap narrowing only under high-intensity active learning. Peer instruction is one of many formats pooled; the synthesis does not isolate it, and the entries have not been confirmed against their sources.
- For what the vote alone may contribute, [classroom quizzing](../claims/classroom-quizzing-improves-exam-performance-across-grades-and-content.md) [+W] is reported (second-hand, via a review chapter) to improve classroom exams without any discussion step. A design that drops discussion is a different configuration, and gains from the full cycle should not be attributed to discussion alone.
- For what the cycle may not change, [content gains without reasoning gains](../claims/reformed-pedagogy-content-gains-but-no-reasoning-gains.md) [~W] records normalized gains of about 0.38–0.42 on content instruments but 0.06 on a scientific-reasoning test under an active-engagement pedagogy, in an associational study with no comparison group, not yet checked. Do not expect concept-question practice to build general reasoning ability unless that is taught and measured.
- For grouping, [poor group leadership](../claims/cooperative-conceptual-change-chemistry-misconceptions.md) [~W] is reported (second-hand) to have prevented effective discussion in cooperative conceptual-change groups in community-college chemistry. Watch who closes the discussion.

Do not convert a normalized gain into a d, rank these studies by effect labels, or predict delayed retention from in-class revote changes. A precise abstention names the missing comparison, target or observation and the next way to resolve it.

## Further evidence, not yet read against this model
<!-- Restored 2026-10-01 (maintainer's decision): claims this page cited before the 2026-10-01 rewrite, which kept only claims whose sources it had re-read. Each marker keeps its old direction, capped by the claim's recorded evidence (strength_cap); each label says how far the claim's own entries have been checked against their sources by check_load_bearing.py. None has been re-read for the conditional model above, so treat them as candidates for it, not as part of it. -->
Claims this page cited before it was rewritten as a conditional model. They are evidence about the relationship, but none has yet been re-read against the model above; each says how far its own sources have been checked.

- [Prompting learners to self-explain improves understanding and problem solving on immediate tests by a moderate average amount, with little evidence yet on delayed or classroom gains.](../claims/self-explanation-improves-conceptual-understanding.md) [+S] — not settled: the text available could not confirm the entries (abstract)
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M] — not settled: the text available could not confirm the entries (abstract)
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M] — not settled: the text available could not confirm the entries (abstract)
- [Specific, difficult goals lead to higher performance than easy or vague "do your best" goals.](../claims/specific-difficult-goals-lead-to-higher-performance.md) [~M] — not yet checked against its sources

## Illustrative design instance and observation record

*Invented illustration, not a tested lesson.* In an introductory physics lecture, the instructor poses a question on whether a heavier and a lighter ball dropped together land at the same time. Individual answers split between two options. A learner says she wants to be able to explain her answer to a younger sibling; the instructor's objective is reasoning about acceleration that transfers to an inclined-plane case. After discussion and revote, learners answer an isomorphic question about two carts on a ramp alone, then the instructor explains and asks for a one-line justification; the same kind of question returns on a quiz the following week. These are local design choices; the evidence above does not establish their optimality.

Record: **question and intended distinction → individual answer, confidence and reason → distribution shown or withheld → group composition and sampled talk → revote → isomorphic individual answer → candidate interpretations (revision, copying, convergence) and their basis → instructor explanation given → next observation at the stated horizon**. Preserve the learner's stated purpose and any change in it. An agent may summarize this record but must not fabricate missing inputs or assign numerical probabilities of understanding without a calibrated model.

## Elements and limits

[ConcepTest](../elements/conceptest.md), [conceptual questioning](../elements/conceptual-questioning.md), [misconception probes](../elements/misconception-probes.md), [peer discussion](../elements/peer-discussion.md), [reassessment](../elements/reassessment.md), [feedback](../elements/feedback.md) and [debrief](../elements/debrief.md). Principles the cycle draws on: [Peer Discussion](../principles/peer-discussion.md), [Formative Assessment](../principles/formative-assessment.md), [Immediate Feedback](../principles/immediate-feedback.md) and [Purposeful Reflection](../principles/purposeful-reflection.md).

This pattern is scoped to conceptual questions with a defensible answer. Open-ended discussion, procedural fluency, first exposure to unfamiliar material and attitude change need different configurations and evidence. The policy supports observation and design reasoning; its branches, any discussion threshold and its effect on delayed or transfer outcomes remain to be tested with learners.

## Related Patterns
- [Think-Pair-Share](think-pair-share.md)
- [Discussion Group](discussion-based-learning.md)

## Examples
- Physics learners debating force or motion concept questions before repolling.
- Medical learners comparing diagnostic reasoning on a conceptual clinical prompt.
- Math or engineering classes using concept checks before moving into longer problem work.

## Key Sources
- Mazur, E. (1997). *Peer instruction: A user's manual*. Prentice Hall.
- Crouch, C. H., & Mazur, E. (2001). Peer instruction: Ten years of experience and results. *American Journal of Physics, 69*(9), 970-977. [https://doi.org/10.1119/1.1374249](https://doi.org/10.1119/1.1374249)
- Hake, R. R. (1998). Interactive-engagement versus traditional methods: A six-thousand-student survey of mechanics test data for introductory physics courses. *American Journal of Physics, 66*(1), 64-74. [doi:10.1119/1.18809](https://doi.org/10.1119/1.18809)
- Deslauriers, L., Schelew, E., & Wieman, C. (2011). Improved learning in a large-enrollment physics class. *Science, 332*(6031), 862-864. [doi:10.1126/science.1201783](https://doi.org/10.1126/science.1201783)
- Arduini-Van Hoose, N. (2020). Flipped classroom. In *Educational psychology*. Retrieved from https://edpsych.pressbooks.sunycreate.cloud. CC BY-NC-SA 4.0.

<!-- deprecated 2026-10-01: superseded by the conditional model above; the body it replaced, kept verbatim.

## Description
Peer Instruction is a pattern in which learners first answer a conceptual question individually, then discuss their reasoning with peers, and then answer again before instructor debrief. The key mechanism is not the poll itself. It is the combination of commitment, peer explanation, reconsideration, and feedback that helps learners confront misconceptions and refine understanding.

The pattern is especially effective for conceptual questions that require reasoning rather than recall. It works well in large classes because it creates active processing without needing the instructor to hear every learner individually.

In practice, students typically answer individually via clickers or a handheld response system (anonymously, with results visible immediately to the instructor); if a large fraction of the class (usually 30-65%) answers incorrectly, students discuss in small groups while the instructor circulates, then answer again, with the instructor closing the cycle by explaining the correct answer and following up with related questions — each full cycle typically taking 13-15 minutes. The evidence for its effectiveness is unusually well quantified: Hake's (1998) large survey compared 2,084 students in 14 traditionally-taught introductory physics courses against 4,458 students in 48 courses using "interactive engagement" methods (broadly, active, feedback-rich approaches including peer instruction), finding pre/post-test learning gains almost two standard deviations higher for the interactive-engagement group (0.48 ± 0.14 vs. 0.23 ± 0.04). Assessing peer instruction specifically across eight years at Harvard, Crouch and Mazur (2001) found even larger gains (0.49 to 0.74), compared to just 0.25-0.40 for traditionally-taught sections at the same institution during the same period. Deslauriers, Schelew, and Wieman (2011) found a similar effect in a more tightly controlled comparison: two sections of the same large-enrollment physics course, showing no prior differences, were taught identically until one section was "flipped" for a single week (pre-class reading and quizzes, in-class small-group discussion of clicker and written-response questions, no lecture) while the other continued as before — the flipped section still showed a substantial learning-gain advantage over the matched control from that single week's change alone.

## Implications

### Context
#### Requirements
- **Conceptually rich questions**: The prompt needs to provoke reasoning and disagreement, not simple memory.
- **Initial individual commitment**: Learners should answer before discussion so they have something to compare and defend.
- **Peer explanation time**: The discussion phase must give enough time for reasoning exchange.
- **Instructor debrief**: Learners need closure on why the stronger reasoning is stronger.
#### Constraints
- **Weak questions flatten the pattern**: Fact recall items do not generate much conceptual change.
- **Noisy consensus risk**: Learners can converge on an answer socially without improving reasoning if facilitation is weak.
- **Technology is optional but not sufficient**: Clickers or polling help, but the real work happens in the discussion.
- **Not ideal for first exposure to very unfamiliar material**: Some initial orientation may be needed before conceptual polling works.
#### Grain Size
- Lesson

### Target Goals
- **Conceptual understanding**: Surfacing and revising misconceptions.
- **Reasoning articulation**: Learners explain why an answer makes sense.
- **Formative diagnosis**: Instructors see where understanding is strong or weak.

### Target Learners
- **Learners in STEM and concept-heavy courses**: Strong fit for questions where common misconceptions are predictable.
- **Large-group settings**: Useful where whole-class interactivity is otherwise difficult.
- **Learners who benefit from peer explanation**: The pattern leverages students as reasoning partners.

### Theory
#### Supporting
- Social constructivist perspectives — learners refine ideas by explaining and comparing reasoning with peers.
- Conceptual change traditions — confronting conflicting explanations can trigger revision of prior understanding.
- Formative assessment perspectives — repeated questioning provides immediate evidence about current understanding.
#### Contradicting / Qualifying
- Peer instruction is not just polling; without discussion and debrief it loses much of its value.
- The pattern is stronger for conceptual reasoning than for pure procedural fluency.

### Claims
#### Supporting
- [Self-explanation improves conceptual understanding and problem-solving performance.](../claims/self-explanation-improves-conceptual-understanding.md) [+S]
- [Self-monitoring improves self-regulation and supports better learning decisions.](../claims/self-monitoring-improves-self-regulation.md) [~M]
- [Contingent scaffolding improves learning more than fixed or absent support.](../claims/contingent-scaffolding-improves-learning.md) [~M]
#### Contradicting
- [Specific, difficult goals lead to higher performance than easy or vague "do your best" goals.](../claims/specific-difficult-goals-lead-to-higher-performance.md) [~S]

## Design

### Sequence
1. Pose a conceptual question and have learners answer individually.
2. Reveal the distribution or ask learners to compare responses without announcing the answer.
3. Have learners discuss reasoning with peers.
4. Re-poll or reassess after discussion.
5. Debrief the reasoning and clarify the concept.

### Elements Used
- [Conceptual Questioning](../elements/conceptual-questioning.md)
- [Peer Discussion](../elements/peer-discussion.md)
- [Reassessment](../elements/reassessment.md)
- [Feedback](../elements/feedback.md)

### Affordances
- [Peer Discussion](../principles/peer-discussion.md)
- [Formative Assessment](../principles/formative-assessment.md)
- [Immediate Feedback](../principles/immediate-feedback.md)
- [Purposeful Reflection](../principles/purposeful-reflection.md)

### Personalization
- Questions can be delivered through clickers, cards, hand signals, or digital polls.
- Pairs or small groups can be mixed intentionally depending on confidence and prior knowledge.
- The amount of instructor explanation after the repoll can vary depending on the quality of peer reasoning.

## Impact
- Often improves engagement and conceptual understanding in large classes.
- Most effective when misconceptions are surfaced through strong questions and resolved through debrief.

-->
