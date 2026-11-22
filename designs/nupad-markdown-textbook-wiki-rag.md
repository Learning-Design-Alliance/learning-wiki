---
type: design
id: nupad-markdown-textbook-wiki-rag
title: Markdown textbook with Wiki RAG and custom structural tags
description: The course material is rewritten as interlinked Markdown files following a Wiki RAG architecture, replacing PDFs whose parsing the article says suffers severe degradation.
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-21
sources:
  - id: chong-qi-2026
    resource: "https://arxiv.org/abs/2609.36930"
    title: "Chong Qi. (2026). NuPaD: A Generative AI Framework for Fostering Deep Learning in Subatomic Physics. arXiv. https://arxiv.org/abs/2609.36930"
    author: Chong Qi
---

# Markdown textbook with Wiki RAG and custom structural tags

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The course material is rewritten as interlinked Markdown files following a Wiki RAG architecture, replacing PDFs whose parsing the article says suffers severe degradation. Custom tags give each block a pedagogical role: "The<concept>tag defines a core qualitative model, term, or physical quantity, annotated with a unique identifier and a minimum student level", alongside <derivation>, <checkpoint>, <prediction>, <misconception>, and <exercise> tags. A retrieved <derivation> triggers procedural questioning, a <checkpoint> triggers pause-and-probe, and a <misconception> triggers corrective debugging.

## Design Implications

### Context
#### Requirements
- Chapters written as separate Markdown files with frontmatter declaring Intended Learning Outcomes, key ideas, and prerequisites
#### Constraints
- The article notes PDF ingestion degrades logical structure, motivating the Markdown-native format

### Target Learners
- graduate subatomic physics students across three self-declared levels

### Learning Goals
- retrieval of pedagogically contextualized course content during tutoring

### Claims
- 

## Related Designs

- [NuPaD framework: three coupled components transforming GenAI into an inquiry-driven tutor](nupad-framework.md)
- [GraphRAG textbook knowledge retrieval for grounded tutoring](graphrag-textbook-retrieval-math-tutor.md)
- [RAG-encoded textbook Slackbot for course Q&A](rag-textbook-slackbot-astro17.md)
- [Retrieval-augmented generative AI learning platform for construction education](rag-generative-ai-platform-construction-education.md)
- [Offline RAG-plus-SLM architecture for an accessible AI tutor](offline-rag-slm-tutor-architecture.md)

## Examples
-

## Key Sources
- Chong Qi. (2026). NuPaD: A Generative AI Framework for Fostering Deep Learning in Subatomic Physics. arXiv. https://arxiv.org/abs/2609.36930
