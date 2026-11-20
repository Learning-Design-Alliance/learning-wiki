---
type: strategy
id: gmsl-prompt-framework-self-critique
title: GMSL-specific GPT-4 prompt with classroom context, reframing instruction, and one self-critique round
description: "The paper's coaching tool prompts GPT-4 with a system text containing the GMSL Guide's tenets, the classroom context, the utterance marked for reframing, and optionally one self-critique round."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-19
sources:
  - id: kunal-handa-2023
    resource: "https://arxiv.org/abs/2310.10637"
    title: "Kunal Handa, Margaret Clapper, Jessica Boyle, Rose E Wang, Diyi Yang, David S Yeager, Dorottya Demszky. (2023). \"Mistakes Help Us Grow\": Facilitating and Evaluating Growth Mindset Supportive Language in Classrooms. https://arxiv.org/abs/2310.10637"
    author: Kunal Handa, Margaret Clapper, Jessica Boyle, Rose E Wang, Diyi Yang, David S Yeager, Dorottya Demszky
---

# GMSL-specific GPT-4 prompt with classroom context, reframing instruction, and one self-critique round

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The paper's coaching tool prompts GPT-4 with a system text containing the GMSL Guide's tenets, the classroom context, the utterance marked for reframing, and optionally one self-critique round. "We utilize recent advancements in prompting and self-critique (Huang et al., 2022) techniques to de- sign a detailed, GMSL-specific prompt." The prompt personalizes reframings to each classroom instance and instructs the model to directly revise the teacher's last utterance to be mindset supportive.

## Design Implications

### Context
#### Requirements
- GMSL Guide tenets embedded in the system text
- Classroom context supplied for each conversation
- Utterance to reframe demarcated and preceded by two prior utterances
#### Constraints
- Due to context-window limits, the model could not see the entire conversation leading up to the utterance, unlike the expert teachers
- Categorization-based and few-shot prompting variants produced robotic or degraded outputs in the authors' testing

### Target Learners
- K-12 and elementary teachers

### Target Learning Goals
- growth mindset supportive classroom language

## Claims

- [GPT-4 reframings of unsupportive teacher utterances are rated as more growth mindset supportive than the original utterances across all survey dimensions](../claims/gpt4-reframings-outperform-original-utterances.md) [+W]
- [Model reframings consistently receive better ratings than expert-teacher reframings, including 23% higher challenge-seeking behavior](../claims/model-reframings-beat-expert-teacher-reframings.md) [+W]
- [Reframings contain more explicit growth mindset supportive language than original utterances, with model reframings using the most GMSL diction](../claims/reframings-contain-more-gmsl-lexicon.md) [+W]
- [One round of self-critique improves GPT-4's GMSL reframings, and nearly doubles students' hypothetical challenge-seeking relative to original utterances](../claims/self-critique-improves-gmsl-reframings.md) [+W]
- [About 22.8% of task-related teacher utterances in the elementary math transcripts contained unsupportive language](../claims/high-rate-unsupportive-language-transcripts.md) [+W]

## Related Strategies
- 

## Examples
-

## Key Sources
- Kunal Handa, Margaret Clapper, Jessica Boyle, Rose E Wang, Diyi Yang, David S Yeager, Dorottya Demszky. (2023). "Mistakes Help Us Grow": Facilitating and Evaluating Growth Mindset Supportive Language in Classrooms. https://arxiv.org/abs/2310.10637
