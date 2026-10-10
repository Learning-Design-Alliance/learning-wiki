---
type: design
id: prompt-programming-platform-bug-injection-pipeline
title: Prompt Programming platform with bug injection pipeline
description: A publicly available web platform supporting prompt-based programming through dialogue with a GenAI assistant (GPT-4o-mini), hidden-test execution, and direct code editing.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: victor-alexandru-pădurean-kaitlin-riegel-alkis
    resource: "https://doi.org/10.1145/3765964.3811667"
    title: "Victor-Alexandru Pădurean, Kaitlin Riegel, Alkis Gotovos, Jyotika Mahapatra, Ahana Ghosh, Paul Denny, Juho Leinonen, James Prather, and Adish Singla. 2026. When AI Is Wrong on Purpose: How Students Respond to Buggy GenAI Code. Proceedings of the ACM Conference on International Computing Education Research Vol. 1 (ICER 2026 Vol. 1). https://doi.org/10.1145/3765964.3811667"
---

# Prompt Programming platform with bug injection pipeline

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 2 studies (1 causal, 1 associational), `q3` · 0 of 2 report an effect size · 2 claims rest on one study

## Description
A publicly available web platform supporting prompt-based programming through dialogue with a GenAI assistant (GPT-4o-mini), hidden-test execution, and direct code editing. The bug injection pipeline acts as middleware that intercepts correct generated code and replaces it with validated, runnable near-miss variants containing subtle faults. Students receive a problem specification, craft a natural-language prompt, and can iterate by reprompting or editing code directly. The platform was deployed in a CS1 course at the University of Auckland with five programming tasks covering arrays, matrices, and binary operations.

## Design Implications

### Context
#### Requirements
- A GenAI code-generation model and hidden unit tests to validate that injected bug variants compile and fail
#### Constraints
- Bug injection is limited to a set of candidate variants, permitting some slip-through cases where original correct code is served unchanged

### Target Learners
- CS1 introductory programming students

### Learning Goals
- code review
- debugging
- prompt specification
- verification of AI-generated code

### Claims
- [Injected Bugs Eliciting Direct Edits Natural Bugs Reprompting](../claims/injected-bugs-eliciting-direct-edits-natural-bugs-reprompting.md) [+M]
- [Higher Immediate Success After Injected Bugs](../claims/higher-immediate-success-after-injected-bugs.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Victor-Alexandru Pădurean, Kaitlin Riegel, Alkis Gotovos, Jyotika Mahapatra, Ahana Ghosh, Paul Denny, Juho Leinonen, James Prather, and Adish Singla. 2026. When AI Is Wrong on Purpose: How Students Respond to Buggy GenAI Code. Proceedings of the ACM Conference on International Computing Education Research Vol. 1 (ICER 2026 Vol. 1). https://doi.org/10.1145/3765964.3811667
