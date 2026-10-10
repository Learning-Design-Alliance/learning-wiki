---
type: research-method
id: confidence-aware-selective-automated-scoring-framework
title: Confidence-aware selective automated scoring framework
description: The framework adapts a pretrained ViT with LoRA and derives a response-level confidence score from the stability of predictions under semantic-preserving test-time perturbations (crops, rotations).
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Confidence-aware selective automated scoring framework

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 associational), `q2` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The framework adapts a pretrained ViT with LoRA and derives a response-level confidence score from the stability of predictions under semantic-preserving test-time perturbations (crops, rotations). The article states that "automated scoring systems must decide not only what score to assign, but also whether that score can be trusted." A Top-η test-time selection step retains only the most decisive perturbed views before aggregating the final prediction and confidence. Varying the threshold τ controls the trade-off between automated coverage and scoring risk.

## Accounts
<!-- How each source describes or uses the method -->
- **Confidence-aware selective automated scoring framework**: The framework adapts a pretrained ViT with LoRA and derives a response-level confidence score from the stability of predictions under semantic-preserving test-time perturbations (crops, rotations). The article states that "automated scoring systems must decide not only what score to assign, but also whether that score can be trusted." A Top-η test-time selection step retains only the most decisive perturbed views before aggregating the final prediction and confidence. Varying the threshold τ controls the trade-off between automated coverage and scoring risk. (Fang et al. (2026))

### Claims
- [Confidence-aware selective test-time scoring achieves the best average agreement with expert rubric scoring across six NGSS drawing items](../claims/ca-selective-best-average-agreement-drawings.md) [+M]
- [The response-level confidence score correlates positively and significantly with scoring accuracy](../claims/confidence-score-correlates-scoring-accuracy.md) [+M]

## Related Research Methods
-

## Key Sources
- Fang, L., Zhang, Y., Park, J., Wang, Z., Ma, P., Zhai, X. (2026). Confidence-Aware Automated Assessment of Student-Drawn Scientific Models. https://arxiv.org/abs/2606.20264
