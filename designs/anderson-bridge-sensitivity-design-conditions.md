---
type: design
id: anderson-bridge-sensitivity-design-conditions
title: Design the Anderson bridge with R1 = R3 much greater than R2 = R4 (R2 very small), XL much greater than Xc, and high audio frequency to obtain good sensitivity
description: The article derives, using Network Analysis theorems and the Maximum Power Transfer Theorem, a set of circuit conditions for good bridge sensitivity, defined as a large change in headphone power for a small change in r.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-10
sources:
  - id: p-arun-2008
    resource: "https://arxiv.org/abs/0804.3932v1"
    title: "P. Arun, Kuldeep Kumar & Mamta. (2008). Considerations for Anderson-Bridge Experiment. https://arxiv.org/abs/0804.3932v1"
    author: "P. Arun, Kuldeep Kumar & Mamta"
---

# Design the Anderson bridge with R1 = R3 much greater than R2 = R4 (R2 very small), XL much greater than Xc, and high audio frequency to obtain good sensitivity

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article derives, using Network Analysis theorems and the Maximum Power Transfer Theorem, a set of circuit conditions for good bridge sensitivity, defined as a large change in headphone power for a small change in r. It summarises: "We summarize here the circuitial conditions one must maintain to get good sensitivity for the Anderson Bridge", listing large R1 and R3 with very small R2, XL >> Xc, and high audio frequency. The conclusion restates that "for a better sensitivity, one should work at high frequencies and use a low R2 and high capacitance (making XL >> Xc)."

## Design Implications

### Context
#### Requirements
- The headphone impedance is inductive and of low value, so the Thevenin impedance must be capacitive for maximum power transfer
#### Constraints
- Very high capacitances are usually electrolytic, thus introducing problems of their own, and the frequency must remain in the audible range, so Xc ∼ 0 may be difficult to attain

### Target Learners
- undergraduate physics laboratory students

### Learning Goals
- measuring self-inductance of a coil with an AC bridge
- applying Network Analysis theorems to circuit design

### Claims
- [Anderson Bridge Redesign Yields Accurate Inductance](../claims/anderson-bridge-redesign-yields-accurate-inductance.md) [+M]
- Smaller Capacitance Degrades Anderson Bridge Accuracy [+M]
- [Low Audio Frequency Degrades Anderson Bridge Accuracy](../claims/low-audio-frequency-degrades-anderson-bridge-accuracy.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- P. Arun, Kuldeep Kumar & Mamta. (2008). Considerations for Anderson-Bridge Experiment. https://arxiv.org/abs/0804.3932v1
