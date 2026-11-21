---
type: design
id: notebooklm-collaborative-ai-physics-tutor
title: NotebookLM-based collaborative AI physics tutor with chat-only shared interface and two operating modes
description: "A tutor implemented on NotebookLM, a RAG-based platform powered by Google's Gemini models, in which the AI guides students through conceptual physics problems by posing targeted questions rather than giving direct ans..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: eugenio-tufino-2025
    resource: "https://arxiv.org/abs/2504.09720"
    title: "Eugenio Tufino. (2025). NotebookLM as a Socratic physics tutor: Design and preliminary observations of a RAG-based tool. arXiv preprint. https://arxiv.org/abs/2504.09720"
    author: Eugenio Tufino
---

# NotebookLM-based collaborative AI physics tutor with chat-only shared interface and two operating modes

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A tutor implemented on NotebookLM, a RAG-based platform powered by Google's Gemini models, in which the AI guides students through conceptual physics problems by posing targeted questions rather than giving direct answers. It operates in two modes: with curated solutions as sources it "primarily uses guiding questions derived from Socratic/collaborative principles", and without pre-loaded solutions it offers provisional step-by-step guidance from the underlying model. NotebookLM Plus enables sharing a secure, chat-only interface that hides the underlying source documents from students.

## Design Implications

### Context
#### Requirements
- A NotebookLM Plus subscription to share a chat-only interface with students
- Teacher-curated source documents including the Training Manual and selected problems
- Students need a Google account for access
#### Constraints
- Chat-only interaction limits support for pedagogies requiring dynamic visual collaboration, such as the ISLE framework
- NotebookLM currently does not render LaTeX mathematics
- Responses for problems without curated guidance may occasionally contain inaccuracies

### Target Learners
- physics students in high school and university contexts

### Learning Goals
- conceptual understanding of physics through guided problem-solving

### Claims
- [Notebooklm Socratic Tutor Facilitates Dialogue](../claims/notebooklm-socratic-tutor-facilitates-dialogue.md) [+M]
- [Training Manual Confidentiality Protocol Adherence](../claims/training-manual-confidentiality-protocol-adherence.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Eugenio Tufino. (2025). NotebookLM as a Socratic physics tutor: Design and preliminary observations of a RAG-based tool. arXiv preprint. https://arxiv.org/abs/2504.09720
