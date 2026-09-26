---
type: element
id: assessment-tool-apis-shared-infrastructure
title: Application programming interfaces as shared infrastructure for automated assessment tools
description: "The report identifies two classes of software needed for computer-based automated assessment tools: individual tool applications and application programming interfaces."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-25
sources:
  - id: chung-1997
    resource: "https://eric.ed.gov/?id=ED418102"
    title: "Chung, G. K. W. K., Herl, H. E., Klein, D. C. D., O'Neil, H. F., Jr., & Schacter, J. (1997). Estimate of the Potential Costs and Effectiveness of Scaling Up CRESST Assessment Software. https://eric.ed.gov/?id=ED418102"
    author: "Chung, G. K. W. K., Herl, H. E., Klein, D. C. D., O'Neil, H. F., Jr., & Schacter, J"
---

# Application programming interfaces as shared infrastructure for automated assessment tools

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The report identifies two classes of software needed for computer-based automated assessment tools: individual tool applications and application programming interfaces. "Application programming interfaces provide transparent layers for collecting, parsing, managing, analyzing, and outputting data." Shared APIs for authoring, data logging, reporting, collaboration, search, simulation, text classification, scoring, and process analysis avoid recreating code per tool; for example, one standard data logging API serves all tools.

## Design Implications

### Context
#### Requirements
- Tools interact indirectly with the APIs while end users interact directly with the application software
#### Constraints
- The text classifier API "may not be scalable if the number of requested comparisons is large, or if the textbase used for comparison is large"

### Target Learners
- students and trainees using the assessment tools

### Target Learning Goals
- automated scoring, reporting, and process analysis of assessment data

## Related Elements

- [CRESST Integrated Assessment System: a computer-based suite of performance assessment tasks](cresst-integrated-assessment-system.md)
- [Eight proposed CRESST assessment tools with specifications and scalability outlooks](cresst-proposed-assessment-tools.md)

## Examples

- [Use a spiral development model with periodic prototype deliveries for assessment software](../strategies/spiral-development-for-assessment-software.md)

## Key Sources
- Chung, G. K. W. K., Herl, H. E., Klein, D. C. D., O'Neil, H. F., Jr., & Schacter, J. (1997). Estimate of the Potential Costs and Effectiveness of Scaling Up CRESST Assessment Software. https://eric.ed.gov/?id=ED418102
