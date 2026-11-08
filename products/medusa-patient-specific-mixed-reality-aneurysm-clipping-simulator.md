---
type: product
id: medusa-patient-specific-mixed-reality-aneurysm-clipping-simulator
title: MEDUSA patient-specific mixed-reality aneurysm clipping simulator
description: A hybrid mixed-reality neurosurgical simulation system developed by Gmeiner et al.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-06
---

# MEDUSA patient-specific mixed-reality aneurysm clipping simulator

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A hybrid mixed-reality neurosurgical simulation system developed by Gmeiner et al. that combines a patient-specific physical skull and brain phantom with tracked instruments, virtual aneurysm anatomy, and simulated blood-flow feedback for aneurysm-clipping training and planning.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **Mass–spring vessel deformation model with Verlet integration for clipping simulation**: The simulation computes vessel deformation from clip-applied force using a mass–spring model with Verlet integration, chosen because it "is not that computationally expensive and still provides a plausible deformation". Mass points are vertices of the vessel triangle mesh; spring forces follow Hooke's law, positions are solved numerically with damping, collisions move points to 0.9 times the collision distance, and a stretching compensation limits errors from large time steps. Force visualisations derive from the vector between each vertex's initial and displaced position. (Allgaier M et al. (2021))

### Claims
- [The mixed-reality aneurysm clipping simulator achieved robust face and content validity, with mean questionnaire scores between 3.13 and 4.25 among 40 neurosurgeons](../claims/medusa-simulator-face-content-validity.md) [+M]
- [Blood flow simulation was the highest-rated simulator component (mean 4.25), and preoperative planning potential was rated 4.20](../claims/medusa-blood-flow-simulation-highest-rated.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Gmeiner M, Schrempf A, Thurner T, Fenz W, Sabrowsky-Hirsch B, Giretzlehner M, Prückl R, Schaffelhofer S, Major Z, Lämmermann S, Baumgartner M, Drabauer L, Nagy J, Esposito G, Colombo E, Stroh-Holly N, Gruber A. (2025). Development and external validation of a mixed-reality aneurysm clipping simulator. Neurosurgical Review. https://doi.org/10.1007/s10143-025-03846-x
- Allgaier M, Neyazi B, Preim B, Saalfeld S. (2021). Distance and force visualisations for improved simulation of intracranial aneurysm clipping. International Journal of Computer Assisted Radiology and Surgery. https://doi.org/10.1007/s11548-021-02413-1
