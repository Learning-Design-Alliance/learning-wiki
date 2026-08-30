---
type: strategy
title: Explicit Instruction
description: Systematic, teacher-directed instruction in which skills are modeled directly, practiced with guidance, and gradually released to independent performance.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Explicit Instruction

## Description
Explicit instruction is a structured, teacher-directed approach in which the instructor clearly states the learning goal, models the skill or strategy step by step, guides learners through supported practice, and releases them to independent application. It makes the reasoning behind each step visible rather than leaving learners to infer procedures from examples or discovery. The canonical sequence is often summarized as "I do, we do, you do."

## Design Implications

Explicit instruction is grounded in cognitive load theory: novices lack the schemas to benefit from unguided exploration, so directly presenting procedures and strategies reduces unproductive search [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]. Its effectiveness depends on pairing modeling with guided practice and timely feedback, then fading support as competence develops [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [+S]. Instruction should be sequenced from simple to complex, with each step building on the last, and should include frequent checks for understanding so errors are corrected before they consolidate.

### Context
#### Requirements
- A clear, decomposed model of the target skill with an identified sequence of steps
- [Think-Aloud](../elements/think-aloud.md) modeling that makes expert reasoning audible, not just the visible actions
- High-frequency, success-rich [Practice](../elements/practice.md) with active learner responses (not passive listening)
- Continuous checks for understanding and immediate corrective [Feedback](../elements/feedback.md)
- A plan for [Fading](../elements/fading.md) support as accuracy and fluency grow

#### Constraints
- Sustained explicit instruction without independent practice produces weak retention [Pairing worked examples with practice or fading supports transfer better than examples alone.](../claims/worked-examples-with-practice-improve-transfer.md) [-S] — teacher talk crowds out the responding that drives encoding
- Less effective for learners with strong prior knowledge, who experience redundancy and disengagement [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
- Poorly suited to ill-structured, open-ended goals (creative writing, open inquiry) where no single expert procedure exists to model
- Over-scripted delivery can suppress learner [Autonomy](../principles/autonomy.md) and reduce motivation over time [~W]

#### Implementation Variability
- **Full explicit model** (e.g., Engelmann's Direct Instruction): tightly scripted programs with choral responding — highest structure
- **Strategy-explicit model** (e.g., reciprocal teaching's early phases): teacher models a cognitive strategy, then transfers control of it to student-led groups
- **Media-based model**: narrated worked examples and video modeling deliver the same sequence asynchronously

### Target Learners
- Novices and struggling learners who lack the prior knowledge to guide their own search [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- Young learners and learners with learning disabilities, for whom the evidence base is strongest (especially in reading and mathematics)
- Less beneficial for advanced learners, who benefit more from problem-solving and inquiry [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]

### Target Learning Goals
- Procedural and foundational skills: decoding, arithmetic operations, grammatical conventions
- Cognitive strategies: comprehension strategies, problem-solving heuristics, study routines
- Prerequisite knowledge that must be automatic before higher-order work ([Automaticity](../elements/automaticity.md))

### Instructions
1. State the objective and activate relevant prior knowledge ([Activation](activation.md)).
2. Model the skill with a [Think-Aloud](../elements/think-aloud.md), demonstrating one clear example and, where useful, a [Non-Examples](../elements/non-examples.md) contrast.
3. Guide practice: learners attempt parallel problems with prompts, worked-example study, and immediate correction ([Practice](../elements/practice.md)).
4. Check understanding frequently with brief, all-learner responses (choral response, whiteboards, quick polls) ([Assessment](../elements/assessment.md)).
5. Fade support — move from full worked examples to completion problems to independent problems ([Fading](../elements/fading.md)).
6. Extend to independent application and spaced review to build [Automaticity](../elements/automaticity.md).

## Related Strategies
- [Worked Examples](worked-examples.md) — the problem-solving form of the modeling phase
- [Scaffolded Questioning](scaffolded-questioning.md) — the guided-practice counterpart that replaces telling with prompting
- [Spaced Practice](../principles/spaced-practice.md) — the retention mechanism for skills first taught explicitly

## Examples
- **Engelmann's Direct Instruction (DI)** programs (e.g., *Reading Mastery*) — scripted, fast-paced lessons with choral responding and continuous assessment; strong effects in Project Follow Through.
- **Reciprocal Teaching** (Palincsar & Brown) — the teacher explicitly models predicting, questioning, clarifying, and summarizing before students lead.
- **[Khan Academy](https://www.khanacademy.org)** — narrated video demonstrations followed by hint-supported practice, enacting the model–guide–release sequence asynchronously.
- **Explicit phonics programs** such as [Sounds-Write](https://www.sounds-write.co.uk) — direct modeling of grapheme–phoneme correspondences with immediate guided blending practice.

## Key Sources
- Rosenshine, B. (2012). Principles of instruction: Research-based strategies that all teachers should know. *American Educator, 36*(1), 12–19.
- Hattie, J. (2009). *Visible Learning: A Synthesis of Over 800 Meta-Analyses Relating to Achievement*. Routledge. [doi:10.4324/9780203887332](https://doi.org/10.4324/9780203887332)
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Archer, A. L., & Hughes, C. A. (2011). *Explicit Instruction: Effective and Efficient Teaching*. Guilford Press.