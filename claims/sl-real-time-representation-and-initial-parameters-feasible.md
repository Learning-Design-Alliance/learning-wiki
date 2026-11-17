---
type: claim
title: Second Life scripts can represent physical quantities in real time and set initial position, velocity, and mass, satisfying key teaching-oriented simulator criteria
description: Second Life scripts can represent physical quantities in real time and set initial position, velocity, and mass, satisfying key teaching-oriented simulator criteria
id: sl-real-time-representation-and-initial-parameters-feasible
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-17
evidence_strength: weak
newest_evidence: 2014
recheck_by: 2017
sources:
  - id: dos-santos-2014
    resource: "https://doi.org/10.48550/arXiv.1405.6703"
    title: "dos Santos, R. P. (2014). Second Life as a Platform for Physics Simulations and Microworlds: An Evaluation. Originally published 2012. [doi:10.48550/arXiv.1405.6703](https://doi.org/10.48550/arXiv.1405.6703)"
    author: dos Santos, R. P.
    q: 1
    i: "?"
    kind: design
    rigour: 2
  - id: dos-santos-2014-2
    resource: "https://doi.org/10.48550/arXiv.1405.6703"
    title: "dos Santos, R. P. (2014). Second Life as a Platform for Physics Simulations and Microworlds: An Evaluation. Originally published 2012. [doi:10.48550/arXiv.1405.6703](https://doi.org/10.48550/arXiv.1405.6703)"
    author: dos Santos, R. P.
    q: 1
    i: "?"
    kind: design
    rigour: 2
---

# Second Life scripts can represent physical quantities in real time and set initial position, velocity, and mass, satisfying key teaching-oriented simulator criteria

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q1`
> **Currency** · newest study 2014 · not yet checked against its sources · not reviewed by a person · **overdue for a recheck since 2017**: tool and model accuracy changes quickly

## Subclaims
`q1 i?` Position and velocity can be represented directly, in real time, during the entire duration of the phenomenon, via LSL functions. [→ dos Santos 2014](#dos-santos-2014)
`q1 i?` Manipulation of initial parameters such as velocities, masses, and positions is feasible in SL via llRezObject and llSetScale. [→ dos Santos 2014 (2)](#dos-santos-2014-2)

## Evidence

### dos Santos 2014

dos Santos, R. P. (2014). Second Life as a Platform for Physics Simulations and Microworlds: An Evaluation. Originally published 2012. [doi:10.48550/arXiv.1405.6703](https://doi.org/10.48550/arXiv.1405.6703)

`q1 · i?` · `design · r2`

Criterion-based evaluation of SL following Reis & Andrade Neto (2002): although the SL client does not automatically display physical quantities, LSL functions llGetPos and llGetVel let scripts represent position and velocity "directly, in real time , during the entire duration of the phenomenon".

> "Therefore, these quantities can be represented directly, in real time , during the entire duration of the phenomenon, as highlighted in Figure 1 and in Figure 4."

### dos Santos 2014 (2)

dos Santos, R. P. (2014). Second Life as a Platform for Physics Simulations and Microworlds: An Evaluation. Originally published 2012. [doi:10.48550/arXiv.1405.6703](https://doi.org/10.48550/arXiv.1405.6703)

`q1 · i?` · `design · r2`

On the initial-parameters criterion the evaluation judges manipulation "feasible in SL", using llRezObject for initial position and velocity and llSetScale for mass, since mass in SL depends on object size rather than material.

> "It is feasible in SL, as the script can use the LSL llRezObject function to set the initial position and velocity of a physical object. To define the object 's mass, it can use the llSetScale function"

## Discussion


## Related Claims
- [Second Life can run qualitative and simple mechanics experiments, but with reduced accuracy and no consistent millisecond response times](sl-experiments-accuracy-limits.md) — related
- [MICA's universal visualization scripts encode about a dozen data dimensions, and OpenSim worlds allow visualization of ~100,000 data points](immersive-visualization-dimensions-and-opensim-scale.md) — related
- [Smartphones with real-time microsensors can accompany a Classical Mechanics course across its main topics](smartphones-accompany-classical-mechanics-course.md) — related
- [Despite restrictions and differences from traditional simulators, Second Life shows itself as a viable and flexible platform for microworlds and simulations](sl-viable-flexible-platform-microworlds.md) — a broader claim this one bears on
- [Visualizing an array of driven spring-mass systems on the resonance graph is hypothesized to build greater physical intuition of resonance](resonance-graph-visualization-intuition-hypothesis.md) — related
