---
type: claim
title: The RP-RCT identifies the ATE among non-cheaters and the proportion of cheaters from privatized outcomes
description: The RP-RCT identifies the ATE among non-cheaters and the proportion of cheaters from privatized outcomes
id: rp-rct-identifies-ate-among-non-cheaters
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

# The RP-RCT identifies the ATE among non-cheaters and the proportion of cheaters from privatized outcomes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · theoretical `r3` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Under assumptions A1-A8, the ATE among non-cheaters is identified from privatized outcomes re-weighed by the FRR parameters and the estimated proportion of cheaters, and the proportion of cheaters is itself identified via sample splitting. [→ Manjusha Kancharla and Hyunseung Kang 2021](#manjusha-kancharla-and-hyunseung-kang-2021)

## Evidence

### Manjusha Kancharla and Hyunseung Kang 2021

Manjusha Kancharla and Hyunseung Kang. (2021). A Robust, Differentially Private Randomized Experiment for Evaluating Online Educational Programs With Sensitive Student Data. [doi:10.48550/arXiv.2112.02452](https://doi.org/10.48550/arXiv.2112.02452)

`q2 · i?` · `theoretical · r3`

Analytical identification result (Theorem 2) showing the ATE among non-cheaters is identified from privatized outcomes "re-weighed by the FRR parameters r,r′ and the proportion of cheaters λ"; the proportion of cheaters is identified through moment conditions from sample splitting. If everyone is a cheater, identification fails.

> "Theorem 2 shows that our new design can identify the ATE among non-cheaters by taking the diﬀerence in the averages of the privatized outcomes~Yi among treated and control units, re-weighed by the FRR parameters r,r′ and the proportion of cheaters λ."

## Discussion


## Related Claims
- [Estimated proportion of cheaters varied by question, higher for learning-ability outcomes than instruction outcomes](cheater-proportion-varies-by-question.md) — a narrower finding that bears on this claim
- [Instructor-present video lectures improved self-reported attention among honest students relative to instructor-absent lectures](instructor-present-videos-improved-attention.md) — a narrower finding that bears on this claim
- [The RP-RCT difference-in-means estimator is never as asymptotically efficient as the standard RCT estimator when privacy is guaranteed](rp-rct-efficiency-cost-of-privacy.md) — related
- [Responses from non-cheaters in an RP-RCT are differentially private with privacy loss determined by the FRR parameters](rp-rct-non-cheater-privacy-guarantee.md) — possibly the same claim (merge candidate)
