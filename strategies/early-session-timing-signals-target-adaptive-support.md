---
type: strategy
id: early-session-timing-signals-target-adaptive-support
title: Use early-session timing signals, interpreted relative to proficiency, to identify students needing adaptive support
description: The article recommends that timing-based signals be used to identify early risk and guide context-sensitive interventions rather than as global indicators of effort quality.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: conrad-borchers-lijin-zhang-kexin
    resource: "https://doi.org/10.1145/3774398.3811624"
    title: "Conrad Borchers, Lijin Zhang, Kexin Yang, Tomohiro Nagashima, and Benjamin W. Domingue. 2026. Understanding Student Effort Using Response-Time Propensities During Problem Solving. Proceedings of the Thirteenth ACM Conference on Learning @ Scale (L@S '26). https://doi.org/10.1145/3774398.3811624"
---

# Use early-session timing signals, interpreted relative to proficiency, to identify students needing adaptive support

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends that timing-based signals be used to identify early risk and guide context-sensitive interventions rather than as global indicators of effort quality. Because the RT–learning relationship is most structured in the earliest session slice, the authors suggest early-session response-time patterns could trigger adaptive supports, noting that "timing-based signals are best used to identify early risk and guide context-sensitive interventions". Heuristics equating fast responding with efficiency or slow responding with disengagement risk misclassifying higher-proficiency students whose slower pacing may reflect constructive processing.

## Design Implications

### Context
#### Requirements
- Response-time propensities estimated with difficulty adjustment (student and knowledge-component random effects)
- Interpretation conditional on learner proficiency and position within the session
#### Constraints
- The article states the analyses are correlational and causal interpretations are not warranted; experimental or quasi-experimental tests of timing-triggered supports are a next step
- Extended latencies among lower-proficiency students early in practice may signal emerging difficulties with task initiation or persistence

### Target Learners
- middle- and high-school mathematics students in classroom tutoring deployments

### Target Learning Goals
- detecting emerging disengagement and low persistence; targeting adaptive support when effort is most diagnostic

### Affordances
- [Response Time Propensities Construct](../research-methods/response-time-effort-rte.md)

## Related Strategies

- [Use an early warning system based on linked school and human services data to target resources and lessen risks before they become more serious](early-warning-system-target-resources-near-term-risks.md)
- [Use postsecondary readiness indicators in an early warning system and combine cultural responsiveness with tiered interventions to address disparities](early-warning-system-with-tiered-culturally-responsive-supports.md)
- [Use early cheating-risk predictions only for low-stakes support with human review, never for disciplinary decisions](support-oriented-use-of-cheating-risk-predictions.md)
- [Use LCF risk clusters to target Supplemental Instruction recruitment and resource allocation](lcf-clusters-guide-si-resource-allocation.md)
- [Use early-run purchase predictions to trigger interventions guiding learners towards paying behaviour](early-purchase-prediction-interventions.md)

## Examples
-

## Key Sources
- Conrad Borchers, Lijin Zhang, Kexin Yang, Tomohiro Nagashima, and Benjamin W. Domingue. 2026. Understanding Student Effort Using Response-Time Propensities During Problem Solving. Proceedings of the Thirteenth ACM Conference on Learning @ Scale (L@S '26). https://doi.org/10.1145/3774398.3811624
