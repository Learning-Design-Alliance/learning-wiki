---
type: strategy
id: threshold-priority-prompt-selection
title: Select adaptive prompts through rule-linked feedback thresholds and priorities
description: "When a production rule fires, APTA checks whether the resulting skill adjustment falls within feedback thresholds linked to that rule; qualifying rule-threshold pairs enter a candidate list, and \"the rule-threshold wi..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: walker-2014
    resource: "https://doi.org/10.1007/s40593-013-0001-9"
    title: "Walker, E., Rummel, N., & Koedinger, K. R. (2014). Adaptive Intelligent Support to Improve Peer Tutoring in Algebra. Int J Artif Intell Educ 24, 33–61. https://doi.org/10.1007/s40593-013-0001-9"
    author: "Walker, E., Rummel, N., & Koedinger, K. R"
---

# Select adaptive prompts through rule-linked feedback thresholds and priorities

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
When a production rule fires, APTA checks whether the resulting skill adjustment falls within feedback thresholds linked to that rule; qualifying rule-threshold pairs enter a candidate list, and "the rule-threshold with the highest priority was chosen to be the target rule for a reflective prompt," with ties broken randomly and a random message chosen from the target's message set. Lower skill assessments trigger more explicit, urgent messages; high proficiency suppresses positive feedback. Multiple message variants ensure students rarely receive the same prompt twice.

## Design Implications

### Context
#### Requirements
- Priorities and thresholds assigned from a theoretical model of rule importance, piloting, and prior-study data
- Multiple prompt variants per rule-threshold combination
#### Constraints
- Thresholds and priorities were hand-tuned for this domain; the article reports tuning so tutors received one prompt per three tutor actions

### Target Learners
- High school peer tutors receiving adaptive help-giving prompts

### Target Learning Goals
- Improving quality of help given to a tutee

## Claims

- [APTA's machine classifiers reached training-data accuracy of .81 for help type and .66 for conceptual content under 10-fold cross validation](../claims/apta-classifier-accuracy-help-type-conceptual.md) [+W]
- [A prior-study corpus of 84 peer tutoring sessions was coded for help type and conceptual content with kappa of 0.83 and 0.72](../claims/apta-peer-tutoring-dialogue-corpus-coding.md) [+W]

## Related Strategies

- [Give collaborators the benefit of the doubt by inflating guess and slip parameters in collaborative knowledge tracing](inflated-guess-slip-collaborative-kt.md)
- [Adaptive Learning](adaptive-learning.md)

## Examples
-

## Key Sources
- Walker, E., Rummel, N., & Koedinger, K. R. (2014). Adaptive Intelligent Support to Improve Peer Tutoring in Algebra. Int J Artif Intell Educ 24, 33–61. https://doi.org/10.1007/s40593-013-0001-9
