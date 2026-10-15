---
type: design
id: school-aggregation-benchmark-generator
title: Synthetic benchmark instance generator for school aggregation problems
description: Because no public benchmark existed, the article developed a structured random instance generator producing synthetic yet realistic regional school networks.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: alessia-ciacco-2026
    resource: "https://arxiv.org/abs/2608.05427"
    title: "Alessia Ciacco, Luigi Di Puglia Pugliese, Francesca Guerriero. (2026). School network reorganization under educational and spatial constraints using classical and quantum optimization. https://arxiv.org/abs/2608.05427"
    author: Alessia Ciacco, Luigi Di Puglia Pugliese, Francesca Guerriero
---

# Synthetic benchmark instance generator for school aggregation problems

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Because no public benchmark existed, the article developed a structured random instance generator producing synthetic yet realistic regional school networks. It reproduces hierarchical settlement geography (provincial capitals, large, medium, and small municipalities), heterogeneous school types and educational tracks, and differentiated territorial criticality levels. Four instance sizes were considered with n in {250,500,750,1000}, spanning medium-scale to large-scale regional planning scenarios, with schools clustered around municipality centers via bivariate Gaussian sampling.

## Design Implications

### Context
#### Requirements
- Real-world demographic data to calibrate instance sizes and territorial structures
#### Constraints
- Instances are synthetic and abstract; the article notes limitations of the tested benchmark instances for quantum evaluation

### Target Learners
- school-age students in synthetic regional networks

### Learning Goals
- evaluating scalability of school dimensioning optimization models

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Alessia Ciacco, Luigi Di Puglia Pugliese, Francesca Guerriero. (2026). School network reorganization under educational and spatial constraints using classical and quantum optimization. https://arxiv.org/abs/2608.05427
