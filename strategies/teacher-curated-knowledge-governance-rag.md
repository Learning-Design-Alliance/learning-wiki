---
type: strategy
id: teacher-curated-knowledge-governance-rag
title: Govern tutor knowledge through teacher-curated document corpora with RAG and document-driven adaptation
description: The Teacher Interaction Layer lets educators delimit what the virtual tutor may know by curating an approved corpus.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: lorenzo-stacchio-2026
    resource: "https://arxiv.org/abs/2606.30662"
    title: "Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni. (2026). ELEVATE: Designing Human-Centered GenAI Virtual Tutors for Scalable and Inclusive Education. arXiv preprint. https://arxiv.org/abs/2606.30662"
    author: Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni
---

# Govern tutor knowledge through teacher-curated document corpora with RAG and document-driven adaptation

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The Teacher Interaction Layer lets educators delimit what the virtual tutor may know by curating an approved corpus. "Educators can curate a corpus of materials (e.g., textbook excerpts, lecture notes, worksheets, institutional policies, or open educational resources) that delimit the knowledge boundary of the system." These materials ground responses through retrieval-augmented generation at query time or support lightweight fine-tuning where policy permits, aligning explanations with the exact terminology and sequencing used in class.

## Design Implications

### Context
#### Requirements
- Teacher time to curate and maintain the document corpus
- Institutional policy permitting the chosen adaptation mechanism
- Tracking of corpus versions and update workflows for auditability
#### Constraints
- Fine-tuning or continual adaptation is described as feasible only when permitted by institutional policy

### Target Learners
- students in institutionally governed school deployments

### Target Learning Goals
- factual consistency and curriculum-aligned explanations grounded in approved sources

### Affordances
- [Elevate Three Stratum Genai Avatar Tutor Framework](../products/elevate-efficient-llm-education-with-virtual-avatar-teaching-engine.md)

## Related Strategies

- [Curating Resources](curating_resources.md)
- [Adopt AI incrementally in waves from simple to complex tasks, on free-tier tools, with mandatory multi-step human review before any document is issued](incremental-free-tier-ai-adoption-with-triple-review.md)

## Examples
-

## Key Sources
- Lorenzo Stacchio, Michele Giordano, Daniele Berardini, Primo Zingaretti, Emanuele Frontoni. (2026). ELEVATE: Designing Human-Centered GenAI Virtual Tutors for Scalable and Inclusive Education. arXiv preprint. https://arxiv.org/abs/2606.30662
