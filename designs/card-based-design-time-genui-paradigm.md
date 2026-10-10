---
type: design
id: card-based-design-time-genui-paradigm
title: Card-based design-time GenUI paradigm for educational content
description: The paper proposes organizing educational content as bounded, modality-agnostic semantic cards whose learning objective is encoded separately from any interface representation.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: seyed-parsa-neshaei-2026
    resource: "https://arxiv.org/abs/2606.15902"
    title: "Seyed Parsa Neshaei, Abhinand Shibu, and Fatma Betül Güres. (2026). The Missing Layer: Why EdTech Needs Design-Time Generative UI, Not Just Runtime Personalization. https://arxiv.org/abs/2606.15902"
    author: Seyed Parsa Neshaei, Abhinand Shibu, and Fatma Betül Güres
---

# Card-based design-time GenUI paradigm for educational content

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 theoretical), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The paper proposes organizing educational content as bounded, modality-agnostic semantic cards whose learning objective is encoded separately from any interface representation. At authoring time, a GenAI engine produces a defined set of representation variants (interactive, audio, simplified text, low-bandwidth), which the instructor reviews before delivery; approved variants are stored in repositories for deployment without runtime generation. The authors state this "embeds Universal Design for Learning principles into the authoring workflow, and removed per-learner inference costs." The card boundary is presented as what makes generation tractable and keeps a domain-knowledgeable human in the loop.

## Design Implications

### Context
#### Requirements
- Educators define bounded learning units as cards with explicit learning objectives and content fields before any representation is generated
- Generated representations are reviewed and approved by the instructor before learners see them
#### Constraints
- The assumption that card variants are interchangeable from a learning perspective is stated by the authors as an unvalidated empirical claim
- Client may still invoke runtime AI for selected functions such as answering questions or feedback

### Target Learners
- Diverse learners including those needing audio-first, simplified-text, interactive, or low-bandwidth representations

### Learning Goals
- Preserving the intended learning objective across multiple interface representations

### Claims
- [Runtime Genui Too Late Costly Inequitable](../claims/runtime-genui-too-late-costly-inequitable.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Seyed Parsa Neshaei, Abhinand Shibu, and Fatma Betül Güres. (2026). The Missing Layer: Why EdTech Needs Design-Time Generative UI, Not Just Runtime Personalization. https://arxiv.org/abs/2606.15902
