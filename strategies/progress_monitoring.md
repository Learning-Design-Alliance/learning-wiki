---
type: strategy
id: progress_monitoring
title: Progress Monitoring
description: Progress monitoring is the repeated, systematic measurement of learner performance on target skills over time, used to judge responsiveness to instruction and to adjust teaching accordingly.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Progress Monitoring

> **Strategy** · [All strategies](index.md)

## Description
Progress monitoring is the repeated, systematic measurement of learner performance on target skills across time, used to judge whether instruction is working and to adjust teaching when it is not. Unlike a one-off test, it uses brief, frequent, parallel measures (e.g., weekly or biweekly probes) plotted against an expected trajectory, so that both instructor and learner can see growth — or its absence — early enough to act on it. The practice originated in curriculum-based measurement (CBM) in special education [Deno's CBM framework.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S] and now underpins tiered intervention systems and adaptive learning platforms.

## Design Implications

Progress monitoring operationalizes [Assessment for Learning](../principles/assessment-for-learning.md): the data exist to change instruction, not to certify attainment. Meta-analytic evidence shows that systematic formative evaluation produces meaningful achievement gains, with the largest effects when teachers use the data to make instructional decisions rather than merely recording it [Formative evaluation benefits require instructional adjustment.](../claims/feedback-most-effective-at-task-and-process-levels.md) [+S]. Giving learners access to their own progress graphs also builds self-regulatory skill, because visible trajectories prompt strategy evaluation and goal adjustment — a core move in [Self-Regulated Learning](../theories/self-regulated-learning.md) [+M].

### Context
#### Requirements
- Brief, reliable, repeatable measures of the target skill (curriculum-based measurement probes, mastery quizzes)
- An explicit performance criterion or expected growth rate to compare against
- A decision rule: what data pattern triggers an instructional change ([Fading](../elements/fading.md) of support, regrouping, reteaching)
- Time for administration, plotting, and analysis — protected in the instructional routine

#### Constraints
- Gains depend on teachers actually modifying instruction in response to data; monitoring without decision rules yields little benefit [Formative evaluation benefits require instructional adjustment.](../claims/feedback-most-effective-at-task-and-process-levels.md) [-S]
- Frequent testing on narrow skills can narrow the taught curriculum to what is measured, crowding out unmeasured goals [~M]
- Poorly calibrated measures (too hard, too easy, or unreliable) produce noisy graphs that mislead instructional decisions [-M]
- Overhead is real: without efficient tools, monitoring frequency degrades and the time series loses diagnostic value

#### Implementation Variability
- **Teacher-administered** (classic CBM in special education): instructor probes weekly and graphs results
- **Self-administered**: learners track their own mastery, e.g., [Mastery Learning](../patterns/mastery-learning.md) dashboards, which shifts monitoring toward metacognitive training [+M]
- **System-administered**: adaptive platforms ([Adaptive Difficulty](../elements/adaptive-difficulty.md)) infer mastery continuously from item responses, trading transparency for low overhead
- **Tiered intensity**: weekly probes in general education; daily or twice-weekly probes for learners in intensive intervention

### Target Learners
- Struggling learners and learners with disabilities, for whom early detection of non-response prevents accumulating deficits [+S]
- All K–12 learners in foundational skill areas (reading, mathematics), where skill hierarchies make early gaps costly
- Adult and self-directed learners, where visible progress data support persistence and self-efficacy [+M]
- Less valuable for advanced learners working on ill-structured goals, where single-skill probes poorly represent performance [~W]

### Target Learning Goals
- Procedural and foundational skill fluency (decoding, math facts, computation)
- Mastery decisions: determining when a skill is ready for the next unit ([Competency-Based Learning](../patterns/competency-based-learning.md))
- Self-regulated learning: learners learn to read their own data and set goals [+M]

### Instructions
1. Define the target skill and the criterion for mastery or expected growth rate.
2. Select or build a brief, parallel probe of that skill; keep it under ~10 minutes ([Assess Performance](../elements/assess-performance.md)).
3. Administer on a fixed schedule (weekly is typical) and plot scores against the aim line ([Assessment](../elements/assessment.md)).
4. Share the graph with learners and have them interpret it — where am I relative to my goal? ([Check-ins](../principles/check-ins.md))
5. Apply a decision rule: e.g., 4 consecutive points below aim line triggers an instructional change, not more of the same ([Coaching](../elements/coaching.md), [Adaptive Difficulty](../elements/adaptive-difficulty.md)).
6. After the change, continue monitoring to verify the intervention worked; fade probe frequency as growth stabilizes ([Fading](../elements/fading.md)) [Fading support promotes transfer of responsibility.](../claims/fading-support-promotes-transfer-of-responsibility.md) [+M].

## Related Strategies
- [Formative Assessment](../patterns/formative-assessment.md) — the broader practice of eliciting and using evidence; progress monitoring is its longitudinal, quantified form
- [Mastery Learning](../patterns/mastery-learning.md) — uses progress data as the gate for advancing to new material
- [Competency-Based Learning](../patterns/competency-based-learning.md) — progress monitoring supplies the evidence base for competency decisions

## Related Elements
- [Assess Performance](../elements/assess-performance.md) — the measurement act itself
- [Assessment](../elements/assessment.md) — the general element; progress monitoring is assessment iterated over time
- [Coaching](../elements/coaching.md) — what the instructor does with the data between probes
- [Adaptive Difficulty](../elements/adaptive-difficulty.md) — automated progress monitoring driving task selection
- [Fading](../elements/fading.md) — monitoring determines when support can be withdrawn

## Examples
- **DIBELS / Acadience Reading probes** (https://acadiencelearning.org) — brief oral-reading-fluency measures administered weekly; teachers graph scores and flag non-responders for intensified intervention.
- **AIMSweb (Pearson)** — a commercial CBM system for reading, math, and behavior with built-in aim lines and decision rules.
- **Khan Academy mastery dashboard** (https://www.khanacademy.org) — learners see per-skill mastery levels update as they practice; the dashboard is a self-facing progress monitor.
- **Response-to-Intervention (RTI/MTSS)** — tiered systems in which progress-monitoring graphs are the formal evidence for moving students between intervention tiers.

## Key Sources
- Fuchs, L. S., & Fuchs, D. (1986). Effects of systematic formative evaluation: A meta-analysis. *Exceptional Children, 53*(3), 199–208. [doi:10.1177/001440298605300301](https://doi.org/10.1177/001440298605300301)
- Stecker, P. M., Fuchs, L. S., & Fuchs, D. (2005). Using curriculum-based measurement to improve student achievement: Review of research. *Psychology in the Schools, 42*(8), 795-819. [doi:10.1002/pits.20113](https://doi.org/10.1002/pits.20113)
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74. [doi:10.1080/0969595980050102](https://doi.org/10.1080/0969595980050102)
- Deno, S. L. (1985). Curriculum-based measurement: The emerging alternative. *Exceptional Children, 52*(3), 219–232. [doi:10.1177/001440298505200303](https://doi.org/10.1177/001440298505200303)
- Zimmerman, B. J. (2002). Becoming a self-regulated learner: An overview. *Theory Into Practice, 41*(2), 64–70. [doi:10.1207/s15430421tip4102_2](https://doi.org/10.1207/s15430421tip4102_2)
