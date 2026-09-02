---
type: strategy
id: data-driven-instruction
title: Data Driven Instruction
description: Using ongoing evidence of student learning to select, adjust, and differentiate instruction rather than relying on pacing guides or intuition.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Data Driven Instruction

> **Strategy** · [All strategies](index.md)

## Description
Data driven instruction (DDI) is the systematic collection and analysis of student learning evidence — formative assessments, exit tickets, curriculum-based measures, work samples — and the use of that evidence to decide what to reteach, regroup, or accelerate. It replaces assumptions about what students know with direct measurement, typically on short cycles (weekly to unit-length) rather than end-of-year summative tests.

## Design Implications

DDI operationalizes [Assessment for Learning](../principles/assessment-for-learning.md): assessment information changes subsequent teaching rather than merely certifying it [Formative assessment practices improve achievement when they feed forward into instruction.](../claims/assessment-for-learning-improves-achievement.md) [+S]. The mechanism is not the data itself but the instructional decision it triggers — data reviewed without a concrete reteaching plan produces little gain. Feedback and reteaching are most effective when they target the task and process level rather than the learner globally [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S].

### Context
#### Requirements
- Brief, frequent, aligned measures that actually discriminate between mastery and non-mastery (item quality matters more than quantity)
- Protected time and a protocol for analyzing results and planning responses (e.g., data team meetings with a fixed agenda)
- A repertoire of instructional responses — reteaching, regrouping, tiered tasks — so identified gaps can actually be acted on
- Item-level analysis, not just aggregate scores; a class average of 70% hides which students missed which skills

#### Constraints
- Over-reliance on easily automated measures (multiple-choice, low-complexity items) narrows instruction toward what those items can detect [-M]
- Frequent low-stakes testing without instructional response consumes time and can raise anxiety with no learning benefit [~M]
- Data dashboards that display scores without diagnostic interpretation shift teacher attention to rankings rather than causes [-W]
- For advanced learners, data-driven reteaching of already-mastered content wastes time; the expertise-reversal pattern applies to grouping decisions too [~M]

#### Implementation Variability
- **Teacher-level cycles**: exit tickets analyzed nightly, next-day reteach groups
- **Team-level cycles**: grade-level or department data meetings on a fixed cadence (e.g., every 6 weeks)
- **System-level**: adaptive platforms ([Adaptive Learning](../patterns/adaptive-learning.md)) automate the measure-and-adjust loop, though algorithmic grouping still needs teacher oversight
- **Standards-based grading variants**: tracking mastery per skill rather than averaged points

### Target Learners
- Struggling learners, who benefit most when gaps are caught early and addressed with targeted reteaching [Formative assessment practices improve achievement when they feed forward into instruction.](../claims/assessment-for-learning-improves-achievement.md) [+S]
- Whole classes in skill-hierarchical domains (early literacy, mathematics) where unaddressed gaps compound
- Less useful for advanced learners already above the measured ceiling, or in open-ended domains where mastery is not decomposable into discrete items

### Target Learning Goals
- Procedural and foundational skill mastery in hierarchical domains
- Closing prerequisite gaps before new instruction builds on them
- Monitoring progress toward competency-based outcomes ([Competency-Based Learning](../patterns/competency-based-learning.md))

### Instructions
1. **Define the mastery criteria** for the upcoming unit — which skills, at what item difficulty, with what evidence ([Assessment](../elements/assessment.md))
2. **Administer a brief aligned check** before and during instruction — pre-assessment, exit tickets, or curriculum-based measures ([Check-In](../elements/check-in.md))
3. **Analyze at the item level**: sort students by specific skill gaps, not total score
4. **Plan a concrete response**: reteach to a small group, adjust whole-class pacing, or assign targeted practice ([Coaching](../elements/coaching.md))
5. **Re-assess after the response** to verify the gap closed; if not, change the approach rather than repeating it
6. **Feed results forward** into feedback that names the process or strategy to change [Feedback is most effective at task and process levels.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]

## Related Strategies
- [Formative Assessment](../patterns/formative-assessment.md) — the assessment layer DDI depends on; DDI adds the decision protocol
- [Direct Instruction](../patterns/direct-instruction.md) — a common reteaching response when data reveals whole-group gaps
- [Adaptive Learning](../patterns/adaptive-learning.md) — automates the measure-adjust cycle at scale

## Examples
- **Uncommon Schools / Relay GSE DDI model** — weekly interim assessments, item-level analysis in teacher meetings, and scripted reteach plans; widely replicated in charter networks
- **[MAP Growth (NWEA)](https://www.nwea.org/map-growth/)** — adaptive interim assessment with class-level reports teachers use to form flexible groups
- **[Zearn](https://www.zearn.org)** — digital math lessons that report per-standard mastery to teachers, who use the data to plan small-group instruction alongside the Eureka Math curriculum

## Key Sources
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. [doi:10.1080/0969595980050102](https://doi.org/10.1080/0969595980050102)
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112. [doi:10.3102/003465430298487](https://doi.org/10.3102/003465430298487)
- Wiliam, D. (2011). *Embedded formative assessment*. Solution Tree Press.
- Hamilton, L., Halverson, R., Jackson, S., Mandinach, E., Supovitz, J., & Wayman, J. (2009). *Using student achievement data to support instructional decision making* (NCEE 2009-4067). National Center for Education Evaluation and Regional Assistance, IES. [doi:10.1037/e533772010-001](https://doi.org/10.1037/e533772010-001)