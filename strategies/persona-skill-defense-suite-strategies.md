---
type: strategy
id: persona-skill-defense-suite-strategies
title: "Defense suite for persona skills: online sanitization, post-hoc adversarial obfuscation, and semantic backdoor watermarking"
description: "AntiSkillBench designs and evaluates four defense configurations intervening at different stages of the persona-skill lifecycle, covering \"online versus post-hoc intervention and active risk suppression versus passive..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: yongli-xiang-2026
    resource: "https://arxiv.org/abs/2608.03700"
    title: "Yongli Xiang, Zhifang Zhang, Bojun Yang, Ziming Hong, Lei Feng, Miao Xu, Tongliang Liu. (2026). When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills. arXiv. https://arxiv.org/abs/2608.03700"
    author: Yongli Xiang, Zhifang Zhang, Bojun Yang, Ziming Hong, Lei Feng, Miao Xu, Tongliang Liu
---

# Defense suite for persona skills: online sanitization, post-hoc adversarial obfuscation, and semantic backdoor watermarking

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
AntiSkillBench designs and evaluates four defense configurations intervening at different stages of the persona-skill lifecycle, covering "online versus post-hoc intervention and active risk suppression versus passive backdoor protection". Privacy Sanitization rewrites user queries online to remove private cues while preserving task intent; Adversarial Obfuscation appends conflicting private attributes post-hoc to mislead distillation; Semantic-level Backdoor Injection implants semantic watermarks in both settings so unauthorized skill reuse can later be traced.

## Design Implications

### Context
#### Requirements
- The defender can only intervene on the trace side before distillation, transforming or augmenting the traces without modifying the distillation function, the agent, or the deployed skill-use interface
#### Constraints
- Active defenses primarily suppress surface-level communication cues while leaving deeper background and personality information exposed; backdoor-based protection degrades under persona-centric abstraction

### Target Learners
- LLM-based agent systems and their developers

### Target Learning Goals
- Protecting distilled persona skills against privacy leakage, impersonation, and unauthorized reuse

## Related Strategies
- 

## Examples
-

## Key Sources
- Yongli Xiang, Zhifang Zhang, Bojun Yang, Ziming Hong, Lei Feng, Miao Xu, Tongliang Liu. (2026). When Agents Learn to Be You: Benchmarking Privacy Leakage, Impersonation Risk, and Defenses in Persona Skills. arXiv. https://arxiv.org/abs/2608.03700
