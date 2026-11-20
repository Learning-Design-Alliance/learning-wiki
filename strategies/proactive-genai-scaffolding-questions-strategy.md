---
type: strategy
id: proactive-genai-scaffolding-questions-strategy
title: Use proactive GenAI agents that guide students through visualisations with pre-defined scaffolding questions and feedback on responses
description: "The article's proactive GenAI agents go beyond answering queries: they follow \"pre-defined scaffolding narratives with guiding questions\" and give feedback on students' prior responses, asking students to elaborate or..."
status: review
generated:
  by: "process:wiki-ingest"
  at: 2026-11-20
sources:
  - id: lixiang-yan-2024
    resource: "https://arxiv.org/abs/2409.11645"
    title: "Lixiang Yan, Roberto Martinez-Maldonado, Yueqiao Jin, Vanessa Echeverria, Mikaela Milesi, Jie Fan, Linxuan Zhao, Riordan Alfredo, Xinyu Li and Dragan Gašević. (2024). The Effects of Generative AI Agents and Scaffolding on Enhancing Students' Comprehension of Visual Learning Analytics. https://arxiv.org/abs/2409.11645"
    author: Lixiang Yan, Roberto Martinez-Maldonado, Yueqiao Jin, Vanessa Echeverria, Mikaela Milesi, Jie Fan, Linxuan Zhao, Riordan Alfredo, Xinyu Li and Dragan Gašević
---

# Use proactive GenAI agents that guide students through visualisations with pre-defined scaffolding questions and feedback on responses

> **Strategy** · [All strategies](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 causal), `q3` · 1 of 1 report an effect size · 2 claims rest on one study

## Description
The article's proactive GenAI agents go beyond answering queries: they follow "pre-defined scaffolding narratives with guiding questions" and give feedback on students' prior responses, asking students to elaborate or move to the next guiding question. Each response assesses the correctness of students' answers via semantic search over vector embeddings and generates encouraging or corrective feedback. This implements a step-by-step, educator-like guidance style within the agent, targeting each element of the visualisations in turn.

## Design Implications

### Context
#### Requirements
- A pre-defined scaffolding narrative of guiding questions crafted by educators and researchers
- A knowledge database with contextual information enabling semantic assessment of student responses
#### Constraints
- The strategy was implemented with multimodal GPT-4o plus retrieval-augmented generation in a healthcare simulation VLA context

### Target Learners
- higher education students

### Target Learning Goals
- comprehension of visual learning analytics

### Affordances
- [Genai Agent Five Component Vla Design](../designs/genai-agent-five-component-vla-design.md)

## Claims

- [In the data storytelling condition, correct scores for VLA comprehension improved significantly from pre-intervention to both the intervention and post-intervention phases, with large effects](../claims/data-storytelling-vla-score-gains-persist-post-intervention.md) [+W]
- [A preliminary mixed linear model found no significant change in correct scores from the intervention to the post-intervention phase in one uncontrolled pre-post study](../claims/no-learning-effects-repeated-exposure-vla-task.md) [+W]

## Related Strategies

- [Train ChatGPT to pose a follow-up question after each answer to check learner understanding through retrieval practice](chatgpt-followup-questions-retrieval-practice.md)
- [GenAI learning interfaces should actively scaffold monitoring, evaluation, and AI-shaping behaviors adolescents may not bring to the interaction on their own](scaffold-monitoring-evaluation-ai-shaping-genai-interfaces.md)

## Examples
-

## Key Sources
- Lixiang Yan, Roberto Martinez-Maldonado, Yueqiao Jin, Vanessa Echeverria, Mikaela Milesi, Jie Fan, Linxuan Zhao, Riordan Alfredo, Xinyu Li and Dragan Gašević. (2024). The Effects of Generative AI Agents and Scaffolding on Enhancing Students' Comprehension of Visual Learning Analytics. https://arxiv.org/abs/2409.11645
