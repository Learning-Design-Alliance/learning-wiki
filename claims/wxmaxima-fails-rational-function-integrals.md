---
type: claim
title: wxMaxima fails to compute several rational-function integrals that Axiom and the commercial 3M software can compute
description: wxMaxima fails to compute several rational-function integrals that Axiom and the commercial 3M software can compute
id: wxmaxima-fails-rational-function-integrals
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2021
sources:
  - id: karjanto-2021
    resource: "https://doi.org/10.3390/math9121317"
    title: "Karjanto, N.; Husain, H.S. (2021). Not Another Computer Algebra System: Highlighting wxMaxima in Calculus. Mathematics 2021, 9, 1317. https://doi.org/10.3390/math9121317"
    author: Karjanto, N.; Husain, H.S.
    q: 2
    i: "?"
    kind: design
    rigour: 1
  - id: karjanto-2021-2
    resource: "https://doi.org/10.3390/math9121317"
    title: "Karjanto, N.; Husain, H.S. (2021). Not Another Computer Algebra System: Highlighting wxMaxima in Calculus. Mathematics 2021, 9, 1317. https://doi.org/10.3390/math9121317"
    author: Karjanto, N.; Husain, H.S.
    q: 2
    i: "?"
    kind: design
    rigour: 1
---

# wxMaxima fails to compute several rational-function integrals that Axiom and the commercial 3M software can compute

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r1` · `q2`
> **Currency** · newest study 2021 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` For Bronstein's definite integral of a rational function, wxMaxima could not compute the integral while Axiom and the 3M software could. [→ Karjanto 2021](#karjanto-2021)
`q2 i?` For Tobey's indefinite integral of a rational function, all other compared CAS could compute the integral except wxMaxima. [→ Karjanto 2021 (2)](#karjanto-2021-2)

## Evidence

### Karjanto 2021

Karjanto, N.; Husain, H.S. (2021). Not Another Computer Algebra System: Highlighting wxMaxima in Calculus. Mathematics 2021, 9, 1317. https://doi.org/10.3390/math9121317

`q2 · i?` · `design · r1`

Demonstration in Section 2.2 (Example 8) where the authors ran the integrate command in wxMaxima on Bronstein's definite integral; wxMaxima failed while "Axiom and 3M can tackle it", with Axiom, Maple, Mathematica and Matlab each producing symbolic outputs of the same numerical value.

> "When we attempt the command "integrate((x^4-3*x^2+6)/(x^6-5*x^4+5*x^2+4), x,1,2);", wxMaxima could not compute this integral. However, Axiom and 3M can tackle it."

### Karjanto 2021 (2)

Karjanto, N.; Husain, H.S. (2021). Not Another Computer Algebra System: Highlighting wxMaxima in Calculus. Mathematics 2021, 9, 1317. https://doi.org/10.3390/math9121317

`q2 · i?` · `design · r1`

Demonstration in Section 2.2 (Example 10) of Tobey's indefinite integral of a rational function: the authors report that "all other CAS can compute this integral" while wxMaxima could not, with the known result obtained by the Rothstein–Trager method.

> "Except for wxMaxima, all other CAS can compute this integral. The result can be found on page 502 of [34] using the Rothstein–Trager method."

## Discussion


## Related Claims
- [Students' feedback on embedding wxMaxima and other CAS in Calculus courses was predominantly negative](student-feedback-negative-toward-cas-embedding.md) — related
- [Students can apply procedural knowledge to solve integration problems but show limited understanding of basic integration concepts](procedural-strong-conceptual-limited-integral.md) — related
