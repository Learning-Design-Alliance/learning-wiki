---
type: claim
title: Groups with higher revision coefficients show larger improvements in group-mean accuracy in decentralized networks, but not in centralized networks
description: Groups with higher revision coefficients show larger improvements in group-mean accuracy in decentralized networks, but not in centralized networks
id: revision-coefficient-predicts-group-mean-improvement
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: moderate
newest_evidence: 2017
sources:
  - id: becker-et-al-2017
    resource: "https://doi.org/10.1073/pnas.1615978114"
    title: "Joshua Becker, Devon Brackbill, and Damon Centola. (2017). Network dynamics of social influence in the wisdom of crowds. PNAS. https://doi.org/10.1073/pnas.1615978114"
    author: Joshua Becker, Devon Brackbill, and Damon Centola
    q: 3
    i: 3
    kind: causal
    rigour: 2
  - id: becker-et-al-2017-2
    resource: "https://doi.org/10.1073/pnas.1615978114"
    title: "Joshua Becker, Devon Brackbill, and Damon Centola. (2017). Network dynamics of social influence in the wisdom of crowds. PNAS. https://doi.org/10.1073/pnas.1615978114"
    author: Joshua Becker, Devon Brackbill, and Damon Centola
    q: 3
    i: "?"
    kind: causal
    rigour: 2
---

# Groups with higher revision coefficients show larger improvements in group-mean accuracy in decentralized networks, but not in centralized networks

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i3` large
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q3 i3` In decentralized networks, the group revision coefficient is strongly correlated with improvement in the group mean (ρ = −0.71). [→ Becker et al. 2017](#becker-et-al-2017)
`q3 i?` In centralized networks, there was no significant correlation between the revision coefficient and change in group mean (ρ = −0.16). [→ Becker et al. 2017 (2)](#becker-et-al-2017-2)

## Evidence

### Becker et al. 2017

Joshua Becker, Devon Brackbill, and Damon Centola. (2017). Network dynamics of social influence in the wisdom of crowds. PNAS. https://doi.org/10.1073/pnas.1615978114

`q3 · i3` · `causal · r2`

Across 59 decentralized estimation tasks, controlling for repeated estimates by the same group, the correlation was "ρ= −0.71, 95% CI [−0.82, −0.56]"; |r| ≥ .37 corresponds to a large effect.

> "in decentralized networks, groups with higher revision coefficients also exhibited larger improvements in group accuracy (n= 59 estimation tasks, ρ= −0.71, 95% CI [−0.82, −0.56]."

### Becker et al. 2017 (2)

Joshua Becker, Devon Brackbill, and Damon Centola. (2017). Network dynamics of social influence in the wisdom of crowds. PNAS. https://doi.org/10.1073/pnas.1615978114

`q3 · i?` · `causal · r2`

Across 57 centralized estimation tasks the correlation was not significant ("ρ= −0.16, 95% CI [−0.33, 0.10]"); no effect size interpretation is warranted beyond the printed non-significant coefficient.

> "in centralized networks, there was no significant correlation between the revision coefficient and the change in group mean (n = 57, ρ= −0.16, 95% CI [−0.33, 0.10])"

## Discussion


## Related Claims
- [Improvements from social influence are not explained by independent revision: control groups showed only small individual gains and no change in group accuracy](control-condition-no-group-improvement.md) — related
- [In decentralized networks, social influence also improves the accuracy of the group mean, contrary to the prediction that the mean stays fixed](decentralized-networks-group-mean-improves.md) — related
- [Graph theory parameters distinguish centralized from decentralized discussion groups (density and centralization)](graph-parameters-centralized-decentralized.md) — related
- [More accurate individuals make smaller revisions, indicating a positive correlation between accuracy and self-weight (the revision coefficient)](revision-coefficient-accuracy-self-weight-correlation.md) — related
