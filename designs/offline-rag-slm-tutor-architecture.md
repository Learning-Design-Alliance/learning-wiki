---
type: design
id: offline-rag-slm-tutor-architecture
title: Offline RAG-plus-SLM architecture for an accessible AI tutor
description: The article describes a closed-system AI tutor composed of a RAG pipeline and a small language model.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: juan-segundo-hevia-2025
    resource: "https://arxiv.org/abs/2510.06255"
    title: "Juan Segundo Hevia, Facundo Arredondo, Vishesh Kumar. (2025). Towards an Efficient, Customizable, and Accessible AI Tutor. https://arxiv.org/abs/2510.06255"
    author: Juan Segundo Hevia, Facundo Arredondo, Vishesh Kumar
---

# Offline RAG-plus-SLM architecture for an accessible AI tutor

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article describes a closed-system AI tutor composed of a RAG pipeline and a small language model. The RAG component "ensures factuality by managing knowledge retrieval from a local corpus of the user's choice, using cosine similarity", while the SLM delivers conversational generation. The pipeline is designed per-coursework, grounded in a pre-built vectorized textbook database (OpenStax biology, 300-token chunks, k=2), so all heavy processing happens offline in preprocessing and the tutor runs without internet connectivity.

## Design Implications

### Context
#### Requirements
- A pre-processed vectorized document database built from domain textbooks, using an embedding model and cosine distance to retrieve the K closest text fragments
#### Constraints
- The SLM must remain small and low-capacity for constrained deployment, which the article says creates a trade-off between context awareness and computational cost

### Target Learners
- students in low-resource or internet-limited settings studying college or high-school biology

### Learning Goals
- answering factual questions about coursework content

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Juan Segundo Hevia, Facundo Arredondo, Vishesh Kumar. (2025). Towards an Efficient, Customizable, and Accessible AI Tutor. https://arxiv.org/abs/2510.06255
