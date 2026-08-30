---
type: strategy
title: Whole Task Practice
description: Learners practice complete, authentic versions of the target task from the start, rather than isolated subskills practiced separately before being combined.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Whole Task Practice

## Description
Whole task practice asks learners to work on integrated, realistic versions of the target task from the beginning of instruction, rather than first mastering isolated components and combining them later. Complexity is managed by sequencing simple-to-complex whole tasks (task classes) and providing [Scaffolding](../elements/scaffolding.md) within each task, not by fragmenting the task into decontextualized drills. This is the organizing principle of the learning-task component in [Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md).

## Design Implications

Whole task practice supports schema construction by letting learners experience how components interact in context, which part-task training tends to miss [~M]. It also builds coordination and conditional knowledge — knowing *when* and *why* to apply a skill, not just *how* — that isolated drills rarely develop [+M]. The central design problem is cognitive load: full tasks can overwhelm novices, so early tasks must be simplified (not fragmented) and supported [Cognitive overload degrades learning outcomes.](../claims/cognitive-overload-degrades-learning.md) [-S].

### Context
#### Requirements
- A task analysis identifying the constituent skills and their interactions
- A set of authentic tasks ordered into simple-to-complex task classes, each still a *whole* task
- Supportive information (mental models, strategies) and just-in-time procedural information available during task performance
- [Scaffolding](../elements/scaffolding.md) that fades within each task class as learners progress ([Fading](../elements/fading.md))

#### Constraints
- Unsequenced or overly complex whole tasks overload novices; simplification is essential, and without it performance and learning suffer [Cognitive overload degrades learning outcomes.](../claims/cognitive-overload-degrades-learning.md) [-S]
- For tasks with highly automated subskills (e.g., phonics, arithmetic facts), some part-task or isolated drill is more efficient before integration [~S] — whole-task-only approaches can leave fluency gaps
- Whole tasks are resource-intensive: designing, assessing, and providing feedback on authentic performance costs more time than drill-based sequences
- Learners with very low prior knowledge may flounder without strong scaffolds or an initial [Demonstration](../elements/demonstration.md) of the whole task

#### Implementation Variability
- **Task-class sequencing (4C/ID):** multiple whole tasks per class, increasing complexity across classes while fading support within each
- **Case-based whole tasks:** [Case Studies](../elements/case-studies.md) or simulations as the vehicle for integrated practice in ill-structured domains
- **Hybrid sequencing:** brief part-task fluency work on automated subskills embedded within a predominantly whole-task sequence
- **Problem-based variants:** whole problems as the driver, with learners working in groups supported by facilitation

### Target Learners
- Learners who must integrate multiple skills in realistic settings (professionals, complex domains) [Case-based learning improves exam performance in complex domains.](../claims/case-based-learning-improves-exam-performance.md) [+M]
- Learners who already have partial component skills and need coordination and conditional knowledge
- Complete novices benefit only when early tasks are heavily simplified and scaffolded [Cognitive overload degrades learning outcomes.](../claims/cognitive-overload-degrades-learning.md) [~M]

### Target Learning Goals
- Integrated skill performance: coordinating multiple component skills on authentic tasks
- Transfer: applying skills to novel, varied situations through practice on varied whole tasks [Comparing and contrasting cases improves learning and transfer.](../claims/comparing-contrasting-cases-improves-learning.md) [+M]
- Conditional knowledge: recognizing which strategy applies when

### Instructions
1. Analyze the target task into constituent skills and identify which subskills require automation versus integration.
2. Design a set of whole tasks within the first, simplest task class — each task complete but simplified in complexity.
3. Open the sequence with a [Demonstration](../elements/demonstration.md) or worked model of a whole task so learners see expert coordination before performing.
4. Have learners perform whole tasks with [Scaffolding](../elements/scaffolding.md) (performance constraints, prompts, checklists), fading support across tasks within the class ([Fading](../elements/fading.md)).
5. Provide [Practice](../elements/practice.md) on multiple varied tasks per class, then move to the next complexity class; embed brief part-task drills only for subskills that need automation.

## Related Strategies
- [Part-Task Practice](../elements/part-task-practice.md) — the complementary strategy for automating subskills; whole task practice provides integration, part-task practice provides fluency
- [Worked Examples](worked-examples.md) — a low-load way to expose learners to whole tasks before independent performance
- [Case-Based Learning](case-based-learning.md) — whole-task practice applied to ill-structured, case-anchored domains

## Examples
- **4C/ID implementations in medical education** — students perform simplified but complete patient consultations from early training, with complexity increasing across task classes (see [Open Universiteit 4C/ID resources](https://www.4cid.org)).
- **Project Lead The Way** ([pltw.org](https://www.pltw.org)) — K-12 engineering units in which students design and build complete artifacts from the first activity, with scaffolds for component skills.
- **Driver education** — learners drive real (simplified) routes from early lessons with an instructor handling or prompting subskills, rather than mastering steering, signaling, and observation separately before ever driving.

## Key Sources
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten steps to complex learning* (3rd ed.). Routledge. [doi:10.4324/9781315116874](https://doi.org/10.4324/9781315116874)
- van Merriënboer, J. J. G., Clark, R. E., & de Croock, M. B. M. (2002). Blueprints for complex learning: The 4C/ID-model. *Educational Technology Research and Development, 50*(2), 39–64. [doi:10.1007/BF02504993](https://doi.org/10.1007/BF02504993)
- van Merriënboer, J. J. G., Kester, L., & Paas, F. (2006). Teaching complex rather than simple tasks: Balancing intrinsic and extraneous load. *Psychological Research, 70*(5), 333–342. [doi:10.1007/s00426-005-0228-0](https://doi.org/10.1007/s00426-005-0228-0)
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review, 31*(2), 261–292. [doi:10.1007/s10648-019-09465-5](https://doi.org/10.1007/s10648-019-09465-5)