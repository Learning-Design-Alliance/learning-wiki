---
type: strategy
title: Augmented Reality (AR) for Space Industry Training
description: Augmented reality overlays digital work instructions and 3D visualizations onto the physical workspace, supporting astronauts and ground crews in complex maintenance, assembly, and exploration-preparation tasks.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Augmented Reality (AR) for Space Industry Training

## Description
Augmented reality overlays task-relevant digital content — 3D models, step-by-step visual instructions, labels, and remote expert annotations — onto the learner's real workspace, so guidance appears in the location where the work is performed. NASA's Project Sidekick, developed with Microsoft HoloLens, exemplifies this approach: crew members receive virtual holographic illustrations overlaid on equipment during International Space Station maintenance, eliminating the need to cross-reference paper manuals mid-task. AR is also used to reconstruct the Martian landscape from surface photography, giving scientists and astronauts realistic environmental rehearsal for exploration missions.

## Design Implications

AR's core learning advantage is spatial contiguity: instructions are presented at the point of action, reducing the working-memory cost of holding procedural steps in mind while locating and manipulating hardware [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+M]. Well-designed AR functions as just-in-time [Practice](../elements/practice.md) support rather than a replacement for it — the overlay guides performance while the learner builds the underlying schema through doing. Meta-analyses of AR in education find moderate positive effects on learning outcomes overall, but effects depend heavily on instructional design quality rather than the technology itself [Garzón & Acevedo, 2019] [+M].

### Context
#### Requirements
- AR headsets (e.g., HoloLens) or tablet-based AR clients, with ruggedized hardware for operational environments
- Accurate 3D models and task-sequenced content authored with domain experts
- Network connectivity for remote-expert modes (or offline content packages for spaceflight, where bandwidth is scarce)
- A follow-on structure of guided [Practice](../elements/practice.md) and [Assess Performance](../elements/assess-performance.md) so the overlay can be faded

#### Constraints
- Poorly integrated AR can *increase* cognitive load: split attention between the overlay and the physical task, or cluttered displays, degrade performance [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [-S]
- Over-reliance on persistent visual prompts can produce dependency — learners perform well with the overlay but fail when it is removed; guidance must be faded as expertise grows [Expertise reversal effect.](../claims/expertise-reversal-effect.md) [~M]
- Limited haptic feedback means AR rehearsal cannot fully substitute for physical training on force-sensitive tasks
- Content creation and maintenance require sustained engineering and SME effort; stale overlays on modified hardware are worse than no overlay

#### Implementation Variability
- **Headset AR** (Sidekick-style): hands-free, suited to two-handed maintenance tasks
- **Tablet/monitor AR**: lower cost, suited to ground training and procedure familiarization
- **Remote-expert mode**: a ground controller annotates the crew member's live view — a form of [Coaching](../elements/coaching.md) at distance
- **Simulated environments**: photogrammetric reconstructions of Mars terrain for geology traverse rehearsal, a form of [Anchored Instruction](../elements/anchored-instruction.md) in authentic context

### Target Learners
- Novices and infrequent performers of complex procedures (astronauts trained on many systems, ground crew rotating across tasks), where point-of-work guidance reduces unguided search [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [+M]
- Expert crews benefit mainly from AR as a job aid, not as instruction — full overlays become redundant and intrusive for highly practiced tasks [Expertise reversal effect.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Procedural fluency: executing multi-step maintenance and assembly sequences accurately
- Spatial understanding: internalizing the 3D structure of equipment and environments (dual coding of verbal and visual channels supports this [Dual coding improves recall.](../claims/dual-coding-improves-recall.md) [+M])
- Situated readiness: rehearsing exploration tasks in realistic reconstructed environments

### Instructions
1. **Model the task**: present the procedure via [Direct Instruction](../elements/direct-instruction.md) or expert demonstration before first hands-on contact.
2. **Overlay guidance**: deliver step-by-step holographic work instructions during initial [Practice](../elements/practice.md) attempts, keeping each display chunk minimal.
3. **Coach remotely**: use expert annotation of the learner's live view for corrective [Coaching](../elements/coaching.md) during early performance.
4. **Fade the overlay**: progressively reduce prompt completeness (full hologram → labels → checklist) as fluency develops.
5. **Assess and apply**: verify unaided performance via [Assess Performance](../elements/assess-performance.md), then transfer to [Application](../elements/application.md) on operational hardware.

## Related Strategies
- [Simulation-based training](simulation-based-training.md) — AR is one modality within the broader simulation family; both trade fidelity against cost
- [Performance support / job aids](performance-support-job-aids.md) — AR work instructions are job aids delivered at the point of need rather than before it

## Examples
- **[NASA Project Sidekick](https://www.nasa.gov/directorates/heo/scan/engineering/technology/project_sidekick/)** — HoloLens-based holographic instructions and remote-expert "Sidekick" calls used on the International Space Station for maintenance and science procedures.
- **ESA astronaut training with AR/VR** — European Space Agency uses mixed-reality reconstructions of station modules to rehearse procedures before parabolic-flight and on-orbit execution.
- **Mars terrain reconstruction** — photogrammetric models built from rover imagery (e.g., Curiosity and Perseverance data) let scientists rehearse traverse and sampling decisions in the actual terrain before commanding the real rover.

## Key Sources
- Azuma, R. T. (1997). A survey of augmented reality. *Presence: Teleoperators and Virtual Environments, 6*(4), 355–385. [doi:10.1162/pres.1997.6.4.355](https://doi.org/10.1162/pres.1997.6.4.355)
- Wu, H.-K., Lee, S. W.-Y., Chang, H.-Y., & Liang, J.-C. (2013). Current status, opportunities and challenges of augmented reality in education. *Computers & Education, 62*, 41–49. [doi:10.1016/j.compedu.2012.10.024](https://doi.org/10.1016/j.compedu.2012.10.024)
- Radu, I. (2014). Augmented reality in education: A meta-review and cross-media analysis. *Computers & Education, 73*, 1–11. [doi:10.1007/s00779-013-0747-y](https://doi.org/10.1007/s00779-013-0747-y)
- Garzón, J., & Acevedo, J. (2019). Meta-analysis of the impact of augmented reality on students' learning gains. *Educational Research Review, 27*, 244–260. [doi:10.1016/j.edurev.2019.100303](https://doi.org/10.1016/j.edurev.2019.100303)