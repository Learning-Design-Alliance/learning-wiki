---
type: design
id: gemini-gem-socratic-physics-tutor
title: Custom Socratic physics tutor built as a Google Gemini Gem
description: "A customized AI tutor implemented with Google's Gemini Gems feature, configured through an \"Instructions\" panel defining the AI's role and persona, a \"Knowledge\" section for uploading up to 10 grounding documents, and..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: eugenio-tufino-2025
    resource: "https://arxiv.org/abs/2507.05795"
    title: "Eugenio Tufino, Bor Gregorcic. (2025). Creating a customisable Socratic AI physics tutor. https://arxiv.org/abs/2507.05795"
    author: Eugenio Tufino, Bor Gregorcic
---

# Custom Socratic physics tutor built as a Google Gemini Gem

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q1` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A customized AI tutor implemented with Google's Gemini Gems feature, configured through an "Instructions" panel defining the AI's role and persona, a "Knowledge" section for uploading up to 10 grounding documents, and a preview window for iterative refinement. Students engage with the final tutor directly through the Gemini smartphone app. The paper demonstrates the tutor on a dynamics force-diagram task (using a Knowledge file with two-subscript notation rules) and an electromagnetic induction task using pre-trained knowledge alone.

## Design Implications

### Context
#### Requirements
- Instructors must share Knowledge files separately (e.g., via Google Docs) when distributing the Gem, since public-link sharing excludes uploaded Knowledge files, and students upload them to their own instance
#### Constraints
- Free educational access to the 2.5 Pro model may have usage caps preventing extended interactions
- Consumer tools may store submitted materials and conversation content and use them for model training

### Target Learners
- physics students using algebra-based coursework

### Learning Goals
- force-diagram construction with course-specific notation
- conceptual and quantitative reasoning in electromagnetism

### Claims
- [Gem Multimodal Force Diagram Notation Feedback](../claims/gem-multimodal-force-diagram-notation-feedback.md) [+M]
- [Gem Socratic Electromagnetic Induction Reasoning](../claims/gem-socratic-electromagnetic-induction-reasoning.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Eugenio Tufino, Bor Gregorcic. (2025). Creating a customisable Socratic AI physics tutor. https://arxiv.org/abs/2507.05795
