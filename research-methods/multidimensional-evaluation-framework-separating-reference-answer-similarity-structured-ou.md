---
type: research-method
id: multidimensional-evaluation-framework-separating-reference-answer-similarity-structured-ou
title: Multidimensional evaluation framework separating reference-answer similarity, structured-output stability, and domain-specific correctness
description: The article proposes an evaluation framework for educational question-answering models that combines automatic text metrics with structured-output features and bootstrap confidence intervals.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Multidimensional evaluation framework separating reference-answer similarity, structured-output stability, and domain-specific correctness

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes an evaluation framework for educational question-answering models that combines automatic text metrics with structured-output features and bootstrap confidence intervals. ROUGE-1/2/L measure lexical overlap, BERTScore-F1 measures semantic proximity, and has_solution/has_method/has_teaching_points coverage rates measure conformity to the pedagogical template. The framework's central boundary condition is that "ROUGE and BERTScore primarily capture lexical and semantic proximity, while the structured-output metrics measure template stability" — none can certify formula accuracy, derivational rigor, or instructional usefulness, which require expert assessment or task-specific rubrics.

## Accounts
<!-- How each source describes or uses the method -->
- **Multidimensional evaluation framework separating reference-answer similarity, structured-output stability, and domain-specific correctness**: The article proposes an evaluation framework for educational question-answering models that combines automatic text metrics with structured-output features and bootstrap confidence intervals. ROUGE-1/2/L measure lexical overlap, BERTScore-F1 measures semantic proximity, and has_solution/has_method/has_teaching_points coverage rates measure conformity to the pedagogical template. The framework's central boundary condition is that "ROUGE and BERTScore primarily capture lexical and semantic proximity, while the structured-output metrics measure template stability" — none can certify formula accuracy, derivational rigor, or instructional usefulness, which require expert assessment or task-specific rubrics. (Shaowen Lu et al. (2026))

### Claims
- [LoRA fine-tuning on control systems course data increases lexical and semantic similarity between model responses and course reference answers at both 3B and 7B model sizes](../claims/lora-improves-reference-answer-similarity-control-systems.md) [+M]
- [LoRA fine-tuning makes the Solution-Method-Teaching Points instructional format more stable, with Solution and Method coverage reaching 1.00 at r=8 and r=16 for the 3B model](../claims/lora-improves-structured-instructional-output-stability.md) [+M]

## Related Research Methods
-

## Key Sources
- Shaowen Lu, Chengxu Liu, Ping Zhou and Tao Yang. (2026). LoRA Fine-Tuned Models for Control Systems Course Q&A: A Multidimensional Evaluation of Model Scale and Rank Effects. https://arxiv.org/abs/2609.13918
