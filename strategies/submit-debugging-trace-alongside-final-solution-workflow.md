---
type: strategy
id: submit-debugging-trace-alongside-final-solution-workflow
title: "Classroom workflow: publish a debugging task, have students run an Evaluation session, and review the exported report and trace alongside the final solution"
description: "The article describes a lightweight classroom workflow: an instructor publishes a debugging task with its source, tests, and any custom test-command patterns; students open it in VS Code, run an Evaluation session, de..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: jiatong-liu-2026
    resource: "https://doi.org/10.1145/3837729.3840500"
    title: "Jiatong Liu, Xue Yao, Zehua Zhang, and Yongqiang Tian. (2026). DebugTracker: Lightweight Process Evidence for Classroom Debugging. Companion Proceedings of the 2026 ACM SIGPLAN International Conference on Systems, Programming, Languages, and Applications: Software for Humanity (SPLASH Companion '26). https://doi.org/10.1145/3837729.3840500"
    author: Jiatong Liu, Xue Yao, Zehua Zhang, and Yongqiang Tian
---

# Classroom workflow: publish a debugging task, have students run an Evaluation session, and review the exported report and trace alongside the final solution

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article describes a lightweight classroom workflow: an instructor publishes a debugging task with its source, tests, and any custom test-command patterns; students open it in VS Code, run an Evaluation session, debug normally, and "submit the exported report and trace alongside their final solution". An instructor or teaching assistant then reviews the process evidence directly and can attach rubric labels through the human-label mechanism, stored as later events leaving the original trace intact.

## Design Implications

### Context
#### Requirements
- Instructor-authored tasks with source, tests, and optionally custom test-command patterns; students and reviewers use VS Code with the extension installed
#### Constraints
- Reviewers attach labels after the session; the article states these labels are stored as separate events rather than overwriting the raw trace

### Target Learners
- Students in programming courses completing debugging exercises

### Target Learning Goals
- Demonstrating a systematic debugging narrative: failure reproduced, suspect code inspected, hypothesis before edit, targeted repair, verification after edit

## Related Strategies
- 

## Examples
-

## Key Sources
- Jiatong Liu, Xue Yao, Zehua Zhang, and Yongqiang Tian. (2026). DebugTracker: Lightweight Process Evidence for Classroom Debugging. Companion Proceedings of the 2026 ACM SIGPLAN International Conference on Systems, Programming, Languages, and Applications: Software for Humanity (SPLASH Companion '26). https://doi.org/10.1145/3837729.3840500
