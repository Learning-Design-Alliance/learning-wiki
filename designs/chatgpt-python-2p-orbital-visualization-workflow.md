---
type: design
id: chatgpt-python-2p-orbital-visualization-workflow
title: ChatGPT-assisted Python visualization workflow for hydrogen 2p orbitals
description: A workflow in which ChatGPT-4o first solves the 2p orbitals of the hydrogen atom step by step (quantum numbers, separation of variables, radial and angular parts), then generates a Python script using numpy, matplotli...
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: huiping-han-and-liang-wu-2024
    resource: "https://arxiv.org/abs/2409.06925"
    title: "Huiping Han and Liang Wu. (2024). ChatGPT-Assisted Visualization of Atomic Orbitals: Understanding Symmetry, Mixed State, and Superposition. https://arxiv.org/abs/2409.06925"
    author: Huiping Han and Liang Wu
---

# ChatGPT-assisted Python visualization workflow for hydrogen 2p orbitals

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
A workflow in which ChatGPT-4o first solves the 2p orbitals of the hydrogen atom step by step (quantum numbers, separation of variables, radial and angular parts), then generates a Python script using numpy, matplotlib, and skimage marching cubes to plot the probability density isosurface of a chosen 2p orbital. The script is executed in a Python IDE, and the remaining orbitals are visualized by substituting wavefunctions. The authors note that generating custom scripts offers "the significant advantage of allowing these illustrations observable from all perspectives, thereby enhancing comprehension".

## Design Implications

### Context
#### Requirements
- A Python IDE to execute the generated script; the paper notes ChatGPT can also provide a step-by-step installation guide for readers unfamiliar with installing one
#### Constraints
- Multiple constraints on the plotting process were needed, so the authors omitted the detailed conversation with ChatGPT from the paper

### Target Learners
- undergraduate students newly introduced to quantum mechanics

### Learning Goals
- visualize 3D probability densities of atomic orbitals
- connect orbital mathematics to orbital shapes

### Claims
- 

## Related Designs

- [ExperiMentor: a custom GPT-based chatbot that generates and executes Python code for guided physics data analysis](experimentor-custom-gpt-physics-chatbot.md)

## Examples
-

## Key Sources
- Huiping Han and Liang Wu. (2024). ChatGPT-Assisted Visualization of Atomic Orbitals: Understanding Symmetry, Mixed State, and Superposition. https://arxiv.org/abs/2409.06925
