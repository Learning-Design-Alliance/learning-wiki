---
type: strategy
id: llm-preconception-prompting-pilot-testing
title: Use theory-guided preconception prompting of ChatGPT to generate synthetic field-testing data for concept inventories
description: "The strategy is to prompt a generative LLM such as ChatGPT with established, theory-derived student preconceptions (e.g., \"Respond to the following questions from the perspective of a person who has the preconception..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: fabian-kieser-2023
    resource: "https://arxiv.org/abs/2307.14475"
    title: "Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann. (2023). Educational data augmentation in physics education research using ChatGPT. https://arxiv.org/abs/2307.14475"
    author: Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann
---

# Use theory-guided preconception prompting of ChatGPT to generate synthetic field-testing data for concept inventories

> **Strategy** · [All strategies](index.md)
> **Evidence** · 6 claims (4 for, 2 mixed) · 2 studies (2 design), `q2` · 0 of 2 report an effect size · 6 claims rest on one study

## Description
The strategy is to prompt a generative LLM such as ChatGPT with established, theory-derived student preconceptions (e.g., "Respond to the following questions from the perspective of a person who has the preconception that ...") to synthesize response sets for pilot-testing assessments. The article showed this yields "meaningful variability in the data set", unlike cohort prompting. It recommends this for researchers pilot-testing instruments and for practitioners designing classroom or state-wide exams.

## Design Implications

### Context
#### Requirements
- Prompts must be grounded in established theory about learner preconceptions, since the article found theory-based, specific prompting yielded most variance
#### Constraints
- Users currently have to outsource their instruments to a private company
- Real students may hold conceptions not included in the theoretically derived set of preconceptions
- Generalization to other concept inventories (climate change, electricity, biological evolution) requires further research

### Target Learners
- physics education researchers
- practitioners designing classroom exams
- policy agents designing state-wide exams

### Target Learning Goals
- valid assessment of students' conceptual understanding of Newtonian mechanics

## Claims

- [ChatGPT based on GPT-4 solves the FCI accurately, scoring on average 83% correct](../claims/chatgpt-gpt4-solves-fci-accurately.md) [+W]
- [ChatGPT correctly reasons within two validated preconceptions (centrifugal force and impetus) when prompted to respond as-if a student held them](../claims/chatgpt-reasons-within-preconceptions.md) [+W]
- [Prompting ChatGPT to respond as-if from different cohorts yields no differences in FCI response distributions](../claims/cohort-prompting-no-response-differences.md) [~W]
- [Figure-to-text transcription of FCI items may cause difficulties for ChatGPT, with eleven items unsolved in every run](../claims/figure-transcription-hinders-chatgpt-fci.md) [~W]
- [Prompting ChatGPT with specific physics preconceptions introduces much response variance that approximates real student FCI distributions](../claims/preconception-prompting-yields-variance.md) [+W]
- [ChatGPT's FCI errors include impetus-type preconceptions shared with beginning physics students](../claims/chatgpt-impetus-preconception-errors.md) [+W]

## Related Strategies

- [Use rubric-guided multiagent LLM simulation workflows for scalable, auditable psychotherapy practice and formative feedback](multiagent-llm-simulation-psychotherapy-training-strategy.md)
- [Run a controlled comparison of traditional cybersecurity instruction versus ChatGPT-augmented exploration, assessed with the Cybersecurity Concept Inventory](proposed-cci-chatgpt-controlled-comparison.md)

## Examples
-

## Key Sources
- Fabian Kieser, Peter Wulff, Jochen Kuhn, and Stefan Küchemann. (2023). Educational data augmentation in physics education research using ChatGPT. https://arxiv.org/abs/2307.14475
