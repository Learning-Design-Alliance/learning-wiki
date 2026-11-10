---
type: claim
title: "Reducing program delay by assembly programming did not raise sampling rate: total reset delay of 0.05 seconds had to stay constant or the ADC became unreliable"
description: "Reducing program delay by assembly programming did not raise sampling rate: total reset delay of 0.05 seconds had to stay constant or the ADC became unreliable"
id: reset-delay-constant-assembly-tradeoff
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

# Reducing program delay by assembly programming did not raise sampling rate: total reset delay of 0.05 seconds had to stay constant or the ADC became unreliable

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q1`
> **Currency** · newest study 2007 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2010**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Testing on an 8085 microprocessor training kit showed that when assembly programming reduced the program delay, the inserted delay had to increase to keep the reset delay constant, indicating a second SOC given 0.05 sec before the first EOC lapse makes the chip unreliable. [→ Sumit Ghambir and P.Arun 2007](#sumit-ghambir-and-parun-2007)

## Evidence

### Sumit Ghambir and P.Arun 2007

Sumit Ghambir and P.Arun. (2007). Threadbare Parallel Port DAQ Card. Department of Physics and Electronics, S.G.T.B. Khalsa College, University of Delhi. http://www-server.bcc.ac.uk/~zcapl31/LptADC.html [doi:10.48550/arXiv.0708.3487](https://doi.org/10.48550/arXiv.0708.3487)

`q1 · i?` · `design · r2`

The authors decompose the total delay as "Reset Delay =Program Delay + Insert Delay" and tested the circuit on an 8085 microprocessor training kit. Lowering the program delay via assembly only forced the insert delay up; this "implies that if a second SOC is given to the ADC0809 0.05sec before the lapse of the first EOC, the behavior of the chip becomes unreliable".

> "While the program delay was bought down we saw that the insert delay had to be increased such that the reset delay remained constant."

## Discussion


## Related Claims
- [The DAQ card samples reliably only in the Hz range, giving erratic results when data are collected faster than one reading per 0.05 seconds](daq-card-reliable-only-hz-range.md) — related
- [Building the threadbare DAQ card taught students the fundamentals of interfacing and enabled slow-event physics experiments](daq-card-taught-interfacing-fundamentals.md) — a broader claim this one bears on
- [Unstructured ChatGPT use in programming education is linked to overreliance, reduced persistence, unreliable outputs, and academic integrity risks](unstructured-chatgpt-use-risks-programming-education.md) — related
