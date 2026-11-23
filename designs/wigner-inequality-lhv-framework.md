---
type: design
id: wigner-inequality-lhv-framework
title: "Wigner's Inequality is an accessible set-theoretic alternative to Bell's theorem for testing local hidden-variables models"
description: "The paper presents Wigner's Inequality (WIE) as a route to testing quantum correlations without the full apparatus of Bell's theorem."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-23
sources:
  - id: maximilian-rottensteiner-2026
    resource: "https://arxiv.org/abs/2606.30255"
    title: "Maximilian Rottensteiner, Dorian Schiffer, Tobias Pausch, Alois Mair, and Anton Zeilinger. (2026). Photonic Violation of Wigner's Inequality. https://arxiv.org/abs/2606.30255"
    author: Maximilian Rottensteiner, Dorian Schiffer, Tobias Pausch, Alois Mair, and Anton Zeilinger
---

# Wigner's Inequality is an accessible set-theoretic alternative to Bell's theorem for testing local hidden-variables models

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The paper presents Wigner's Inequality (WIE) as a route to testing quantum correlations without the full apparatus of Bell's theorem. It states that "Formally, WIE follows from a local hidden-variables (LHV) model derived using a set-theoretic argument with minimal assumptions, making it particularly well suited for introductory physics courses." The derivation models particle outcomes as drawn from eight predefined anti-correlated sets (Table I), yielding the bound W ≥ 0, and quantum predictions are computed via Born's Rule on the singlet Bell state. Any observation of a negative Wigner value rules out classical predefined correlations. The paper uses this framework to connect a theoretical derivation, an optical experiment, and student data analysis.

## Design Implications

### Context
#### Requirements
- A source producing polarization-entangled photon pairs in the singlet Bell state, which exhibits perfect anti-correlation for all choices of the absolute angle
- Three measurement settings per observer, realized as polarization filters, with two possible outcomes each (transmission or rejection)
#### Constraints
- The derivation assumes perfect anti-correlation, which cannot be achieved experimentally; the authors note this constitutes an additional loophole and that their demonstration does not address loopholes
- The authors recommend discussing loophole-closure strategies with students

### Target Learners
- Undergraduate physics students
- Introductory physics course students

### Learning Goals
- Understand quantum correlations and where classical local-realist models fail
- Develop intuition for quantum mechanics and a rigorous scientific mindset

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Maximilian Rottensteiner, Dorian Schiffer, Tobias Pausch, Alois Mair, and Anton Zeilinger. (2026). Photonic Violation of Wigner's Inequality. https://arxiv.org/abs/2606.30255
