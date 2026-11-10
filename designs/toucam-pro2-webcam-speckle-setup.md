---
type: design
id: toucam-pro2-webcam-speckle-setup
title: Montage de speckle sur banc optique avec webcam Toucam Pro 2 sans objectif
description: "Élément matériel permettant de réaliser et enregistrer des figures de speckle à faible coût sur un banc d'optique : laser He-Ne, verre dépoli, diaphragme calibré et webcam dont l'objectif est retiré."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-10
sources:
  - id: chenaud-boris-2005
    resource: "http://astrosurf.org/buil/us/iris/iris.htm"
    title: "Chenaud Boris, Valvin Pierre. (2005). Granularité laser et interférences de speckles. http://astrosurf.org/buil/us/iris/iris.htm"
    author: Chenaud Boris, Valvin Pierre
---

# Montage de speckle sur banc optique avec webcam Toucam Pro 2 sans objectif

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
Élément matériel permettant de réaliser et enregistrer des figures de speckle à faible coût sur un banc d'optique : laser He-Ne, verre dépoli, diaphragme calibré et webcam dont l'objectif est retiré. L'article précise : "nous avons utilisé une webcam Toucam Pro 2  munie du capteur Sony ICX098BQ. Ce capteur est constitué de 659 x 494 pixels" avec "le pas de notre capteur est de 5,6 µm". Le dépoli est translaté par une vis micrométrique et les images sont traitées par un programme Labview ou par le logiciel gratuit Iris. Le retrait de l'objectif permet d'enregistrer les seuls speckles objectifs. Les images servent à mesurer la taille des speckles et à calculer des TF de superpositions.

## Design Implications

### Context
#### Requirements
- Un faisceau laser cohérent (He-Ne), un diffuseur (verre dépoli), un diaphragme de diamètre calibré D, un banc d'optique et un capteur CCD sans objectif ; un critère d'échantillonnage imposant au moins 5 pixels par détail fin de speckle.
#### Constraints
- Les enregistrements se font directement sur la CCD, objectif dévissé, pour éviter le champ de speckles subjectifs causé par l'optique de la webcam ; pour les interférences, L > 1 m pour se placer en conditions de Fraunhofer.

### Target Learners
- étudiants en optique de niveau universitaire (enseignement de la physique)

### Learning Goals
- comprendre le phénomène de speckle
- maîtriser l'optique de Fourier (produit, convolution)
- ancrer les interférences à 2 et N ondes et la diffraction par les réseaux

### Claims
- [Speckle Grain Size Proportional L Over D](../claims/speckle-grain-size-proportional-l-over-d.md) [+M]
- [Two Wave Fringes From Shifted Speckle Superposition](../claims/two-wave-fringes-from-shifted-speckle-superposition.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Chenaud Boris, Valvin Pierre. (2005). Granularité laser et interférences de speckles. http://astrosurf.org/buil/us/iris/iris.htm
