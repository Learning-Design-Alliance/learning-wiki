---
type: design
id: pykinetic-parsons-problem-design
title: "Parsons problems design for smartphones: single combined area, pre-indented single LOCs, incomplete LOCs with menu-based SE prompts"
description: "The article's Parsons problems differ from common implementations in four ways the authors enumerate."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-28
sources:
  - id: fabic-2019
    resource: "https://doi.org/10.1007/s40593-019-00184-0"
    title: "Fabic, G. V. F., Mitrovic, A., & Neshatian, K. (2019). Evaluation of Parsons Problems with Menu-Based Self-Explanation Prompts in a Mobile Python Tutor. International Journal of Artificial Intelligence in Education, 29, 507–535. https://doi.org/10.1007/s40593-019-00184-0"
    author: "Fabic, G. V. F., Mitrovic, A., & Neshatian, K"
---

# Parsons problems design for smartphones: single combined area, pre-indented single LOCs, incomplete LOCs with menu-based SE prompts

> **Design** · [All designs](index.md)
> **Evidence** · 4 claims (2 for, 2 mixed) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 4 claims rest on one study

## Description
The article's Parsons problems differ from common implementations in four ways the authors enumerate. First, students solve problems "in the same area where the LOCs are presented", with no separation between problem and solution space, making better use of limited smartphone screen space. Second, all lines are provided with correct indentation as scaffolding for novices. Third, all blocks contain only single LOCs, encouraging students to think about each individual line. Fourth, the problems contain incomplete LOCs accompanied by menu-based SE prompts that learners must answer upon solving them, targeting both procedural and conceptual knowledge.

## Design Implications

### Context
#### Requirements
- Menu-based SE prompts require feedback on incorrect choices so learners with misconceptions receive guidance
#### Constraints
- Combining problem and solution areas might overwhelm learners because all LOCs are displayed at once, though the authors did not observe this as an issue given the 16-LOC limit

### Target Learners
- novice programmers learning on smartphones

### Learning Goals
- code sequencing and writing skills
- declarative and procedural Python knowledge

### Claims

- Menu Based Se Prompts Increase Normalized Gains [+M]
- [Low prior knowledge students learned more from PyKinetic's Parsons problems than high prior knowledge students, especially in the experimental group with SE prompts](../claims/parsons-problems-benefit-low-prior-knowledge-students.md) [+W]
- [The experimental group spent significantly more time per problem and completed significantly fewer problems than the control group](../claims/se-prompts-increase-time-per-problem.md) [~W]
- [Both groups improved significantly on harder-to-guess questions, and the experimental group outperformed the control group on them at post-test](../claims/se-prompts-harder-to-guess-questions.md) [+W]
- [High prior knowledge students scored significantly higher on SE prompts overall and on conceptual SE prompts, but not on procedural SE prompts](../claims/hp-students-score-higher-se-prompts.md) [~W]

## Related Designs
- Pykinetic Mobile Python Tutor

## Examples
-

## Key Sources
- Fabic, G. V. F., Mitrovic, A., & Neshatian, K. (2019). Evaluation of Parsons Problems with Menu-Based Self-Explanation Prompts in a Mobile Python Tutor. International Journal of Artificial Intelligence in Education, 29, 507–535. https://doi.org/10.1007/s40593-019-00184-0
