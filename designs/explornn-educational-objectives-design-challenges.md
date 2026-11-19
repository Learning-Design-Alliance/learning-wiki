---
type: design
id: explornn-educational-objectives-design-challenges
title: Educational objectives and design challenges for educational RNN visualizations
description: "The article defines four educational objectives based on Bloom's taxonomy — justification (RNNs for sequential data and BPTT), cell structure (LSTM gates and memory), training setup (network structure, training parame..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-19
sources:
  - id: alex-bäuerle-2022
    resource: "https://arxiv.org/abs/2012.06326"
    title: "Alex Bäuerle, Patrick Albus, Raphael Stork, Tina Seufert, and Timo Ropinski. (2022). exploRNN: Teaching Recurrent Neural Networks through Visual Exploration. https://arxiv.org/abs/2012.06326"
    author: Alex Bäuerle, Patrick Albus, Raphael Stork, Tina Seufert, and Timo Ropinski
---

# Educational objectives and design challenges for educational RNN visualizations

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article defines four educational objectives based on Bloom's taxonomy — justification (RNNs for sequential data and BPTT), cell structure (LSTM gates and memory), training setup (network structure, training parameters, data feeding), and task (application areas and transfer to learners' own scenarios) — and derives visualization design challenges from them: "Complexity", "Dynamics", "Multiscale", and "Supervision". Complexity requires visualizations that are "interpretable and intuitive, but realistic enough to form a compelling use case"; dynamics requires communicating sequential data and training processes both forward and backward; multiscale requires fluidly inspectable network, cell, and cell-component granularities; and supervision requires visual guidance to substitute for a teacher in a standalone environment.

## Design Implications

### Context
#### Requirements
- Target users must already understand fundamental DL concepts and feed-forward networks, since explaining these would extend the scope
- Visual guidance must substitute for teacher supervision because the environment is standalone
#### Constraints
- The objectives target recall, comprehension, and transfer (Bloom levels 1–3); analyze, evaluate, and create are left for application in the wild

### Target Learners
- deep learning novices who know feed-forward networks but not RNNs

### Learning Goals
- understanding RNN concepts: sequential data suitability, BPTT, LSTM cell structure and gates, training setup, and application to real tasks

### Claims
- 

## Related Designs
- Explornn Interactive Rnn Visualization

## Examples
-

## Key Sources
- Alex Bäuerle, Patrick Albus, Raphael Stork, Tina Seufert, and Timo Ropinski. (2022). exploRNN: Teaching Recurrent Neural Networks through Visual Exploration. https://arxiv.org/abs/2012.06326
