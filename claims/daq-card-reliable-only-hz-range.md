---
type: claim
title: The DAQ card samples reliably only in the Hz range, giving erratic results when data are collected faster than one reading per 0.05 seconds
description: The DAQ card samples reliably only in the Hz range, giving erratic results when data are collected faster than one reading per 0.05 seconds
id: daq-card-reliable-only-hz-range
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

# The DAQ card samples reliably only in the Hz range, giving erratic results when data are collected faster than one reading per 0.05 seconds

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2007 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2010**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` After many trials the authors found the circuit gives erratic results at sampling rates faster than one reading in 0.05 seconds, and that with a 10-sample-per-cycle requirement the maximum reliably recreatable input frequency is 2 Hz. [→ Sumit Ghambir and P.Arun 2007](#sumit-ghambir-and-parun-2007)

## Evidence

### Sumit Ghambir and P.Arun 2007

Sumit Ghambir and P.Arun. (2007). Threadbare Parallel Port DAQ Card. Department of Physics and Electronics, S.G.T.B. Khalsa College, University of Delhi. http://www-server.bcc.ac.uk/~zcapl31/LptADC.html [doi:10.48550/arXiv.0708.3487](https://doi.org/10.48550/arXiv.0708.3487)

`q1 · i?` · `design · r2`

Empirical testing of the card during the class project: the authors report erratic results "if data is collected at rates faster than 1 reading in 0.05sec", so a 0.05 sec delay between readings was required. From a 20 Hz sampling rate and 10 samples per cycle they derive a maximum reliable input frequency of 2 Hz.

> "After many trials we found that our circuit gives erratic results if data is collected at rates faster than 1 reading in 0.05sec."

## Discussion


## Related Claims
- [Captured sine-wave data showed the wave trend but could not be confidently quantified without curve fitting, yielding about five data points per cycle](captured-sine-wave-curve-fitting.md) — related
- [Reducing program delay by assembly programming did not raise sampling rate: total reset delay of 0.05 seconds had to stay constant or the ADC became unreliable](reset-delay-constant-assembly-tradeoff.md) — related
- [Turbo-basic's MTIMER function is unreliable in the microseconds regime but reliable in the milliseconds regime, limiting capturable signal frequencies](mtimer-unreliable-microseconds.md) — related
- [Building the threadbare DAQ card taught students the fundamentals of interfacing and enabled slow-event physics experiments](daq-card-taught-interfacing-fundamentals.md) — a broader claim this one bears on
- [Third-year physics/electronics students show lower mean reaction time and narrower deviation from the mean than first- and second-year students](third-year-students-faster-reaction-time-narrower-deviation.md) — related
