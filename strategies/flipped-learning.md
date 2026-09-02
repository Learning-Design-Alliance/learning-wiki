---
type: strategy
id: flipped-learning
title: Flipped Learning
description: A pedagogical model that moves first exposure to content outside class (typically via video) and reserves class time for active, instructor-guided application.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Flipped Learning

> **Strategy** · [All strategies](index.md)

## Description
Flipped learning reverses the traditional sequence: learners encounter new content individually before class — usually through short pre-recorded videos, readings, or podcasts — and class time is devoted to active learning such as problem-solving, discussion, case work, and group projects. The instructor shifts from content deliverer to facilitator, guiding learners as they apply, extend, and get feedback on what they studied. The model depends on both halves working: pre-class exposure *and* purposefully structured in-class application.

## Design Implications

Flipped learning works because it reallocates scarce, socially rich classroom time to the activities that benefit most from instructor presence and peer interaction, while letting learners control pacing of first exposure [Active learning improves exam performance relative to lecture.](../claims/active-learning-improves-exam-performance.md) [+S]. A meta-analysis of 317 studies (51,437 participants) found flipped classrooms improve academic performance, engagement, and metacognitive skills, with the largest gains in language, technology, and health-science courses [~M] — effects vary by discipline and implementation quality. The pre-class materials must be short, focused, and paired with accountability or formative checks, or the in-class activities collapse.

### Context
#### Requirements
- Curated or created pre-class materials: short videos (ideally under ~10 minutes each), readings, or audio, with [Chunking](../principles/chunking.md) applied to segment content
- A pre-class accountability mechanism — embedded questions or a brief quiz — so learners arrive prepared [Assessment for learning improves achievement.](../claims/assessment-for-learning-improves-achievement.md) [+M]
- Structured in-class time built around [Application](../elements/application.md), [Class Discussion](../elements/class-discussion.md), [Case Studies](../elements/case-studies.md), and [Peer Collaboration](../elements/peer-collaboration.md) rather than re-lecturing the video content
- Instructor readiness to facilitate and give individualized feedback rather than present

#### Constraints
- Effectiveness collapses when students skip the pre-class work; without accountability, in-class activities assume knowledge that isn't there [-M]
- High initial production cost for materials; instructors underestimate the time to create quality videos
- Weaker evidence in mathematics and engineering, where novices attempting problems before adequate instruction can flounder without careful scaffolding [~M]
- Pre-class quizzes can shift learner focus from understanding toward test performance, encouraging shallow viewing [-W]
- Re-lecturing the video content in class negates the model and signals that preparation is optional [-M]

#### Implementation Variability
- Full flip (all content online) vs. partial flip (some topics flipped, others taught conventionally)
- Pre-class materials vary: screencasts, curated external videos (e.g., Khan Academy), readings, podcasts — supporting different preferences and access needs
- In-class formats range from structured problem sets to peer instruction, [Case Studies](../elements/case-studies.md), or studio-style project work
- First-exposure accountability ranges from low-stakes quizzes to ticket-in reflections or peer teaching

### Target Learners
- Secondary and higher-education learners across disciplines; strongest evidence in language, technology, and health-science courses [~M]
- Learners who benefit from self-paced first exposure — the ability to pause, rewind, and revisit video supports learners with variable preparation or processing speed [+M]
- Less suitable without adaptation for novices in highly technical subjects (math, engineering) who need more guided first exposure, or for learners without reliable access to technology or study time outside class [-W]

### Target Learning Goals
- Foundational knowledge acquired before class, freeing class time for higher-order application and analysis
- Applied and procedural skills practiced with expert feedback available
- Metacognitive development: self-pacing, time management, and monitoring one's own preparation [+W]
- Collaboration and communication skills through in-class group work

### Instructions
1. Identify content suitable for first exposure and produce or curate short, focused pre-class materials ([Pre-Class Video/Lecture](../elements/pre-class-videolecture.md))
2. Add a low-stakes pre-class check — embedded questions or a brief quiz — to create accountability and surface misconceptions ([Formative Assessment](../elements/formative-assessment.md))
3. Design in-class activities that *apply* the pre-class content at a higher cognitive level: problem-solving, [Case Studies](../elements/case-studies.md), or structured [Class Discussion](../elements/class-discussion.md)
4. Build in [Peer Collaboration](../elements/peer-collaboration.md) so learners explain and critique each other's reasoning with the instructor circulating
5. Close with individual or group [Reflection](../elements/reflection.md) connecting the applied work back to the pre-class concepts

## Related Strategies
- [Blended Learning](../patterns/blended-learning.md) — flipped learning is a specific, time-swap form of blending online and face-to-face modes
- [Peer Instruction](peer-instruction.md) — a common in-class activity structure used inside flipped classrooms
- [Active Learning](../principles/active-learning.md) — the in-class half of the flip depends on these techniques to produce gains

## Examples
- **[Clintondale High School](https://flippedhighschool.com) (Michigan)** — flipped its entire curriculum school-wide; failure rates dropped substantially (reported ~33% in some subjects) in the first year.
- **[MEF University](https://www.mef.edu.tr) (Istanbul)** — the first university to adopt flipped learning institution-wide across all programs.
- **Robert Talbert's screencasts** — YouTube screencasts teaching mathematics concepts before class, with class time devoted to collaborative problem-solving; documented in Talbert (2017).
- **Health sciences simulation courses** — students watch procedure videos before class, then spend contact hours practicing on mannequins with instructor feedback.

## Key Sources
- Strelan, P., Osborn, A., & Palmer, E. (2020). The flipped classroom: A meta-analysis of effects on student performance across disciplines and education levels. *Assessment & Evaluation in Higher Education, 45*(6), 899–921. [doi:10.1016/j.edurev.2020.100314](https://doi.org/10.1016/j.edurev.2020.100314)
- Låg, T., & Sæle, R. G. (2019). Does the flipped classroom improve student learning and satisfaction? A systematic review and meta-analysis. *AERA Open, 5*(3). [doi:10.1177/2332858419870497](https://doi.org/10.1177/2332858419870497)
- Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)
- Bergmann, J., & Sams, A. (2012). *Flip your classroom: Reach every student in every class every day.* ISTE/ASCD.
- Talbert, R. (2017). *Flipped learning: A guide for higher education faculty.* Stylus Publishing.