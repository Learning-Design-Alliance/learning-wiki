---
type: theory
title: "HelpNeed classification: a five-category step-level taxonomy of productivity based on step efficiency and duration"
description: "The HelpNeed classification labels each problem-solving step using two data-driven dimensions: step duration (Quick vs Long, thresholded at the 75th percentile of historical per-problem step time) and step efficiency..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: maniktala-2020
    resource: "https://jedm.educationaldatamining.org/index.php/JEDM/article/view/450"
    title: "Maniktala, M., Cody, C., Isvik, A., Lytle, N., Chi, M., & Barnes, T. (2020). Extending the Hint Factory for the Assistance Dilemma: A Novel, Data-driven Help-Need Predictor for Proactive Problem-solving Help. Journal of Educational Data Mining, Volume 12, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/450"
    author: "Maniktala, M., Cody, C., Isvik, A., Lytle, N., Chi, M., & Barnes, T"
---

# HelpNeed classification: a five-category step-level taxonomy of productivity based on step efficiency and duration

> **Theory** · [All theories](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 6 claims rest on one study

## Description
The HelpNeed classification labels each problem-solving step using two data-driven dimensions: step duration (Quick vs Long, thresholded at the 75th percentile of historical per-problem step time) and step efficiency (derived from Hint Factory state quality and progress). It defines three no-help categories — Expert-like ("A quick efficient step; demonstrating mastery"), Strategic, and Opportunistic (a single quick but inefficient step) — and two help-needed categories, Far Off (consecutive quick inefficient steps) and Futile (a long inefficient step). The taxonomy is designed to identify steps that reflect suboptimal strategies in well-structured open-ended domains.

## Design Implications

### Context
#### Requirements
- Historical per-problem student step-time data to compute the 75th-percentile duration thresholds
- Prior student solution data to build Hint Factory state quality values for the efficiency metric
#### Constraints
- Duration thresholds are per-problem; a Long step in a difficult problem exceeded 5.48 min versus 2.95 min in an easy problem
- The Far Off definition could be adjusted for other domains using a combination of duration and efficiency

### Target Learners
- undergraduate discrete math students

### Target Learning Objectives
- efficient multi-step propositional logic proof construction

### Claims

- [Helpneed Proportion Negatively Correlated Posttest Optimality](../claims/helpneed-proportion-negatively-correlated-posttest-optimality.md) [+M]
- [Adaptive students show fewer Opportunistic and Far Off training steps than Control, with no difference in Futile steps](../claims/adaptive-fewer-opportunistic-far-off-steps.md) [+M]
- [Adaptive students request significantly fewer on-demand hints and spend longer on a step before requesting help than Control students](../claims/adaptive-hint-seeking-behavior-differences.md) [+M]
- [Students receiving Adaptive proactive hints based on HelpNeed predictions achieve significantly higher posttest optimality than Control students](../claims/adaptive-proactive-hints-higher-posttest-optimality.md) [+M]
- [Adaptive-condition students complete the posttest in significantly less time than Control students](../claims/adaptive-proactive-hints-less-posttest-time.md) [+M]
- [A generalized cross-problem HelpNeed predictor performs as well as problem-specific models and better when less historical data is available](../claims/generalized-cross-problem-helpneed-predictor.md) [+M]

## Related Theories
- 

## Examples
-

## Key Sources
- Maniktala, M., Cody, C., Isvik, A., Lytle, N., Chi, M., & Barnes, T. (2020). Extending the Hint Factory for the Assistance Dilemma: A Novel, Data-driven Help-Need Predictor for Proactive Problem-solving Help. Journal of Educational Data Mining, Volume 12, No 4. https://jedm.educationaldatamining.org/index.php/JEDM/article/view/450
