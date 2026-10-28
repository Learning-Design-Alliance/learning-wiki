---
type: strategy
id: author-by-tutoring-machine-learning-agent
title: Author by tutoring a machine-learning agent rather than demonstrating solutions
description: When authoring an expert model for a cognitive tutor, interactively tutor a machine-learning agent by posing problems, providing yes/no feedback on its suggested steps, and demonstrating steps only when the agent cann...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: matsuda-2015
    resource: "https://doi.org/10.1007/s40593-014-0020-1"
    title: "Matsuda, N., Cohen, W. W., & Koedinger, K. R. (2015). Teaching the Teacher: Tutoring SimStudent Leads to More Effective Cognitive Tutor Authoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-014-0020-1"
    author: "Matsuda, N., Cohen, W. W., & Koedinger, K. R"
---

# Author by tutoring a machine-learning agent rather than demonstrating solutions

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
When authoring an expert model for a cognitive tutor, interactively tutor a machine-learning agent by posing problems, providing yes/no feedback on its suggested steps, and demonstrating steps only when the agent cannot proceed. This strategy embeds formative assessment naturally, since observing the agent's performance reveals flaws in the expert model, and reduces the number of demonstrations needed as learning progresses. The article recommends this over pure demonstration based on both simulation and case study results.

## Design Implications

### Context
#### Requirements
- The author must be able to identify errors in solution attempts and provide correctness feedback on the agent's suggested steps.
#### Constraints
- Authors must tag purposefully demonstrated incorrect production rules accordingly, since the agent does not recognize incorrect steps as incorrect.

### Target Learners
- Domain experts authoring cognitive tutors

### Target Learning Goals
- Efficient and accurate creation of expert models for intelligent tutoring systems

## Claims

- [Authoring by Tutoring yields a more accurate expert model than Authoring by Demonstration while maintaining the same level of completeness](../claims/authoring-by-tutoring-higher-accuracy-than-demonstration.md) [+W]
- [Authoring by Tutoring requires less time than Authoring by Demonstration](../claims/authoring-by-tutoring-more-efficient-than-demonstration.md) [+W]
- [Explicit negative feedback on incorrect production applications drives the accuracy advantage of Authoring by Tutoring](../claims/negative-feedback-drives-tutoring-accuracy-advantage.md) [+W]
- [Authoring by Tutoring produces fewer errors of all types than Authoring by Demonstration](../claims/tutoring-fewer-error-types-than-demonstration.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Matsuda, N., Cohen, W. W., & Koedinger, K. R. (2015). Teaching the Teacher: Tutoring SimStudent Leads to More Effective Cognitive Tutor Authoring. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-014-0020-1
