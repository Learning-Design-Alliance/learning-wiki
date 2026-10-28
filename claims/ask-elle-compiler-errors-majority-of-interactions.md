---
type: claim
title: Compiler errors accounted for over half of diagnosis interactions in the log analysis
description: Compiler errors accounted for over half of diagnosis interactions in the log analysis
id: ask-elle-compiler-errors-majority-of-interactions
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
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Compiler errors accounted for over half of diagnosis interactions in the log analysis

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2016 · not yet checked against its sources · not reviewed by a person

## Subclaims
`q2 i?` In the 2013 log analysis, compiler errors accounted for 55.4% of interactions (1920 of 3466) and 21.8% of attempts, making it the largest single category of diagnosis outcomes. [→ Gerdes 2016](#gerdes-2016)

## Evidence

### Gerdes 2016

Gerdes, A., Heeren, B., Jeuring, J., & van Binsbergen, L. T. (2016). Ask-Elle: an Adaptable Programming Tutor for Haskell Giving Automated Feedback. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-015-0080-x

`q2 · i?` · `design · r2`

Table 2 of the log analysis reports the Compiler error category with 142 attempts (21.8%) and 1920 interactions (55.4%). This is the largest category by interactions, indicating many submissions contained syntax or type errors that the student had to repair before further feedback could be given.

> "Compiler error 142 (21.8%) 1920 (55.4%)"

## Discussion


## Related Claims

- [In log analysis of 3466 interactions, 56.1% of interactions and 46.3% of attempts were recognised as correct model solutions](ask-elle-log-analysis-recognition-rates.md) — related
- [All three LLM-generated feedback types are associated with faster time to solution than a compiler-errors-only baseline, with Single-Issue Feedback showing the largest reduction](llm-feedback-faster-time-to-solution.md)
