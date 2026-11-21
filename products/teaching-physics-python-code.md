---
type: product
id: teaching-physics-python-code
title: Teaching-physics Python code
description: A GitHub-released Python simulator and associated implementation for visualizing the electric field produced by multiple charges, developed for teaching electromagnetism and laboratory courses.
product_kind: software
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-18
---

# Teaching-physics Python code

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · no claims cited

## Description
A GitHub-released Python simulator and associated implementation for visualizing the electric field produced by multiple charges, developed for teaching electromagnetism and laboratory courses.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **GitHub release of the teaching-physics Python code**: The article states that the code is available on GitHub at https://github.com/alexestupinan123/Teaching_physics_Python.git, making the simulator and its methodology reproducible and reusable by other instructors. The release accompanies the implementation of the tool in electromagnetism and laboratory courses at three institutions of higher education in Colombia. (K L Cristiano et al. (2019))
- **Python routine computing the magnetic field of a finite straight wire arbitrarily oriented in space**: A short python function (Fig. 2) computes the magnitude of the magnetic field produced by a finite straight current-carrying wire arbitrarily oriented in space, implementing the Cartesian-coordinate form of the finite-wire expression (Eq. 4). The article states its inputs are 'the coordinates (x,y ) where B is evaluated', 'the position of the wire ( rA,rB)', and 'the value of the electric current I'. It is presented as a tool that lets students explore how each parameter of Eq. (4) affects the field and visualize different configurations, since python is described as very friendly with a wide set of tools usable without deep programming knowledge. (J.E. García-Farieta et al. (2020))
- **Open-source Python script suite reproducing all figures for classroom use**: The article's appendix compiles Python scripts, one per figure, presented step by step with comments so students can compute and visualize trajectory parameters. The scripts use numpy and matplotlib and "can be executed directly in environments such as Jupyter Notebook or Google Colab", letting students reproduce all results and modify v0 and θ to explore new configurations. They serve as the reproducible computational tool underlying the framework's visualizations. (L. Hernández-Sánchez et al. (2026))

### Claims

## Related Products and Programmes
-

## Key Sources
- K L Cristiano, D A Triana, A. Estupiñán. (2019). Python script used as simulator for the teaching of electric field in electromagnetism course. https://arxiv.org/abs/1901.08670
- J.E. García-Farieta and A. Hurtado-Márquez. (2020). Beyond the magnetic field of a finite wire: a teaching approach using the superposition principle. https://arxiv.org/abs/2001.05966
- L. Hernández-Sánchez, I. Ramos-Prieto, F. Soto-Eguibar, and H.M. Moya-Cessa. (2026). A computational and pedagogical framework for projectile motion using Python visualizations. https://arxiv.org/abs/2601.05769
