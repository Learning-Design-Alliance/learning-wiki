---
type: design
id: battery-resistor-loudspeaker-analogy
title: Battery-resistor-loudspeaker analogy for measurement uncertainty
description: The article proposes a thought experiment in which measurement noise is modeled as a random voltage source in series with an ideal battery, feeding an ideal resistive loudspeaker, so the uncertainty becomes literally...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: gabriel-l-a-de-sousa-george-c-cardoso-2018
    resource: "https://arxiv.org/abs/1611.03425v6"
    title: "Gabriel L. A. de Sousa & George C. Cardoso. (2018). A battery-resistor analogy for further insights on measurement uncertainties. https://arxiv.org/abs/1611.03425v6"
    author: "Gabriel L. A. de Sousa & George C. Cardoso"
---

# Battery-resistor-loudspeaker analogy for measurement uncertainty

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article proposes a thought experiment in which measurement noise is modeled as a random voltage source in series with an ideal battery, feeding an ideal resistive loudspeaker, so the uncertainty becomes literally audible. In this framework "the acoustic power of the noise is the variance of quantity being measured", while the statistical distribution of the noise corresponds to the timbre of the sound. The circuit lets introductory laboratory students derive the variance as mean noise power, the quadrature addition of uncorrelated uncertainties, and the square-root-of-n scaling of the uncertainty of the mean from basic electric-power arguments rather than advanced statistics.

## Design Implications

### Context
#### Requirements
- Rudimentary concepts of electric power and summation notation, which the article names as the only background knowledge needed to follow the arguments.
#### Constraints
- The analogies are directly valid for sums and differences of quantities with uncertainties; propagation through an arbitrary function requires extending the power argument via partial derivatives or finite differences.

### Target Learners
- introductory laboratory students

### Learning Goals
- physical intuition about measurement uncertainties
- interpreting standard deviation and uncertainty of the mean
- adding uncertainties of uncorrelated quantities

### Claims
- Variance Is Mean Power Of Fluctuations [+W]
- Uncorrelated Uncertainties Add Quadratically [+W]
- Sd Interpretation Depends On Noise Distribution [+W]
- Uncertainty Of Mean Insensitive To Noise Distribution [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Gabriel L. A. de Sousa & George C. Cardoso. (2018). A battery-resistor analogy for further insights on measurement uncertainties. https://arxiv.org/abs/1611.03425v6
