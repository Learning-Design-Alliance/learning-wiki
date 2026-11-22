---
type: strategy
id: ambiguous-eavesdropper-quarter-wave-plate
title: "Implement the eavesdropper as a quarter-wave plate in a mount visually identical to Alice's and Bob's to keep its presence ambiguous"
description: "Rather than inserting a separate fake-Alice/fake-Bob station that makes Eve visually obvious and dooms the protocol, this strategy introduces Eve as a third wave-plate in a mount visually similar to the other players'..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: john-m-donohue-2026
    resource: "https://arxiv.org/abs/2607.20738"
    title: "John M. Donohue, Silas Ifeanyi, Andrew Chisholm, Julien Côté, Quazell Cunningham, Jamiel Nasser, Aaron Xayvongsa, Evangeline Dryburgh, Fiona Dang, Gabriel Ghrayeb, Ian Jinzo Macpherson, Fareed Rasheed, Andi Zhao, Simarjeet S. Saini. (2026). Interactive and accessible quantum key distribution modules for introducing students to quantum science and engineering. https://arxiv.org/abs/2607.20738"
    author: John M. Donohue, Silas Ifeanyi, Andrew Chisholm, Julien Côté, Quazell Cunningham, Jamiel Nasser, Aaron Xayvongsa, Evangeline Dryburgh, Fiona Dang, Gabriel Ghrayeb, Ian Jinzo Macpherson, Fareed Rasheed, Andi Zhao, Simarjeet S. Saini
---

# Implement the eavesdropper as a quarter-wave plate in a mount visually identical to Alice's and Bob's to keep its presence ambiguous

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
Rather than inserting a separate fake-Alice/fake-Bob station that makes Eve visually obvious and dooms the protocol, this strategy introduces Eve as a third wave-plate in a mount visually similar to the other players' mounts, containing a quarter-wave plate instead of a half-wave plate. The quarter-wave plate rotates the basis states to circular polarization, producing random measurement outcomes unless Eve happens to align to the same basis. The authors write: "To keep the presence of Eve ambiguous and avoid the need for a third student to role-play Eve, we introduce Eve as a third wave-plate in a mount visually similar to Alice and Bob's."

## Design Implications

### Context
#### Requirements
- A quarter-wave plate film cut to the same mount format as the half-wave plates
- Mounts designed so each player's setting is visible only to themselves
#### Constraints
- The quarter-wave plate would be modeled as a state rotation rather than projective measurement, but because students have no way of measuring circular polarizations, the overall effect is the same

### Target Learners
- high-school students
- undergraduate students

### Target Learning Goals
- eavesdropper disturbance effect
- measurement-induced state disturbance
- error rate estimation in QKD

## Claims

- [Revised simulation and activity significantly improved introductory students' answers on actions Alice and Bob can take to detect Eve (78.0% vs 58.9% correct)](../claims/revised-sim-improved-detect-eve-answers.md) [+W]

## Related Strategies

- [BB84 classroom activity with eavesdropper roles and a security test on part of the key](bb84-classroom-eavesdropping-activity.md)
- [Debriefing session that reveals Eve and discusses why the setup deviates from ideal BB84](eve-reveal-debriefing-strategy.md)
- [Predefined Eve protocols variant for high-scale or high-school delivery](predefined-eve-protocols-scale-variant.md)
- [Extend the QKD analogy kit to broader one-qubit quantum concepts by re-labeling mounts and adding optical elements](qkd-kit-extensions-one-qubit-concepts.md)

## Examples
-

## Key Sources
- John M. Donohue, Silas Ifeanyi, Andrew Chisholm, Julien Côté, Quazell Cunningham, Jamiel Nasser, Aaron Xayvongsa, Evangeline Dryburgh, Fiona Dang, Gabriel Ghrayeb, Ian Jinzo Macpherson, Fareed Rasheed, Andi Zhao, Simarjeet S. Saini. (2026). Interactive and accessible quantum key distribution modules for introducing students to quantum science and engineering. https://arxiv.org/abs/2607.20738
