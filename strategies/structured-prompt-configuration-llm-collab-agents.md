---
type: strategy
id: structured-prompt-configuration-llm-collab-agents
title: Configure LLM collaboration support agents with structured prompts defining persona, scenario, response structure, and divided labor
description: "The article recommends customizing LLM agent behavior through structured prompt design principles adapted from Phoenix and Taylor (2024), \"which emphasize tailoring prompts to guide agents effectively\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: wu-2025
    resource: "http://bit.ly/4leDl0U"
    title: "Wu, Z., Shi, J., Murray, R. C., Rosé, C., & San Andres, M. (2025). LLM Bazaar: A Service Design for Supporting Collaborative Learning with an LLM-Powered Multi-Party Collaboration Infrastructure. CSCL 2025 Proceedings. http://bit.ly/4leDl0U"
    author: "Wu, Z., Shi, J., Murray, R. C., Rosé, C., & San Andres, M"
---

# Configure LLM collaboration support agents with structured prompts defining persona, scenario, response structure, and divided labor

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends customizing LLM agent behavior through structured prompt design principles adapted from Phoenix and Taylor (2024), "which emphasize tailoring prompts to guide agents effectively". Users define each agent's persona (name, occupation, age, personality), set a scenario, specify response structure such as length and level of detail, embed sample responses, and divide labor within the prompt into clear instructional steps. Prompt quality is then refined iteratively by observing agent responses in action.

## Design Implications

### Context
#### Requirements
- Iterative evaluation: users observe the agent's responses in action and refine prompts until quality aligns with expectations
#### Constraints
- Prompts are demonstrated in a cooking-domain scenario; the article illustrates rather than experimentally validates the prompt principles

### Target Learners
- instructors and researchers configuring LLM support agents
- college students in collaborative programming courses

### Target Learning Goals
- goal-driven dialogue aligned with instructional objectives
- encouraging teamwork among students

## Related Strategies

- [Use a simulated multiagent prompt combining role, instruction-based, chain, and few-shot prompting to generate OSCE stations with an LLM](simulated-multiagent-prompting-for-osce-generation.md)
- [Use an LLM moderator with structured persona-aware prompting to balance participation and manage disruptive behavior in group discussion](llm-moderator-equitable-participation-strategy.md)

## Examples
-

## Key Sources
- Wu, Z., Shi, J., Murray, R. C., Rosé, C., & San Andres, M. (2025). LLM Bazaar: A Service Design for Supporting Collaborative Learning with an LLM-Powered Multi-Party Collaboration Infrastructure. CSCL 2025 Proceedings. http://bit.ly/4leDl0U. [doi:10.48550/arxiv.2510.18877](https://doi.org/10.48550/arxiv.2510.18877)
