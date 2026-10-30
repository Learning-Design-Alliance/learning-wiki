---
type: claim
title: Two main causes of incorrect analysis were unhandled constructs and string-literal quote inconsistencies
description: Two main causes of incorrect analysis were unhandled constructs and string-literal quote inconsistencies
id: php-its-error-causes-constructs-quotes
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
evidence_strength: moderate
newest_evidence: 2014
recheck_by: 2017
sources:
  - id: weragama-2014
    resource: "https://doi.org/10.1007/s40593-014-0014-z"
    title: "Weragama, D. & Reye, J. (2014). Analysing Student Programs in the PHP Intelligent Tutoring System. Int J Artif Intell Educ 24:162–188. https://doi.org/10.1007/s40593-014-0014-z"
    author: "Weragama, D. & Reye, J."
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Two main causes of incorrect analysis were unhandled constructs and string-literal quote inconsistencies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Remaining analysis errors stemmed from students using constructs outside the knowledge base and from difficulty standardising single- versus double-quoted string literals. [→ Weragama 2014](#weragama-2014)

## Evidence

### Weragama 2014

Weragama, D. & Reye, J. (2014). Analysing Student Programs in the PHP Intelligent Tutoring System. Int J Artif Intell Educ 24:162–188. https://doi.org/10.1007/s40593-014-0014-z

`q2 · i?` · `design · r2`

Investigation of exercises still not analysed correctly by the third version identified two main issues. The first was unhandled constructs; the second was that "strings were stored in the predicates using single quotes" while PHP permits both quote types.

> "First, some students were using constructs which were not part of the PHP language that the PHP ITS was designed to teach. Since the knowledge base does not handle these constructs, it is unable to analyze the programs correctly."

## Discussion


## Related Claims
- [The final PHP ITS version correctly analysed 96.31% of student solutions to programming exercises](php-its-96-percent-analysis-accuracy.md) — related
- [Errors serve as valuable feedback for teachers and learners, but unhandled errors risk fossilization](errors-as-feedback-fossilization-risk.md) — related
- [PHP ITS identifies semantically equivalent solutions without bug libraries, ideal solutions or heuristics](php-its-no-bug-libraries-no-heuristics.md) — related
- [Per-exercise analysis accuracy improved from 15 of 27 exercises above 80% to all 27 above 80% in the third version](php-its-per-exercise-accuracy-improvement.md) — related
- [PHP ITS handles interleaved PHP and HTML code via a two-step AST walking process](php-its-two-step-html-php-analysis.md) — related
