---
type: strategy
id: threat-profile-keyed-generation-protocol
title: "Select the variant-generation prompting protocol by deployment threat profile: zero-shot or structured CoT for construct fidelity, few-shot or dimension-preserving generation for surface separation"
description: "The article recommends that institutions deploying AIAA-style variant generation choose a prompting protocol keyed to the application's threshold profile."
status: review
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
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

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

## Claims

- [Few-shot anchoring trades surface diversity against construct equivalence and readability parity, with each direction significant at p = 0.004 relative to zero-shot](../claims/few-shot-anchoring-three-way-tradeoff.md) [+W]
- [Under illustrative property thresholds, no prompting strategy passes all measured AIAA properties in every model-blueprint cell; few-shot anchoring passes only 2 of 9 cells](../claims/threshold-gating-no-strategy-fully-passes.md) [+W]

## Related Strategies

- [Translate deductive coding rubrics into structured zero-shot prompts to compare LLM coding against human coding](zero-shot-prompt-codebook-translation-strategy.md)

## Examples
-

## Key Sources
- Ernesto Lee. (2026). VARIA: Benchmarking Frontier LLMs on Construct-Equivalent Assessment Variant Generation. https://doi.org/10.35542/osf.io/u6xef_v2
