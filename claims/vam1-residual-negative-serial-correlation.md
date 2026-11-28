---
type: claim
title: VAM1 residuals are strongly negatively serially correlated across grades, so the model gives unearned credit to teachers assigned students with low prior-year gains
description: VAM1 residuals are strongly negatively serially correlated across grades, so the model gives unearned credit to teachers assigned students with low prior-year gains
id: vam1-residual-negative-serial-correlation
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
    i: 3
    kind: associational
    rigour: 2
---

# VAM1 residuals are strongly negatively serially correlated across grades, so the model gives unearned credit to teachers assigned students with low prior-year gains

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · associational `r2` · `q2` · `i3` large
> **Currency** · newest study 2008 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2011**: tool and model accuracy changes quickly

## Subclaims
`q2 i3` The correlation between VAM1 residuals in 4th and 5th grade is r = -0.38 in math and r = -0.37 in reading, producing mean-reversion bias in estimated teacher effects. [→ Rothstein 2008](#rothstein-2008)

## Evidence

### Rothstein 2008

Rothstein, Jesse. (2008). Teacher Quality in Educational Production: Tracking, Decay, and Student Achievement. NBER Working Paper No. 14442. http://www.nber.org/papers/w14442

`q2 · i3` · `associational · r2`

Re-estimation of VAM1 for 4th grade teachers' effects on 4th grade gains in the North Carolina panel; the printed across-grade residual correlations are effect sizes of r = -0.38 in math and r = -0.37 in reading — "The correlation between ê1i4 and ê1i5 is -0.38 in math and -0.37 in reading" — indicating negative serial correlation that generates mean-reversion bias.

> "To examine this, I re-estimated VAM1 for 4th grade teachers' effects on 4th grade gains. The correlation between ê1i4 and ê1i5 is -0.38 in math and -0.37 in reading."

## Discussion


## Related Claims
- [Bias from non-random classroom assignments is large relative to estimated teacher effects in VAM1 and somewhat smaller in VAM2](vam-bias-nonrandom-assignment-magnitude.md) — related
- [In North Carolina elementary data, 5th grade classroom assignments significantly predict students' 4th grade test score gains, violating the VAM1 exclusion restriction](vam1-future-teacher-assignment-predicts-past-gains.md) — related
- [VAM2's exclusion restriction is violated in North Carolina data: residuals are correlated across grades and 5th grade teachers predict 4th grade gains controlling for 4th grade scores](vam2-exclusion-restriction-violated-north-carolina.md) — related
- [VAM3's conditional strict exogeneity assumption is rejected: 5th grade teacher coefficients for 3rd and 4th grade gains are near-zero correlated, and the restricted model fails the overidentification test](vam3-strict-exogeneity-rejected-north-carolina.md) — related
