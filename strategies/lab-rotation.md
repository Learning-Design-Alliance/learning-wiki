---
type: strategy
title: Lab Rotation
description: Students rotate on a fixed schedule between a computer lab for online learning and a classroom for teacher-led instruction.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-30
---

# Lab Rotation

> **Strategy** · [All strategies](index.md)

## Description
Lab Rotation is a blended-learning model in which students move on a fixed schedule between a computer laboratory — where they work through online or adaptive courseware — and a traditional classroom with a teacher. The online segment typically delivers content, practice, or [assessment](../elements/assessment.md), while the face-to-face segment is reserved for discussion, remediation, enrichment, or hands-on work that technology handles poorly. It is one of the original rotation models described in the Christensen Institute taxonomy of blended learning, distinguished from [Station Rotation](station-rotation.md) by rotation between whole rooms (including the lab) rather than within one classroom.

## Design Implications

Lab Rotation concentrates the scalable, self-paced parts of instruction (content delivery, drill, adaptive practice) in the lab and reserves scarce teacher time for high-value interaction. Its effectiveness depends on the online segment being genuinely instructional rather than digitized worksheets, and on the classroom segment doing something the software cannot [Active learning outperforms lecture alone.](../claims/active-learning-improves-exam-performance.md) [+S]. Because lab time is often supervised by a paraprofessional or monitor, the model shifts design burden upstream: the courseware must carry the instructional load, including feedback and [practice](../elements/practice.md) sequencing.

### Context
#### Requirements
- Sufficient devices and bandwidth for a whole class or cohort in a dedicated lab
- Online content that is adaptive or at minimum self-paced, with built-in feedback [Adaptive learning improves outcomes relative to static materials.](../claims/adaptive-learning-improves-outcomes.md) [+M]
- A data pathway: lab performance data must reach the classroom teacher in time to inform the face-to-face session
- A fixed, predictable rotation schedule students can follow without re-explanation

#### Constraints
- If the lab segment is passive content consumption, the model reduces to supervised screen time with no learning advantage [Active learning outperforms lecture alone.](../claims/active-learning-improves-exam-performance.md) [-S]
- Rotation schedules fixed by logistics rather than mastery force students to move on before they are ready or wait after they are done [~M]
- Lab sessions supervised by non-teachers lose the in-the-moment diagnosis and [check-in](../elements/check-in.md) that make practice productive [-M]
- Whole-class rotation can add transition overhead and fragment attention, increasing extraneous load at session boundaries [Cognitive overload degrades learning.](../claims/cognitive-overload-degrades-learning.md) [~W]

#### Implementation Variability
- **Flipped-lab variant:** online work happens at home; the "lab" period is used for supported practice — closer to a flipped classroom
- **Individual-rotation variant:** only students who need a given module rotate to the lab, enabling remediation without holding back the cohort
- **Lab-plus-project variant:** lab time covers skill practice; classroom time runs [case studies](../elements/case-studies.md) or collaborative work the software cannot host
- **Courseware-only vs. teacher-authored:** schools may adopt a commercial platform (e.g., IXL, DreamBox, ALEKS) or build rotations around teacher-curated online modules

### Target Learners
- K–12 students in schools with shared device resources, where whole-class lab scheduling is the practical way to guarantee screen time
- Students who benefit from self-paced practice with immediate feedback, particularly in procedural domains like mathematics [Adaptive learning improves outcomes relative to static materials.](../claims/adaptive-learning-improves-outcomes.md) [+M]
- Less suitable for learners who need sustained adult scaffolding during online work, since lab supervision is typically thin [-M]

### Target Learning Goals
- Procedural fluency and skill practice with immediate feedback
- Content coverage that frees classroom time for higher-order work [Active learning outperforms lecture alone.](../claims/active-learning-improves-exam-performance.md) [+S]
- Early development of independent work habits and self-management of pace

### Instructions
1. **Map the split.** Identify which objectives the courseware can teach and assess, and reserve discussion-, collaboration-, or equipment-dependent objectives for the classroom.
2. **Select and configure courseware.** Choose adaptive or mastery-based software; align its scope-and-sequence with the classroom curriculum so the two segments reinforce each other.
3. **Build the rotation schedule.** Fix a predictable cadence (e.g., daily 45-minute lab block alternating with classroom instruction) and communicate it visually.
4. **Close the data loop.** Before each classroom session, review lab dashboards and use the data to target [direct instruction](../patterns/direct-instruction.md), regroup students, or plan a [check-in](../elements/check-in.md) with strugglers.
5. **Protect the classroom segment.** Use face-to-face time for [active learning](../principles/active-learning.md) — discussion, [practice](../elements/practice.md) with feedback, application — not for re-delivering what the software already covered [Active learning outperforms lecture alone.](../claims/active-learning-improves-exam-performance.md) [+S].
6. **Review and adjust.** Periodically audit whether lab time is producing mastery data that changes instruction; if not, the rotation is decorative.

## Related Strategies
- [Station Rotation](station-rotation.md) — the within-classroom counterpart; useful when a dedicated lab is unavailable
- [Flipped Classroom](flipped-classroom.md) — inverts the same split by moving content delivery outside class time
- [Individual Rotation](individual-rotation.md) — replaces the fixed schedule with per-student pathways

## Examples
- **Rocketship Public Schools (San Jose, CA)** — early and prominent lab-rotation charter network; students rotate between a Learning Lab for adaptive software and classroom instruction, a model that drew both replication and critique about lab staffing.
- **KIPP Empower Academy (Los Angeles)** — blends rotational online learning with small-group teacher instruction in early grades.
- **ALEKS-based math labs** — many secondary schools run lab rotations on [ALEKS](https://www.aleks.com), using its adaptive assessment to drive the classroom teacher's reteaching groups.

## Key Sources
- Staker, H., & Horn, M. B. (2012). *Classifying K–12 blended learning*. Christensen Institute (formerly Innosight Institute). [https://www.christenseninstitute.org/publications/classifying-k-12-blended-learning/](https://www.christenseninstitute.org/publications/classifying-k-12-blended-learning/)
- Means, B., Toyama, Y., Murphy, R., & Baki, M. (2013). The effectiveness of online and blended learning: A meta-analysis of the empirical literature. *Teachers College Record, 115*(3), 1–47. [doi:10.1177/016146811311500307](https://doi.org/10.1177/016146811311500307)
- Freeman, S., Eddy, S. L., McDonough, M., Smith, M. K., Okoroafor, N., Jordt, H., & Wenderoth, M. P. (2014). Active learning increases student performance in science, engineering, and mathematics. *PNAS, 111*(23), 8410–8415. [doi:10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111)
- Pane, J. F., Steiner, E. D., Baird, M. D., Hamilton, L. S., & Pane, J. D. (2017). Informing progress: Insights on personalized learning implementation and effects. *RAND Corporation*. [https://doi.org/10.7249/RR2042](https://doi.org/10.7249/RR2042)