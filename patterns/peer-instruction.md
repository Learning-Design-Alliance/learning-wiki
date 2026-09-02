---
type: pattern
id: peer-instruction
title: Peer Instruction
description: Peer Instruction is a pattern in which learners first answer a conceptual question individually, then discuss their reasoning with peers, and then answer again before instructor debrief.
status: review
generated:
  by: claude/unspecified
  at: 2026-08-29
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

## Related Patterns
- [Think-Pair-Share](think-pair-share.md)
- [Discussion Group](discussion-group.md)

## Examples
- Physics learners debating force or motion concept questions before repolling.
- Medical learners comparing diagnostic reasoning on a conceptual clinical prompt.
- Math or engineering classes using concept checks before moving into longer problem work.

## Impact
- Often improves engagement and conceptual understanding in large classes.
- Most effective when misconceptions are surfaced through strong questions and resolved through debrief.

## Key Sources
- Mazur, E. (1997). *Peer instruction: A user's manual*. Prentice Hall.
- Crouch, C. H., & Mazur, E. (2001). Peer instruction: Ten years of experience and results. *American Journal of Physics, 69*(9), 970-977. [https://doi.org/10.1119/1.1374249](https://doi.org/10.1119/1.1374249)
- Hake, R. R. (1998). Interactive-engagement versus traditional methods: A six-thousand-student survey of mechanics test data for introductory physics courses. *American Journal of Physics, 66*(1), 64-74. [doi:10.1119/1.18809](https://doi.org/10.1119/1.18809)
- Deslauriers, L., Schelew, E., & Wieman, C. (2011). Improved learning in a large-enrollment physics class. *Science, 332*(6031), 862-864. [doi:10.1126/science.1201783](https://doi.org/10.1126/science.1201783)
- Arduini-Van Hoose, N. (2020). Flipped classroom. In *Educational psychology*. Retrieved from https://edpsych.pressbooks.sunycreate.cloud. CC BY-NC-SA 4.0.
