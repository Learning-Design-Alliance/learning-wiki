---
type: design
id: task-trees-knowledge-representation
title: "Task Trees: hierarchical knowledge representation for task recognition and event selection"
description: Task Trees are the knowledge structure used by both the Task Model Reasoner and the Narrative Manager in the Bio-safety Lab.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-27
sources:
  - id: alvarez-2014
    resource: "https://doi.org/10.1007/s40593-014-0022-z"
    title: "Alvarez, N., Sanchez-Ruiz, A., Cavazza, M., Shigematsu, M., & Prendinger, H. (2014). Narrative Balance Management in an Intelligent Biosafety Training Application for Improving User Performance. Int J Artif Intell Educ 25, 35–59. https://doi.org/10.1007/s40593-014-0022-z"
    author: "Alvarez, N., Sanchez-Ruiz, A., Cavazza, M., Shigematsu, M., & Prendinger, H"
---

# Task Trees: hierarchical knowledge representation for task recognition and event selection

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Task Trees are the knowledge structure used by both the Task Model Reasoner and the Narrative Manager in the Bio-safety Lab. A tree's root represents the whole task, intermediate nodes are subtasks, and leaves are Task-Level Events; sibling nodes relate through AND, OR and SEQ conditions, and leaf nodes marked as errors let the system recognize plausible but incorrect actions. The article states "A Task Tree is a hierarchical model which has a root node representing the whole task to perform on the top of the tree and child nodes being the subtasks in which it can be divided". Narrative Manager trees additionally mark system nodes with Balance, Impact and Closure parameters.

## Design Implications

### Context
#### Requirements
- The spill-clearing task tree contains more than 250 nodes, so building one requires detailed protocol knowledge and expert annotation of error nodes
#### Constraints
- The article contrasts this with Death Kitchen's Danger Matrix, which allowed only one constraint (partial order) for event selection

### Target Learners
- Bio-safety laboratory workers in training
- Medical students

### Learning Goals
- Recognition and correction of user errors during protocol execution
- Real-time monitoring of multi-step laboratory procedures

### Claims
- 

## Related Designs

- [Argument visualization: tree diagrams exposing the logical structure of argumentative texts](argument-visualization-tree-diagrams.md)

## Examples
-

## Key Sources
- Alvarez, N., Sanchez-Ruiz, A., Cavazza, M., Shigematsu, M., & Prendinger, H. (2014). Narrative Balance Management in an Intelligent Biosafety Training Application for Improving User Performance. Int J Artif Intell Educ 25, 35–59. https://doi.org/10.1007/s40593-014-0022-z
