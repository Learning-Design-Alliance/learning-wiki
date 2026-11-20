---
type: claim
title: "Fuzzy membership functions correctly determine students' cluster membership even when clusters are not clearly separated"
description: "Fuzzy membership functions correctly determine students' cluster membership even when clusters are not clearly separated"
id: fuzzy-membership-correct-borderline-assignment
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
source_checked: 2026-11-20
recheck_by: 2026
sources:
  - id: serhiy-balovsyak-2023
    resource: "https://doi.org/10.5815/ijmecs.2023.06.03"
    title: "Serhiy Balovsyak, Oleksandr Derevyanchuk, Hanna Kravchenko, Yuriy Ushenko, Zhengbing Hu. (2023). Clustering Students According to their Academic Achievement Using Fuzzy Logic. International Journal of Modern Education and Computer Science (IJMECS), Vol.15, No.6, pp. 31-43. https://doi.org/10.5815/ijmecs.2023.06.03"
    author: Serhiy Balovsyak, Oleksandr Derevyanchuk, Hanna Kravchenko, Yuriy Ushenko, Zhengbing Hu
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Fuzzy membership functions correctly determine students' cluster membership even when clusters are not clearly separated

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2023 · checked against its sources 2026-11-20 (automated, 1 of 1 entry) · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Processing test educational data with the developed software showed fuzzy logic ensures correct determination of students' belonging degree to clusters in the absence of clear boundaries between clusters. [→ Serhiy Balovsyak 2023](#serhiy-balovsyak-2023)

## Evidence

### Serhiy Balovsyak 2023

Serhiy Balovsyak, Oleksandr Derevyanchuk, Hanna Kravchenko, Yuriy Ushenko, Zhengbing Hu. (2023). Clustering Students According to their Academic Achievement Using Fuzzy Logic. International Journal of Modern Education and Computer Science (IJMECS), Vol.15, No.6, pp. 31-43. https://doi.org/10.5815/ijmecs.2023.06.03

`q2 · i?` · `design · r2`

Verification of the developed software on test educational data (Q = 1000 students with math, reading and writing scores) clustered by K-Means; the article reports that "the use of fuzzy logic ensures the correct determination of the belonging degree of students". No effect size is printed.

> "Testing of the developed software showed that the use of fuzzy logic ensures the correct determination of the belonging degree of students to certain groups (clusters) even in the absence of clear boundaries between clusters."

## Discussion


## Related Claims
- [Fuzzy membership degrees support individualized task-difficulty recommendations, e.g. student iv=12 assigned mostly to cluster 3 with additional cluster 2 tasks](fuzzy-membership-task-difficulty-recommendation.md) — related
- [A near-normal distribution of cluster sizes indicates the chosen task difficulty level is appropriate](normal-cluster-size-distribution-difficulty-check.md) — related
