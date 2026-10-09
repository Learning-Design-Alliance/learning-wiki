---
type: claim
title: In simulations, Bayesian GLASSO estimation outperforms frequentist GLASSO on bias in edge weights, centrality measures, correlation between estimated and true partial correlations, and specificity
description: In simulations, Bayesian GLASSO estimation outperforms frequentist GLASSO on bias in edge weights, centrality measures, correlation between estimated and true partial correlations, and specificity
id: bayesian-glasso-outperforms-frequentist-glasso-network-estimation
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: moderate
sources:
  - id: joran-jongerling-2022
    resource: "https://www.nwea.org/research/publication/bayesian-uncertainty-estimation-for-gaussian-graphical-models-and-centrality-indices/"
    title: "Joran Jongerling, Sacha Epskamp, Donald Williams. (2022). Bayesian uncertainty estimation for Gaussian graphical models and centrality indices. Multivariate Behavioral Research. https://www.nwea.org/research/publication/bayesian-uncertainty-estimation-for-gaussian-graphical-models-and-centrality-indices/"
    author: Joran Jongerling, Sacha Epskamp, Donald Williams
    q: 1
    i: "?"
    kind: causal
    rigour: 2
---

# In simulations, Bayesian GLASSO estimation outperforms frequentist GLASSO on bias in edge weights, centrality measures, correlation between estimated and true partial correlations, and specificity

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · causal `r2` · `q1`

## Subclaims
`q1 i?` The Bayesian GLASSO outperformed the frequentist GLASSO with respect to bias in edge weights, centrality measures, correlation between estimated and true partial correlations, and specificity in extensive simulations. [→ Joran Jongerling 2022](#joran-jongerling-2022)

## Evidence

### Joran Jongerling 2022

Joran Jongerling, Sacha Epskamp, Donald Williams. (2022). Bayesian uncertainty estimation for Gaussian graphical models and centrality indices. Multivariate Behavioral Research. https://www.nwea.org/research/publication/bayesian-uncertainty-estimation-for-gaussian-graphical-models-and-centrality-indices/

`q1 · i?` · `causal · r2`

Extensive simulation study comparing estimation of symptom networks with Bayesian GLASSO- and Horseshoe priors to frequentist GLASSO; results showed that "the Bayesian GLASSO outperformed the frequentist GLASSO" on the listed measures. No effect sizes are printed in the available text.

> "the Bayesian GLASSO outperformed the frequentist GLASSO with respect to bias in edge weights, centrality measures, correlation between estimated and true partial correlations, and specificity."

## Discussion


## Related Claims
- [In simulations, the Bayesian GLASSO performed better than the Horseshoe prior for estimating symptom networks](bayesian-glasso-beats-horseshoe-prior.md) — related
- [Bayesian GLASSO shows good coverage of uncertainty for strength and closeness centrality, but uncertainty in betweenness centrality is estimated less well](bayesian-glasso-coverage-strength-closeness-not-betweenness.md) — related
- [Sensitivity is better for the frequentist GLASSO than for the Bayesian GLASSO, though Bayesian GLASSO performance is usually close](frequentist-glasso-higher-sensitivity-network-estimation.md) — related
- [The frequentist graphical LASSO has difficulty estimating centrality indices and uncertainty in these measures in symptom networks](frequentist-glasso-difficulty-uncertainty-centrality.md) — related
