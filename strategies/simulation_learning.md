---
type: strategy
title: Simulation Learning
description: Simulation learning engages learners in active, role-based experiences that model simplified versions of reality, allowing them to act, see consequences, and learn from each other without real-world risk.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Simulation Learning

> **Strategy** · [All strategies](index.md)

## Description
Simulation learning places learners inside a simplified, interactive model of a real-world system, event, or role, where their decisions produce observable consequences without real-world stakes. Learners take on assigned roles, act within the simulation's rules, and then examine what happened — learning as much from peers' moves and the debriefing as from the instructor. Effective simulations follow a three-phase arc: preparation, active participation, and structured debriefing that connects the experience to course goals.

## Design Implications

Simulations work because they make learners generate decisions and experience their consequences, converting abstract principles into lived cause-and-effect [Active learning improves exam performance relative to lecture alone.](../claims/active-learning-improves-exam-performance.md) [+S]. The learning payoff, however, sits largely in the debrief: without facilitated reflection, participants remember the activity but not the principles it was designed to teach [Debriefing is a critical component of simulation-based education.](https://doi.org/10.2310/6480.2007.00212) [+S]. Because a single scenario is necessarily partial, complex or ill-structured concepts benefit from multiple varied simulations rather than one repeated run [Learning from multiple contrasting cases supports flexible transfer.](../claims/cognitive-flexibility-theory-multiple-cases.md) [+M].

### Context
#### Requirements
- Intensive pre-simulation preparation: aligning the scenario with course goals, reviewing supporting materials, and conducting a trial run
- Active participation structures in which each learner assumes a defined role with real decision authority ([Assigned Positions](../elements/assigned-positions.md))
- Sufficient protected time for post-simulation debriefing, with facilitation that surfaces the reasoning behind moves rather than only outcomes ([Articulation](../elements/articulation.md), [Class Discussion](../elements/class-discussion.md))
- A [Problem Scenario](../elements/problem-scenario.md) whose constraints and feedback loops genuinely mirror the target system

#### Constraints
- Resource-intensive to design and run; poorly aligned scenarios drift from course goals and consume class time without producing the intended learning
- Learners may "game" the simulation or get carried away by play dynamics, requiring instructor redirection [-M]
- Learners who do not prefer experiential or high-visibility participation may disengage or experience the role-play as threatening rather than instructive [~M]
- Without debriefing, the vivid experience can entrench misconceptions as easily as correct models — a memorable wrong lesson is still memorable [-S]
- Novices may lack the schema to interpret simulation feedback, overloading working memory when the scenario is too complex too early [Cognitive overload degrades learning outcomes.](../claims/cognitive-overload-degrades-learning.md) [~M]

#### Implementation Variability
- **Role-play simulations** (negotiations, Model UN, clinical scenarios) emphasize perspective-taking and interpersonal dynamics
- **Computer-based simulations** ([PhET Interactive Simulations](https://phet.colorado.edu), business simulators) allow rapid iteration and parameter exploration with immediate feedback
- **Standardized-patient and virtual-reality simulations** in health professions education provide controlled, repeatable practice of high-stakes procedures
- Complexity, role granularity, and fidelity can be scaled to learner level; simulations can run face-to-face or online and combine with [Cooperative Learning](../patterns/cooperative-learning.md) structures

### Target Learners
- Learners who already hold enough baseline knowledge to interpret scenario feedback; complete novices typically need direct instruction first [~M]
- Professional and pre-professional learners (healthcare, business, teaching, public policy) who must integrate knowledge, decision-making, and interpersonal skill
- Learners developing empathy for stakeholders or positions unlike their own — role assignment forces perspective adoption [Building empathy improves intergroup attitudes.](../claims/building-empathy-improves-intergroup-attitudes.md) [+M]
- Learners motivated by autonomy and agency; simulations satisfy competence and autonomy needs when learners make consequential choices [Autonomy supports intrinsic motivation.](../claims/autonomy-supports-intrinsic-motivation.md) [+M]

### Target Learning Goals
- Applying concepts to dynamic situations where multiple variables interact ([Application of Knowledge](../elements/application-of-knowledge.md))
- Challenging misconceptions by letting learners watch their flawed mental models fail in the simulation [Cognitive disequilibrium motivates conceptual change.](../claims/cognitive-disequilibrium-motivates-conceptual-change.md) [+M]
- Perspective-taking, negotiation, and interpersonal skill development
- Understanding complex systems and emergent, second-order consequences that lectures cannot demonstrate

### Instructions
1. **Prepare.** Align the scenario with course goals, brief learners on roles and rules, and assign positions ([Assigned Positions](../elements/assigned-positions.md), [Problem Scenario](../elements/problem-scenario.md)).
2. **Activate prior knowledge.** Have learners research their role's interests and constraints before the run ([Activation](../elements/activation.md)).
3. **Run the simulation.** Learners act, negotiate, and decide within the scenario's rules, applying course concepts under realistic pressure ([Application of Knowledge](../elements/application-of-knowledge.md), [Act It Out](../elements/act-it-out.md)).
4. **Debrief.** Facilitate structured reflection: what happened, why, what reasoning drove each move, and how outcomes map to course concepts ([Articulation](../elements/articulation.md), [Class Discussion](../elements/class-discussion.md)).
5. **Consolidate and assess.** Connect the experience to the abstract principle; assess via reflection papers, position analyses, or transfer tasks ([Assessment](../elements/assessment.md)).

## Related Strategies
- [Case-Based Learning](case-based-learning.md) — a lower-fidelity cousin: learners analyze a fixed case rather than acting inside a live scenario
- [Role-Play](acting-role-play.md) — the interpersonal subset of simulation, focused on perspective adoption rather than system dynamics
- [Debate](debate.md) — structured adversarial role-taking without a simulated outcome system

## Related Elements
- [Problem Scenario](../elements/problem-scenario.md) — the scenario frame that defines goals, constraints, and feedback
- [Application of Knowledge](../elements/application-of-knowledge.md) — the mechanism by which simulation converts concepts into decisions
- [Articulation](../elements/articulation.md) — the debrief practice that makes tacit reasoning explicit
- [Assigned Positions](../elements/assigned-positions.md) — role structure that distributes participation and forces perspective-taking
- [Case Studies](../elements/case-studies.md) — a common preparation or follow-up material for simulations

## Patterns That Use This Strategy
- [Experiential Learning Cycle](../patterns/experiential-learning-cycle.md) — the simulation is the concrete experience; debriefing is the reflective observation and abstract conceptualization phases
- [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) — simulation provides the exploration and articulation phases in a safe environment
- [Anchored Instruction](../patterns/anchored-instruction.md) — simulations act as rich, problem-dense anchors for subsequent instruction

## Tools
- [PhET Interactive Simulations](https://phet.colorado.edu) — open physics, chemistry, and math simulations with parameter manipulation
- [Harvard Business Publishing Simulations](https://www.harvardbusiness.org) — decision-based business simulations for higher education
- [iCivics](https://www.icivics.org) — free civic-education role-play games for K–12
- [SimSchool](https://simschool.org) — classroom-management simulation for teacher preparation

## Examples
- **Model United Nations** — students represent assigned countries, negotiate resolutions, and debrief on how national interest and procedure shaped outcomes.
- **Nursing standardized-patient simulations** — students manage a simulated clinical deterioration scenario, then debrief with video review; meta-analytic evidence shows simulation-based training outperforms or matches traditional clinical instruction [Simulation-based training with debriefing improves clinical outcomes.](https://doi.org/10.1001/jama.2013.282057) [+S].
- **PhET circuit simulations** — physics students manipulate voltage and resistance and immediately observe consequences, testing predictions before formal instruction.
- **Marketplace Simulations** — business students run a virtual company in teams, making pricing, product, and marketing decisions across competitive rounds.

## Key Sources
- Garris, R., Ahlers, R., & Driskell, J. E. (2002). Games, motivation, and learning: A research and practice model. *Simulation & Gaming, 33*(4), 441–467. [doi:10.1177/1046878102238607](https://doi.org/10.1177/1046878102238607)
- Cook, D. A., Hatala, R., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Barsuk, J. H. (2013). Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. *JAMA, 310*(9), 978–988. [doi:10.3109/0142159x.2012.714886](https://doi.org/10.3109/0142159x.2012.714886)
- Fanning, R. M., & Gaba, D. M. (2007). The role of debriefing in simulation-based learning. *Simulation in Healthcare, 2*(2), 115–125. [doi:10.1097/sih.0b013e3180315539](https://doi.org/10.1097/sih.0b013e3180315539)
- Chernikova, O., Heitzmann, N., Stadler, M., Holzberger, D., Seidel, T., & Fischer, F. (2020). Simulation-based learning in higher education: A meta-analysis. *Review of Educational Research, 90*(4), 499–541. [doi:10.3102/0034654320933544](https://doi.org/10.3102/0034654320933544)
- Kolb, D. A. (1984). *Experiential learning: Experience as the source of learning and development.* Prentice Hall.