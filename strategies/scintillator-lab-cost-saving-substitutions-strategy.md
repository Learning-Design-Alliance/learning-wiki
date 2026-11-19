---
type: strategy
id: scintillator-lab-cost-saving-substitutions-strategy
title: "Cost-saving equipment substitutions with stated performance tradeoffs: EJ-309, plastic scintillators, organic glass, SiPMs, and lower-cost digitizers"
description: "The article states that \"The equipment used for this laboratory may be substituted for lower-cost alternatives.\" EJ-309 and plastic scintillators are capable for multiplicity counting but lack trans-stilbene's low-ene..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: flynn-b-darby-2023
    resource: "https://arxiv.org/abs/2308.06282"
    title: "Flynn B. Darby, Michael Y. Hua, Oskari V. Pakari, Shaun D. Clarke, and Sara A. Pozzi. (2023). Multiplicity counting using organic scintillators to distinguish neutron sources: An advanced teaching laboratory. https://arxiv.org/abs/2308.06282"
    author: Flynn B. Darby, Michael Y. Hua, Oskari V. Pakari, Shaun D. Clarke, and Sara A. Pozzi
---

# Cost-saving equipment substitutions with stated performance tradeoffs: EJ-309, plastic scintillators, organic glass, SiPMs, and lower-cost digitizers

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article states that "The equipment used for this laboratory may be substituted for lower-cost alternatives." EJ-309 and plastic scintillators are capable for multiplicity counting but lack trans-stilbene's low-energy PSD capability, requiring higher thresholds and longer measurement times for the same statistics. Organic glass is a promising untested low-cost alternative with comparable timing precision to trans-stilbene but worse PSD. Photomultiplier tubes may be replaced by silicon photomultipliers at potentially lower cost, and the digitizer and high-voltage units by cheaper units at the cost of ease of use and PSD fidelity.

## Design Implications

### Context
#### Requirements
- Higher measurement light-output thresholds when using scintillators with worse low-energy PSD, which require longer measurement times to achieve the same statistics
#### Constraints
- A cheaper, lower-frequency (less than 500 MHz) digitizer comes at a loss of PSD fidelity and pulse timing precision, and lower-cost electronics lose built-in compatibility with routinely maintained software like CoMPASS

### Target Learners
- nuclear engineering and physics students in resource-constrained instructional laboratories

### Target Learning Goals
- neutron multiplicity counting
- pulse-shape discrimination

## Related Strategies

- [Extension laboratories: PSD figure-of-merit optimization, neutron time-of-flight, cross-correlation, and coincidence anisotropy measurements](scintillator-lab-extension-experiments-strategy.md)

## Examples
-

## Key Sources
- Flynn B. Darby, Michael Y. Hua, Oskari V. Pakari, Shaun D. Clarke, and Sara A. Pozzi. (2023). Multiplicity counting using organic scintillators to distinguish neutron sources: An advanced teaching laboratory. https://arxiv.org/abs/2308.06282
