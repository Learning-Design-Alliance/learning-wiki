---
type: strategy
title: Simulation Based Training
description: Learners practice skills in a replicated or synthetic task environment where errors are safe and performance can be systematically varied, observed, and debriefed.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Simulation Based Training

## Description
Simulation based training places learners inside a replicated version of the target task environment — a flight simulator, a mannequin-based clinical scenario, a business negotiation role-play, a virtual patient — where they perform the task under realistic conditions. Because the environment is synthetic, errors carry no real-world cost, difficulty can be controlled and escalated, and performance can be recorded for structured [feedback](../elements/feedback.md) and debriefing.

## Design Implications

Simulation works because it compresses experience: learners encounter rare, high-stakes, or slow-unfolding situations repeatedly instead of waiting for them to occur naturally. Its effectiveness depends less on the fidelity of the simulator than on the instructional design around it — clear objectives, controlled difficulty progression, and above all structured debriefing, which meta-analytic evidence identifies as the active ingredient in simulation outcomes [Cook et al. (2013) found simulation consistently improves learning compared with no intervention.](https://doi.org/10.1001/jama.2013.282057) [+S]. High physical fidelity is not required for learning; psychological fidelity — whether the scenario evokes the same decisions and demands as the real task — matters more [~M].

### Context
#### Requirements
- A task environment that reproduces the *decision demands* of the real task, not merely its surface appearance
- Defined learning objectives that map to specific scenario features
- A trained facilitator and a structured debriefing protocol (e.g., advocacy-inquiry or plus-delta formats)
- Mechanisms for recording performance (video, system logs) to ground debriefing in observed behavior

#### Constraints
- Simulation without structured debriefing produces little durable learning; learners repeat and entrench errors [-S]
- Overly high fidelity can overload novices with irrelevant detail, degrading learning [Cognitive overload degrades learning when extraneous demands exceed working memory capacity.](../claims/cognitive-overload-degrades-learning.md) [-M]
- Skills learned in the simulator do not automatically transfer to the workplace; transfer requires deliberate attention to context variation and follow-on practice in the real setting [~M]
- Expensive to build and maintain; cost is rarely justified for tasks that can be safely practiced in the real environment

#### Implementation Variability
- **Fidelity spectrum:** from tabletop exercises and role-plays through screen-based simulators to full-mission immersive environments; choose the lowest fidelity that preserves the target decisions
- **Part-task vs. whole-task:** isolated skill drills (e.g., IV insertion) vs. integrated team scenarios; part-task suits novices, whole-task suits integration and coordination goals
- **Embedded vs. post-hoc instruction:** prompts and teaching moments inside the scenario vs. full debriefing afterward; embedded instruction speeds early acquisition but interrupts realism
- **Distributed practice:** spaced simulation sessions outperform massed blocks for retention [~M]

### Target Learners
- Novices in high-stakes domains (aviation, surgery, emergency response) where real-world error is unacceptable
- Intermediate learners consolidating skills under varied conditions, where scenario variation supports transfer
- Teams practicing coordination and communication, not just individuals practicing technique
- Less valuable for learners who already perform the task routinely in real settings, unless targeting rare events

### Target Learning Goals
- Procedural and psychomotor skill acquisition under realistic constraints
- Decision-making and situation assessment in dynamic, time-pressured environments
- Team coordination, communication, and crisis resource management
- Recognition and management of rare or high-consequence events

### Instructions
1. Define the target competency and the specific decisions it requires; design scenarios around those decision points rather than around simulator capabilities.
2. Orient learners to the simulator's interface and conventions so that operating the simulation does not consume working memory needed for the task itself [Cognitive load management](../principles/cognitive-load-management.md).
3. Run the scenario at controlled difficulty, escalating complexity as competence grows ([Fading](../elements/fading.md)).
4. Debrief immediately using a structured protocol: review recorded performance, contrast intended with actual actions, and have learners articulate what they would do differently ([Think-Aloud](../elements/think-aloud.md) during replay makes reasoning visible).
5. Repeat with varied scenarios so learners extract general principles rather than a single scenario script ([Comparing Cases](../elements/comparing-cases.md)).
6. Follow with supervised performance in the real environment to close the transfer gap ([Practice](../elements/practice.md)).

## Related Strategies
- [Case-Based Learning](case-based-learning.md) — simulation is the interactive, first-person extension of the case method
- [Role-Play](acting-role-play.md) — low-fidelity simulation using human participants as the environment
- [Deliberate Practice](../principles/deliberate-practice.md) — simulation provides the controlled, repeatable conditions deliberate practice requires

## Examples
- **Flight simulation (aviation)** — Full-motion simulators with standardized proficiency checks are the canonical case; airline pilots log most initial type-rating hours in simulation before touching the aircraft.
- **[SimOne](https://www.simone.ca) / mannequin-based medical simulation** — High-fidelity patient simulators used for crisis resource management training in anesthesiology and emergency medicine, followed by video-assisted debriefing.
- **[CapsimInbox](https://www.capsim.com)** — Inbox-style business simulations in which learners manage a simulated company through email-driven decisions, used in management education for strategy and leadership practice.
- **Virtual patient platforms (e.g., [i-Human Patients](https://www.ihuman.com))** — Screen-based clinical reasoning simulations where learners interview, examine, and treat virtual patients with branching consequences.

## Key Sources
- Cook, D. A., Hamstra, S. J., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Hatala, R. (2013). Comparative effectiveness of instructional design features in simulation-based education: Systematic review and meta-analysis. *Medical Teacher, 35*(1), e867–e898. [doi:10.3109/0142159x.2012.714886](https://doi.org/10.3109/0142159x.2012.714886)
- Cook, D. A., Hatala, R., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Hamstra, S. J. (2013). Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. *JAMA, 310*(9), 978–988. [doi:10.1001/jama.2013.282057](https://doi.org/10.1001/jama.2013.282057)
- McGaghie, W. C., Issenberg, S. B., Petrusa, E. R., & Scalese, R. J. (2010). A critical review of simulation-based medical education research: 2003–2009. *Medical Education, 44*(1), 50–63. [doi:10.1111/j.1365-2923.2009.03547.x](https://doi.org/10.1111/j.1365-2923.2009.03547.x)
- Gaba, D. M. (2004). The future vision of simulation in health care. *Quality and Safety in Health Care, 13*(suppl 1), i2–i10. [doi:10.1136/qshc.2004.009878](https://doi.org/10.1136/qshc.2004.009878)
- Salas, E., DiazGranados, D., Weaver, S. J., & King, H. (2008). Does team training work? Principles for health care. *Academic Emergency Medicine, 15*(11), 1002–1009.