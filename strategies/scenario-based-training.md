---
type: strategy
title: Scenario Based Training
description: Learners practice decision-making and skill application inside a realistic, contextualized scenario that simulates the conditions of real performance.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Scenario Based Training

## Description
Scenario based training places learners inside a realistic, contextualized situation — a patient case, a customer complaint, an emergency drill — and requires them to make decisions and perform actions as they would on the job. The scenario supplies the conditions, constraints, and consequences of real performance, so learning occurs through situated decision-making rather than decontextualized instruction. It is typically built from a [Demonstration or briefing, followed by learner action, then structured debriefing.

## Design Implications

Scenario based training works because it forces retrieval and application under realistic conditions, converting declarative knowledge into usable procedure [Active learning improves exam performance relative to lecture.](../claims/active-learning-improves-exam-performance.md) [+S]. Its effectiveness depends on scenario fidelity being high enough to trigger transfer-relevant decisions but low enough to avoid cognitive overload [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [~M]. The debrief — not the scenario itself — is where much of the learning consolidates; scenarios without structured reflection produce weaker transfer.

### Context
#### Requirements
- Scenarios drawn from authentic task analysis of the target performance domain
- Decision points with meaningful consequences and feedback tied to learner choices
- A structured debrief that connects actions to underlying principles ([Feedback](../elements/feedback.md), [Assess Performance](../elements/assess-performance.md))
- Sequenced difficulty: early scenarios narrow and scaffolded, later ones complex and open ([Fading](../elements/fading.md))

#### Constraints
- High-fidelity scenarios can overload novices with irrelevant detail; simplified or part-task scenarios work better early in learning [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]
- Scenarios that teach one specific path can anchor learners; multiple contrasting scenarios are needed for transfer to varied situations [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+M]
- Poorly designed branching or free-play scenarios let learners practice errors without detection, entrenching misconceptions
- Development cost is high; low-fidelity paper or discussion-based scenarios often achieve comparable outcomes for knowledge-level goals [~W]

#### Implementation Variability
- **Branching simulations** (e.g., healthcare virtual patients) where choices alter the scenario trajectory
- **Tabletop / role-play scenarios** ([Acting-Role-Play](acting-role-play.md)) using human interaction instead of software
- **Case-based discussion** ([Case-Based Learning](../elements/case-based-learning.md)) — a written scenario analyzed in groups, trading fidelity for scalability
- **Embedded drill scenarios** in high-stakes fields (aviation, military, emergency medicine) combining simulation with repeated practice

### Target Learners
- Intermediate learners who have foundational knowledge and need to learn *when and how* to apply it under realistic conditions
- Professionals in high-stakes domains (clinical, aviation, emergency response) where errors carry real consequences
- Novices benefit only from heavily scaffolded, low-complexity scenarios; full-complexity scenarios can overwhelm them [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [~M]

### Target Learning Goals
- Decision-making and judgment under realistic constraints
- Procedural fluency and integration of multiple skills in context
- Transfer of classroom knowledge to authentic performance situations
- Team coordination and communication when scenarios are run collaboratively

### Instructions
1. Conduct a task analysis to identify the critical decisions and conditions the scenario must reproduce.
2. Open with a brief [Demonstration or orientation so learners understand the scenario's rules and success criteria.
3. Present the scenario with an authentic trigger ([Anchored Instruction](../patterns/anchored-instruction.md)) and require learners to act, not just analyze.
4. Provide consequences that follow logically from learner choices, delivered as immediate [Feedback](../elements/feedback.md).
5. Run a structured debrief: what was done, why, what alternatives existed, what principle explains the outcome.
6. Follow with a contrasting scenario that varies surface conditions but shares underlying structure [Comparing contrasting cases improves learning.](../claims/comparing-contrasting-cases-improves-learning.md) [+M].
7. Fade scaffolds across the scenario sequence until learners handle full-complexity cases independently.

## Related Strategies
- [Case-Based Learning strategies and pages](../elements/case-based-learning.md) — the discussion-based, lower-fidelity variant of the same idea
- [Acting-Role-Play](acting-role-play.md) — human-performed scenarios emphasizing interpersonal skills
- [Simulation-based practice](../elements/practice.md) — repeated scenario execution builds automaticity

## Examples
- **Harvard Business School case method** ([Case-Based Learning (Harvard Method)](../patterns/case-based-learning-harvard-method.md)) — written business scenarios discussed under instructor facilitation; a scalable, low-fidelity form of scenario training.
- **vSim for Nursing (Laerdal/Wolters Kluwer)** (https://www.wolterskluwer.com/en/solutions/vsim-for-nursing) — branching virtual patient scenarios with embedded decision feedback and post-scenario debriefing.
- **FAA/airline Line-Oriented Flight Training (LOFT)** — full-mission flight simulator scenarios replicating realistic flight conditions, followed by crew debrief; the canonical high-fidelity example.
- **Code.org CS Discoveries "problem-solving process" units** (https://code.org/educate/curriculum/cs-discoveries) — structured scenarios requiring learners to apply a defined process to novel situations.

## Key Sources
- Clark, R. C., & Mayer, R. E. (2016). *E-Learning and the Science of Instruction* (4th ed.). Wiley. [doi:10.1002/9781119239086](https://doi.org/10.1002/9781119239086)
- Freeman, S., et al. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)
- van Merriënboer, J. J. G., & Kirschner, P. A. (2018). *Ten Steps to Complex Learning* (3rd ed.). Routledge.
- Kolodner, J. L. (1997). Educational implications of analogy and memory: The case of case-based reasoning. *Educational Technology, 37*(1), 26–34. [doi:10.1037/0003-066x.52.1.57](https://doi.org/10.1037/0003-066x.52.1.57)
