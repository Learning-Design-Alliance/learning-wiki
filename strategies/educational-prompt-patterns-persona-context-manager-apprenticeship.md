---
type: strategy
id: educational-prompt-patterns-persona-context-manager-apprenticeship
title: Revise educational SLM system prompts using the Persona and Context Manager patterns plus cognitive-apprenticeship scaffolding guidelines
description: The revised prompt combined the Persona pattern (defining a consistent tutoring role with specific responsibilities) and the Context Manager pattern (explicitly scoping what the model should and should not address), w...
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: h-chad-lane-2026
    resource: "https://github.com/InviteInstitute/CSTutorBench"
    title: "H. Chad Lane, Bryson Kageler. (2026). CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming. SLM4ED'26: The 1st Workshop of Small Language Models for Education. https://github.com/InviteInstitute/CSTutorBench"
    author: H. Chad Lane, Bryson Kageler
---

# Revise educational SLM system prompts using the Persona and Context Manager patterns plus cognitive-apprenticeship scaffolding guidelines

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The revised prompt combined the Persona pattern (defining a consistent tutoring role with specific responsibilities) and the Context Manager pattern (explicitly scoping what the model should and should not address), which Holmes et al.'s evaluation found the most effective pairing for educational applications. It added cognitive-apprenticeship elements: "graduated mentorship that favors coaching and hinting over direct demonstration," affirming student effort before addressing errors, and grounding feedback in the student's specific artifact. Explicit formatting constraints (no markdown, no bullet points, 1–3 sentences) replaced open-ended rules, and domain-specific context such as sensor behavior clarifications was added.

## Design Implications

### Context
#### Requirements
- Requires domain-specific context a real tutoring system would provide, such as clarifications about sensor behavior and notes on common sources of bugs
#### Constraints
- The revised prompt roughly quadrupled in length (from approximately 50 to 400 words of instructional content) and conciseness decreased slightly on average, possibly because the structured response format encouraged additional scaffolding elements that added length

### Target Learners
- middle school students (grades 6–8) working with an SLM tutor

### Target Learning Goals
- block-based programming tutoring in VEX VR

## Related Strategies

- [Use a natural-language strategy guideline in the generator prompt so tutoring strategy can be revised without code changes](collearn-natural-language-strategy-guideline.md)

## Examples
-

## Key Sources
- H. Chad Lane, Bryson Kageler. (2026). CSTutorBench: Benchmarking Small Language Models as Tutors for Block-Based Programming. SLM4ED'26: The 1st Workshop of Small Language Models for Education. https://github.com/InviteInstitute/CSTutorBench
