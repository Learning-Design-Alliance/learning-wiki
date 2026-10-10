---
type: strategy
id: onboard-new-ai-assistants-via-configuration-payloads
title: Onboard new educational AI assistants to shared analytics via configuration payloads, not new code
description: "The authors recommend that future educational AI assistants adopt the pipeline's existing statistical options by writing an analysis configuration payload rather than new analysis code."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: y-bai-2025
    resource: "https://arxiv.org/abs/2605.30303"
    title: "Y. Bai, P. Thajchayapong, A. Goel. (2025). Generalizing a Highly Configurable Analytics Pipeline to Replicate and Support Educational Research Across Multiple Domains. https://arxiv.org/abs/2605.30303"
    author: Y. Bai, P. Thajchayapong, A. Goel
---

# Onboard new educational AI assistants to shared analytics via configuration payloads, not new code

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The authors recommend that future educational AI assistants adopt the pipeline's existing statistical options by writing an analysis configuration payload rather than new analysis code. They state, "No code will need to be written for XYZ to get started with using the analytics capabilities of the pipeline", where XYZ is a placeholder for a not-yet-deployed assistant. Like the VERA-to-SAMI power calculation transfer, a new assistant can apply statistical tests originally used by other research domains to its own datasets.

## Design Implications

### Context
#### Requirements
- Classroom usage and context data for the new assistant must be available in the A4L data stores.
- A researcher must construct an analysis configuration payload with domain-specific key values.
#### Constraints
- Key values in the configuration are expected to change per domain; the authors expect, but have not yet demonstrated, that the codebase will need no modification for future assistants such as Ivy.

### Target Learners
- researchers deploying new educational AI assistants in online courses

### Target Learning Goals
- analyzing new AI assistant interaction data with existing statistical methods

### Affordances
- [Hcs Configurable Analytics Design](../designs/hcs-configurable-analytics-design.md)

## Related Strategies
- 

## Examples
-

## Key Sources
- Y. Bai, P. Thajchayapong, A. Goel. (2025). Generalizing a Highly Configurable Analytics Pipeline to Replicate and Support Educational Research Across Multiple Domains. https://arxiv.org/abs/2605.30303
