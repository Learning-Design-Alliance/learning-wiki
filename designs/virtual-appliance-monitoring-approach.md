---
type: design
id: virtual-appliance-monitoring-approach
title: Virtual appliances as self-contained, instrumentable environments for learning analytics
description: "The approach packages a course's full tool set in a virtual machine distributed to students, exploiting virtualization's isolation, compatibility and encapsulation so that \"a multi-level comprehensive monitoring schem..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-29
sources:
  - id: romero-zaldivar-2012
    resource: "https://doi.org/10.1016/j.compedu.2011.12.003"
    title: "Romero-Zaldivar, V.-A., Pardo, A., Burgos, D., & Delgado Kloos, C. (2012). Monitoring student progress using virtual appliances: A case study. Computers & Education, 58(4), 1058–1067. https://doi.org/10.1016/j.compedu.2011.12.003"
    author: "Romero-Zaldivar, V.-A., Pardo, A., Burgos, D., & Delgado Kloos, C"
---

# Virtual appliances as self-contained, instrumentable environments for learning analytics

> **Design** · [All designs](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The approach packages a course's full tool set in a virtual machine distributed to students, exploiting virtualization's isolation, compatibility and encapsulation so that "a multi-level comprehensive monitoring scheme can be deployed" inside the appliance. Rather than forcing activities onto a generic platform, the design places "generic 'sensors' closer to the environment in which students interact" — instrumenting applications with wrapper programs and relaying events through the Subversion client to a central server. This trades a tool-embedding approach (high specialization, partial coverage) for generic monitoring with broad coverage of the student's actual workspace.

## Design Implications

### Context
#### Requirements
- All course tools must be installed in the appliance; each tool to be recorded must be instrumentalized individually (wrapper programs or log harvesting); a central collection server and version control channel must be configured
#### Constraints
- Monitoring must comply with data protection legislation (EU Directive 1995/46/EC, Spanish LOPD), so students must be informed and can disable monitoring; if the tool set changes, the monitoring module must be modified unless recording is moved to the operating system level

### Target Learners
- university students in tool-intensive courses
- students in face-to-face or distance settings

### Learning Goals
- predicting academic achievement
- instructor monitoring and adjustment of course activities

### Claims

- [Virtual Appliance Workspace Monitoring Feasible](../claims/virtual-appliance-workspace-monitoring-feasible.md) [+M]
- [Tool Use Events Correlate With Final Grade](../claims/tool-use-events-correlate-with-final-grade.md) [+M]
- Regression Worktime Profiler Predicts Grade [+M]
- [In face-to-face scenarios, workspace monitoring data yields a better estimate of academic achievement than LMS forum data](../claims/workspace-monitoring-beats-lms-forum-prediction.md) [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Romero-Zaldivar, V.-A., Pardo, A., Burgos, D., & Delgado Kloos, C. (2012). Monitoring student progress using virtual appliances: A case study. Computers & Education, 58(4), 1058–1067. https://doi.org/10.1016/j.compedu.2011.12.003
