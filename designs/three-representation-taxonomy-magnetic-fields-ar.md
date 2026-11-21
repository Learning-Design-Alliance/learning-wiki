---
type: design
id: three-representation-taxonomy-magnetic-fields-ar
title: Three-representation taxonomy for visualizing magnetic fields in the Lorentz force experiment
description: "The learning environment provides three scientific model representations: the field vector representation, which \"emphasizes the vector field character of the magnetic field\" by drawing vectors whose length and orient..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: warkentin-2025
    resource: "https://arxiv.org/abs/2502.06421"
    title: "Warkentin, M., Altmeyer, K., Liang, Y., Steinmacher, B., Gränz, B., Lichtenberger, A., Küchemann, S., Kuhn, J. and Hoyer, C. (2025). Hands-on Experiment Supported by Augmented Reality Smartglasses for Learning the Lorentz Force. https://arxiv.org/abs/2502.06421"
    author: Warkentin, M., Altmeyer, K., Liang, Y., Steinmacher, B., Gränz, B., Lichtenberger, A., Küchemann, S., Kuhn, J. and Hoyer, C
---

# Three-representation taxonomy for visualizing magnetic fields in the Lorentz force experiment

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The learning environment provides three scientific model representations: the field vector representation, which "emphasizes the vector field character of the magnetic field" by drawing vectors whose length and orientation encode field value; the field line representation, which shows lines tangent to dipole directions with density encoding field strength; and the right-hand rule representation, which visualizes that the Lorentz force is orthogonal to current and magnetic field. Two representations make the invisible fields visible, while the right-hand rule visualizes the relevant quantities for the Lorentz force.

## Design Implications

### Context
#### Requirements
- Numerically computed magnetic fields of the magnet and conductor to drive the visualizations
- Seed-point distributions for field lines that mirror the field strength behavior
#### Constraints
- Field line density encoding makes proper field line representations more complicated to produce, since equidistant seed points cannot usually be used
- The right-hand rule representation may be difficult for less knowledgeable learners, especially at high school level, because it relates to the vector product

### Target Learners
- High school students
- University physics students

### Learning Goals
- Understanding the Lorentz force and its direction
- Superposition of magnetic fields
- Representational competence of vector fields

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Warkentin, M., Altmeyer, K., Liang, Y., Steinmacher, B., Gränz, B., Lichtenberger, A., Küchemann, S., Kuhn, J. and Hoyer, C. (2025). Hands-on Experiment Supported by Augmented Reality Smartglasses for Learning the Lorentz Force. https://arxiv.org/abs/2502.06421
