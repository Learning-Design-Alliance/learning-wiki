---
type: strategy
id: tool-layer-tutoring-component-separation
title: Build tutoring systems as a robust tool layer attached to a tutoring component responsible for feedback and scaffolding
description: "The author recommends constructing instructional systems as a powerful tool layer attached to a tutoring component, allowing developers to specialize: some focus on tool and interface development while others focus on..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: ritter-2016
    resource: "https://doi.org/10.1007/s40593-015-0062-z"
    title: "Ritter, S. (2016). Plug-in Tutor Agents: Still Pluggin'. International Journal of Artificial Intelligence in Education, 26, 405–415. https://doi.org/10.1007/s40593-015-0062-z"
    author: Ritter, S
---

# Build tutoring systems as a robust tool layer attached to a tutoring component responsible for feedback and scaffolding

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (2 for, 3 mixed) · 1 study (1 theoretical), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The author recommends constructing instructional systems as a powerful tool layer attached to a tutoring component, allowing developers to specialize: some focus on tool and interface development while others focus on instructional pedagogy. This division "results in a more flexible system and one that can appropriately divide the labor for building such systems."

## Design Implications

### Context
#### Requirements
- A clear messaging protocol between tool and tutor components
#### Constraints
- 

### Target Learners
- students in intelligent tutoring systems

### Target Learning Goals
- domain learning through tool-based problem solving

## Claims

- [The commentary pattern can cause tool-tutor desynchronization when students act faster than the tutor reacts](../claims/commentary-pattern-synchronization-problem.md) [~W]
- [Leveraging existing OS mechanisms (script recording, accessibility interfaces) for tutoring is problematic for widespread deployment](../claims/os-mechanism-tutoring-deployment-problematic.md) [~W]
- [The permission pattern, where tool actions await tutor approval, addresses cases where preventing student action is the appropriate instructional response](../claims/permission-pattern-tutor-approval.md) [+W]
- [The tool-tutor architecture's plug-in vision for off-the-shelf software did not come to pass, but its pedagogical approach remains relevant](../claims/plug-in-tutor-architecture-retrospective.md) [~W]
- [Semantic-level communication between tool and tutor allows changes in either component without modifying both together](../claims/semantic-messaging-tool-tutor-decoupling.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Ritter, S. (2016). Plug-in Tutor Agents: Still Pluggin'. International Journal of Artificial Intelligence in Education, 26, 405–415. https://doi.org/10.1007/s40593-015-0062-z
