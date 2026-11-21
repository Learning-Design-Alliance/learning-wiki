---
type: strategy
id: iterative-training-manual-refinement-strategy
title: "Iteratively develop and refine a pedagogical Training Manual by observing the tutor's actual behavior in preliminary tests"
description: "The tutor's conversational strategies and pedagogical constraints are defined in a 'Training Manual' provided as a source document to the AI."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: eugenio-tufino-2025
    resource: "https://arxiv.org/abs/2504.09720"
    title: "Eugenio Tufino. (2025). NotebookLM as a Socratic physics tutor: Design and preliminary observations of a RAG-based tool. arXiv preprint. https://arxiv.org/abs/2504.09720"
    author: Eugenio Tufino
---

# Iteratively develop and refine a pedagogical Training Manual by observing the tutor's actual behavior in preliminary tests

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 3 claims rest on one study

## Description
The tutor's conversational strategies and pedagogical constraints are defined in a 'Training Manual' provided as a source document to the AI. The manual "was developed iteratively": initial versions were refined after observing NotebookLM's behavior in preliminary tests, adding stricter instructions to counteract a tendency to offer direct solutions and an adaptive scaffolding rule added after observing user frustration. The initial and updated versions are released as Supplementary Material to document the process.

## Design Implications

### Context
#### Requirements
- Access to the platform's source-document mechanism so the manual can be supplied to the AI
- Preliminary test sessions in which the tutor's actual behavior can be observed
#### Constraints
- Adherence to the manual depends on the underlying language model's ability to prioritize instructional phrases retrieved from source documents

### Target Learners
- educators implementing grounded AI tutors in their own teaching contexts

### Target Learning Goals
- configuring AI tutor behavior for guided, questioning-based dialogue

## Claims

- [A NotebookLM-based tutor configured with a Training Manual and teacher-curated sources can facilitate Socratic dialogue for conceptual physics problems](../claims/notebooklm-socratic-tutor-facilitates-dialogue.md) [+W]
- [Withholding direct answers frustrated some pre-service teachers, while an updated tutor with adaptive scaffolding received an overwhelmingly positive reception from approximately 95 in-service teachers](../claims/socratic-tutor-motivation-frustration-reception.md) [+W]
- [A strict confidentiality protocol in the Training Manual prevented the tutor from revealing its operational instructions when prompted during testing](../claims/training-manual-confidentiality-protocol-adherence.md) [+W]

## Related Strategies

- [Develop tutorials iteratively through one-on-one think-aloud interviews and classroom refinement](quilt-iterative-development-interviews.md)
- [Teachers iteratively refine LLM-simulated student ideas with classroom context before instructional use](iterative-teacher-llm-refinement-strategy.md)
- [Generative-AI-assisted content creation with domain-expert validation for adaptive tutoring systems](genai-assisted-content-creation-expert-validation.md)

## Examples
-

## Key Sources
- Eugenio Tufino. (2025). NotebookLM as a Socratic physics tutor: Design and preliminary observations of a RAG-based tool. arXiv preprint. https://arxiv.org/abs/2504.09720
