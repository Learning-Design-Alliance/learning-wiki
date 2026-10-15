---
type: strategy
id: incremental-llm-simulation-development
title: Develop complex simulations incrementally, testing each stage before adding the next feature
description: "For complex simulations, the article recommends building in stages rather than using one comprehensive prompt: \"we found it more effective to develop the simulation incrementally, adding features in stages ensuring th..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-12
sources:
  - id: yossi-ben-zion-2024
    resource: "https://arxiv.org/abs/2412.07482"
    title: "Yossi Ben-Zion, Roi Einhorn Zarzecki, Joshua Glazer, Noah D. Finkelstein. (2024). Leveraging AI for Rapid Generation of Physics Simulations in Education: Building Your Own Virtual Lab. https://arxiv.org/abs/2412.07482"
    author: Yossi Ben-Zion, Roi Einhorn Zarzecki, Joshua Glazer, Noah D. Finkelstein
---

# Develop complex simulations incrementally, testing each stage before adding the next feature

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For complex simulations, the article recommends building in stages rather than using one comprehensive prompt: "we found it more effective to develop the simulation incrementally, adding features in stages ensuring that each stage worked correctly before introducing the next element". Each stage was thoroughly tested before proceeding, which the authors say ensured robust functionality and serves as a template for other 3D simulations.

## Design Implications

### Context
#### Requirements
- Willingness to run multiple prompt rounds and test each stage's functionality before adding the next element
#### Constraints
- The article states this approach was applied because a single prompt for the 3D random walk may lead to inconsistent results due to task complexity

### Target Learners
- educators and students generating their own simulations

### Target Learning Goals
- producing robust AI-generated simulations of complex systems

## Related Strategies

- [Use AI-generated simulations where ready-made tools are unavailable, for edge cases, or as comparative learning tools](ai-simulations-as-complement-to-established-tools.md)
- [Adopt AI incrementally in waves from simple to complex tasks, on free-tier tools, with mandatory multi-step human review before any document is issued](incremental-free-tier-ai-adoption-with-triple-review.md)

## Examples
-

## Key Sources
- Yossi Ben-Zion, Roi Einhorn Zarzecki, Joshua Glazer, Noah D. Finkelstein. (2024). Leveraging AI for Rapid Generation of Physics Simulations in Education: Building Your Own Virtual Lab. https://arxiv.org/abs/2412.07482
