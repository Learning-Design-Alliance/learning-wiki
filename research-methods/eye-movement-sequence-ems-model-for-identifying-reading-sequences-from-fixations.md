---
type: research-method
id: eye-movement-sequence-ems-model-for-identifying-reading-sequences-from-fixations
title: Eye Movement Sequence (EMS) model for identifying reading sequences from fixations
description: The EMS model is an algorithm the authors developed for an earlier study to identify reading sequences from eye-tracking fixation data over look zones.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-18
---

# Eye Movement Sequence (EMS) model for identifying reading sequences from fixations

> **Research Method** · [All research methods](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The EMS model is an algorithm the authors developed for an earlier study to identify reading sequences from eye-tracking fixation data over look zones. It scores a sequence after each fixation, updating with the maximum of the current score and fixation duration when the next fixation is compatible, and subtracting a constant times the fixation duration when it deviates; if the score becomes negative the sequence terminates. In this study a constant C of 2.0 was used, meaning an out-of-sequence fixation could be at most half the longest in-sequence fixation, and minimally three subsequent row or column look zones had to be present to count as a sequence.

## Accounts
<!-- How each source describes or uses the method -->
- **Eye Movement Sequence (EMS) model for identifying reading sequences from fixations**: The EMS model is an algorithm the authors developed for an earlier study to identify reading sequences from eye-tracking fixation data over look zones. It scores a sequence after each fixation, updating with the maximum of the current score and fixation duration when the next fixation is compatible, and subtracting a constant times the fixation duration when it deviates; if the score becomes negative the sequence terminates. In this study a constant C of 2.0 was used, meaning an out-of-sequence fixation could be at most half the longest in-sequence fixation, and minimally three subsequent row or column look zones had to be present to count as a sequence. (Jan van der Meij et al. (2017))

### Claims
- [Reading order in matrix diagrams followed the header content (types) rather than arrow orientation](../claims/header-content-guides-reading-order-over-arrows.md) [+M]
- [Arrows did not guide initial reading behavior in matrix diagrams with two nominal headers](../claims/arrows-not-guide-initial-reading-matrix-diagrams.md) [+M]

## Related Research Methods
-

## Key Sources
- Jan van der Meij, Marije van Amelsvoort, Anjo Anjewierden. (2017). How design guides learning from matrix diagrams. Instructional Science. https://doi.org/10.1007/s11251-017-9425-1
