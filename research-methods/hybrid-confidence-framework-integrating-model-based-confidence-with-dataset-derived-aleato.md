---
type: research-method
id: hybrid-confidence-framework-integrating-model-based-confidence-with-dataset-derived-aleato
title: Hybrid confidence framework integrating model-based confidence with dataset-derived aleatoric uncertainty via semantic heterogeneity
description: "The framework treats LLM grading unreliability as arising from two sources: epistemic uncertainty, estimated from model-based signals (verbalized, latent, and consistency-based confidence), and aleatoric uncertainty, estimated from the dataset."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Hybrid confidence framework integrating model-based confidence with dataset-derived aleatoric uncertainty via semantic heterogeneity

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The framework treats LLM grading unreliability as arising from two sources: epistemic uncertainty, estimated from model-based signals (verbalized, latent, and consistency-based confidence), and aleatoric uncertainty, estimated from the dataset. Aleatoric uncertainty is operationalized by embedding student responses with a sentence-transformer model, clustering them with Ward linkage, and computing normalized Shannon entropy of label distributions within each cluster as a heterogeneity proxy. The signals are fused by a Random Forest classifier with Platt scaling into a calibrated hybrid confidence score. The article states it proposes "a hybrid confidence framework that integrates model-based confidence signals with an explicit estimate of dataset-derived aleatoric uncertainty."

## Accounts
<!-- How each source describes or uses the method -->
- **Hybrid confidence framework integrating model-based confidence with dataset-derived aleatoric uncertainty via semantic heterogeneity**: The framework treats LLM grading unreliability as arising from two sources: epistemic uncertainty, estimated from model-based signals (verbalized, latent, and consistency-based confidence), and aleatoric uncertainty, estimated from the dataset. Aleatoric uncertainty is operationalized by embedding student responses with a sentence-transformer model, clustering them with Ward linkage, and computing normalized Shannon entropy of label distributions within each cluster as a heterogeneity proxy. The signals are fused by a Random Forest classifier with Platt scaling into a calibrated hybrid confidence score. The article states it proposes "a hybrid confidence framework that integrates model-based confidence signals with an explicit estimate of dataset-derived aleatoric uncertainty." (Longwei Cong et al. (2026))

### Claims
- [A hybrid confidence measure combining model-based signals with dataset-derived aleatoric uncertainty achieves the highest AUROC and strongest accuracy gains in selective grading of LLM-graded short answers](../claims/hybrid-confidence-highest-auroc-selective-asag.md) [+M]
- [The hybrid confidence measure with aleatoric uncertainty yields the best calibration (Brier 0.138, ECE 0.044, MCE 0.100) among compared methods](../claims/hybrid-aleatoric-best-calibration-asag.md) [+M]

## Related Research Methods
-

## Key Sources
- Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, and Ulf Kroehne. (2026). Confidence Estimation in Automatic Short Answer Grading with LLMs. https://arxiv.org/abs/2605.00200
