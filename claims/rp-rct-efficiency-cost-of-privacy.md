---
type: claim
title: The RP-RCT difference-in-means estimator is never as asymptotically efficient as the standard RCT estimator when privacy is guaranteed
description: The RP-RCT difference-in-means estimator is never as asymptotically efficient as the standard RCT estimator when privacy is guaranteed
id: rp-rct-efficiency-cost-of-privacy
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: manjusha-kancharla-and-hyunseung-kang-2021
    resource: "https://doi.org/10.48550/arXiv.2112.02452"
    title: "Manjusha Kancharla and Hyunseung Kang. (2021). A Robust, Differentially Private Randomized Experiment for Evaluating Online Educational Programs With Sensitive Student Data. [doi:10.48550/arXiv.2112.02452](https://doi.org/10.48550/arXiv.2112.02452)"
    author: Manjusha Kancharla and Hyunseung Kang
    q: 2
    i: "?"
    kind: theoretical
    rigour: 3
---

# The RP-RCT difference-in-means estimator is never as asymptotically efficient as the standard RCT estimator when privacy is guaranteed

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For any finite privacy loss epsilon and no cheaters, the RP-RCT estimator has strictly larger asymptotic variance than the standard RCT difference-in-means estimator; relative efficiency approaches 1 only as epsilon approaches infinity. [→ Manjusha Kancharla and Hyunseung Kang 2021](#manjusha-kancharla-and-hyunseung-kang-2021)

## Evidence

### Manjusha Kancharla and Hyunseung Kang 2021

Manjusha Kancharla and Hyunseung Kang. (2021). A Robust, Differentially Private Randomized Experiment for Evaluating Online Educational Programs With Sensitive Student Data. [doi:10.48550/arXiv.2112.02452](https://doi.org/10.48550/arXiv.2112.02452)

`q2 · i?` · `theoretical · r3`

Analytical result (Theorem 4) deriving the relative asymptotic efficiency of the RP-RCT versus standard RCT estimators as a function of the privacy loss epsilon. The article reports the relative efficiency "is monotonically increasing in ϵ" and equals 1 only in the limit of no privacy.

> "In fact, only when the privacy loss approaches inﬁnity, i.e.,ϵ→∞ , do we have relative eﬃciency equaling 1 and thus, ˆτH,Diﬀ will never be as eﬃcient as ˆτDiﬀ as long as we want to guarantee some amount of data privacy."

## Discussion


## Related Claims
- [Responses from non-cheaters in an RP-RCT are differentially private with privacy loss determined by the FRR parameters](rp-rct-non-cheater-privacy-guarantee.md) — related
- [The RP-RCT identifies the ATE among non-cheaters and the proportion of cheaters from privatized outcomes](rp-rct-identifies-ate-among-non-cheaters.md) — related
