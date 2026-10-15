---
type: design
id: rag-genai-chatbot-learning-task
title: RAG-based GenAI chatbot used as the AI-assisted learning support in the external validity study
description: "The external validity study used a GenAI chatbot built with a retrieval-augmented generation approach: learner prompts are embedded, cosine similarity retrieves relevant stored knowledge, and GPT-4o generates response..."
status: review
generated:
  by: "process:settle-candidates"
  at: 2026-10-12
sources:
  - id: yueqiao-jin-2024
    resource: "https://arxiv.org/abs/2411.00283"
    title: "Yueqiao Jin, Roberto Martinez-Maldonado, Dragan Gašević and Lixiang Yan. (2024). GLAT: The Generative AI Literacy Assessment Test. https://arxiv.org/abs/2411.00283"
    author: Yueqiao Jin, Roberto Martinez-Maldonado, Dragan Gašević and Lixiang Yan
---

# RAG-based GenAI chatbot used as the AI-assisted learning support in the external validity study

> **Design** · [All designs](index.md)
> **Evidence** · no claims cited

## Description
The external validity study used a GenAI chatbot built with a retrieval-augmented generation approach: learner prompts are embedded, cosine similarity retrieves relevant stored knowledge, and GPT-4o generates responses using the retrieved context, chat history, and the question. The article states this design was chosen "to improveresponserelevanceandreduceinaccuracies(hallucinations)" and represents openly accessible chatbots such as ChatGPT, Gemini, and Claude. Conversations are stored in the knowledge base for future context.

## Design Implications

### Context
#### Requirements
- Retrieval of relevant contextual information via vector embeddings and cosine similarity before response generation
#### Constraints
- The article presents it as a representation of openly accessible GenAI chatbots, not a novel system

### Target Learners
- higher education students with medical, healthcare, and nursing backgrounds

### Learning Goals
- comprehending complex visual analytics of teamwork in healthcare simulations

### Claims
- 

## Related Designs
- 

## Examples
-

## Key Sources
- Yueqiao Jin, Roberto Martinez-Maldonado, Dragan Gašević and Lixiang Yan. (2024). GLAT: The Generative AI Literacy Assessment Test. https://arxiv.org/abs/2411.00283
