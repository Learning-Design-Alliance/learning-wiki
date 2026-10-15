---
type: strategy
id: frame-genai-labs-as-verification-and-repair-practice
title: Frame GenAI labs explicitly as verification and repair practice alongside prompting
description: "The article's deployment strategy: at the start of the activity, students were explicitly warned that the code generation model was likely to make mistakes, then instructed to carefully read generated code and manuall..."
status: review
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
> **Evidence** · 1 claim (1 mixed) · 1 study (1 associational), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

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

## Claims

- [Manual reasoning is the most consistently used verification method across assignments, with no significant difference in its use across subfields](../claims/manual-reasoning-consistent-verification-across-subfields.md) [~W]

## Related Strategies

- [Scaffolded critique-of-AI-output assignment sequence with paired verification of individual understanding](critique-ai-output-assignment-sequence.md)
- [Provide explicit instruction in AI prompting and information verification alongside AI integration in laboratory courses](explicit-ai-prompting-verification-instruction.md)
- [Embed verification routines and cognitive forcing functions into AI-supported learning tasks](verification-routines-cognitive-forcing-ai-tasks.md)
- [Embed SRL-oriented AIGC pedagogy: prompt-and-reflect routines, verification rubrics, and feedback literacy](srl-oriented-aigc-pedagogy-routines.md)

## Examples
-

## Key Sources
- Victor-Alexandru Pădurean, Kaitlin Riegel, Alkis Gotovos, Jyotika Mahapatra, Ahana Ghosh, Paul Denny, Juho Leinonen, James Prather, and Adish Singla. 2026. When AI Is Wrong on Purpose: How Students Respond to Buggy GenAI Code. Proceedings of the ACM Conference on International Computing Education Research Vol. 1 (ICER 2026 Vol. 1). https://doi.org/10.1145/3765964.3811667
