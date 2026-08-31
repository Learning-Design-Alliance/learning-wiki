---
type: strategy
title: Self Monitoring
description: Learners deliberately track their own comprehension, performance, and progress against criteria during learning, feeding those judgments into adjustments of strategy and effort.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Self Monitoring

## Description
Self monitoring is the ongoing process by which learners observe and judge their own understanding, performance, or progress — asking "Do I actually get this?" or "How did I do against the criteria?" — and use those judgments to regulate further study. It is the monitoring phase of [Self-Regulated Learning](../theories/self-regulated-learning.md), sitting between forethought (planning) and reflection (evaluation). In practice it is carried out through self-questioning, self-testing, checklists, progress tracking, and comparing one's work against models or rubrics.

## Design Implications

Self monitoring only improves learning when the monitoring is *accurate* and when it triggers *adjustment*: learners frequently judge their comprehension as better than it is, especially after rereading or fluent lectures [~M]. Designers should therefore build in external checks — retrieval practice, criterion-referenced rubrics, worked models — that calibrate learners' judgments against actual performance rather than relying on feelings of fluency [Self-assessment improves achievement when learners compare work against explicit criteria.](../claims/assessment-for-learning-improves-achievement.md) [+S].

### Context
#### Requirements
- Explicit criteria, rubrics, or expert models against which learners can compare their own work
- Low-stakes opportunities to test understanding ([Practice](../elements/practice.md), self-quizzing) so judgments are based on retrieval, not recognition
- Time and prompts built into the learning sequence for monitoring to occur ([Check-In](../elements/check-in.md), learning logs)
- A follow-on action: monitoring without a mechanism to revise strategy or restudy produces no benefit

#### Constraints
- Judgments made from fluency cues (ease of rereading, familiarity) are systematically miscalibrated and can *reduce* effective study allocation [-M] — learners restudy what already feels easy and skip what needs work
- Younger learners and novices monitor poorly without external scaffolds; unguided "monitor yourself" prompts often produce no measurable gain [~M]
- Excessive self-tracking overhead can consume working memory needed for the task itself, particularly for complex material [~W]

#### Implementation Variability
- **Judgment-of-learning prompts**: after studying, learners rate confidence per item, then restudy low-confidence items
- **Self-testing**: learners generate answers before checking, converting monitoring into retrieval practice
- **Criterion comparison**: learners score their own draft against a rubric or expert model before submission
- **Progress dashboards**: systems surface performance data (e.g., mastery bars, error patterns) for learners to interpret

### Target Learners
- Adolescents and adults; monitoring accuracy develops slowly and requires heavy scaffolding in younger children [~M]
- Learners preparing for independent study or assessment, where study-allocation decisions matter
- Struggling learners benefit most when monitoring is paired with explicit criteria — without them, they tend to overestimate mastery [-M]

### Target Learning Goals
- Metacognitive skill: accurate self-assessment and study regulation as a transferable capability
- Retention and exam performance, via better allocation of restudy effort [Practice testing strengthens retention more than rereading.](../claims/distributed-practice-improves-retention.md) [+S]
- Self-regulated learning dispositions: independence, persistence, ownership of progress

### Instructions
1. Establish criteria: give learners a rubric, expert model, or answer key they can access independently ([Advance Organizers](../elements/advance-organizers.md) can frame what "understanding" looks like).
2. Prompt a monitoring event: after a study segment, have learners predict or rate their understanding *before* checking ([Check-In](../elements/check-in.md)).
3. Test the judgment: require retrieval or application ([Practice](../elements/practice.md)) rather than recognition, so judgments rest on evidence.
4. Compare and calibrate: learners contrast their prediction with actual performance and note the gap ([Annotating](../principles/annotating.md) a monitoring log makes gaps visible over time).
5. Act on the gap: direct learners to restudy, change strategy, or seek help — monitoring must connect to a decision ([Assessment](../elements/assessment.md) results feed the next cycle).

## Related Strategies
- [Self-Evaluation](self-evaluation.md) — the terminal reflection that closes the monitoring loop at the end of a task
- [Goal Setting](../elements/goal-setting.md) — supplies the standard against which monitoring judgments are made
- [Spaced Practice](../principles/spaced-practice.md) — monitoring determines *what* to space; the two strategies compound

## Examples
- **Khan Academy mastery tracking** — learners see per-skill mastery bars and are prompted to continue or revisit skills, externalizing the monitoring judgment.
- **Exam wrappers** — post-exam reflection forms (used widely in undergraduate STEM courses) ask students to compare predicted with actual scores and plan study changes for the next exam.
- **Reciprocal teaching** — students take turns leading comprehension-monitoring questions ("What was confusing?"), making monitoring a visible, practiced routine.

## Key Sources
- Zimmerman, B. J. (2002). Becoming a self-regulated learner: An overview. *Theory Into Practice, 41*(2), 64–70. [doi:10.1207/s15430421tip4102_2](https://doi.org/10.1207/s15430421tip4102_2)
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest, 14*(1), 4–58. [doi:10.1177/1529100612453266](https://doi.org/10.1177/1529100612453266)
- Sitzmann, T., & Ely, K. (2011). A meta-analysis of self-regulated learning in work-related training and educational attainment. *Personnel Psychology, 64*(2), 361–403. [doi:10.1037/a0022777](https://doi.org/10.1037/a0022777)
- Winne, P. H., & Hadwin, A. F. (1998). Studying as self-regulated engagement in learning. In D. J. Hacker, J. Dunlosky, & A. C. Graesser (Eds.), *Metacognition in educational theory and practice* (pp. 277–304). Erlbaum.