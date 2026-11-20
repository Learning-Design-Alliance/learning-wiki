---
type: strategy
id: adaptive-empathetic-feedback-generation-strategy
title: "Generate adaptive empathetic feedback tailored to the learner's recent utterances"
description: "When the system registers distress signals such as heightened negative affect or prolonged pauses, a ChatGPT prompt \"optimized through the DSPy framework\" produces empathetic feedback from past user utterances that so..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: li-siyan-2024
    resource: "https://arxiv.org/abs/2406.17982"
    title: "Li Siyan, Teresa Shao, Zhou Yu, Julia Hirschberg. (2024). EDEN: Empathetic Dialogues for English learning. arXiv:2406.17982v2 [cs.CL]. https://arxiv.org/abs/2406.17982"
    author: Li Siyan, Teresa Shao, Zhou Yu, Julia Hirschberg
---

# Generate adaptive empathetic feedback tailored to the learner's recent utterances

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
When the system registers distress signals such as heightened negative affect or prolonged pauses, a ChatGPT prompt "optimized through the DSPy framework" produces empathetic feedback from past user utterances that sounds empathetic and colloquial and includes examples and actionable feedback, with rewrite prompts to shorten it and reduce formality. Feedback is personalized via user preference questions about Mandarin translations and feedback length.

## Design Implications

### Context
#### Requirements
- Signals of user distress (negative affect, prolonged pauses) must be detectable
- Past user utterances available as context for generation
#### Constraints
- Feedback generated from text may still sound overly formal and needs rewriting prompts
- Only triggered when distress signals occur, so highly proficient participants may never trigger it

### Target Learners
- L2 English learners in spoken conversation practice

### Target Learning Goals
- Perceived affective support
- L2 grit

## Claims

- [Adaptive empathetic feedback yields higher chatbot perceived affective support than fixed or no empathetic feedback in a preliminary user study](../claims/adaptive-empathetic-feedback-higher-chatbot-pas.md) [+W]
- [Components of chatbot perceived affective support correlate with positive changes in L2 grit](../claims/chatbot-pas-components-correlate-l2-grit-changes.md) [+W]
- [Chatbot perceived affective support correlates positively with conversation quality ratings](../claims/chatbot-pas-correlates-conversation-quality.md) [+W]
- [Higher perceived appreciation is an intermediate-strength predictor of higher post-survey L2 grit, partially generalizing teacher-PAS findings to chatbots](../claims/perceived-appreciation-predicts-post-survey-l2-grit.md) [+W]

## Related Strategies

- Eden Empathetic English Chatbot
- [Adaptive responses to carelessness should take probable student affect into account and tailor messages to highly engaged students](affect-aware-carelessness-interventions.md)

## Examples
-

## Key Sources
- Li Siyan, Teresa Shao, Zhou Yu, Julia Hirschberg. (2024). EDEN: Empathetic Dialogues for English learning. arXiv:2406.17982v2 [cs.CL]. https://arxiv.org/abs/2406.17982
