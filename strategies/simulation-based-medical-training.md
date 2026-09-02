---
type: strategy
id: simulation-based-medical-training
title: Simulation Based Medical Training
description: Learners rehearse clinical skills and decisions in realistic but risk-free simulated environments — manikins, task trainers, standardized patients, or virtual scenarios — followed by structured debriefing.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Simulation Based Medical Training

> **Strategy** · [All strategies](index.md)

## Description
Simulation based medical training places learners in replicated clinical situations — high-fidelity manikins, partial task trainers, standardized patients, screen-based scenarios, or immersive virtual reality — where they perform assessments, procedures, and team decisions without risk to real patients. The simulation itself is only half the design: a structured debriefing afterward, in which learners reflect on performance against expert standards, is where much of the durable learning occurs.

## Design Implications

Simulation works because it allows deliberate practice with immediate feedback — repeated, effortful rehearsal of specific skills at the edge of competence, which is difficult to arrange safely in live clinical care [Simulation improves clinical knowledge, skills, and behaviors compared with no intervention.](https://jamanetwork.com/journals/jama/fullarticle/1104489) [+S]. Its effectiveness depends on scenario design that manages cognitive load: novices overwhelmed by full-fidelity environments learn less than those who start with part-task trainers isolating one skill [Part-task practice reduces working memory load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [+M]. Debriefing quality is a stronger predictor of learning outcomes than simulator fidelity; learner-centered, facilitated reflection outperforms instructor-led lecturing about what went wrong [Debriefing with good judgment improves learning from simulation.](https://onlinelibrary.wiley.com/doi/10.1111/medu.12775) [+M].

### Context
#### Requirements
- Clearly defined learning objectives that determine the required level of physical, conceptual, and psychological fidelity
- Valid, reliable performance assessment (checklists, global rating scales, or automated metrics) to drive feedback
- Trained facilitators for scenario delivery and debriefing — untrained debriefers reliably degrade outcomes
- Psychological safety: learners must believe errors in simulation carry no professional penalty, or they will not attempt difficult tasks

#### Constraints
- High physical fidelity without instructional alignment wastes resources; low-fidelity models often teach the underlying skill as well as expensive simulators [~M]
- Skills learned in simulation do not automatically transfer to clinical practice without deliberate curriculum integration and follow-up practice in context [-M]
- Simulation without debriefing produces substantially weaker learning than simulation with structured reflection [-S]
- Overly complex scenarios for novices trigger extraneous load and performance collapse; expertise-appropriate complexity is required [Guidance that helps novices can hinder experts.](../claims/expertise-reversal-effect.md) [~M]

#### Implementation Variability
- **Part-task trainers** (e.g., central line insertion pads, suture boards) isolate psychomotor skills for massed practice
- **Full-body high-fidelity manikins** (e.g., Laerdal SimMan, CAE Healthcare) support team crisis response scenarios
- **Standardized patients** (trained actors) develop communication, history-taking, and breaking-bad-news skills
- **In situ simulation** runs scenarios in the actual clinical environment, surfacing latent system and teamwork errors
- **Screen-based/VR simulation** (e.g., Touch Surgery, Osso VR) enables distributed, self-paced procedural rehearsal

### Target Learners
- Novices and trainees acquiring procedures and clinical reasoning before patient contact [Part-task practice reduces working memory load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [+M]
- Experienced clinicians maintaining rare, high-stakes skills (e.g., crisis resource management) where real-case volume is insufficient [+M]
- Interprofessional teams practicing communication and role coordination under stress [+M]

### Target Learning Goals
- Procedural and psychomotor skill acquisition with accuracy and speed benchmarks
- Clinical decision-making and management of deteriorating patients
- Teamwork, leadership, and crisis resource management behaviors
- Transfer-appropriate preparation for infrequent, high-consequence events

### Instructions
1. Define specific, assessable objectives and select the lowest-fidelity simulator that supports them ([Cognitive Load Management](../principles/cognitive-load-management.md)).
2. Pre-brief: establish psychological safety, orient learners to the simulator's capabilities and limits, and state expectations.
3. Run the scenario with embedded cues and, where appropriate, in-scenario coaching ([Coaching](../elements/coaching.md)).
4. Debrief using a structured framework (e.g., PEARLS or advocacy-inquiry), focusing feedback at the task and process levels rather than the person [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].
5. Repeat with deliberate practice until a mastery standard is reached, then schedule spaced refresher sessions to combat skill decay.
6. Integrate into the broader curriculum with clinical follow-up so simulated learning connects to real practice ([Situated Learning](../theories/situated-learning.md)).

## Related Strategies
- [Case-Based Learning](../patterns/case-based-learning.md) — simulation scenarios are often built from clinical cases; the case supplies the decision structure the simulation enacts
- [Deliberate Practice](../principles/deliberate-practice.md) — the mastery-standard, feedback-driven repetition model that underpins simulation curricula
- [Role Play](role-play.md) — the low-technology ancestor for communication and team skills training

## Examples
- **[Center for Medical Simulation, Harvard](https://harvardmedsim.org)** — pioneer of the "debriefing with good judgment" method now widely adopted in simulation faculties.
- **[Resuscitation council advanced life support courses](https://www.resus.org.uk)** — manikin-based cardiac arrest simulation with structured debriefing as the core instructional method.
- **[Osso VR](https://ossovr.com)** — virtual reality surgical simulation with objective performance scoring used in orthopedic training.
- **In situ team training in labor and delivery units** — simulations run in the actual clinical space to expose latent safety threats (e.g., missing equipment, unclear escalation roles).

## Key Sources
- Cook, D. A., Hatala, R., Brydges, R., Zendejas, B., Szostek, J. H., Wang, A. T., Erwin, P. J., & Hamstra, S. J. (2011). Technology-enhanced simulation for health professions education: A systematic review and meta-analysis. *JAMA, 306*(9), 978–988. [doi: 10.1001/jama.2011.1234](https://doi.org/10.1001/jama.2011.1234)
- Issenberg, S. B., McGaghie, W. C., Petrusa, E. R., Lee Gordon, D., & Scalese, R. J. (2005). Features and uses of high-fidelity medical simulations that lead to effective learning: A BEME systematic review. *Medical Teacher, 27*(1), 10–28. [doi:10.1080/01421590500046924](https://doi.org/10.1080/01421590500046924)
- McGaghie, W. C., Issenberg, S. B., Petrusa, E. R., & Scalese, R. J. (2010). A critical review of simulation-based medical education research: 2003–2009. *Medical Education, 44*(1), 50–63. [doi:10.1111/j.1365-2923.2009.03547.x](https://doi.org/10.1111/j.1365-2923.2009.03547.x)
- Eppich, W., & Cheng, A. (2015). Promoting excellence and reflective learning in simulation (PEARLS): Development and rationale for a blended approach to health care simulation debriefing. *Simulation in Healthcare, 10*(2), 106–115. [doi:10.1097/SIH.0000000000000072](https://doi.org/10.1097/SIH.0000000000000072)
- McGaghie, W. C., Issenberg, S. B., Cohen, E. R., Barsuk, J. H., & Wayne, D. B. (2011). Does simulation-based medical education with deliberate practice yield better results than traditional clinical education? A meta-analytic comparative review. *Academic Medicine, 86*(6), 706–711. [doi:10.1097/ACM.0b013e318217e119](https://doi.org/10.1097/ACM.0b013e318217e119)