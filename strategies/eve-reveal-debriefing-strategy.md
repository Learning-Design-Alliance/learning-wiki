---
type: strategy
id: eve-reveal-debriefing-strategy
title: Debriefing session that reveals Eve and discusses why the setup deviates from ideal BB84
description: "After the hacking succeeds, the workshop closes with a debriefing in which the eavesdropped message is revealed to provoke discussion of the protocol's security assumptions."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-18
sources:
  - id: adrian-nugraha-utama-2020
    resource: "https://arxiv.org/abs/1911.02565"
    title: "Adrian Nugraha Utama, Jianwei Lee, and Mathias Alexander Seidler. (2020). A Hands-On Quantum Cryptography Workshop For Pre-University Students. arXiv:1911.02565v2 [physics.ed-ph]. https://arxiv.org/abs/1911.02565"
    author: Adrian Nugraha Utama, Jianwei Lee, and Mathias Alexander Seidler
---

# Debriefing session that reveals Eve and discusses why the setup deviates from ideal BB84

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
After the hacking succeeds, the workshop closes with a debriefing in which the eavesdropped message is revealed to provoke discussion of the protocol's security assumptions. "The debrieﬁng session (Fig. 9) usually starts with Eve reading out loud the secret message that Alice sends to Bob." Facilitators then review how the setup differs from an ideal BB84 system (no single-photon light), the assumptions BB84 requires, the no-cloning theorem's role, and how device-independent QKD protocols can alleviate some assumptions. Facilitators also reveal the beam-splitter and polarization analyzer locations that students often overlooked.

## Design Implications

### Context
#### Requirements
- A successful eavesdropping attempt by the Eve teams preceding the debriefing; facilitators prepared to discuss BB84 assumptions and device-independent QKD
#### Constraints
- The debriefing depends on the intentional macroscopic-light loophole; in this implementation Eve does not resend "qubits", so the key-comparison detection step was omitted

### Target Learners
- pre-university students aged 15 to 19

### Target Learning Goals
- understanding the no-cloning theorem as the central operating principle of QKD security
- recognizing practical vulnerabilities of real QKD implementations

## Claims

- [The apparent failure of the QKD system during the hacking attempt creates cognitive conflict that the authors link to greater learning gains](../claims/cognitive-conflict-hacking-bb84.md) [+W]
- [Pre-university students responded positively to the hands-on BB84 workshop and found its difficulty well balanced](../claims/bb84-workshop-student-feedback.md) [+W]

## Related Strategies

- [BB84 classroom activity with eavesdropper roles and a security test on part of the key](bb84-classroom-eavesdropping-activity.md)
- [Play the BB84 quantum cryptography protocol using only part 1 of the game](entangle-game-bb84-extension.md)

## Examples
-

## Key Sources
- Adrian Nugraha Utama, Jianwei Lee, and Mathias Alexander Seidler. (2020). A Hands-On Quantum Cryptography Workshop For Pre-University Students. arXiv:1911.02565v2 [physics.ed-ph]. https://arxiv.org/abs/1911.02565
