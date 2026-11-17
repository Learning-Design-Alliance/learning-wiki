---
type: design
id: two-stage-op-amp-troubleshooting-interview-task
title: Two-stage op-amp troubleshooting task with two intentional flaws
description: The task is a cascading amplifier circuit with a non-inverting stage of gain 2 and an inverting stage of gain -10, giving an overall output twenty times larger than and 180 degrees out of phase with the input.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-17
sources:
  - id: kevin-l-van-de-bogart-2015
    resource: "https://arxiv.org/abs/1503.07056"
    title: "Kevin L. Van De Bogart, Dimitri R. Dounas-Frazer, H. J. Lewandowski, and MacKenzie R. Stetzer. (2015). The role of metacognition in troubleshooting: an example from electronics. https://arxiv.org/abs/1503.07056"
    author: Kevin L. Van De Bogart, Dimitri R. Dounas-Frazer, H. J. Lewandowski, and MacKenzie R. Stetzer
---

# Two-stage op-amp troubleshooting task with two intentional flaws

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The task is a cascading amplifier circuit with a non-inverting stage of gain 2 and an inverting stage of gain -10, giving an overall output twenty times larger than and 180 degrees out of phase with the input. "The physical circuit given to students was constructed with two distinct, intentional flaws": a 100 ohm resistor R3 in place of the nominal 1 kohm, making stage 2's gain ten times larger than expected, and a damaged stage-2 op-amp whose output was constant at approximately -15 V regardless of input. Students received a schematic without stages or faults identified and were told to treat the circuit as built by peers and malfunctioning.

## Design Implications

### Context
#### Requirements
- The flaws must leave stage 1 unaffected so that a split-half troubleshooting strategy can be used, and the two distinct errors must require multiple rounds of troubleshooting
#### Constraints
- The specific combination of errors was chosen because neither impacted stage 1 operation, allowing the problem space to be reduced; the second fault was anticipated to be harder to identify because the resistor flaw differed visually

### Target Learners
- junior-level undergraduate electronics students working in pairs

### Learning Goals
- diagnosing and repairing malfunctioning op-amp circuits
- iterative and logical troubleshooting

### Claims
- Paired Think Aloud Op Amp Troubleshooting Interviews [+W]

## Related Designs
- 

## Examples
-

## Key Sources
- Kevin L. Van De Bogart, Dimitri R. Dounas-Frazer, H. J. Lewandowski, and MacKenzie R. Stetzer. (2015). The role of metacognition in troubleshooting: an example from electronics. https://arxiv.org/abs/1503.07056
