---
type: strategy
id: nudge-active-practice-mitigate-gaming
title: Nudge learners toward active practice and mitigate gaming behavior in LLM-based conversational tutoring
description: Based on their log analyses, the authors recommend future system revisions that nudge users toward active practice and mitigate gaming behavior, since help-seeking and gaming patterns were associated with lower perfor...
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: robin-schmucker-2024
    resource: "https://arxiv.org/abs/2404.17460"
    title: "Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell. (2024). Ruffle&Riley: Insights from Designing and Evaluating a Large Language Model-Based Conversational Tutoring System. https://arxiv.org/abs/2404.17460"
    author: Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell
---

# Nudge learners toward active practice and mitigate gaming behavior in LLM-based conversational tutoring

> **Strategy** · [All strategies](index.md)
> **Evidence** · 3 claims (3 for) · 1 study (1 causal), `q2` · 1 of 1 report an effect size · 3 claims rest on one study

## Description
Based on their log analyses, the authors recommend future system revisions that nudge users toward active practice and mitigate gaming behavior, since help-seeking and gaming patterns were associated with lower performance while conversation-focused, non-help-seeking users achieved the highest gains. They also recommend enhancing the system's ability to provide feedback that helps users elicit all information in their explanations.

## Design Implications

### Context
#### Requirements
- Interaction log data to detect help-seeking and gaming patterns
- Feedback mechanisms that prompt users to complete partial explanations
#### Constraints
- The authors state the system was lenient toward user responses that only covered parts of one expectation, moving the conversation ahead too quickly

### Target Learners
- Adult online learners in conversational tutoring activities

### Target Learning Goals
- Deeper understanding of lesson concepts through complete, active explanations

## Claims

- [Conversation-log analysis found the system hosted coherent EMT-based dialogues but was lenient toward partial explanations and sometimes repeated requests](../claims/conversation-analysis-coherent-but-lenient.md) [+W]
- [Conversation features correlate with learning performance: words and learning time positively, help and revision requests negatively](../claims/conversation-features-correlate-with-learning-performance.md) [+M]
- [Four distinct usage patterns emerged, with conversation-focused users who did not request help showing the highest learning gains](../claims/four-usage-patterns-conversation-focused-highest-gains.md) [+M]

## Related Strategies

- [Use dynamic user models to recognize non-optimal learning behaviors and redirect students toward more effective behaviors](dynamic-user-models-redirect-non-optimal-behaviors.md)
- [Scaffold question formulation and active help-seeking in AI-supported tutoring systems](scaffold-question-formulation-ai-help-seeking.md)
- [Recognize high-spendency behavior and prompt students toward less spending and more generative practice](prompt-high-spendency-students-toward-generative-practice.md)

## Examples
-

## Key Sources
- Robin Schmucker, Meng Xia, Amos Azaria, and Tom Mitchell. (2024). Ruffle&Riley: Insights from Designing and Evaluating a Large Language Model-Based Conversational Tutoring System. https://arxiv.org/abs/2404.17460
