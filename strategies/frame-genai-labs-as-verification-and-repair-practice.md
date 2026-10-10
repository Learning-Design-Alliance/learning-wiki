---
type: strategy
id: frame-genai-labs-as-verification-and-repair-practice
title: Frame GenAI labs explicitly as verification and repair practice alongside prompting
description: "The article's deployment strategy: at the start of the activity, students were explicitly warned that the code generation model was likely to make mistakes, then instructed to carefully read generated code and manuall..."
status: draft
generated:
  by: "process:wiki-ingest"
  at: 2026-10-10
sources:
  - id: victor-alexandru-pădurean-kaitlin-riegel-alkis
    resource: "https://doi.org/10.1145/3765964.3811667"
    title: "Victor-Alexandru Pădurean, Kaitlin Riegel, Alkis Gotovos, Jyotika Mahapatra, Ahana Ghosh, Paul Denny, Juho Leinonen, James Prather, and Adish Singla. 2026. When AI Is Wrong on Purpose: How Students Respond to Buggy GenAI Code. Proceedings of the ACM Conference on International Computing Education Research Vol. 1 (ICER 2026 Vol. 1). https://doi.org/10.1145/3765964.3811667"
---

# Frame GenAI labs explicitly as verification and repair practice alongside prompting

> **Strategy** · [All strategies](index.md)
> **Evidence** · no claims cited

## Description
The article's deployment strategy: at the start of the activity, students were explicitly warned that the code generation model was likely to make mistakes, then instructed to carefully read generated code and manually edit it where needed, framing the lab as verification and repair practice alongside prompting. The interface did not indicate whether failing code was natural or injected, so students had to verify code themselves. This framing supports a pedagogically useful GenAI workflow where students practice both specification refinement through prompts and debugging through code editing.

## Design Implications

### Context
#### Requirements
- A prompt-based programming platform with hidden tests and a bug injection pipeline
- An explicit warning to students that the model is likely to make mistakes
#### Constraints
- The interface did not indicate whether failing code was due to a natural or injected bug

### Target Learners
- CS1 introductory programming students

### Target Learning Goals
- careful review of generated code
- debugging
- prompt refinement

## Related Strategies
- 

## Examples
-

## Key Sources
- Victor-Alexandru Pădurean, Kaitlin Riegel, Alkis Gotovos, Jyotika Mahapatra, Ahana Ghosh, Paul Denny, Juho Leinonen, James Prather, and Adish Singla. 2026. When AI Is Wrong on Purpose: How Students Respond to Buggy GenAI Code. Proceedings of the ACM Conference on International Computing Education Research Vol. 1 (ICER 2026 Vol. 1). https://doi.org/10.1145/3765964.3811667
