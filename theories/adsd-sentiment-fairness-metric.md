---
type: theory
title: Absolute distributional sentiment divergence (ADSD) as a distribution-level fairness metric for generated replies
description: ADSD is a proposed metric that quantifies sentiment bias by measuring the divergence between the sentiment-score distributions a model produces for original posts and for gender-counterfactual posts.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-09
sources:
  - id: liu-2025
    resource: "https://doi.org/10.18608/jla.2025.8885"
    title: "Liu, Z., Xing, W., Jiao, X., & Li, C. (2025). Exploring Fairness and Explainability in LLM-Generated Support for Online Learning Discussion Forums. Journal of Learning Analytics, 12(3), 8–33. https://doi.org/10.18608/jla.2025.8885"
    author: "Liu, Z., Xing, W., Jiao, X., & Li, C"
---

# Absolute distributional sentiment divergence (ADSD) as a distribution-level fairness metric for generated replies

> **Theory** · [All theories](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
ADSD is a proposed metric that quantifies sentiment bias by measuring the divergence between the sentiment-score distributions a model produces for original posts and for gender-counterfactual posts. The authors "use the absolute area difference between the two curves (i.e., the shaded areas in Figure 2) as the fairness metric ADSD", integrating the absolute difference between the two density functions. A smaller ADSD value indicates greater fairness; the metric needs no predefined ideal sentiment baseline and suits generative tasks better than classification-accuracy fairness metrics.

## Design Implications

### Context
#### Requirements
- Requires a sentiment classifier applied to replies for both original and counterfactual post sets, and kernel density estimation of the two sentiment distributions
#### Constraints
- Bias is defined relative to distributional divergence between two datasets differing only in a sensitive attribute, not against a universal sentiment baseline

### Target Learners
- online course forum learners in MOOCs

### Target Learning Objectives
- fair and equitable automated socio-emotional support in discussion forums

### Claims
- [Counterfactual Fine Tuning Reduces Sentiment Bias](../claims/counterfactual-fine-tuning-reduces-sentiment-bias.md) [+M]

## Related Theories
- 

## Examples

- [Evaluate and mitigate sentiment bias across sensitive attributes before deploying LLM forum support](../strategies/evaluate-mitigate-llm-sentiment-bias-before-deployment.md)

## Key Sources
- Liu, Z., Xing, W., Jiao, X., & Li, C. (2025). Exploring Fairness and Explainability in LLM-Generated Support for Online Learning Discussion Forums. Journal of Learning Analytics, 12(3), 8–33. https://doi.org/10.18608/jla.2025.8885
