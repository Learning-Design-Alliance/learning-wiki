---
type: design
id: bella-student-model-150-tuples
title: "BELLA student model: about 150 tuples covering Common Core concepts, skills, bugs and missing heuristics, each scored 0–100 with full change history"
description: "BELLA models each student's domain knowledge as a set of about 150 tuples, each corresponding to a Common Core concept, skill, or specific type of bug or missing heuristic."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
sources:
  - id: lenat-2014
    resource: "https://doi.org/10.1007/s40593-014-0016-x"
    title: "Lenat, D. B., & Durlach, P. J. (2014). Reinforcing Math Knowledge by Immersing Students in a Simulated Learning-By-Teaching Experience. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-014-0016-x"
    author: "Lenat, D. B., & Durlach, P. J"
---

# BELLA student model: about 150 tuples covering Common Core concepts, skills, bugs and missing heuristics, each scored 0–100 with full change history

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
BELLA models each student's domain knowledge as a set of about 150 tuples, each corresponding to a Common Core concept, skill, or specific type of bug or missing heuristic. Each element is summarized as a number from 0 to 100, and BELLA stores the entire history of every model element — every action or inaction that caused the number to change. The teacher can drill down through a UI to see the exact historical in-game events that caused each revision. The authors estimate the model will grow to about 200 tuples when the sixth-grade Common Core curriculum is fully covered.

## Design Implications

### Context
#### Requirements
- Model initialization method not yet settled: options include pretesting, a normative 6th-grade model, interviewing the teacher or student, or starting with a very incompetent Elle
#### Constraints
- The authors hypothesize but have not tested that this set of about 150 elements suffices for the BELLA task

### Target Learners
- Sixth-grade mathematics students

### Learning Goals
- Diagnosing and tracking specific Common Core concepts, skills, bugs and heuristics in pre-algebra

### Claims
- 

## Related Designs
- Bella Simulated Lbt Architecture

## Examples
-

## Key Sources
- Lenat, D. B., & Durlach, P. J. (2014). Reinforcing Math Knowledge by Immersing Students in a Simulated Learning-By-Teaching Experience. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-014-0016-x
