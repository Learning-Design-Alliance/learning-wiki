---
type: research-method
id: two-stage-simulate-then-calibrate-approach-to-difficulty-estimation
title: Two-stage simulate-then-calibrate approach to difficulty estimation
description: "The article proposes modeling difficulty the way it emerges in practice: a neural network first predicts each student's probability of answering each question correctly, producing a full matrix of synthetic responses, and a 1PL IRT model is then applied to that matrix to derive difficulty parameters"
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
---

# Two-stage simulate-then-calibrate approach to difficulty estimation

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article proposes modeling difficulty the way it emerges in practice: a neural network first predicts each student's probability of answering each question correctly, producing a full matrix of synthetic responses, and a 1PL IRT model is then applied to that matrix to derive difficulty parameters. The article notes that few studies have explored "first simulating student responses to questions and then deriving difficulty parameters from these simulated response patterns", and argues this yields interpretable models capturing both question characteristics and student abilities, plus byproducts such as discrimination parameters.

## Accounts
<!-- How each source describes or uses the method -->
- **Two-stage simulate-then-calibrate approach to difficulty estimation**: The article proposes modeling difficulty the way it emerges in practice: a neural network first predicts each student's probability of answering each question correctly, producing a full matrix of synthetic responses, and a 1PL IRT model is then applied to that matrix to derive difficulty parameters. The article notes that few studies have explored "first simulating student responses to questions and then deriving difficulty parameters from these simulated response patterns", and argues this yields interpretable models capturing both question characteristics and student abilities, plus byproducts such as discrimination parameters. (Matías Hoyl (2026))

### Claims
- [IRT difficulty parameters can be estimated without student testing via simulated responses, reaching a Pearson correlation of 0.7791 with benchmark difficulty on unseen questions](../claims/synthetic-responses-irt-difficulty-estimation.md) [+M]
- [Simulated-response difficulty estimates match the accuracy of a traditional 1PL analysis using approximately 5,818 real student answers (about 22.87% of available data)](../claims/rmse-efficiency-5818-real-answers.md) [+M]

## Related Research Methods
-

## Key Sources
- Matías Hoyl. (2026). Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation. arXiv. https://arxiv.org/abs/2602.00034
