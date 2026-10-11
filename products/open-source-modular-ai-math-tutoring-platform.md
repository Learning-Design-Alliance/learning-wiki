---
type: product
id: open-source-modular-ai-math-tutoring-platform
title: Open-source modular AI math tutoring platform
description: An open-source modular platform developed by Jarosław A.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# Open-source modular AI math tutoring platform

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (1 for, 1 mixed) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
An open-source modular platform developed by Jarosław A. Chudziak and colleagues for AI-powered personalized mathematics tutoring, integrating conversational tutoring, retrieval, task generation, symbolic solving, plotting, and course-graph tools.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **AITutor: an LLM-based iPad tutoring app translating pedagogical mechanisms into UI features**: AITutor is a React Native/Expo iPad app with a Python/FastAPI backend that orchestrates LLM calls, curriculum-constrained prompting, retrieval over digitized course materials, and telemetry logging. Rather than "treating the AI as an open-ended chatbot, we constrained the interaction, translating pedagogical mechanisms into explicit UI features." Its features are layered worked examples (overview, orientation, explanation, final-answer checkpoint, exam-format layer), step-linked visual grounding, a contextual follow-up dock, and a delayed retrieval/wrong-book loop. (From Answer Generators to Reasoning Facilitators: Designing AI Tutors for Mathematical Rea)
- **MathBuddy: multimodal emotion-aware LLM math tutoring system**: MathBuddy is an emotionally aware LLM-powered math tutor that, per the authors, "dynamically models the student's emotions and maps them to relevant pedagogical strategies, making the tutor-student conversation a more empathetic one." It captures emotions from conversational text (a fine-tuned DistilBERT classifier) and from webcam facial expressions (face-api.js, reporting 76% accuracy and 71% F1 on its test set), aggregates both modalities into Positive/Neutral/Negative, and prompts the LLM tutor accordingly. The system has a TypeScript frontend with chat interface, webcam input, and visual workspace, and a Python REST backend for inference. Code, dataset, and demo video are publicly released. (Debanjana Kar et al. (2025))

### Claims
- [In a within-subject user study, participants showed longer positive facial expressions under the emotion-aware (Emotion ON) tutoring condition](../claims/emotion-on-longer-positive-facial-expressions.md) [+M]
- [MathBuddy's multimodal emotion aggregation matched participant-reviewed emotions at 60% overall accuracy, with sharply reduced recall for the Neutral class](../claims/multimodal-emotion-aggregation-60-percent-accuracy.md) [~M]

## Related Products and Programmes
-

## Key Sources
- Jarosław A. Chudziak and Adam Kostka. (2025). AI-Powered Math Tutoring: Platform for Personalized and Adaptive Education. arXiv preprint. https://arxiv.org/abs/2507.12484
- Harry Feng, Yuan Tian, and Erica Zhao. 2026. From Answer Generators to Reasoning Facilitators: Designing AI Tutors for Mathematical Reasoning in High-Stakes Environments. https://arxiv.org/abs/2607.01692
- Debanjana Kar, Leopold Böss, Dacia Braca, Sebastian Dennerlein, Nina Hubig, Philipp Wintersberger, and Yufang Hou. (2025). MathBuddy: A Multimodal System for Affective Math Tutoring. https://arxiv.org/abs/2508.19993
