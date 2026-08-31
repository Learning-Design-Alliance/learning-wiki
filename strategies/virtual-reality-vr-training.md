---
type: strategy
title: Virtual Reality (VR) Training
description: VR training places learners inside simulated, interactive 3D environments where they can rehearse procedures and decisions safely before performing them in real settings.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Virtual Reality (VR) Training

> **Strategy** · [All strategies](index.md)

## Description
Virtual Reality (VR) training uses head-mounted displays and interactive simulation to place learners inside a three-dimensional representation of a task environment — an operating theatre, a cockpit, a hazardous industrial site — where they can rehearse procedures and make decisions without real-world consequences. Effective VR training is not passive immersion: it pairs the simulated environment with structured [Practice](../elements/practice.md), [Demonstration](../elements/demonstration.md), and feedback loops, so the medium serves an instructional design rather than substituting for one.

## Design Implications

VR's distinctive contribution is *embodied, consequence-free practice* in environments that are dangerous, expensive, or rare in real life. Meta-analytic and review evidence shows VR training improves learning outcomes and skill transfer relative to conventional instruction in many domains, but the advantage is largest when the simulation affords interactivity and guided feedback rather than passive 360° viewing [~M]. Immersive media also impose extraneous cognitive load — navigating an unfamiliar interface competes with learning the content — so designs must manage that load deliberately [Cognitive Load Management](../principles/cognitive-load-management.md) [~M].

### Context
#### Requirements
- Headsets and controllers, well-built virtual environments that faithfully represent the target task's critical features, and a facilitator or system that structures pre-briefing, practice, and debriefing
- Instructional scaffolding inside the simulation: prompts, [Coaching](../elements/coaching.md), and feedback tied to learner actions [Feedback is most effective at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
- A pre-training orientation to the controls, so interface manipulation does not consume working memory during learning [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]

#### Constraints
- Passive or exploratory VR without guidance often underperforms simpler media: learners attend to surface features and miss the to-be-learned content, and immersion can add extraneous load that harms retention [~S] — pre-training on the interface and signaling of critical features mitigates this
- Cybersickness affects a substantial minority of users and degrades both experience and performance; session length and locomotion design matter
- High development and maintenance costs are only justified for tasks that are dangerous, rare, or expensive to practice otherwise — VR for content easily taught by text or video is a poor investment
- Transfer depends on *fidelity to the task*, not visual realism per se; photorealistic but procedurally shallow simulations add cost without learning benefit

#### Implementation Variability
- Fully immersive (head-mounted) vs. desktop simulation vs. 360° video — immersion is a continuum, and lower-cost formats often achieve similar outcomes for declarative goals
- Individual rehearsal vs. multi-user collaborative scenarios (e.g., team-based emergency response)
- Standalone simulation vs. blended designs that interleave VR practice with classroom or on-the-job instruction [Blended Learning](../patterns/blended-learning.md)

### Target Learners
- Novices in procedural, high-stakes domains (surgery, aviation, industrial safety) who need safe repetition before real performance [+M]
- Learners who benefit from spatially embodied understanding of environments and equipment layouts
- Less valuable for learners who already perform the task competently, unless the goal is rare-event or failure-mode rehearsal

### Target Learning Goals
- Procedural skill acquisition and motor sequencing through repeated safe rehearsal
- Spatial and situational awareness: learning the layout and dynamics of a real environment
- Decision-making under pressure, including rare and emergency scenarios that cannot be staged safely
- Confidence and readiness: successful virtual performance builds self-efficacy that supports persistence in real settings [Self-efficacy predicts academic persistence.](../claims/self-efficacy-predicts-academic-persistence.md) [+M]

### Instructions
1. **Brief and orient** — pre-train learners on the controls and task goals so interface handling becomes automatic before content learning begins
2. **Model the performance** — show an expert execution of the procedure in the simulation or via [Demonstration](../elements/demonstration.md) before learner attempts
3. **Practice with feedback** — have learners perform the task in the simulation with immediate, action-contingent feedback [Feedback is most effective at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]; break complex procedures into segments using [Part-Task Practice](../elements/part-task-practice.md) for novices [Part-task practice reduces load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [+M]
4. **Increase complexity and variability** — progress to whole-task scenarios with complications, distractors, and failure states
5. **Debrief** — review performance data and errors with a facilitator, connecting virtual performance to real-world application [Application](../elements/application.md)
6. **Space the rehearsal** — distribute repeat sessions over time rather than massing them [Spaced repetition improves retention.](../claims/spaced-repetition-improves-retention.md) [+S]

## Related Strategies
- [Simulation-Based Training](simulation-based-training.md) — the broader family; VR is its most immersive form
- [Role-Play](acting-role-play.md) — low-tech embodiment of the same principle of enacted practice
- [Flipped Classroom](flipped-classroom.md) — VR sessions can serve as the application layer after preparatory study

## Related Elements
- [Practice](../elements/practice.md) — the core activity VR enables at scale and without risk
- [Demonstration](../elements/demonstration.md) — expert models can be shown inside the same environment learners will perform in
- [Coaching](../elements/coaching.md) — facilitator or system guidance during simulation
- [Application](../elements/application.md) — debriefing and transfer activities that convert virtual performance into real competence

## Tools
- **Osso VR** — surgical rehearsal platform with objective performance scoring
- **STRIVR** — workplace and safety training using immersive scenario practice
- **Oxford Medical Simulation** — virtual patient simulators for clinical decision-making in nursing and medicine

## Examples
- **Surgical training:** randomized studies of VR laparoscopic simulation (e.g., MIST-VR) show trainees trained in VR perform procedures faster and with fewer errors than conventionally trained controls [+M]
- **Walmart** used STRIVR's VR modules to prepare associates for high-pressure events (Black Friday, emergency procedures) at scale across thousands of stores
- **Flight simulation** — the longest-standing VR-adjacent training tradition; full-motion simulators are the regulatory standard for airline pilot certification

## Key Sources
- Makransky, G., & Mayer, R. E. (2022). Benefits of immersion and presence in a virtual reality-based learning environment. *Educational Psychology Review, 34*, 2323–2345. [doi:10.4324/9781003386131-13](https://doi.org/10.4324/9781003386131-13)
- Parong, J., & Mayer, R. E. (2018). Learning science in immersive virtual reality. *Journal of Educational Psychology, 110*(6), 785–797. [doi:10.1037/edu0000241](https://doi.org/10.1037/edu0000241)
- Jensen, L., & Konradsen, F. (2018). A review of the use of virtual reality head-mounted displays in education and training. *Education and Information Technologies, 23*, 1515–1529. [doi:10.1007/s10639-017-9676-0](https://doi.org/10.1007/s10639-017-9676-0)
- Seymour, N. E., Gallagher, A. G., Roman, S. A., O'Brien, M. K., Bansal, V. K., Andersen, D. K., & Satava, R. M. (2002). Virtual reality training improves operating room performance: Results of a randomized, double-blinded study. *Annals of Surgery, 236*(4), 458–464. [doi:10.1097/00000658-200210000-00008](https://doi.org/10.1097/00000658-200210000-00008)
