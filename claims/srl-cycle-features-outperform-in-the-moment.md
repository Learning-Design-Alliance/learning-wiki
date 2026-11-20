---
type: claim
title: A model including SRL cycle characteristics fits next-attempt correctness better than a model using only in-the-moment SRL codes
description: A model including SRL cycle characteristics fits next-attempt correctness better than a model using only in-the-moment SRL codes
id: srl-cycle-features-outperform-in-the-moment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
sources:
  - id: conrad-borchers-2024
    title: Conrad Borchers 2024
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# A model including SRL cycle characteristics fits next-attempt correctness better than a model using only in-the-moment SRL codes

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` Adding historical SRL cycle features (loop state, attempts since last closed loop, attempts per cycle) to in-the-moment SRL codes significantly improved model fit. [→ Conrad Borchers 2024](#conrad-borchers-2024)

## Evidence

### Conrad Borchers 2024

Conrad Borchers, Jiayi Zhang, Ryan S. Baker, and Vincent Aleven. 2024. Using Think-Aloud Data to Understand Relations between Self-Regulation Cycle Characteristics and Student Performance in Intelligent Tutoring Systems. In The 14th Learning Analytics and Knowledge Conference (LAK '24). ACM. https://doi.org/10.1145/3636555.3636911

`q2 · i?` · `associational · r1`

Likelihood-ratio comparison of mixed logistic regression models on the same 630-attempt dataset (N = 630 as printed in Table 3); the cycle-features model was preferred, with student intercepts explaining "𝑅2 = 14.0% of the variance in correctness beyond fixed effects".

> "The model with SRL cycle characteristics significantly fit the data better than the model using only in-the-moment SRL codes right before attempts based on a likelihood-ratio test,𝜒 2(3) = 14.08,𝑝 =.003."

## Discussion


## Related Claims
- [Correctness rises the farther students are into an ongoing SRL cycle, and longer average cycles relate to higher correctness](srl-cycle-position-correctness.md) — related
- [In-tutor correctness is lower after processing and error-realization utterances and higher after enacting utterances in stoichiometry ITS](srl-codes-moment-correctness-its.md) — related
- [No individual unigram in think-aloud utterances significantly distinguished correct from incorrect subsequent attempts after multiple-testing correction](unigrams-null-next-attempt-correctness.md) — related
