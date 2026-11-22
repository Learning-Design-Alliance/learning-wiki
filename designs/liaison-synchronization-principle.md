---
type: design
id: liaison-synchronization-principle
title: Synchronize translated documentation through a dedicated liaison supported by AI-assisted translation and merge-triggered updates
description: "The article recommends keeping translations synchronized by assigning a dedicated liaison whose focus is \"entirely on translating, validating, and applying upstream modifications\" so the Chinese documentation stays ac..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-22
sources:
  - id: morris-2026
    resource: "https://arxiv.org/abs/2609.35830"
    title: "Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X. (2026). Translating LHCb's Documentation: First experiences and ensuring maintenance. https://arxiv.org/abs/2609.35830"
    author: Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X
---

# Synchronize translated documentation through a dedicated liaison supported by AI-assisted translation and merge-triggered updates

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article recommends keeping translations synchronized by assigning a dedicated liaison whose focus is "entirely on translating, validating, and applying upstream modifications" so the Chinese documentation stays accurate and up to date with the English. Liaisons are notified when merge requests are submitted and translate revisions before the code or content is merged, using a two-stage process: a fine-tuned LLM generates the initial translation, then human verification refines the output. The authors state this guarantees rapid deployment and accuracy while ensuring a human has checked all pages before they go live.

## Design Implications

### Context
#### Requirements
- a dedicated liaison role with responsibility for one language community
- reviewers notifying liaisons promptly at merge-request submission
#### Constraints
- the approach was designed for a two-language pairing with the liaison attached to a specific project work package; extensibility to other languages is anticipated but not yet exercised

### Target Learners
- users of translated onboarding documentation, including LHCb collaborators in China

### Learning Goals
- maintaining accurate, up-to-date multilingual training documentation

### Claims
- [Hybrid Llm Human Translation Strategy](../strategies/hybrid-llm-human-translation-strategy.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Morris, A., Wang, Z., Yuan, X., Fu, Y., Hallett, G., He, J., Liu, K., Zhao, J., and Zhou, X. (2026). Translating LHCb's Documentation: First experiences and ensuring maintenance. https://arxiv.org/abs/2609.35830
