---
type: claim
title: The polynomial-time Hungarian algorithm maximized aggregate team score for role assignment, and the team-assembly approach stayed close to the balanced case
description: The polynomial-time Hungarian algorithm maximized aggregate team score for role assignment, and the team-assembly approach stayed close to the balanced case
id: hungarian-assignment-maximizes-team-score
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: weak
newest_evidence: 2022
sources:
  - id: sang-yoon-chang-2022
    resource: "https://doi.org/10.48550/arXiv.2206.08971"
    title: "Sang-Yoon Chang, Kay Yoon, Simeon Wuthier, and Kelei Zhang. (2022). Capture the Flag for Team Construction in Cybersecurity. [doi:10.48550/arXiv.2206.08971](https://doi.org/10.48550/arXiv.2206.08971)"
    author: Sang-Yoon Chang, Kay Yoon, Simeon Wuthier, and Kelei Zhang
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: sang-yoon-chang-2022-2
    resource: "https://doi.org/10.48550/arXiv.2206.08971"
    title: "Sang-Yoon Chang, Kay Yoon, Simeon Wuthier, and Kelei Zhang. (2022). Capture the Flag for Team Construction in Cybersecurity. [doi:10.48550/arXiv.2206.08971](https://doi.org/10.48550/arXiv.2206.08971)"
    author: Sang-Yoon Chang, Kay Yoon, Simeon Wuthier, and Kelei Zhang
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# The polynomial-time Hungarian algorithm maximized aggregate team score for role assignment, and the team-assembly approach stayed close to the balanced case

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`
> **Currency** · newest study 2022 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` Exhaustive-search comparison verified the Hungarian algorithm maximized the team score for role assignments. [→ Sang-Yoon Chang 2022](#sang-yoon-chang-2022)
`q1 i?` Team assembly deviated from the Averaged/Balanced Case by only 2.0821% per team, versus a 31.645% discrepancy for the Max Capacity for Team 1 alternative. [→ Sang-Yoon Chang 2022 (2)](#sang-yoon-chang-2022-2)

## Evidence

### Sang-Yoon Chang 2022

Sang-Yoon Chang, Kay Yoon, Simeon Wuthier, and Kelei Zhang. (2022). Capture the Flag for Team Construction in Cybersecurity. [doi:10.48550/arXiv.2206.08971](https://doi.org/10.48550/arXiv.2206.08971)

`q1 · i?` · `design · r2`

A numerical comparison of role-assignment solutions shown in Fig. 3b: the Hungarian algorithm result was checked against exhaustive search over all role-assignment cases for the study data. The article reports this as verification, not as an analytic proof.

> "We also verified that, once the teams are assembled, the polynomial-time-efficient Hungarian algorithm maximizes the team score by comparing it with all other possible cases for role assignments (exhaustive search on the role assignments)."

### Sang-Yoon Chang 2022 (2)

Sang-Yoon Chang, Kay Yoon, Simeon Wuthier, and Kelei Zhang. (2022). Capture the Flag for Team Construction in Cybersecurity. [doi:10.48550/arXiv.2206.08971](https://doi.org/10.48550/arXiv.2206.08971)

`q1 · i?` · `design · r2`

Numerical team-capacity comparison after team assembly, shown in Fig. 3a, across the study's approach, the Averaged/Balanced Case (infeasible due to fractional capacities), and Max Capacity for Team 1. Printed discrepancies are 2.0821% versus 31.645%.

> "It shows that our approach was close to the Averaged/Balanced Case where Team 1 only outperformed by 27212665.5− 1 = 2.0821% and Team 2 only lagged by 26102665.5 =−2.0821%. In contrast, the most imbalanced case for Max Capacity for Team 1 had a discrepancy of +31.645% for Team 1 and -31.645% for Team 2."

## Discussion


## Related Claims
- [Brute-force search over all possible course sets is computationally infeasible for specialisations with large course catalogues](brute-force-course-set-search-infeasible.md) — related
