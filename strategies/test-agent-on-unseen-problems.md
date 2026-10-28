---
type: strategy
id: test-agent-on-unseen-problems
title: Test an apprentice learner agent on previously unseen problems to determine when it has correctly learned target skills
description: When authoring with a simulated student, it is difficult to determine when the agent has correctly learned the target skills.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: christopher-j-maclellan-kenneth-r-koedinger-2022
    resource: "https://doi.org/10.1007/s40593-020-00214-2"
    title: "Christopher J. MacLellan & Kenneth R. Koedinger. (2022). Domain-General Tutor Authoring with Apprentice Learner Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00214-2"
    author: "Christopher J. MacLellan & Kenneth R. Koedinger"
---

# Test an apprentice learner agent on previously unseen problems to determine when it has correctly learned target skills

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
When authoring with a simulated student, it is difficult to determine when the agent has correctly learned the target skills. The authors address this by testing the agent on previously unseen problems, incrementally evaluating its performance on each subsequent training problem before providing feedback. This solution is common to both determining whether a human student has learned something and verifying that a program is correctly implemented.

## Design Implications

### Context
#### Requirements
- Requires a set of problems that can be presented incrementally with performance evaluated before feedback
#### Constraints
- 

### Target Learners
- tutor authors training apprentice learner models

### Target Learning Goals
- verifying that learned expert models are correct

## Claims

- [Apprentice learner models act as a check against expert blind spots because they start without target skills](../claims/apprentice-learner-models-check-expert-blind-spots.md) [+W]
- [Apprentice learner models are domain-general: they learn expert models across eight tutor domains without specialized domain knowledge](../claims/apprentice-learner-models-domain-general.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Christopher J. MacLellan & Kenneth R. Koedinger. (2022). Domain-General Tutor Authoring with Apprentice Learner Models. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-020-00214-2
