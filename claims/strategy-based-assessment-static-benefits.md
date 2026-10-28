---
type: claim
title: Strategy-based assessment statically determines which solution strategy a student used and guarantees correctness of recognised programs
description: Strategy-based assessment statically determines which solution strategy a student used and guarantees correctness of recognised programs
id: strategy-based-assessment-static-benefits
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2016
sources:
  - id: gerdes-2016
    resource: "https://doi.org/10.1007/s40593-015-0080-x"
    title: "Gerdes, A., Heeren, B., Jeuring, J., & van Binsbergen, L. T. (2016). Ask-Elle: an Adaptable Programming Tutor for Haskell Giving Automated Feedback. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0080-x"
    author: "Gerdes, A., Heeren, B., Jeuring, J., & van Binsbergen, L. T."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Strategy-based assessment statically determines which solution strategy a student used and guarantees correctness of recognised programs

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q1 i?` The authors argue that strategy-based assessment addresses four problems of test-based assessment: it guarantees correctness of recognised programs, recognises imperfections, identifies the algorithm implemented, and is carried out statically. [→ Gerdes 2016](#gerdes-2016)

## Evidence

### Gerdes 2016

Gerdes, A., Heeren, B., Jeuring, J., & van Binsbergen, L. T. (2016). Ask-Elle: an Adaptable Programming Tutor for Haskell Giving Automated Feedback. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0080-x

`q1 · i?` · `design · r2`

Theoretical argument in the assessment section, contrasting strategy-based assessment with test-based tools. The authors state "if a program is determined to be equivalent, it is guaranteed to be correct" and list the four problems testing cannot address. Adding QuickCheck testing reintroduces vulnerability to bugs and malicious software.

> "Using strategies for assessing student programs solves the four problems of using testing for assessment described above: 1. if a program is determined to be equivalent, it is guaranteed to be correct 2. we can recognise and report imperfections 3. we can determine which algorithm has been implemented 4. strategy-based assessment is carried out statically."

## Discussion


## Related Claims
- [Strategy-based assessment recognised 62 of 72 correct student programs (86%) from four model solutions with no false positives](ask-elle-assessment-recognises-62-of-72-programs.md) — related
- [In log analysis of 3466 interactions, 56.1% of interactions and 46.3% of attempts were recognised as correct model solutions](ask-elle-log-analysis-recognition-rates.md) — related
