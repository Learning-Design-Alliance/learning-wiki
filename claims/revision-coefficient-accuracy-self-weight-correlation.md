---
type: claim
title: More accurate individuals make smaller revisions, indicating a positive correlation between accuracy and self-weight (the revision coefficient)
description: More accurate individuals make smaller revisions, indicating a positive correlation between accuracy and self-weight (the revision coefficient)
id: revision-coefficient-accuracy-self-weight-correlation
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
    i: 2
    kind: causal
    rigour: 2
---

# More accurate individuals make smaller revisions, indicating a positive correlation between accuracy and self-weight (the revision coefficient)

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · causal `r2` · `q3` · `i2`–`i3`
> **Currency** · newest study 2017 · not yet checked against its sources · not reviewed by a person
> **Design limits** · Becker et al. 2017 (2): no comparison group (read from the study by two models, 2026-11-24)

## Subclaims
`q3 i3` Individual revision magnitude is positively correlated with initial error (ρ = 0.41). [→ Becker et al. 2017](#becker-et-al-2017)
`q3 i2` The correlation persists after controlling for distance between an individual's estimate and their neighborhood average (ρ = 0.25). [→ Becker et al. 2017 (2)](#becker-et-al-2017-2)

## Evidence

### Becker et al. 2017

Joshua Becker, Devon Brackbill, and Damon Centola. (2017). Network dynamics of social influence in the wisdom of crowds. PNAS. https://doi.org/10.1073/pnas.1615978114

`q3 · i3` · `causal · r2`

Analysis of covariance over 4,340 estimates by 1,040 subjects found "ρ=0.41, 95% CI [0.39, 0.43]", controlling for repeated estimates by the same individual; ρ = 0.41 corresponds to a large effect.

> "the magnitude of an individual's revisions from round 1 to 3 was significantly correlated with the magnitude of their initial error (n =4,340 estimates by 1,040 subjects, ρ=0.41, 95% CI [0.39, 0.43], P <0.001, analysis of covariance)"

### Becker et al. 2017 (2)

Joshua Becker, Devon Brackbill, and Damon Centola. (2017). Network dynamics of social influence in the wisdom of crowds. PNAS. https://doi.org/10.1073/pnas.1615978114

`q3 · i2` · `causal · r2`

Partial correlation holding constant the distance between each estimate and the neighborhood average remained significant, "ρ= 0.25, 95% CI [0.22, 0.28]"; the authors call this partial correlation the revision coefficient.

> "even with this statistical control, more accurate individuals still made smaller revisions to their estimates than less accurate individuals (n= 4,340 estimates by 1,040 subjects, ρ= 0.25, 95% CI [0.22, 0.28], P <0.001, analysis of covariance)"

## Discussion


## Related Claims
- [Improvements from social influence are not explained by independent revision: control groups showed only small individual gains and no change in group accuracy](control-condition-no-group-improvement.md) — related
- [Self-other parameter differences in model-based weights and model-free learning rates predict prosocial behavioural signatures at the participant level](parameter-differences-predict-prosocial-signatures.md) — related
- [Groups with higher revision coefficients show larger improvements in group-mean accuracy in decentralized networks, but not in centralized networks](revision-coefficient-predicts-group-mean-improvement.md) — related
