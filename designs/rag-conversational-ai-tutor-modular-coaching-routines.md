---
type: design
id: rag-conversational-ai-tutor-modular-coaching-routines
title: Retrieval-augmented Conversational AI Tutor with modular GROW-aligned coaching routines
description: "The Conversational AI Tutor is a retrieval-grounded conversational module built on GPT-4.1 with a RAG layer that anchors each response in the learner's own multimodal records (transcripts, BARS scores, emotion descrip..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: hung-yue-suen-and-kuo-en-hung-2026
    resource: "https://doi.org/10.1109/TLT.2026.3693864"
    title: "Hung-Yue Suen and Kuo-En Hung. (2026). An Interpretable Closed-Loop Intelligent Tutoring System for Multimodal Affective Feedback in Asynchronous Presentation Training. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2026.3693864"
    author: Hung-Yue Suen and Kuo-En Hung
---

# Retrieval-augmented Conversational AI Tutor with modular GROW-aligned coaching routines

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The Conversational AI Tutor is a retrieval-grounded conversational module built on GPT-4.1 with a RAG layer that anchors each response in the learner's own multimodal records (transcripts, BARS scores, emotion descriptors, feature summaries) and maintains records across submissions for longitudinal reflection. The tutor implements three modular routines—performance summarization, strength and weakness highlighting, and translation of analytic indicators into learner-facing concepts—with phrasing drawn from a curated library of expert coaching aligned to the BARS rubric and the GROW model (Goals, Reality, Options, Will).

## Design Implications

### Context
#### Requirements
- Verifiable learner records to retrieve; modular routine specifications with fixed instructional goals, required evidence fields, and output schemas to reduce stylistic drift
#### Constraints
- The RAG layer restricts generation to retrieved sources from the learner's own records, minimizing unconstrained free-form output

### Target Learners
- adult learners in self-directed online presentation practice

### Learning Goals
- interpreting analytic feedback and planning concrete delivery improvements

### Claims
- [Closed Loop Three Layer Interpretable Its Architecture](closed-loop-three-layer-interpretable-its-architecture.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Hung-Yue Suen and Kuo-En Hung. (2026). An Interpretable Closed-Loop Intelligent Tutoring System for Multimodal Affective Feedback in Asynchronous Presentation Training. IEEE Transactions on Learning Technologies. https://doi.org/10.1109/TLT.2026.3693864
