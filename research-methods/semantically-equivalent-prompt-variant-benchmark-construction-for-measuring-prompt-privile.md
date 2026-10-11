---
type: research-method
id: semantically-equivalent-prompt-variant-benchmark-construction-for-measuring-prompt-privile
title: Semantically equivalent prompt-variant benchmark construction for measuring prompt privilege
description: "A benchmark construction methodology that instantiates prompt privilege on the MedQA benchmark: for each original MedQA question, four additional semantically equivalent prompt variants are generated representing distinct user cohorts — Low Literacy, Everyday User, Educated User, and Prompt Engineer"
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
---

# Semantically equivalent prompt-variant benchmark construction for measuring prompt privilege

> **Research Method** · [All research methods](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A benchmark construction methodology that instantiates prompt privilege on the MedQA benchmark: for each original MedQA question, four additional semantically equivalent prompt variants are generated representing distinct user cohorts — Low Literacy, Everyday User, Educated User, and Prompt Engineer. Variants are produced with GPT-5.5 under rewriting instructions that preserve all clinically relevant information, answer choices, and the original ground-truth label, so observed performance differences can be attributed to prompt formulation rather than task difficulty or information content.

## Accounts
<!-- How each source describes or uses the method -->
- **MedQA semantically equivalent user-cohort benchmark for measuring prompt privilege**: A benchmark construction methodology that instantiates prompt privilege on the MedQA benchmark: for each original MedQA question, four additional semantically equivalent prompt variants are generated representing distinct user cohorts — Low Literacy, Everyday User, Educated User, and Prompt Engineer. Variants are produced with GPT-5.5 under rewriting instructions that preserve all clinically relevant information, answer choices, and the original ground-truth label, so observed performance differences can be attributed to prompt formulation rather than task difficulty or information content. (Lier Jin et al. (2026))

### Claims
- [LLM accuracy increases monotonically with prompt sophistication across semantically equivalent medical questions, with Low Literacy users scoring significantly below Prompt Engineer users](../claims/prompt-privilege-monotonic-accuracy-gap-medqa.md) [+M]

## Related Research Methods
-

## Key Sources
- Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942
