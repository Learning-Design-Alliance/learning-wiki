---
type: strategy
id: vlm-role-prompting-dast-auto-scoring-strategy
title: Use role-prompted VLMs with the DAST-C rubric to automatically score drawn images and provide scoring rationales for classroom use
description: "The article demonstrates a scoring pipeline: assign the machine the role of \"a unbiased science education researcher that score a response to the draw-a-scientist test (DAST)\", then require analysis of each input imag..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-23
sources:
  - id: gyeonggeon-lee-2025
    resource: "https://arxiv.org/abs/2504.19005"
    title: "Gyeonggeon Lee. (2025). Artificial Intelligence Generates Stereotypical Images of Scientists but Can Also Detect Them: A Pilot Study Using the Draw-A-Scientist Test. Version 1 - Last modified: Apr 27, 2025. https://arxiv.org/abs/2504.19005"
    author: Gyeonggeon Lee
---

# Use role-prompted VLMs with the DAST-C rubric to automatically score drawn images and provide scoring rationales for classroom use

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
The article demonstrates a scoring pipeline: assign the machine the role of "a unbiased science education researcher that score a response to the draw-a-scientist test (DAST)", then require analysis of each input image according to the DAST-C checklist instructions. The VLM returns per-feature scores with rationales, which the author says could assist teachers and might be mounted on an interactive digital learning platform to support students in classroom settings.

## Design Implications

### Context
#### Requirements
- Iterative prompt engineering against the scoring rubric and access to a pre-trained vision language model via API
#### Constraints
- Agreement is lower on uncertain features than on concrete ones, and the author plans further prompt engineering to increase MHA

### Target Learners
- science classroom students
- teachers using AI assessment tools

### Target Learning Goals
- assessment of students' images of scientists
- beyond conceptual understandings, more abstract constructs in drawn images

## Claims

- [gpt-4.1-mini can detect stereotypical features in AI-generated scientist images with 79% average human-machine agreement on the same 100 images](../claims/gpt-mini-detects-dast-stereotypes-79-mha.md) [+W]
- [Machine-human agreement on DAST-C features varies widely, from 49-100%, being high for concrete features and low for uncertain ones such as scientist working indoors and middle-aged/elderly appearance](../claims/mha-varies-concrete-vs-uncertain-features.md) [~W]

## Related Strategies

- [Use lightweight task-adapted vision backbones rather than zero-shot multimodal foundation models for rubric-aligned drawing scoring](task-adapted-vit-over-zero-shot-vlm-scoring.md)
- [Use detailed, refined marking schemes within LLM grading prompts to obtain more consistent and precise grading](refined-marking-scheme-llm-grading-strategy.md)

## Examples
-

## Key Sources
- Gyeonggeon Lee. (2025). Artificial Intelligence Generates Stereotypical Images of Scientists but Can Also Detect Them: A Pilot Study Using the Draw-A-Scientist Test. Version 1 - Last modified: Apr 27, 2025. https://arxiv.org/abs/2504.19005
