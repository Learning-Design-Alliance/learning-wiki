---
type: strategy
id: menu-based-response-selection-lbt
title: Menu-based response selection to sidestep natural language understanding in a tutoring dialogue
description: BELLA sidesteps the unsolved problem of unrestricted natural language understanding by providing the user with gestures and a menu of responses to choose from at each problem-solving step.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: lenat-2014
    resource: "https://doi.org/10.1007/s40593-014-0016-x"
    title: "Lenat, D. B., & Durlach, P. J. (2014). Reinforcing Math Knowledge by Immersing Students in a Simulated Learning-By-Teaching Experience. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-014-0016-x"
    author: "Lenat, D. B., & Durlach, P. J"
---

# Menu-based response selection to sidestep natural language understanding in a tutoring dialogue

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
BELLA sidesteps the unsolved problem of unrestricted natural language understanding by providing the user with gestures and a menu of responses to choose from at each problem-solving step. BELLA formulates five or ten possible choices via alternative-generator rules, then invokes meta-rules to select the three or four best — those most useful at revealing the user's mental model or helping correct Elle. The user usually sees just two or three revealing alternatives to select among.

## Design Implications

### Context
#### Requirements
- Requires a set of alternative-generator rules and meta-rules for selecting the most diagnostic or productive options
#### Constraints
- User expression is limited to the offered menu choices and gestures rather than free text

### Target Learners
- Sixth-grade mathematics students

### Target Learning Goals
- Revealing the user's mental model through their choice of tutoring responses

## Related Strategies

- Bella Simulated Lbt Architecture
- [Let students choose the complexity level of the LLM feedback](student-selected-feedback-complexity-level.md)

## Examples
-

## Key Sources
- Lenat, D. B., & Durlach, P. J. (2014). Reinforcing Math Knowledge by Immersing Students in a Simulated Learning-By-Teaching Experience. Int J Artif Intell Educ. https://doi.org/10.1007/s40593-014-0016-x
