---
type: design
id: social-visualization-persuasive-pattern
title: Socially-oriented persuasive strategies implemented as social visualizations of student performance data in a learning support system.
description: "This design pattern implements persuasive strategies (social learning, social comparison, competition) as social visualizations showing students' assessment grades inside a learning support system."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
sources:
  - id: orji-2021
    resource: "https://doi.org/10.1007/s40593-021-00260-4"
    title: "Orji, F. A., Greer, J., & Vassileva, J. (2021). Evaluating a Persuasive Intervention for Engagement in a Large University Class. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00260-4"
    author: "Orji, F. A., Greer, J., & Vassileva, J"
---

# Socially-oriented persuasive strategies implemented as social visualizations of student performance data in a learning support system.

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 1 claim rests on one study

## Description
This design pattern implements persuasive strategies (social learning, social comparison, competition) as social visualizations showing students' assessment grades inside a learning support system. The article states "The persuasive strategy defines what information is visualized, e.g. whether the student can see just the score of the group (social learning) or also their own score to easily compare it with that of the group (social comparison) and or with specific peers (competition)." The visualizations update dynamically and include emoji feedback, and the authors note they "use familiar designs and can be implemented in any domain to represent various measures of student performance."

## Design Implications

### Context
#### Requirements
- Access to student assessment grade data to populate the visualizations
- Pseudonymized display of peers' grades and points to protect privacy while letting each viewer see their own real ID
- A learning support system into which the visualizations can be integrated
#### Constraints
- The article notes it was not possible to make the behaviour of others directly observable due to the asynchronous nature of the online activities and privacy considerations, so the social learning strategy was implemented as aggregated performance of other students

### Target Learners
- University students in large blended undergraduate courses

### Learning Goals
- Increased engagement in online learning activities

### Claims
- [Persuasive Social Visualizations Increase Lss Engagement](../claims/persuasive-social-visualizations-increase-lss-engagement.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Orji, F. A., Greer, J., & Vassileva, J. (2021). Evaluating a Persuasive Intervention for Engagement in a Large University Class. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00260-4
