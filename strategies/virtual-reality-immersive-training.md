---
type: strategy
id: virtual-reality-immersive-training
aliases: [virtual-reality-vr-training, virtual-reality-training]
title: Virtual Reality Immersive Training
description: Learners practice skills inside a computer-generated, head-tracked 3D environment that simulates the target performance context.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Virtual Reality Immersive Training

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (3 for, 2 mixed, 1 against) · 18 studies (7 review, 5 causal, 4 quant-synthesis, 2 theoretical), `q1`–`q4` · 4 of 18 report an effect size

## Description
Virtual reality (VR) immersive training places learners inside a simulated, interactive 3D environment — typically via a head-mounted display — where they can rehearse procedures, explore environments, or respond to scenarios that are dangerous, expensive, or logistically difficult to stage in reality. The strategy combines [Simulation](../elements/simulation.md) with embodied interaction: learners act in the environment rather than merely viewing it, and the system can capture performance data for [Feedback](../elements/feedback.md) and debriefing.

## Design Implications

Immersion can increase engagement and situational interest, but engagement is not learning: VR's benefit depends on whether the environment supports the cognitive processes the objective requires [Makransky & Petersen's CAMIL model argues immersion affects learning indirectly through affordances and presence, not directly.](../claims/expertise-reversal-effect.md) [~M]. Because immersive environments are rich in novel, often irrelevant sensory detail, they can overload working memory — segmenting, pretraining, and signaling are essential [Parong & Mayer found that adding summarization/segmenting to immersive VR science content improved retention and transfer over unguided immersion.](../claims/chunking-reduces-working-memory-load.md) [+S]. VR works best as one component of a blended sequence with pretraining, guided practice, and debrief, not as a stand-alone experience.

### Context
#### Requirements
- A clearly defined performance objective that maps onto actions the simulation can actually support
- Pretraining on the interface and key concepts before immersion ([Advance Organizers](../elements/advance-organizers.md))
- Embedded or post-hoc [Feedback](../elements/feedback.md) tied to specific learner actions, plus a structured debrief
- Session length limits and comfort protocols (motion sickness, physical space)
- A task with meaningful physical, spatial, or procedural fidelity requirements — VR earns its cost only when the simulation maps onto real performance
- Pre-training that orients learners to the interface and task goals before immersion, reducing load during the simulation
- A debriefing or reflection step connecting the simulated experience to transfer contexts
- Headsets and controllers, well-built virtual environments that faithfully represent the target task's critical features, and a facilitator or system that structures pre-briefing, practice, and debriefing
- Instructional scaffolding inside the simulation: prompts, [Coaching](../elements/coaching.md), and feedback tied to learner actions [Feedback is most effective at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]

#### Constraints
- Unguided exploration of rich immersive environments frequently impairs learning relative to desktop [simulation](../elements/simulation.md) because extraneous processing displaces germane processing [Parong & Mayer found that adding summarization/segmenting to immersive VR science content improved retention and transfer over unguided immersion.](../claims/chunking-reduces-working-memory-load.md) [-S]
- Novelty and "wow factor" consume attention; learning gains often fade once novelty wears off or when compared to cheaper media delivering the same content [Meta-analytic evidence finds VR effects on learning are small-to-moderate and highly heterogeneous across designs.](../claims/expertise-reversal-effect.md) [~M]
- Poorly matched to objectives requiring symbolic abstraction, extended reading, or fine verbal detail; head-mounted displays render dense text hard to read
- Physical side effects (cybersickness) and equipment cost constrain session length and scale
- Immersion without instructional scaffolding often underperforms desktop video or slides for declarative learning outcomes [VR's affective and behavioral advantages do not automatically translate to knowledge gains.](../claims/cognitive-overload-degrades-learning.md) [~S]
- High visual fidelity and decorative detail can hurt learning; irrelevant immersive detail competes with essential content [Coherence principle: irrelevant material hurts learning.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [-M]
- Cybersickness, equipment cost, and per-learner headset logistics limit session length and cohort scale
- Poor transfer when the simulation's affordances diverge from the real task (negative training)
- Passive or exploratory VR without guidance often underperforms simpler media: learners attend to surface features and miss the to-be-learned content, and immersion can add extraneous load that harms retention [~S] — pre-training on the interface and signaling of critical features mitigates this
- Cybersickness affects a substantial minority of users and degrades both experience and performance; session length and locomotion design matter
- High development and maintenance costs are only justified for tasks that are dangerous, rare, or expensive to practice otherwise — VR for content easily taught by text or video is a poor investment
- Transfer depends on *fidelity to the task*, not visual realism per se; photorealistic but procedurally shallow simulations add cost without learning benefit

#### Implementation Variability
- **360° passive video** vs. **fully interactive simulation** — interactivity matters only when the objective requires decision-making, not for observational learning
- **Desktop VR / screen-based simulation** as a lower-cost, lower-cybersickness alternative that often achieves comparable outcomes [Meta-analytic evidence finds VR effects on learning are small-to-moderate and highly heterogeneous across designs.](../claims/expertise-reversal-effect.md) [~M]
- **Single-user practice** vs. **multi-user social VR** for team coordination and communication skills
- **Embedded guidance** (in-scenario prompts, virtual coach) vs. **post-session debrief** in the style of simulation-based training
- **Full-immersion headset VR** for spatial/procedural tasks (surgery, equipment operation, hazard response)
- **Desktop simulation / screen-based VR** — cheaper, scalable, often equally effective for declarative goals [~S]
- **360° video VR** — passive but immersive; suited to situational awareness and empathy-oriented goals
- **VR + debrief hybrid** — simulation followed by instructor-led review, the format with the strongest evidence base in medical simulation
- Fully immersive (head-mounted) vs. desktop simulation vs. 360° video — immersion is a continuum, and lower-cost formats often achieve similar outcomes for declarative goals
- Individual rehearsal vs. multi-user collaborative scenarios (e.g., team-based emergency response)
- Standalone simulation vs. blended designs that interleave VR practice with classroom or on-the-job instruction [Blended Learning](../patterns/blended-learning.md)

### Target Learners
- Novices who need safe exposure to hazardous, rare, or high-stakes situations (surgery, firefighting, emergency response) before real practice
- Learners who benefit from embodied, spatially structured content — anatomy, architecture, spatial reasoning [Meta-analytic evidence finds VR effects on learning are small-to-moderate and highly heterogeneous across designs.](../claims/expertise-reversal-effect.md) [~M]
- Less valuable for learners who already have the procedural skill and need only refinement — the added immersion becomes redundant overhead [Guidance and elaborate media that help novices can hurt learners with higher prior knowledge.](../claims/expertise-reversal-effect.md) [~M]
- Novices in procedural, spatial, or high-risk domains who need safe repetition before real-world exposure [+S]
- Learners who benefit from embodied, first-person experience of rare or dangerous scenarios [~M]
- Less effective for learners still struggling with the interface itself, or for purely conceptual/verbal learning goals where simpler media suffice [-M]
- Novices in procedural, high-stakes domains (surgery, aviation, industrial safety) who need safe repetition before real performance [+M]
- Learners who benefit from spatially embodied understanding of environments and equipment layouts
- Less valuable for learners who already perform the task competently, unless the goal is rare-event or failure-mode rehearsal

### Target Learning Goals
- Procedural and psychomotor skill rehearsal under realistic constraints
- Spatial knowledge: navigating environments, understanding 3D structures
- Affective outcomes: empathy, threat response habituation, confidence/self-efficacy — outcomes where immersion shows its most consistent advantages [Meta-analytic evidence finds VR effects on learning are small-to-moderate and highly heterogeneous across designs.](../claims/expertise-reversal-effect.md) [+W]
- Procedural and psychomotor skill acquisition with safe, repeatable trials
- Spatial understanding of environments, equipment, or anatomy
- Situational readiness: recognizing hazards and making decisions under simulated pressure
- Affective outcomes such as empathy and attitude change, where presence shows promise [+W]
- Procedural skill acquisition and motor sequencing through repeated safe rehearsal
- Spatial and situational awareness: learning the layout and dynamics of a real environment
- Decision-making under pressure, including rare and emergency scenarios that cannot be staged safely
- Confidence and readiness: successful virtual performance builds self-efficacy that supports persistence in real settings [Self-efficacy predicts academic persistence.](../claims/self-efficacy-predicts-academic-persistence.md) [+M]

### Instructions
1. Define the observable performance the simulation must elicit; if the objective can be met with text or video, use the cheaper medium.
2. Deliver [Advance Organizers](../elements/advance-organizers.md) and interface pretraining before immersion to reduce extraneous load.
3. Run short, segmented immersion sessions with embedded [Feedback](../elements/feedback.md) on learner actions, following [Cognitive Load Management](../principles/cognitive-load-management.md) — signaling, segmenting, and removing decorative detail.
4. Follow immersion with [Practice](../elements/practice.md) in transfer contexts and a structured debrief, as in [Cognitive Apprenticeship](../patterns/cognitive-apprenticeship.md) (reflection and articulation phases).
5. Fade simulation support over repeated sessions — increasing scenario difficulty and removing prompts — consistent with [Scaffolding](../elements/scaffolding.md) and [Fading](../elements/fading.md).

## Related Strategies

- [Simulation-Based Training](simulation-based-training.md) — the broader category; VR is the immersive end of the simulation spectrum
- [Role-Play](acting-role-play.md) — the non-digital analogue; VR can scaffold toward live role-play
- [Flipped Classroom](flipped-classroom.md) — VR practice sessions can occupy the in-class active slot
- [Spaced Practice](../principles/spaced-learning.md) — repeated short VR sessions outperform massed immersion
- [Use AI-enabled immersive virtual environments to enrich project-based learning in vocational design education](ai-ive-pbl-vocational-design-strategy.md)
- [Use risk-free high-fidelity VR simulation to complement physical training for hazardous clinical procedures](risk-free-vr-pretraining-for-hazardous-procedures.md)
- [Case-based learning](case-based-learning.md) — alternative for decision-making goals where physical fidelity is unnecessary
- [Use simulated task environments for learning tasks so multimedia principles support inductive learning](simulated-task-environments-inductive-learning-strategy.md)
- [Structured activity design and moderate realism benefit shared VR learning environments](structured-activity-moderate-realism-vr.md)
- [Use advanced immersive learning technologies as research and learning tools to deliver developmentally-appropriate metacognitive scaffolding](immersive-tech-metacognitive-scaffolding-strategy.md)
- [Structure simulator sessions as short introductions followed by repeated task performance with teacher circulation and feedback.](simulator-session-structure-intro-repetition-teacher-circulation.md)
- [Combine error-amplification visual feedback with balance-based exergaming systems to expedite balance training for older adults, delivered via VR](ea-feedback-vr-exergaming-balance-older-adults.md)
- [Use immersive VR with virtual agents and eye-tracking to isolate and manipulate specific social factors (gaze, feedback, embodiment, multimodality) in L2 learning experiments](immersive-vr-social-l2-experiments.md)
- [Do not assume that reducing orientation effort automatically frees resources for deeper learning when orientation and learning happen simultaneously](cautious-orientation-support-dual-task-vr.md)
- [Supplement VR lessons with pre-training and follow-up reflection activities, and keep VR sessions short to limit fatigue and cybersickness](vr-sce-session-design-pretraining-reflection.md)
- [Immersive navigation inside musical rooms for active genre listening](immersive-musical-rooms-navigation.md)

## Examples
- **Osso VR** (https://ossovr.com) — hands-on surgical training simulations with performance analytics used in medical device training and residency preparation.
- **STRIVR** (https://www.strivr.com) — immersive training for workplace safety and operational procedures at companies including Walmart and Verizon, built on scenario repetition and debrief.
- **Firefighter and HazMat simulators** (e.g., FLAIM Systems, https://flaimsystems.com) — VR scenarios combining heat, smoke, and equipment simulation for hazardous-environment rehearsal.
- **Labster** (https://www.labster.com) — virtual science labs; its screen-based simulations are a widely studied lower-immersion comparison point for VR lab work.
- **Fundamentals of Laparoscopic Surgery (FLS)** — VR laparoscopic simulators with proficiency-based progression; the Seymour et al. (2002) trial showed VR-trained residents performed surgery 29% faster with fewer errors ([JAMA trial](https://jamanetwork.com/journals/jama/fullarticle/195478)).
- **Osso VR** — commercial surgical VR training platform using proficiency scoring and repeated immersive rehearsal ([ossovr.com](https://www.ossovr.com)).
- **STRIVR / Walmart Academies** — VR used at scale for retail operational and soft-skill scenarios (e.g., Black Friday crowd management), paired with on-the-floor practice.
- **Firefighter and hazmat VR drills** (e.g., [FLAIM Systems](https://flaimsystems.com)) — immersive hazard scenarios too dangerous to rehearse live, with after-action debrief.
- **Surgical training:** randomized studies of VR laparoscopic simulation (e.g., MIST-VR) show trainees trained in VR perform procedures faster and with fewer errors than conventionally trained controls [+M]
- **Walmart** used STRIVR's VR modules to prepare associates for high-pressure events (Black Friday, emergency procedures) at scale across thousands of stores
- **Flight simulation** — the longest-standing VR-adjacent training tradition; full-motion simulators are the regulatory standard for airline pilot certification

## Key Sources
- Makransky, G., & Petersen, G. B. (2021). The Cognitive Affective Model of Immersive Learning (CAMIL): A theoretical research-based model of learning in immersive virtual reality. *Educational Psychology Review, 33*(3), 937–959. [doi:10.1007/s10648-020-09586-2](https://doi.org/10.1007/s10648-020-09586-2)
- Parong, J., & Mayer, R. E. (2018). Learning science in immersive virtual reality. *Journal of Educational Psychology, 110*(6), 785–797. [doi:10.1037/edu0000241](https://doi.org/10.1037/edu0000241)
- Makransky, G., Terkildsen, T. S., & Mayer, R. E. (2019). Adding immersive virtual reality to a science lab simulation causes more presence but less learning. *Learning and Instruction, 60*, 225–236. [doi:10.1016/j.learninstruc.2017.12.007](https://doi.org/10.1016/j.learninstruc.2017.12.007)
- Hamilton, D., McKechnie, J., Edgerton, E., & Wilson, C. (2021). Immersive virtual reality as a pedagogical tool in education: A systematic literature review of quantitative learning outcomes and experimental design. *Journal of Computer Assisted Learning, 37*(1), 6–22. [doi:10.1007/s40692-020-00169-2](https://doi.org/10.1007/s40692-020-00169-2)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)
- Seymour, N. E., Gallagher, A. G., Roman, S. A., O'Brien, M. K., Bansal, V. K., Andersen, D. K., & Satava, R. M. (2002). Virtual reality training improves operating room performance: Results of a randomized, double-blinded study. *Annals of Surgery, 236*(4), 458–464. [doi:10.1097/00000658-200210000-00008](https://doi.org/10.1097/00000658-200210000-00008)
- Makransky, G., & Lilleholt, L. (2018). A structural equation modeling investigation of the emotional value of immersive virtual reality in education. *Computers & Education, 123*, 170–184. [doi:10.1007/s11423-018-9581-2](https://doi.org/10.1007/s11423-018-9581-2)
- Mayer, R. E. (2019). Computer multimedia training in virtual reality. In *Computer-Supported Multimedia Instruction* (pp. 419–427). Springer.
- Makransky, G., & Mayer, R. E. (2022). Benefits of immersion and presence in a virtual reality-based learning environment. *Educational Psychology Review, 34*, 2323–2345.
- Jensen, L., & Konradsen, F. (2018). A review of the use of virtual reality head-mounted displays in education and training. *Education and Information Technologies, 23*, 1515–1529. [doi:10.1007/s10639-017-9676-0](https://doi.org/10.1007/s10639-017-9676-0)

<!-- merged 2026-10-13 from strategies/virtual-reality-training ("Virtual Reality Training"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Virtual Reality Training

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 mixed, 1 against) · 5 studies (3 causal, 2 quant-synthesis), `q3`–`q4` · 1 of 5 report an effect size

## Description
Virtual Reality (VR) training places learners inside an interactive, three-dimensional simulated environment where they can rehearse procedures, manipulate equipment, and experience scenarios that would be dangerous, expensive, or impractical to stage in reality. Learning happens through embodied action — the learner performs the task (or a scaled version of it) rather than watching or reading about it, typically with system feedback on performance.

## Design Implications

VR training is most defensible where physical or situational fidelity matters: it allows safe, repeatable [practice](../elements/practice.md) on high-stakes tasks, and meta-analytic evidence shows simulation-based training with deliberate practice and structured feedback outperforms traditional instruction for procedural skills, most famously in surgical training, where residents trained with VR simulation reach proficiency faster and make fewer errors. But immersion is not instruction: high-fidelity visuals can consume working memory without adding learning value, and VR's novelty and sensory richness can depress learning relative to simpler media unless extraneous load is controlled [Immersive environments can impose extraneous cognitive load that reduces learning relative to desktop or video versions.](../claims/cognitive-overload-degrades-learning.md) [~S]. Effective designs pair immersion with pedagogy — pre-training, guided attention, feedback, and debriefing — rather than assuming presence alone produces learning.

### Context
#### Requirements
- A task with meaningful physical, spatial, or procedural fidelity requirements — VR earns its cost only when the simulation maps onto real performance
- Structured [feedback](../elements/feedback.md) within or immediately after the simulation; unguided free exploration produces weak outcomes
- Pre-training that orients learners to the interface and task goals before immersion, reducing load during the simulation
- A debriefing or reflection step connecting the simulated experience to transfer contexts
- Headsets and controllers, well-built virtual environments that faithfully represent the target task's critical features, and a facilitator or system that structures pre-briefing, practice, and debriefing
- Instructional scaffolding inside the simulation: prompts, [Coaching](../elements/coaching.md), and feedback tied to learner actions [Feedback is most effective at the task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]
- A pre-training orientation to the controls, so interface manipulation does not consume working memory during learning [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S]

#### Constraints
- Immersion without instructional scaffolding often underperforms desktop video or slides for declarative learning outcomes [VR's affective and behavioral advantages do not automatically translate to knowledge gains.](../claims/cognitive-overload-degrades-learning.md) [~S]
- High visual fidelity and decorative detail can hurt learning; irrelevant immersive detail competes with essential content [Coherence principle: irrelevant material hurts learning.](../claims/coherence-principle-irrelevant-material-hurts-learning.md) [-M]
- Interface manipulation itself (controllers, locomotion, menus) consumes working memory for novices, leaving less capacity for the target content [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]
- Cybersickness, equipment cost, and per-learner headset logistics limit session length and cohort scale
- Poor transfer when the simulation's affordances diverge from the real task (negative training)
- Passive or exploratory VR without guidance often underperforms simpler media: learners attend to surface features and miss the to-be-learned content, and immersion can add extraneous load that harms retention [~S] — pre-training on the interface and signaling of critical features mitigates this
- Cybersickness affects a substantial minority of users and degrades both experience and performance; session length and locomotion design matter
- High development and maintenance costs are only justified for tasks that are dangerous, rare, or expensive to practice otherwise — VR for content easily taught by text or video is a poor investment
- Transfer depends on *fidelity to the task*, not visual realism per se; photorealistic but procedurally shallow simulations add cost without learning benefit

#### Implementation Variability
- **Full-immersion headset VR** for spatial/procedural tasks (surgery, equipment operation, hazard response)
- **Desktop simulation / screen-based VR** — cheaper, scalable, often equally effective for declarative goals [~S]
- **360° video VR** — passive but immersive; suited to situational awareness and empathy-oriented goals
- **VR + debrief hybrid** — simulation followed by instructor-led review, the format with the strongest evidence base in medical simulation
- Fully immersive (head-mounted) vs. desktop simulation vs. 360° video — immersion is a continuum, and lower-cost formats often achieve similar outcomes for declarative goals
- Individual rehearsal vs. multi-user collaborative scenarios (e.g., team-based emergency response)
- Standalone simulation vs. blended designs that interleave VR practice with classroom or on-the-job instruction [Blended Learning](../patterns/blended-learning.md)

### Target Learners
- Novices in procedural, spatial, or high-risk domains who need safe repetition before real-world exposure [+S]
- Learners who benefit from embodied, first-person experience of rare or dangerous scenarios [~M]
- Less effective for learners still struggling with the interface itself, or for purely conceptual/verbal learning goals where simpler media suffice [-M]
- Novices in procedural, high-stakes domains (surgery, aviation, industrial safety) who need safe repetition before real performance [+M]
- Learners who benefit from spatially embodied understanding of environments and equipment layouts
- Less valuable for learners who already perform the task competently, unless the goal is rare-event or failure-mode rehearsal

### Target Learning Goals
- Procedural and psychomotor skill acquisition with safe, repeatable trials
- Spatial understanding of environments, equipment, or anatomy
- Situational readiness: recognizing hazards and making decisions under simulated pressure
- Affective outcomes such as empathy and attitude change, where presence shows promise [+W]
- Procedural skill acquisition and motor sequencing through repeated safe rehearsal
- Spatial and situational awareness: learning the layout and dynamics of a real environment
- Decision-making under pressure, including rare and emergency scenarios that cannot be staged safely
- Confidence and readiness: successful virtual performance builds self-efficacy that supports persistence in real settings [Self-efficacy predicts academic persistence.](../claims/self-efficacy-predicts-academic-persistence.md) [+M]

### Instructions
1. Define the observable performance the simulation must train and verify the simulation maps onto it (avoid negative training).
2. Deliver pre-training: task goals, interface orientation, and an [advance organizer](../elements/advance-organizers.md) for the procedure.
3. Run short, focused simulation episodes with embedded [feedback](../elements/feedback.md) on actions, not just outcomes.
4. Require repeated, increasingly difficult trials until a proficiency criterion is met — deliberate practice, not time-on-task [+S].
5. Debrief: connect simulated performance to real-world conditions and common errors.
6. Follow with real or high-fidelity [practice](../elements/practice.md) to confirm transfer.

## Related Strategies

- [Simulation-based training](simulation-based-training.md) — the broader family; VR is the immersive end of the fidelity spectrum
- [Role-play](acting-role-play.md) — low-tech embodied rehearsal sharing the same active-performance logic
- [Case-based learning](case-based-learning.md) — alternative for decision-making goals where physical fidelity is unnecessary
- [Use risk-free high-fidelity VR simulation to complement physical training for hazardous clinical procedures](risk-free-vr-pretraining-for-hazardous-procedures.md)
- [Flipped Classroom](flipped-classroom.md) — VR sessions can serve as the application layer after preparatory study
- [Use AI-enabled immersive virtual environments to enrich project-based learning in vocational design education](ai-ive-pbl-vocational-design-strategy.md)

## Examples
- **Fundamentals of Laparoscopic Surgery (FLS)** — VR laparoscopic simulators with proficiency-based progression; the Seymour et al. (2002) trial showed VR-trained residents performed surgery 29% faster with fewer errors ([JAMA trial](https://jamanetwork.com/journals/jama/fullarticle/195478)).
- **Osso VR** — commercial surgical VR training platform using proficiency scoring and repeated immersive rehearsal ([ossovr.com](https://www.ossovr.com)).
- **STRIVR / Walmart Academies** — VR used at scale for retail operational and soft-skill scenarios (e.g., Black Friday crowd management), paired with on-the-floor practice.
- **Firefighter and hazmat VR drills** (e.g., [FLAIM Systems](https://flaimsystems.com)) — immersive hazard scenarios too dangerous to rehearse live, with after-action debrief.
- **Surgical training:** randomized studies of VR laparoscopic simulation (e.g., MIST-VR) show trainees trained in VR perform procedures faster and with fewer errors than conventionally trained controls [+M]
- **Walmart** used STRIVR's VR modules to prepare associates for high-pressure events (Black Friday, emergency procedures) at scale across thousands of stores
- **Flight simulation** — the longest-standing VR-adjacent training tradition; full-motion simulators are the regulatory standard for airline pilot certification

## Key Sources
- Seymour, N. E., Gallagher, A. G., Roman, S. A., O'Brien, M. K., Bansal, V. K., Andersen, D. K., & Satava, R. M. (2002). Virtual reality training improves operating room performance: Results of a randomized, double-blinded study. *Annals of Surgery, 236*(4), 458–464. [doi:10.1097/00000658-200210000-00008](https://doi.org/10.1097/00000658-200210000-00008)
- Makransky, G., & Petersen, G. B. (2021). The Cognitive Affective Model of Immersive Learning (CAMIL): A theoretical research-based model of learning in immersive virtual reality. *Educational Psychology Review, 33*(3), 937–959. [doi:10.1007/s10648-020-09586-2](https://doi.org/10.1007/s10648-020-09586-2)
- Makransky, G., & Lilleholt, L. (2018). A structural equation modeling investigation of the emotional value of immersive virtual reality in education. *Computers & Education, 123*, 170–184. [doi:10.1007/s11423-018-9581-2](https://doi.org/10.1007/s11423-018-9581-2)
- Mayer, R. E. (2019). Computer multimedia training in virtual reality. In *Computer-Supported Multimedia Instruction* (pp. 419–427). Springer.
- Makransky, G., & Mayer, R. E. (2022). Benefits of immersion and presence in a virtual reality-based learning environment. *Educational Psychology Review, 34*, 2323–2345.
- Parong, J., & Mayer, R. E. (2018). Learning science in immersive virtual reality. *Journal of Educational Psychology, 110*(6), 785–797. [doi:10.1037/edu0000241](https://doi.org/10.1037/edu0000241)
- Jensen, L., & Konradsen, F. (2018). A review of the use of virtual reality head-mounted displays in education and training. *Education and Information Technologies, 23*, 1515–1529. [doi:10.1007/s10639-017-9676-0](https://doi.org/10.1007/s10639-017-9676-0)

<!- - merged 2026-10-13 from strategies/virtual-reality-vr-training ("Virtual Reality (VR) Training"),  a duplicate of this page: its body as it stood. Its bullets this page lacked were added above.

# Virtual Reality (VR) Training

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 11 studies (4 quant-synthesis, 4 review, 3 causal), `q2`–`q4` · 3 of 11 report an effect size · 1 claim rests on one study

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
6. **Space the rehearsal** — distribute repeat sessions over time rather than massing them [Spaced repetition improves retention.](../claims/spaced-practice-improves-retention.md) [+S]

## Related Strategies

- [Simulation-Based Training](simulation-based-training.md) — the broader family; VR is its most immersive form
- [Role-Play](acting-role-play.md) — low-tech embodiment of the same principle of enacted practice
- [Flipped Classroom](flipped-classroom.md) — VR sessions can serve as the application layer after preparatory study
- [Use AI-enabled immersive virtual environments to enrich project-based learning in vocational design education](ai-ive-pbl-vocational-design-strategy.md)
- [Use risk-free high-fidelity VR simulation to complement physical training for hazardous clinical procedures](risk-free-vr-pretraining-for-hazardous-procedures.md)

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
- Makransky, G., & Mayer, R. E. (2022). Benefits of immersion and presence in a virtual reality-based learning environment. *Educational Psychology Review, 34*, 2323–2345.
- Parong, J., & Mayer, R. E. (2018). Learning science in immersive virtual reality. *Journal of Educational Psychology, 110*(6), 785–797. [doi:10.1037/edu0000241](https://doi.org/10.1037/edu0000241)
- Jensen, L., & Konradsen, F. (2018). A review of the use of virtual reality head-mounted displays in education and training. *Education and Information Technologies, 23*, 1515–1529. [doi:10.1007/s10639-017-9676-0](https://doi.org/10.1007/s10639-017-9676-0)
- Seymour, N. E., Gallagher, A. G., Roman, S. A., O'Brien, M. K., Bansal, V. K., Andersen, D. K., & Satava, R. M. (2002). Virtual reality training improves operating room performance: Results of a randomized, double-blinded study. *Annals of Surgery, 236*(4), 458–464. [doi:10.1097/00000658-200210000-00008](https://doi.org/10.1097/00000658-200210000-00008)
- ->
-->
