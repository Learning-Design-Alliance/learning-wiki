---
type: pattern
title: Project Space and Instructional Space
description: Reigeluth's response to problem-based instruction's weaknesses — learners work on an authentic project and "freeze" it whenever they hit a learning gap, moving into an individualized instructional space for targeted mastery practice before returning to apply the new skill.
status: draft
generated:
  by: claude/unspecified
  at: 2026-08-29
author: Charles M. Reigeluth
grain_size: unit
---

# Project Space and Instructional Space

## Description
Reigeluth (2011) identifies four persistent weaknesses of problem-based instruction (PBI): team-based assessment makes it hard to verify that *every* individual learned the intended content (a "loafer" can ride the team's work); learners typically use a given skill only once or twice within a project, insufficient for the extensive practice complex skills need to transfer to new situations; PBI does not build automaticity for skills that need to be executed with reduced conscious effort; and unguided search for information within a project wastes significant learner time. His response is not to abandon PBI for direct instruction, but to architect two distinct, alternating spaces within the same learning experience.

Learners work in a **project space**: an authentic, ill-structured task, ideally in a computer-based simulation, using established project-based/problem-based design guidance (problem selection, group formation, tutor facilitation, authentic assessment, debriefing). Whenever a learner or team hits a learning gap, they **"freeze" the project** and enter an **instructional space** — individualized tutoring (conceivably delivered by a virtual mentor/avatar) that tells, shows, and gives practice with immediate feedback on the specific skill needed, across diverse situations, until the learner reaches an explicit mastery criterion (including a speed criterion when automaticity matters). Only then does the learner return to the unfrozen project to apply the new skill and continue until the next gap. Instructional strategy within the instructional space is matched to the type of learning involved: drill-and-practice (chunking, repetition, mnemonics) for memorization; tutorials with generality, examples, and feedback for skill application; analogies and advance organizers for conceptual understanding; and causal exploration (examining causes, effects, and solutions) for theoretical understanding.

This design directly answers PBI's four weaknesses: individual — not just team — mastery becomes assessable because the instructional space tracks each learner's own practice to criterion; transfer is supported because the instructional space provides repeated practice across diverse situations rather than the one or two uses a project alone would offer; automaticity becomes achievable via an explicit speed criterion; and efficiency improves because targeted instruction replaces unguided search, with assessment folded directly into the practice-to-criterion process rather than run as a separate activity.

## Implications

### Context
#### Requirements
- A means of "freezing" the authentic project without losing learner engagement or project state — most naturally a computer-based simulation, though Reigeluth notes the project space could also be entirely real-world (with the instructional space then delivered on a mobile device) or a hybrid
- Individualized instructional content or tutoring capable of diagnosing exactly which skill gap a learner has hit and delivering targeted tell-show-practice-feedback for it
- An explicit mastery criterion (and, where relevant, a speed/automaticity criterion) that gates return to the project space
#### Constraints
- Requires substantially more instructional design investment than either a pure project-based unit or pure direct instruction alone, since both a project space and a parallel, diagnosable instructional space must be built
- The individualized diagnosis-and-tutoring step depends on either a sophisticated computer-based system or significant human tutoring capacity — without one of these, the "freeze and get individualized help" mechanic is difficult to deliver at any scale
#### Grain Size
- Unit
- Course

### Target Goals
- Preserving PBI's intrinsic motivation and authenticity while directly fixing its documented weaknesses in individual mastery assessment, transfer, automaticity, and efficiency
- Attainment-based (not time-based) progress, consistent with the broader [Learner-Centered Paradigm of Education](../principles/learner-centered-paradigm.md)

### Target Learners
- Learners working on complex, authentic projects who need certifiable individual mastery of component skills, not just a good team product

### Theory
#### Supporting
- [First Principles of Instruction](../theories/first-principles-of-instruction.md) [+S] — the instructional space's tell-show-practice-with-feedback structure, generalized across diverse situations, is a direct application of Merrill's demonstration and application principles
- [Cognitive Load Theory](../theories/cognitive-load-theory.md) [+M] — targeted instruction at the moment of an identified gap avoids the wasted search time and load PBI's unguided struggle imposes
#### Contradicting / Qualifying
- Explicitly framed as a response to documented weaknesses of unmodified problem-based instruction (team-based assessment hiding individual non-mastery, insufficient repetition for transfer, no automatization, and unguided-search inefficiency)

### Claims

## Design

### Sequence
1. Place learners (individually or in small teams) into an authentic project, ideally within a computer-based simulation.
2. When a learner encounters a learning gap, "freeze" the project.
3. Diagnose the specific skill/knowledge gap and enter the instructional space: tell, show (for diverse situations), and provide practice with immediate feedback.
4. Continue practice until the learner reaches the mastery criterion for the skill (and a speed criterion, when automaticity is required).
5. Unfreeze the project and have the learner apply the newly mastered skill to continue the project.
6. Repeat the freeze/instruct/unfreeze cycle at each new learning gap.

### Affordances
- [Problem-based Learning](../principles/problem-based-learning.md)
- [Mastery Learning](../principles/mastery-learning.md)
- [First Principles of Instruction](../theories/first-principles-of-instruction.md)

### Personalization
- Each learner progresses through the instructional space at their own pace and only for the specific gaps they individually encounter, rather than a fixed group sequence
- The instructional strategy used within the instructional space adapts to the type of learning required (memorization, skill, conceptual, or theoretical understanding) rather than applying one method uniformly

## Related Patterns
- [Epistemic Games](epistemic-games.md) — both embed learning within an authentic simulated task, though epistemic games focus on inhabiting a professional identity rather than alternating with a separate diagnostic instructional space

## Examples
- STAR LEGACY, a computer-based simulation cited by Reigeluth as an example project-space environment
- A military training simulation where a trainee's project is paused for individualized skill remediation whenever a competency gap is detected, then resumed

## Key Sources
- Reigeluth, C. M. (2011). An instructional theory for the post-industrial age. *Educational Technology, 51*(5), 25–29. Republished in R. West (Ed.), *Foundations of Learning and Instructional Design Technology*. EdTech Books. [https://edtechbooks.org/lidtfoundations/postindustrial_age_theory](https://edtechbooks.org/lidtfoundations/postindustrial_age_theory)
- Merrill, M. D. (1983). Component display theory. In C. M. Reigeluth (Ed.), *Instructional-Design Theories and Models*. Lawrence Erlbaum Associates.
