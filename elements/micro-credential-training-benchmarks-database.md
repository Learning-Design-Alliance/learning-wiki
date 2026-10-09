---
type: element
id: micro-credential-training-benchmarks-database
title: Training Benchmarks Database of expert-scored submissions
description: For each micro-credential, the issuer creates a library of expert-scored submissions—a Benchmarks Database—comprising submission examples reflecting each score option.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: michelle-riconscente-2016
    resource: "https://digitalpromise.dspacedirect.org/items/ddd022c9-a271-4548-9667-38dbfe9bf9c6"
    title: "Michelle Riconscente, Designs for Learning, Inc. (2016). Designing a Process for Micro-credentials at Scale. Digital Promise. https://digitalpromise.dspacedirect.org/items/ddd022c9-a271-4548-9667-38dbfe9bf9c6"
    author: Michelle Riconscente, Designs for Learning, Inc
---

# Training Benchmarks Database of expert-scored submissions

> **Element** · [All elements](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
For each micro-credential, the issuer creates a library of expert-scored submissions—a Benchmarks Database—comprising submission examples reflecting each score option. At least two experts independently score each submission using the rubric, inter-rater reliability is calculated as a check, and conflicts are resolved in conference so one final score serves as ground truth for reviewer training and maintenance. The minimum database size is set by a formula based on scoring options and expected reviewer attempts.

## Design Implications

### Context
#### Requirements
- Expert scorers identified by the issuer whose scores serve as ground truth
- Sufficient examples in each score category
- Acceptable inter-rater reliability between experts before entries are finalized
#### Constraints
- As adoption increases, security of the training database will need to be addressed so the system is difficult to game

### Target Learners
- prospective micro-credential reviewers

### Target Learning Goals
- consistent application of scoring rubrics to micro-credential submissions

## Claims

- [Reviewer certification requires scoring benchmark samples on par with issuer-determined scores, with guessing odds made quantifiable](../claims/benchmark-scored-reviewer-certification.md) [+W]
- [For a pass/not-yet micro-credential, the chance of guessing five benchmark scores with 100% accuracy is approximately 0.001](../claims/guessing-probability-five-benchmark-samples.md) [+W]

## Related Elements
- 

## Examples

- [Maintain reviewer quality through explicit benchmark checks and implicit analytics on scoring drift](../strategies/explicit-implicit-reviewer-pool-maintenance.md)

## Key Sources
- Michelle Riconscente, Designs for Learning, Inc. (2016). Designing a Process for Micro-credentials at Scale. Digital Promise. https://digitalpromise.dspacedirect.org/items/ddd022c9-a271-4548-9667-38dbfe9bf9c6
