---
type: strategy
id: preference-matched-genai-supplements-strategy
title: Tailor AI-generated supplementary material format to individual learner preferences
description: "The article's third contribution is a design guideline for AI-driven educational tools: \"emphasizing optimizing visual content to accommodate diverse cognitive styles and learning preferences\"."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-21
sources:
  - id: ryugo-morita-2025
    resource: "https://arxiv.org/abs/2503.07463"
    title: "Ryugo Morita, Ko Watanabe, Jinjia Zhou, Andreas Dengel, and Shoya Ishimaru. (2025). GenAIReading: Augmenting Human Cognition with Interactive Digital Textbooks Using Large Language Models and Image Generation Models. https://arxiv.org/abs/2503.07463"
    author: Ryugo Morita, Ko Watanabe, Jinjia Zhou, Andreas Dengel, and Shoya Ishimaru
---

# Tailor AI-generated supplementary material format to individual learner preferences

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (4 for) · 1 study (1 causal), `q2` · 0 of 1 report an effect size · 4 claims rest on one study

## Description
The article's third contribution is a design guideline for AI-driven educational tools: "emphasizing optimizing visual content to accommodate diverse cognitive styles and learning preferences". Because text-preference learners scored highest with text summaries and image-preference learners with image summaries, the recommended strategy is to offer both text-based and image-based supplementary materials and match their format to each learner's stated preference. The article argues this tailoring "not only improves engagement but also enhances comprehension, retention, and overall learning outcomes".

## Design Implications

### Context
#### Requirements
- A way to elicit each learner's preference for text-generation vs image-generation materials (in the study, post-survey questions Q3 and Q4)
- A pipeline able to generate both text summaries and image summaries for the same reading content
#### Constraints
- The supporting preference-performance pattern is observational; the authors cannot definitively claim a statistical correlation
- Personalization was tested only with young adult participants familiar with LLMs and IGMs

### Target Learners
- diverse learners reading digital textbooks, including verbal-preference and visual-preference learners

### Target Learning Goals
- reading comprehension
- memory retention
- learner engagement

## Claims

- [Learners perform best when supplementary material format matches their stated text or image preference](../claims/preference-congruent-supplements-raise-scores.md) [+W]
- [AI-generated inline images yield only a slight average improvement over baseline and add performance variability](../claims/genai-inline-images-slight-gain-high-variability.md) [+W]
- [Eye-tracking AOI ratios reveal substantial individual differences in engagement with GenAI materials](../claims/aoi-ratio-individual-differences-genai.md) [+W]
- [Verbal vs. visual preference learners show distinct gaze patterns, though no statistical correlation is claimed](../claims/verbal-visual-preference-gaze-patterns.md) [+W]

## Related Strategies

- [Respect Diverse Talents and Ways of Learning](respect_diverse_talents_and_ways_of_learning.md)
- [Customizing Display of Information](customizing_display_of_information.md)
- [Customizable Display of Information](customizable_display_of_information.md)
- [Include relevant textbook-based visuals alongside textual explanations in conversational AI for visually rich STEM domains](textbook-visuals-alongside-text-in-stem-conversational-ai.md)

## Examples
-

## Key Sources
- Ryugo Morita, Ko Watanabe, Jinjia Zhou, Andreas Dengel, and Shoya Ishimaru. (2025). GenAIReading: Augmenting Human Cognition with Interactive Digital Textbooks Using Large Language Models and Image Generation Models. https://arxiv.org/abs/2503.07463
