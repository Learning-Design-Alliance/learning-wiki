---
type: pattern
title: Programmed Instruction
description: Programmed Instruction breaks content into small self-contained steps, each requiring an active response with immediate confirmation, so learners advance individually rather than at a group's pace.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
author: B. F. Skinner (linear); Norman Crowder (branching/intrinsic)
grain_size: lesson
---

# Programmed Instruction

## Description
Programmed Instruction (PI) restructures content as a sequence of small "frames," each presenting a small amount of information and then requiring the learner to make an active response — write or select an answer — before immediately revealing whether it was correct. Skinner's original **linear programming** moved every learner through the same fixed sequence of small steps; Norman Crowder's **intrinsic (branching) programming** let learners skip ahead through easy material or branch to remedial frames when they struggled, based on their responses (Molenda, 2008).

PI was devised as a humane alternative to lock-step, group-paced instruction: it lets each learner work at their own pace, guarantees a response at every step (rather than passive listening), and provides confirmation immediately rather than after a delay. It was the first instructional format subjected to the "90/90 criterion" (at least 90% of the target population achieving 90% of objectives) as a mandatory development standard, which drove a discipline of testing and revising materials during development — a direct precursor to systematic instructional design.

While PI itself receded after the 1960s once most of its specific hypotheses (small steps, linear sequencing, immediate reinforcement as universally necessary) failed to hold up under testing, several descendants inherited its core mechanism — a small step, an active response, and confirmation or correction — while adding features PI lacked: **Programmed Tutoring** (Ellson) added a human tutor providing social reinforcement and hints instead of a mechanical device; **Direct Instruction** (Engelmann) added fast-paced, scripted, teacher-led group unison responding; and the **Personalized System of Instruction** ("Keller Plan") added self-paced units with a mastery test and proctor feedback at the end of each unit before the learner advances — the direct forerunner of mastery-based and self-paced distance education.

## Implications

### Context
#### Requirements
- Content that can be broken into small, sequential, well-defined steps, each pairing information with a checkable response
- A mechanism (mechanical device, book layout, tutor, or software) for withholding the correct answer until after the learner responds, and revealing it immediately after
#### Constraints
- Small-step, linear sequencing is not itself necessary for effectiveness — later research found branching and larger chunks worked as well or better for many learners; the pattern's value lies in active responding and immediate confirmation, not the specific step size
- Poorly suited to open-ended, ill-structured content where there is no single correct response to confirm at each step
- Schools found PI materials effective in isolation but could not realize gains without restructuring surrounding classroom routines and pacing — the pattern strains against institutions built around fixed group pacing
#### Grain Size
- Lesson
- Unit

### Target Goals
- Discrete, checkable knowledge and skills: recall of facts, application of rules, execution of procedures
- Self-paced mastery, letting faster learners advance without waiting and slower learners repeat without holding others back

### Target Learners
- Learners who benefit from working independently at their own pace rather than a fixed group pace
- Learners in domains (military and corporate training, in particular) where efficiency and measurable objective attainment matter enough to justify the design and testing investment PI requires

### Theory
#### Supporting
- [Behaviorism](../theories/behaviorism.md) [+S] — PI is behaviorism's most direct instructional expression: small stimulus-response steps strengthened by immediate reinforcement (confirmation of the correct response)
#### Contradicting / Qualifying
- Subsequent research undermined several of PI's specific behaviorist hypotheses (that steps must be small, sequencing must be linear, and "knowledge of correct response" is a universal reinforcer), even though PI as a format continued to outperform "conventional" group instruction in comparison studies

### Claims

## Design

### Sequence
1. Break the content into small, sequential frames, each presenting a bit of information.
2. Require the learner to make an active response (write or select an answer) before moving on.
3. Reveal the correct answer or confirm the learner's response immediately.
4. For branching/intrinsic programming: route the learner to a remedial frame on an incorrect response, or let them skip ahead on strong performance.
5. Let the learner progress through the full sequence at their own pace, rather than a fixed group pace.

### Elements Used
- [Self-Paced Learning](../elements/self-paced-learning.md)
- [Immediate Feedback](../elements/immediate-feedback.md)
- [Practice](../elements/practice.md)

### Affordances
- [Mastery Learning](../principles/mastery-learning.md)
- [Immediate Feedback](../principles/immediate-feedback.md)

### Personalization
- Branching (intrinsic) programming personalizes the path itself, sending struggling learners to remedial frames and letting confident learners skip ahead
- Even linear programming personalizes pace, since every learner moves through the same steps but on their own schedule

## Related Patterns
- [Game-Based Mastery Learning](game-based-mastery-learning.md) — a modern descendant that adds game mechanics (streaks, levels, adaptive difficulty) to the same small-step, immediate-feedback, self-paced core PI established

## Examples
- Skinner's original teaching-machine frames and linear programmed textbooks (e.g., *English 2600*)
- Crowder's AutoTutor and TutorText branching programmed books
- The Personalized System of Instruction ("Keller Plan"): self-paced units with a mastery test and proctor feedback before advancing

## Key Sources
- Molenda, M. (2008). The programmed instruction era: When effectiveness mattered. *TechTrends, 52*(2), 52–58. Republished in R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/programmed_instruction](https://edtechbooks.org/lidtfoundations/programmed_instruction)
- Skinner, B. F. (1954). The science of learning and the art of teaching. *Harvard Educational Review, 24*, 86–97.
- Keller, F. S. (1968). Goodbye, teacher... *Journal of Applied Behavior Analysis, 1*, 78–79.
