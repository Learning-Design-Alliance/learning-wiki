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
> **Evidence** · 15 claims (5 for, 9 mixed, 1 against) · 12 studies (5 causal, 2 review, 2 associational, 2 design, 1 theoretical), `q2`–`q3` · 3 of 12 report an effect size · 14 claims rest on one study

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
- [K-12 learners preferred incremental hints and multiple attempts over immediately revealed solutions](../claims/learners-prefer-incremental-hints-over-solutions.md) [+W]
- [GPT-4 generates targeted corrective feedback for 66% of student errors, but 35% of hints are too general, incorrect, or give away the answer](../claims/gpt4-feedback-66-percent-targeted-35-percent-flawed.md) [~W]
- [Advanced students showed reduced attempts with all hint types, while novices did not clearly benefit and made slightly more submissions with Single-Issue Feedback](../claims/advanced-students-attempt-reduction-novices-not.md) [~W]
- [Learning gains showed significant main effects of hint condition and subject, with no significant condition-by-subject interaction](../claims/condition-subject-main-effects-no-interaction.md) [~W]
- [Persistence and performance costs concentrate among participants who used the AI to obtain direct solutions, while hint-users resemble controls](../claims/persistence-costs-concentrated-among-direct-solution-users.md) [+W]
- [Learning gains from ChatGPT-generated hints were not statistically significantly different from human tutor-authored hints, though ChatGPT gains were numerically higher in all subjects](../claims/chatgpt-gains-equivalent-human-tutor-hints.md) [~W]
- [Low-performing students access solutions more often than higher-performing students, while hint access does not differ across quartiles](../claims/solution-access-differs-hints-do-not.md) [~W]
- [Stimulus and phonemic cues did not notably help adult struggling readers name objects on the BNT](../claims/cues-did-not-help-adult-struggling-readers-naming.md) [-W]
- [Hint Factory MDP-generated hints gave correct next-step hints over 80% of the time and a pilot showed students solved more logic proofs with hints](../claims/hint-factory-mdp-hints-effective.md) [+W]
- [Feedback effects on time to solution did not differ significantly between novice and advanced students, though predicted trends suggest feedback was more beneficial for advanced students](../claims/no-significant-feedback-expertise-interaction.md) [~W]
- [Students incorrectly considered partially hinting images helpful](../claims/students-misjudge-hint-images-as-helpful.md) [~W]
- [Children give more disempowering help (right answers) to peers portrayed as incompetent and more empowering help (hints) to competent peers](../claims/children-disempowering-help-incompetent-peers.md) [~W]
- [Children aged 6–9 think peers who receive hints will learn more than peers who receive correct answers](../claims/children-hint-recipients-learn-more.md) [+W]
- [Children aged 7–9 give more empowerment help (hints) to competent peers and more non-empowerment help (answers) to incompetent peers](../claims/children-differentiate-help-by-peer-competence.md) [~W]

## The evidence by question

- *Do hints during practice improve learning over no hints, and do AI-written hints work as well as tutor-written ones?* [Learners receiving ChatGPT-generated hints showed statistically significant learning gains compared to a no-hint control in an online mathematics tutoring experiment](../claims/chatgpt-hints-significant-gains-versus-control.md) [+M]
- *Should help stop at a hint rather than give the solution, and what happens when learners can get the answer directly?* [Persistence and performance costs concentrate among participants who used the AI to obtain direct solutions, while hint-users resemble controls](../claims/persistence-costs-concentrated-among-direct-solution-users.md) [+M]

## Related Elements
- [Feedback](feedback.md)
- [Coaching](coaching.md)
- [Worked Examples](worked-examples.md)

## Patterns That Use This Element
- [Mastery Learning](../patterns/mastery-learning.md)
- [Game-Based Mastery Learning (e.g., Duolingo Pattern)](../patterns/game-based-mastery-learning.md)

## Examples

- A tutoring system offers a first hint that points to the next subgoal, then a later hint that shows the relevant formula.
- A writing teacher gives a prompt about evidence quality instead of rewriting the paragraph for the student.
- [Provide subgoal hints alongside step hints in proof construction](../strategies/subgoal-hints-in-proof-tutoring.md)

## Key Sources
- Koedinger, K. R., & Aleven, V. (2007). Exploring the assistance dilemma in experiments with cognitive tutors. *Educational Psychology Review, 19*(3), 239-264. [https://doi.org/10.1007/s10648-007-9049-0](https://doi.org/10.1007/s10648-007-9049-0)
- Wood, D., Bruner, J. S., & Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry, 17*(2), 89-100. [https://doi.org/10.1111/j.1469-7610.1976.tb00381.x](https://doi.org/10.1111/j.1469-7610.1976.tb00381.x)
