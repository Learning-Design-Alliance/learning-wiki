---
type: strategy
id: gpt3-zero-shot-cue-generation-strategy
title: Use GPT-3 with zero-shot prompting to generate curiosity-prompting cues for educational texts without fine-tuning
description: The article describes a prompting pipeline in which GPT-3 (text-davinci-002, temperature 0.7) is given a short scientific text and prompted to generate key ideas, related keywords, divergent questions, and short answers.
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-28
sources:
  - id: abdelghani-2023
    resource: "https://hal.science/hal-03890447v1"
    title: "Abdelghani, R., Wang, Y.-H., Yuan, X., Wang, T., Lucas, P., Sauzéon, H., & Oudeyer, P.-Y. (2023). GPT-3-driven pedagogical agents for training children's curious question-asking skills. International Journal of Artificial Intelligence in Education. https://hal.science/hal-03890447v1"
    author: "Abdelghani, R., Wang, Y.-H., Yuan, X., Wang, T., Lucas, P., Sauzéon, H., & Oudeyer, P.-Y"
---

# Use GPT-3 with zero-shot prompting to generate curiosity-prompting cues for educational texts without fine-tuning

> **Strategy** · [All strategies](index.md)
> **Evidence** · 5 claims (5 for) · 1 study (1 causal), `q3` · 0 of 1 report an effect size · 5 claims rest on one study

## Description
The article describes a prompting pipeline in which GPT-3 (text-davinci-002, temperature 0.7) is given a short scientific text and prompted to generate key ideas, related keywords, divergent questions, and short answers. These outputs serve as the agent's linguistic and semantic cues. The approach uses "a zero-shot setting" with no parameter updates, making it accessible to practitioners without machine learning expertise. Cues are generated offline, checked for inappropriate content, translated, and stored in a database before the agent uses them with children.

## Design Implications

### Context
#### Requirements
- Short scientific text-based educational resources as context (mean of 109 words per article in this study)
- Offline generation with human verification that cues do not include inappropriate or offensive words
- A database connecting educational resources to their generated cues
#### Constraints
- The authors had no control over GPT-3's outputs, so children were not put in direct contact with the model; an offline implementation was used

### Target Learners
- Children aged 9-10.5 years (4th grade primary school students)

### Target Learning Goals
- Divergent question-asking skills
- Curiosity-driven exploration of educational texts

## Claims

- [GPT-3-generated cues matched hand-crafted cues in offensiveness, contextual relevance, semantic relatedness, and divergence level](../claims/gpt3-cue-quality-comparable.md) [+M]
- [GPT-3-generated incentive cues produced divergent question-asking performance similar to hand-crafted cues](../claims/gpt3-cues-match-handcrafted-performance.md) [+M]
- [GPT-3 and hand-generated questioning words showed similar variety and complexity distributions](../claims/gpt3-linguistic-cues-similar-variety.md) [+M]
- [Children trained with the GPT-3-driven open-cue agent generated a significantly higher percentage of divergent questions than children with either incentive agent](../claims/open-agent-better-divergent-qa-performance.md) [+M]
- [Children with the open agent used the agent's cues more often than children with either incentive agent](../claims/open-agent-higher-cue-usage.md) [+M]

## Related Strategies
- 

## Examples
-

## Key Sources
- Abdelghani, R., Wang, Y.-H., Yuan, X., Wang, T., Lucas, P., Sauzéon, H., & Oudeyer, P.-Y. (2023). GPT-3-driven pedagogical agents for training children's curious question-asking skills. International Journal of Artificial Intelligence in Education. https://hal.science/hal-03890447v1
