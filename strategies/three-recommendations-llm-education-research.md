---
type: strategy
id: three-recommendations-llm-education-research
title: "Three future research directions: education-focused benchmarks, a taxonomy of educational LLM harms, and multi-turn human feedback"
description: The review concludes with three recommendations for future research on LLMs in education.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: lee-2023
    resource: "https://wileyonlinelibrary.com/journal/"
    title: "Lee, J., Hicke, Y., Yu, R., Brooks, C., & Kizilcec, R. F. (2023). The Life Cycle of Large Language Models: A Review of Biases in Education. https://wileyonlinelibrary.com/journal/"
    author: "Lee, J., Hicke, Y., Yu, R., Brooks, C., & Kizilcec, R. F"
---

# Three future research directions: education-focused benchmarks, a taxonomy of educational LLM harms, and multi-turn human feedback

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 3 claims rest on one study

## Description
The review concludes with three recommendations for future research on LLMs in education. First, "there is a need for education-focused benchmark datasets that better represent a broader range of sociodemographic groups across the world" and for high-quality education datasets for pre-training and fine-tuning. Second, a specific taxonomy of harms for LLMs in educational contexts that highlights the perspectives of educators, students, and their families, since current taxonomies are domain-agnostic and developer-centered. Third, using high-quality human feedback from multi-turn scenarios to improve alignment of LLMs with educational objectives, for specialized tasks such as math tutoring.

## Design Implications

### Context
#### Requirements
- Collaboration between education technology developers, researchers, and communities represented in benchmark data
#### Constraints
- The article notes most current evaluation methods examine only a single isolated model output (single-turn) rather than an entire multi-turn conversation

### Target Learners
- students and teachers using LLM-based educational tools
- researchers
- policymakers

### Target Learning Goals
- evaluating and mitigating bias in educational LLM applications
- aligning LLMs with educational objectives

## Claims

- [No evaluated LLM tutor is reliably safe: every model exceeds 60% harm rate on at least five risk categories in single-turn and six in multi-turn evaluation](../claims/no-llm-tutor-reliably-safe-60-percent-harm.md) [+W]
- [Harm profiles are subject-dependent: metacognitive harm crosses 90% in all three subjects in multi-turn, peaking at 97.44% for Qwen2.5-32B in Mathematics](../claims/tutor-harm-subject-dependent-mitigations.md) [+W]
- [Current LLMs are more vulnerable to education-specific risks such as academic misconduct and excessive cognitive load than to conventional safety risks in K-12 educational interactions](../claims/eduzone-education-specific-risk-vulnerability.md) [+W]

## Related Strategies

- [Extend educational LLM benchmarks with broader item formats, human-in-the-loop item curation, and multi-turn evidence-based feedback measures](extend-educational-llm-benchmarks-human-in-loop-multiturn.md)
- [Establish standardized misconception benchmarks using isomorphic items, paraphrases, and multi-turn curricula](standardized-misconception-benchmarks-ess.md)
- [Extend educational LLM benchmarking toward multilingual contexts, real classroom interaction data, and targeted training for identified capability gaps](future-educational-llm-benchmark-extensions.md)
- [Pair a contamination-resistant static benchmark core with a learner-in-the-loop layer for next-generation education evaluation](learner-in-the-loop-next-benchmark.md)

## Examples
-

## Key Sources
- Lee, J., Hicke, Y., Yu, R., Brooks, C., & Kizilcec, R. F. (2023). The Life Cycle of Large Language Models: A Review of Biases in Education. https://wileyonlinelibrary.com/journal/
