---
type: strategy
id: refine-llm-prompts-rag-reduce-verbosity
title: Refine LLM feedback prompts and adopt RAG to reduce verbosity and align feedback with course content
description: "As future work, the authors propose refining the prompt used to generate combined feedback and adopting Retrieval-Augmented Generation (RAG) techniques with a twofold aim: \"improving focused attention (e.g., by reduci..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: letteri-2025
    resource: "https://doi.org/10.1007/s40593-025-00492-8"
    title: "Letteri, I. & Vittorini, P. (2025). Enhancing Student Feedback in Data Science Education: Harnessing the Power of AI-Generated Approaches. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00492-8"
    author: "Letteri, I. & Vittorini, P"
---

# Refine LLM feedback prompts and adopt RAG to reduce verbosity and align feedback with course content

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 mixed) · 1 study (1 theoretical), `q1` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
As future work, the authors propose refining the prompt used to generate combined feedback and adopting Retrieval-Augmented Generation (RAG) techniques with a twofold aim: "improving focused attention (e.g., by reducing verbosity)" and "better aligning the feedback with the course content", the latter to tackle students' reports that the LLM suggested commands not covered in lectures (e.g., rowSums instead of the '+' operator).

## Design Implications

### Context
#### Requirements
- Access to an LLM-based feedback pipeline whose prompts can be engineered, plus a retrieval mechanism (RAG) grounded in course materials.
#### Constraints
- The article frames this as future research; the current study found the combined feedback required additional cognitive effort from students.

### Target Learners
- Higher education students in data science courses

### Target Learning Goals
- Statistical analysis and R programming skills practiced through formative assessment exercises

## Claims

- [Retrieval-augmented generation reduces but does not eliminate hallucinations in AI-assisted verification](../claims/rag-reduces-not-eliminates-hallucinations.md) [~W]

## Related Strategies

- [Planned enhancements: multi-turn conversational follow-up, RAG-based personalization, and feedback analytics for AI-assisted instruction](planned-ai-instruction-enhancements-rag-multiturn.md)
- [Upgrade retrieval to Agentic RAG and adopt context-aware emotive narration to reduce cognitive load](agentic-rag-and-context-aware-audio-upgrades.md)
- [Technical integration of GSR knowledge via onboarding system prompts, knowledge graphs, retrieval-augmented generation, and a control module](gsr-knowledge-technical-integration-strategies.md)

## Examples
-

## Key Sources
- Letteri, I. & Vittorini, P. (2025). Enhancing Student Feedback in Data Science Education: Harnessing the Power of AI-Generated Approaches. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-025-00492-8
