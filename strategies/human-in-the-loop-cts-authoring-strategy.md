---
type: strategy
id: human-in-the-loop-cts-authoring-strategy
title: Add human-in-the-loop capabilities so practitioners can edit or choose among LLM-generated tutoring script components
description: The authors recommend extending the fully automated LLM authoring workflow with human-in-the-loop capabilities so that educators participate in instructional design.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: robin-schmucker-2023
    resource: "https://arxiv.org/abs/2310.01420"
    title: "Robin Schmucker, Meng Xia, Amos Azaria, Tom Mitchell. (2023). Ruffle&Riley: Towards the Automated Induction of Conversational Tutoring Systems. NeurIPS'23 Workshop on Generative AI for Education (GAIED). https://arxiv.org/abs/2310.01420"
    author: Robin Schmucker, Meng Xia, Amos Azaria, Tom Mitchell
---

# Add human-in-the-loop capabilities so practitioners can edit or choose among LLM-generated tutoring script components

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The authors recommend extending the fully automated LLM authoring workflow with human-in-the-loop capabilities so that educators participate in instructional design. They write that "We want to enable general educational practitioners to get involved in the instruction design process", for example by letting teachers include their own review questions, insert expectations for students' answers, or choose among different candidates the LLM provides. They argue that including human domain experts can further improve trustworthiness and content quality.

## Design Implications

### Context
#### Requirements
- An LLM that can provide multiple candidate script components for practitioners to choose among or edit
#### Constraints
- The present study's system was fully automated; human-in-the-loop capabilities are a stated future direction, not an evaluated feature

### Target Learners
- teachers and general educational practitioners authoring conversational tutoring content

### Target Learning Goals
- improving trustworthiness and content quality of automatically induced tutoring scripts

## Claims

- [Across 28 project contexts, human-in-the-loop and independent peer review identified no conceptual or mathematical hallucinations, and Python visualization scripts executed without compilation errors on the zero-shot attempt.](../claims/no-conceptual-hallucinations-28-contexts.md) [+W]

## Related Strategies

- [Extend educational LLM benchmarks with broader item formats, human-in-the-loop item curation, and multi-turn evidence-based feedback measures](extend-educational-llm-benchmarks-human-in-loop-multiturn.md)
- [Instructors should review and edit all AI-generated feedback before sending it to students](human-in-the-loop-review-of-ai-feedback.md)
- [Human-in-the-loop quality control for AI-generated educational content](human-in-the-loop-ai-content-quality-control.md)
- [Design GenAI-in-the-loop XR tools with editable components, reproducible generation, continuity with existing artifacts, and shared-attention cues](genai-xr-tool-design-strategy.md)
- [Embed the tool in the subject's workflow and design feed-forward prompts, symbolic-answer handling, and progress tracking before full release](embed-genai-practice-tool-in-subject-workflow.md)

## Examples
-

## Key Sources
- Robin Schmucker, Meng Xia, Amos Azaria, Tom Mitchell. (2023). Ruffle&Riley: Towards the Automated Induction of Conversational Tutoring Systems. NeurIPS'23 Workshop on Generative AI for Education (GAIED). https://arxiv.org/abs/2310.01420
