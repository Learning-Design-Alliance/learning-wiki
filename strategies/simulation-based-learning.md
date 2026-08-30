---
type: strategy
title: Simulation Based Learning
description: Learners practice skills in an interactive, modeled environment that approximates a real task, receiving feedback on their performance without real-world stakes.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Simulation Based Learning

## Description
Simulation based learning places learners inside an interactive model of a real task, environment, or system — a flight simulator, a standardized patient, a business game, a virtual lab — where they make decisions, act, and observe consequences without real-world risk. It is carried out through cycles of scenario engagement, feedback, and often structured debriefing, in which the simulated experience is reviewed and connected to underlying principles.

## Design Implications

Simulation works because it lets learners generate and test hypotheses in an environment that responds like the real system, combining [Active Learning](../principles/active-learning.md) with safe failure. Its effectiveness depends heavily on deliberate design: simulation without structured debriefing produces far weaker learning than simulation plus debriefing, and feedback during or after the scenario is one of the strongest moderators of outcomes [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]. Fidelity — how closely the simulation matches reality — matters less than instructional alignment; high physical fidelity with poor pedagogy underperforms low-fidelity simulations with good feedback and debriefing [~M].

### Context
#### Requirements
- A scenario model that responds meaningfully to learner actions, with the critical variables of the target task represented
- Embedded or post-hoc feedback tied to learner decisions, not just outcomes ([Coaching](../elements/coaching.md) during the scenario, debriefing after)
- Structured debriefing that connects the experience to concepts and alternatives — the phase where most durable learning occurs
- Clear performance objectives so the scenario exercises the intended skills rather than generic exploration

#### Constraints
- Unstructured "play" in a simulation yields shallow learning; without debriefing, learners encode surface events rather than transferable principles [-M]
- High cognitive load from complex interfaces can overwhelm novices, who spend capacity operating the simulation rather than learning from it [Part-task practice reduces load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [~M] — simplify or pre-train on controls before full scenarios
- Simulations can teach misrepresentations if the model omits or distorts critical variables; learners may overgeneralize from an artificial context [-W]
- For experts, highly guided simulation can be redundant and inefficient [Guidance benefits shrink or reverse as expertise grows.](../claims/expertise-reversal-effect.md) [~M]

#### Implementation Variability
- **Fidelity spectrum:** from tabletop exercises and role-plays to high-fidelity mannequins and VR; choose fidelity for the learning goal, not realism for its own sake
- **Individual vs. team simulation:** team scenarios (e.g., crisis resource management) add coordination and communication goals
- **Simulator-as-assessment:** the same scenario can be used for summative performance assessment with standardized scoring

### Target Learners
- Novices and intermediates in high-stakes domains (medicine, aviation, engineering) where real practice is dangerous or costly [+S]
- Learners who need procedural fluency and decision-making under time pressure, which cannot be safely rehearsed live
- Less efficient for learners who already perform fluently; at high expertise, simulation time is better spent on real tasks [Guidance benefits shrink or reverse as expertise grows.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Procedural and psychomotor skill acquisition with safe error tolerance
- Decision-making and situation assessment in dynamic, ill-structured scenarios
- Team coordination and communication under pressure
- Transfer of classroom concepts to applied contexts ([Case-Based Learning](../patterns/case-based-learning.md) goals with added interactivity)

### Instructions
1. Define the target performance and the critical decisions the scenario must exercise.
2. Pre-train learners on the interface and any prerequisite subskills to reduce extraneous load ([Cognitive Load Management](../principles/cognitive-load-management.md)).
3. Brief learners on the scenario's purpose and their role, without revealing the specific challenges.
4. Run the scenario with a facilitator [Coaching](../elements/coaching.md) or embedded prompts as needed; allow errors to occur and play out.
5. Debrief with a structured protocol (e.g., plus-delta or advocacy-inquiry): elicit the learner's reasoning, compare it to expert reasoning, and generalize to principles.
6. Repeat with varied scenarios so learners abstract the underlying structure rather than memorizing one scenario ([Multiple contrasting cases support abstraction.](../claims/multiple-contrasting-cases-support-abstraction.md)) [+M].

## Related Strategies
- [Case-Based Learning](case-based-learning.md) — the non-interactive sibling: learners analyze a described case rather than acting inside a simulated one
- [Role Play](acting-role-play.md) — human-only simulation of interpersonal scenarios
- [Game-Based Learning](../principles/game-based-learning.md) — simulations that add explicit game mechanics and scoring

## Examples
- **[Laerdal SimMan](https://www.laerdal.com)** and standardized-patient programs in health professions education — high-fidelity patient simulation with structured debriefing; meta-analytic evidence shows large gains over no simulation and comparable or better outcomes than traditional instruction [Cook et al., 2013](https://doi.org/10.1001/jama.2013.282057) [+S]
- **[Flight simulators](https://www.faa.gov)** (FAA-certified training devices) — the original modern simulation context; instrument procedures are rehearsed to proficiency before live flight
- **[Harvard Business School Publishing simulations](https://www.hbsp.harvard.edu)** — business simulations (e.g., *Change Management*, *Operations Management*) where learners run a virtual organization and debrief against management theory
- **[PhET Interactive Simulations](https://phet.colorado.edu)** — low-fidelity science simulations for physics and chemistry concepts, effective when paired with guided inquiry activities [~M]

## Key Sources
- Cook, D. A., Hamstra, S. J., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Hatala, R. (2013). Comparative effectiveness of instructional design features in simulation-based education: Systematic review and meta-analysis. *Medical Teacher, 35*(1), e867–e898. [doi:10.3109/0142159x.2012.714886](https://doi.org/10.3109/0142159x.2012.714886)
- Cook, D. A., Hatala, R., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Hamstra, S. J. (2013). Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. *JAMA, 310*(9), 978–988. [doi:10.1001/jama.2013.282057](https://doi.org/10.1001/jama.2013.282057)
- Gaba, D. M. (2004). The future vision of simulation in health care. *Quality and Safety in Health Care, 13*(suppl 1), i2–i10. [doi:10.1136/qshc.2004.009878](https://doi.org/10.1136/qshc.2004.009878)
- Sitzmann, T. (2011). A meta-analytic examination of the instructional effectiveness of computer-based simulation environments. *Personnel Psychology, 64*(2), 489–528. [doi:10.1111/j.1744-6570.2011.01190.x](https://doi.org/10.1111/j.1744-6570.2011.01190.x)