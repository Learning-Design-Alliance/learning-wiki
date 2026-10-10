---
type: design
id: hallucination-inducing-film-question-set
title: Hallucination-inducing film-detail question set with pre-generated incorrect AI responses
description: "A six-question instrument about fine visual details of films (e.g., Agatha's hairstyle in The Grand Budapest Hotel), designed, in the article's words, to be \"both hard for participants to answer and likely to induce h..."
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
sources:
  - id: chiara-marcoccia-2026
    resource: "https://osf.io/nwx6r/overview?view_only=a03ae0ca587c4c84a442c44d55ab97b6"
    title: "Chiara Marcoccia, Walter Quattrociocchi, Valerio Capraro. (2026). AI advice suppresses people's willingness to say \"I don't know\", even when the advice is wrong and accuracy is incentivized. https://osf.io/nwx6r/overview?view_only=a03ae0ca587c4c84a442c44d55ab97b6"
    author: Chiara Marcoccia, Walter Quattrociocchi, Valerio Capraro
---

# Hallucination-inducing film-detail question set with pre-generated incorrect AI responses

> **Design** · [All designs](index.md)
> **Evidence** · 1 claim (1 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 1 claim rests on one study

## Description
A six-question instrument about fine visual details of films (e.g., Agatha's hairstyle in The Grand Budapest Hotel), designed, in the article's words, to be "both hard for participants to answer and likely to induce hallucinations (i.e., fabricated answers)" from the LLM used, Step 3.5 Flash. Because the advice was usually wrong, any drop in suspension cannot be read as sensible delegation to a reliable tool. In later studies, AI replies were drawn at random from pre-recorded outputs so every advice-seeker received a complete, well-formed answer.

## Design Implications

### Context
#### Requirements
- Questions about details minor enough to be largely absent from online text, so that language models trained on such text fabricate answers
- Pre-generated responses per question so displayed advice is complete and constant across participants
#### Constraints
- The questions engineer an almost-always-wrong AI, so the paradigm isolates unreliable advice; the article states it is untested whether suspension collapses equally with usually-correct advice

### Target Learners
- Adult crowdworkers (Prolific, US-based)

### Learning Goals
- Measuring judgment suspension, correctness, confidence, and AI-advice seeking under uncertain knowledge

### Claims
- [Ai Access Nearly Eliminates Judgment Suspension](../claims/ai-access-nearly-eliminates-judgment-suspension.md) [+M]

## Related Designs
- 

## Examples
-

## Key Sources
- Chiara Marcoccia, Walter Quattrociocchi, Valerio Capraro. (2026). AI advice suppresses people's willingness to say "I don't know", even when the advice is wrong and accuracy is incentivized. https://osf.io/nwx6r/overview?view_only=a03ae0ca587c4c84a442c44d55ab97b6
