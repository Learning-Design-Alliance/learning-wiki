---
type: element
id: simulation
title: Simulation
description: A simulation is an interactive model of a system or environment in which learners act, observe consequences, and iterate, learning through controlled experimentation rather than direct instruction.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Simulation

> **Element** · [All elements](index.md)

## Description
A simulation is an interactive model of a real or hypothetical system — physical, biological, economic, social, or procedural — in which learners take actions, observe the consequences, and adjust their approach. Unlike a [Demonstration](demonstration.md), which presents expert performance for observation, a simulation makes the learner the actor, embedding practice inside a simplified environment where errors are safe and consequences are visible.

## Design Implications

Simulations support learning by making system dynamics explorable: learners build causal mental models by manipulating variables and observing outcomes, which is difficult to convey through exposition alone [~M]. Their effectiveness depends on structure — unguided exploration of a complex simulation can overwhelm novices, so effective designs pair the environment with goals, prompts, or [Scaffolding](scaffolding.md) [~S]. Simulations are most powerful when followed by debriefing, in which learners articulate what happened and why; without debriefing, experience alone often fails to produce transferable understanding [~M].

### Context
#### Requirements
- A model whose behavior is faithful enough to the target system that inferences from it transfer
- Clear goals or challenge scenarios that direct exploration toward the learning objective
- Feedback that makes the link between actions and outcomes visible ([Feedback](feedback.md))
- A structured debrief or reflection step that converts experience into generalizable principles

#### Constraints
- Unguided discovery within a simulation is ineffective for novices; minimal-guidance exploration produces poorer learning than structured instruction [~S] — learners may draw wrong conclusions from the model or flounder without building usable schemas
- Simulations of complex systems can impose heavy extraneous load; without [Cognitive Load Management](../principles/cognitive-load-management.md), learners attend to interface mechanics rather than underlying principles
- A simplified model can teach misconceptions if its divergences from reality are not made explicit
- Fidelity costs: high-fidelity simulations are expensive to build and maintain, and added fidelity does not reliably improve learning outcomes [~W]

### Target Learners
- Novices who need to build an initial causal model of a system before formal instruction [~M]
- Intermediate learners consolidating and testing understanding through experimentation
- Learners for whom real-world practice is dangerous, expensive, slow, or ethically impossible (e.g., flight, surgery, emergency response)
- Less beneficial for learners with strong prior knowledge, who may extract little from guided exploration [Expertise reverses the benefit of instructional guidance.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Conceptual understanding of dynamic systems and causal relationships
- Procedural fluency and decision-making under realistic constraints
- Transfer: applying principles across varied scenarios by experiencing multiple cases
- Diagnosis and troubleshooting: interpreting system states and responding

### Affordances
- [Active Learning](../principles/active-learning.md) — simulation enacts this principle by requiring learners to generate actions and predictions rather than receive explanations; the environment responds to what the learner does, not what the learner is told
- [Scaffolding](../principles/scaffolding.md) — simulations can stage complexity, starting with few variables and adding them as competence grows; [Fading](fading.md) applies naturally by progressively removing hints, prompts, and constraints
- [Cognitive Load Management](../principles/cognitive-load-management.md) — a well-designed simulation strips away irrelevant real-world complexity, letting learners attend to the variables that matter
- [Feedback](feedback.md) — the simulation's response to learner actions is immediate, task-level feedback; effectiveness rises when debriefing elevates it to the process level [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]

## Related Elements
- [Practice](practice.md) — simulation is a structured environment for deliberate practice with built-in consequences
- [Case Studies](case-studies.md) — a case presents a snapshot of a system; a simulation lets learners intervene in it
- [Coaching](coaching.md) — instructor or system guidance during simulation attempts
- [Fading](fading.md) — progressively removing scaffolds within the simulation as expertise grows
- [Feedback](feedback.md) — the core mechanism through which simulation actions become learning

## Patterns That Use This Element
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — simulation provides the exploration and articulation phases in a safe environment
- [Case-Based Learning](../patterns/case-based-learning.md) — interactive cases extend static cases into consequential decision-making [Case-based learning improves exam performance.](../claims/case-based-learning-improves-exam-performance.md) [+M]
- [Anchored Instruction](../patterns/anchored-instruction.md) — simulations serve as the anchor problem context in which knowledge is applied

## Examples

**[PhET Interactive Simulations](https://phet.colorado.edu)** — Research-based physics, chemistry, and math simulations (e.g., *Circuit Construction Kit*) with guided-inquiry activity sheets; studies show conceptually targeted sims outperform real equipment demonstrations for building circuit understanding.

**[SimSchool](https://simschool.org)** — A classroom simulation in which teacher candidates practice instructional decisions and see simulated student responses, bridging coursework and live teaching.

**[Flight simulators](https://www.faa.gov/about/office_org/headquarters_offices/avs/offices/afs/afs200)** — The canonical high-fidelity example; FAA-approved simulators substitute for substantial flight hours, illustrating how simulation enables safe practice of high-stakes procedures.

**[NetLogo](https://ccl.northwestern.edu/netlogo)** — Agent-based modeling environment used in science education for learners to build and perturb models of complex systems (epidemics, ecosystems), supporting exploration of emergent behavior.

## Key Sources
- Garris, R., Ahlers, R., & Driskell, J. E. (2002). Games, motivation, and learning: A research and practice model. *Simulation & Gaming, 33*(4), 441–467. [doi:10.1177/1046878102238607](https://doi.org/10.1177/1046878102238607)
- Finkelstein, N. D., Adams, W. K., Keller, C. J., Kohl, P. B., Perkins, K. K., Podolefsky, N. S., Reid, S., & LeMaster, R. (2005). When learning about the real world is better done virtually: A study of substituting computer simulations for laboratory equipment. *Physical Review Special Topics — Physics Education Research, 1*(1), 010101. [doi:10.1103/physrevstper.1.010103](https://doi.org/10.1103/physrevstper.1.010103)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Issenberg, S. B., McGaghie, W. C., Petrusa, E. R., Lee Gordon, D., & Scalese, R. J. (2005). Features and uses of high-fidelity medical simulations that lead to effective learning: A BEME systematic review. *Medical Teacher, 27*(1), 10–28. [doi:10.1080/01421590500046924](https://doi.org/10.1080/01421590500046924)
- Wouters, P., van Nimwegen, C., van Oostendorp, H., & van der Spek, E. D. (2013). A meta-analysis of the cognitive and motivational effects of serious games. *Journal of Educational Psychology, 105*(2), 249–265. [doi:10.1037/a0031311](https://doi.org/10.1037/a0031311)