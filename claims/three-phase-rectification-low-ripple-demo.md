---
type: claim
title: A three-diode rectifier on the simulated 3-phase supply shows continuous DC output with little ripple without filtering
description: A three-diode rectifier on the simulated 3-phase supply shows continuous DC output with little ripple without filtering
id: three-phase-rectification-low-ripple-demo
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-10
evidence_strength: moderate
newest_evidence: 2009
recheck_by: 2012
sources:
  - id: amit-kumar-singhal-parun-2009
    resource: "https://doi.org/10.48550/arXiv.0907.3279"
    title: "Amit Kumar Singhal & P.Arun. (2009). Studying Three Phase Supply in School. arXiv preprint. https://arxiv.org/abs/0907.3279"
    author: "Amit Kumar Singhal & P.Arun"
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# A three-diode rectifier on the simulated 3-phase supply shows continuous DC output with little ripple without filtering

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study · design `r2` · `q2`
> **Currency** · newest study 2009 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2012**: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Rectifying the simulated 3-phase supply with three diodes and a load resistance yields a DC output that is continuous with little ripple even without a filtering circuit. [→ Amit Kumar Singhal & P.Arun 2009](#amit-kumar-singhal-parun-2009)

## Evidence

### Amit Kumar Singhal & P.Arun 2009

Amit Kumar Singhal & P.Arun. (2009). Studying Three Phase Supply in School. arXiv preprint. https://arxiv.org/abs/0907.3279 [doi:10.48550/arXiv.0907.3279](https://doi.org/10.48550/arXiv.0907.3279)

`q2 · i?` · `design · r2`

Demonstration experiment on the simulated supply using "3 diodes and a load resistan ce". The article attributes the low ripple to the load seeing an input frequency three times that of a single phase supply, since ripple is inversely proportional to frequency.

> "The output waveform is DC and also notice even without any ﬁl tering circuit, the output is continuous with little ripple. This is because, as s een by the load, the input frequency is three times that of a single phase supply."

## Discussion


## Related Claims
- [The simulated circuit produces three phases with measured phase difference near 120 degrees and equal peak voltages](circuit-measured-phase-difference-112-degrees.md) — related
- [Polyphase supply delivers more power to a load than single phase, shown analytically for a 2-phase example](polyphase-delivers-more-power-derivation.md) — related
