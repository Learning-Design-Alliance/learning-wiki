---
type: claim
title: Bayesian GLASSO shows good coverage of uncertainty for strength and closeness centrality, but uncertainty in betweenness centrality is estimated less well
description: Bayesian GLASSO shows good coverage of uncertainty for strength and closeness centrality, but uncertainty in betweenness centrality is estimated less well
id: bayesian-glasso-coverage-strength-closeness-not-betweenness
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
    kind: design
    rigour: 2
---

# Bayesian GLASSO shows good coverage of uncertainty for strength and closeness centrality, but uncertainty in betweenness centrality is estimated less well

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` For uncertainty in centrality measures, the Bayesian GLASSO shows good coverage for strength and closeness centrality, while betweenness centrality uncertainty is estimated less well. [→ Joran Jongerling 2022](#joran-jongerling-2022)

## Evidence

### Joran Jongerling 2022

Joran Jongerling, Sacha Epskamp, Donald Williams. (2022). Bayesian uncertainty estimation for Gaussian graphical models and centrality indices. Multivariate Behavioral Research. https://www.nwea.org/research/publication/bayesian-uncertainty-estimation-for-gaussian-graphical-models-and-centrality-indices/

`q1 · i?` · `design · r2`

Simulation results on uncertainty estimation: "the Bayesian GLASSO shows good coverage for strength and closeness centrality", with betweenness estimated less well. No coverage rates are printed in the available text.

> "the Bayesian GLASSO shows good coverage for strength and closeness centrality, but uncertainty in betweenness centrality is estimated less well."

## Discussion


## Related Claims
- [In simulations, the Bayesian GLASSO performed better than the Horseshoe prior for estimating symptom networks](bayesian-glasso-beats-horseshoe-prior.md) — related
- [In simulations, Bayesian GLASSO estimation outperforms frequentist GLASSO on bias in edge weights, centrality measures, correlation between estimated and true partial correlations, and specificity](bayesian-glasso-outperforms-frequentist-glasso-network-estimation.md) — related
- [The frequentist graphical LASSO has difficulty estimating centrality indices and uncertainty in these measures in symptom networks](frequentist-glasso-difficulty-uncertainty-centrality.md) — related
