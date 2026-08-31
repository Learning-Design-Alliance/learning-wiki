---
type: strategy
title: Simulation Based Practice
description: Learners rehearse a task in a simplified, safe, interactive replica of a real-world environment, receiving feedback on performance without real-world consequences.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Simulation Based Practice

> **Strategy** · [All strategies](index.md)

## Description
Simulation based practice places learners in an interactive model of a real task environment — a flight simulator, patient manikin, business game, or virtual lab — where they perform the target skill under conditions that approximate the real thing but remove risk, cost, and time pressure. Performance is typically followed by structured [feedback](../elements/practice.md) or debriefing, which is where much of the learning actually occurs.

## Design Implications

Simulation works because it enables high-volume, low-stakes [practice](../elements/practice.md) with immediate consequences, allowing errors to surface and be corrected safely [Simulation-based training improves clinical performance across health professions.](https://doi.org/10.1001/jama.2013.2820) [+S]. The critical design lever is the debrief: simulation without structured reflection produces markedly weaker transfer than simulation with guided after-action review [Debriefing is a key moderator of simulation learning outcomes.](https://doi.org/10.1097/SIH.0b013e3180315309) [+M]. Fidelity must be matched to the learning goal — physical realism matters for psychomotor skills, but psychological and functional fidelity (realistic decisions and pressures) matter more for judgment-heavy tasks [~M].

### Context
#### Requirements
- A task model that preserves the decision structure of the real environment, even if visuals are simplified
- Clear performance criteria so the simulation can generate or support meaningful [feedback](../elements/practice.md)
- A structured debrief protocol (what happened, why, what to change) rather than unstructured discussion
- Scenario variation across repetitions so learners generalize rather than memorize one scenario

#### Constraints
- High physical fidelity without instructional alignment wastes budget and can overload learners [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M] — realistic detail competes with the target skill for working memory
- Learners can learn the simulation's quirks rather than the underlying skill, producing illusory competence [-M]
- Poor or absent debriefing substantially reduces transfer; the event alone is not the intervention [~S]
- Over-scaffolding scenarios (single correct path) undermines adaptability for ill-structured domains

#### Implementation Variability
- **Manikin/part-task trainers** — physical fidelity for procedural and psychomotor skills
- **Screen-based simulation and games** — scalable decision-making practice (e.g., business simulations, virtual patients)
- **Standardized patients / role-play** — social and communication skills with human variability
- **Virtual/augmented reality** — spatial and situational awareness tasks where immersion aids encoding [~W]
- **Rapid-cycle deliberate practice** — short simulation–feedback loops with increasing difficulty until mastery

### Target Learners
- Novices who must reach a safe competence threshold before touching real equipment or patients [Simulation-based training improves clinical performance across health professions.](https://doi.org/10.1001/jama.2013.2820) [+S]
- Intermediate learners consolidating skills under varied, pressured conditions
- Less valuable for experts, who gain little from routine scenarios unless they introduce genuine novelty or edge cases [~M]

### Target Learning Goals
- Procedural and psychomotor skill acquisition to a defined standard
- Decision-making and triage under time pressure
- Team coordination and communication (crew resource management, crisis response)
- Transfer of classroom knowledge into applied performance

### Instructions
1. Define the target performance and observable criteria; align scenarios to them ([Constructive Alignment](../patterns/constructive-alignment.md))
2. Brief learners on roles, goals, and simulation conventions — but not the specific challenge to be encountered
3. Run the scenario, minimizing instructor interruption ([Practice](../elements/practice.md))
4. Debrief immediately with a facilitator using an after-action framework (e.g., PEARLS: reaction → analysis → synthesis) ([Articulation](../elements/articulation.md))
5. Repeat with varied scenarios and increasing difficulty, fading support as competence grows ([Fading](../elements/fading.md))
6. Assess transfer on a *different* scenario than those practiced

## Related Strategies
- [Deliberate Practice](../principles/deliberate-practice.md) — simulation is the delivery vehicle; deliberate practice defines the effortful, feedback-rich quality bar
- [Role-Play](acting-role-play.md) — the human-interaction variant of simulation
- [Case-Based Learning](case-based-learning.md) — the lower-fidelity, discussion-based cousin; simulation adds enactment

## Examples
- **[Flight simulators](https://www.faa.gov/training_testing/training/sim)** — FAA-certified full-motion simulators are the canonical case; airline pilots log most initial type-rating hours in simulation before flying a real aircraft.
- **[SimCenter / virtual patient platforms](https://www.mededportal.org)** — virtual patient cases (e.g., the CLIPP series in pediatric education) let medical students practice diagnostic reasoning with unlimited repetitions.
- **[Capsim](https://www.capsim.com)** and **[Harvard Business Publishing simulations](https://www.harvardbusiness.org/simulations/)** — business students run multi-round company simulations, debriefing decisions against market outcomes each round.
- **[PhET Interactive Simulations](https://phet.colorado.edu)** — physics and chemistry simulations used for inquiry practice before or alongside real labs.

## Key Sources
- Cook, D. A., Hatala, R., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Barsuk, J. H. (2013). Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. *JAMA, 310*(9), 978–988. [doi:10.3109/0142159x.2012.714886](https://doi.org/10.3109/0142159x.2012.714886)
- Issenberg, S. B., McGaghie, W. C., Petrusa, E. R., Lee Gordon, D., & Scalese, R. J. (2005). Features and uses of high-fidelity medical simulations that lead to effective learning: A BEME systematic review. *Medical Teacher, 27*(1), 10–28. [doi:10.1080/01421590500046924](https://doi.org/10.1080/01421590500046924)
- McGaghie, W. C., Issenberg, S. B., Petrusa, E. R., & Scalese, R. J. (2010). A critical review of simulation-based medical education research: 2003–2009. *Medical Education, 44*(1), 50–63. [doi:10.1111/j.1365-2923.2009.03547.x](https://doi.org/10.1111/j.1365-2923.2009.03547.x)
- Fanning, R. M., & Gaba, D. M. (2007). The role of debriefing in simulation-based learning. *Simulation in Healthcare, 2*(2), 115–125. [doi:10.1097/sih.0b013e3180315539](https://doi.org/10.1097/sih.0b013e3180315539)