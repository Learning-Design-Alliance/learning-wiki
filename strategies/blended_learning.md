---
type: strategy
title: Blended Learning
description: Blended learning combines face-to-face instruction with online learning through an LMS, offering the advantages of direct interaction and the convenience of eLearning.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Blended Learning

> **Strategy** · [All strategies](index.md)

## Description
Blended learning combines face-to-face instruction with online learning through an LMS, offering the advantages of direct interaction and the convenience of eLearning. It involves live training sessions, additional online resources, and assignments to ensure complete understanding. The defining design decision is *which* activities go in each mode: typically, content delivery and self-paced work move online, while scarce in-person time is reserved for interaction, feedback, and application.

## Design Implications

Blended designs outperform either mode alone when the two components are deliberately integrated rather than parallel offerings — a "course-and-a-half" of redundant content produces no gains [~M]. Meta-analytic evidence indicates blended instruction modestly outperforms purely face-to-face instruction, but that the advantage is driven by added instructional time and materials, not the medium itself [~S]. The strongest designs use online time for content exposure and [Practice](../elements/practice.md), and free in-person time for [Active Learning](../principles/active-learning.md) [Active learning improves exam performance relative to lecture.](../claims/active-learning-improves-exam-performance.md) [+S].

### Context
#### Requirements
- An LMS that supports a wide range of content formats (video, documents, quizzes) and tracks completion
- Face-to-face facilities and instructors skilled in both modes
- Explicit integration: online and in-person activities must reference and build on each other, not run as separate tracks
- Alignment of each activity to the mode that serves it best — e.g., [Lectures](../elements/lectures.md) online, [Discussion Sections](../elements/discussion-sections.md) and [Peer Discussion](../elements/peer-discussion.md) in person

#### Constraints
- Poorly integrated blends add coordination overhead without learning benefit; students report frustration when online and in-person components duplicate or diverge [~M]
- Self-paced online components depend on learner self-regulation; low self-regulation predicts disengagement and attrition in the online strand [~S]
- Requires infrastructure and instructor time; resource-constrained settings often produce "blended" courses that are effectively online-only with token contact hours [-W]
- Adding online materials on top of an unchanged lecture load can [overload rather than help](../claims/cognitive-overload-degrades-learning.md) [-M]

#### Implementation Variability
- **Flipped models**: content delivery fully online before class; class time for problem-solving ([Flipped Classroom](../patterns/flipped-classroom.md))
- **Rotation models**: learners rotate on a fixed schedule between online and in-person stations (common in K–12, e.g., station rotation)
- **Enriched/blended campus model**: traditional course with supplementary online resources, quizzes, and discussion forums
- **Flex models**: online delivery is primary; in-person time is on-demand coaching and support

### Target Learners
- Adult and higher-education learners with the self-regulation to manage self-paced components [Self-regulated learning strategies predict academic achievement.](../claims/self-regulated-learning-predicts-achievement.md) [+M]
- Working professionals who need schedule flexibility but benefit from periodic live interaction and accountability
- Less suited, without added scaffolding, to novice learners or those with weak study skills, who may neglect the online strand [-M]

### Target Learning Goals
- Knowledge acquisition and procedural fluency via self-paced online [Practice](../elements/practice.md) with immediate feedback
- Application, discussion, and collaborative skill via in-person sessions
- Documentation and reporting of training effectiveness through LMS analytics

### Affordances
- [Cognitive Load Management](../principles/cognitive-load-management.md) — self-paced online materials let learners pause, replay, and segment content, controlling the pace of information intake in ways live lectures cannot
- [Community of Inquiry](../principles/community-of-inquiry.md) — blending supports the three presences: social and teaching presence in live sessions, cognitive presence sustained through asynchronous discussion
- [Assessment for Learning](../principles/assessment-for-learning.md) — LMS quizzes and analytics make the online strand continuously formatively assessed rather than only summatively examined
- [Mastery Learning](../principles/mastery-learning.md) — self-paced online modules can gate progression on demonstrated mastery rather than calendar time

### Personalization
- Customize online resources and adaptive pathways to individual learner needs ([Adaptive Learning](../principles/adaptive-learning.md))
- Use LMS data to target in-person time: spend scarce face-to-face minutes on the concepts the cohort's quiz data shows are weakest
- Provide personalized feedback through the LMS [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]

### Instructions
1. **Map outcomes to modes.** Assign each learning objective to the mode that serves it: content exposure online, application and discussion in person.
2. **Build the online strand.** Publish segmented content, worked examples, and low-stakes quizzes in the LMS; require completion before class ([Assess Performance](../elements/assess-performance.md)).
3. **Redesign in-person time.** Replace re-delivered content with [Practice](../elements/practice.md), [Peer Discussion](../elements/peer-discussion.md), and [Provide Guidance](../elements/provide-guidance.md) during live sessions.
4. **Close the loop.** Use pre-class quiz data to focus the live session; use live-session observations to adjust the next online module ([Supportive Information](../elements/supportive-information.md)).
5. **Assess and report.** Track participation and performance across both strands; gather learner feedback each cycle.

## Related Strategies
- [Flipped Classroom](../patterns/flipped-classroom.md) — the most researched blended variant; inverts the content/practice split
- [Case-Based Learning](../patterns/case-based-learning.md) — a common use of freed-up in-person time in professional education
- [Competency-Based Learning](../patterns/competency-based-learning.md) — pairs naturally with self-paced online modules

## Related Elements
- [Lectures](../elements/lectures.md) — typically relocated to the online strand as recorded video
- [Discussion Sections](../elements/discussion-sections.md) — the in-person strand's core activity
- [Provide Feedback](../elements/provide-feedback.md) — automated online plus human in-person
- [Whole-Task Performance](../elements/whole-task-performance.md) — complex integrative tasks best reserved for live sessions with support

## Tools
- LMS platforms (Moodle, Canvas, Blackboard) for content delivery, quizzing, and analytics
- Video platforms with in-video questioning (e.g., Panopto, Edpuzzle) to keep online viewing active
- Audience-response tools (Poll Everywhere, Mentimeter) to connect pre-class data to live sessions

## Examples
- A university course with weekly in-person meetings plus online modules completed at the learner's own pace, with pre-class quizzes setting the live-session agenda.
- Corporate training: a live workshop, followed by resources and an assessment posted to the LMS, with completion and score reporting for compliance tracking.
- K–12 station rotation (e.g., Rocketship Public Schools' lab-rotation model): learners rotate between teacher-led instruction, collaborative work, and adaptive online practice.

## Key Sources
- Means, B., Toyama, Y., Murphy, R., & Baki, M. (2013). The effectiveness of online and blended learning: A meta-analysis of the empirical literature. *Teachers College Record, 115*(3), 1–47. [doi:10.1177/016146811311500307](https://doi.org/10.1177/016146811311500307)
- Garrison, D. R., & Kanuka, H. (2004). Blended learning: Uncovering its transformative potential in higher education. *The Internet and Higher Education, 7*(2), 95–105. [doi:10.1016/j.iheduc.2004.02.001](https://doi.org/10.1016/j.iheduc.2004.02.001)
- Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)