---
type: strategy
id: simulations
title: Simulations
description: Simulations use electronic or software-based activities to simulate a real-world situation to which a learner must react, allowing safe practice and consequence exploration.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Simulations

> **Strategy** · [All strategies](index.md)

## Description
Simulations use electronic or software-based activities to model a real-world situation to which a learner must react — operating equipment, managing a patient, negotiating with a customer, or responding to a system failure. Learners practice skills, make decisions, and experience the consequences of mistakes in a safe environment. Long established in aviation and healthcare, simulation-based training is spreading across industries as AI and VR lower the cost of realistic scenario generation.

## Design Implications

Simulation works because it lets learners practice whole tasks with realistic decision consequences, which supports transfer better than isolated skill drills [Whole-task practice supports transfer to real performance.](../claims/whole-task-performance-improves-transfer.md) [+M]. Its effectiveness depends heavily on structured [debriefing](../elements/debriefing.md) and [feedback](../elements/provide-feedback.md): simulation alone produces modest gains, but simulation plus guided reflection produces large ones [Simulation-based education with deliberate practice and feedback outperforms no intervention.](https://doi.org/10.1001/jama.2011.1234) [+S]. Fidelity should be matched to the learning goal — physical realism matters less than functional and psychological realism (do the decisions and consequences behave like the real task?).

### Context
#### Requirements
- A device and software capable of running the simulation, with scenario logic that responds meaningfully to learner decisions
- A facilitator or system that guides the learning process and delivers [feedback](../elements/provide-feedback.md) on decisions
- A structured debriefing step in which learners examine what they did, why, and what consequences followed
- Scenario design that maps decisions to realistic consequences ([Problem Scenario](../elements/problem-scenario.md))

#### Constraints
- High development and maintenance cost; low-fidelity or poorly modeled scenarios can teach wrong mental models [-M]
- Excessive physical fidelity can consume working memory on surface features rather than the underlying decision structure [Managing extraneous load is essential for effective learning.](../principles/cognitive-load-management.md) [~M]
- Without debriefing, learners may enjoy the experience but extract little transferable learning [Simulation without structured debriefing yields weaker outcomes.](https://doi.org/10.1097/SIH.0b013e3180315539) [-M]
- Complex whole-task simulations can overwhelm novices; starting with [part-task practice](../elements/part-task-practice.md) reduces load for them [Part-task practice reduces cognitive load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [+M]

#### Implementation Variability
- Screen-based branching scenarios (e.g., decision trees) — low cost, good for procedural and judgment skills
- Immersive VR/AR — high presence, useful where spatial or equipment familiarity matters
- Human-in-the-loop simulation with actors or instructors (standardized patients, flight instructors) — adds social and communication skill practice
- AI-driven conversational simulations — adaptive scenario branching tailored to the learner's own work context

### Target Learners
- Employees at all levels in corporate training settings, especially those preparing for high-stakes or infrequent events (emergencies, difficult conversations, system failures)
- Novices benefit from simplified, part-task versions before full-complexity scenarios [Part-task practice reduces cognitive load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [+M]
- Experienced practitioners benefit most from rare, high-consequence scenarios and [coaching](../elements/coaching.md) during replay

### Target Learning Goals
- Procedural and psychomotor skill acquisition under realistic conditions
- Decision-making: understanding the consequences of different choices ([Decision-Making](../elements/decision-making.md))
- Team coordination and crisis resource management
- Transfer of classroom knowledge to applied performance ([Application](../elements/application.md))

### Instructions
1. Define the target performance and the decisions it requires; design a [Problem Scenario](../elements/problem-scenario.md) whose branches map to realistic consequences.
2. Brief learners on their role and objectives, then let them [Practice](../elements/practice.md) by making decisions in the simulation ([Decision-Making](../elements/decision-making.md)).
3. Track learner decisions and provide immediate or post-hoc [feedback](../elements/provide-feedback.md) tied to consequences.
4. Run a structured debrief: replay key moments, ask learners to explain their reasoning ([self-explanation improves conceptual understanding](../claims/self-explanation-improves-conceptual-understanding.md) [+M]).
5. Increase scenario complexity or fade support across repetitions as competence grows [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].

## Related Strategies
- [Case-based learning](../patterns/case-based-learning.md) — simulations are interactive, consequential cases; cases are reflective, pre-resolved ones
- [Role-play](../strategies/role-play.md) — human-performed simulation without software mediation
- [Scenario-based e-learning](../strategies/scenario-based_e-learning.md) — lighter-weight branching simulations

## Related Elements
- [Practice](../elements/practice.md) — the core activity the simulation hosts
- [Provide Feedback](../elements/provide-feedback.md) — consequence feedback is what converts play into learning
- [Problem Scenario](../elements/problem-scenario.md) — the scenario structure that defines decision points
- [Decision-Making](../elements/decision-making.md) — the primary cognitive skill simulations exercise
- [Coaching](../elements/coaching.md) — facilitator guidance during and after runs

## Examples
- **[FlightSafety International](https://www.flightsafety.com)** — full-motion flight simulators with instructor-led scenario replay and debriefing; the canonical high-fidelity example.
- **[Laerdal SimCenter](https://www.laerdal.com)** — patient simulators and scenario platforms used in nursing and medical education with standardized debriefing protocols.
- **[CapsimInbox](https://www.capsim.com)** — inbox-style business simulations where learners manage a simulated company and see financial and team consequences of decisions.
- **[Mursion](https://www.mursion.com)** — VR simulations with human-powered avatars for practicing difficult workplace conversations.

## Key Sources
- Cook, D. A., Hatala, R., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Barsuk, J. H. (2011). Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. *JAMA, 306*(9), 978–988. [doi:10.1001/jama.2011.1234](https://doi.org/10.1001/jama.2011.1234)
- Sitzmann, T. (2011). A meta-analytic examination of the instructional effectiveness of computer-based simulation environments. *Personnel Psychology, 64*(2), 489-528. [doi:10.1111/j.1744-6570.2011.01190.x](https://doi.org/10.1111/j.1744-6570.2011.01190.x)
- Fanning, R. M., & Gaba, D. M. (2007). The role of debriefing in simulation-based learning. *Simulation in Healthcare, 2*(2), 115–125. [doi:10.1097/SIH.0b013e3180315539](https://doi.org/10.1097/SIH.0b013e3180315539)
- Gaba, D. M. (2004). The future vision of simulation in health care. *Quality and Safety in Health Care, 13*(suppl 1), i2–i10. [doi:10.1136/qshc.2004.009878](https://doi.org/10.1136/qshc.2004.009878)