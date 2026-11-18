---
type: claim
title: Engagement, number of views and star ratings carry very different information, with near-zero correlation between engagement and ratings
description: Engagement, number of views and star ratings carry very different information, with near-zero correlation between engagement and ratings
id: engagement-decoupled-from-views-and-ratings
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
evidence_strength: moderate
newest_evidence: 2020
recheck_by: 2023
sources:
  - id: sahan-bulathwela-2020
    resource: "https://doi.org/10.48550/arXiv.2006.00592"
    title: "Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)"
    author: Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor
    q: 2
    i: "?"
    kind: associational
    rigour: 1
---

# Engagement, number of views and star ratings carry very different information, with near-zero correlation between engagement and ratings

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r1` · `q2`
> **Currency** · newest study 2020 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2023**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` MNET engagement correlates near zero with mean star ratings (SROCC 0.028) and rather negatively with number of views (SROCC -0.333), so these implicit and explicit signals represent different information. [→ Sahan Bulathwela 2020](#sahan-bulathwela-2020)

## Evidence

### Sahan Bulathwela 2020

Sahan Bulathwela, María Pérez-Ortiz, Aldo Lipani, Emine Yilmaz and John Shawe-T aylor. (2020). Predicting Engagement in Video Lectures. [doi:10.48550/arXiv.2006.00592](https://doi.org/10.48550/arXiv.2006.00592)

`q2 · i?` · `associational · r1`

Observational analysis of the VLN dataset shown in Figure 1 scatter plots of mean star rating vs MNET and number of views. The printed coefficients are SROCC 0.028 for rating vs MNET and SROCC -0.333 for rating vs views; the authors note "The SROCC is close to zero" for all four engagement encodings tested.

> "The SROCC is close to zero, mainly because of the large number of lectures with high rating but low engagement and number of views."

## Discussion


## Related Claims
- [Intervention engagement (narratives consumed) showed no clear association with outcome changes](story-mine-engagement-outcome-null-association.md) — related
- [Raw LMNET is the most predictable engagement encoding, and Random Forest with kernelised models performs best, indicating non-linearity](raw-lmnet-rf-best-engagement-prediction.md) — related
