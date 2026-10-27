---
type: strategy
id: inflated-guess-slip-collaborative-kt
title: Give collaborators the benefit of the doubt by inflating guess and slip parameters in collaborative knowledge tracing
description: "To handle uncertainty in assessing collaboration, APTA initializes p(Lo) to 0.9 so that \"The system assumes that students know how to collaborate effectively, unless they repeatedly provide evidence that they do not,\"..."
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

# Give collaborators the benefit of the doubt by inflating guess and slip parameters in collaborative knowledge tracing

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
To handle uncertainty in assessing collaboration, APTA initializes p(Lo) to 0.9 so that "The system assumes that students know how to collaborate effectively, unless they repeatedly provide evidence that they do not," and inflates p(G) and p(S) following Beck and Sison, redefining them as broader false-positive and false-negative probabilities that include system error. Valence matters: somewhat effective and somewhat ineffective rules use higher p(G) and p(S), so skill estimates move less on ambiguous evidence. This reserves prompts for persistent patterns rather than single actions.

## Design Implications

### Context
#### Requirements
- A rule set whose rules carry valence labels so parameter values can vary by valence
- Piloting and prior data to set the inflated parameter values
#### Constraints
- The article notes this is a first pass; future work is to modify the core algorithm, validate against human-coded skill assessments, and make it more fine-grained

### Target Learners
- Students in collaborative learning environments being assessed by an automated system

### Target Learning Goals
- Accurate enough skill assessment to trigger useful collaborative support despite noisy dialogue assessment

### Affordances
- [Four Valence Production Rule Model Collaboration](../theories/bayesian-knowledge-tracing-two-state-model.md)

## Related Strategies

- [Initialize BKT parameters from simulated student data when no human data is available](initialize-bkt-parameters-from-simulated-data.md)
- [Use posterior credible intervals on condition-specific BKT parameter contrasts to compare experimental conditions](posterior-contrasts-condition-specific-bkt-parameters.md)
- [Select adaptive prompts through rule-linked feedback thresholds and priorities](threshold-priority-prompt-selection.md)

## Examples
-

## Key Sources
- Walker, E., Rummel, N., & Koedinger, K. R. (2014). Adaptive Intelligent Support to Improve Peer Tutoring in Algebra. Int J Artif Intell Educ 24, 33–61. https://doi.org/10.1007/s40593-013-0001-9
