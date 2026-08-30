---
type: strategy
title: Explicit Teaching
description: The teacher clearly shows students what to do and how to do it, making learning intentions and success criteria transparent, modelling the target performance, checking for understanding, and consolidating at the close of each lesson.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Explicit Teaching

## Description
Explicit teaching is a structured approach in which the teacher decides on the learning intentions and success criteria, makes them transparent to students, and demonstrates the target skill or concept through modelling. Instruction proceeds through showing and explaining, guided practice with checks for understanding, and a closing segment that revisits and ties together what was covered. It is the practical enactment of teacher-led, fully guided instruction rather than discovery-oriented learning.

## Design Implications

Explicit teaching reduces ambiguity about what success looks like and lowers the working-memory burden of unguided search, consistent with evidence that fully guided instruction benefits novices more than minimal-guidance approaches [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M] and that cognitive overload degrades learning when learners must simultaneously discover content and learn it [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S]. Its effectiveness depends on active processing during and after modelling: explanation alone, without checking for understanding and student practice, produces shallow engagement [Active learning improves exam performance.](../claims/active-learning-improves-exam-performance.md) [+S].

### Context
#### Requirements
- Clearly defined learning intentions and success criteria, communicated in learner-accessible language
- Modelling of the desired outcome — thinking made visible, not just the end product (see [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md))
- Frequent checks for understanding (questioning, brief [check-ins](../elements/check-in.md)) with reteaching when understanding is incomplete
- Guided then independent practice opportunities within and across lessons
- Lesson closure that revisits and consolidates the content

#### Constraints
- Purely didactic delivery without student activity is less effective than explicit teaching interleaved with practice and discussion [Active learning improves exam performance.](../claims/active-learning-improves-exam-performance.md) [-S]
- Overly detailed explanation can become redundant for learners with strong prior knowledge, reducing its benefit [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
- Modelling a single method can anchor learners to one approach; contrasting cases mitigate this [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+M]
- If success criteria are vague or purely procedural, students learn to comply rather than to understand the underlying concepts

#### Implementation Variability
- Vary the level of support and modelling by student need — more scaffolding for novices, faded models as competence grows
- Whole-class explicit teaching can be combined with subsequent collaborative or independent work
- In digital environments, explicit teaching takes the form of narrated demonstrations, worked examples, and adaptive hints

### Target Learners
- Novices and learners with limited prior knowledge, who benefit most from fully guided instruction [Worked examples reduce unnecessary search for novices.](../claims/worked-examples-reduce-novice-search.md) [+M]
- All learner levels, with the degree of guidance adjusted downward as expertise develops [Worked-example guidance becomes less effective as learner expertise increases.](../claims/worked-examples-less-effective-with-expertise.md) [~M]
- Learners who benefit from reduced ambiguity, including those with attention or language-processing needs

### Target Learning Goals
- Procedural skill acquisition and accurate execution of defined processes
- Conceptual understanding built through clear explanation and modelling
- Metacognitive awareness of what quality performance looks like (success criteria)

### Instructions
1. Set the learning intention and success criteria; state them in student-friendly language and post them visibly (an [advance organizer](../claims/advance-organizers-improve-learning.md) [+M] for the lesson).
2. Model the target skill or concept, narrating decisions aloud so reasoning is observable — the modelling phase of [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md).
3. Check for understanding through targeted questioning or brief [check-ins](../elements/check-in.md); reteach immediately where understanding is incomplete.
4. Move to guided practice, then independent practice, fading support as competence grows.
5. Close the lesson by revisiting what was covered and connecting it to the success criteria and prior learning.

## Related Strategies
- [Direct Instruction](../patterns/direct-instruction.md) — the highly scripted pattern that explicit teaching generalizes from
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — situates modelling within a broader modelling–coaching–fading sequence
- [4C/ID Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md) — embeds explicit supportive information within whole learning tasks

## Examples
- **Explicit Direct Instruction (EDI)** — a widely implemented lesson structure (activate prior knowledge → explain → model → guided practice → closure) used across thousands of schools; see [DataWORKS Educational Research](https://dataworks-ed.com/about-explicit-direct-instruction/).
- **Rosenshine's Principles of Instruction** — a research synthesis translating effective explicit teaching into ten classroom principles, including daily review, modelling, and checks for understanding ([AFSA](https://www.aft.org/sites/default/files/periodicals/Rosenshine.pdf)).
- **Khan Academy** — narrated video modelling of problem solving followed by practice with on-demand hints, an online analogue of the model–check–practice cycle.

## Key Sources
- Rosenshine, B. (2012). Principles of instruction: Research-based strategies that all teachers should know. *American Educator, 36*(1), 12–19.
- Hattie, J. (2009). *Visible learning: A synthesis of over 800 meta-analyses relating to achievement*. Routledge. [doi:10.4324/9780203887332](https://doi.org/10.4324/9780203887332)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for problem solving in learning algebra. *Cognition and Instruction, 2*(1), 59–89. [doi:10.1207/s1532690xci0201_3](https://doi.org/10.1207/s1532690xci0201_3)
- Freeman, S., et al. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)