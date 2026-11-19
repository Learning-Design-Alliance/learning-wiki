---
type: claim
title: Suspected IP addresses in the test sets originate from geographically similar locations, and fewer than 10 cases were flagged per test set
description: Suspected IP addresses in the test sets originate from geographically similar locations, and fewer than 10 cases were flagged per test set
id: suspected-ips-geographically-similar-locations
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
sources:
  - id: leslie-ching-ow-tiong-2022
    resource: "https://doi.org/10.48550/arXiv.2201.13226"
    title: "Leslie Ching Ow Tiong, HeeJeong Jasmine Lee, Kai Li Lim. (2022). Online Assessment Misconduct Detection using Internet Protocol and Behavioural Classification. arXiv preprint. [doi:10.48550/arXiv.2201.13226](https://doi.org/10.48550/arXiv.2201.13226)"
    author: Leslie Ching Ow Tiong, HeeJeong Jasmine Lee, Kai Li Lim
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Suspected IP addresses in the test sets originate from geographically similar locations, and fewer than 10 cases were flagged per test set

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` PCA visualisation of six test sets showed fewer than 10 suspected-IP cases per test set, and many suspected IP addresses originated from geographically similar locations such as roommates or housemates. [→ Leslie Ching Ow Tiong 2022](#leslie-ching-ow-tiong-2022)

## Evidence

### Leslie Ching Ow Tiong 2022

Leslie Ching Ow Tiong, HeeJeong Jasmine Lee, Kai Li Lim. (2022). Online Assessment Misconduct Detection using Internet Protocol and Behavioural Classification. arXiv preprint. [doi:10.48550/arXiv.2201.13226](https://doi.org/10.48550/arXiv.2201.13226)

`q2 · i?` · `design · r2`

Evaluation of the IP detection agent across six test sets, with PCA visualisation shown in Fig. 4; the quoted sentences report the flagged-case count and the geographic co-location observation.

> "From Fig. 4, there are less than 10 cases where IP addresses were flagged as ‘suspected’ in a given test set. We observed that many ‘suspected’ IP addresses originate from geographically similar locations, i.e., the candidates were roommates, housemates or located within the same premise."

## Discussion


## Related Claims
- [The combined IP detector and behavioural monitor flagged a real plagiarism case involving twins sharing the suspected IP address 211.243.246.3](twin-plagiarism-case-flagged-by-system.md) — related
