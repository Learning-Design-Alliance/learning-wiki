---
type: claim
title: KT predicts much worse performance after a failure than PFA, with observed data falling between the two but much closer to PFA
description: KT predicts much worse performance after a failure than PFA, with observed data falling between the two but much closer to PFA
id: kt-overestimates-failure-impact
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
evidence_strength: moderate
newest_evidence: 2009
recheck_by: 2012
sources:
  - id: pavlik-jr-2009
    resource: "https://doi.org/10.3233/978-1-60750-028-5-531"
    title: "Pavlik Jr., P.I., Cen, H., Koedinger, K.R. (2009). Performance Factors Analysis – A New Alternative to Knowledge Tracing. https://doi.org/10.3233/978-1-60750-028-5-531"
    author: Pavlik Jr., P.I., Cen, H., Koedinger, K.R.
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# KT predicts much worse performance after a failure than PFA, with observed data falling between the two but much closer to PFA

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2012**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Learning-curve analysis shows KT overestimates the importance of failure; observed post-failure performance is much closer to PFA's predictions. [→ Pavlik Jr. 2009](#pavlik-jr-2009)

## Evidence

### Pavlik Jr. 2009

Pavlik Jr., P.I., Cen, H., Koedinger, K.R. (2009). Performance Factors Analysis – A New Alternative to Knowledge Tracing. https://doi.org/10.3233/978-1-60750-028-5-531

`q2 · i?` · `associational · r2`

Subsidiary learning-curve analysis of predicted performance probability conditional on the previous response, in the fractions and geometry datasets. The observed average "falling between the two model predictions, but much closer to PFA" indicated KT misfit.

> "We noticed that the KT model had a tendency to predict much worse performance after a failure than did PFA, with the observed average in the data (for performance following failure) falling between the two model predictions, but much closer to PFA."

## Discussion


## Related Claims
- [Across four tutor datasets, the PFA model achieves better LL, BIC, r and A' than two knowledge tracing variants, though the differences are not large](pfa-outperforms-kt-fit-four-datasets.md) — related
- [The survey reports, citing Pavlik et al., that no single knowledge tracing model was always the best, and that a better model must consider multiple student features and the learning context.](no-single-knowledge-tracing-model-is-always-best.md) — a broader claim this one bears on
- [BKT's interpretable latent estimates may not be as useful as thought, though BKT retains uses where model structure must be explained](bkt-latent-estimates-less-useful-than-thought.md) — related
- [Full LFA is marginally superior to PFA on LL and BIC in 3 of 4 datasets, but PFA ties or beats LFA on the Fractions dataset](pfa-approaches-lfa-accuracy.md) — related
