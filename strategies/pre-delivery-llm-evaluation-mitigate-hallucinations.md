---
type: strategy
id: pre-delivery-llm-evaluation-mitigate-hallucinations
title: Incorporate pre-delivery LLM-based evaluation approaches into GenAI-powered personalised SRL scaffolding systems to mitigate hallucinations
description: The article recommends incorporating reliability evaluation and quality evaluation approaches into GenAI-powered personalised SRL scaffolding systems before scaffolds are presented to students.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-29
sources:
  - id: qian-2025
    resource: "https://arxiv.org/abs/2508.05929"
    title: "Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D. (2025). Towards Reliable Generative AI-Driven Scaffolding: Reducing Hallucinations and Enhancing Quality in Self-Regulated Learning Support. https://arxiv.org/abs/2508.05929"
    author: "Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D"
---

# Incorporate pre-delivery LLM-based evaluation approaches into GenAI-powered personalised SRL scaffolding systems to mitigate hallucinations

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article recommends incorporating reliability evaluation and quality evaluation approaches into GenAI-powered personalised SRL scaffolding systems before scaffolds are presented to students. This process aims to reduce educator workload while enhancing educational effectiveness by automatically screening out low-quality and hallucinated scaffolds, triggering LLM regeneration, and selecting high-quality scaffolds from multiple LLM-generated candidates.

## Design Implications

### Context
#### Requirements
- LLM-based reliability evaluation using a multi-agent structure
- LLM-as-a-Judge quality evaluation with position swapping to control for position bias
#### Constraints
- The LLM-as-a-Judge approach exhibits position bias, self-enhancement bias, sequential API call bias, and verbosity bias that must be accounted for

### Target Learners
- secondary school students

### Target Learning Goals
- self-regulated learning

## Claims

- [GPT-4-Turbo as an LLM Judge reliably selects better scaffolds and mitigates hallucination errors, while weaker LLM Judges do not](../claims/gpt4-turbo-judge-mitigates-hallucinations-weaker-judges-do-not.md) [+W]
- [LLM-generated scaffolds show low precision and high irrelevance rates in targeting intended SRL processes](../claims/llm-scaffolds-low-precision-high-irrelevance.md) [+W]
- [Multi-agent LLM parsers outperform single-agent structures and BERT baselines in evaluating scaffold reliability](../claims/multi-agent-llm-parsers-outperform-single-agent-and-bert.md) [+W]
- [Multi-agent LLM parsers achieve near-perfect agreement with human experts when evaluating the reliability of LLM-generated SRL scaffolds](../claims/multi-agent-llm-reliability-evaluation-near-perfect-agreement.md) [+W]

## Related Strategies

- [Incorporate learning context external to the chat into future scaffolding benchmarks, rubrics, and alignment datasets](incorporate-learning-context-into-scaffolding-benchmarks.md)
- [Integrate GPT models into LA-supported feedback systems with an iterative instructor-student validation loop to improve reliability](iterative-validation-loop-gpt-feedback-systems.md)

## Examples
-

## Key Sources
- Qian, K., Liu, S., Li, T., Raković, M., Li, X., Guan, R., Molenaar, I., Nawaz, S., Swiecki, Z., Yan, L., & Gašević, D. (2025). Towards Reliable Generative AI-Driven Scaffolding: Reducing Hallucinations and Enhancing Quality in Self-Regulated Learning Support. https://arxiv.org/abs/2508.05929
