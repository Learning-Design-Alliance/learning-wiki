---
type: claim
title: Reference distance (RefD) models prerequisite relations via asymmetry of Wikipedia reference patterns
description: Reference distance (RefD) models prerequisite relations via asymmetry of Wikipedia reference patterns
id: refd-reference-asymmetry-wikipedia
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
evidence_strength: weak
sources:
  - id: bai-et-al-2025
    title: Bai et al. 2025
    q: 2
    i: "?"
    kind: review
    rigour: "?"
---

# Reference distance (RefD) models prerequisite relations via asymmetry of Wikipedia reference patterns

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · review `r?` · `q2`
> **Currency** · no dated study recorded · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` The RefD metric quantitatively models prerequisite relations by evaluating the asymmetry of reference patterns between Wikipedia KCs, with values near 1 indicating that A is likely a prerequisite for B. [→ Bai et al. 2025](#bai-et-al-2025)

## Evidence

### Bai et al. 2025

Youheng Bai, Zitao Liu, Teng Guo, Mingliang Hou, and Kui Xiao. 2025. Prerequisite Relation Learning: A Survey and Outlook. ACM Comput. Surv. 57, 11, Article 279. https://doi.org/10.1145/3733593

`q2 · i?` · `review · r?`

The survey reports, citing Liang et al., the link-based reference distance metric: a continuous score between -1 and 1 with a threshold mechanism, where "the value of RefD(A,B) is close to 1" signals a prerequisite direction based on citation asymmetry among related Wikipedia concepts. No effect size is printed.

> "when the value of RefD(A,B) is close to 1, it indicates that the related concepts of B cite A much more frequently than the related concepts of A cite B, implying that A is likely a prerequisite for B"

## Discussion


## Related Claims
- [Wikipedia click-stream navigation patterns reveal implicit prerequisite structures between concepts](clickstream-navigation-pr-evidence.md) — related
- [Asymmetric DKT prediction improvement indicates prerequisite direction between knowledge concepts](dkt-asymmetric-prediction-pr-direction.md) — related
- [The PREREQ model, synthesizing multiple educational data sources, outperforms existing methods on standard datasets](prereq-outperforms-standard-datasets.md) — related
