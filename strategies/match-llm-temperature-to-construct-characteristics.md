---
type: strategy
id: match-llm-temperature-to-construct-characteristics
title: Match LLM temperature settings to construct characteristics when coding educational dialogue
description: The article recommends calibrating LLM sampling parameters to the psychological construct being coded rather than applying one configuration universally.
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-08
sources:
  - id: ober-2026
    resource: "https://doi.org/10.17605/osf.io/s85ck"
    title: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck"
    author: "Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F"
---

# Match LLM temperature settings to construct characteristics when coding educational dialogue

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article recommends calibrating LLM sampling parameters to the psychological construct being coded rather than applying one configuration universally. Its results suggest "constructs with moderate theoretical coherence benefited from higher temperatures, while well-defined constructs required deterministic settings," and that low-clarity constructs may need higher temperatures to capture varied expressions. Without systematic frameworks for matching parameter configurations to construct types, researchers risk settings that bias results toward certain constructs while undermining the reliability of others.

## Design Implications

### Context
#### Requirements
- Systematic evaluation to ensure methodological choices produce outcomes likely to be reliable and interpretable by researchers; construct definitions and prompts refined with clear operational definitions and examples of evidence
#### Constraints
- Even setting temperature to 0 does not guarantee perfect reproducibility, as model updates, non-deterministic software elements, and API-specific configurations can still produce variations across sessions and platforms

### Target Learners
- middle school students classified as English learners

### Target Learning Goals
- reliable automated coding of persistence and related psychological constructs from student dialogue

### Affordances
- [Construct Evaluation Framework Measurement Dimensions](../theories/construct-evaluation-framework-measurement-dimensions.md)

## Related Strategies

- [Use structured multi-stage prompts with clearly defined constructs when eliciting LLM topic labels for qualitative coding](structured-prompts-clear-construct-definitions-llm-labeling.md)

## Examples
-

## Key Sources
- Ober, T. M., Zhang, S., Zapata-Rivera, D., Schroeder, N. L., & Botelho, A. F. (2026). Using LLMs to Identify Indicators of Persistence from Students' Dialogues with a Pedagogical Agent. Journal of Educational Data Mining, Volume 18, No 1. https://doi.org/10.17605/osf.io/s85ck
