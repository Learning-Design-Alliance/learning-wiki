---
type: strategy
id: gpt-transcript-summaries-educator-feedback
title: GPT-summarised chat transcripts as data-driven educator feedback with the educator as human in the loop
description: The article describes saving student chat transcripts to a database, extracting and summarising them with GPT to generate feedback based on student interactions with the AI patient and supervisor.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-05
sources:
  - id: b-jones-2026
    resource: "https://doi.org/10.1111/eje.13135"
    title: "B. Jones, A. Desu, and C. D. F. Honig. (2026). Artificial Intelligence Chatbots as Virtual Patients in Dental Education: A Constructivist Approach to Classroom Implementation. European Journal of Dental Education 30(2): 447–456. https://doi.org/10.1111/eje.13135"
    author: B. Jones, A. Desu, and C. D. F. Honig
---

# GPT-summarised chat transcripts as data-driven educator feedback with the educator as human in the loop

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 against) · 3 studies (2 design, 1 associational), `q2`–`q3` · 0 of 3 report an effect size · 4 claims rest on one study

## Description
The article describes saving student chat transcripts to a database, extracting and summarising them with GPT to generate feedback based on student interactions with the AI patient and supervisor. Student queries and GPT replies are recorded in MongoDB, the complete transcript is fed into a GPT for summarisation, and "The educator becomes the 'human in the loop' who can interpret the summaries and relay feedback to the students." The authors state this demonstrates how educators, regardless of class size, could leverage GPT to augment instruction and provide personalised, real-time feedback.

## Design Implications

### Context
#### Requirements
- A mechanism to save student interactions with the chatbot (e.g., MongoDB recording of queries and replies)
- Educator interpretation of the AI-generated summaries before relaying feedback
#### Constraints
- The article notes the initial summarisation approach could not be applied in real time, though the process has since been automated on the user interface

### Target Learners
- dental and oral health students in classroom tutorials

### Target Learning Goals
- timely, tailored feedback on history taking and clinical decision-making

## Claims

- [GPT-4o mini achieved the lowest ACT balance MAE (6.12) in replicating human supervisor ratings across 49 full transcripts](../claims/gpt-4o-mini-lowest-act-balance-mae.md) [+W]
- [GPT-4o mini showed progressive turn-level convergence with accumulating context while larger models showed increasing or stable error](../claims/turn-level-convergence-gpt-4o-mini.md) [+W]
- [Prior studies summarised in one article report that students rate instructor feedback above AI-generated feedback, and rate AI feedback lower once they know its origin](../claims/students-prefer-human-feedback-over-ai.md) [-W]
- [Human scoring and feedback for HDR takes about 11 minutes 30 seconds per learner, while GPT-based scoring and feedback is nearly instant](../claims/hdr-human-scoring-time-burden.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- B. Jones, A. Desu, and C. D. F. Honig. (2026). Artificial Intelligence Chatbots as Virtual Patients in Dental Education: A Constructivist Approach to Classroom Implementation. European Journal of Dental Education 30(2): 447–456. https://doi.org/10.1111/eje.13135
