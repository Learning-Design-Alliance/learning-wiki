---
type: strategy
title: Task Analysis
description: A systematic method for breaking down a complex skill or task into its component knowledge, skills, and decision points so instruction can be designed around what learners actually need to master.
status: review
generated:
  by: "claude/unspecified"
  at: 2026-08-29
---

# Task Analysis

> **Strategy** · [All strategies](index.md)

## Description
Task analysis is the systematic decomposition of a target task into its constituent steps, subtasks, prerequisite knowledge, and — in its cognitive form — the invisible decisions and strategies experts use. It is carried out before instruction is designed, typically through expert interviews, observation, think-aloud protocols, or document analysis, and produces a structured map of what must be taught, sequenced, and practiced.

## Design Implications

Task analysis is the diagnostic foundation of instructional design: without an accurate model of the task, sequencing, practice, and support are aimed at the wrong targets. Cognitive task analysis (CTA) is especially valuable because much expert knowledge is tacit — experts routinely omit steps and decisions they execute automatically, and instruction built on their unaided self-reports misses critical content [~M]. Decomposing tasks also allows designers to manage intrinsic load by sequencing simple-to-complex whole tasks or isolating part tasks for novices [Part-task practice reduces cognitive load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [+M] and by grouping constituent skills into learnable chunks [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S].

### Context
#### Requirements
- Access to one or more genuine experts (or expert performance records) for interviews and observation
- A structured elicitation method — [Think-Aloud](../elements/think-aloud.md) protocols, critical decision probes, or structured interviews — rather than a single open-ended "walk me through it" request
- A representation format suited to the task type: hierarchical (goal–subtask) for procedural tasks, information-processing or GOMS-style for cognitive tasks, prerequisite matrices for knowledge-heavy domains
- Iteration: first-pass analyses almost always omit automatic expert steps and must be validated against actual performance data

#### Constraints
- Experts systematically omit automatic steps when self-reporting; unvalidated analyses produce incomplete instruction [-M]
- Over-decomposition fragments integrated skills: teaching isolated subtasks without whole-task context can produce knowledge that learners cannot reassemble in performance [~M] — whole-task sequencing is generally preferable for complex learning
- Analysis is expensive; for rapidly changing tasks the analysis can be obsolete before the instruction ships [-W]
- Highly automatic expert performance is hard to verbalize even with probes; CTA captures more but still not all expert knowledge [-W]

#### Implementation Variability
- **Hierarchical task analysis** — decompose goals into subtasks and operations; best for observable procedural skills
- **Cognitive task analysis** — elicit cues, judgments, and strategies via structured interviews and think-alouds; best for decision-rich tasks (diagnosis, troubleshooting, triage)
- **Prerequisite analysis** — map knowledge/skill dependencies to build a learning hierarchy for sequencing
- **Whole-task design** — instead of isolating parts, sequence progressively more complex whole-task classes (as in [Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md))

### Target Learners
- Designers serving novices benefit most: analysis reveals which constituent skills need isolated support and which load points require scaffolding [Part-task practice reduces cognitive load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [+M]
- As expertise grows, the fine-grained decomposition becomes counterproductive; instruction should shift to whole tasks and reduced guidance [Guidance effectiveness reverses with learner expertise.](../claims/expertise-reversal-effect.md) [~M]

### Target Learning Goals
- Procedural skill acquisition: identifying the exact steps and their order
- Complex cognitive skills: surfacing expert decision rules, heuristics, and cue recognition
- Curriculum sequencing: determining prerequisites and a simple-to-complex task progression

### Instructions
1. Define the terminal objective and performance conditions precisely, including the standard of acceptable performance.
2. Select an analysis method matched to the task type (hierarchical for procedures, cognitive for decision-rich work).
3. Elicit expert performance using [Think-Aloud](../elements/think-aloud.md) protocols and structured probes ("What were you noticing at that point?"), and observe real performance where possible.
4. Decompose the task into steps, decisions, and prerequisite knowledge; chunk constituent skills into learnable units [Chunking reduces working memory load.](../claims/chunking-reduces-working-memory-load.md) [+S].
5. Validate the analysis with a second expert and against actual performance data, specifically hunting for omitted automatic steps.
6. Use the analysis to sequence instruction — simple-to-complex whole tasks or part-task practice for high-load components [Part-task practice reduces load for novices.](../claims/part-task-practice-reduces-load-for-novices.md) [+M] — and to plan [Scaffolding](scaffolding.md) and fading.

## Related Strategies
- [Learner Analysis](learner-analysis.md) — task analysis identifies what must be taught; learner analysis identifies who is being taught and what they already bring
- [Sequencing](../principles/sequencing.md) — the analysis output is the primary input for ordering instruction
- [Worked Examples](worked-examples.md) — the steps surfaced by task analysis become the content of worked demonstrations

## Examples
- **[Four-Component Instructional Design](../patterns/4cid-four-component-instructional-design.md)** — the Ten Steps method operationalizes task analysis as its first phase: analyzing constituent skills and cognitive strategies to design whole-task learning tasks.
- **Aviation and medical training** — cognitive task analysis of expert anesthesiologists' crisis decision-making has been used to build simulation scenarios and checklists that teach the cues and decision rules experts otherwise leave tacit.
- **GOMS analysis in interface design** — Card, Moran, and Newell's Goals–Operators–Methods–Selection rules decompose user tasks at the second-by-second level to predict performance and guide training.

## Key Sources
- Jonassen, D. H., Tessmer, M., & Hannum, W. H. (1999). *Task analysis methods for instructional design*. Lawrence Erlbaum Associates.
- Clark, R. E., Feldon, D. F., van Merriënboer, J. J. G., Yates, K., & Early, S. (2008). Cognitive task analysis. In J. M. Spector et al. (Eds.), *Handbook of research on educational communications and technology* (3rd ed., pp. 577–593). Lawrence Erlbaum Associates.
- van Merriënboer, J. J. G., Kirschner, P. A., & Kester, L. (2003). Taking the load off a learner's mind: Instructional design for complex learning. *Educational Technology Research and Development, 51*(3), 5–13. [doi:10.1007/BF02505062](https://doi.org/10.1007/BF02505062)
- Schraagen, J. M., Chipman, S. F., & Shalin, V. L. (Eds.). (2000). *Cognitive task analysis*. Lawrence Erlbaum Associates.
- van Merriënboer, J. J. G., & Kirschner, P. A. (2007). *Ten steps to complex learning: A systematic approach to four-component instructional design*. Lawrence Erlbaum Associates.