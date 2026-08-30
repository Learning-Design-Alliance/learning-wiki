---
type: strategy
title: Learner Analysis
description: Systematically gathering information about learners' prior knowledge, skills, motivations, and constraints to inform instructional design decisions.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Learner Analysis

## Description
Learner analysis is the systematic collection and interpretation of information about the target audience before and during instruction: their prior knowledge, prerequisite skills, motivations, attitudes, language proficiency, and access constraints. It is carried out through pre-assessments, surveys, interviews, analysis of performance data, and observation, and its findings drive decisions about sequencing, scaffolding, pacing, and examples.

## Design Implications

Learner analysis operationalizes the core finding that learning is a function of the interaction between instruction and what the learner brings to it — the aptitude-treatment interaction tradition [~M]. Prior knowledge is the single most influential learner characteristic: it determines whether guidance helps or hinders, as predicted by the [Expertise Reversal Effect](../theories/expertise-reversal-effect.md) [~S]. Analysis findings should map directly onto design decisions — activating what learners already know ([Activation](../principles/activation.md)), calibrating load ([Cognitive Load Management](../principles/cognitive-load-management.md)), and selecting adaptive pathways ([Adaptive Learning](../principles/adaptive-learning.md)).

### Context
#### Requirements
- A pre-assessment or diagnostic that measures prerequisite knowledge, not just demographics
- A documented decision rule: each finding must change a specific design choice (examples, pacing, scaffolding, vocabulary level)
- Ongoing formative checks, since initial analysis is a snapshot that becomes stale as learning progresses

#### Constraints
- Static front-end analysis misleads when learner knowledge changes rapidly during instruction; without mid-course re-assessment, designs calibrated to novices continue over-supporting learners who have moved on [~S]
- Self-report surveys of confidence and preference correlate weakly with actual knowledge and can actively mislead design decisions [-M] — learners with low prior knowledge are poorest at judging their own competence
- Over-segmenting audiences by learning-style preferences has no empirical support and wastes design effort [X]
- Analysis without a mechanism to act on findings (e.g., branching, differentiated tasks) yields information but no instructional benefit

#### Implementation Variability
- **General audience analysis**: broad surveys and entry testing for large-enrollment or self-paced courses
- **Enhanced event analysis** (Dick & Carey): describes the specific skills and attitudes learners bring to one particular unit
- **Continuous diagnostic analysis**: embedded pre-tests and adaptive routing, as in mastery-based platforms
- **Motivational profiling**: Keller's ARCS audience analysis of attention, relevance, confidence, and satisfaction drivers

### Target Learners
- Heterogeneous groups with wide prior-knowledge variance, where a single fixed instructional path will misfit most learners [~S]
- Novices, who benefit most from the extra structure and prerequisite remediation that analysis reveals as necessary [Activation improves learning when it surfaces relevant prior knowledge.](../claims/activation-improves-learning.md) [+M]
- Advanced learners are poorly served by designs built from novice-calibrated analysis; guidance should be reduced as expertise grows [~S]

### Target Learning Goals
- Any goal where prerequisite knowledge determines success: procedural skills, conceptual understanding, problem solving
- Goals requiring differentiated pacing or pathways ([Adaptive Learning](../principles/adaptive-learning.md))
- Goals where motivation is a bottleneck — analysis identifies relevance gaps before content is finalized

### Instructions
1. Define the entry behaviors and prerequisites the instruction assumes; write them as observable skills.
2. Collect diagnostic data: short pre-tests of prerequisites, surveys of experience and motivation, and analysis of existing performance data.
3. Interpret findings against design levers — what will be reviewed, what will be assumed, what examples and vocabulary will be used ([Accessible Vocabulary & Syntax](../principles/accessible-vocabulary-syntax.md)).
4. Activate relevant prior knowledge at the start of instruction ([Advance Organizers](../elements/advance-organizers.md), [Activation](../principles/activation.md)).
5. Build in re-assessment checkpoints and adjust scaffolding as learner expertise grows, avoiding the expertise reversal trap.
6. Document the analysis and the design decisions it drove, so later revisions can test whether the assumptions held.

## Related Strategies
- [Learner and Context Analysis](../strategies/learner-and-context-analysis.md) — the broader Dick & Carey analysis that pairs audience data with environmental and task context
- [Diagnostic Pre-Assessment](../strategies/diagnostic-pre-assessment.md) — the primary data-collection instrument for learner analysis
- [Differentiated Instruction](../strategies/differentiated-instruction.md) — the instructional response when analysis reveals heterogeneous readiness

## Examples
- **Dick & Carey systems approach** — "learner and context analysis" is a required front-end step, producing entry-behavior descriptions that shape objectives and assessments.
- **Khan Academy** — placement diagnostics route learners to a starting level and mastery checks continuously re-run a lightweight learner analysis as they progress.
- **ARCS motivational design (Keller)** — audience analysis of motivational profiles precedes the design of attention and relevance tactics in course development projects.

## Key Sources
- Dick, W., Carey, L., & Carey, J. O. (2015). *The systematic design of instruction* (8th ed.). Pearson.
- Keller, J. M. (1987). Development and use of the ARCS model of instructional design. *Journal of Instructional Development, 10*(3), 2–10. [doi:10.1007/BF02905780](https://doi.org/10.1007/BF02905780)
- Tobias, S. (1994). Interest, prior knowledge, and learning. *Review of Educational Research, 64*(1), 63–93. [doi:10.3102/00346543064001063](https://doi.org/10.3102/00346543064001063)
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31. [doi:10.1207/S15326985EP3801_4](https://doi.org/10.1207/S15326985EP3801_4)
- Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. *Psychological Science in the Public Interest, 9*(3), 105–119. [doi:10.1111/j.1539-6053.2009.01038.x](https://doi.org/10.1111/j.1539-6053.2009.01038.x)