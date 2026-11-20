---
type: strategy
id: llm-prompt-schema-and-preprocessing-strategy
title: Improve LLM feedback quality via JSON-schema prompts with hidden scoring keys and preprocessing code into structured dictionaries
description: "The authors' prompt-engineering recipe for consistent, standardizable LLM feedback."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: juliette-woodrow-2024
    resource: "https://doi.org/10.1145/3626252.3630773"
    title: "Juliette Woodrow, Ali Malik, and Chris Piech. 2024. AI Teaches the Art of Elegant Coding: Timely, Fair, and Helpful Style Feedback in a Global Course. In Proceedings of the 55th ACM Technical Symposium on Computer Science Education V. 1 (SIGCSE 2024). https://doi.org/10.1145/3626252.3630773"
    author: Juliette Woodrow, Ali Malik, and Chris Piech
---

# Improve LLM feedback quality via JSON-schema prompts with hidden scoring keys and preprocessing code into structured dictionaries

> **Strategy** · [All strategies](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
The authors' prompt-engineering recipe for consistent, standardizable LLM feedback. Their first insight was "to instruct the LLM to produce output as a JSON conforming to the schema detailed in the prompt," which standardized content, mitigated student exposure to unconstrained LLM output, and enabled systematic parsing and validation. Schema keys included hidden ones that raised output quality: requiring the model to score each variable name (unseen by students) significantly improved its ability to distinguish robust from weak names, and asking it to detect type-misleading names caught cases it otherwise missed. Their second insight was preprocessing each student's code to send additional structured information, such as a dictionary mapping each variable to its assigned values.

## Design Implications

### Context
#### Requirements
- Per-feedback-type prompts each outlining a unique JSON schema with specific keys, and preprocessing pipelines that attach structured context (variable-value and line-number-to-comment dictionaries) to the code text.
#### Constraints
- Initially, when only the code text and prompt were provided, the generated output showed incomplete consideration of identifier names and inaccurate line number information.

### Target Learners
- CS1 students receiving automated style feedback

### Target Learning Goals
- consistent, high-quality automated feedback on identifier names and comments

## Claims

- [Schema-constrained Structured Outputs eliminated parse failures: every /challenge and /unlock call returned a valid, fully-typed object during development testing](../claims/structured-outputs-eliminate-parse-failure-class.md) [+W]

## Related Strategies

- [Safeguard LLM feedback for students by stripping identity information, limiting interaction rounds, and forcing validated JSON output](llm-feedback-safety-safeguards-strategy.md)
- [Constrain an LLM to inquiry-only questioning via negative system-prompt constraints plus strict JSON schemas](negative-constraint-prompting-inquiry-only-llm.md)
- [Engineer LLM grading prompts with detailed, domain-specific evaluation criteria and band descriptors](prompt-llm-grading-with-detailed-band-descriptors.md)
- [Design GPT feedback prompts with few-shot examples covering each response category and documented student preconceptions as context](few-shot-prompt-with-preconceptions-for-feedback-generation.md)

## Examples
-

## Key Sources
- Juliette Woodrow, Ali Malik, and Chris Piech. 2024. AI Teaches the Art of Elegant Coding: Timely, Fair, and Helpful Style Feedback in a Global Course. In Proceedings of the 55th ACM Technical Symposium on Computer Science Education V. 1 (SIGCSE 2024). https://doi.org/10.1145/3626252.3630773
