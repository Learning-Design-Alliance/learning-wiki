---
type: claim
title: Bayesian network parameters learned from Andes data show probability of gaming is higher for high-gamer/low-gamed-problem combinations than the reverse
description: Bayesian network parameters learned from Andes data show probability of gaming is higher for high-gamer/low-gamed-problem combinations than the reverse
id: bayesian-network-student-class-predicts-gaming
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-26
evidence_strength: moderate
newest_evidence: 2010
sources:
  - id: kasia-muldner-winslow-burleson-brett-van-de-sande-kurt-vanlehn-2010
    resource: "https://doi.org/10.1007/s11257-010-9086-0"
    title: "Kasia Muldner · Winslow Burleson · Brett Van de Sande · Kurt VanLehn (2010). An analysis of students’ gaming behaviors in an intelligent tutoring system: predictors and impacts. User Model User-Adap Inter. https://doi.org/10.1007/s11257-010-9086-0"
    author: Kasia Muldner · Winslow Burleson · Brett Van de Sande · Kurt VanLehn
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# Bayesian network parameters learned from Andes data show probability of gaming is higher for high-gamer/low-gamed-problem combinations than the reverse

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2`
> **Currency** · newest study 2010 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In a naïve Bayes classifier learned from Andes data, setting studentClass high and problemClass low gives gaming probability 0.48, versus 0.28 for the reverse configuration. [→ Kasia Muldner · Winslow Burleson · Brett Van de Sande · Kurt VanLehn 2010](#kasia-muldner-winslow-burleson-brett-van-de-sande-kurt-vanlehn-2010)

## Evidence

### Kasia Muldner · Winslow Burleson · Brett Van de Sande · Kurt VanLehn 2010

Kasia Muldner · Winslow Burleson · Brett Van de Sande · Kurt VanLehn (2010). An analysis of students’ gaming behaviors in an intelligent tutoring system: predictors and impacts. User Model User-Adap Inter. https://doi.org/10.1007/s11257-010-9086-0

`q2 · i?` · `associational · r2`

Bayesian network parameter learning with Netica's counting algorithm on Andes log data (nodes observable and binary; median splits defined studentClass and problemClass). The article reports the predictive network showed the same pattern, with gaming probability below 20% whenever studentClass was low.

> "if we set the value of ‘studentClass’ = high and ‘problemClass’ = low, the probability of gaming is 0.48, higher than the p = 0.28 obtained when we set the value of ‘studentClass’ = low and ‘problemClass’ = high"

## Discussion


## Related Claims
- [Low gamers game by guessing more than high gamers, while high gamers skip more high-level hints, plan less, and copy more bottom-out hints](low-versus-high-gamer-gaming-profiles.md) — related
- [In Cognitive Tutor data from high school students, student is a better gaming predictor for the majority of analyses, but the gaming-distribution analysis did not support this](cognitive-tutor-student-predictor-validation.md) — related
