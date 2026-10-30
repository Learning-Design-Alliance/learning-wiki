---
type: claim
title: PHP ITS identifies semantically equivalent solutions without bug libraries, ideal solutions or heuristics
description: PHP ITS identifies semantically equivalent solutions without bug libraries, ideal solutions or heuristics
id: php-its-no-bug-libraries-no-heuristics
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: weak
newest_evidence: 2014
recheck_by: 2017
sources:
  - id: weragama-2014
    resource: "https://doi.org/10.1007/s40593-014-0014-z"
    title: "Weragama, D. & Reye, J. (2014). Analysing Student Programs in the PHP Intelligent Tutoring System. Int J Artif Intell Educ 24:162–188. https://doi.org/10.1007/s40593-014-0014-z"
    author: "Weragama, D. & Reye, J."
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# PHP ITS identifies semantically equivalent solutions without bug libraries, ideal solutions or heuristics

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The PHP ITS uses generalised predicates rather than stored ideal solutions, enabling recognition of diverse alternative solutions. [→ Weragama 2014](#weragama-2014)

## Evidence

### Weragama 2014

Weragama, D. & Reye, J. (2014). Analysing Student Programs in the PHP Intelligent Tutoring System. Int J Artif Intell Educ 24:162–188. https://doi.org/10.1007/s40593-014-0014-z

`q1 · i?` · `design · r2`

Comparison to related work (type e). The authors argue their approach avoids limitations of bug libraries, cognitive tutors' production rules, and intention-based analysis heuristics by using "a set of generalized predicates".

> "The method of program analysis used in the PHP ITS does not depend on an ideal solution but on a set of generalized predicates. This means that many alternative solutions can result in the same set of predicates and therefore, the method is suitable for handling diversity in student programs."

## Discussion


## Related Claims
- [The final PHP ITS version correctly analysed 96.31% of student solutions to programming exercises](php-its-96-percent-analysis-accuracy.md) — related
- [Two main causes of incorrect analysis were unhandled constructs and string-literal quote inconsistencies](php-its-error-causes-constructs-quotes.md) — related
- [Strategy-based assessment statically determines which solution strategy a student used and guarantees correctness of recognised programs](strategy-based-assessment-static-benefits.md) — related
