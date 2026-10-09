---
type: claim
title: The frequentist graphical LASSO has difficulty estimating centrality indices and uncertainty in these measures in symptom networks
description: The frequentist graphical LASSO has difficulty estimating centrality indices and uncertainty in these measures in symptom networks
id: frequentist-glasso-difficulty-uncertainty-centrality
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
evidence_strength: weak
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

# The frequentist graphical LASSO has difficulty estimating centrality indices and uncertainty in these measures in symptom networks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`

## Subclaims
`q1 i?` The estimation method often used with symptom networks, the frequentist graphical LASSO, has difficulty estimating centrality indices and uncertainty in these measures. [→ Joran Jongerling 2022](#joran-jongerling-2022)

## Evidence

### Joran Jongerling 2022

Joran Jongerling, Sacha Epskamp, Donald Williams. (2022). Bayesian uncertainty estimation for Gaussian graphical models and centrality indices. Multivariate Behavioral Research. https://www.nwea.org/research/publication/bayesian-uncertainty-estimation-for-gaussian-graphical-models-and-centrality-indices/

`q1 · i?` · `design · r2`

The article's motivating statement about the frequentist GLASSO: it "has difficulty estimating (uncertainty in) these measures" — centrality indices capturing direct and indirect influences among symptoms. No supporting statistics are printed in the available text.

> "the estimation method often used with these networks, the frequentist graphical LASSO (GLASSO), has difficulty estimating (uncertainty in) these measures."

## Discussion


## Related Claims
- [In simulations, the Bayesian GLASSO performed better than the Horseshoe prior for estimating symptom networks](bayesian-glasso-beats-horseshoe-prior.md) — related
- [Bayesian GLASSO shows good coverage of uncertainty for strength and closeness centrality, but uncertainty in betweenness centrality is estimated less well](bayesian-glasso-coverage-strength-closeness-not-betweenness.md) — related
- [In simulations, Bayesian GLASSO estimation outperforms frequentist GLASSO on bias in edge weights, centrality measures, correlation between estimated and true partial correlations, and specificity](bayesian-glasso-outperforms-frequentist-glasso-network-estimation.md) — related
- [Regularization-based graphical modeling has key drawbacks, including difficulty obtaining valid parameter uncertainty and inflated false positive rates](regularization-drawbacks-uncertainty-false-positives.md) — a broader claim this one bears on
