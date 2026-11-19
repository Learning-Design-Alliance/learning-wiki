---
type: design
id: opt-in-study-group-matching-system
title: Open-source opt-in study group matching system with reassignment rounds
description: The article describes an opt-in study group formation system integrated into a large remote course.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: sumer-kohli-2023
    resource: "https://doi.org/10.1145/3545945.3569885"
    title: "Sumer Kohli, Neelesh Ramachandran, Ana Tudor, Gloria Tumushabe, Olivia Hsu, and Gireeja Ranade. 2023. Inclusive Study Group Formation At Scale. In Proceedings of the 54th ACM Technical Symposium on Computer Science Education V. 1 (SIGCSE 2023). https://doi.org/10.1145/3545945.3569885"
    author: Sumer Kohli, Neelesh Ramachandran, Ana Tudor, Gloria Tumushabe, Olivia Hsu, and Gireeja Ranade
---

# Open-source opt-in study group matching system with reassignment rounds

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 1 claim rests on one study

## Description
The article describes an opt-in study group formation system integrated into a large remote course. Students "may choose to form their own group, ask us to form a group, or have no group at all". A Week 1 survey collects scheduling, course-background and optional demographic information; reassignment rounds run in Weeks 5 and 9; a three-phase partitioning algorithm assigns groups of four to six students and removes solo-status by pairing students sharing gender and race identities. All processes, surveys and code are released open-source.

## Design Implications

### Context
#### Requirements
- Student preference survey data (schedule, timezone, coursework, optional gender/race identity) collected at course start
- Course scale large enough that demographic partitions are viable; instructor integration into course structure
#### Constraints
- The course composition may make avoiding solo-status impossible for some students; the process stops once solo-status students fall below a configurable threshold
- Partitions smaller than four students must be merged into neighboring partitions

### Target Learners
- Undergraduate students in large introductory Engineering/CS courses, including students from underrepresented groups

### Learning Goals
- Building long-term study groups and social support networks for coursework

### Claims
- [Underrepresented Students Request Software Matched Groups More](../claims/underrepresented-students-request-software-matched-groups-more.md) [+M]
- [Comparable Group Experiences Across Demographics](../claims/comparable-group-experiences-across-demographics.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Sumer Kohli, Neelesh Ramachandran, Ana Tudor, Gloria Tumushabe, Olivia Hsu, and Gireeja Ranade. 2023. Inclusive Study Group Formation At Scale. In Proceedings of the 54th ACM Technical Symposium on Computer Science Education V. 1 (SIGCSE 2023). https://doi.org/10.1145/3545945.3569885
