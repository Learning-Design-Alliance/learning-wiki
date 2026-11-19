---
type: design
id: 3d-to-2d-protein-slice-puzzle-pattern
title: Slicing 3D protein structures into 2D puzzle pieces at the point of contact
description: "The game's core design pattern converts academically accurate 3D protein structures into playable 2D puzzle pieces."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: frederic-fol-leymarie-2022
    resource: "https://arxiv.org/abs/2204.12425"
    title: "Frederic Fol Leymarie, William Latham, Guido Salimbeni, Suhail A. Islam, Christopher Reynolds, Charlie Cook, Luis Armas Suarez, Richard Leinfellner, and Michael J. E. Sternberg. (2022). Bioblox 2.5D — Developing an Educational Game Based on Protein Docking. https://arxiv.org/abs/2204.12425"
    author: Frederic Fol Leymarie, William Latham, Guido Salimbeni, Suhail A. Islam, Christopher Reynolds, Charlie Cook, Luis Armas Suarez, Richard Leinfellner, and Michael J. E. Sternberg
---

# Slicing 3D protein structures into 2D puzzle pieces at the point of contact

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The game's core design pattern converts academically accurate 3D protein structures into playable 2D puzzle pieces. The authors state: 'We simplified the molecular binding mechanism into a puzzle game using a solution that cuts the 3D shapes of the docking proteins at the known point of contact into 2D slices.' Models downloaded from the PDB are cut in halves at the exact point of main contact, keeping one half of each chain as the puzzle piece, which preserves correct 3D orientation for docking while enabling an entertaining puzzle experience and shadowed, volume-rendered graphics that increase immersion.

## Design Implications

### Context
#### Requirements
- Access to 3D protein structures in their docking position, e.g. from the Protein Data Bank, so the cut can be made at the known point of contact
#### Constraints
- The manipulated piece is essentially 2D; the (illusion of a) 3D visual shape is maintained graphically rather than through true 3D manipulation

### Target Learners
- teenagers between 13 and 17 years of age learning biology

### Learning Goals
- understanding the complexity of molecular interaction and the importance of shapes and sizes in protein docking

### Claims
- 

## Related Designs
- Bioblox 2 5D Protein Docking Game

## Examples
-

## Key Sources
- Frederic Fol Leymarie, William Latham, Guido Salimbeni, Suhail A. Islam, Christopher Reynolds, Charlie Cook, Luis Armas Suarez, Richard Leinfellner, and Michael J. E. Sternberg. (2022). Bioblox 2.5D — Developing an Educational Game Based on Protein Docking. https://arxiv.org/abs/2204.12425
