---
type: claim
title: "Turbo-basic's MTIMER function is unreliable in the microseconds regime but reliable in the milliseconds regime, limiting capturable signal frequencies"
description: "Turbo-basic's MTIMER function is unreliable in the microseconds regime but reliable in the milliseconds regime, limiting capturable signal frequencies"
id: mtimer-unreliable-microseconds
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-10
evidence_strength: weak
newest_evidence: 2007
recheck_by: 2010
sources:
  - id: sumit-ghambir-and-parun-2007
    resource: "https://doi.org/10.48550/arXiv.0708.3487"
    title: "Sumit Ghambir and P.Arun. (2007). Threadbare Parallel Port DAQ Card. Department of Physics and Electronics, S.G.T.B. Khalsa College, University of Delhi. http://www-server.bcc.ac.uk/~zcapl31/LptADC.html"
    author: Sumit Ghambir and P.Arun
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Turbo-basic's MTIMER function is unreliable in the microseconds regime but reliable in the milliseconds regime, limiting capturable signal frequencies

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2007 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2010**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` The MTIMER library function, though nominally offering 1-microsecond timing resolution, proved unreliable for microsecond timing while working reliably at millisecond scales. [→ Sumit Ghambir and P.Arun 2007](#sumit-ghambir-and-parun-2007)

## Evidence

### Sumit Ghambir and P.Arun 2007

Sumit Ghambir and P.Arun. (2007). Threadbare Parallel Port DAQ Card. Department of Physics and Electronics, S.G.T.B. Khalsa College, University of Delhi. http://www-server.bcc.ac.uk/~zcapl31/LptADC.html [doi:10.48550/arXiv.0708.3487](https://doi.org/10.48550/arXiv.0708.3487)

`q1 · i?` · `design · r2`

The authors observed during testing that "Mtimer was not a reliable timer in the microseconds regime but was working very reliable in the milliseconds regime", which "crippled our ability to work with very high frequencies" though KHz-range capture was nominally still possible.

> "we found that Mtimer was not a reliable timer in the microseconds regime but was working very reliable in the milliseconds regime."

## Discussion


## Related Claims
- [The DAQ card samples reliably only in the Hz range, giving erratic results when data are collected faster than one reading per 0.05 seconds](daq-card-reliable-only-hz-range.md) — related
- [Building the threadbare DAQ card taught students the fundamentals of interfacing and enabled slow-event physics experiments](daq-card-taught-interfacing-fundamentals.md) — a broader claim this one bears on
- [A sound card has a time resolution of a fraction of a millisecond, comparable to that of photogate timers](sound-card-timer-accuracy-comparable-photogate.md) — related
