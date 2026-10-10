---
type: design
id: transcript-derived-virtual-patient-profiles
title: Transcript-derived patient profiles conditioning virtual patient behavior across seven dimensions
description: "Four anonymized patient profiles (two male, two female) were synthesized with GPT-5.2 from 4–7 real ACT sessions each, which \"averaged 58–92 therapist-patient turn pairs and lasted 38–60 minutes\"."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: pascal-riachi-2026
    resource: "https://arxiv.org/abs/2606.17786"
    title: "Pascal Riachi, Sofie Kamber, Stella Brogna, Andrew Gloster, Rafael Wampfler. (2026). Toward Accessible Psychotherapy Training Using AI-Driven Interactive Patient Avatars. https://arxiv.org/abs/2606.17786"
    author: Pascal Riachi, Sofie Kamber, Stella Brogna, Andrew Gloster, Rafael Wampfler
---

# Transcript-derived patient profiles conditioning virtual patient behavior across seven dimensions

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
Four anonymized patient profiles (two male, two female) were synthesized with GPT-5.2 from 4–7 real ACT sessions each, which "averaged 58–92 therapist-patient turn pairs and lasted 38–60 minutes". A structured prompt extracted stable patterns across seven dimensions (patient overview, core difficulties, values and motivations, emotional and cognitive themes, behavioral patterns, progress trajectory, simulation hooks) and constrained the model to rely only on transcript content and produce anonymized descriptions.

## Design Implications

### Context
#### Requirements
- Real therapy transcripts as source material
- Joint analysis of multiple sessions to capture stable patterns
#### Constraints
- Profiles are anonymized approximations derived only from transcript content

### Target Learners
- Psychotherapists in training

### Learning Goals
- Clinically plausible patient interaction practice

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Pascal Riachi, Sofie Kamber, Stella Brogna, Andrew Gloster, Rafael Wampfler. (2026). Toward Accessible Psychotherapy Training Using AI-Driven Interactive Patient Avatars. https://arxiv.org/abs/2606.17786
