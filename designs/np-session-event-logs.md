---
type: design
id: np-session-event-logs
title: NP session event logs as embedded assessment data
description: "Newton's Playground automatically records detailed gameplay telemetry for assessment purposes."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-16
sources:
  - id: ventura-2013
    resource: "https://eric.ed.gov/?q=Assessing+Persistence+in+Educational+Games"
    title: "Ventura, M., Shute, V., & Small, M. (2013). Assessing Persistence in Educational Games. Design Recommendations for Intelligent Tutoring Systems - Volume 2: Adaptive Instructional Management. https://eric.ed.gov/?q=Assessing+Persistence+in+Educational+Games"
    author: "Ventura, M., Shute, V., & Small, M"
---

# NP session event logs as embedded assessment data

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 associational), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Newton's Playground automatically records detailed gameplay telemetry for assessment purposes. "NP automatically uploads log files to a server for each gaming session (i.e., log activity between login and logout)." Each event log for a puzzle visit records features such as game_time, pause_time, restart_count, object_count, nudge_count, erase_count, pin_count, agent vectors, ball trajectory, silver and gold trophy status, and whether the problem was solved. These logs supplied the raw data from which the game-based assessment of persistence was derived.

## Design Implications

### Context
#### Requirements
- Log files must be uploaded to a server for each gaming session between login and logout
#### Constraints
- 

### Target Learners
- middle school students

### Learning Goals
- stealth assessment of persistence during gameplay

### Claims
- [Gap Construct Validity Persistence Measures](../claims/gap-construct-validity-persistence-measures.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Ventura, M., Shute, V., & Small, M. (2013). Assessing Persistence in Educational Games. Design Recommendations for Intelligent Tutoring Systems - Volume 2: Adaptive Instructional Management. https://eric.ed.gov/?q=Assessing+Persistence+in+Educational+Games
