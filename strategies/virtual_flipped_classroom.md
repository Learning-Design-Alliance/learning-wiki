---
type: strategy
title: Virtual Flipped Classroom
description: A fully online variant of the flipped classroom in which all instruction is delivered asynchronously and synchronous contact is reserved for individualized tutoring and office hours.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
sources:
  - id: strelan-2020
    resource: "https://doi.org/10.1016/j.edurev.2019.100314"
    title: "Strelan, P., Osborn, A., & Palmer, E. (2020). The flipped classroom: A meta-analysis of effects on student performance across disciplines and education levels. *Educational Research Review, 30*, 100314"
    author: "Strelan, P., Osborn, A., & Palmer, E"
  - id: van-alten-2019
    resource: "https://doi.org/10.1016/j.edurev.2019.100303"
    title: "van Alten, D. C. D., Phielix, C., Janssen, J., & Kester, L. (2019). Effects of flipping the classroom on learning outcomes and satisfaction: A meta-analysis. *Educational Research Review, 28*, 100303"
    author: "van Alten, D. C. D., Phielix, C., Janssen, J., & Kester, L"
  - id: bergmann-2012
    resource: "https://doi.org/10.4135/9781544318497"
    title: "Bergmann, J., & Sams, A. (2012). *Flip your classroom: Reach every student in every class every day*. ISTE/ASCD"
    author: "Bergmann, J., & Sams, A"
---

# Virtual Flipped Classroom

## Description
A virtual flipped classroom moves all first-exposure instruction — videos, readings, worked examples — into asynchronous online modules, and reserves synchronous online sessions for application: problem-solving, discussion, feedback, and individualized tutoring. Unlike the blended [Flipped Classroom](../patterns/flipped-classroom.md), there is no physical classroom; the "group space" is a video conference or collaborative online environment, and the instructor's synchronous role shifts from presenter to coach.

## Design Implications

The flipped model's advantage comes from spending scarce synchronous time on active application rather than transmission [Active learning improves exam performance relative to lecture transmission.](../claims/active-learning-improves-exam-performance.md) [+S], and meta-analytic evidence supports flipped designs over traditional lecture across disciplines [Strelan et al., 2020](https://doi.org/10.1016/j.edurev.2019.100314) [+M]. In the fully virtual variant, the asynchronous layer must do more motivational and structural work, since learners complete it alone and without the social accountability of an upcoming class meeting.

### Context
#### Requirements
- Short, focused asynchronous instruction (ideally 6–12 minute segments) with embedded questions or prompts to enforce engagement
- A pre-class comprehension check that lets the instructor calibrate the synchronous session to actual gaps ([Assessment](../elements/assessment.md) used formatively)
- Synchronous sessions structured around application tasks — problem sets, case discussion, peer critique — not re-delivery of the asynchronous content
- Low-stakes accountability for preparation, since voluntary pre-work completion is the model's most common failure point

#### Constraints
- Without accountability or embedded checks, a large share of students skip the asynchronous preparation, collapsing the synchronous session into re-teaching [van Alten et al., 2019](https://doi.org/10.1016/j.edurev.2019.100303) [~M]
- Students with low self-regulation skills struggle more in flipped designs, where responsibility for first exposure shifts to the learner [van Alten et al., 2019](https://doi.org/10.1016/j.edurev.2019.100303) [-M]
- Fully virtual delivery removes the informal monitoring cues of a physical room; instructors need explicit [Check-Ins](../elements/check-in.md) and small-group structures to detect confusion
- Increased instructor workload for producing media and facilitating online sessions can degrade quality if the model is adopted without time to build materials [Bergmann & Sams, 2012](https://doi.org/10.4135/9781544318497) [~W]

#### Implementation Variability
- **Individual vs. group space emphasis:** some implementations make synchronous sessions optional office hours; others run required collaborative workshops. Required application sessions show stronger outcomes.
- **Synchronous session size:** one-to-one or small-group tutoring maximizes the individualization benefit; large synchronous lectures forfeit the model's main advantage.
- **Asynchronous interactivity:** embedding questions in video (e.g., PlayPosit, H5P) versus passive viewing — interactive versions better protect preparation quality.

### Target Learners
- Students with basic self-regulation skills who can manage asynchronous first exposure independently
- Underprepared students benefit disproportionately from the ability to pause, rewatch, and re-attempt instruction [Strelan et al., 2020](https://doi.org/10.1016/j.edurev.2019.100314) [+M]
- Less suitable for students with very weak self-regulation unless paired with structured deadlines and scaffolds [van Alten et al., 2019](https://doi.org/10.1016/j.edurev.2019.100303) [~M]

### Target Learning Goals
- Procedural and problem-solving skill, where synchronous time is spent applying what was studied asynchronously
- Conceptual understanding deepened through discussion and feedback during live sessions
- Self-regulated learning, since the format itself requires students to manage their preparation

### Instructions
1. Publish short asynchronous instruction (video, reading, or [Worked Examples](../principles/worked-examples.md)) with an advance organizer stating what learners should be able to do afterward ([Advance Organizers](../elements/advance-organizers.md)).
2. Embed comprehension questions in the asynchronous material and require a brief pre-session check-in ([Check-In](../elements/check-in.md)) to surface gaps.
3. Use the check data to design the synchronous session around the hardest unresolved problems, not content review.
4. Run the synchronous session as active application: small-group problem solving, [Class Discussion](../elements/class-discussion.md), or peer feedback, with the instructor circulating as a coach ([Coaching](../elements/coaching.md)).
5. Follow with individual or group [Practice](../elements/practice.md) and close the loop with feedback targeted at task and process levels [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].

## Related Strategies
- Station-Rotation Blended Learning — the physical-room cousin; same inversion logic with scheduled rotation instead of full virtualization
- Peer Instruction — a common structure for the synchronous application session in virtual flipped courses
- Asynchronous Discussion Protocols — an alternative application layer when synchronous attendance is impractical

## Examples
- **Michigan State University's fully online flipped calculus courses** — students watch short videos and complete online checks before live problem-solving sessions; published studies report improved pass rates over lecture-based online sections.
- **[Khan Academy](https://www.khanacademy.org)** used as the asynchronous layer — narrated demonstrations with embedded practice — freeing synchronous time for tutoring.
- **Coursera MOOCs with live "office hours"** (e.g., Andrew Ng's Machine Learning specializations) — asynchronous lectures plus optional synchronous Q&A and application support.

## Key Sources
- Strelan, P., Osborn, A., & Palmer, E. (2020). The flipped classroom: A meta-analysis of effects on student performance across disciplines and education levels. *Educational Research Review, 30*, 100314. [doi:10.1016/j.edurev.2020.100314](https://doi.org/10.1016/j.edurev.2020.100314)
- van Alten, D. C. D., Phielix, C., Janssen, J., & Kester, L. (2019). Effects of flipping the classroom on learning outcomes and satisfaction: A meta-analysis. *Educational Research Review, 28*, 100303. [doi:10.1016/j.edurev.2019.100303](https://doi.org/10.1016/j.edurev.2019.100303)
- Bergmann, J., & Sams, A. (2012). *Flip your classroom: Reach every student in every class every day*. ISTE/ASCD. [doi:10.4135/9781544318497](https://doi.org/10.4135/9781544318497)
- Freeman, S., et al. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)

