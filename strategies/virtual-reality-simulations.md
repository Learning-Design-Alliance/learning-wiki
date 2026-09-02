---
type: strategy
id: virtual-reality-simulations
title: Virtual Reality Simulations
description: Immersive, computer-generated environments that let learners enact procedures, explore phenomena, or rehearse decisions in a safe, controlled replica of a real setting.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Virtual Reality Simulations

> **Strategy** · [All strategies](index.md)

## Description
Virtual reality (VR) simulations place learners inside an interactive, computer-generated environment where they can perform procedures, manipulate objects, and experience scenarios that would be dangerous, expensive, or impractical in the real world. Learning is carried out through embodied action — the learner *does* the task (or a scaled version of it) rather than reading or watching about it, typically with system feedback on performance.

## Design Implications

VR's core pedagogical value is safe, repeatable practice of procedural and spatial tasks with immediate feedback, which meta-analytic evidence supports over conventional instruction, particularly in health professions and technical training [Kyaw et al., 2019] [+M]. However, immersion is not instruction: VR's novelty and sensory richness impose extraneous load, and learning gains depend on embedding sound instructional design (clear objectives, guidance, debriefing) inside the simulation [Makransky & Mayer, 2022] [~M]. The medium amplifies whatever design it contains — a well-structured simulation teaches; a poorly structured one merely entertains.

### Context
#### Requirements
- Clearly defined learning objectives that map to actions the learner can actually perform in the environment
- Embedded guidance: prompts, hints, or an in-scenario coach ([Scaffolding](../principles/scaffolding.md)) rather than free exploration
- Performance feedback and a structured debrief after the scenario ([Assessment](../elements/assessment.md), [Practice](../elements/practice.md))
- Attention to cognitive load: segment scenarios, minimize decorative detail, and pretrain on controls before content [Makransky & Mayer, 2022] [+M]

#### Constraints
- High extraneous cognitive load from immersive detail and interface manipulation can degrade learning, especially for novices [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-M]
- Novelty effects inflate short-term engagement measures but do not reliably produce retention gains [Makransky & Mayer, 2022] [~W]
- Cybersickness and headset discomfort limit session length and exclude some learners (vestibular disorders, young children) [-M]
- Cost, content-development effort, and device logistics make VR inefficient for verbal/conceptual goals that a text or video would serve as well [-M]
- Unstructured "exploration" in open virtual environments often produces wandering rather than learning [~M]

#### Implementation Variability
- **Fully immersive (headset)** vs. **desktop simulation** — desktop versions often achieve comparable learning outcomes at far lower cost [Kyaw et al., 2019] [~M]
- **Procedural rehearsal** (surgical steps, lab safety) vs. **decision rehearsal** (triage, crisis management) vs. **spatial exploration** (anatomy, field sites)
- **Single-user** vs. **multi-user collaborative scenarios** with role assignment
- **360° video** as a low-cost middle ground for observational (non-manipulative) learning

### Target Learners
- Novices in high-stakes procedural domains (medicine, aviation, laboratory science, trades) who need safe rehearsal before real performance [Kyaw et al., 2019] [+M]
- Learners who benefit from spatial/embodied understanding of structures and processes that are hard to convey in 2D [~M]
- Less valuable for learners whose goals are purely verbal, conceptual, or argumentative — the added immersion adds cost without adding learning [Makransky & Mayer, 2022] [~M]

### Target Learning Goals
- Procedural skill acquisition and psychomotor rehearsal
- Spatial knowledge: anatomy, architecture, molecular structure, terrain
- Decision-making under realistic constraints and time pressure
- Affective outcomes: empathy and perspective-taking through embodied role experience [~W]

### Instructions
1. Define the observable performance the simulation should train and how success will be measured ([Assessment](../elements/assessment.md)).
2. Pretrain learners on the interface and domain vocabulary outside VR to free working memory for the task itself ([Cognitive Load Management](../principles/cognitive-load-management.md)) [+M].
3. Run a guided scenario with embedded prompts and feedback ([Practice](../elements/practice.md), [Scaffolding](../principles/scaffolding.md)); increase difficulty or variability across repeated runs ([Adaptive Difficulty](../elements/adaptive-difficulty.md)).
4. Debrief immediately after the scenario — compare learner decisions against expert decisions and edge cases ([Case Studies](../elements/case-studies.md)) [+M].
5. Follow with transfer tasks in a different format (real equipment, written cases) to check that learning did not stay trapped in the virtual context [~M].

## Related Strategies
- [Simulation-based practice with manikins](simulation-based-practice.md) — the physical-equipment analogue; VR often substitutes for or precedes it
- [Case-based discussion](case-based-discussion.md) — the debrief structure from case methods transfers directly to post-scenario reflection
- [Video-based modeling](video-based-modeling.md) — a lower-cost observational alternative when manipulation is not required

## Examples
- **Osso VR** (https://ossovr.com) — surgical rehearsal platform; randomized studies showed orthopedic trainees using it outperformed conventionally trained peers on assessed procedure performance [+M]
- **Labster** (https://www.labster.com) — virtual science laboratory simulations used in university chemistry and biology courses, with embedded quizzes and guided storylines
- **vSim for Nursing** (https://www.elsevier.com/vsim) — Wolters Kluwer/Laerdal patient scenarios with branching decisions and post-simulation debriefing worksheets
- **Google Expeditions (archived)** — 360° field-trip VR for K-12; a large-scale study found learning gains only when paired with structured, teacher-guided tasks rather than free exploration [~M]

## Key Sources
- Kyaw, B. M., Saxena, N., Posadzki, P., Vseteckova, J., Nikolaou, C. K., George, P. P., Divakar, U., Masiello, I., Kononowicz, A. A., Zary, N., & Tudor Car, L. (2019). Virtual reality for health professions education: Systematic review and meta-analysis. *Journal of Medical Internet Research, 21*(1), e12959. [doi:10.2196/12959](https://doi.org/10.2196/12959)
- Makransky, G., & Mayer, R. E. (2022). Benefits and costs of immersive virtual reality learning environments: A learning sciences perspective. *Nature Reviews Psychology, 1*, 691–707. [doi:10.4324/9781003386131-13](https://doi.org/10.4324/9781003386131-13)
- Makransky, G., & Petersen, G. B. (2021). The Cognitive Affective Model of Immersive Learning (CAMIL): A theoretical research-based model of learning in immersive virtual reality. *Educational Research Review, 34*, 100417. [doi:10.1007/s10648-020-09586-2](https://doi.org/10.1007/s10648-020-09586-2)
- Mayer, R. E. (2021). *Multimedia Learning* (3rd ed.). Cambridge University Press. [doi:10.1017/9781316941355](https://doi.org/10.1017/9781316941355)