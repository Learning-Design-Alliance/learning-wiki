---
type: strategy
id: fuzzy-cluster-task-difficulty-strategy
title: Recommend task difficulty per student from fuzzy cluster membership of prior grades
description: "The article recommends using fuzzy cluster membership of a student's previous evaluations to set task difficulty: \"it is possible to more accurately determine the recommended level of difficulty of tasks for each stud..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: serhiy-balovsyak-2023
    resource: "https://doi.org/10.5815/ijmecs.2023.06.03"
    title: "Serhiy Balovsyak, Oleksandr Derevyanchuk, Hanna Kravchenko, Yuriy Ushenko, Zhengbing Hu. (2023). Clustering Students According to their Academic Achievement Using Fuzzy Logic. International Journal of Modern Education and Computer Science (IJMECS), Vol.15, No.6, pp. 31-43. https://doi.org/10.5815/ijmecs.2023.06.03"
    author: Serhiy Balovsyak, Oleksandr Derevyanchuk, Hanna Kravchenko, Yuriy Ushenko, Zhengbing Hu
---

# Recommend task difficulty per student from fuzzy cluster membership of prior grades

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 2 studies (1 qualitative, 1 design), `q2` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The article recommends using fuzzy cluster membership of a student's previous evaluations to set task difficulty: "it is possible to more accurately determine the recommended level of difficulty of tasks for each student, depending on his previous evaluations." Each cluster number corresponds to a corresponding level of difficulty of the task, and a student with memberships in two clusters receives main tasks at one level and additional tasks at the other.

## Design Implications

### Context
#### Requirements
- Cluster analysis of intermediate and final learning results using the developed software, with fuzzy membership functions computed for each student
#### Constraints
- Recommendations are based on previous learning results in the analyzed subjects; clusters may not be clearly separated

### Target Learners
- students assessed by numeric subject scores in electronic learning systems

### Target Learning Goals
- adjusting the level of difficulty of learning tasks to individual achievement

### Affordances
- [Fuzzy Membership Cluster Account](../research-methods/fuzzy-membership-functions-as-an-account-of-borderline-student-cluster-membership.md)

## Claims

- [Fuzzy membership functions correctly determine students' cluster membership even when clusters are not clearly separated](../claims/fuzzy-membership-correct-borderline-assignment.md) [+W]
- [Fuzzy membership degrees support individualized task-difficulty recommendations, e.g. student iv=12 assigned mostly to cluster 3 with additional cluster 2 tasks](../claims/fuzzy-membership-task-difficulty-recommendation.md) [+W]
- [A near-normal distribution of cluster sizes indicates the chosen task difficulty level is appropriate](../claims/normal-cluster-size-distribution-difficulty-check.md) [+W]
- [K-12 students and teachers both consider AI imperfect at detecting students' knowledge and assigning appropriate tasks, and therefore prefer more human control over AI decisions](../claims/students-teachers-see-ai-imperfect-prefer-human-control.md) [-W]

## Related Strategies

- [In online flipped classrooms, set appropriate task difficulty, organize team grouping, build incentive mechanisms, and use multi-dimensional digital evaluation](online-flipped-classroom-task-difficulty-grouping-incentives.md)

## Examples
-

## Key Sources
- Serhiy Balovsyak, Oleksandr Derevyanchuk, Hanna Kravchenko, Yuriy Ushenko, Zhengbing Hu. (2023). Clustering Students According to their Academic Achievement Using Fuzzy Logic. International Journal of Modern Education and Computer Science (IJMECS), Vol.15, No.6, pp. 31-43. https://doi.org/10.5815/ijmecs.2023.06.03
