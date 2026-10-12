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
> **Evidence** · 3 claims (3 for) · 2 studies (2 causal), `q2` · 1 of 2 report an effect size · 3 claims rest on one study

## Description
A benchmark construction methodology that instantiates prompt privilege on the MedQA benchmark: for each original MedQA question, four additional semantically equivalent prompt variants are generated representing distinct user cohorts — Low Literacy, Everyday User, Educated User, and Prompt Engineer. Variants are produced with GPT-5.5 under rewriting instructions that preserve all clinically relevant information, answer choices, and the original ground-truth label, so observed performance differences can be attributed to prompt formulation rather than task difficulty or information content.

## Accounts
<!-- How each source describes or uses the method -->
- **MedQA semantically equivalent user-cohort benchmark for measuring prompt privilege**: A benchmark construction methodology that instantiates prompt privilege on the MedQA benchmark: for each original MedQA question, four additional semantically equivalent prompt variants are generated representing distinct user cohorts — Low Literacy, Everyday User, Educated User, and Prompt Engineer. Variants are produced with GPT-5.5 under rewriting instructions that preserve all clinically relevant information, answer choices, and the original ground-truth label, so observed performance differences can be attributed to prompt formulation rather than task difficulty or information content. (Lier Jin et al. (2026))
- **Benchmark designers should use controlled families of representational variants rather than single-form problem instances**: The article recommends that math benchmarks stop treating representationally equivalent formulations as interchangeable. Because performance varies substantially across representations of the same mathematical structure even under deterministic decoding, high benchmark scores may reflect "sensitivity to favored surface forms rather than stable representation-invariant ability". Controlled families of representational variants make it possible to distinguish robustness from overfitting to presentation style, and the article extends this to any domain admitting multiple surface realizations of the same structure. (Sagnik Nath et al. (2026))

### Claims
- [LLM accuracy increases monotonically with prompt sophistication across semantically equivalent medical questions, with Low Literacy users scoring significantly below Prompt Engineer users](../claims/prompt-privilege-monotonic-accuracy-gap-medqa.md) [+M]
- [LLM accuracy varies across mathematically equivalent problem representations even under deterministic decoding, in both interaction conditions](../claims/llm-representational-sensitivity-equivalent-math-forms.md) [+M]
- [Baseline versus code-augmented performance differs significantly for story and symbolic representations but not word-equations, with small effect sizes](../claims/interaction-condition-chi-square-representation-differences.md) [+M]

## Related Research Methods
-

## Key Sources
- Lier Jin, Lan Hu, Binqi Shen, Hanyu Cai, and Yuting Xin. (2026). Same Question, Different Answer? Measuring and Mitigating Prompt Privilege for Equitable AI Access. https://arxiv.org/abs/2608.08942
- Sagnik Nath, Edith Aurora Graf, Liang Zhang and Diego Zapata-Rivera. (2026). Representation Robustness under Executable Reasoning Constraints in Large Language Models for Mathematical Problem Solving. https://github.com/sagniknath91/HCI-2026-dataset/blob/main/datasheet.csv
