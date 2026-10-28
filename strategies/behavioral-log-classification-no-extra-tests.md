---
type: strategy
id: behavioral-log-classification-no-extra-tests
title: Classify adult readers by automatically collected behavioral data rather than requiring extra tests
description: The article proposes using behavioral data (accuracy and response time) collected automatically during ITS interaction to classify adult readers into performance profiles.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: fang-2021
    resource: "https://doi.org/10.1007/s40593-021-00266-y"
    title: "Fang, Y., Lippert, A., Cai, Z., Chen, S., Frijters, J. C., Greenberg, D., & Graesser, A. C. (2021). Patterns of Adults with Low Literacy Skills Interacting with an Intelligent Tutoring System. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00266-y"
    author: "Fang, Y., Lippert, A., Cai, Z., Chen, S., Frijters, J. C., Greenberg, D., & Graesser, A. C"
---

# Classify adult readers by automatically collected behavioral data rather than requiring extra tests

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 associational), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
The article proposes using behavioral data (accuracy and response time) collected automatically during ITS interaction to classify adult readers into performance profiles. Prior studies classified adults based on scores on reading measures such as vocabulary, word reading and spelling, which need to be collected through reading tests. In contrast, behavioral data can be collected automatically when adults interact with AutoTutor during their learning, providing a way to classify adult readers without requiring them to take extra tests.

## Design Implications

### Context
#### Requirements
- An ITS that logs per-question accuracy and response time
- Sufficient log observations to support clustering
#### Constraints
- Clustering was restricted to items all participants received (fixed-sequence questions and medium-difficulty texts) to ensure comparability

### Target Learners
- adults with low literacy skills in literacy programs

### Target Learning Goals
- identifying reader profiles to inform adaptive instruction

## Claims

- [Cluster membership moderated the relationship between theoretical comprehension level and both response time and accuracy in AutoTutor](../claims/cluster-by-level-interaction-autotutor.md) [+W]
- [Adults with low literacy using AutoTutor fall into four behavioral clusters: higher performers, conscientious readers, under-engaged readers, and struggling readers](../claims/four-behavioral-clusters-adult-literacy-autotutor.md) [+W]
- [Higher performers outperformed struggling readers on posttest comprehension after controlling for pretest, on both WJ-III and RAPID measures](../claims/higher-performers-beat-struggling-posttest.md) [+W]
- [Higher performers achieved the highest accuracy across all theoretical levels and the shortest response times on situation model questions](../claims/higher-performers-fast-accurate.md) [+W]
- [Higher performers' response time decreased with question number within situation model and rhetorical structure lessons](../claims/response-time-decreases-question-number.md) [+W]
- [Struggling readers were slow and inaccurate, with the lowest accuracy across all theoretical levels](../claims/struggling-readers-slow-inaccurate.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Fang, Y., Lippert, A., Cai, Z., Chen, S., Frijters, J. C., Greenberg, D., & Graesser, A. C. (2021). Patterns of Adults with Low Literacy Skills Interacting with an Intelligent Tutoring System. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-021-00266-y
