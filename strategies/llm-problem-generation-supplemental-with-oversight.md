---
type: strategy
id: llm-problem-generation-supplemental-with-oversight
title: Use LLM-generated isomorphic problems as supplemental instructional content with expert oversight, targeting distractor logic and narrative depth as future improvements
description: "The article positions reliable problem generation as a step toward an AI-powered tutoring system providing timely, personalized instructional content, while echoing the literature's caution that LLMs should be supplem..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: xian-wu-and-lindim-ismaili-2026
    resource: "https://arxiv.org/abs/2607.13190"
    title: "Xian Wu and Lindim Ismaili. (2026). Reliable isomorphic physics problem generation with large language models. https://arxiv.org/abs/2607.13190"
    author: Xian Wu and Lindim Ismaili
---

# Use LLM-generated isomorphic problems as supplemental instructional content with expert oversight, targeting distractor logic and narrative depth as future improvements

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (3 for, 3 against) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The article positions reliable problem generation as a step toward an AI-powered tutoring system providing timely, personalized instructional content, while echoing the literature's caution that LLMs should be supplemental tools requiring expert oversight. Future work focuses on "preserving distractor logic for MCQs and generating context -rich problems that better match the narrative depth" of originals, and the long-term goal is adapting problems to students' backgrounds, interests, and learning needs.

## Design Implications

### Context
#### Requirements
- Generated problems must be checked against usability criteria such as being solvable as written and free of physics, numerical, typographical, grammatical, and ambiguity errors before direct use.
#### Constraints
- The literature the article cites concludes that excessive dependence on AI-generated assistance may weaken students' critical thinking and independent problem-solving abilities over time.

### Target Learners
- introductory physics students

### Target Learning Goals
- addressing specific misconceptions, strengthening mathematical manipulation skills, and supporting different learning pathways

## Claims

- [The system failed to vary scenarios for abstract-context questions, using a different scenario in only 5% of such cases](../claims/llm-abstract-context-scenario-variation-fails.md) [-W]
- [In a preliminary test, LLM generation of context-rich problems with changed thematic focus was unsatisfactory, replacing surface cover stories rather than redesigning scenarios](../claims/llm-context-rich-problem-generation-unsatisfactory.md) [-W]
- [89% of LLM-generated isomorphic MCQs were rated fully specified and solvable as written, usable without expert revision](../claims/llm-isomorphic-mcq-89-percent-directly-usable.md) [+W]
- [The system did not consistently preserve distractor logic in generated MCQs, with only 59% preserving the logical structure of distractors overall and 47% for abstract-context numerical questions](../claims/llm-mcq-distractor-logic-preservation-weak.md) [-W]
- [Most LLM-generated MCQs from video transcripts met established quality criteria, with 84.05% rated clear, 86.38% containing plausible distractors, and 93.39% directly answerable](../claims/llm-mcq-video-quality-ratings-majority-clear.md) [+W]
- [In a preliminary test, the system generated shared-scenario MCQ sets that preserved the shared-scenario structure of the QMCA](../claims/llm-shared-scenario-mcq-generation-preliminary.md) [+W]

## Related Strategies

- [Subject AI-generated items to trained human expert review, including a technical review and difficulty refinement](human-expert-review-of-ai-mcqs.md)
- [Apply human quality-check supervision before deploying LLM-generated hint content in tutoring systems](human-quality-checks-for-llm-hints.md)
- [Use isomorphic problem sets to prompt students to generate both mathematical and conceptual problems from the same content](isomorphic-sets-for-generated-problems.md)

## Examples
-

## Key Sources
- Xian Wu and Lindim Ismaili. (2026). Reliable isomorphic physics problem generation with large language models. https://arxiv.org/abs/2607.13190
