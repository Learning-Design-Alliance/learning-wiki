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
> **Evidence** · 18 claims (14 for, 3 mixed, 1 against) · 20 studies (8 quant-synthesis, 7 causal, 3 review, 1 qualitative, 1 design), `q2`–`q4` · 8 of 20 report an effect size · 9 claims rest on one study

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

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [Minimal guidance is less effective for novices than explicit instruction](../claims/minimal-guidance-less-effective-for-novices.md) [+S]
- [Guided discovery outperforms pure discovery](../claims/guided-discovery-outperforms-pure-discovery.md) [+S]
- [Teacher-guided inquiry outperforms student-led](../claims/teacher-guided-inquiry-outperforms-student-led.md) [+S]
- [Expertise reversal: guidance hurts experts](../claims/expertise-reversal-guidance-hurts-experts.md) [~S]
- [Simulation-based education with deliberate practice improves clinical outcomes](../claims/simulation-based-education-with-deliberate-practice-improves-clinical-outcomes.md) [+M]
- [Simulation-based education improves outcomes](../claims/simulation-based-education-improves-outcomes.md) [+M]
- [Physical experience enhances science learning](../claims/physical-experience-enhances-science-learning.md) [~M]
- [Virtual simulation stimulated higher self-reported purposefulness than authentic video](../claims/vs-higher-purposefulness-reflection.md) [+M]
- [Authentic video outperformed virtual simulation on analysis and support dimensions](../claims/av-advantage-analysis-support-dimensions.md) [-M]
- [Pretraining improves transfer](../claims/pretraining-improves-transfer.md) [+M]
- [Feedback improves learning](../claims/feedback-improves-learning.md) [+S]
- [Students find computer-based simulation feedback insufficient](../claims/simucase-feedback-insufficient.md) [+M]
- [Graduate SLP students perceive the simulation's learning mode as highly beneficial](../claims/simucase-learning-mode-perceived-beneficial.md) [+M]
- [Reflective practice improves outcomes when structured](../claims/reflective-practice-improves-outcomes-when-structured.md) [+S]
- [Students perceive debriefing as among the most beneficial components of a simulated clinical course](../claims/debriefing-psychometric-instruction-valued.md) [+M]

## Design Decisions
<!-- Decision section (2026-09-30 pilot): drafted from the linked claim pages only; every choice
     cites the claims that settle it, with markers capped by each claim's recorded evidence. -->

### How much guidance should learners get inside the simulation?
- **Default:** give novices structure — goals, prompts, feedback, worked examples — rather than leaving them to discover the model's rules unaided; explicit instruction beat unassisted discovery (d = 0.38, 580 comparisons), while discovery enhanced with feedback, worked examples or scaffolding beat other instruction (d = 0.30) — [Minimal guidance is less effective for novices than explicit instruction](../claims/minimal-guidance-less-effective-for-novices.md) [+S], [Guided discovery outperforms pure discovery](../claims/guided-discovery-outperforms-pure-discovery.md) [+S]
- **Default:** in inquiry settings, teacher-led guidance outperformed student-led conditions by about .40 in effect size (37 studies, overall g = .50) — [Teacher-guided inquiry outperforms student-led](../claims/teacher-guided-inquiry-outperforms-student-led.md) [+S]
- **Changes when:** learners already hold the relevant schemas → fade the guidance; formats that help novices lost their advantage, and in several paradigms reversed, for more experienced learners — [Expertise reversal: guidance hurts experts](../claims/expertise-reversal-guidance-hurts-experts.md) [~S]
- **Tested with:** meta-analyses of discovery and inquiry learning (largely school science), 112 third- and fourth-graders learning experimental design, electrical trainees reading circuit diagrams; none of these claims tests guidance levels inside a simulation specifically.
- **Not settled:** how fast to fade guidance within a simulation, and whether the discovery findings carry over unchanged to interactive models; no wiki claim tests it.

### What should the simulation be built around?
- **Default:** repeated, goal-directed practice with mastery standards and immediate feedback; simulation-based medical education with deliberate practice beat traditional clinical education (d = 0.71, 14 studies, mostly procedural skills) — [Simulation-based education with deliberate practice improves clinical outcomes](../claims/simulation-based-education-with-deliberate-practice-improves-clinical-outcomes.md) [+M]
- **Default:** against no intervention, technology-enhanced simulation gave large pooled effects on knowledge and skills (g ≈ 1.09–1.20) and a moderate one on direct patient outcomes (g = 0.50, k = 32) — [Simulation-based education improves outcomes](../claims/simulation-based-education-improves-outcomes.md) [+M]
- **Changes when:** the comparison is equally long non-simulation practice → the no-intervention meta-analysis cannot say, and its subgroup analyses found no consistent interaction with feedback, repetition, mastery learning, distributed practice or curricular integration — [Simulation-based education improves outcomes](../claims/simulation-based-education-improves-outcomes.md) [~M]
- **Tested with:** physicians, nurses, dentists and other health-professions trainees (609 studies, 35,226 trainees; 14 studies for the deliberate-practice comparison).
- **Not settled:** which design features drive the effect, how durable gains are, dose–response for amount of practice, and cost against low-fidelity alternatives; both claim pages list these as open.

### How realistic does the simulation need to be?
- **Default:** a virtual model can stand in for physical materials for conceptual learning; physical, virtual and combined manipulation of heat-and-temperature experiments were equally effective and all beat traditional instruction — [Physical experience enhances science learning](../claims/physical-experience-enhances-science-learning.md) [~M]
- **Changes when:** the goal is reflecting on the situation → a simplified virtual simulation gave higher self-reported purposefulness of reflection than authentic video (d = 0.507) — [Virtual simulation stimulated higher self-reported purposefulness than authentic video](../claims/vs-higher-purposefulness-reflection.md) [+M]
- **Changes when:** the goal is analysing rich real situations → authentic video outscored the simplified simulation on the analysis and support dimensions of observation assignments — [Authentic video outperformed virtual simulation on analysis and support dimensions](../claims/av-advantage-analysis-support-dimensions.md) [-M]
- **Tested with:** 234 undergraduates in physics (physical vs virtual); 34 preschool teacher candidates in 8 groups in one design-based study (simulation vs video), which is one small study.
- **Not settled:** fidelity levels in procedural or clinical simulation; no wiki claim compares high- and low-fidelity versions of the same simulation, so the Constraints line above on fidelity cost rests on no recorded study.

### What should learners get before the simulation?
- **Default:** a short primer naming the parts and functions of the system; a pretraining video before an immersive-VR procedural lesson gave better knowledge scores and fewer errors on a real-world transfer task, with lower reported load — [Pretraining improves transfer](../claims/pretraining-improves-transfer.md) [+M]
- **Tested with:** 93 participants learning a micropipette procedure in VR; one randomised experiment, read as an abstract, no effect size.
- **Not settled:** whether pretraining is redundant for learners who already know the terms (the claim page expects so but records no test), and whether gains last to delayed tests.

### What feedback should the simulation itself give?
- **Default:** say why a response is wrong, not only that it is; high-information feedback (d = 0.99) far outperformed reinforcement or punishment (d = 0.24), and over a third of feedback interventions lowered performance — [Feedback improves learning](../claims/feedback-improves-learning.md) [+S]
- **Default:** students in a computer-based clinical simulation found right/wrong marking without reasoning not beneficial — [Students find computer-based simulation feedback insufficient](../claims/simucase-feedback-insufficient.md) [+M]
- **Default:** let learners retry cases without grade penalty; students rated an unlimited-attempts learning mode highly beneficial — [Graduate SLP students perceive the simulation's learning mode as highly beneficial](../claims/simucase-learning-mode-perceived-beneficial.md) [+M]
- **Tested with:** 435 education studies and 607 effect sizes across settings (feedback); 10 speech-language pathology graduate students in one focus-group pilot (the two simulation claims, which report perceptions, not learning).
- **Not settled:** immediate versus end-of-scenario feedback inside a simulation; no wiki claim tests it.

### What should follow the simulation?
- **Default:** a structured reflection with specific prompts rather than a generic invitation; metacognitive-reflection prompts were the strongest moderator in 48 writing-to-learn studies (b = 0.48), and specific prompts beat generic ones for 208 engineering students — [Reflective practice improves outcomes when structured](../claims/reflective-practice-improves-outcomes-when-structured.md) [+S]
- **Default:** students in a simulated clinical course named the weekly debriefing among its most beneficial parts — [Students perceive debriefing as among the most beneficial components of a simulated clinical course](../claims/debriefing-psychometric-instruction-valued.md) [+M]
- **Tested with:** school writing-to-learn studies and a first-year engineering course (structured reflection); 10 SLP graduate students (debriefing, perception only).
- **Not settled:** no wiki claim compares a simulation with and without a debrief; see [Debrief](debrief.md) for the debrief's own decisions.

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
- [Embed puzzles and challenges in simulations for continued engagement and self-assessment](../strategies/embed-puzzles-and-challenges-in-sims.md)
- [Use simulation as a non-threatening alternative to direct experimentation when testing office reorganizations](../strategies/simulation-as-non-threatening-experimentation-alternative.md)

## Key Sources
- Garris, R., Ahlers, R., & Driskell, J. E. (2002). Games, motivation, and learning: A research and practice model. *Simulation & Gaming, 33*(4), 441–467. [doi:10.1177/1046878102238607](https://doi.org/10.1177/1046878102238607)
- Finkelstein, N. D., Adams, W. K., Keller, C. J., Kohl, P. B., Perkins, K. K., Podolefsky, N. S., Reid, S., & LeMaster, R. (2005). When learning about the real world is better done virtually: A study of substituting computer simulations for laboratory equipment. *Physical Review Special Topics — Physics Education Research, 1*(1), 010101. [doi:10.1103/physrevstper.1.010103](https://doi.org/10.1103/physrevstper.1.010103)
- Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work: An analysis of the failure of constructivist, discovery, problem-based, experiential, and inquiry-based teaching. *Educational Psychologist, 41*(2), 75–86. [doi:10.1207/s15326985ep4102_1](https://doi.org/10.1207/s15326985ep4102_1)
- Issenberg, S. B., McGaghie, W. C., Petrusa, E. R., Lee Gordon, D., & Scalese, R. J. (2005). Features and uses of high-fidelity medical simulations that lead to effective learning: A BEME systematic review. *Medical Teacher, 27*(1), 10–28. [doi:10.1080/01421590500046924](https://doi.org/10.1080/01421590500046924)
- Wouters, P., van Nimwegen, C., van Oostendorp, H., & van der Spek, E. D. (2013). A meta-analysis of the cognitive and motivational effects of serious games. *Journal of Educational Psychology, 105*(2), 249–265. [doi:10.1037/a0031311](https://doi.org/10.1037/a0031311)