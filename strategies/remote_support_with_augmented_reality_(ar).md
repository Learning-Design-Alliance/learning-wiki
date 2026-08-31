---
type: strategy
title: Remote Support with Augmented Reality (AR)
description: AR apps allow technicians and users to communicate with experts in real time, with annotations overlaid on the user's field of view.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Remote Support with Augmented Reality (AR)

## Description
Remote AR support connects a field worker or novice with a remote expert through a shared augmented view: the local user's camera feed is transmitted to the expert, who overlays annotations (arrows, circles, drawings, 3D pointers) directly onto objects in the user's field of view. Because the expert sees what the learner sees, spatial references that are notoriously ambiguous in voice-only support ("the bolt to the left of the valve") become unambiguous. AR headsets can additionally connect to IoT sensors and diagnostic data, surfacing equipment state in the same view as the guidance.

## Design Implications

Remote AR support is essentially [Demonstration](../elements/demonstration.md) and [Scaffolding](../principles/scaffolding.md) delivered in situ: the expert models and guides a task in the learner's actual work context, which supports [Situated Learning](../theories/situated-learning.md) by anchoring instruction in the authentic environment and equipment [+W]. Compared with voice-only remote support, shared visual reference measurably reduces task completion time and communication errors [+M], though the advantage depends on task type — it is largest for spatially complex, manipulation-heavy tasks and smallest for simple verbal troubleshooting [~M]. A key learning-design risk is that the expert's annotations can become a crutch: learners execute steps without building transferable schemas, so sessions should be structured to fade support and require learner articulation [Contingent scaffolding improves learning.](../claims/contingent-scaffolding-improves-learning.md) [+M].

### Context
#### Requirements
- AR-capable hardware (smartphone, tablet, or headset) with a stable, high-bandwidth connection on both ends
- A remote expert with access to the same visual context and, ideally, diagnostic data (IoT sensors, manuals, schematics)
- An annotation interface that lets the expert point, draw, and anchor marks to objects rather than to screen coordinates
- A debrief or documentation step so the guidance persists beyond the live session

#### Constraints
- Poor signal quality or latency degrades the shared reference and can make AR support worse than a phone call [-M]
- Annotation-heavy guidance can induce [cognitive overload](../claims/cognitive-overload-degrades-learning.md) [-M] when overlaid marks, camera view, and instructions compete for visual attention; experts must annotate sparingly
- Heavy reliance on expert direction can suppress the learner's own troubleshooting skill development; without fading, learners remain dependent [-W]
- Hands-free operation matters: holding a tablet while manipulating equipment splits attention and degrades performance [-M]

#### Implementation Variability
- **Headset-based** (e.g., HoloLens, RealWear) for hands-free field work vs. **mobile-based** (TeamViewer Pilot, AR Assist) for lower-cost deployment
- **Live expert** vs. **recorded AR overlays** replayed as just-in-time procedural guidance
- **Expert-led** (expert drives each step) vs. **learner-led** (learner attempts, expert intervenes on error), which better supports skill acquisition

### Target Learners
- Novice technicians and field workers performing unfamiliar repair or maintenance tasks [+W]
- Remote workers who lack physical access to experts; particularly valuable where travel is costly or equipment downtime is expensive
- Less beneficial for experienced technicians, for whom expert annotation adds little beyond what they already know [~W]

### Target Learning Goals
- Procedural skill acquisition: executing repair and assembly steps correctly in context
- Troubleshooting and diagnosis: connecting observed symptoms to causes, supported by sensor data overlays
- Communication and collaboration: learning to give and receive precise spatial references during remote work

### Instructions
1. **Establish the shared view** — confirm the learner's camera feed and connection quality before beginning ([Gain Attention](../elements/gain-attention.md)).
2. **Diagnose together** — have the learner describe symptoms while the expert overlays annotations; connect observations to sensor or diagnostic data ([Application](../elements/application.md)).
3. **Model the first intervention** — the expert demonstrates the fix with annotations while narrating reasoning ([Articulation](../elements/articulation.md)).
4. **Fade to learner-led execution** — the learner performs subsequent steps while the expert intervenes only on error ([Practice](../elements/practice.md)).
5. **Debrief and document** — capture the annotated session as a reusable reference and have the learner restate the procedure in their own words.

## Related Strategies
- Remote Expert Consultation — voice/video-only predecessor; AR adds shared spatial reference
- Just-in-Time Performance Support — recorded AR overlays serve the same function asynchronously
- Video Coaching — similar expert-observation loop without in-context annotation

## Related Elements
- [Demonstration](../elements/demonstration.md) — the expert's annotated modeling is a demonstration embedded in the learner's own environment
- [Practice](../elements/practice.md) — learner-led execution with expert backup is the practice phase
- [Articulation](../elements/articulation.md) — requiring learners to verbalize steps prevents passive dependence on annotations
- [Application](../elements/application.md) — the repair task itself is the authentic application context

## Tools
- **TeamViewer Pilot** — mobile AR remote support with expert annotation
- **Microsoft Dynamics 365 Remote Assist** (HoloLens) — headset-based expert collaboration with Teams integration
- **PTC Vuforia Chalk** — remote AR assistance with object-anchored annotations

## Examples
- **Field service (manufacturing)**: A technician repairing a production line uses Dynamics 365 Remote Assist to share a HoloLens view with a remote engineer, who circles the faulty valve and overlays the correct torque sequence, cutting downtime versus a parts-by-phone call.
- **Medical device support**: Hospital biomedical staff use AR annotation sessions with equipment vendors to troubleshoot imaging hardware on-site without waiting for a site visit.
- **Utilities training**: New line workers complete supervised procedures via AR remote guidance, with sessions recorded and annotated overlays reused as just-in-time references for the next cohort.

## Key Sources
- Dey, A., Billinghurst, M., Lindeman, R. W., & Swan, J. E. (2018). A systematic review of 10 years of research on augmented reality remote collaboration. *Computers & Graphics, 74*, 13–37.
- Billinghurst, M., Clark, A., & Lee, G. (2015). A survey of augmented reality. *Foundations and Trends in Human–Computer Interaction, 8*(2–3), 73–272. [doi:10.1561/1100000049](https://doi.org/10.1561/1100000049)
- Garzón, J., & Acevedo, J. (2019). Meta-analysis of the impact of augmented reality on students' learning gains. *Educational Research Review, 27*, 244–260. [doi:10.1016/j.edurev.2019.04.001](https://doi.org/10.1016/j.edurev.2019.04.001)
- Radu, I. (2014). Augmented reality in education: A meta-review and cross-media analysis. *Computers & Education, 73*, 1–11. [doi:10.1007/s00779-013-0747-y](https://doi.org/10.1007/s00779-013-0747-y)
- Zhu, J., Mosher, R., Mendoza, R., & Antonenko, P. (2019). The effects of augmented reality on spatial ability and learning achievement. *Educational Technology Research and Development, 67*, 1041–1059. [doi:10.1007/s11423-018-9636-2](https://doi.org/10.1007/s11423-018-9636-2)