---
type: element
id: gpt-4o-dialogue-annotation-correctness-and-common-core-kcs
title: GPT-4o Automated Dialogue Annotation with Recursive Common Core Tagging
description: The article annotates each student turn with correctness and KC labels using GPT-4o via simple, zero-shot chain-of-thought prompting, instructing it to summarize turns before labeling.
status: draft
generated:
  by: claude/unspecified
  at: 2026-09-24
sources:
  - id: alexander-scarlatos-2024
    resource: "https://arxiv.org/abs/2409.16490"
    title: "Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490"
    author: Alexander Scarlatos, Ryan S. Baker, and Andrew Lan
---

# GPT-4o Automated Dialogue Annotation with Recursive Common Core Tagging

> **Element** · [All elements](index.md)
> **Evidence** · no claims cited

## Description
The article annotates each student turn with correctness and KC labels using GPT-4o via simple, zero-shot chain-of-thought prompting, instructing it to summarize turns before labeling. "For KC annotation, we adapt the recursive tagging algorithm from [34], which tags math word problems with Common Core math standards": the model selects domains, then clusters, then turn-level standards from the Achieve the Core coherence map. The two tasks are run separately because "doing so leads to improved accuracy compared to combining them".

## Design Implications

### Context
#### Requirements
- The full dialogue as input, and the hierarchically organized Common Core standards (domains, clusters, standards) from the Achieve the Core coherence map.
- Separate prompts for correctness annotation and KC annotation.
#### Constraints
- Annotating a full dialogue with a single prompt makes real-time KT impossible; annotating one turn at a time is costly and is left for future work.
- Several dialogues are not covered by Common Core standards, so it may be necessary to augment the standards with other sources or defer to humans for labeling.

### Target Learners
- Students in one-on-one math tutoring dialogues with human or LLM-powered tutors (the article uses the CoMTA and MathDial datasets)

### Target Learning Goals
- Labeling student response correctness and the math knowledge components involved in each tutoring dialogue turn

### Affordances
- [Dialogue Knowledge Tracing Framework](../theories/dialogue-knowledge-tracing-framework.md)

## Related Elements
- [Annotating](../principles/annotating.md)

## Examples
-

## Key Sources
- Alexander Scarlatos, Ryan S. Baker, and Andrew Lan. (2024). Exploring Knowledge Tracing in Tutor-Student Dialogues using LLMs. Published in LAK25: The 15th International Learning Analytics and Knowledge Conference. https://arxiv.org/abs/2409.16490
