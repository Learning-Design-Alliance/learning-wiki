---
type: pattern
id: explicit-versus-inferred-compliance-prompt-taxonomy
title: "Two-category taxonomy of SRL prompts by how compliance can be evaluated: explicit vs inferred compliance prompts"
description: "The article classifies MetaTutor's SRL prompts into two categories based on how compliance can be evaluated."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-02
sources:
  - id: lallé-2017
    resource: "https://educationaldatamining.org/EDM2017/"
    title: "Lallé, S., Mudrick, N., Conati, C., Taub, M., Azevedo, R. (2017). On the Influence on Learning of Student Compliance with Prompts Fostering Self-Regulated Learning. Proceedings of the 10th International Conference on Educational Data Mining. https://educationaldatamining.org/EDM2017/"
    author: Lallé, S., Mudrick, N., Conati, C., Taub, M., Azevedo, R
---

# Two-category taxonomy of SRL prompts by how compliance can be evaluated: explicit vs inferred compliance prompts

> **Pattern** · [All patterns](index.md)
> **Evidence** · 6 claims (3 for, 3 mixed) · 1 study (1 associational), `q3` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The article classifies MetaTutor's SRL prompts into two categories based on how compliance can be evaluated. "Explicit compliance prompts" are those for which compliance "can be explicitly assessed from students subsequent responses", e.g. prompts requiring a yes/no answer or a specific action within a time frame. "Inferred compliance prompts" are those for which "compliance needs to be inferred by mining a variety of behaviors", such as staying on or moving from a page. The article mines window length, number of fixations, and number of SRL strategies to evaluate the latter.

## Design Implications

### Context
#### Requirements
- For inferred prompts, the system must log interaction and eye-tracking behaviors in data windows following each prompt delivery
#### Constraints
- Explicit compliance prompts require additional interactions that "might not always be possible, or might even be intrusive for some students"; for inferred prompts "there is no clear definition of what compliance means"

### Target Learners
- college students learning with an intelligent tutoring system

### Target Goals
- self-regulated learning strategy use

### Claims

- [No Learning Effect For Metacognitive Monitoring Prompts](../claims/no-learning-effect-for-metacognitive-monitoring-prompts.md) [~M]
- [More fixations on the learning content after an add-subgoal prompt are associated with higher learning gains, suggesting complying with that prompt may not be effective](../claims/add-subgoal-prompt-compliance-may-not-help-learning.md) [~M]
- [Compliance with MetaTutor's summarize, stay-on-subgoal, move-to-next-subgoal, and open-diagram prompts shows no significant effect on learning gains](../claims/no-learning-effect-for-four-explicit-srl-prompts.md) [~W]
- [Higher compliance with MetaTutor's review-notes prompt is associated with larger proportional learning gains](../claims/review-notes-compliance-predicts-learning-gains.md) [+W]
- [Higher compliance with MetaTutor's revise-summary prompt is associated with larger proportional learning gains](../claims/revise-summary-compliance-predicts-learning-gains.md) [+W]
- [Higher compliance with MetaTutor's suggest-subgoal prompt is associated with larger proportional learning gains](../claims/suggest-subgoal-compliance-predicts-learning-gains.md) [+W]

## Related Patterns
- 

## Examples
-

## Key Sources
- Lallé, S., Mudrick, N., Conati, C., Taub, M., Azevedo, R. (2017). On the Influence on Learning of Student Compliance with Prompts Fostering Self-Regulated Learning. Proceedings of the 10th International Conference on Educational Data Mining. https://educationaldatamining.org/EDM2017/
