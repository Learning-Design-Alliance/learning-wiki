---
type: strategy
id: chatgpt-followup-questions-retrieval-practice
title: Train ChatGPT to pose a follow-up question after each answer to check learner understanding through retrieval practice
description: "The article's pedagogical principle of proactive knowledge checking instructs ChatGPT to answer a learner query and then ask a relevant follow-up question."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-10-27
sources:
  - id: murtaza-2024
    resource: "https://doi.org/10.1007/s40593-024-00407-z"
    title: "Murtaza, M., Cheng, C.-T., Fard, M., & Zeleznikow, J. (2024). Transforming Driver Education: A Comparative Analysis of LLM-Augmented Training and Conventional Instruction for Autonomous Vehicle Technologies. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00407-z"
    author: "Murtaza, M., Cheng, C.-T., Fard, M., & Zeleznikow, J"
---

# Train ChatGPT to pose a follow-up question after each answer to check learner understanding through retrieval practice

> **Strategy** · [All strategies](index.md)
> **Evidence** · 4 claims (3 for, 1 mixed) · 2 studies (1 causal, 1 design), `q2`–`q3` · 0 of 2 report an effect size · 4 claims rest on one study

## Description
The article's pedagogical principle of proactive knowledge checking instructs ChatGPT to answer a learner query and then ask a relevant follow-up question. The authors state that "Using follow-up questions is one of the best methods to reinforce learning through retrieval practice". In the driver-training study, ChatGPT was instructed, after explaining how to activate an ADAS function, to ask "Do you understand how to use this function, or would you like me to explain it to you again?".

## Design Implications

### Context
#### Requirements
- The ChatGPT prompt must explicitly instruct the model to pose a follow-up question to the participant after each response
#### Constraints
- 

### Target Learners
- adult learners interacting with an LLM-based training tool

### Target Learning Goals
- retention and verification of procedural knowledge

### Affordances
- [Chatgpt Prompt Framework General Pedagogical Principles](../designs/chatgpt-prompt-framework-general-pedagogical-principles.md)

## Claims

- [ChatGPT-based training produced significantly higher ADAS activation accuracy than conventional video-and-manual training for the LKA, CA and ACC functions](../claims/chatgpt-training-higher-adas-accuracy-than-conventional.md) [+M]
- [The ChatGPT group outperformed the video-based group on the LKA function, achieving 92% accuracy versus 71%](../claims/chatgpt-group-lka-92-versus-video-71.md) [+M]
- [Frequency of ChatGPT usage is positively correlated with improvement in ADAS response accuracy among ChatGPT-trained participants](../claims/chatgpt-familiarity-correlates-with-adas-accuracy.md) [+W]
- [Research-question responses score higher Answer Relevancy (0.87) than follow-ups (0.72), while Faithfulness, Context Relevance and Response Groundedness are lower](../claims/rq-higher-relevancy-lower-grounding.md) [~W]

## Related Strategies

- [Question Answering](question-answering.md)
- [Interactive Delivery With Questioning](interactive_delivery_with_questioning.md)

## Examples
-

## Key Sources
- Murtaza, M., Cheng, C.-T., Fard, M., & Zeleznikow, J. (2024). Transforming Driver Education: A Comparative Analysis of LLM-Augmented Training and Conventional Instruction for Autonomous Vehicle Technologies. International Journal of Artificial Intelligence in Education. https://doi.org/10.1007/s40593-024-00407-z
