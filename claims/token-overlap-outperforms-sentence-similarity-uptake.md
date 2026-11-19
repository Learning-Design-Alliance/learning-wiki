---
type: claim
title: Word-overlap measures outperform sentence-level similarity measures, including neural ones, at measuring uptake
description: Word-overlap measures outperform sentence-level similarity measures, including neural ones, at measuring uptake
id: token-overlap-outperforms-sentence-similarity-uptake
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
recheck_by: 2024
sources:
  - id: dorottya-demszky-2021
    resource: "https://doi.org/10.18653/v1/2021.acl-long.130"
    title: "Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)"
    author: Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Word-overlap measures outperform sentence-level similarity measures, including neural ones, at measuring uptake

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2024**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Token-based measures outperform utterance-level similarity measures, with %-IN-T (ρ=.523) the best baseline, significantly beating GLOVE [ALIGNED] (p<0.001). [→ Dorottya Demszky 2021](#dorottya-demszky-2021)

## Evidence

### Dorottya Demszky 2021

Dorottya Demszky, Jing Liu, Zid Mancenido, Julie Cohen, Heather Hill, Dan Jurafsky, Tatsunori Hashimoto. (2021). Measuring Conversational Uptake: A Case Study on Student-Teacher Interactions. [doi:10.18653/v1/2021.acl-long.130](https://doi.org/10.18653/v1/2021.acl-long.130)

`q2 · i?` · `design · r2`

Baseline comparison on the annotated exchange dataset: Spearman correlations between nine unsupervised measures and human uptake labels, with 1000-iteration bootstrap confidence intervals. %-IN-T reached "ρ=.523", and a paired bootstrap test showed it significantly outperformed GLOVE [ALIGNED] (p<0.001); all measures correlated significantly with human judgments.

> "Overall, we ﬁnd that token-based measures outperform utterance-based measures, with %- IN-T (ρ=.523), GLOVE [ALIGNED ] (ρ=.518) (a soft word over-lap measure) and BLEU (ρ = .510) performing the best."

## Discussion


## Related Claims
- [PJSD significantly outperforms the best repetition-based baseline (%-IN-T) at predicting expert uptake annotations](pjsd-outperforms-repetition-baseline-uptake.md) — related
