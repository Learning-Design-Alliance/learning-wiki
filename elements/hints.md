---
type: element
id: hints
title: Hints
description: Hints are partial prompts or cues that help learners continue a task without fully giving away the answer.
canonical: true
status: review
generated:
  by: codex/unspecified
  at: 2026-04-07
sources:
  - id: koedinger-2007
    resource: "https://doi.org/10.1007/s10648-007-9049-0"
    title: "Koedinger, K. R., & Aleven, V. (2007). Exploring the assistance dilemma in experiments with cognitive tutors. *Educational Psychology Review, 19*(3), 239-264"
    author: "Koedinger, K. R., & Aleven, V"
  - id: wood-1976
    resource: "https://doi.org/10.1111/j.1469-7610.1976.tb00381.x"
    title: "Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89-100"
    author: "Wood, D., Bruner, J. S., & Ross, G"
---

# Hints

> **Element** · [All elements](index.md)
> **Evidence** · 6 claims (2 for, 4 mixed) · 6 studies (3 causal, 2 design, 1 associational), `q2`–`q3` · 1 of 6 report an effect size · 6 claims rest on one study

## Description
Hints are partial prompts or cues that help learners continue a task without fully giving away the answer. They are useful when the design goal is to preserve productive struggle while reducing the chance of stuckness, confusion, or abandonment.

## Design Implications

### Context
#### Requirements
- **A task learners can still attempt**: Hints are most useful when learners retain meaningful work to do.
- **Graduated support**: Strong implementations move from light cueing to more explicit help only as needed.
- **Alignment to the misconception or step**: Hints need to target the actual obstacle.
#### Constraints
- **Over-helping**: Hints that reveal too much can bypass learning.
- **Weak targeting**: Generic hints frustrate learners if they do not address the real issue.

### Target Learners
- Learners who are engaged but temporarily stuck on a problem, procedure, or draft move.

### Target Learning Goals
- Maintain momentum while supporting independence and strategy use.

### Affordances
- [Scaffolding and Fading](../principles/scaffolding-and-fading.md)
- [Immediate Feedback](../principles/immediate-feedback.md)
- [Guided Practice](../principles/guided-practice.md)

### Claims
<!-- Claims bearing on this element, each a link to a claim page followed by its evidence tag, e.g. [+M] -->
- [Hint takers spend less time on a question than learners who attempt it, regardless of attempt outcome](../claims/hint-takers-spend-less-time-than-attempters.md) [~W]
- [K-12 learners preferred incremental hints and multiple attempts over immediately revealed solutions](../claims/learners-prefer-incremental-hints-over-solutions.md) [+W]
- [GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer](../claims/gpt4-feedback-66-percent-targeted-35-percent-flawed.md) [~W]
- [Advanced students showed reduced attempts with all hint types, while novices did not clearly benefit and made slightly more submissions with Single-Issue Feedback](../claims/advanced-students-attempt-reduction-novices-not.md) [~W]
- [Learning gains showed significant main effects of hint condition and subject, with no significant condition-by-subject interaction](../claims/condition-subject-main-effects-no-interaction.md) [~W]
- [Persistence and performance costs concentrate among participants who used the AI to obtain direct solutions, while hint-users resemble controls](../claims/persistence-costs-concentrated-among-direct-solution-users.md) [+W]

## Related Elements
- [Feedback](feedback.md)
- [Coaching](coaching.md)
- [Worked Examples](worked-examples.md)

## Patterns That Use This Element
- [Mastery Learning](../patterns/mastery-learning.md)
- [Game-Based Mastery Learning (e.g., Duolingo Pattern)](../patterns/game-based-mastery-learning-eg-duolingo-pattern.md)

## Examples
- A tutoring system offers a first hint that points to the next subgoal, then a later hint that shows the relevant formula.
- A writing teacher gives a prompt about evidence quality instead of rewriting the paragraph for the student.

## Key Sources
- Koedinger, K. R., & Aleven, V. (2007). Exploring the assistance dilemma in experiments with cognitive tutors. *Educational Psychology Review, 19*(3), 239-264. [https://doi.org/10.1007/s10648-007-9049-0](https://doi.org/10.1007/s10648-007-9049-0)
- Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89-100. [https://doi.org/10.1111/j.1469-7610.1976.tb00381.x](https://doi.org/10.1111/j.1469-7610.1976.tb00381.x)
