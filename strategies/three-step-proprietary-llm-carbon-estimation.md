---
type: strategy
id: three-step-proprietary-llm-carbon-estimation
title: Three-step procedure for estimating computational cost and CO2 of proprietary LLMs with unknown parameters
description: "For proprietary models where CodeCarbon cannot be used and parameter counts are unknown, the article recommends: (1) sum context and output tokens, which most inference APIs readily report; (2) estimate active paramet..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: eimler-2026
    resource: "https://arxiv.org/abs/2606.11215"
    title: "Eimler, S.C., Erle, L., Flood, D., Haiman, A., Häckert, L., Helgert, A., McGinness, L., Yapici, B. (2026). The Environmental Cost of LLMs in AIED: Reporting and Practices. https://arxiv.org/abs/2606.11215"
    author: Eimler, S.C., Erle, L., Flood, D., Haiman, A., Häckert, L., Helgert, A., McGinness, L., Yapici, B
---

# Three-step procedure for estimating computational cost and CO2 of proprietary LLMs with unknown parameters

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
For proprietary models where CodeCarbon cannot be used and parameter counts are unknown, the article recommends: (1) sum context and output tokens, which most inference APIs readily report; (2) estimate active parameters by assuming frontier models are similar in size to open source models of similar performance, roughly 100 billion active parameters for state-of-the-art models and 30 billion for flash/fast models based on Qwen3's architecture; (3) apply FLOPs = 2Nn and convert to CO2 assuming an H100 GPU at about 2 T-FLOPs/Joule, a global mean PUE of 1.5, and approximately 384 grams of CO2 per KWh in the United States, giving about 6×10−5 grams of CO2 per T-FLOP.

## Design Implications

### Context
#### Requirements
- Access to token counts from the LLM API
- Willingness to accept an order-of-magnitude estimate
#### Constraints
- The procedure only gives an order of magnitude estimate of FLOPs and carbon intensity
- If the model size estimate is underestimated by a multiplicative factor, the reported FLOPs are underestimated by the same factor

### Target Learners
- AIED researchers using proprietary LLMs on external servers

### Target Learning Goals
- Consistent sustainability benchmarking of LLM-based AI systems

## Related Strategies
- 

## Examples
-

## Key Sources
- Eimler, S.C., Erle, L., Flood, D., Haiman, A., Häckert, L., Helgert, A., McGinness, L., Yapici, B. (2026). The Environmental Cost of LLMs in AIED: Reporting and Practices. https://arxiv.org/abs/2606.11215
