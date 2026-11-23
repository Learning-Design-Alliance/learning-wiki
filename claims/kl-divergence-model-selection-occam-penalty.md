---
type: claim
title: Surprisal-based model selection adds an Occam-factor penalty for superfluous fit-parameters on top of goodness of fit
description: Surprisal-based model selection adds an Occam-factor penalty for superfluous fit-parameters on top of goodness of fit
id: kl-divergence-model-selection-occam-penalty
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-16
evidence_strength: weak
newest_evidence: 2011
sources:
  - id: p-fraundorf-2011
    resource: "https://doi.org/10.48550/arXiv.1106.4698"
    title: "P. Fraundorf. (2011). Metric-first & entropy-first surprises. arXiv preprint. [doi:10.48550/arXiv.1106.4698](https://doi.org/10.48550/arXiv.1106.4698)"
    author: P. Fraundorf
    q: 2
    i: "?"
    kind: theoretical
    rigour: 2
---

# Surprisal-based model selection adds an Occam-factor penalty for superfluous fit-parameters on top of goodness of fit

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r2` · `q2`
> **Currency** · newest study 2011 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` KL-divergence-based model selection formally considers both goodness of fit and algorithmic simplicity, penalizing superfluous fit-parameters. [→ P. Fraundorf 2011](#p-fraundorf-2011)

## Evidence

### P. Fraundorf 2011

P. Fraundorf. (2011). Metric-first & entropy-first surprises. arXiv preprint. [doi:10.48550/arXiv.1106.4698](https://doi.org/10.48550/arXiv.1106.4698)

`q2 · i?` · `theoretical · r2`

Analytical derivation (Eqs. 2-3) of cross-entropy for a least-squares model fit, showing the expected net-surprisal equals uncertainty in best-fit plus an Occam cost of fit; the article notes "the Occam factor term in such surprisal analyses in eﬀect adds a penalty for superﬂuous ﬁt-parameters".

> "Like other goodness- of-ﬁt measures (which can be seen as special cases of this) the Occam factor term in such surprisal analyses in eﬀect adds a penalty for superﬂuous ﬁt-parameters."

## Discussion


## Related Claims
- [A reinforcement learning model with separate surprise and uncertainty learning-rate parameters per condition best fits gambling behavior, though individual parameter estimates did not reach significance](rl-model-separate-surprise-uncertainty-el-ol.md) — related
- [KL-divergence and binary cross-entropy losses for course prediction yield grade prediction within 1-2% of each other](kl-versus-bce-loss-ablation.md) — related
- [KL divergence loss with small τ (≤ 1.0) mitigates noisy-label corruption better than extreme logit matching](small-tau-kl-mitigates-noisy-labels.md) — related
