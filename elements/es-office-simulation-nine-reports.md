---
type: element
id: es-office-simulation-nine-reports
title: Local office simulation model with nine statistical output reports
description: "The report's central artifact is a computer simulation of a local office day, stepping through applicant interviews, job-order handling and miscellaneous tasks hour by hour while gathering statistics on system behavior."
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-25
sources:
  - id: cohen-1975
    resource: "https://eric.ed.gov/?id=CE005601"
    title: "Cohen, Malcolm S. (1975). A Study of On-Line Use of Job Information in Employment Service Local Offices. Volume II: A Simulation Study. https://eric.ed.gov/?id=CE005601"
    author: Cohen, Malcolm S
---

# Local office simulation model with nine statistical output reports

> **Element** · [All elements](index.md)

## Description
The report's central artifact is a computer simulation of a local office day, stepping through applicant interviews, job-order handling and miscellaneous tasks hour by hour while gathering statistics on system behavior. After a run, nine reports can be requested: Input, Applicant, Receptionist Facility, Receptionist Queue, Employment Officer Facility, Interview Queue, Terminal Facility, Terminal Queue, and Job Order Queue reports. Each provides hourly and full-day statistics such as staff utilization, queue contents, and waiting-time means and standard deviations, enabling diagnosis of bottlenecks such as terminal waiting.

## Design Implications

### Context
#### Requirements
- User-supplied input parameters: arrival means per hour, activity-duration distributions, and hourly staff and terminal levels
#### Constraints
- Job display area is modeled as effectively unlimited capacity; a microfiche-based system would require setting capacity to the number of readers
- Miscellaneous work is measured only in one-minute intervals

### Target Learners
- Employment Service local office managers and planners

### Target Learning Goals
- Diagnosing office bottlenecks and evaluating staffing and terminal configurations

### Affordances
- [Descriptive Simulation Modeling Framework Es Office](../theories/descriptive-simulation-modeling-framework-es-office.md)

## Related Elements
- 

## Examples
-

## Key Sources
- Cohen, Malcolm S. (1975). A Study of On-Line Use of Job Information in Employment Service Local Offices. Volume II: A Simulation Study. https://eric.ed.gov/?id=CE005601
