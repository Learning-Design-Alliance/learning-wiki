---
type: strategy
id: guidelines-llm-qualitative-coding-pipelines
title: Four guidelines for designing LLM-assisted qualitative coding pipelines
description: The article distills its combined agreement and verification evidence into four guidelines for researchers designing large-scale coding pipelines.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: liu-2026
    resource: "https://arxiv.org/abs/2607.28890"
    title: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890"
    author: "Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M"
---

# Four guidelines for designing LLM-assisted qualitative coding pipelines

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article distills its combined agreement and verification evidence into four guidelines for researchers designing large-scale coding pipelines. These are: evaluate candidate models on the target instrument before deployment; set the division of labor at the code level using the two-dimensional assessment rather than blanket decisions; use confidence-based triage only after testing that high-confidence annotations are actually endorsed more often; and do not treat high human-human agreement as sufficient evidence that human coding is correct. The article states that "high human-human agreement should not be treated as sufficient evidence that human coding is correct", since coders can share a conservative interpretation that LLM coding exceeds.

## Design Implications

### Context
#### Requirements
- Investment in model evaluation on the researcher’s own instrument before deployment.
- A two-dimensional (agreement plus verification endorsement) assessment to support code-level allocation decisions.
- Calibrated model confidence, tested on the specific instrument, before confidence-based routing is used.
#### Constraints
- The guidelines emerge from one codebook and one dataset of educator messages; the article warns the specific code assignments may not generalize to other domains or coding approaches.
- Enhanced prompting strategies were left unexplored because all inference used temperature zero with no session memory.

### Target Learners
- Researchers designing large-scale deductive qualitative coding pipelines
- Teams deciding between human-only, LLM-assisted, and hybrid coding workflows

### Target Learning Goals
- Scaling deductive qualitative analysis without sacrificing coding quality
- Retaining human oversight where contextual inference is required

### Affordances
- Code Level Division Of Labor Framework

## Related Strategies

- [Instruction-guided LLM annotation with human-in-the-loop prompt refinement for large-scale interaction labeling](instruction-guided-llm-annotation-interaction-labels.md)

## Examples
-

## Key Sources
- Liu, A., Esbenshade, L., Xiao, M., Tian, V., Zhang, Z., He, K., & Sun, M. (2026). Agreement Is Not Quality: Blind Expert Verification of Human and LLM Qualitative Coding When Human Consensus Is Not Ground Truth. Preprint, no identifier printed in text. https://arxiv.org/abs/2607.28890
