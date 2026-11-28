---
type: claim
title: "VAM3's conditional strict exogeneity assumption is rejected: 5th grade teacher coefficients for 3rd and 4th grade gains are near-zero correlated, and the restricted model fails the overidentification test"
description: "VAM3's conditional strict exogeneity assumption is rejected: 5th grade teacher coefficients for 3rd and 4th grade gains are near-zero correlated, and the restricted model fails the overidentification test"
id: vam3-strict-exogeneity-rejected-north-carolina
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
    i: 0
    kind: associational
    rigour: 3
  - id: rothstein-2008-2
    resource: "http://www.nber.org/papers/w14442"
    title: "Rothstein, Jesse. (2008). Teacher Quality in Educational Production: Tracking, Decay, and Student Achievement. NBER Working Paper No. 14442. http://www.nber.org/papers/w14442"
    author: Rothstein, Jesse
    q: 2
    i: "?"
    kind: associational
    rigour: 2
---

# VAM3's conditional strict exogeneity assumption is rejected: 5th grade teacher coefficients for 3rd and 4th grade gains are near-zero correlated, and the restricted model fails the overidentification test

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · associational `r2`–`r3` · `q2` · `i0` negligible
> **Currency** · newest study 2008 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2011**: tool and model accuracy changes quickly

## Subclaims
`q2 i0` Under strict exogeneity the 5th grade teacher coefficients in the 3rd and 4th grade gain equations should be perfectly correlated, but the estimated correlations are -0.04 (math) and -0.06 (reading). [→ Rothstein 2008](#rothstein-2008)
`q2 i?` The optimal minimum distance test of the restricted VAM3 model is overwhelmingly rejected for both math and reading gains. [→ Rothstein 2008 (2)](#rothstein-2008-2)

## Evidence

### Rothstein 2008

Rothstein, Jesse. (2008). Teacher Quality in Educational Production: Tracking, Decay, and Student Achievement. NBER Working Paper No. 14442. http://www.nber.org/papers/w14442

`q2 · i0` · `associational · r3`

Correlated random effects projection (Table 5): with 3rd and 4th grade gains regressed on teacher indicators from grades 3-5, 5th grade teacher coefficients correlate "-0.04 for math and -0.06 for reading" across the two equations, far from the perfect correlation strict exogeneity implies.

> "The most important correlation is that for 5th grade teachers, -0.04 for math and -0.06 for reading."

### Rothstein 2008 (2)

Rothstein, Jesse. (2008). Teacher Quality in Educational Production: Tracking, Decay, and Student Achievement. NBER Working Paper No. 14442. http://www.nber.org/papers/w14442

`q2 · i?` · `associational · r2`

Optimal minimum distance test of the restricted VAM3 model for math gains: the estimated ability-loading ratio "is 0.14", implying ability matters far more for 3rd grade than 4th grade gains, and the overidentifying restrictions are overwhelmingly rejected.

> "For math scores, the estimated ratio ∆τ4/∆τ3 from the less restrictive model is 0.14, implying that student ability is much more important to 3rd grade than to 4th grade gains."

## Discussion


## Related Claims
- [In North Carolina elementary data, 5th grade classroom assignments significantly predict students' 4th grade test score gains, violating the VAM1 exclusion restriction](vam1-future-teacher-assignment-predicts-past-gains.md) — related
- [VAM1 residuals are strongly negatively serially correlated across grades, so the model gives unearned credit to teachers assigned students with low prior-year gains](vam1-residual-negative-serial-correlation.md) — related
- [VAM2's exclusion restriction is violated in North Carolina data: residuals are correlated across grades and 5th grade teachers predict 4th grade gains controlling for 4th grade scores](vam2-exclusion-restriction-violated-north-carolina.md) — related
- [Bias from non-random classroom assignments is large relative to estimated teacher effects in VAM1 and somewhat smaller in VAM2](vam-bias-nonrandom-assignment-magnitude.md) — a broader claim this one bears on
