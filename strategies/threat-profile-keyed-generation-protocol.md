---
type: strategy
id: threat-profile-keyed-generation-protocol
title: "Select the variant-generation prompting protocol by deployment threat profile: zero-shot or structured CoT for construct fidelity, few-shot or dimension-preserving generation for surface separation"
description: "The article recommends that institutions deploying AIAA-style variant generation choose a prompting protocol keyed to the application's threshold profile."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
sources:
  - id: ernesto-lee-2026
    resource: "https://doi.org/10.35542/osf.io/u6xef_v2"
    title: "Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://doi.org/10.35542/osf.io/u6xef_v2"
    author: Ernesto Lee
---

# Select the variant-generation prompting protocol by deployment threat profile: zero-shot or structured CoT for construct fidelity, few-shot or dimension-preserving generation for surface separation

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends that institutions deploying AIAA-style variant generation choose a prompting protocol keyed to the application's threshold profile. Where "construct fidelity is paramount — high-stakes credentialling — zero-shot or structured chain-of-thought is the safest default", because these deliver the highest construct equivalence and tightest readability dispersion. Where the threat is lexical copy-paste in large-enrolment formative assessment, few-shot anchoring or dimension-preserving constrained generation buys surface separation at an equivalence cost that downstream rubric validation must absorb.

## Design Implications

### Context
#### Requirements
- Institution-specific threshold settings; per-cell validation of the chosen model-prompt pair; downstream rubric validation when accepting an equivalence cost.
#### Constraints
- At the illustrative default thresholds, few-shot anchoring passes all measured properties in only 2 of 9 cells, so an institution choosing it must either relax the Flesch threshold deliberately or filter generated sets cell by cell.

### Target Learners
- higher-education students in large-enrolment and high-stakes courses

### Target Learning Goals
- integrity-bearing per-student assessment variant generation without surveillance

## Related Strategies
- 

## Examples
-

## Key Sources
- Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://doi.org/10.35542/osf.io/u6xef_v2
