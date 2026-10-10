---
type: design
id: hcs-configurable-analytics-design
title: Highly Configurable System design for cross-domain learning analytics
description: "The pipeline applies Highly Configurable System (HCS) principles, \"enabling a single underlying codebase to be applied to different scenarios through flexible configuration\"."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: y-bai-2025
    resource: "https://arxiv.org/abs/2511.11877"
    title: "Y. Bai, P. Thajchayapong, A. Goel. (2025). Generalizing a Highly Configurable Analytics Pipeline to Replicate and Support Educational Research Across Multiple Domains. https://arxiv.org/abs/2511.11877"
    author: Y. Bai, P. Thajchayapong, A. Goel
---

# Highly Configurable System design for cross-domain learning analytics

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The pipeline applies Highly Configurable System (HCS) principles, "enabling a single underlying codebase to be applied to different scenarios through flexible configuration". Each statistical option's parameters — alternative hypothesis, dataset, independent and dependent variables, and result storage location — are programmed as variables whose values are read from keys in the JSON analysis configuration payload, so the same analysis-module code serves different domains. Santana et al 2025 found this yields a pipeline that is extensible and flexible while maintaining structural coherence, defined as the absence of invalid system configurations.

## Design Implications

### Context
#### Requirements
- Analysis configuration payloads must supply valid values for each configurable key (statistic name, dataset, variables, result file name).
#### Constraints
- Structural coherence depends on configurations being valid; the balance between flexibility and structural coherence was established in prior work by Santana et al 2025.

### Target Learners
- researchers and instructors analyzing educational AI assistant data

### Learning Goals
- reproducible cross-domain analysis of learner interaction data

### Claims
- [A4L Pipeline Extends Power Analysis Vera To Sami](../claims/a4l-pipeline-extends-power-analysis-vera-to-sami.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Y. Bai, P. Thajchayapong, A. Goel. (2025). Generalizing a Highly Configurable Analytics Pipeline to Replicate and Support Educational Research Across Multiple Domains. https://arxiv.org/abs/2511.11877
