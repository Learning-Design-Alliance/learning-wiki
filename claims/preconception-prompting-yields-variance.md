---
type: claim
title: Prompting ChatGPT with specific physics preconceptions introduces much response variance that approximates real student FCI distributions
description: Prompting ChatGPT with specific physics preconceptions introduces much response variance that approximates real student FCI distributions
id: preconception-prompting-yields-variance
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
evidence_strength: moderate
newest_evidence: 2023
recheck_by: 2026
sources:
  - id: fabian-kieser-2023
    resource: "https://doi.org/10.1103/physrevphyseducres.19.020150"
    title: "Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann. (2023). Educational data augmentation in physics education research using ChatGPT. [doi:10.1103/physrevphyseducres.19.020150](https://doi.org/10.1103/physrevphyseducres.19.020150)"
    author: Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann
    q: 2
    i: "?"
    kind: design
    rigour: 2
  - id: fabian-kieser-2023-2
    resource: "https://doi.org/10.1103/physrevphyseducres.19.020150"
    title: "Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann. (2023). Educational data augmentation in physics education research using ChatGPT. [doi:10.1103/physrevphyseducres.19.020150](https://doi.org/10.1103/physrevphyseducres.19.020150)"
    author: Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann
    q: 2
    i: "?"
    kind: design
    rigour: 2
---

# Prompting ChatGPT with specific physics preconceptions introduces much response variance that approximates real student FCI distributions

> **Claim** · [All claims](index.md)
> **Evidence** · 1 study (2 entries) · design `r2` · `q2`
> **Currency** · newest study 2023 · not yet checked against its sources · not reviewed by a person · recheck by 2026: tool and model accuracy changes quickly

## Subclaims
`q2 i?` Prompting ChatGPT to respond as-if holding a specific preconception (e.g., impetus, active force, action-reaction) produced widely spread accuracy distributions, with accuracy dropping considerably, sometimes below random guessing. [→ Fabian Kieser 2023](#fabian-kieser-2023)
`q2 i?` Simulated students with the action-reaction (AR) preconception almost systematically fail all items, whereas simulated students with the centrifugal-force (CF) preconception solve the FCI as accurately as without preconceptions. [→ Fabian Kieser 2023 (2)](#fabian-kieser-2023-2)

## Evidence

### Fabian Kieser 2023

Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann. (2023). Educational data augmentation in physics education research using ChatGPT. [doi:10.1103/physrevphyseducres.19.020150](https://doi.org/10.1103/physrevphyseducres.19.020150)

`q2 · i?` · `design · r2`

Findings section on RQ3: response sets generated for each preconception (at least 7 per preconception) showed widely spread distributions; the discussion notes "prompting ChatGPT with preconceptions resulted in distributions that were equally spread as real students' distributions".

> "Here, we found large differences in the response behaviour of ChatGPT. ChatGPT knew about all preconceptions."

### Fabian Kieser 2023 (2)

Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann. (2023). Educational data augmentation in physics education research using ChatGPT. [doi:10.1103/physrevphyseducres.19.020150](https://doi.org/10.1103/physrevphyseducres.19.020150)

`q2 · i?` · `design · r2`

Distributional analysis of preconception-prompted response sets (Fig. 2) reported in the RQ3 Findings section: "students with the AR preconception almost systematically fail at all items" while CF-prompted responses stayed accurate.

> "Interestingly, students with the AR preconception almost systematically fail at all items, whereas simulated students with CF solve the FCI as accurately as without preconceptions"

## Discussion


## Related Claims
- [ChatGPT correctly reasons within two validated preconceptions (centrifugal force and impetus) when prompted to respond as-if a student held them](chatgpt-reasons-within-preconceptions.md) — related
- [Prompting ChatGPT to respond as-if from different cohorts yields no differences in FCI response distributions](cohort-prompting-no-response-differences.md) — related
- [ChatGPT's FCI errors include impetus-type preconceptions shared with beginning physics students](chatgpt-impetus-preconception-errors.md) — related
