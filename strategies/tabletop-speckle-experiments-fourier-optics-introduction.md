---
type: strategy
id: tabletop-speckle-experiments-fourier-optics-introduction
title: "Introduire l'optique de Fourier et l'interférométrie par des expériences de speckle réalisables sur un coin de table"
description: "Stratégie d'enseignement proposée par les auteurs : utiliser des montages de speckle simples et peu coûteux pour introduire le phénomène de tavelure et l'interférométrie stellaire."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-10
sources:
  - id: chenaud-boris-2005
    resource: "http://astrosurf.org/buil/us/iris/iris.htm"
    title: "Chenaud Boris, Valvin Pierre. (2005). Granularité laser et interférences de speckles. http://astrosurf.org/buil/us/iris/iris.htm"
    author: Chenaud Boris, Valvin Pierre
---

# Introduire l'optique de Fourier et l'interférométrie par des expériences de speckle réalisables sur un coin de table

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
Stratégie d'enseignement proposée par les auteurs : utiliser des montages de speckle simples et peu coûteux pour introduire le phénomène de tavelure et l'interférométrie stellaire. Selon l'article, "Les expériences proposées ici permettent une introduction du phénomène de speckle réalisable sur un «  coin de table » et au contenu physique très riche", et "L'interférométrie par speckles permet d'appréhender l' optique de Fourier et son formalisme (produit, convolution…), sous un autre angle". La démarche part de l'observation de granularité laser, passe par la mesure de la taille des speckles, puis superpose des figures décalées pour retrouver les interférences à 2 et N ondes et la diffraction par les réseaux, jusqu'à l'application astronomique suivant Labeyrie. La popularisation des capteurs CCD via les webcams rend ces expériences accessibles.

## Design Implications

### Context
#### Requirements
- Un laser cohérent, un diffuseur, un capteur CCD (webcam sans objectif) et un traitement d'images (programme Labview ou logiciel gratuit Iris) pour sommer les images et calculer les TF.
#### Constraints
- Les montages s'adressent à l'introduction des notions d'optique de Fourier et d'interférométrie ; l'application astronomique suppose un télescope suivi par une monture motorisée et des poses courtes figeant la turbulence.

### Target Learners
- étudiants du supérieur en physique-optique

### Target Learning Goals
- comprendre la cohérence spatiale et le speckle
- revisiter la diffraction par les réseaux
- relier l'optique de table à la mesure astronomique

## Claims

- [La superposition de N figures de speckle décalées se comporte, en transformée de Fourier, comme la diffraction d'un réseau à N motifs : N−2 minima secondaires (visibles jusqu'à N = 10) et pics principaux s'affinant en 1/N](../claims/n-speckle-superposition-grating-analogy.md) [+W]
- [La taille des speckles objectifs varie proportionnellement à L et inversement à D, vérifiée par régression pour λ = 633,0 µm](../claims/speckle-grain-size-proportional-l-over-d.md) [+W]
- [L'interférométrie de speckles avec un télescope amateur mesure l'orientation et la séparation de l'étoile double Gamma Leo, cohérentes avec le catalogue WDS](../claims/speckle-interferometry-gamma-leo-separation.md) [+W]
- [La superposition de deux figures de speckle translatées donne, après transformée de Fourier, des franges à 2 ondes dont l'interfrange diminue quand le pas h augmente](../claims/two-wave-fringes-from-shifted-speckle-superposition.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Chenaud Boris, Valvin Pierre. (2005). Granularité laser et interférences de speckles. http://astrosurf.org/buil/us/iris/iris.htm
