---
type: design
id: ai-book-discussion-companion-whisper-gpt35
title: "AI book discussion companion: a fixed peer-role conversational agent using Whisper speech-to-text and GPT-3.5"
description: A conversational AI system developed by the research team for elementary book talk.
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-11
sources:
  - id: liao-2026
    resource: "https://doi.org/10.1007/s10639-026-13958-6"
    title: "Liao, C.-Y. (2026). Beyond a single role: Justifying a role-adaptive framework for ai companions through a comparative study in elementary book talk. Education and Information Technologies. https://doi.org/10.1007/s10639-026-13958-6"
    author: Liao, C.-Y
---

# AI book discussion companion: a fixed peer-role conversational agent using Whisper speech-to-text and GPT-3.5

> **Design** · [All designs](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
A conversational AI system developed by the research team for elementary book talk. "This system utilized Ope - nAI's Whisper API for accurate speech-to-text transcription of student utterances and the GPT-3.5 API for natural language understanding and the generation of contextu - ally relevant responses, delivered via both text and synthesized speech (Web Speech API)." For the comparative study it was configured to act as a peer-like, non-evaluative partner following the 4F framework sequentially, and it operated in this fixed role throughout AI sessions. The system automatically logged session durations and generated complete transcripts used for analysis.

## Design Implications

### Context
#### Requirements
- Speech-to-text and language-model APIs for transcription and response generation
- A fixed peer-role system prompt following the 4F framework sequentially
#### Constraints
- Operated in a single fixed peer role for the study, without context-aware role adaptation

### Target Learners
- Elementary school students in Grades 4 and 5

### Learning Goals
- Book talk dialogue about self-chosen books
- Reflection prompted in a non-evaluative manner

### Claims
- [Ai Peer Longer Book Talk Sessions](../claims/ai-peer-longer-book-talk-sessions.md) [+M]
- [Ai Conversational Dominance Lower Student Contribution](../claims/ai-conversational-dominance-lower-student-contribution.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Liao, C.-Y. (2026). Beyond a single role: Justifying a role-adaptive framework for ai companions through a comparative study in elementary book talk. Education and Information Technologies. https://doi.org/10.1007/s10639-026-13958-6
