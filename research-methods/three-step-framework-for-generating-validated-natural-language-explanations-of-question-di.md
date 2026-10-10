---
type: research-method
id: three-step-framework-for-generating-validated-natural-language-explanations-of-question-di
title: Three-step framework for generating validated natural-language explanations of question difficulty
description: "The article introduces a framework that treats difficulty as \"a quantity to be explained\" rather than only estimated."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Three-step framework for generating validated natural-language explanations of question difficulty

> **Research Method** · [All research methods](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The article introduces a framework that treats difficulty as "a quantity to be explained" rather than only estimated. It first fits a 1PL IRT model to LLM response matrices to estimate each item's difficulty, then repeatedly samples "contrastive sets of difficult and easy items" and prompts an LLM to propose hypotheses explaining the gap, and finally refines, matches, and selects hypotheses via L1-regularized regression on held-out questions. The output is interpretable natural-language difficulty factors that can be used predictively and causally.

## Accounts
<!-- How each source describes or uses the method -->
- **A three-step framework for generating validated natural-language explanations of question difficulty**: The article introduces a framework that treats difficulty as "a quantity to be explained" rather than only estimated. It first fits a 1PL IRT model to LLM response matrices to estimate each item's difficulty, then repeatedly samples "contrastive sets of difficult and easy items" and prompts an LLM to propose hypotheses explaining the gap, and finally refines, matches, and selects hypotheses via L1-regularized regression on held-out questions. The output is interpretable natural-language difficulty factors that can be used predictively and causally. (Peng Cui et al. (2026))

### Claims
- [Generated hypotheses discriminate hard from easy questions, mostly with medium-to-large effects](../claims/hypotheses-discriminate-difficulty-effect-sizes.md) [+M]
- [Hypothesis-based predictors match or beat black-box difficulty regressors on unseen questions](../claims/hypothesis-predictor-matches-black-box-regressors.md) [+M]
- [Editing questions according to a hypothesis shifts measured difficulty in the expected direction](../claims/hypothesis-guided-editing-shifts-difficulty-causally.md) [+M]

## Related Research Methods
-

## Key Sources
- Peng Cui, Qiaoyuan Zheng, Rudolf Debelak, Mrinmaya Sachan. (2026). What Makes Something Hard(er)? Explaining Question Difficulty in Natural Language. Preprint. https://arxiv.org/abs/2610.01627
