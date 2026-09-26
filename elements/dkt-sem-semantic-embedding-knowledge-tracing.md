---
type: element
id: dkt-sem-semantic-embedding-knowledge-tracing
title: "DKT-Sem: Deep Knowledge Tracing with Semantic Embeddings"
description: "DKT-Sem is the article's simpler alternative KT method for dialogues, described as a strong baseline."
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: alexander-scarlatos-2024
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
---

# DKT-Sem: Deep Knowledge Tracing with Semantic Embeddings

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
DKT-Sem is the article's simpler alternative KT method for dialogues, described as a strong baseline. The authors "slightly modify the deep KT (DKT) model [46] to use semantic embeddings of the textual content in dialogues": S-BERT embeddings of the tutor turn, student turn and averaged KC embeddings feed an LSTM, and KC masteries are predicted via a bilinear projection onto KC embeddings. It is trained with the same objective as LLMKT.

## Design Implications

### Context
#### Requirements
- Sentence-BERT embeddings (the article uses the all-mpnet-base-v2 model) of tutor turns, student turns and KC descriptions.
- Turn-level correctness labels mapped to a learnable embedding, as in DKT.
#### Constraints
- Its advantage over existing KT methods is smaller on the larger MathDial dataset than on CoMTA.

### Target Learners
- Students in one-on-one math tutoring dialogues with human or LLM-powered tutors (the article uses the CoMTA and MathDial datasets)

### Target Learning Goals
- Estimating student knowledge of math knowledge components (Common Core standards) and predicting student response correctness across dialogue turns

### Affordances
- [Dialogue Knowledge Tracing Framework](../theories/dialogue-knowledge-tracing-framework.md)

## Related Elements
- 

## Examples
-

## Key Sources
- Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490
