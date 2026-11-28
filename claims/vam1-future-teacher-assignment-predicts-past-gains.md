---
type: claim
title: "In North Carolina elementary data, 5th grade classroom assignments significantly predict students' 4th grade test score gains, violating the VAM1 exclusion restriction"
description: "In North Carolina elementary data, 5th grade classroom assignments significantly predict students' 4th grade test score gains, violating the VAM1 exclusion restriction"
id: vam1-future-teacher-assignment-predicts-past-gains
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-28
evidence_strength: moderate
newest_evidence: 2008
recheck_by: 2011
sources:
  - id: rothstein-2008
    resource: "http://www.nber.org/papers/w14442"
    title: "Rothstein, Jesse. (2008). Teacher Quality in Educational Production: Tracking, Decay, and Student Achievement. NBER Working Paper No. 14442. http://www.nber.org/papers/w14442"
    author: Rothstein, Jesse
    q: 2
    i: "?"
    kind: associational
    rigour: 3
---

# In North Carolina elementary data, 5th grade classroom assignments significantly predict students' 4th grade test score gains, violating the VAM1 exclusion restriction

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r3` · `q2`
> **Currency** · newest study 2008 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2011**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Substituting 4th grade gains for 5th grade gains in the VAM1 specification yields significant apparent effects of 5th grade teachers (standard deviation 0.08 in each subject), showing students are sorted into classrooms on the basis of past gains. [→ Rothstein 2008](#rothstein-2008)

## Evidence

### Rothstein 2008

Rothstein, Jesse. (2008). Teacher Quality in Educational Production: Tracking, Decay, and Student Achievement. NBER Working Paper No. 14442. http://www.nber.org/papers/w14442

`q2 · i?` · `associational · r3`

Falsification analysis of North Carolina administrative data (Table 3): with 4th grade gains substituted as the dependent variable, the standard deviation of 5th grade teachers' coefficients is "0.08 in each subject", and zero association is rejected in both math and reading.

> "The standard deviation of 5th grade teachers' "effects" on 4th grade gains is 0.08 in each subject, and the hypothesis of zero association is rejected in each specification."

## Discussion


## Related Claims
- [Bias from non-random classroom assignments is large relative to estimated teacher effects in VAM1 and somewhat smaller in VAM2](vam-bias-nonrandom-assignment-magnitude.md) — related
- [VAM2's exclusion restriction is violated in North Carolina data: residuals are correlated across grades and 5th grade teachers predict 4th grade gains controlling for 4th grade scores](vam2-exclusion-restriction-violated-north-carolina.md) — related
- [VAM1 residuals are strongly negatively serially correlated across grades, so the model gives unearned credit to teachers assigned students with low prior-year gains](vam1-residual-negative-serial-correlation.md) — related
- [VAM3's conditional strict exogeneity assumption is rejected: 5th grade teacher coefficients for 3rd and 4th grade gains are near-zero correlated, and the restricted model fails the overidentification test](vam3-strict-exogeneity-rejected-north-carolina.md) — related
