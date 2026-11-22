---
type: strategy
id: interpretability-layers-ale-fanova
title: Use post hoc interpretation tools (ALE and fANOVA, or SHAP) across three layers to explain ML-based regime recommendations to families and administrators
description: "Because flexible ML makes the recommendation mechanism hard to explain, the article divides interpretability into three layers: (1) key moderator discovery, (2) non-additivity (interaction) detection, and (3) individu..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: chenguang-pan-2026
    resource: "https://arxiv.org/abs/2610.10843"
    title: "Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk. (2026). Estimating Optimal Dynamic Treatment Regimes for Personalized Education: A Tutorial and Applications with Machine Learning. https://arxiv.org/abs/2610.10843"
    author: Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk
---

# Use post hoc interpretation tools (ALE and fANOVA, or SHAP) across three layers to explain ML-based regime recommendations to families and administrators

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
Because flexible ML makes the recommendation mechanism hard to explain, the article divides interpretability into three layers: (1) key moderator discovery, (2) non-additivity (interaction) detection, and (3) individual-level effect decomposition. It states that "the combination of accumulated local effect (ALE; Apley & Zhu, 2020) and functional ANOVA (fANOVA; Hooker, 2004, 2007) provides a solution to address all three layers", with ALE decomposing individual-level estimates into a grand mean, first-order terms, and higher-order remainders, and fANOVA splitting total variance into shares per covariate, interactions, and a leftover. Shapley value (SHAP) is named as another commonly used post hoc tool.

## Design Implications

### Context
#### Requirements
- A fitted regime model whose individual-level estimates can be decomposed post hoc
#### Constraints
- Ensemble methods deliver accuracy at the cost of transparency, per the article's limitations section

### Target Learners
- high school students

### Target Learning Goals
- transparent personalized course recommendations

### Affordances

## Related Strategies

- [Mitigate equity risk from propensity-based trimming by reporting subgroup trimming rates, varying cutoffs, and excluding protected variables from the treatment model](equity-mitigation-propensity-trimming.md)
- [Use explainability tools (SHAP/LIME) and human monitoring for fair, transparent AI-driven personalized learning](explainability-tools-human-monitoring-personalized-learning.md)
- [Use explainable AI methods (LIME, SHAP) to investigate the relation between individual features and model predictions](explainable-ai-lime-shap-validity-evidence.md)

## Examples
-

## Key Sources
- Chenguang Pan, Yuxuan Li, Thomas Harris, and Youmi Suk. (2026). Estimating Optimal Dynamic Treatment Regimes for Personalized Education: A Tutorial and Applications with Machine Learning. https://arxiv.org/abs/2610.10843
