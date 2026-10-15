---
type: design
id: anchor-llm-inference-provenance-onchain-instructor-cosign
title: Anchor LLM inference provenance on-chain and require instructor co-signatures for high-stakes grading records
description: "To make AI-generated educational decisions auditable and attributable, the framework records not only the AI output but the full inference configuration on the consortium ledger: \"the model release and inference confi..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-15
sources:
  - id: fuan-xiao-2026
    resource: "https://doi.org/10.1186/s41239-026-00618-5"
    title: "Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li. (2026). Integrating LLM with consortium blockchain for personalized and verifiable online education in higher education. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00618-5"
    author: Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li
---

# Anchor LLM inference provenance on-chain and require instructor co-signatures for high-stakes grading records

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
To make AI-generated educational decisions auditable and attributable, the framework records not only the AI output but the full inference configuration on the consortium ledger: "the model release and inference configuration (model/checkpoint ID, prompt-template hash, decoding parameters, and random seed, etc.) as hashed records on a consortium blockchain". High-stakes records such as final grades and certificates carry both an AI service signature and an instructor co-signature, and any later override is appended as a linked, traceable transaction rather than overwriting history.

## Design Implications

### Context
#### Requirements
- The AI service must sign its outputs and the smart contract must enforce the hybrid AI-plus-instructor signing protocol for important records
#### Constraints
- Applies to key grading outcomes; low-risk tutoring interactions are not recorded on-chain

### Target Learners
- higher education students in online courses

### Learning Goals
- accountable and reproducible automated assessment

### Claims
- [Llm Grader Precision Recall Tradeoffs Single Metric Insufficient](../claims/llm-grader-precision-recall-tradeoffs-single-metric-insufficient.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Fuan Xiao, Jiahui Huang, Jia-Xin Huang, Huali Ren and Lang Li. (2026). Integrating LLM with consortium blockchain for personalized and verifiable online education in higher education. International Journal of Educational Technology in Higher Education. https://doi.org/10.1186/s41239-026-00618-5
