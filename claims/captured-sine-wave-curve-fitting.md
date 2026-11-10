---
type: claim
title: Captured sine-wave data showed the wave trend but could not be confidently quantified without curve fitting, yielding about five data points per cycle
description: Captured sine-wave data showed the wave trend but could not be confidently quantified without curve fitting, yielding about five data points per cycle
id: captured-sine-wave-curve-fitting
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

# Captured sine-wave data showed the wave trend but could not be confidently quantified without curve fitting, yielding about five data points per cycle

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2007 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2010**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Data logged by the card and plotted with Wgnuplot showed the sine-wave trend, but the peak voltage and frequency could not be confidently read from the plot; software curve fitting with Curxprt was used, and five data points per cycle implied a sampling rate of 10 samples per second. [→ Sumit Ghambir and P.Arun 2007](#sumit-ghambir-and-parun-2007)

## Evidence

### Sumit Ghambir and P.Arun 2007

Sumit Ghambir and P.Arun. (2007). Threadbare Parallel Port DAQ Card. Department of Physics and Electronics, S.G.T.B. Khalsa College, University of Delhi. http://www-server.bcc.ac.uk/~zcapl31/LptADC.html [doi:10.48550/arXiv.0708.3487](https://doi.org/10.48550/arXiv.0708.3487)

`q1 · i?` · `design · r2`

Figure 9 shows data stored as an ASCII file and plotted with Wgnuplot; "the trend of the sine wave is evident" but quantification required curve fitting with Curxprt. The authors report five data points per cycle, i.e. a sampling rate of 10 samples per second, one reading per 0.1 sec.

> "While the trend of the sine wave is evident, it was impossible to quantify the wave confidently. That is, one couldn’t comment on V m or the frequency confidently."

## Discussion


## Related Claims
- [The simulated circuit produces three phases with measured phase difference near 120 degrees and equal peak voltages](circuit-measured-phase-difference-112-degrees.md) — related
- [The DAQ card samples reliably only in the Hz range, giving erratic results when data are collected faster than one reading per 0.05 seconds](daq-card-reliable-only-hz-range.md) — related
- [Building the threadbare DAQ card taught students the fundamentals of interfacing and enabled slow-event physics experiments](daq-card-taught-interfacing-fundamentals.md) — a broader claim this one bears on
