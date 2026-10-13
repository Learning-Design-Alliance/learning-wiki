---
type: strategy
id: mitigate-llm-feedback-errors-context-and-fact-checking
title: Mitigate LLM feedback errors by supplying course materials and compiler errors in the prompt, fact-checking generated feedback, and adapting feedback structure to student behavior
description: "The article's discussion and future-work section recommend concrete mitigations for LLM-generated feedback errors: providing relevant learning materials in the prompt may mitigate issues \"especially when the model's k..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-11
sources:
  - id: tsvetomila-mihaylova-2026
    resource: "https://arxiv.org/abs/2605.16933"
    title: "Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen. (2026). The Effects of Structured LLM-Generated Feedback on Programming Assignment Performance. https://arxiv.org/abs/2605.16933"
    author: Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen
---

# Mitigate LLM feedback errors by supplying course materials and compiler errors in the prompt, fact-checking generated feedback, and adapting feedback structure to student behavior

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article's discussion and future-work section recommend concrete mitigations for LLM-generated feedback errors: providing relevant learning materials in the prompt may mitigate issues "especially when the model's knowledge is outdated", and including compiler error messages could guide the LLM toward key issues. It further proposes automated fact-checking mechanisms to verify feedback correctness before display, and adaptive feedback approaches that adjust feedback structure based on student behavior, task characteristics, or prior interaction patterns rather than fixed formats.

## Design Implications

### Context
#### Requirements
- Access to up-to-date course materials or retrieval to counter outdated model knowledge
- Automated fact-checking of generated feedback before display to students
#### Constraints
- The article notes a single feedback strategy is unlikely to be optimal for all students or tasks, given substantial variation across students and assignments

### Target Learners
- Novice and advanced programmers in online introductory programming courses

### Target Learning Goals
- Reaching correct programming solutions efficiently (fewer attempts, less time)

## Related Strategies

- [Apply error mitigation such as self-consistency before deploying LLM-generated help, and frame unmitigated LLM feedback as an imperfect source](mitigate-llm-hint-errors-before-deployment.md)
- [Provide LLM graders with the full human rubric, accepted solutions, and common-mistake penalties in the prompt (rubric-enhanced prompting)](rubric-enhanced-llm-grading-prompt.md)

## Examples
-

## Key Sources
- Tsvetomila Mihaylova, Evanfiya Logacheva, Arto Hellas, Jing Fan, Francisco Castro, Bita Akram, Narges Norouzi, Peter Brusilovsky, Juho Leinonen. (2026). The Effects of Structured LLM-Generated Feedback on Programming Assignment Performance. https://arxiv.org/abs/2605.16933
