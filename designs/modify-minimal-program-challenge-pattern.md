---
type: design
id: modify-minimal-program-challenge-pattern
title: "Challenge-by-modification pattern: learners modify a minimal working program to test their own model"
description: "The QRC's instructional pattern is a minimal, transparent computer realization of an experiment that learners modify to embody their own favored model."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-09-26
sources:
  - id: vongehr-2012
    resource: "https://doi.org/10.48550/arXiv.1207.5294"
    title: "Vongehr, S. (2012). Quantum Randi Challenge. arXiv:1207.5294. [doi:10.48550/arXiv.1207.5294](https://doi.org/10.48550/arXiv.1207.5294)"
    author: "Vongehr, S."
---

# Challenge-by-modification pattern: learners modify a minimal working program to test their own model

> **Design** · [All designs](index.md)
> **Evidence** · 6 claims (6 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 6 claims rest on one study

## Description
The QRC's instructional pattern is a minimal, transparent computer realization of an experiment that learners modify to embody their own favored model. The article states "Any directly real model whatever needs modification of only three lines of the code", covering hidden-variable construction and the measurement parts, while the random angle choice stays unaltered. Because any directly real model can in principle be realized on classical computers, modification is trivial, so the difficulty lies in the physics, not the programming.

## Design Implications

### Context
#### Requirements
- The experimental setup must be simple (restricted angle choices, exactly 800 photon pairs) so the program stays minimal and lay-accessible
- Hidden variables may have any complexity; simplicity comes from the setup, not from restricting the model
#### Constraints
- The rest of the program, like the random choice of angles, must stay unaltered
- The article notes the envisioned multiplayer game distributed over three computers would need internet communication cut at appropriate times to prevent cheating via artificial non-locality

### Target Learners
- educated lay audience
- high-school level students (envisioned)
- programmers and online physics community members

### Target Goals
- understanding what local hidden variable models entail
- distinguishing measurement prescriptions from hidden variables
- learning through modifying and running simulations

### Claims

- [Qrc Simulation Violates Bell 99 Percent 800 Pairs](../claims/qrc-simulation-violates-bell-99-percent-800-pairs.md) [+M]
- [Classical Indeterminism Model Fails Anticorrelation](../claims/classical-indeterminism-model-fails-anticorrelation.md) [+M]
- [Demanding anti-correlation is argued to be didactically superior to employing the CHSH inequality in the QRC](../claims/anti-correlation-superior-to-chsh-didactically.md) [+W]
- [Cheating hidden variables can violate Bell about 85% of the time only by sacrificing anti-correlation](../claims/cheating-hidden-variables-85-percent-lose-anticorrelation.md) [+W]
- [Hidden variables that skip preparing certain pair classes violate the Bell and CHSH inequality in half of all runs](../claims/hidden-variables-violate-bell-50-percent.md) [+W]
- [An initial QRC deployment terminated artificially created pseudoscience debates on several popular web portals](../claims/qrc-deployment-terminated-online-debates.md) [+W]

## Related Patterns

- [Computational Essay Writing](../patterns/computational-essay-writing.md)

## Examples

- [Quantum Randi Challenge: a modifiable computer game teaching quantum mechanics](../products/quantum-randi-challenge-qrc.md)

## Key Sources
- Vongehr, S. (2012). Quantum Randi Challenge. arXiv:1207.5294. [doi:10.48550/arXiv.1207.5294](https://doi.org/10.48550/arXiv.1207.5294)
