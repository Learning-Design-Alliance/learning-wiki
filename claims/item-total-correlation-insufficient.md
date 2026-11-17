---
type: claim
title: Item-total correlation is insufficient for unfair-item identification because unfair items can have positive correlations and fair items negative ones
description: Item-total correlation is insufficient for unfair-item identification because unfair items can have positive correlations and fair items negative ones
id: item-total-correlation-insufficient
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: weak
newest_evidence: 2012
recheck_by: 2015
sources:
  - id: bakman-2012
    resource: "https://doi.org/10.48550/arXiv.1205.3380"
    title: "Bakman, Y. (2012). Identifying Unfair Items in Educational Measurement. Originally published 2007. [doi:10.48550/arXiv.1205.3380](https://doi.org/10.48550/arXiv.1205.3380)"
    author: Bakman, Y.
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Item-total correlation is insufficient for unfair-item identification because unfair items can have positive correlations and fair items negative ones

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2012 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2015**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The performed analysis shows r is clearly insufficient: unfair Item 25 had r=0.32 while almost-trivial fair Item 2 (53 of 55 students correct) had r=-0.05 and was flagged unfair by the traditional method. [→ Bakman 2012](#bakman-2012)

## Evidence

### Bakman 2012

Bakman, Y. (2012). Identifying Unfair Items in Educational Measurement. Originally published 2007. [doi:10.48550/arXiv.1205.3380](https://doi.org/10.48550/arXiv.1205.3380)

`q2 · i?` · `design · r2`

Conclusion of the comparison section, grounded in the real-test example: Item 25's topic was insufficiently taught (di = -0.29) yet r=0.32, and Item 2, 'a trivial item cannot be unfair', lies near the ideal line but has item-total correlation r = -0.05.

> "The performed analysis shows that r is clearly insufficient for the identification of unfair items."

## Discussion


## Related Claims
- [The proposed method identifies unfair items with positive item-total correlations that the traditional method misses, supported by expert judgments](method-finds-unfair-items-positive-correlation.md) — possibly the same claim (merge candidate)
- [Deleting identified unfair items brings fair-item points closer to the ideal line, halving the sum of positive distances](unfair-item-deletion-halves-positive-distances.md) — related
- [Teaching influences which items are identified as unfair: three lecturer groups agree on items 5, 25, and 28 but differ on others](teaching-influences-unfair-item-identification.md) — related
