---
type: design
id: genai-agent-five-component-vla-design
title: Five-component GenAI agent design combining multimodal LLMs, retrieval-augmented generation, and agentic scaffolding for VLA comprehension
description: "The article presents a system design in which passive and proactive generative AI agents support comprehension of visual learning analytics through five components: agent characteristics, prompt integration, knowledge..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-11-20
sources:
  - id: lixiang-yan-2024
    resource: "https://arxiv.org/abs/2409.11645"
    title: "Lixiang Yan, Roberto Martinez-Maldonado, Yueqiao Jin, Vanessa Echeverria, Mikaela Milesi, Jie Fan, Linxuan Zhao, Riordan Alfredo, Xinyu Li and Dragan Gašević. (2024). The Effects of Generative AI Agents and Scaffolding on Enhancing Students' Comprehension of Visual Learning Analytics. https://arxiv.org/abs/2409.11645"
    author: Lixiang Yan, Roberto Martinez-Maldonado, Yueqiao Jin, Vanessa Echeverria, Mikaela Milesi, Jie Fan, Linxuan Zhao, Riordan Alfredo, Xinyu Li and Dragan Gašević
---

# Five-component GenAI agent design combining multimodal LLMs, retrieval-augmented generation, and agentic scaffolding for VLA comprehension

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The article presents a system design in which passive and proactive generative AI agents support comprehension of visual learning analytics through five components: agent characteristics, prompt integration, knowledge database, response generation, and exemplar behaviours. The agents use multimodal GPT-4o, LangChain and Chroma for retrieval-augmented generation, and agentic system design to keep responses contextually accurate. The two interaction styles differ in initiative: "Proactive agents, however, offer scaffolding with guided questions and feedback", whereas passive agents wait for student-initiated queries and focus on explanation and clarity. The knowledge database is populated from learning design documents and peer-reviewed publications describing each visualisation, converted to vector embeddings for semantic search.

## Design Implications

### Context
#### Requirements
- A knowledge database of task-specific materials, descriptions, and detailed explanations of visualisation components drawn from learning design documents and publications
- Pre-defined scaffolding narratives with guiding questions crafted by educators and researchers for the proactive agent
#### Constraints
- The prototype was evaluated in a healthcare simulation learning setting with higher education students of healthcare, medical, or nursing backgrounds

### Target Learners
- higher education students

### Learning Goals
- comprehension of visual learning analytics
- data visualisation literacy

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Lixiang Yan, Roberto Martinez-Maldonado, Yueqiao Jin, Vanessa Echeverria, Mikaela Milesi, Jie Fan, Linxuan Zhao, Riordan Alfredo, Xinyu Li and Dragan Gašević. (2024). The Effects of Generative AI Agents and Scaffolding on Enhancing Students' Comprehension of Visual Learning Analytics. https://arxiv.org/abs/2409.11645
