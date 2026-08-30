---
type: strategy
title: Augmented Reality (AR) for Military Training
description: AR overlays virtual objects and scenario elements onto real training environments, allowing soldiers to rehearse tasks more frequently, safely, and cheaply than live exercises permit.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Augmented Reality (AR) for Military Training

## Description
AR overlays virtual objects — enemy combatants, vehicles, hazards, equipment callouts — onto the physical world as seen through head-mounted displays, tablets, or projected systems. This lets trainees rehearse tactical, maintenance, and decision-making tasks in real terrain and on real equipment without the cost, travel, range time, and risk of fully live exercises. Unlike [Virtual Reality](../strategies/virtual-reality-simulations.md), AR preserves the physical cues of the actual environment, supporting [situated learning](../theories/situated-learning.md) [~M].

## Design Implications

AR's training value comes from combining real-world context with controllable, repeatable scenario content — a form of [Simulation](../strategies/simulation-based-training.md) that reduces the gap between training and operational environments. Because AR adds visual information to an already demanding task, scenario design must manage [cognitive load](../principles/cognitive-load-management.md): poorly integrated overlays can split attention between the display and the real world [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+S]. AR is most effective as a component within a blended training pipeline, not a replacement for live exercises [~M].

### Context
#### Requirements
- Reliable tracking and registration so virtual objects stay anchored to real positions; misregistration destroys training value
- Scenario content aligned to actual mission-relevant tasks, not technology demonstrations
- Instructor control of scenario variables (adversary behavior, weather, failures) to enable [Practice](../elements/practice.md) with varied conditions
- Debrief capability — recorded scenario data supports [Feedback](../elements/feedback.md) and after-action review

#### Constraints
- AR cannot replicate live-fire stress, physical fatigue, or the consequences of real danger; over-reliance risks confidence without competence [-M]
- Display field-of-view limits and latency can degrade marksmanship and vehicle-handling skill transfer [-M]
- Effectiveness drops for tasks where the virtual overlay cues attention learners must eventually allocate themselves; guidance should fade as proficiency grows [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]
- Hardware fragility, battery life, and environmental conditions (bright sun, dust) constrain field use [-W]

#### Implementation Variability
- **Head-mounted AR** (e.g., IVAS-style systems) for dismounted squad tactics and navigation
- **Tablet/phone AR** for maintenance training, overlaying step-by-step procedures on actual equipment
- **Projected/dome AR** for vehicle and gunnery simulators
- **Marker-based overlays on ranges** to populate live ranges with virtual adversaries at fraction of live-opposition cost

### Target Learners
- Novice soldiers learning equipment operation, procedures, and spatial tasks, where contextual overlays reduce search and error [AR supports learning by visualizing spatial and procedural information in context.](../claims/cognitive-overload-degrades-learning.md) [+M]
- Experienced personnel benefit mainly from scenario variability and stress inoculation, not from procedural overlays, which become redundant [Guidance becomes less effective as learner expertise increases.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Procedural skill: weapons maintenance, equipment checks, call-for-fire procedures
- Spatial and situational awareness: navigation, terrain association, threat detection
- Team coordination and decision-making under simulated operational conditions
- Knowledge retention through repeated, low-cost rehearsal [~M]

### Instructions
1. **Brief and orient** — deliver [Direct Instruction](../elements/direct-instruction.md) on the task and the AR system's conventions before first use.
2. **Demonstrate** — model the task with AR overlays active, using [Coaching](../elements/coaching.md) to narrate decisions.
3. **Practice with feedback** — trainees perform the task in AR scenarios; instructors adjust difficulty and deliver task-level [Feedback](../elements/feedback.md) [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].
4. **Debrief** — replay recorded scenario data in an after-action review; require trainees to [Articulate](../elements/articulation.md) their decisions.
5. **Fade and transfer** — progressively remove overlays and cues, then confirm performance in live training [Application](../elements/application.md).

## Related Strategies
- [Simulation-Based Training](../strategies/simulation-based-training.md) — AR is a variant that preserves real-world context
- [Virtual Reality Training](../strategies/virtual-reality-training.md) — fully synthetic alternative when real terrain is unavailable
- [Scenario-Based Training](../strategies/scenario-based-training.md) — AR supplies the scenario content layer
- [After-Action Review](../strategies/after-action-review.md) — the debrief method that converts AR exercise data into learning

## Related Elements
- [Practice](../elements/practice.md) — AR enables high-repetition, low-cost practice
- [Coaching](../elements/coaching.md) — instructor intervention during AR scenarios
- [Assess Performance](../elements/assess-performance.md) — AR systems log objective performance data
- [Application](../elements/application.md) — AR rehearsal must culminate in live-task application

## Examples
- **U.S. Army Integrated Visual Augmentation System (IVAS)** — head-mounted AR for squad-level training and rehearsal, projecting virtual adversaries and waypoints onto real terrain (https://peo-soldier.army.mil).
- **AVTR (Augmented Virtuality Tactical Rehearsal) and synthetic training environments** — mixed-reality range systems that overlay virtual opposing forces onto live ranges.
- **Maintenance AR applications** — tablet-based overlays guiding armorers and mechanics through weapon and vehicle procedures step by step, reducing errors and training time [+M].

## Key Sources
- Akçayır, M., & Akçayır, G. (2017). Advantages and challenges associated with augmented reality for education: A systematic review of the literature. *Computers & Education, 114*, 506–527. [doi:10.1016/j.compedu.2016.11.002](https://doi.org/10.1016/j.compedu.2016.11.002)
- Bacca, J., Baldiris, S., Fabregat, R., Graf, S., & Kinshuk. (2014). Augmented reality trends in education: A systematic review of research and applications. *Educational Technology & Society, 17*(4), 133–149.
- Billinghurst, M., Clark, A., & Lee, G. (2015). A survey of augmented reality. *Foundations and Trends in Human–Computer Interaction, 8*(2–3), 73–272. [doi:10.1561/1100000049](https://doi.org/10.1561/1100000049)
- Mayer, R. E. (2021). *Multimedia learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Stone, R. J., & Watts, K. P. (2010). Steering simulation technologies for military training. In E. Salas et al. (Eds.), *Military training effectiveness* (pp. 155–190). Wiley.